# Motion 32 Pointer Search Probe

## Target `0x00003ac4`

- no Ghidra references to aligned address
- raw little-endian pattern: `c4 3a 00 00`
  - no raw hits
- instruction scalar/immediate hits:
  - no scalar hits

## Target `0x00003ac5`

- no Ghidra references to aligned address
- raw little-endian pattern: `c5 3a 00 00`
  - no raw hits
- instruction scalar/immediate hits:
  - no scalar hits

## Target `0x000020a4`

- no Ghidra references to aligned address
- raw little-endian pattern: `a4 20 00 00`
  - no raw hits
- instruction scalar/immediate hits:
  - no scalar hits

## Target `0x000020a5`

- no Ghidra references to aligned address
- raw little-endian pattern: `a5 20 00 00`
  - raw hit `00087acc` in `<none>` @ `<none>`
- instruction scalar/immediate hits:
  - no scalar hits

## Target `0x00002098`

- Ghidra ref from `00003f92` in `FUN_00003f88` @ `00003f88` type=UNCONDITIONAL_CALL
- raw little-endian pattern: `98 20 00 00`
  - no raw hits
- instruction scalar/immediate hits:
  - no scalar hits

## Target `0x00002099`

- Ghidra ref from `00003f92` in `FUN_00003f88` @ `00003f88` type=UNCONDITIONAL_CALL
- raw little-endian pattern: `99 20 00 00`
  - raw hit `00021b7b` in `<none>` @ `<none>`
  - raw hit `00029297` in `<none>` @ `<none>`
  - raw hit `000292ed` in `<none>` @ `<none>`
  - raw hit `000296d7` in `<none>` @ `<none>`
  - raw hit `00029dff` in `<none>` @ `<none>`
  - raw hit `00029ee7` in `<none>` @ `<none>`
  - raw hit `0002a4e5` in `<none>` @ `<none>`
  - raw hit `0002b05d` in `<none>` @ `<none>`
  - raw hit `0002bc6b` in `<none>` @ `<none>`
  - raw hit `0002bd35` in `<none>` @ `<none>`
  - raw hit `0002bdd7` in `<none>` @ `<none>`
  - raw hit `0002bff3` in `<none>` @ `<none>`
  - raw hit `0002c047` in `<none>` @ `<none>`
  - raw hit `0002c0b7` in `<none>` @ `<none>`
  - raw hit `0002c0ed` in `<none>` @ `<none>`
  - raw hit `0002c28b` in `<none>` @ `<none>`
  - raw hit `0002c5af` in `<none>` @ `<none>`
  - raw hit `0002c793` in `<none>` @ `<none>`
  - raw hit `0002c837` in `<none>` @ `<none>`
  - raw hit `0002ca41` in `<none>` @ `<none>`
  - raw hit `0002cac7` in `<none>` @ `<none>`
  - raw hit `0002caf3` in `<none>` @ `<none>`
  - raw hit `0002ccab` in `<none>` @ `<none>`
  - raw hit `00058db3` in `<none>` @ `<none>`
- instruction scalar/immediate hits:
  - no scalar hits

## Target `0x00002e6c`

- no Ghidra references to aligned address
- raw little-endian pattern: `6c 2e 00 00`
  - no raw hits
- instruction scalar/immediate hits:
  - no scalar hits

## Target `0x00002e6d`

- no Ghidra references to aligned address
- raw little-endian pattern: `6d 2e 00 00`
  - no raw hits
- instruction scalar/immediate hits:
  - scalar hit `00003f88: movw r0,#0x2e6d` in `FUN_00003f88` @ `00003f88`

