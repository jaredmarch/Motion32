# Motion 32 — Control-Link, paging, and User mode

**Why this file exists:** `Motion 32.surfacedata` (70 KB, named as the `hostDataFile` in
`Motion 32.device`) and `skin/skin.xml` were cited by **no** doc. Between them they define how the
factory integration decides *what the 8 encoders control*, *how you page through parameters*, and
*what User mode actually is*. That is the substance of Phase 3 (the flagship Plugin view) and of the
User-mode feature we'd otherwise have had to invent. Everything here is **[SRC]**.

---

## 1. Control-Link in one paragraph

Studio One's "Control-Link" is the binding layer between the 8 physical encoders and whatever is in
focus. `Motion 32.surfacedata` is its **persisted assignment database**: for each plugin, an ordered
list of **pages**, each page mapping `knob[0..7]` → a named plugin parameter, plus optionally a
`controlLinkTouchStrip` → a parameter. `skin.xml` is the editor UI over that database.

## 2. The data model (from `Motion 32.surfacedata`)

```xml
<SurfaceData surfaceID="{A342310B-…}" revision="2">
  <SurfaceDeviceAssignment deviceID="{D9AE9ACD-…}" friendlyName="Pro EQ">
    <List x:id="pages">
      <SurfaceAssignmentPage>
        <Association key="knob[0]" value="{D9AE9ACD-…}/lowcut.lcfreq"/>
        …
        <Association key="knob[7]" value="{D9AE9ACD-…}/opt.gain"/>
      </SurfaceAssignmentPage>
    </List>
  </SurfaceDeviceAssignment>
</SurfaceData>
```

Contents of the factory file:

| Thing | Count |
|---|---|
| `SurfaceDeviceAssignment` blocks (plugins + pseudo-devices) | 49 distinct device IDs / ~90 friendly names |
| `SurfaceAssignmentPage` (pages of 8) | 121 |
| `Association` rows | 472 |
| `knob[n]` assignments | 441 |
| `commandSection0.command[n]` assignments | 24 |
| `controlLinkTouchStrip` assignments | 7 |

### Five properties worth copying

