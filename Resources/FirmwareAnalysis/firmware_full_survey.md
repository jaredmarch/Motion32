# Motion 32 Firmware Survey

- Program: `motionupgrade.bin`
- Language: `ARM:LE:32:Cortex`
- Compiler spec: `default`
- Image base/min address: `00000000` / `00000000`
- Max address: `000ba0a3`

## Vector Table Candidate

- Vector-table base used by survey: `00001000`

- `00` @ `00001000`: `0x200068e0` -> `200068e0` 
- `01` @ `00001004`: `0x00008759` (Thumb) -> `00008758` 
- `02` @ `00001008`: `0x000084a5` (Thumb) -> `000084a4` 
- `03` @ `0000100c`: `0x00008755` (Thumb) -> `00008754` 
- `04` @ `00001010`: `0x00008755` (Thumb) -> `00008754` 
- `05` @ `00001014`: `0x00008755` (Thumb) -> `00008754` 
- `06` @ `00001018`: `0x00008755` (Thumb) -> `00008754` 
- `07` @ `0000101c`: `0x00008755` (Thumb) -> `00008754` 
- `08` @ `00001020`: `0x00000000`
- `09` @ `00001024`: `0x00000000`
- `10` @ `00001028`: `0x00000000`
- `11` @ `0000102c`: `0x00008755` (Thumb) -> `00008754` 
- `12` @ `00001030`: `0x00008755` (Thumb) -> `00008754` 
- `13` @ `00001034`: `0x00000000`
- `14` @ `00001038`: `0x00008755` (Thumb) -> `00008754` 
- `15` @ `0000103c`: `0x00008755` (Thumb) -> `00008754` 
- `16` @ `00001040`: `0x00004b7d` (Thumb) -> `00004b7c` `FUN_00004914`
- `17` @ `00001044`: `0x00004abd` (Thumb) -> `00004abc` `FUN_00004914`
- `18` @ `00001048`: `0x00004cc1` (Thumb) -> `00004cc0` `FUN_00004c98`
- `19` @ `0000104c`: `0x00004d35` (Thumb) -> `00004d34` `FUN_00004ce8`
- `20` @ `00001050`: `0x00004b7d` (Thumb) -> `00004b7c` `FUN_00004914`
- `21` @ `00001054`: `0x00004abd` (Thumb) -> `00004abc` `FUN_00004914`
- `22` @ `00001058`: `0x00004cc1` (Thumb) -> `00004cc0` `FUN_00004c98`
- `23` @ `0000105c`: `0x00004d35` (Thumb) -> `00004d34` `FUN_00004ce8`
- `24` @ `00001060`: `0x00005075` (Thumb) -> `00005074` `FUN_00004e3a`
- `25` @ `00001064`: `0x000081c5` (Thumb) -> `000081c4` 
- `26` @ `00001068`: `0x000081d5` (Thumb) -> `000081d4` 
- `27` @ `0000106c`: `0x000082ad` (Thumb) -> `000082ac` 
- `28` @ `00001070`: `0x00000000`
- `29` @ `00001074`: `0x00000000`
- `30` @ `00001078`: `0x00000000`
- `31` @ `0000107c`: `0x00000000`

## Function Summary

- Functions: `1050`
- Functions with bodies: `1050`
- Function-body bytes: `145375`

First functions by address:
- `000014e4` `FUN_000014e4` size=276
- `000015fc` `FUN_000015fc` size=188
- `000016b8` `FUN_000016b8` size=198
- `00001780` `FUN_00001780` size=26
- `0000179c` `FUN_0000179c` size=198
- `00001864` `FUN_00001864` size=26
- `00001880` `FUN_00001880` size=86
- `000018d8` `FUN_000018d8` size=120
- `00001950` `FUN_00001950` size=74
- `0000199c` `FUN_0000199c` size=34
- `000019c0` `FUN_000019c0` size=40
- `000019e8` `FUN_000019e8` size=328
- `00001b30` `FUN_00001b30` size=190
- `00001bf0` `FUN_00001bf0` size=156
- `00001c8c` `FUN_00001c8c` size=112
- `00001cfc` `FUN_00001cfc` size=42
- `00001d28` `FUN_00001d28` size=42
- `00001d54` `FUN_00001d54` size=22
- `00001d6c` `FUN_00001d6c` size=40
- `00001d94` `FUN_00001d94` size=42
- `00001dc0` `FUN_00001dc0` size=144
- `00001e50` `FUN_00001e50` size=12
- `00001e5c` `FUN_00001e5c` size=94
- `00001ebc` `FUN_00001ebc` size=46
- `00001eec` `FUN_00001eec` size=128
- `00001f6c` `FUN_00001f6c` size=66
- `00001fb0` `FUN_00001fb0` size=68
- `00002030` `FUN_00002030` size=103
- `00002098` `FUN_00002098` size=12
- `000020a4` `FUN_000020a4` size=334
- `00002288` `FUN_00002288` size=196
- `0000234c` `FUN_0000234c` size=190
- `0000240c` `FUN_0000240c` size=524
- `00002618` `FUN_00002618` size=218
- `000026f4` `FUN_000026f4` size=168
- `000027a0` `FUN_000027a0` size=12
- `000027ac` `FUN_000027ac` size=38
- `000027d4` `FUN_000027d4` size=26
- `00002834` `FUN_00002834` size=102
- `000028d0` `FUN_000028d0` size=60

## Scale/Chord String Survey

### `Scale`

- string bytes at `000601fc`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`
- string bytes at `00060238`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Chord`

- string bytes at `00060218`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`
- string bytes at `0006027c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Scales`

- string bytes at `00060238`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Famous`

- string bytes at `00060274`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Simple`

- string bytes at `0006024c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Progressions`

- string bytes at `0006025c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Chords/Intervals`

- string bytes at `0006027c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Choose Key`

- string bytes at `00060240`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Guide`

- string bytes at `00060230`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Layout`

- string bytes at `00060210`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Type`

- string bytes at `00060220`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Quality`

- string bytes at `00060228`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `DAW mode`

- string bytes at `000602c0`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Global Settings`

- string bytes at `00061254`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Firmware`

- string bytes at `00060328`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Ionian`

- string bytes at `00060fd4`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Dorian`

- string bytes at `00060fdc`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Phrygian`

- string bytes at `00060fe4`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Lydian`

- string bytes at `00060ff0`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Mixolydian`

- string bytes at `00060ff8`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Aeolian`

- string bytes at `00061004`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Locrian`

- string bytes at `0006100c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Major Pent`

- string bytes at `00061014`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `M. Minor`

- string bytes at `00061020`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Minor Pent`

- string bytes at `0006102c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Minor Blues`

- string bytes at `00061038`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Major Blues`

- string bytes at `00061044`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Triad`

- string bytes at `00060d4c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Sus2`

- string bytes at `00060d54`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Sus4`

- string bytes at `00060d5c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `Add 7`

- string bytes at `00060d64`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

### `I V vi IV`

- string bytes at `00060eb8`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_00060048` @ `00060048`

## Decompile Snippets For String-Referencing Functions

## Immediate Constants Worth Checking

- `0x08`: 0 operand-0 hits
- `0x20`: 0 operand-0 hits
- `0x21`: 0 operand-0 hits
- `0x22`: 0 operand-0 hits
- `0x23`: 0 operand-0 hits
- `0x36`: 0 operand-0 hits
- `0x7e`: 0 operand-0 hits
- `0x7f`: 0 operand-0 hits
- `0xf0`: 0 operand-0 hits
- `0xf7`: 0 operand-0 hits

