# Motion 32 Firmware Table Probe

- Program: `motionupgrade.bin`
- Language: `ARM:LE:32:Cortex`

## Thumb/ARM Pointer Hits

### `outgoing Fender SysEx builder / false 0x8f lead` @ `0x0002164c`

- no raw pointer hits

### `UI redraw/update candidate` @ `0x00021f24`

- no raw pointer hits

### `MIDI/control map refresh candidate` @ `0x00022b70`

- no raw pointer hits

### `config getter` @ `0x0002ec30`

- no raw pointer hits

### `config setter-ish candidate` @ `0x0002ea70`

- no raw pointer hits

### `ranked 0x8f UI/graphics candidate` @ `0x0003e600`

- no raw pointer hits

### `ranked 0x8f UI/assert candidate` @ `0x0003bb58`

- no raw pointer hits

### `Tiny/packet-ish ranked candidate` @ `0x0005ed60`

- no raw pointer hits

## MIDI Map Byte-Pattern Hits

### `native transport ascending tap/rec/play/stop`

- no exact hits

### `native transport descending stop/play/rec/tap`

- no exact hits

### `pre-native transport symptom`

- hit at `00064a93`
  - containing function: `<none>` @ `<none>`
  - bytes: 73 68 5f 63 61 63 68 65 5f 66 75 6e 63 00 00 00 00 30 31 32 33 34 35 36 37 38 39 61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 7a 00 00 00 00 ec 09 10 10 dc 09 10 10 fe 09 10 10 08 0a 10 10 14 0a 10 10 ec 09 10

### `native nav exact`

- no exact hits

### `encoder CCs`

- hit at `00064e48`
  - containing function: `<none>` @ `<none>`
  - bytes: 5f 74 6f 00 50 5f 5a 00 00 00 00 01 01 02 02 03 03 04 04 05 05 06 07 07 08 09 09 0a 0b 0c 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1d 1e 1f 21 22 23 25 26 28 2a 2b 2d 2f 31 33 35 37 39 3b 3d 3f 42 44 47 49 4c 4e 51 54 57 5a 5d 60 64

### `encoder touch CCs`

- hit at `00064a9d`
  - containing function: `<none>` @ `<none>`
  - bytes: 75 6e 63 00 00 00 00 30 31 32 33 34 35 36 37 38 39 61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 7a 00 00 00 00 ec 09 10 10 dc 09 10 10 fe 09 10 10 08 0a 10 10 14 0a 10 10 ec 09 10 10 f2 09 10 10 5c 0a 10 10 c2

### `native pads 36-51`

- no exact hits

### `native pads 52-67`

- no exact hits

### `standalone pads 80-95`

- no exact hits

### `standalone pads 96-111`

- no exact hits