1. **A page is 8 knobs, and pages are ordered.** Big plugins get many (Surround Delay has 7; Big Fuzz
   20 rows' worth). Paging is the primary navigation, not scrolling.
2. **Pages may be sparse and out of order.** Several pages omit a knob entirely, and `knob[4]` sometimes
   appears before `knob[3]`. So a page is a *dict*, not a list — an unassigned knob is a legal state
   (and renders greyed, per `USERCOMMANDUNASSIGNED` / `PARAMSPLUGINDISABLED`).
3. **The touch strip is an assignable Control-Link target.** `controlLinkTouchStrip` sits inside the
   page alongside the knobs, so it's effectively a **9th assignable control per page** — Surround Delay assigns it
   to `showtap` on six pages and `mix` on the seventh. **This is not in any other doc.**
4. **The active page is persisted per device.** `activePage="0"` appears as an attribute on
   `SurfaceDeviceAssignment` — returning to a plugin restores the page you left it on.
5. **Two pseudo-devices are first-class Control-Link targets**, with fixed 1:1 macro maps:
   - `Channel Controls` — `AudioChannelMacroControlSet/float-1..8` (the focused channel's 8 macros)
   - `Macro Controls` — `GlobalMacroControlSet/float-1..8` (8 global macros)

## 3. Paging and Auto-Fill (from `skin/skin.xml`)

The `MotionSharedControlLinkPaging` form exposes the whole paging contract:

| Control | Meaning |
|---|---|
| `pagingMode` | 3 variants; **Auto-Fill** is one of them (`value="2"`) |
| `pageTitle` | editable when user-defined, read-only text when auto-filled |
| `pageNumber` / `pageCount` | the "n / m" readout (this is the source of the captured `"User 1 of 8"` in Template 0 zone 7) |
| `prevPage` / `nextPage` | page stepping |

**Auto-Fill** is the mode where the host fills the 8 knobs from the focused plugin's parameter list in
order, instead of using a curated page. The distinction matters: a curated page has a **name**; an
auto-filled page is named by position. The mode is a per-device toggle, and note that the paging
`pageTitle` style differs between the two (`MotionSharedPageTitleUser` vs `PageTitleAutofill`).

Also confirmed by the same form: `focusDeviceFullName` is the string that feeds the header title, and
each `knob[i]` carries a `userAssignment` text field — the string the encoder tile label renders.

## 4. User mode is a command-page system

This is the part that was least understood. Three sources agree:

- **`Motion 32.surface.xml`** declares `lcdUserButton[0]`–`[7]`, titled **"User 1"–"User 8"**, as
  `type="trigger" options="receive"` with **no `<MidiMessage>`** — i.e. *virtual* controls, exactly like
  `screenTemplateSwitch`. They are a second logical identity for the same physical LCD soft buttons
  (CC `0x24`–`0x2B`); which identity is live is decided by the merged state's `screenButtonsMode`.
- **`skin.xml`** binds them via `UserCommandSection0/Command0..7`, each with `commandTitle`,
  `commandNumber` and `commandAssigned`, laid out as **top row = commands 0–3, bottom row = 4–7** —
  which also confirms the physical→screen mapping (top row ↔ Template 0 header labels 1–4, bottom row ↔
  footer labels 5–8). It has its **own independent paging** (`UserCommandSection0/Paging`), separate
  from Control-Link's.
- **`Motion 32.surfacedata`** ships the three factory pages:

| Page | Commands 0–7 |
|---|---|
| **Chord Track** | Open Chord Track · Show Chord Track in Editor · Chord Display · Chord Selector · Extract to Chord Track · Apply Chords from Chord Track · Detect Chords · Insert Instrument Parts from Chord Track |
| **Note Actions** | Quantize 50% · Macro "Humanize" (`SHVtYW5pemU=` = base64 "Humanize") · Restore Timing · Quantize End · Extend to Part End · Repeat Notes to Part End · Split at Grid · Toggle Mute |
| **Select** | Select All · Deselect All · Invert Selection · Select All on Tracks · Deselect All on Tracks · Select All in Loop · Select Events in Range · Select Muted Events |

So: **User mode = named pages of 8 host commands on the LCD soft buttons, with its own paging.** Reached
by **Shift + Control** (handshake spec §2.2), rendered in Template 0's header/footer label zones, and
coloured by `BUTTONUSERCOMMAND*` / `USERCOMMAND*` (blue when active, grey when unassigned).

## 5. How this translates to Ableton Live

The mechanism maps cleanly; only the target vocabulary changes.

### 5.1 Plugin view (Phase 3)
| Studio One | Live equivalent |
|---|---|
| Control-Link page of 8 | The `Device` component's parameter bank — `parameter_controls` |
| Page prev/next | Bank buttons / soft L-R / wheel, per `wheelMode = ControlLinkPaging` |
| Auto-Fill | Live's **default best-of-bank ordering** already is auto-fill. Live's own "banks" (a device's curated pages) are the *curated* equivalent — so Live gives us both halves of `pagingMode` for free |
| `Channel Controls` (channel macros 1–8) | The 8 **Macro** knobs of a selected Rack (`Audio/Instrument/Drum Rack`) |
| `Macro Controls` (global macros 1–8) | No exact analogue. Best fit: a user-defined bank of 8 targets — a natural home for the v3 "beyond the Atom SQ" ambition |
| `activePage` persisted per device | Cache the bank index per device (keyed by the device object) and restore on re-focus |
| `controlLinkTouchStrip` (9th assignable per page) | An assignable strip target per device page — a genuinely Motion-only feature worth building |
| `focusDeviceFullName` → header | `device.name` through `compactify(…, 13)` |
| Sparse pages / unassigned knob | A bank with fewer than 8 params: grey the empty tiles rather than leaving stale labels |

### 5.2 User mode (Phase 7-adjacent, but designable now)
Live's LOM has no command registry, so "commands" become a table of Python callables. The structure to
copy is the *page*:

```
UserPage = {"title": str, "commands": {0..7: (label, callable)}}
```

Then: Shift+Control enters User mode → `screenButtonsMode = UserCommands` → the 8 LCD buttons fire
`commands[i]`, the header/footer labels render `compactify(label, …)`, the wheel pages through User
pages, and unassigned slots render grey. Sensible first Live pages, all backed by real LOM calls:

- **Edit** — Undo, Redo, Duplicate Clip, Delete Clip, Quantize, Double Loop, Consolidate*, Crop
- **Select/Nav** — prev/next track, prev/next scene, prev/next device, toggle device on/off
- **Session** — Capture MIDI, Duplicate Scene, Delete Scene, Stop All Clips, Re-enable Automation, Tap Tempo, Metronome, Loop
- **View** — toggle Session/Arrangement, Detail view, Browser, Device/Clip view

\* `Consolidate`/`Split` remain the known LOM gaps flagged in `Motion32_Build_Roadmap.md` §4.6 — keep
them greyed as `USERCOMMANDUNASSIGNED` rather than silently doing nothing. The grey-when-unassigned
convention exists precisely for this.

### 5.3 Design consequence worth stating plainly
The factory has **two independent paging systems** running at once — Control-Link pages (encoders) and
User command pages (soft buttons) — each with its own title, index and count, both surfaced on the same
screen template. Our state model should carry two independent page cursors, not one. Collapsing them
into a single "page" is the kind of shortcut that produces exactly the screen-ownership collisions
`Motion32_Build_Roadmap.md` §0.3 warns about.
