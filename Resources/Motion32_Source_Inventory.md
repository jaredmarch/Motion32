# Motion 32 — Source Inventory & Provenance

**Purpose:** one page that answers "have we mined everything, and where did each claim come from?"
Every primary source file in this folder is listed with its format, what has been extracted from it,
which doc carries that extraction, and whether anything is left unmined.

Audit date: **2026-07-24**, revised **2026-07-25**.
Re-run the audit if new captures or firmware are added.

> ⚠️ **The 2026-07-24 audit missed four folders**, and its "nothing substantial is left unmined"
> conclusion was wrong. `Musical Scales/`, `Chorder/`, `Chords/` and `Chord Sounds/` sit alongside the
> files it did list, and between them they settled the project's last blocking question and corrected a
> guiding principle. They are now in the table below and in
> **`Motion32_Scale_and_Chord_Engine.md`**. The lesson for future audits: the audit walked the files
> *named by the manifest* (`Motion 32.device`) and the loose files beside them — it never listed the
> package's subdirectories, so folders no manifest attribute points at were invisible to it. Enumerate
> the tree, not the manifest.

---

## 1. `From Studio Pro/` — the Studio One / Studio Pro integration package

This is the device's own factory integration, and it is the single richest source. `Motion 32.device`
is the manifest that names every other file in the package:

```
classFile      = Motion32MidiDevice.js     (wire protocol)
scriptFile     = Motion32Component.js      (host logic / state machine)
surfaceFile    = Motion 32.surface.xml     (control + screen definition)
hostDataFile   = Motion 32.surfacedata     (Control-Link + user-command assignment database)
skinFile       = skin/                     (the host's on-screen editor panel)
imageFile/textFile = Motion 32.png / .txt  (cosmetic only)
detectorPortName = "Motion 32,Motion 32 Main"
sendMidiClock=1  feedbackSupported=1  autoMappingSupported=1
```

