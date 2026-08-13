# Can the native-mode strip assignment be changed by patching the firmware?

Date: 2026-08-10
Scope: `motion32_fw_payload_0x1000.bin` (image base 0), `motionupgrade.bin` header.
Method: Capstone Thumb disassembly of the payload, plus structural analysis of the update image.
No Ghidra — every address below was recovered by exhaustive 2-byte-aligned decode of the raw image
and can be re-derived without a project database.

**Verdict: no, not on the evidence available. Do not attempt it.** The reasoning is below, and the
last section gives a safer avenue that is worth probing before the idea is abandoned entirely.

---

## 1. What was confirmed

### The mode byte is a product variant, decided at boot — not native mode

`FUN_00000e5c` is the init routine:

```
00000e5c  push  {r4, lr}
00000e62  movw  r0, #0x5cbc        ; handle -> 0x20005cbc
00000e68  movw  r1, #0x204         ; parameter index 0x204
00000e72  bl    #0x4df4            ; read from persistent parameter store
00000e76  movw  r3, #0x4291
00000e82  strb  r2, [r3]           ; DAT_20004291 = stored value
00000e84  bl    #0x2a14            ; USB endpoint init
00000eb0  bl    #0x16f4            ; <-- mode setup (counts)
00000eb4  bl    #0x17d4
00000eb8  b     #0xeb4             ; main loop
```

The mode byte is read **once, at boot, from persistent storage**, and applied before the USB link is
even usable. Nothing in the native-mode handshake re-runs this. `FUN_00000e50` is merely its getter.

That it is the **Motion 32 / Motion 16 product selector** is confirmed three ways: it picks between
the SysEx prefixes `F0 08 26 05` and `F0 08 24 05` at `0x95f4` (`0x26`/`0x24` being the two product
ids), and the update image header names *both* products — `Motion 16` at `0x40`, `Motion 32` at
`0x50` — in a single image.

This corroborates the existing conclusion in `Motion32_Implementation_Notes.md` §6b-33.

### The control counts are immediate operands, not a table

`FUN_000016f4`:

```
000016f6  bl    #0xe50             ; r0 = mode
000016fc  bne   #0x1796
000016fe  movs  r3, #8             ; mode 0: 8 relative controls
00001700  movs  r2, #2             ; mode 0: 2 ABSOLUTE controls
0000170a  strb  r3, [r7]           ; -> DAT_200045cc (relative count)
00001728  strb  r2, [r3]           ; -> DAT_200045ca (absolute count)
...
00001796  movs  r3, #9             ; mode 1: 9 relative controls
00001798  movs  r2, #1             ; mode 1: 1 ABSOLUTE control
```

Two absolute 14-bit controls on the Motion 32, one on the Motion 16. Those are the touch strips, and
the count is baked into the instruction stream at `0x1700` / `0x1798`.

### There *is* a genuine table — but for the wrong controls

`0x9664` holds two 9-byte relative control-id orders, read from nine sites in `0x14fc`–`0x15fc`:

```
mode 0:  00 03 05 07 01 02 04 06 08
mode 1:  02 08 06 05 01 00 07 04 03
```

This is real, table-driven, and patchable. It governs the **encoders**, not the strips.

### The absolute controls take their id from the loop counter

`FUN_00001288` iterates `r5` from `0` to `DAT_200045ca - 1` and passes `r5` directly as the control
id to the 14-bit encoder at `0xeec`. There is no table for the strips — the id *is* the index.

`FUN_00000eec` (verified by disassembly, not by prior summary) emits:

```
selector = (control_id - 0x50) & 0xff        -> 0xB0, 0xB1 for ids 0, 1
then      0x16, high7
then      0x36, low7
```

Read as MIDI that is a 14-bit CC pair — CC 22 MSB / CC 54 LSB — on channels 1 and 2.

---

## 2. The problem: this is not the path that emits pitch bend

