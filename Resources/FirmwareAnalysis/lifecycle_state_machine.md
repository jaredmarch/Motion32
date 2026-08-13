# The lifecycle state machine

Date: 2026-08-10
Derived from `motion32_app_region_0x10100000.bin` by Capstone; every address below was read from
the image rather than inferred from a decompiler summary.

Companion to `native_mode_lifecycle_resolved.md`, which establishes that `8F 00 7F` /`8F 00 00`
reach `FUN_101044b8` and call `FUN_1010048c(*0x2000aaa0, 3)` / `(…, 2)`.

---

## 1. First correction: 3 and 2 are *events*, not states

`FUN_1010048c` is a two-line wrapper:

```
1010048c  push {r4, lr}
1010048e  movs r2, #0            ; arg = 0
10100490  bl   #0x10100314       ; FUN_10100314(handle, event, arg)
10100494  movs r0, #0
```

`FUN_10100314` is a **generic table-driven FSM engine**, not a switch on native mode:

```
10100380  ldrh r1, [r4, #4]      ; width  (events per state)
10100384  muls r1, r2, r1        ; current_state * width
10100386  add  r1, r8            ; + event          <- the 2 or 3 lands here
1010038a  lsls r1, r1, #1
1010038c  ldrh r1, [r1, r6]      ; r6 = [r4+8] = transition table
10100390  strh r1, [r0]          ; -> next state
```

So `2` and `3` are **column indices into a transition table** — inputs, not destinations. Describing
them as "lifecycle state 3" is close enough to be useful but wrong in a way that matters if you ever
try to reason about what state the device is in.

### The FSM descriptor

| Offset | Meaning |
|---|---|
| `+0x00` | u16 — number of action rows |
| `+0x02` | u16 |
| `+0x04` | u16 — width (events per state) |
| `+0x08` | transition table `[state * width + event] -> next state` |
| `+0x0c`, `+0x10` | action tables |
| `+0x14` | exit-action table |
| `+0x18` | entry-action table |
| `+0x1c` | action dispatcher, called via `blx` |

A sentinel value (loaded PC-relative) means "no transition" / "no action".

⚠️ **The descriptor at `*0x2000aaa0` is in RAM and its tables are populated by an initialiser I have
not located.** So the *event* vocabulary below is solid, but the **state set itself is still
unknown** — we cannot yet say which state event 3 lands in, or how many states exist.

---

## 2. The event vocabulary

Ten call sites go through the wrapper (so `arg = 0`); fourteen post to the engine directly.

### Via `FUN_1010048c` — confirmed by disassembly at each site

| Event | Site | Trigger | Confidence |
|---|---|---|---|
| `0` | `0x10102394` | end of the native-setup body, after a range check on `[r2+0xc4]` in 3…6 | inferred: "setup complete" |
| `1` | `0x101005cc` | tiny unconditional poster | inferred: boot/start |
| **`2`** | `0x10104548` | **`8F 00 00`** — id `0x0f`, type 0, d1 0, **d2 == 0** | **confirmed** |
| `2` | `0x10104a82` | second exit path in the same handler family | confirmed site, purpose inferred |
| **`3`** | `0x101044e8` | **`8F 00 7F`** — id `0x0f`, type 0, d1 0, **d2 != 0** | **confirmed** |
| `4` | `0x1010472a` | message with `data2 == 1` | inferred |
| `5` | `0x10104710` | message with `data2 == 1`, also clears a byte flag | inferred |
| `6` | `0x10104a74` | message with `data2 == 0`, also clears a byte flag | inferred |
| `7` | `0x101008a4` | `FUN_1010edfc(...)` returned non-zero | inferred |
| `7` / `8` | `0x101004e0` | if mode ∈ {5,6}: flag `[0x1010052c]` == 1 → `7`, else `8` | inferred: a connected/disconnected pair |

### Posted directly to `FUN_10100314`

| Events | Sites | Neighbourhood |
|---|---|---|
| `9`, `10`, `11`, `12` | `0x1010244c`–`0x1010247c` | inside the native-setup region — sub-steps of bring-up |
| `13`, `14` | `0x1010314a`, `0x10103166` | `FUN_10103114`, driven by the poll |
| `22` ×3 | `0x10103054`, `0x10103070`, `0x10103088` | `FUN_10103098` |
| `24` | `0x101030fe` | — |

---

## 3. The 10-tick delay before setup

`FUN_10103174` is the event-0 poll. The byte at **`0x2003cefe`** is a step counter:

```c
cVar1 = *(char *)0x2003cefe;
if (cVar1 == '\n') {            // 0x0A
    FUN_101022a0();             // <- the native setup body
    *pcVar2 = -1;               // 0xFF = idle
}
else if (cVar1 == -1) {         // idle: run the screensaver/idle timer instead
    if (FUN_1010dc30(1) != 6) { /* idle animation timing */ }
}
else {
    *(char *)0x2003cefe = cVar1 + 1;   // count up, one per poll tick
}
```

So the latch does not run setup. It starts a counter, and setup fires **ten poll ticks later**.

**This is the single most useful operational fact in this document.** Between `8F 00 7F` and the
device actually being configured there is a fixed, non-trivial delay, and `FUN_101022a0` is what
copies the routing tables, enables host port modes, starts the host tasks and emits the ack
`F0 08 26 05 41 F7`.

Anything the script sends in that window arrives at a device that has not yet been reconfigured.
**Waiting for the `41` ack rather than assuming readiness is the correct handshake discipline**, and
this is a plausible mechanism for intermittent startup problems.

Note also the `!= 6` test in the idle branch: while in mode 6 the idle timer is suppressed entirely.

---

## 4. The mode setting

`FUN_1010dc30(id)` is the app's settings getter; **id `1` is the operating mode**. It is called 163
times across the app. Values compared against, with sites:

| Mode | Compared at |
|---|---|
| `0` | `0x10101d56`, `0x10103fc4`, `0x1010426a` |
| `1` | `0x10103bc6`, `0x10104378` |
| `3` | `0x101004be`, `0x101028d4`, `0x10102a98`, `0x10102e9e`, `0x10103cae`, `0x101043f4`, `0x1010440c` |
| `4` | `0x10100662`, `0x10104250` |
| `5` | `0x10104518` |
| **`6`** | `0x1010066c`, `0x101031c6`, `0x1010453c` | 

**Mode 6 is native/host mode.** It is tested in the native-off path (`0x1010453c`, immediately
before posting event 2), in the poll's idle branch (`0x101031c6`), and at `0x1010066c`.

Modes 5 and 6 are treated as a pair in `FUN_101004b8` (`subs r0,#5; cmp r0,#1; bhi`), so mode 5 is
probably an adjacent host-ish mode rather than an unrelated one.

---

## 5. What is still open

1. **The transition table.** It is in RAM at `*0x2000aaa0` with flash-resident tables copied in by
   an initialiser not yet found. Until that is located, we have the input alphabet but not the state
   graph.
2. **Events 4, 5, 6 and 7/8.** The call sites are certain; the meanings are inferred from the
   surrounding comparisons only.
3. **Whether the counter start is observable.** Something writes `0x2003cefe` to begin the count —
   presumably an entry action of the state the FSM enters on event 3. Finding that write would
   confirm the whole chain end to end.
