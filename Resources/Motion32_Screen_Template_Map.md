# Motion 32 — Screen Template / Zone / Element Map

Every addressable element of the Motion 32 display, resolved from `Motion 32.surface.xml`
(all `foreach`/`define`/`@eval` loops expanded). Use with the SysEx update message:

```
F0 08 26 21 <templateId> <zoneId> <elementId> <attr> <data…> F7
attr: 00=text(ASCII)  01=color(R G B)  02=value(0–127)  03=visibility(0/1)  04=fontStyle(0/1)
```

Select the active template first: `F0 08 26 20 <templateId> F7`.

**When each template/page is shown is not described here** — that is driven by the host-side state
machine (the merged state's `screenTemplate` + `pageIndex` attributes). See
`Motion32_Native_Host_Architecture.md`. This file is the *address map*; the architecture doc is the *logic*.

The complete row-by-row list — **433 addressable attribute handlers across 181 unique screen elements**
(template/zone/element addresses) — is in **`Motion32_Screen_Template_Map.csv`**.
Below is the structural summary. `[i]` = repeated per index; "attrs" lists which attributes that element accepts.

**Template structure is confirmed from the surface XML [SRC].** Runtime *purpose* is tagged separately:
[CAP] = confirmed by MIDI capture, [INF] = inferred/unconfirmed.

| Template | Structure (XML) | Runtime role |
|---|---|---|
| 0 | encoder-tile layout | **Confirmed Control-Link / plugin-parameter view [CAP]** — plugin captures ended with `F0 08 26 20 00 F7` and wrote all 8 params here (zones 3–6, 8–11) |
| 1 | two 6-row menu columns | Scale / Chord / Add / browser menus [CAP] |
| 2 | 8 channel strips | **Confirmed mixer [CAP]** |
| 3 | 8 text label+value tiles | **Confirmed Song / Timeline view [CAP]** — photographed in Studio Pro's Song mode: blue header title, grey centre bar, 8 two-line tiles. Two text elements per tile (label + value); **no bar/arc attribute at all** |

---

## Template 0 — Main / Control-Link / Plugin view [CAP-confirmed plugin screen]
8 encoder value/label tiles + header (title + 4 top soft-button labels) + footer (4 bottom soft-button labels) + a center text area. Captures confirm this is the screen that renders plugin/Control-Link parameters (zone 7 = page label e.g. "User 1 of 8"; zone 1 element 5 = plugin title).

| Zone | Element(s) | attrs | Meaning |
|---|---|---|---|
| 0 | 0 | color | Screen background |
| 1 | 0 | color | Header background |
| 1 | 1–4 | text,color,visible,font | Top soft-button labels 1–4 (LCD buttons) |
| 1 | 5 | text,color,visible,font | Header title text |
| 2 | 0 | color,visible | Header divider |
| 3–6 | 0 | color | Encoder tile background (encoders 1–4 top bank) |
| 3–6 | 1 | color,value,visible | Encoder halo/fill value + color |
| 3–6 | 2 | text,color,visible | Encoder CC label |
| 7 | 0/1 | color,text,visible | Center text area (background + text) |
| 8–11 | 0 | color | Encoder tile background (encoders 5–8) |
| 8–11 | 1 | color,value,visible | Encoder value + color |
| 8–11 | 2 | text,color,visible | Encoder CC label |
| 12 | 0 | color | Footer divider |
| 13 | 0 | color | Footer background |
| 13 | 1–4 | text,color,visible,font | Bottom soft-button labels 5–8 |

(Encoder tiles occupy zones 3–6 for the top row and 8–11 for the bottom row; each has element 0 = background, 1 = value/color arc, 2 = CC text label.)

## Template 1 — Menu (Scale / Chord / Add menus)
Header with title + 4 top button labels, two menu columns of 6 rows each, footer with 4 button labels.

| Zone | Element(s) | attrs | Meaning |
|---|---|---|---|
| 0 | 0 | color | Background |
| 1 | 0 | color | Header background |
| 1 | 1–4 | text,color,visible,font | Header top button labels |
| 1 | 5 | text,color,visible,font | Header title |
| 2 | 0 | color,visible | Header divider |
| 3 | 0 | color | Menu column 1 background |
| 3 | 1–6 | text,color,visible,font | Menu column 1, rows 1–6 |
| 4 | 0 | color | Menu column 2 background |
| 4 | 1–6 | text,color,visible,font | Menu column 2, rows 1–6 |
| 5 | 0 | color | Footer divider |
| 6 | 0 | color | Footer background |
| 6 | 1–4 | text,color,visible,font | Footer button labels |

## Template 2 — Mixer (8 channel strips)
Zones 1–8 = the 8 channel strips; each strip has 9 elements.

| Zone | Element | attrs | Meaning |
|---|---|---|---|
| 0 | 0 | color | Background |
| 1–8 | 0 | color | Channel strip background |
| 1–8 | 1 | text,visible | Channel number |
| 1–8 | 2 | value,visible | Fader position |
| 1–8 | 3 | value,visible | Mute button state |
| 1–8 | 4 | value,visible | Solo button state |
| 1–8 | 5 | color | Channel label background (track color) |
| 1–8 | 6 | text | Channel label (track name) |
| 1–8 | 7 | color,value,visible | Meter — left |
| 1–8 | 8 | color,value,visible | Meter — right |

## Template 3 — **Song / Timeline view [CONFIRMED]**
Header (title + 4 top button labels), zones 3–6 and 8–11 = 8 tiles each with **label + value**, a
title bar at zone 7, footer with 4 button labels.

**Runtime role confirmed 2026-07-25** from a photograph of Studio Pro's Song mode, which supersedes
the earlier `[INF]` "role unconfirmed" note. The photo matches this address map exactly:

- **zone 1 element 5** — header title, on the blue `#0069CC` header background: `"Timeline"`
- **zone 7** — the grey (`#303336`) centre bar: `"Song 1 of 1"`
- **8 tiles**, each showing two lines = `PARAMS_LABEL[n]` above `PARAMS_VALUE[n]`:
  Transport/Timeline · Position/Zoom · Loop/Start · Loop/End · Track/Event · Event/Start ·
  Event/End · Nudge

**Why this template matters more than it looks.** Each tile has **two independent text elements**,
so a parameter name and its current value can be shown *at the same time*. Template 0 has only one
text element per tile, which is what forces the name↔value swap-on-touch there. Template 3 also has
**no `value` (bar/arc) attribute anywhere** — it is text-only, so it suits numeric readouts (tempo,
bars.beats, loop points) and is the wrong choice for anything wanting a visual fill.

Our Ableton build uses Template 3 for **Song mode** (`display.ParamsView`) and Template 0 for
**Plugin mode**, exactly on that trade-off.

| Zone | Element | attrs | Meaning |
|---|---|---|---|
| 0 | 0 | color | Background |
| 1 | 0 | color | Header background |
| 1 | 1–4 | text,color,visible | Header top button labels |
| 1 | 5 | text,color,visible,font | Header title |
| 2 | 0 | color,visible | Header divider |
| 3–6, 8–11 | 0 | color,visible | Param tile background |
| 3–6, 8–11 | 1 | text,color,visible | Param label |
| 3–6, 8–11 | 2 | text,color,visible | Param value |
| 7 | 0/1 | color,text,visible | Title bar (plugin name) |
| 12 | 0 | color | Footer divider |
| 13 | 0 | color | Footer background |
| 13 | 1–4 | text,color,visible | Footer button labels |

---

### Notes
- "value" elements (faders, meters, encoder arcs, mute/solo) take a single 0–127 byte = normalized × 127.
- Color elements take three 7-bit R/G/B bytes.
- Font style applies to text elements (0 regular / 1 bold) — used to highlight the selected menu row / focused item.
- **Text elements are length-limited**, and the factory abbreviates rather than truncates: encoder labels
  **7 chars**, mixer channel labels **8**, header titles **13**, menu button text **16**. The limits, the
  `compactify` algorithm (ported to Python) and the complete factory colour palette are in
  **`Motion32_Screen_Style_Spec.md`** — read it before writing the renderer.
- Template 1 (Menu) additionally has a **higher-level list API**: `menuListItems`, `menuListTextColor`
  and `menuListSelectionColor` are virtual controls that push a whole list rather than addressing the
  12 row elements one at a time.
- Template 0 zone 7 (centre text) is where the factory renders the **page readout** — the captured
  `"User 1 of 8"` is Control-Link/User paging state, not a title. See
  `Motion32_ControlLink_and_User_Mode.md` §3.
- **Verified 2026-07-24:** the CSV holds exactly 433 rows / 181 unique `(template, zone, element)`
  addresses (141 color, 132 visible, 81 text, 48 value, 31 font).
- The device redraws from host state after every `8F 00 7F` connect and after the Global-Settings screen closes, so the script must keep a cached model of all element values and be able to re-send them on invalidate.
