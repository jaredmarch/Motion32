# Native mode: the lifecycle latch, resolved — and why there is no strip table to patch

Date: 2026-08-10
Status: **settled.** The question "what happens internally when the handshake arrives" is answered.
The question "can the strip assignment be patched in firmware" is answered **no**, for a better
reason than before: the assignment is not table-driven at all.

Supersedes the `0x72` hypothesis in `app_midi_routing_engine.md` §3/§5.

---

## 1. The path

```
FUN_101069ec    USB-MIDI 4-byte packet unpacker (cable = top nibble, CIN drives length)
  -> FUN_1010671c   running-status byte assembler, per-port ctx stride 0x1f0
  -> FUN_101065f4   channel-message decoder; assigns source id from the inbound table
  -> FUN_10100264(5, event 0, decoded)
  -> FUN_10104558   event-0 callback
  -> jump-table index 5
  -> FUN_101044b8   lifecycle handler
```

## 2. The latch itself

`FUN_101044b8` decides it, and the test is exact:

```c
uVar3 = (uint)(byte)param_1[1];          // source id
if (uVar3 == 0x72) return 0;             // own-channel traffic: ignored
...
if (uVar3 != 0xf) return 3;              // must be id 0x0F
if (*param_1 != '\0') return 0;          // must be type 0 = Note Off
if (*(short *)(param_1 + 2) != 0) return 0;   // data1 must be 0
if (*(short *)(param_1 + 4) != 0) {
    FUN_1010048c(*DAT_10104550, 3);      // data2 non-zero -> lifecycle state 3 = NATIVE ON
    return 0;
}
FUN_1010048c(*DAT_10104550, 2);          // data2 zero      -> lifecycle state 2 = NATIVE OFF
```

So the message is not a Fender SysEx command at all. It is a plain Note Off on channel 16, which
the inbound table maps to source id `0x0f`, and which this handler recognises by shape.

**🔑 The velocity is tested for non-zero, not for `0x7F`.** `8F 00 01` enters native mode exactly as
`8F 00 7F` does. Only `8F 00 00` exits. The script sends `0x7F` because Studio Pro does; nothing in
the firmware requires it.

⚠️ **Note the earlier mistake, because it is instructive.** The `0x72` branch is real —
`FUN_101065f4` assigns it when the incoming channel equals the port's *own* channel — but every
consumer found discards it. The handshake does not take that path; it takes the ordinary table
lookup and comes out as `0x0f`. Chasing `0x72` cost a full probe cycle.

## 3. What actually happens next

The latch only *requests* a state. Setup happens asynchronously: the event-0 poll `FUN_10103174`
watches `0x2003cefe`, and when that byte reaches `0x0A` it calls `FUN_101022a0` and resets it to
`0xFF`.

`FUN_101022a0` is the native setup body:

- copies flash `0x101469c4` -> RAM `0x20002088` (inbound assignment map)
- copies flash `0x101467c4` -> RAM `0x20001e88` (outbound routing map)
- enables host routing and port modes via `FUN_10102250`
- starts scheduled host-mode tasks via `FUN_101061c8`
- initialises the display-side host machinery
- emits a short ack, `F0 08 26 05 41 F7`

The real Fender SysEx parser is separate: `FUN_101045e4`, which handles identity request and the
screen writes (`F0 08 26 20…`, `F0 08 26 21…`).

## 4. The native tables, decoded

Both copied tables were dumped from the image. **They contain no message-type information of any
kind** — which is the whole answer.

### Inbound assignment `0x101469c4` → `0x20002088`

`(channel * 4 + port) * 2` → source id. 16 channels × 4 ports × 2 bytes.

| channel | port 0 | port 1 | port 2 | port 3 |
|---|---|---|---|---|
| 0–3 | `00`–`03` | `00`–`03` | `20`–`23` | `30`–`33` |
| 4–14 | `7f` (unassigned) | `7f` | `24`–`2e` | `34`–`3e` |
| **15** | **`0f`** | **`0f`** | `2f` | `3f` |

Channel 15 on ports 0 and 1 is the `0x0f` that carries the handshake. Channels 4–14 being `7f` on
those ports means ordinary traffic there is dropped outright.

### Outbound routing `0x101467c4` → `0x20001e88`

`(source * 4 + dest) * 2` → output channel, `0xff` = unrouted.

```
src 0x00-0x0f -> dest 0, channel = src        (identity)
src 0x10-0x1f -> dest 1, channel = src & 0x0f
src 0x20-0x2f -> dest 2, ...
src 0x30-0x3f -> dest 3, ...
```

Pure channel-to-channel plumbing, block-diagonal by port.

## 5. Why there is no "touch strip = pitch bend" table

The other agent looked for `E0`/`E1` in the copied tables and found none. **That is correct and it
is structural, not a gap in the search.**

The message type never appears in these tables. It travels in the event struct at `0x20001e80` as a
small integer — `0`–`6`, where `6` is pitch bend — and is only turned back into a status byte at
the very end, by `FUN_10106508`:

```c
if (*param_2 < 7) bVar4 = *param_2 * '\x10' + 0x80;    // 6 -> 0xE0
```

The tables decide **which channel** a source lands on and **whether** it is forwarded. What kind of
message it is comes from the code that generates the event — the physical control's own handler.

So the strips are pitch benders because the strip scanning code emits type `6`, not because any
table says so. There is no byte to flip.

## 6. Verdict

**Firmware patching is closed as an avenue**, now for a solid reason rather than an absence of
evidence:

1. There is no assignment table for message type. The type is produced in code.
2. Changing it would mean patching the strip handler's emitted type — a code edit, not a data edit,
   with no obvious single site.
3. The integrity word `0x2571` in the update header is still unidentified, and the validating
   bootloader is still not in this image.

**The script-side adaptation is the right path**, and it is now an informed choice rather than a
concession. Two concrete gains for the Remote Script from this work:

- The handshake accepts any non-zero velocity; only `00` exits. Useful for robustness.
- Native setup is asynchronous — the latch requests a state, and `FUN_101022a0` runs later off a
  poll. Anything the script sends immediately after `8F 00 7F` may arrive before setup completes.
  That is a plausible explanation for handshake-timing flakiness and worth testing on hardware.