| File | Format | Status | What we took from it | Lives in |
|---|---|---|---|---|
| `Motion 32.surface.xml` | XML, 252 KB | **fully mined** | Every control's CC/note + LED/RGB handler; the 4 screen templates' 181 elements / 433 attribute handlers; all `$MOTIONSHARED_*` / `$MOTION32_*` constants (LED states, colors, mode enums, **text length limits**) | `Motion32_Control_Surface_Definition.md`, `Motion32_Screen_Template_Map.md/.csv`, `Motion32_Screen_Style_Spec.md` |
| `Motion32MidiDevice.js` | JS, 62 KB | **fully mined** | Native-mode handshake, identity request/reply **byte offsets**, firmware-version rule, SysEx framing, RGB packing, feedback-suspend gate | `Motion32_Handshake_and_SysEx_Spec.md`, `Motion32_Implementation_Notes.md` |
| `Motion32Component.js` | JS, 257 KB | **mined for architecture + formatting**; deep per-page logic is reference-only | 14-layer state chart, merged-state attributes, redraw/commit lifecycle, LED colors + dim/full model, **`StringFormatter.compactify`** label algorithm | `Motion32_Native_Host_Architecture.md`, `Motion32_State_Trace_Table.md`, `Motion32_Screen_Style_Spec.md` |
| `Motion 32.surfacedata` | XML, 70 KB | **fully mined (was previously uncited)** | 121 Control-Link pages across ~90 plugins; 3 User-command pages; the touch strip as an assignable Control-Link target; `Channel Controls` / `Macro Controls` pseudo-devices; persisted `activePage` | `Motion32_ControlLink_and_User_Mode.md` |
| `skin/skin.xml` | XML, 16 KB | **mined (was previously uncited)** | This is the **host's on-screen editor panel**, not the device screen. Confirms the Control-Link paging model (**Auto-Fill**, `pageTitle`/`pageNumber`/`pageCount`, prev/next), the `UserCommandSection0` command model, and that LCD buttons 0–3 are the top row / 4–7 the bottom row | `Motion32_ControlLink_and_User_Mode.md` |
| `skin/images/*` | PNG/SVG | **no further value** | Panel artwork for the Studio One editor window. Nothing device-facing | — |
| `Simple.chords` | JSON | **mined (was previously uncited)** | 27 voicing sets × 16 pads (Major / Harmonic Minor / Natural Minor × Triad, Sus 2, Sus 4, Add 7, Octave, Second, Third, Fourth, Fifth). Pitch range **36–74** | `Motion32_Gap_Analysis.md` §2 |
| `Famous.chords` | JSON | **mined (was previously uncited)** | 39 progressions × 16 pads (15 Major, 24 Minor), 4 notes each. Pitch range **36–86** | `Motion32_Gap_Analysis.md` §2 |
| `AddMenu.data` | JSON | mined for structure | 4 columns of instrument/effect entries with Studio One class IDs + preset paths — the Add-menu content model. The *content* is Studio One specific; the *shape* (4 columns → Menu template) is what we reuse | `Motion32_State_Trace_Table.md` |
| `sdk/` (5 JS files) | JS | **mined** | Generic PreSonus Control Surface SDK base classes: pad→note base (`kPitchC1 = 36`), the 15-entry scale list, pad animation codes, `ControlValue` bipolar/disabled flags, touch-strip event model, handler architecture | `Motion32_Implementation_Notes.md` §7 |
| `Musical Scales/` (15 `.musicalscale`) | XML | **mined 2026-07-25 (was missed)** | The complete scale table as 12-slot semitone bitmasks. Verified to match the SDK `MusicalScaleID` enum exactly and in order; all 15 musically correct | `Motion32_Scale_and_Chord_Engine.md` §4 |
| `Chorder/` (25 `.preset`) | zip → XML | **mined 2026-07-25 (was missed)** | Presets for the Studio One **`Chorder` NoteFX plugin** (`{D2D9B002-…}` = `kNoteFXChorder`) — *not* device assets. Model is `inPitch → [outPitch…]`, with `autofill` transposing a single C4 chord across `loKey`–`hiKey`. Evidence that the factory solves chording with a **device in the signal path** | `Motion32_Scale_and_Chord_Engine.md` §3.1, §5.3 |
| `Chords/` (104 `.chords`) | XML | **mined 2026-07-25 (was missed)** | Studio One **Chord Track** presets (Major 55 / Minor 49) — a different format from `Famous`/`Simple.chords`. `root` is a **circle-of-fifths index** (`semitone = root*7 % 12`), `intervals` a 12-slot mask, `type` the quality. Belongs to the User-mode "Chord Track" command page, not the pads | `Motion32_Scale_and_Chord_Engine.md` §3.2 |
| `Chord Sounds/Chord Preview.preset` | zip → XML | **mined 2026-07-25 (was missed)** | A **Mai Tai** synth patch — the chord-selector audition sound. No protocol value (a clean negative result) | — |
| `Motion 32.device` | XML, 1 KB | **fully mined** | The manifest above; detector port names; `feedbackSupported`/`autoMappingSupported` | this file, `Motion32_Handshake_and_SysEx_Spec.md` §0 |
| `Motion 32.txt` / `.png` / `@2x.png` | text / PNG | **no value** | A one-line connect prompt and product artwork | — |

## 2. `From Universal Control/` — the PreSonus Universal Control support files

This folder describes the device's **stand-alone (non-native) personality** and its firmware. It was
previously uncited by any doc; it is now mined and the results are in §4 below.

| File | Format | Status | What we took from it |
|---|---|---|---|
| `motion32.devicelayout` | JSON, 9 KB | **mined** | The physical inventory of **user-assignable** controls (62) with panel geometry — see §4.1 |
| `motion32.devicescene` | JSON, 52 KB | **mined** | The **factory stand-alone MIDI scene**: what the device sends when *not* in native host mode — see §4.2 |
| `motionhandler.bundle` | Mach-O bundle (x86_64 + arm64), UC 5.1.0 | **mined for strings; no disassembly needed** | Contains only `Motion{16,32}SceneHandler` and `Motion{16,32}FirmwareUpdateTransferCodec` — i.e. it (a) loads/saves the `.devicescene` files and (b) implements "MIDI Transfer Codec for Firmware Updates". Also exposes `factoryScene` / `isTemplate` / `global`. **Nothing native-protocol lives here** — the deep integration is entirely in the Studio Pro package |
| `motionupgrade.bin` | firmware image | **mined at header level; re-checked 2026-07-25 for pad-LED behaviour** | v1.0.6 build `20260630-182229`; RP2040 + LVGL; shared Motion 16 (`0x24`) / Motion 32 (`0x26`) image; DAW Mode options Off/Logic/Ableton/Cubase. **Searched specifically for local pad-LED / note-echo logic and found none** — the only pad-adjacent strings are Global-Settings labels (`Velocity`, `Pressure`, `Pressure Feel`), the note-name table the device's own UI renders, and LVGL/Pico-SDK internals. Consistent with the device being host-rendered in native mode: nothing lights a pad locally, so press feedback is entirely the host's job. Recorded so this is not re-checked a third time |
| `motion32layoutbackground*.png` | PNG | **no value** | Panel artwork |

