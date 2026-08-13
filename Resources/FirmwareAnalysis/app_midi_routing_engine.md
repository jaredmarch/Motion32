# The application's MIDI routing engine — and where native mode actually lives

Date: 2026-08-10
Source: `motion32_app_handler_dump.md` (Ghidra, second code region) + literal-pool resolution
against `motion32_fw_payload_0x1000.bin` at delta `0x100e0000`.

**The headline: the control assignment is not in the firmware. It is a RAM table, written at
runtime by a cluster of setter functions.** Changing what the strips send is therefore a
*configuration* problem, not a firmware-patching problem.

---

## 1. The structures

Every pointer below was resolved by reading the literal pool out of the image, not inferred.

| Literal | Value | What it is |
|---|---|---|
| `DAT_10106718` | `0x20002088` | **Inbound assignment table** — `[channel][port] -> source id` |
| `DAT_10106548` | `0x20001e88` | **Outbound routing table** — `[source][dest] -> output channel` |
| `DAT_10106714` / `DAT_101069e4` | `0x20003f78` | Per-port parser context, stride `0x1f0` |
| `DAT_10106500` | `0x2000a9b0` | Per-port output context, stride `0x32` |
| `DAT_10106710` | `0x20001e80` | The 6-byte event-5 message struct |
| `DAT_101069e8` | `0x10148d54` | `0xF0` system dispatch table (in flash) |

**All of the tables are in RAM.** `FUN_10106328`, the event-5 init, memsets the inbound table to
`0x7f` and the outbound table to `0xff` — both meaning "unassigned". Nothing about the assignment
is a firmware constant.

### Per-port context layout (stride `0x1f0`)

Recovered from `FUN_1010671c` and `FUN_101065f4`:

| Offset | Meaning |
|---|---|
| `+0x000` | port enabled (0 = ignore everything) |
| `+0x001` | port type — compared against `0x10` / `0x11`, else USB |
| `+0x002` | **the port's own channel** |
| `+0x004` | SysEx accumulated length (cap `0x100`) |
| `+0x006` | SysEx buffer |
| `+0x106` | running status |
| `+0x107` | first data byte |
| `+0x108` | parser state (1 = one-byte msg, 2 = awaiting d1, 3 = awaiting d2, 4 = in SysEx) |
| `+0x109`…`+0x10c` | four destination enables |

### The message struct at `0x20001e80`

`[0]` type (0–6), `[1]` source id, `[2..3]` data1, `[4..5]` data2.

Type is the status nibble folded down: `0x80→0`, `0x90→1`, `0xA0→2`, `0xB0→3`, `0xC0→4`,
`0xD0→5`, **`0xE0→6`**. `FUN_10106508` reverses it exactly — `type * 0x10 + 0x80`.

---

## 2. How a byte becomes a routed message

`FUN_1010671c(port, byte)` is a textbook running-status parser. `FUN_101065f4(port, status,
d1, d2)` is the channel-voice handler, and this is the part that matters:

```c
bVar1 = *(byte *)(ctx + port * 0x1f0 + 2);        // the port's OWN channel
if ((uint)bVar1 == (status & 0xf)) {
    msg[1] = 'r';                                  // 0x72 — a fixed internal id
    FUN_10100264(5, 0);                            // post event 5
} else {
    cVar2 = *(char *)(0x20002088 + ((status & 0xf) * 4 + port) * 2);   // assignment lookup
    msg[1] = cVar2;
    if (cVar2 != '\x7f') FUN_10100264(5, 0);       // 0x7f = unassigned, drop
}
```

Two distinct paths:

- **On the port's own channel** → tagged with the fixed id `0x72` and posted.
- **On any other channel** → the id comes from the RAM assignment table; `0x7f` means drop.

Then `FUN_10106508`, the event-5 callback, routes outward — **but only for `id < 0x40`**:

```c
if (*param_2 < 7) bVar4 = *param_2 * '\x10' + 0x80;      // type -> status nibble
...
if ((param_2[1] < 0x40) &&
    (bVar1 = *(byte *)(route + ((uint)param_2[1] * 4 + dest) * 2), bVar1 != 0xff)) {
    FUN_1010646c(dest, bVar1 | bVar4, param_2[2], param_2[4], param_4);
}
```

So the id space splits: **`0x00`–`0x3f` are routable MIDI sources; `0x40`–`0x7f` are internal
and are never forwarded to an output.** `0x72` is in the internal half.

