# Motion 32 — Gap Analysis for an Ableton Remote Script (Scenario 2: Host Integration)

**Scope decision:** we are building an Ableton MIDI Remote Script that **handshakes with the Motion 32
the way Fender Studio Pro does**, putting the device into its rich integrated control set — exactly the
model used for the Atom SQ predecessor. The plain "dumb MIDI controller" scene (Scenario 1) is out of
scope and intentionally ignored here.

Companion documents:
- `Motion32_Handshake_and_SysEx_Spec.md` — connection handshake, control map, LED/RGB, SysEx.
- `Motion32_Screen_Template_Map.md` (+ `.csv`) — every screen template/zone/element.
- `Motion32_Native_Host_Architecture.md` — the host-side state machine (14-layer state chart, supervisor, redraw model, event flow). **Read this before designing the script**; it resolves most of §3 below.

---

## 1. What is now fully specified (no gap)

- **Handshake / mode switch.** `8F 00 7F` to enter host mode, universal Identity Request/Reply for firmware, `8F 00 00` to leave, and the `F0 08 26 22` feedback-gating message. (Spec §1.)
- **Identity constants.** Fender mfr `0x08`; Motion 32 = `0x26`, Motion 16 = `0x24`; min firmware 1003; ships 1.0.6; RP2040 + LVGL.
- **Full control → MIDI map** for integrated mode: encoders (relative, CC 0x0E–0x15), encoder touch (0x70–0x77), all buttons, transport, nav, pads (notes 36–67 over two lanes), touch strips (pitch bend ch0/ch1). (Spec §2.)
- **Feedback protocol.** Button LED states (0/63/127), RGB as 3 component messages, pad LED state/blink/pulse, touch-strip LED addresses. (Spec §3.)
- **Screen protocol.** Template-select + element-update SysEx, all 5 attribute types, and the full screen map — **433 attribute handlers across 181 unique elements** — for all 4 templates. (Spec §4 + screen map.)

That is enough to begin writing the script. The remaining gaps are about *behavior the static files
don't pin down* and *the host-side logic Studio One implements that Ableton will have to re-implement.*

> **Confidence tagging.** Claims across these docs mix three levels — **[SRC]** specified by Studio One source/XML, **[CAP]** observed in MIDI captures, **[INF]** inferred from firmware/behavior. The companion spec now tags them inline; treat only [SRC]/[CAP] items as authoritative.

---

## 1b. Closed by hardware capture (2026-07-25)

Two Studio Pro MIDI captures — a project load and a Chord-button press — closed four items that had
been carried as unknowns since the start:

| Was open | Now |
|---|---|
| LED addressing and value model | **Verified.** Every LED write in the burst decoded against `midi.py` with no unknowns. Halos `0x0E`-`0x15` and wheel `0x1D` at state 127, RGB `(0, 52, 102)` = `#0069CC`. Key LEDs on notes **36-67** with state on `0x90` and RGB on `0x91`/`0x92`/`0x93`, exactly as the SysEx spec claimed |
| Transport resting colours | **Verified**, and they match what we chose: Play dim `(0,64,0)`, Record dim `(127,0,0)`, Stop full `(127,82,0)`, Shift dim magenta, Control full white |
| Does feedback need the handshake? | **No** — screen SysEx works pre-native, which is what masked the handshake bug |
| Scale/Chord host↔device path | **Host-drawn menus.** No on-wire mode command exists to find (item 12 below) |

One behavioural rule worth lifting out: **Studio Pro never writes state 0 to an encoder halo.** Not
once in the burst. On this device a dark halo is an exceptional state, not a resting one.

---

## 2. Real gaps — hardware-behavior unknowns (need a unit + MIDI monitor)

