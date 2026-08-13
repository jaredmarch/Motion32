# The strip translation chain — from capacitive sensor to pitch bend

Date: 2026-08-10
Method: Capstone against `motion32_app_region_0x10100000.bin`.

Prompted by the observation that **a capacitive touch event and a finger slide are different
events**, so a single "strip handler" could not be the whole story. That was correct, and following
it produced the complete chain.

---

## 1. Two firmwares, one file

The image contains two independent code regions with no cross-references:

- **base 0** — the control-scan side. Emits an internal event stream with opcodes
  `0x14` (7-bit absolute), `0x15` (relative delta), `0x16`/`0x36` (14-bit MSB/LSB pair).
- **base `0x10100000`** — the application. Consumes that stream.

`FUN_1010320c` is the bridge, and it is where the translation everyone was looking for happens.

## 2. `FUN_1010320c` — the translator

```
1010320e  ldrb r3, [r0, #1]     ; source id
10103210  cmp  r3, #0x2f
10103212  bls  #0x10103286      ; ids <= 0x2f ignored
10103214  movs r2, #0x70
10103218  strb r2, [r4, #1]     ; output id = 0x70
1010321a  ldrh r3, [r0, #2]     ; OPCODE
1010321c  cmp  r3, #0x16  -> 0x101032ac   ; 14-bit MSB   (position)
10103222  cmp  r3, #0x14  -> 0x1010328a   ; contact      (TOUCH)
10103226  cmp  r3, #0x15  -> encoder delta
10103250  cmp  r3, #0x36  -> 0x101032c2   ; 14-bit LSB   (position)
```

**Touch and position are genuinely different opcodes** — `0x14` versus the `0x16`/`0x36` pair —
exactly as predicted from the capacitive hardware.

The 14-bit reassembly is explicit. `0x16` stashes `value << 7`; `0x36` masks the low seven bits and
ORs them in:

```
101032c4  ldrh r3, [r0, #4]     ; LSB
101032c8  ands r3, r1           ; & 0x7f
101032ca  ldrh r5, [r0]         ; stashed MSB
101032cc  orrs r3, r5           ; 14-bit position
101032d0  movs r0, #6           ; internal code, for control id 0x30
```

Two accumulator slots, `[r0]` and `[r0+2]`, and a branch on control id:

| control id | internal code |
|---|---|
| `0x30` (strip 1) | `6` |
| `0x31` (strip 2) | `2` |

## 3. `FUN_10103114` — where the codes resolve

⚠️ **The codes `6` and `2` are not MIDI message types.** The same field also carries `0x2c` and
`0x48`, which are outside the 0–6 type enum. They are internal message codes:

```c
if (msg[1] != 0x70) return 0;
switch (msg[0]) {
  case 0x2c: FUN_10103018();                  break;  // from opcode 0x14 — buttons/contact
  case 0x48: FUN_10103098();                  break;  // from opcode 0x15 — encoders
  case 6:    FUN_10100314(*0x2000aaa0, 13, packed); break;  // strip 0x30
  case 2:    FUN_10100314(*0x2000aaa0, 14, packed); break;  // strip 0x31
}
```

**`0x2000aaa0` is the same FSM handle that `8F 00 7F` posts event 3 to.** Everything converges on
one state machine:

| input | FSM event |
|---|---|
| `8F 00 00` — native off | `2` |
| `8F 00 7F` — native on | `3` |
| strip 1 position | **`13`** |
| strip 2 position | **`14`** |
| encoders | from a table, or `22`/`23`/`24` |

The 14-bit position rides along as the event *argument*, packed into a 32-bit word.

## 4. So where does pitch bend come from?

**It is an FSM action bound to a state, not a table lookup.**

The physical gesture always produces event 13 or 14. What comes out depends on which state the FSM
is in, and `8F 00 7F` changes that state. Same event in, different MIDI out — which is precisely why
no "strip = pitch bend" table was ever going to be found.

The actions live in the FSM descriptor's tables (`+0x0c`, `+0x10`, `+0x14`, `+0x18`) and are run
through the dispatcher at `+0x1c`. See `lifecycle_state_machine.md` §1.

## 5. A genuine assignment table does exist — for the encoders

`FUN_10103098` looks up an encoder's FSM event from a flash table installed at boot:
`table[id * 12 + 0x0a]`. The installer at `0x10102120`–`0x101021f0` picks between two table sets by
product, using `0x26` (Motion 32) and `0x24` (Motion 16) — the familiar SysEx product bytes.

For the Motion 32 the table is at **`0x10146758`**, 12-byte rows, and it is readable:

| id | status | CC a | CC b | … | FSM event |
|---|---|---|---|---|---|
| 0 | `b0` | `0x10` | `0x46` | … | `0x0f` |
| 1 | `b0` | `0x11` | `0x47` | … | `0x10` |
| 2 | `b0` | `0x12` | `0x4a` | … | `0x11` |
| 3 | `b0` | `0x13` | `0x4c` | … | `0x12` |
| 4 | `b0` | `0x50` | `0x49` | … | `0x13` |
| 5 | `b0` | `0x51` | `0x4b` | … | `0x14` |
| 6 | `b0` | `0x52` | `0x48` | … | `0x15` |
| 7 | `b0` | `0x53` | `0x4f` | … | `0x16` |
| 8 | `b0` | `0xff` | `0xff` | … | `0x17` |

Status `0xB0` and two alternate CC sets per encoder.

⚠️ **This partially contradicts the README's claim that "CC numbers are immediate operands in the
instruction stream".** That was true of the base-0 scan region, which is where the earlier analysis
looked. In the application region the encoder CC numbers are **table-driven and in flash**. The
README should be corrected.

The strips are not in this table — they bypass it, going straight to FSM events 13/14.

## 6. Verdict, unchanged but now fully grounded

There is no strip-to-pitch-bend table because the mapping is not data. It is an action attached to a
state in a state machine whose state native mode changes. Patching the firmware would mean editing
FSM action tables — and those are installed into RAM at boot from flash sets chosen by product.

**Remaining unknown:** the FSM action tables themselves. The variant installer writes
`*0x2000aaa0 = 0x200097cc`, which is RAM, so the descriptor is built at runtime from flash sources
not yet identified. Anyone wanting to finish this should start there.