`Motion32_Pads_Banking_and_Strips.md` §5.2, backed by the 2026-07-27 hardware capture, records that
in native mode the strips send **pitch bend**, strip 1 on channel 0 and strip 2 on channel 1, with
touch as CC `0x7A`/`0x7B`.

The emitter traced above sends `B0/B1 16 hi 36 lo` — CC, not pitch bend. The two do not reconcile.
Either the scanned-control path is the standalone/legacy protocol and native mode uses a separate
emitter, or a later stage rewrites these events. **Either way, the code that assigns the strips to
pitch bend in native mode has not been located.**

This is consistent with the open gap in `NativeMode_USB_EventStream_Report.md`, which states plainly
that the `8F 00 7F` parser "was not found in this path". Two independent efforts have now failed to
find the native-entry handler. It is the missing link, and without it there is nothing to patch.

---

## 3. The update image

| Offset | Value | Reading |
|---|---|---|
| `0x00` | `0x2571` | unknown — **not** CRC16 (CCITT/XMODEM/MODBUS/ARC/MAXIM/USB) or CRC32 of payload, whole file, or header-with-word0-zeroed |
| `0x04` | `0x1000` | payload offset — verified, `upgrade[0x1000:] == payload` exactly |
| `0x08` | `0xffff` | — |
| `0x0c` | `0x55aa` | magic |
| `0x10`–`0xa0` | strings | author, `Fender`, `Motion 16`, `Motion 32`, `01.06`, `1.0.6`, `1.0.0`, build `20260630-182229` |
| `0xc0` | `0x9f00` | unknown |
| `0xd0`–`0xfff` | all `0xff` | **no signature block** |

The absence of a signature blob is mildly encouraging. It is **not** sufficient. Verification is done
by the bootloader, which lives on the device and is not present in this image — so we cannot see what
it checks, and `0x2571` is an unidentified integrity value that would have to be recomputed correctly
for any modified image to be accepted.

---

## 4. Why this should not be attempted

1. **The target has not been found.** The native-mode strip assignment is not located. Everything
   identified so far is the Motion 32/16 product-variant machinery, which runs at boot and is not
   what makes the strips pitch benders under `8F 00 7F`.
2. **The integrity scheme is unsolved.** `0x2571` matches no standard checksum tried. A modified
   image would be rejected — or worse, accepted and unbootable.
3. **The bootloader is unknowable from here.** It is the component that validates, and it is not in
   this file.
4. **The risk is asymmetric to the point of absurdity.** The upside is removing one script-side
   workaround. The downside is a bricked controller with no documented recovery path. Firmware
   modification is also very likely to void warranty and support.

---

## 5. The avenue actually worth probing

`FUN_000016f4` does something more interesting than the counts:

```
0000171c  movw  r5, #0x95fc        ; setup-pair table
00001734  ldrh  r1, [r5]           ; parameter index
0000173a  bl    #0x4df4            ; read from the SAME persistent store as the mode byte
00001746  adds  r5, #4             ; 4-byte entries
0000174a  cmp   r6, r3             ; loop rel_count times
```

Per-control configuration is read from a **persistent parameter store** at handle `0x20005cbc`,
indexed by halfwords in the table at `0x95fc` (`0x0206, 0x0407, 0x040b, 0x0400, 0x0208, 0x090e,
0x0409, 0x0402, 0x0304 …`). The mode byte itself is index `0x204` in that same store.

If any part of the strip configuration lives in that store, it could be changed **without reflashing
anything** — provided something can write it. The device already accepts Fender SysEx, and the
Global Settings screen must persist its choices somewhere.

That is a far better question than firmware patching, and it is cheap and safe to investigate:

1. Find the writer counterpart to `FUN_00004df4` (a `FUN_00004e??`-range store/commit routine).
2. Find its callers, and whether any is reachable from the SysEx command dispatcher.
3. Compare the store indices against the documented Global Settings items.

Even if it fails, it fails harmlessly. **Recommendation: close the firmware-patching idea, keep the
parameter store as an open question, and fix strip 2 in the script.**