1. ~~**Does feedback require the handshake?**~~ **CLOSED (2026-07-25, hardware).** It does **not** — screen SysEx is accepted in the pre-native half-state, and that is precisely what masked the identity-handshake bug for so long (`Motion32_Implementation_Notes.md` §1). Working screen output is therefore *not* evidence that native mode was entered; check the transport CCs (`0x6F` native vs `0x66` pre-native) instead.
2. **Relative encoder acceleration.** Direction/format is **confirmed** (sign-bit at 0x40: `0x01`=+1, `0x41`=−1). What remains: larger deltas / acceleration under different **Encoder Curve** settings, and whether **Fine** changes the wire value or is device-side only.
3. **Button press/release values — CONFIRMED** `0x7F`/`0x00` on tested controls (Pads, Plugin, encoder touch, etc.). Only worth spot-checking unusual controls for toggle vs momentary.
4. ~~**Pad musical-note output**~~ — **CLOSED BY SOURCE (2026-07-25).** There is no firmware transform
   to capture. In native host mode the pads send **one fixed note per pad** — lane 0 = 36–51, lane 1 =
   52–67, declared in the surface XML as `address="$padIndex+36"` / `+52` — and Scale, Chord, Octave,
   root and range are all applied **host-side** by Studio One's `PadSectionComponent`. The two
   "namespaces" turn out to be one: the LED address *is* the note, which is why the SDK calls it a
   *symbolic* pitch and provides `symbolicPitchToPadIndex` to recover the pad from an incoming note.

   **This retires the item that blocked Session mode.** Full evidence in
   `Motion32_Scale_and_Chord_Engine.md` §2.

   > The earlier reasoning is preserved below because it was *nearly* right and shows how the wrong
   > conclusion was reached. The observed 36–86 pitch range is real — but it is the range of the
   > **host's** chord voicing library, which is exactly what you would expect if the host generates the
   > notes. The provenance caveat already recorded in `Motion32_Source_Inventory.md` ("the host's chord
   > library, not a dump of the device's engine") was the thread that unravelled it.

   **What the 2026-07-24 source audit added (still valid):**
   - The **base** is settled: `padIndexToSymbolicPitch = (kPitchC1 + padIndex) % 128`, `kPitchC1 = 36`
     (sdk `musicprotocol.js`). This is the pad's *identity*, and now known to be its output too.
   - `From Studio Pro/Simple.chords` and `Famous.chords` are **explicit 16-row pitch tables** — one row
     per pad — proving the shape of chord output: **27 voicing sets** and **39 progressions**. These are
     the tables the *host* imports (`importChordProgressions`), and they are ours to reuse directly.
   - Observed pitch range across those tables: **36–86**.

   **What the 2026-07-24 source audit added (hard evidence, no capture needed):**
   - The **base** is settled: `padIndexToSymbolicPitch = (kPitchC1 + padIndex) % 128`, `kPitchC1 = 36`
     (sdk `musicprotocol.js`; see implementation notes §7). Scale/Chord/Octave transform on top.
   - `From Studio Pro/Simple.chords` and `Famous.chords` are **explicit 16-row pitch tables** — one row
     per pad — proving the shape of chord output: **27 voicing sets** (Major / Harmonic Minor / Natural
     Minor × Triad, Sus 2, Sus 4, Add 7, Octave, Second, Third, Fourth, Fifth; 2 or 4 notes per pad) and
     **39 progressions** (15 Major, 24 Minor; 4 notes per pad).
   - **Observed pitch range across those tables: 36–86** — which *confirms* the `[INF]` claim that pad
     output escapes the 36–67 LED address range. The two namespaces are definitively distinct.
   - So the remaining unknown is narrow: not *whether* notes exceed the LED range, nor the voicing
     shapes, but **which transform the firmware applies for each Octave/range/bank setting**. One
     capture sweeping Octave ± and A–H closes it.

   ⚠️ Caveat on provenance: those `.chords` files are the **host's** chord library (Studio One chord
   track data), not a dump of the device's engine. Use them as evidence of shape and range, and as a
   ready-made voicing library if we ever build a Live-side chord feature — not as the firmware's table.