## 2b. The manuals — `Resources/*.pdf` (added 2026-07-25)

Previously uncited by this inventory, and they turned out to be **load-bearing** for pad banking and
the touch strips: they document user-facing behaviour that no source file states.

| File | Status | What we took from it |
|---|---|---|
| `OM_2777100104_Motion-32_EN.pdf` (owner's manual) | **mined 2026-07-25** | A–H roles per pad mode and that **Keys mode rests on bank `E`** with Pad 1 as the root; Keys vs Blocks layouts (and that some top-lane pads are deliberately dark); Octave ±12 global, blue when unmodified; touch-strip rest positions, jump-to-touch, and that **strip 1 returns to centre on release while strip 2 holds** |
| `UM_2777100104_Motion-32-Studio-Pro-Integration_EN.pdf` | **mined 2026-07-25** | The Studio Pro side of the same, plus the Shift+tap gesture for the strips' secondary identities |

Both feed `Motion32_Pads_Banking_and_Strips.md`. Tagged **[MAN]** there to distinguish
documented-behaviour claims from `[SRC]` code reading.

## 3. Reference scripts and the framework itself (Ableton side)

| File | Status | Role |
|---|---|---|
| `control_surface/` (in `Motion32/Resources/`) | **primary source — read this first for any framework question** | Live 12's own `ableton/v3/control_surface/` as `.pyc`, decompilable with `xdis`. **This is authoritative** for call signatures, component control names, listenable properties and skin keys. Adding it immediately settled the encoder-parameter accessor, proved `create_skin` merges over the default skin, and caught a `ParameterInfo` unwrapping bug that hardware testing would have shown only as "every halo reads zero". Findings in `Motion32_Implementation_Notes.md` §6b-1 |
| `ATOMSQ.zip` | reference, partially mined (bytecode) | The factory Atom SQ Live 12 script — the **`ableton.v3` idiom** reference. Confirmed component/control vocabulary is in `Motion32_Build_Roadmap.md` Appendix A |
| `CustomAtomSQ Plus.zip` | reference, ideas only | A WIP custom add-on in readable `.py`. **Not canon** — a source of ideas, and useful evidence of working call shapes, but it is not a substitute for the framework source (it was the basis for the `channel=` mistake in §4 by omission) |

### Useful entry points in `control_surface/`

| File | What it settles |
|---|---|
| `elements_base.pyc` | `add_button` / `add_encoder` / `add_*_matrix` signatures — including that `add_matrix` supplies `channel` itself |
| `components/device.pyc` | The Device component: `parameters` (listenable), `bank_name`, `bank_index`, `__getattr__` bank forwarding |
| `components/device_bank_navigation.pyc` | `set_prev_bank_button` / `set_next_bank_button` / `set_bank_scroll_encoder` / `set_bank_select_buttons` |
| `parameter_info.pyc` | `ParameterInfo(parameter, name)` — the wrapper `DeviceComponent.parameters` yields |
| `default_skin.pyc` | Every default colour key, and that `create_skin` merges a partial skin over them |
| `components/` (40 files) | The available component vocabulary: mixer, session, session_ring, channel_strip, target_track, view_control, transport, undo_redo, clip_actions, drum_group, note_editor, step_sequence, … — the menu for later phases |

## 4. What the Universal Control files add (new material)

### 4.1 Physical inventory — which controls are *user-assignable*
`motion32.devicelayout` lists **62** assignable controls in 5 sections:

| Section | Count | IDs |
|---|---|---|
| `encoders` | 8 | `encoder1`–`encoder8` |
| `buttons` | 16 | `buttonpresetup/down`, `buttonarrowup/down/left/right`, `buttonsolo`, `buttonmute`, `buttonsoftscreen1`–`8` |
| `transportcontrols` | 4 | `transportstop`, `transportplay`, `transportrecord`, `transporttap` |
| `pads` | 32 | `pad1`–`pad32` |
| `touchstrips` | 2 | `touchstrippitch`, `touchstripmod` |

**The useful negative result:** the mode buttons (Song/Plugin/Edit/Mix, Add/Scale/Chord/Control, Shift,
bank A–H, Octave ±, "16", Fixed, Pads, Launch, wheel) are **absent** from this list. They are reserved
device functions that Universal Control will not let a user remap — which is consistent with them being
the controls the native host protocol expects to own. It also confirms the strips' default identities:
strip 1 = **pitch**, strip 2 = **mod**.

### 4.2 The stand-alone MIDI scene (out of scope for the script, recorded for completeness)
`motion32.devicescene` is the factory scene used when the device is *not* in native host mode. It is a
**different map from the native one** — do not confuse the two. 166 assignments across 4 scene banks:

| Control | Stand-alone scene | Native host mode (for contrast) |
|---|---|---|
| Encoders 1–8 | **absolute** CC, bank 0 = `16,17,18,19,80,81,82,83`; bank 1 = `70,71,74,76,73,75,72,79` | **relative** CC `0x0E`–`0x15`, sign-bit at 0x40 |
| Soft screen buttons 1–8 | CC `106`–`113` | CC `0x24`–`0x2B` (36–43) |
| Nav up/down/left/right | CC `86 / 87 / 85 / 89` | CC `0x57 / 0x59 / 0x5A / 0x66` |
| Solo / Mute | CC `80 / 81` | CC `0x4A / 0x4B` |
| Transport stop/play/rec/tap | note `102 / 103 / 104 / 105` | CC `0x6F / 0x6D / 0x6B / 0x69` |
| Preset up/down | Program Change | CC `0x2C / 0x2D` |
| Pads 1–32 | notes **80–111 on channel 10**, identical in all 4 banks (pads 17–32 repeat pads 1–16) | notes **36–67**, fixed — the same address serves as LED and note; all musical transforms are host-side |
| Touch strips | both CC `1` | pitch bend on channels 0 and 1 |

Scene bank colors (8 distinct): `#0000ff`, `#008000`, `#ff0000`, `#00ff00`, `#ffc0cb`, `#ff00ff`,
`#00ffff`, `#ffff00`.

**Why this matters even though we don't use it:** it is the definitive answer to "what is the device
doing when my script isn't loaded / hasn't handshaken." If a capture shows encoders sending absolute
CC 16–19 or pads on channel 10, the device is in the stand-alone scene, not native mode — a third
failure signature to add alongside the pre-native `0x66-0x69` transport symptom.

---

## 5. Conclusion of the audit

**Revised 2026-07-25.** With the four missed folders now mined, the remaining unread bytes are artwork,
the Studio One editor panel images, and the body of `Motion32Component.js`'s per-page rendering logic —
which is Studio One host logic we deliberately do not port (we implement the equivalent against Live's
LOM instead).

> The previous wording — "nothing substantial is left unmined" — was stated with more confidence than
> the method supported, and was wrong. The four folders it missed contained the answer to the project's
> one blocking question. Treat a completeness claim as only as strong as its enumeration method.

New material this audit produced, and where it went:

1. `Motion32_Screen_Style_Spec.md` — **new**: text length limits, the `compactify` label algorithm, and
   the full screen/LED color palette with 7-bit conversions.
2. `Motion32_ControlLink_and_User_Mode.md` — **new**: the Control-Link paging/Auto-Fill model, the User
   command-page model, and how both translate to Live.
3. `Motion32_Control_Surface_Definition.md` — **corrected**: added `touchStripButton[0/1]` = CC `0x7A`/`0x7B`,
   the `lcdUserButton[0..7]` and `menuList*` virtual controls, the encoder-halo address, and an explicit
   address-overlap warning.
4. `Motion32_Implementation_Notes.md` — **corrected**: the exact identity-reply byte offsets (which
   settle a live bug in `protocol.py`).
5. `Motion32_Gap_Analysis.md` — **narrowed**: the chord files give hard evidence on pad note ranges.
6. This file — the provenance record.

New material the **2026-07-25** revision produced:

7. `Motion32_Pads_Banking_and_Strips.md` — **new**: pad addressing, the three context-dependent A–H
   roles (default `E`), Octave, and the touch strips — including the correction that
   `touchStripButton[0]/[1]` is a **contact sensor**, not a physical button, so touch and position are
   separable, and that **return-to-centre is host-side**.
8. `Motion32_Scale_and_Chord_Engine.md` — **new**: proof that Scale and Chord are host-side in native
   mode (closing the pad-note gap and correcting the ownership split in three docs), the complete
   15-scale table, the two distinct chord-file formats, and the Live implementation design under a
   no-added-latency constraint.
