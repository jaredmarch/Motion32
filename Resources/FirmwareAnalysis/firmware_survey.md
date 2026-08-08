# Motion 32 Firmware Survey

- Program: `motion32_fw_payload_0x1000.bin`
- Language: `ARM:LE:32:Cortex`
- Compiler spec: `default`
- Image base/min address: `00000000` / `00000000`
- Max address: `000b90a3`

## Vector Table Candidate

- `00` @ `00000000`: `0x200068e0` -> `200068e0` 
- `01` @ `00000004`: `0x00008759` (Thumb) -> `00008758` `FUN_00008758`
- `02` @ `00000008`: `0x000084a5` (Thumb) -> `000084a4` 
- `03` @ `0000000c`: `0x00008755` (Thumb) -> `00008754` `FUN_00008754`
- `04` @ `00000010`: `0x00008755` (Thumb) -> `00008754` `FUN_00008754`
- `05` @ `00000014`: `0x00008755` (Thumb) -> `00008754` `FUN_00008754`
- `06` @ `00000018`: `0x00008755` (Thumb) -> `00008754` `FUN_00008754`
- `07` @ `0000001c`: `0x00008755` (Thumb) -> `00008754` `FUN_00008754`
- `08` @ `00000020`: `0x00000000`
- `09` @ `00000024`: `0x00000000`
- `10` @ `00000028`: `0x00000000`
- `11` @ `0000002c`: `0x00008755` (Thumb) -> `00008754` `FUN_00008754`
- `12` @ `00000030`: `0x00008755` (Thumb) -> `00008754` `FUN_00008754`
- `13` @ `00000034`: `0x00000000`
- `14` @ `00000038`: `0x00008755` (Thumb) -> `00008754` `FUN_00008754`
- `15` @ `0000003c`: `0x00008755` (Thumb) -> `00008754` `FUN_00008754`
- `16` @ `00000040`: `0x00004b7d` (Thumb) -> `00004b7c` `FUN_00004b7c`
- `17` @ `00000044`: `0x00004abd` (Thumb) -> `00004abc` `FUN_00004abc`
- `18` @ `00000048`: `0x00004cc1` (Thumb) -> `00004cc0` `FUN_00004cc0`
- `19` @ `0000004c`: `0x00004d35` (Thumb) -> `00004d34` `FUN_00004d34`
- `20` @ `00000050`: `0x00004b7d` (Thumb) -> `00004b7c` `FUN_00004b7c`
- `21` @ `00000054`: `0x00004abd` (Thumb) -> `00004abc` `FUN_00004abc`
- `22` @ `00000058`: `0x00004cc1` (Thumb) -> `00004cc0` `FUN_00004cc0`
- `23` @ `0000005c`: `0x00004d35` (Thumb) -> `00004d34` `FUN_00004d34`
- `24` @ `00000060`: `0x00005075` (Thumb) -> `00005074` `FUN_00005074`
- `25` @ `00000064`: `0x000081c5` (Thumb) -> `000081c4` 
- `26` @ `00000068`: `0x000081d5` (Thumb) -> `000081d4` 
- `27` @ `0000006c`: `0x000082ad` (Thumb) -> `000082ac` 
- `28` @ `00000070`: `0x00000000`
- `29` @ `00000074`: `0x00000000`
- `30` @ `00000078`: `0x00000000`
- `31` @ `0000007c`: `0x00000000`

## Function Summary

- Functions: `1049`
- Functions with bodies: `1049`
- Function-body bytes: `143490`

First functions by address:
- `0000043c` `FUN_0000043c` size=36
- `00000460` `FUN_00000460` size=44
- `0000048c` `FUN_0000048c` size=44
- `000004e4` `FUN_000004e4` size=276
- `000005fc` `FUN_000005fc` size=188
- `000006b8` `FUN_000006b8` size=198
- `00000780` `FUN_00000780` size=26
- `0000079c` `FUN_0000079c` size=198
- `00000864` `FUN_00000864` size=26
- `00000880` `FUN_00000880` size=86
- `000008d8` `FUN_000008d8` size=120
- `00000950` `FUN_00000950` size=74
- `0000099c` `FUN_0000099c` size=34
- `000009c0` `FUN_000009c0` size=40
- `000009e8` `FUN_000009e8` size=328
- `00000b30` `FUN_00000b30` size=190
- `00000bf0` `FUN_00000bf0` size=156
- `00000c8c` `FUN_00000c8c` size=112
- `00000cfc` `FUN_00000cfc` size=42
- `00000d28` `FUN_00000d28` size=42
- `00000d54` `FUN_00000d54` size=22
- `00000d6c` `FUN_00000d6c` size=40
- `00000d94` `FUN_00000d94` size=42
- `00000dc0` `FUN_00000dc0` size=144
- `00000e50` `FUN_00000e50` size=12
- `00000e5c` `FUN_00000e5c` size=94
- `00000ebc` `FUN_00000ebc` size=46
- `00000eec` `FUN_00000eec` size=128
- `00000f6c` `FUN_00000f6c` size=66
- `00000fb0` `FUN_00000fb0` size=68
- `00000ff4` `FUN_00000ff4` size=60
- `00001030` `FUN_00001030` size=104
- `00001098` `FUN_00001098` size=12
- `000010a4` `FUN_000010a4` size=334
- `00001288` `FUN_00001288` size=196
- `0000134c` `FUN_0000134c` size=190
- `0000140c` `FUN_0000140c` size=524
- `00001618` `FUN_00001618` size=218
- `000016f4` `FUN_000016f4` size=168
- `000017a0` `FUN_000017a0` size=12

## Scale/Chord String Survey

### `Scale`

- string bytes at `0005f1fc`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`
- string bytes at `0005f238`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Chord`

- string bytes at `0005f218`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`
- string bytes at `0005f27c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Scales`

- string bytes at `0005f238`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Famous`

- string bytes at `0005f274`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Simple`

- string bytes at `0005f24c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Progressions`

- string bytes at `0005f25c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Chords/Intervals`

- string bytes at `0005f27c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Choose Key`

- string bytes at `0005f240`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Guide`

- string bytes at `0005f230`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Layout`

- string bytes at `0005f210`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Type`

- string bytes at `0005f220`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Quality`

- string bytes at `0005f228`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `DAW mode`

- string bytes at `0005f2c0`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Global Settings`

- string bytes at `00060254`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Firmware`

- string bytes at `0005f328`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Ionian`

- string bytes at `0005ffd4`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Dorian`

- string bytes at `0005ffdc`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Phrygian`

- string bytes at `0005ffe4`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Lydian`

- string bytes at `0005fff0`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Mixolydian`

- string bytes at `0005fff8`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Aeolian`

- string bytes at `00060004`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Locrian`

- string bytes at `0006000c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Major Pent`

- string bytes at `00060014`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `M. Minor`

- string bytes at `00060020`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Minor Pent`

- string bytes at `0006002c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Minor Blues`

- string bytes at `00060038`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Major Blues`

- string bytes at `00060044`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Triad`

- string bytes at `0005fd4c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Sus2`

- string bytes at `0005fd54`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Sus4`

- string bytes at `0005fd5c`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `Add 7`

- string bytes at `0005fd64`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

### `I V vi IV`

- string bytes at `0005feb8`
  - no direct Ghidra xrefs
  - nearest prior function: `FUN_0005f048` @ `0005f048`

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