5. **Aftertouch.** Channel vs poly (global "Pressure" setting), default state, and the "Pressure Feel" Drum/Piano curve's effect on the data.
6. **Touch strip round-trip.** Confirm both strips report pitch bend on ch0/ch1 in integrated mode, and validate the LED write-back addresses (0x37–0x3F / 0x70–0x78) and the bipolar/fill behaviors. Now also worth confirming the newly-found **strip buttons at CC `0x7A`/`0x7B`** — and note the pitch-bend claim is `[SRC-JS]/[CAP]`, *not* from the surface XML (the XML declares `touchStrip[0/1]` with no MIDI message at all).
7. **`Motion 32 Main` vs the Control/MCU port — PARTIALLY RESOLVED from firmware.** The firmware USB string descriptors define **two** MIDI ports: **`Motion 32 Main`** (native protocol + notes/CC — the port our Scenario-2 script drives) and **`Motion 32 Control`** (the DAW-Mode / Mackie-Control port). So DAW Mode routes Mackie messages out `Motion 32 Control`, leaving `Motion 32 Main` for the native integration. Still to verify on hardware: whether both ports can be driven **simultaneously** (native richness on Main + Mackie transport/faders on Control).

### DAW Mode = Ableton — what the firmware tells us
- DAW Mode is a global setting with four values: **Off / Logic / Ableton / Cubase** (firmware string table). [INF from strings]
- When active, the device speaks **Mackie Control on the `Motion 32 Control` port** (manual + firmware port names). The Logic/Ableton/Cubase choice selects the per-DAW MCU dialect/quirks.
- **This is a separate integration** from the native handshake path (Scenario 2), on a different port: Native = `Motion 32 Main`; DAW/Mackie = `Motion 32 Control`. DAW Mode=Ableton is the zero-code alternative (Live's built-in Mackie support) but yields only transport/mixer basics — no custom screen/pad/encoder control.
- **Whether the two "compete" is unconfirmed.** Because they use different ports, simultaneous operation (native script on Main + Live's Mackie on Control) is *plausible* and could even be useful (Mackie handling some transport/faders while the native script drives screen/pads/encoders) — **but this is untested**, and duplicate events / state conflicts would need to be ruled out. For **v1, DAW Mode Off is recommended** simply to remove ambiguity, not because coexistence is known to fail.
- **Conclusion — DAW Mode=Ableton is a commodity "bone," not a real integration.** It's the standard generic-Mackie transport selector every controller ships; there is **no Ableton-native component** anywhere in the firmware/scripts (unlike the full Studio-Pro native stack). Fender built the deep experience only for their own DAW. **Decision: for v1, set DAW Mode Off and build the Ableton script by piggybacking the documented Studio Pro native integration on `Motion 32 Main`** (revisit Main+Control coexistence later). No further firmware RE is needed for this — the exact MCU dialect is moot while DAW Mode is unused.
- **Not extractable by cheap static RE:** the exact per-DAW byte differences (MCU note/fader dialect). The image is stripped, its string pool is index-packed (no absolute pointer xrefs), no Mackie SysEx handshake template or MCU transport-note constants were found, and linear Thumb disassembly desyncs. Definitive answer needs either interactive disassembly (Ghidra + RP2040 function recovery) or — far cheaper — a MIDI capture of the `Motion 32 Control` port with DAW Mode=Ableton set.

## 3. Host-side logic Ableton must supply

> **Now largely documented.** The Studio One host-side state machine has been fully reconstructed in
> `Motion32_Native_Host_Architecture.md`. The items below are no longer *documentation* gaps — the
> mechanism is known; what remains is **Ableton-specific design** (mapping Motion's model onto Live's).

8. **The device is host-rendered, and in native mode it is host-*driven* musically too.**
   ⚠️ **Corrected 2026-07-25** — this item previously assigned Scale, Chord, Keys/Blocks, Octave and
   range to the firmware. Those are host-owned in native mode. Corrected split (full list in the
   architecture doc §6):
   - **Owned by Motion firmware (local):** Pressure mode + feel, Encoder Curve, DAW Mode, all Global
     Settings and their on-device menu, and the whole stand-alone MIDI scene.
   - **Owned by the host (DAW context):** *all pad→note mapping* — Keys vs Blocks, Scale + root +
     type, A–H range, Octave, chord voicing, Fixed/16‑Velocity — plus plugin assignments, mixer
     values, track names + colors, soft-key labels + colors, and all screen content.

   So our script supplies the host-owned half over SysEx **and owns note generation**. The thing it
   must not do is put Python in the pad→note path: see `Motion32_Scale_and_Chord_Engine.md` §5.
9. **Screen content generation.** The element map is complete; what to render per context is chosen by the `pageIndex` attribute of the active merged state (architecture doc §1). Remaining work: author the actual Ableton content (device params, mixer, transport) and keep a cached model to re-push on redraw.
10. **[MECHANISM DOCUMENTED] Control-focus / mode state machine.** No longer an open question: it's a **14-layer orthogonal state chart** with a supervisor applying side-effects and corrections, resolving to a merged state that stamps `screenTemplate`/`pageIndex`/`knobMode`/`wheelMode`/soft-key mode (architecture doc §1–§4). Remaining work: define the **Ableton-specific** layer values and supervisor predicates (Live's Device/Mixer/Session concepts) and the queued single-commit processor.
11. **[MECHANISM DOCUMENTED] Encoder ↔ parameter binding & paging.** Routing is by `knobMode` (PluginGlobal/PluginFocus/Mixer/Song/Edit…) with wheel-driven paging (architecture doc §7). Remaining work: bind each knobMode to the corresponding Live parameters/sends with takeover logic.
12. **[RESOLVED 2026-07-25 — host-drawn] Scale/Chord.** A MIDI capture of Studio Pro settles it: pressing **Chord** produces nothing but an ordinary inbound `B0 22 7F`, and **the host draws the entire menu**. Studio Pro blanks the Template 3 elements, writes a full Template 1 list — `"Progressions"`, `"Major"`, `"Minor"`, `"Key"`, `"Simple"`, and six progression rows matching the catalogued `Famous.chords` / `Simple.chords` files — repaints the key LEDs with a per-key gradient, and only then sends `F0 08 26 20 01 F7` to select the template. So there is **no on-wire "enter scale mode" command to discover, and no on-device UI to hand control back to**: in native mode the button is a plain input, and the menu/note behavior are host-owned. Full detail in `Motion32_Implementation_Notes.md` §6b-12; the paragraph below is kept for the reasoning that got us here.

    **[superseded reasoning]** The old theory was that note *generation* stayed local to the device (manuals + captures), while the host merely flipped an on-wire "scale on" bit. The capture above disproves that for native mode: `enableScaleMode()` configures Studio One's host-side pad section, and no separate host→device Scale/Chord entry command appears on the wire. This matters for Ableton because Live has no PreSonus pad-section SDK, so we need to own the host-side musical behavior without putting Python directly in the pad→note hot path. (See `Motion32_State_Trace_Table.md`.)

## 4. Firmware disassembly — status & residual value

`motionupgrade.bin` was disassembled (RP2040 Cortex‑M0+ Thumb, flash base `0x00000000`, 0x1000-byte
header, unencrypted). It **corroborated** the device IDs, the `F0 08 26` SysEx family, the global-settings
parameters (DAW Mode / Pressure / Pressure Feel / Encoder Curve), the DAW-Mode targets (Off/Logic/**Ableton**/Cubase),
and the LVGL-based screen. Because the **host side of the protocol is completely specified by the Studio One
JS**, deeper function-level reversing of the firmware is low-value for building the script — reserve it only
if a specific behavior (e.g., exact relative-encoder curve math, or the MCU/DAW-Mode mapping) can't be
captured more cheaply with a MIDI monitor.

---

## 5. Recommended path
1. Stand up a minimal Ableton Remote Script that performs the **handshake** (§1) and confirm the device enters host mode and accepts a test screen write + LED.
2. MIDI-monitor to close the §2 hardware unknowns (encoders, pads, aftertouch, ports).
3. Implement the host-side **layered state engine** following `Motion32_Native_Host_Architecture.md` §8 build order (session + 14-layer model + queued single-commit processor; supervisor with Ableton predicates; knobMode routing).
4. Build out feedback (LEDs, screen templates) per template using the screen map, driven off the cached merged state.

See the architecture doc §8 for the detailed, sequenced build plan — this section is the summary.
