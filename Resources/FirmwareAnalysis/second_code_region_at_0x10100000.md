# The firmware has a second code region that has never been disassembled

Date: 2026-08-10
Program: `motion32_fw_payload_0x1000.bin`
Method: Capstone Thumb decode + pointer-table analysis. Reproducible without a Ghidra project.

**Headline: file offset `0x20000` maps to runtime address `0x10100000`.** Roughly 600 KB of the
image — everything above `0x20000` — has been imported at the wrong base since the beginning, which
is why it looks like data and why `1049` functions covering only `143,490` of `757,924` bytes (19%)
seemed plausible.

**This is why two separate efforts failed to find the `8F 00 7F` handler.** It was never missing;
it was never disassembled.

---

## 1. The base-0 region cannot receive the handshake

This is now closed, not merely unproven. Three facts, each verified by disassembly:

**The USB receive callback feeds exactly one queue.** `FUN_00002ac4`, the callback embedded at
`+0x14` of descriptor `0x9874`, handles only event type `2` (send-ready) and type `4`, and type 4
does `ldrb r1, [r0, #8]` → `FUN_00000d6c(0x200040a0, byte)`. Every inbound byte goes to that one ring.

**The only consumer of that ring parses SysEx and nothing else.** `FUN_000010a4` is a three-state
machine: state 0 discards every byte that is not `0xF0`; state 1 matches the Fender prefix from
`0x95f4`/`0x95f8`; state 2 accumulates until `0xF7` and dispatches through the function pointer at
`DAT_20004298`. At `0x115c` a `lsls r3, r0, #0x18` / `bmi` pair aborts on any byte with bit 7 set.
`8F 00 7F` is dropped in state 0.

There are exactly **three** references to `0x200040a0` in the whole base-0 region (`0x2a18`,
`0x2ab8`, `0x2ad4`) and exactly **one** caller of `FUN_000010a4` (`0x11fa`). Nothing else drains it.

**The second endpoint is never configured.** `FUN_00002a14` selects descriptor `0x97e4` /
context `0x20005cd4` when called with `1`, and `0x9874` / `0x20005d24` otherwise. It has exactly one
caller — `0x00000e84`, in the boot routine, immediately preceded by `movs r0, #9`. Descriptor
`0x97e4`'s callback slot at `+0x14` is `00 00 00 00`.

So within the base-0 image the story is complete and self-consistent: SysEx in, nothing else.

---

## 2. Locating the second region

The last 17 words of the image are a table of odd (Thumb) pointers:

```
000b9060: 0x1013a27d 0x1013a409 0x1013aedd 0x1013aaa9 0x1013ad11 …
000b90a0: 0x101001b1
```

Base-0 code never builds such an address — a scan for `movt` with `#0x1010`/`#0x1013`/`#0x1014`
returns **zero** sites. Meanwhile `0x10xxxxxx` words sit at 3–4% density throughout file
`0x20000`–`0x8ffff`, which is what a code region's own literal pools look like from the outside.

Solving for the mapping: for each candidate delta, count how many of 284 sampled pointers land on a
function prologue (`push` or `sub sp`).

| delta | file offset of `0x10100000` | prologue hits |
|---|---|---|
| **`0x100e0000`** | **`0x20000`** | **156 / 284** |
| `0x100c9fb0` | `0x36050` | 58 |
| `0x100dfffc` | `0x20004` | 54 |

The winner is nearly triple the runner-up and is a round number.

### Verification

```
runtime 0x1013ad10  (file 0x05ad10)
  1013ad12  push     {r4, lr}
  1013ad18  bl       #0x1013a180        <- in-region
  1013ad32  bl       #0x1013aef8        <- in-region

runtime 0x101001b0  (file 0x0201b0)
  101001b2  push     {r4, lr}
  101001c0  bl       #0x10100188        <- in-region
  101001c4  pop      {r4, pc}           <- matches the push
```

Coherent bodies, matched prologue/epilogue, and every call target inside the region. The mapping is
correct.

---

## 3. How to import it

In Ghidra, keep the existing base-0 program and add a second block over the same file bytes:

- **Window → Memory Map → Add Block**
- Name: `app`, Start: `0x10100000`, Length: `0x990a4`
- Source: **File Bytes**, file offset `0x20000`
- Flags: Read + Execute (not Write)

Then **Analysis → Auto Analyze** restricted to the new block. Expect the function count to rise
sharply from 1049.

The base-0 block still covers those file bytes, so the region is mapped twice. That is harmless for
analysis; if it bothers you, shrink the base-0 block to `0x0`–`0x1ffff` first, which is where all
1049 currently-known functions live anyway.

---

## 4. What this means for the open questions

**The `8F 00 7F` handler is almost certainly in the new region**, along with whatever retargets the
controls, opens the screen for host writes, and disconnects the onboard mode logic. Every one of
those behaviours is application logic, and the application is what has been invisible.

**The strip → pitch-bend assignment is very likely there too.** The base-0 emitter
(`FUN_00000eec`) produces `0xB0/0xB1` + CC `0x16`/`0x36` — a 14-bit CC pair — which contradicts the
2026-07-27 capture showing pitch bend on channels 0 and 1. Two emitters, and only one has been read.

**The relationship between the two regions is still open.** Base-0 code never calls into
`0x10100000`, so something else transfers control — a bootloader stage, a second core, or a copy
loop not yet found. One reading is that base-0 is an updater/loader (its SysEx-only parser and
`Fender`-prefixed protocol would suit that) and `0x10100000` is the real application. That does not
fully sit right, because base-0 also contains scanned-control setup and event encoding, which is
application work. **Do not treat this as settled.**

---

## 5. Consequence for the firmware-patching question

`strip_assignment_patchability.md` concluded "do not attempt it", partly on the grounds that the
target could not be found. That reason is now weaker — the target is probably findable. **The
verdict does not change**, because the other reasons stand untouched: the integrity word `0x2571`
is still unidentified, the bootloader that validates an update is still not in this image, and a
failed flash still bricks the device.

What has changed is that the *analysis* is worth continuing. Understanding what native mode actually
does to the device is valuable for the Remote Script whether or not a single byte is ever patched —
it is the difference between matching observed behaviour and knowing the contract.