`FUN_1010646c` finishes the job by building the 4-byte USB-MIDI packet — `(cable << 4) | CIN`,
status, d1, d2 — which is the first time in this whole project that USB-MIDI packet framing has
actually been seen.

---

## 3. What this says about `8F 00 7F`

> ⚠️ **Section 3 as originally written was wrong, and section 5 of this file overstates the case.**
> I proposed that internal id `0x72` was the native-mode trigger. It is not. The handshake carries
> id **`0x0f`**, taken from the inbound assignment table, and is handled by `FUN_101044b8`. The
> `0x72` path exists but is discarded by every consumer found. See
> `native_mode_lifecycle_resolved.md` for the settled account. The structural description of the
> routing engine below is accurate and still worth reading; only the `0x72` conclusion is retracted.

`8F` is Note Off on channel `0x0F`. Follow it through:

1. `FUN_1010671c` sees `0x8F`, matches `(byte & 0xffffffe0) == 0x80`, stores running status and
   moves to state 2.
2. `00` → state 3. `7F` → dispatch `FUN_101065f4(port, 0x8F, 0x00, 0x7F)`.
3. Status nibble `0x80` → message type `0`.
4. **If the port's own channel (`ctx+2`) is `0x0F`, the message is tagged `0x72` and posted as
   event 5 — and because `0x72 >= 0x40`, it is deliberately not forwarded anywhere.**

That is exactly the shape of a control/handshake channel: a reserved channel whose traffic is
consumed internally rather than routed. It explains why the handshake never appears on any output
and why it is a Note Off rather than SysEx — it costs three bytes and rides the ordinary parser.

**This is a strong hypothesis, not yet proof.** What is proven: the path exists, the tagging is
real, and internal ids are not forwarded. What is *not* yet shown: the consumer that acts on id
`0x72` and performs the mode switch. That consumer is the last missing piece.

---

## 4. The configuration setters

A cluster of small functions around `0x10106ae0`–`0x10106b80` writes all of this at runtime:

| Address | Writes |
|---|---|
| `~0x10106ae0` | `ctx[port] + 1` — port type |
| `~0x10106b00` | out-ctx `+1` — output port type |
| `~0x10106b1c` | `ctx[port] + 0` — port enable |
| `~0x10106b38` | out-ctx `+0` — output enable |
| `~0x10106b50` | **the inbound assignment table** |

The last one is the important one:

```
10106b5c  ldr  r1, [pc, #0x1c]     ; -> 0x20002088
10106b64  strh r2, [r1, r3]
10106b66  adds r3, #8
10106b68  cmp  r3, #0x80           ; 16 channels x 8 bytes
```

Striding by 8 to `0x80` confirms the geometry: **16 channels × 4 ports × 2 bytes = 128 bytes**,
addressed as `(channel * 4 + port) * 2` — exactly what `FUN_101065f4` reads.

---

## 5. What this changes

`strip_assignment_patchability.md` concluded "do not patch the firmware". That conclusion stands,
but the *reasoning* is now much better than "we can't find the target":

**The assignment is not in the firmware to patch.** It is a 128-byte RAM table plus per-port
context bytes, all written by setter functions at runtime. Modifying the flash image would only
change whatever code calls those setters — and if a host-reachable path to them exists, no
modification is needed at all.

The question is therefore no longer "can we patch the firmware" but **"can a host reach the
setters?"** — and there is now a concrete place to look: the `0xF0` handler at `0x10106928`, which
is the application's own SysEx entry point, distinct from the base-0 updater parser.

---

## 6. Next targets, in order

1. **`FUN_10100264`** — the event post function. Then find *every* consumer of event 5, not just
   `FUN_10106508`. One of them handles ids `>= 0x40`, and that one performs the mode switch.
2. **Id `0x72`** — search for the constant `0x72` compared or indexed in the app region.
3. **`0x10106928`** — the app's `0xF0` SysEx handler, and whether it reaches the setter cluster.
4. **Callers of the setter at `~0x10106b50`** — whoever populates the assignment table is, by
   definition, what native mode changes.
5. The flash event table at `0x101964f0` lists events `6, 5, 2, 3, 0, 17` with init/callback
   pairs. Event `0` (`init 0x10102119`, `callback 0x10104559`) is the largest unexplored one.
