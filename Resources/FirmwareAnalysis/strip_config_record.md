# The touch-strip configuration record — found, and why native mode ignores it

Date: 2026-08-10
Method: Capstone against `motion32_app_region_0x10100000.bin`. The Ghidra probe that went looking
for these tables failed with `MemoryAccessException: Unable to read bytes at ram:10146b98` — the app
block was not mapped in that read-only project — so everything below was read from the raw image.

**There is a per-strip configuration record, and one of its fields selects the MIDI message type.
In native mode the firmware does not consult it.**

---

## 1. The record

From `Motion32StripControlProbe`'s recovered layouts:

```
FUN_1010ddf0(bank, strip, field)          read    strip <= 1
FUN_1010de1c(bank, strip, field, value)   set     clamped by table @ 0x10146b98
FUN_1010dd0c(bank, strip, field, delta)   nudge   clamped by table @ 0x10146c38

address = *0x2000aa90 + bank * 0x34 + strip * 0x1a + field + 0xeff
```

`0x34 = 2 * 0x1a`, so a bank holds exactly **two strips** of 26 bytes each. That matches the hardware.

## 2. The range tables

Both are 10 rows of 16 bytes — `min` u32, `max` u32, u16, `wrap` u16, `step` u32.

| field | min | max | meaning |
|---|---|---|---|
| 0 | 2 | 11 | — |
| **1** | **1** | **8** | **message type selector** (see §3) |
| **2** | **0** | **15** | **MIDI channel** |
| 3 | 1 (64 in the delta table) | 127 | — |
| 4 | 0 | 127 | — |
| 5 | 127 | 127 | pinned |
| 6 | 2 | 2 | pinned |
| 7 | 0 | 3 | 4-way — there are 4 ports |
| 8 | 0 | 127 | **the live value**; no wrap |
| 9 | 64 | 127 | — |

**Field 8 is the only field ever written at runtime** — all four `FUN_1010de1c` sites and all three
`FUN_1010dd0c` sites use field 8. Fields 0–7 are configuration, read but not written by the MIDI
path.

## 3. Field 1 selects the message type

In `FUN_10102e84` at `0x10102fa4`:

```
10102fa4  movs r2, #1            ; field 1
10102faa  bl   #0x1010ddf0
10102fae  cmp  r0, #7
10102fb0  beq  #0x10102fdc       ; -> movs r3,#6   type 6 = PITCH BEND
10102fb2  cmp  r0, #8
10102fb4  beq  #0x10102fea       ; -> movs r3,#5   type 5 = channel pressure
10102fb6  cmp  r0, #1
10102fb8  bne  #0x10102f2a       ; unhandled -> return
10102fba  movs r3, #3            ;    type 3 = CC
10102fbc  strb r3, [r4]          ; msg[0] = type
```

The 1…8 range matches the min/max table exactly. Types written are the same enum used everywhere
else in the routing engine (`3` = CC, `5` = channel pressure, `6` = pitch bend), which
`FUN_10106508` later turns back into a status byte with `type * 0x10 + 0x80`.

**So in principle a strip's message type is a setting, not a constant.**

## 4. …but the mode gates it, and native mode takes a different path entirely

The outer dispatch in `FUN_10102e84` is on `FUN_1010dc30(1)` — the operating mode:

```
10102e9e  bl   #0x1010dc30       ; mode = settings[1]
10102ea4  cmp  r0, #3
10102ea8  b    #0x10102fc0       ; mode 3 -> movs r3,#6   hardcoded PITCH BEND
10102eac  cmp  r0, #0
10102eae  beq  #0x10102f36       ; mode 0 -> read fields 2..7  CONFIGURABLE PATH
10102eb0  cmp  r0, #1
10102eb4  movs r3, #6            ; mode 1 -> hardcoded PITCH BEND
10102ed2  cmp  r0, #6
10102ed6  movs r7, #0x8f         ; mode 6 (NATIVE) -> build Fender SysEx
```

| mode | strip behaviour |
|---|---|
| 0 | **consults the config record** — fields 2–7, type from field 1 |
| 1 | type `6` (pitch bend), hardcoded |
| 3 | type `6` (pitch bend), hardcoded |
| **6 (native)** | **emits `F0 08 <id> 10 … F7`, twice — once with `r0=0`, once with `r0=2`** |

The mode-6 branch builds a 9-byte Fender SysEx (`strh` of `0x8f0` gives `F0 08`, then device id,
command `0x10`, port selector, strip index, two value bytes, `F7`) and sends it through
`FUN_1010654c` for two different ports.

**Only mode 0 reads the configuration record.** Modes 1, 3 and 6 bypass it completely.

## 5. What this settles, and what it does not

**Settles:** the original question — "modify the table of assigned controls in native mode" — has a
definite answer. A per-strip assignment record exists, with a message-type field and a channel
field, and it is **only honoured in mode 0**. Native mode does not read it. Changing those bytes,
by any means, would not alter native-mode behaviour.

**Does not settle:** this path emits SysEx in mode 6, yet the 2026-07-27 hardware capture shows
pitch bend on channels 0 and 1 in native mode. Those cannot both be the whole story. The likely
resolution is that `FUN_10102e84` handles one strip aspect (touch/secondary, or the `0x10` command
being a strip *report*) while raw position is emitted elsewhere. That second emitter is the one
remaining unknown, and it is the last thing worth chasing if anyone wants completeness.

**Practical consequence is unchanged:** the strips are pitch benders in native mode by code path,
not by a table entry, so there is nothing to edit. `ScriptForwarding` and the script-side handling
of strip 2 remain the fix.
