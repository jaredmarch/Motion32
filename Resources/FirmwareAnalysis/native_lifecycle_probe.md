# Motion 32 Native Lifecycle Probe

Target: host command `8F 00 7F` / `8F 00 00`.
This pass scores decompiled functions for channel-voice MIDI parsing patterns,
USB-MIDI CIN/note-off handling, and writes to RAM state near known control flags.

## Interesting Scalar Sites

### `0x8f`

- `000206f2`: `movs r5,#0x8f` in `FUN_0002064c` @ `0002064c`
- `0003aba4`: `movs r2,#0x8f` in `FUN_0003ab58` @ `0003ab58`
- `0003d7b8`: `movs r3,#0x8f` in `FUN_0003d600` @ `0003d600`

### `0x8`

- `00000598`: `ldr r2,[r2,#0x8]` in `FUN_000004e4` @ `000004e4`
- `0000059e`: `str r2,[r3,#0x8]` in `FUN_000004e4` @ `000004e4`
- `000005be`: `ldr r2,[r2,#0x8]` in `FUN_000004e4` @ `000004e4`
- `000005c2`: `str r2,[r3,#0x8]` in `FUN_000004e4` @ `000004e4`
- `00000616`: `ldrh r3,[r0,#0x8]` in `FUN_000005fc` @ `000005fc`
- `0000064e`: `strh r1,[r3,#0x8]` in `FUN_000005fc` @ `000005fc`
- `00000822`: `strb r0,[r4,#0x8]` in `FUN_0000079c` @ `0000079c`
- `000008c8`: `strh r3,[r0,#0x8]` in `FUN_00000880` @ `00000880`
- `0000090a`: `ldr r1,[r2,#0x8]` in `FUN_000008d8` @ `000008d8`
- `0000091a`: `strh r1,[r0,#0x8]` in `FUN_000008d8` @ `000008d8`
- `0000096c`: `strh r2,[r3,#0x8]` in `FUN_00000950` @ `00000950`
- `00000976`: `ldrh r2,[r0,#0x8]` in `FUN_00000950` @ `00000950`
- `00000b5e`: `strh r3,[r2,#0x8]` in `FUN_00000b30` @ `00000b30`
- `00000bfc`: `sub sp,#0x8` in `FUN_00000bf0` @ `00000bf0`
- `00000c52`: `add sp,#0x8` in `FUN_00000bf0` @ `00000bf0`
- `00000c5a`: `movs r3,#0x8` in `FUN_00000bf0` @ `00000bf0`
- `00000cda`: `movs r3,#0x8` in `FUN_00000c8c` @ `00000c8c`
- `00000d10`: `movs r2,#0x8` in `FUN_00000cfc` @ `00000cfc`
- `00000d32`: `ldr r2,[r4,#0x8]` in `FUN_00000d28` @ `00000d28`
- `00000d58`: `ldr r2,[r0,#0x8]` in `FUN_00000d54` @ `00000d54`
- `00000d6e`: `sub sp,#0x8` in `FUN_00000d6c` @ `00000d6c`
- `00000d72`: `ldr r3,[r0,#0x8]` in `FUN_00000d6c` @ `00000d6c`
- `00000d90`: `add sp,#0x8` in `FUN_00000d6c` @ `00000d6c`
- `00000d96`: `sub sp,#0x8` in `FUN_00000d94` @ `00000d94`
- `00000da2`: `ldr r2,[r0,#0x8]` in `FUN_00000d94` @ `00000d94`
- `00000dba`: `add sp,#0x8` in `FUN_00000d94` @ `00000d94`
- `00000dc8`: `ldr r5,[r0,#0x8]` in `FUN_00000dc0` @ `00000dc0`
- `00000dec`: `ldr r5,[r3,#0x8]` in `FUN_00000dc0` @ `00000dc0`
- `00000e5e`: `sub sp,#0x8` in `FUN_00000e5c` @ `00000e5c`
- `0000123e`: `adds r2,#0x8` in `<none>` @ `<none>`
- `0000125a`: `ldrb r2,[r4,#0x8]` in `<none>` @ `<none>`
- `000014da`: `cmp r3,#0x8` in `FUN_0000140c` @ `0000140c`
- `000015f0`: `ldrb r0,[r3,#0x8]` in `FUN_0000140c` @ `0000140c`
- `000016c6`: `asrs r1,r1,#0x8` in `FUN_00001618` @ `00001618`
- `000016ea`: `asrs r1,r1,#0x8` in `FUN_00001618` @ `00001618`
- `000016fe`: `movs r3,#0x8` in `FUN_000016f4` @ `000016f4`
- `000017a6`: `str r3,[r0,#0x8]` in `FUN_000017a0` @ `000017a0`
- `000017ba`: `ldr r2,[r3,#0x8]` in `FUN_000017ac` @ `000017ac`
- `000017c6`: `str r0,[r3,#0x8]` in `FUN_000017ac` @ `000017ac`
- `000017c8`: `str r2,[r0,#0x8]` in `FUN_000017ac` @ `000017ac`
- `000017ce`: `str r3,[r0,#0x8]` in `FUN_000017ac` @ `000017ac`
- `000017e6`: `ldr r4,[r4,#0x8]` in `FUN_000017d4` @ `000017d4`
- `0000186e`: `ldr r1,[r3,#0x8]` in `FUN_00001834` @ `00001834`
- `00001890`: `str r3,[r4,#0x8]` in `FUN_00001834` @ `00001834`
- `00001894`: `str r4,[r3,#0x8]` in `FUN_00001834` @ `00001834`
- `00001896`: `str r1,[r4,#0x8]` in `FUN_00001834` @ `00001834`
- `000019ca`: `ldr r1,[sp,#0x8]` in `FUN_0000190c` @ `0000190c`
- `000019ce`: `str r1,[sp,#0x8]` in `FUN_0000190c` @ `0000190c`
- `00001a16`: `cmp r3,#0x8` in `FUN_0000190c` @ `0000190c`
- `00001a4e`: `ldr r2,[sp,#0x8]` in `FUN_0000190c` @ `0000190c`
- `00001a52`: `str r2,[r7,#0x8]` in `FUN_0000190c` @ `0000190c`
- `00001a86`: `cmp r3,#0x8` in `FUN_0000190c` @ `0000190c`
- `00001bec`: `ldrh r0,[r1,#0x8]` in `FUN_00001b44` @ `00001b44`
- `00001c4c`: `cmp r2,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001d50`: `ldrh r0,[r1,#0x8]` in `FUN_00001b44` @ `00001b44`
- `00001dda`: `cmp r2,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001e44`: `asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001e5c`: `asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001e74`: `asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001e8c`: `asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001ea4`: `asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001ebc`: `asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001ed2`: `asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001eea`: `asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001ef6`: `cmp r2,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001f02`: `asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001f1a`: `asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `0000206c`: `movs r0,#0x8` in `FUN_00001b44` @ `00001b44`
- `000021ee`: `str r3,[sp,#0x8]` in `FUN_00002120` @ `00002120`
- `000021f4`: `ldr r2,[r4,#0x8]` in `FUN_00002120` @ `00002120`
- `000021fa`: `str r2,[r4,#0x8]` in `FUN_00002120` @ `00002120`
- `0000223e`: `ldr r3,[sp,#0x8]` in `FUN_00002120` @ `00002120`
- `00002260`: `ldr r3,[r4,#0x8]` in `FUN_00002120` @ `00002120`
- `0000226e`: `str r3,[r4,#0x8]` in `FUN_00002120` @ `00002120`
- `000024e8`: `strb r0,[r3,#0x8]` in `FUN_000024e0` @ `000024e0`
- `000027ca`: `str r3,[sp,#0x8]` in `FUN_00002544` @ `00002544`
- `000027fc`: `ldr r3,[sp,#0x8]` in `FUN_00002544` @ `00002544`
- `0000294c`: `ldrb r3,[r3,#0x8]` in `FUN_00002918` @ `00002918`
- `00002b32`: `ldrb r3,[r0,#0x8]` in `FUN_00002af0` @ `00002af0`
- `00002b6a`: `strh r7,[r1,#0x8]` in `FUN_00002af0` @ `00002af0`
- truncated

### `0x7f`

- `00000ef2`: `movs r7,#0x7f` in `FUN_00000eec` @ `00000eec`
- `00002af4`: `movs r4,#0x7f` in `FUN_00002af0` @ `00002af0`
- `000030c6`: `movs r0,#0x7f` in `FUN_0000308c` @ `0000308c`
- `00004af4`: `movs r3,#0x7f` in `FUN_00004abc` @ `00004abc`
- `000059ee`: `movs r1,#0x7f` in `FUN_00005808` @ `00005808`
- `00005bfa`: `movs r1,#0x7f` in `FUN_00005b00` @ `00005b00`
- `00005d60`: `movw r12,#0x7f` in `FUN_00005cb4` @ `00005cb4`
- `000206f0`: `movs r3,#0x7f` in `FUN_0002064c` @ `0002064c`
- `00021bba`: `movs r3,#0x7f` in `FUN_00021b70` @ `00021b70`
- `00042834`: `movs r1,#0x7f` in `FUN_000427a8` @ `000427a8`
- `0004284a`: `movs r0,#0x7f` in `FUN_000427a8` @ `000427a8`
- `000429ea`: `movs r2,#0x7f` in `FUN_000427a8` @ `000427a8`
- `00042d58`: `movs r1,#0x7f` in `<none>` @ `<none>`
- `00042d70`: `movs r0,#0x7f` in `<none>` @ `<none>`
- `00042e02`: `movs r2,#0x7f` in `<none>` @ `<none>`
- `00047094`: `cmp r3,#0x7f` in `FUN_00046e7c` @ `00046e7c`
- `000470d4`: `cmp r3,#0x7f` in `FUN_00046e7c` @ `00046e7c`
- `0004f65a`: `cmp r4,#0x7f` in `FUN_0004f64c` @ `0004f64c`
- `0004f718`: `cmp r1,#0x7f` in `FUN_0004f70c` @ `0004f70c`
- `0004f9a2`: `cmp r3,#0x7f` in `FUN_0004f978` @ `0004f978`
- `0004fd96`: `cmp r2,#0x7f` in `FUN_0004fd0c` @ `0004fd0c`
- `000508ec`: `movs r1,#0x7f` in `FUN_000508aa` @ `000508aa`
- `00050948`: `movs r1,#0x7f` in `FUN_00050912` @ `00050912`
- `00050b22`: `movs r1,#0x7f` in `FUN_00050b20` @ `00050b20`
- `00051a08`: `movs r1,#0x7f` in `FUN_000519d2` @ `000519d2`
- `0005c6d6`: `movs r2,#0x7f` in `FUN_0005c6d0` @ `0005c6d0`
- `0005e7b8`: `movs r1,#0x7f` in `FUN_0005e274` @ `0005e274`

### `0x80`

- `000014de`: `movs r3,#0x80` in `FUN_0000140c` @ `0000140c`
- `00001966`: `movs r5,#0x80` in `FUN_0000190c` @ `0000190c`
- `00004830`: `movs r2,#0x80` in `FUN_000047f0` @ `000047f0`
- `00004902`: `movs r0,#0x80` in `FUN_00004854` @ `00004854`
- `0000493c`: `movs r0,#0x80` in `FUN_00004854` @ `00004854`
- `0000497c`: `movs r1,#0x80` in `FUN_00004854` @ `00004854`
- `00004b26`: `adds r2,#0x80` in `FUN_00004abc` @ `00004abc`
- `00004e5c`: `movs r3,#0x80` in `FUN_00004e18` @ `00004e18`
- `00004ed6`: `adds r3,#0x80` in `FUN_00004e18` @ `00004e18`
- `00004fb4`: `movs r6,#0x80` in `FUN_00004f2c` @ `00004f2c`
- `00004fbc`: `movs r1,#0x80` in `FUN_00004f2c` @ `00004f2c`
- `000051aa`: `subs r2,#0x80` in `<none>` @ `<none>`
- `0000520c`: `subs r3,#0x80` in `<none>` @ `<none>`
- `00005286`: `subs r2,#0x80` in `FUN_00005244` @ `00005244`
- `000052e6`: `subs r3,#0x80` in `FUN_00005244` @ `00005244`
- `0000545e`: `subs r3,#0x80` in `<none>` @ `<none>`
- `000054c0`: `subs r2,#0x80` in `<none>` @ `<none>`
- `000056d0`: `subs r3,#0x80` in `FUN_0000557c` @ `0000557c`
- `00005734`: `subs r2,#0x80` in `FUN_0000557c` @ `0000557c`
- `00005854`: `subs r3,#0x80` in `FUN_00005808` @ `00005808`
- `00005932`: `subs r2,#0x80` in `FUN_00005808` @ `00005808`
- `00005a52`: `subs r2,#0x80` in `FUN_00005808` @ `00005808`
- `00005ac6`: `subs r3,#0x80` in `FUN_00005808` @ `00005808`
- `00005b3e`: `subs r3,#0x80` in `FUN_00005b00` @ `00005b00`
- `00005c52`: `subs r2,#0x80` in `FUN_00005b00` @ `00005b00`
- `00005cf6`: `subs r3,#0x80` in `FUN_00005cb4` @ `00005cb4`
- `00005dc8`: `subs r2,#0x80` in `FUN_00005cb4` @ `00005cb4`
- `00005e74`: `subs r3,#0x80` in `FUN_00005cb4` @ `00005cb4`
- `00005f28`: `subs r2,#0x80` in `FUN_00005cb4` @ `00005cb4`
- `00005fe4`: `subs r3,#0x80` in `FUN_00005cb4` @ `00005cb4`
- `0000603e`: `subs r3,#0x80` in `FUN_00005cb4` @ `00005cb4`
- `000060d2`: `cmp r0,#0x80` in `FUN_00006074` @ `00006074`
- `000060ec`: `movs r1,#0x80` in `FUN_00006074` @ `00006074`
- `0000611a`: `movs r1,#0x80` in `<none>` @ `<none>`
- `00006184`: `cmp r3,#0x80` in `<none>` @ `<none>`
- `0000618c`: `movs r3,#0x80` in `<none>` @ `<none>`
- `00006198`: `movs r3,#0x80` in `<none>` @ `<none>`
- `00006296`: `movs r2,#0x80` in `<none>` @ `<none>`
- `00006330`: `movs r2,#0x80` in `<none>` @ `<none>`
- `00006356`: `movs r1,#0x80` in `<none>` @ `<none>`
- `0000680c`: `movs r2,#0x80` in `<none>` @ `<none>`
- `000068a0`: `movs r2,#0x80` in `<none>` @ `<none>`
- `000068ac`: `movs r2,#0x80` in `<none>` @ `<none>`
- `000068b6`: `movs r2,#0x80` in `<none>` @ `<none>`
- `000087dc`: `movs r2,#0x80` in `FUN_00008764` @ `00008764`
- `00008b10`: `movs r3,#0x80` in `FUN_00008944` @ `00008944`
- `00008b4e`: `movs r0,#0x80` in `FUN_00008944` @ `00008944`
- `00008c06`: `movs r2,#0x80` in `FUN_00008944` @ `00008944`
- `00008dd0`: `movs r3,#0x80` in `FUN_00008944` @ `00008944`
- `00009146`: `movs r1,#0x80` in `FUN_0000912c` @ `0000912c`
- `000091a6`: `movs r3,#0x80` in `FUN_00009174` @ `00009174`
- `000094e4`: `movs r2,#0x80` in `FUN_00009210` @ `00009210`
- `00020fdc`: `movs r3,#0x80` in `FUN_00020f24` @ `00020f24`
- `0002100a`: `movs r3,#0x80` in `FUN_00020f24` @ `00020f24`
- `000210da`: `movs r2,#0x80` in `FUN_00020f24` @ `00020f24`
- `00021116`: `movs r2,#0x80` in `FUN_00020f24` @ `00020f24`
- `00021154`: `movs r2,#0x80` in `FUN_00020f24` @ `00020f24`
- `00021192`: `movs r2,#0x80` in `FUN_00020f24` @ `00020f24`
- `000211d0`: `movs r2,#0x80` in `FUN_00020f24` @ `00020f24`
- `0002120e`: `movs r2,#0x80` in `FUN_00020f24` @ `00020f24`
- `0002124c`: `movs r2,#0x80` in `FUN_00020f24` @ `00020f24`
- `0002128a`: `movs r2,#0x80` in `FUN_00020f24` @ `00020f24`
- `0002143c`: `movs r2,#0x80` in `FUN_00020f24` @ `00020f24`
- `00021b9c`: `cmp r6,#0x80` in `FUN_00021b70` @ `00021b70`
- `00021bb6`: `cmp r6,#0x80` in `FUN_00021b70` @ `00021b70`
- `00021bc0`: `adds r3,#0x80` in `FUN_00021b70` @ `00021b70`
- `0002654c`: `movs r3,#0x80` in `FUN_0002654c` @ `0002654c`
- `00026e28`: `movs r2,#0x80` in `FUN_00026d74` @ `00026d74`
- `00026e5a`: `movs r1,#0x80` in `FUN_00026d74` @ `00026d74`
- `00026f04`: `movs r7,#0x80` in `FUN_00026ecc` @ `00026ecc`
- `00026f3a`: `movs r1,#0x80` in `FUN_00026ecc` @ `00026ecc`
- `0002700e`: `movs r1,#0x80` in `FUN_00026fb4` @ `00026fb4`
- `00032536`: `movs r1,#0x80` in `FUN_00032498` @ `00032498`
- `00032732`: `movs r3,#0x80` in `FUN_000326f0` @ `000326f0`
- `00032768`: `movs r0,#0x80` in `FUN_000326f0` @ `000326f0`
- `00032778`: `movs r1,#0x80` in `FUN_000326f0` @ `000326f0`
- `000327f2`: `movs r3,#0x80` in `FUN_000326f0` @ `000326f0`
- `00032822`: `movs r3,#0x80` in `FUN_000326f0` @ `000326f0`
- `00032f66`: `movs r1,#0x80` in `FUN_00032f38` @ `00032f38`
- `00033198`: `movs r1,#0x80` in `FUN_000330c4` @ `000330c4`
- truncated

### `0xf0`

- `000010e4`: `cmp r0,#0xf0` in `FUN_000010a4` @ `000010a4`
- `00001142`: `cmp r0,#0xf0` in `FUN_000010a4` @ `000010a4`
- `00001150`: `cmp r0,#0xf0` in `FUN_000010a4` @ `000010a4`
- `000213d2`: `movs r3,#0xf0` in `FUN_00020f24` @ `00020f24`
- `000214fc`: `movs r3,#0xf0` in `FUN_00021484` @ `00021484`
- `00030928`: `movs r1,#0xf0` in `FUN_00030730` @ `00030730`
- `00031918`: `movs r1,#0xf0` in `FUN_000318b0` @ `000318b0`
- `00032b82`: `movs r2,#0xf0` in `FUN_00032b50` @ `00032b50`
- `0003577c`: `movs r3,#0xf0` in `FUN_00035738` @ `00035738`
- `000357bc`: `movs r2,#0xf0` in `FUN_00035738` @ `00035738`
- `00035faa`: `movs r3,#0xf0` in `FUN_00035f68` @ `00035f68`
- `0003638c`: `movs r1,#0xf0` in `FUN_00036334` @ `00036334`
- `0003688e`: `movs r0,#0xf0` in `FUN_0003682c` @ `0003682c`
- `000430ee`: `add r0,sp,#0xf0` in `FUN_00042fbc` @ `00042fbc`
- `00043114`: `add r3,sp,#0xf0` in `FUN_00042fbc` @ `00042fbc`
- `0004325e`: `add r0,sp,#0xf0` in `FUN_00042fbc` @ `00042fbc`
- `00046bf8`: `cmp r4,#0xf0` in `FUN_00046bb4` @ `00046bb4`
- `00046df4`: `subs r3,#0xf0` in `FUN_00046db4` @ `00046db4`
- `00050ad6`: `adds r3,#0xf0` in `FUN_00050aae` @ `00050aae`

### `0xf`

- `00002a6a`: `movt r3,#0xf` in `FUN_00002a60` @ `00002a60`
- `00002b76`: `ldrb r7,[r0,#0xf]` in `FUN_00002af0` @ `00002af0`
- `00002de6`: `strb r3,[r5,#0xf]` in `FUN_00002af0` @ `00002af0`
- `00003124`: `strb r5,[r4,#0xf]` in `FUN_0000308c` @ `0000308c`
- `00003294`: `strb r7,[r4,#0xf]` in `FUN_000031fc` @ `000031fc`
- `000034ce`: `ldrb r2,[r3,#0xf]` in `FUN_000031fc` @ `000031fc`
- `000049da`: `movs r0,#0xf` in `FUN_00004854` @ `00004854`
- `00005022`: `lsls r6,r6,#0xf` in `FUN_00004f2c` @ `00004f2c`
- `00005354`: `movt r2,#0xf` in `<none>` @ `<none>`
- `00005390`: `movt r2,#0xf` in `<none>` @ `<none>`
- `0000539c`: `movt r2,#0xf` in `<none>` @ `<none>`
- `000053aa`: `movt r3,#0xf` in `<none>` @ `<none>`
- `000053b6`: `movt r3,#0xf` in `<none>` @ `<none>`
- `0000550e`: `movt r2,#0xf` in `<none>` @ `<none>`
- `00005520`: `movt r2,#0xf` in `<none>` @ `<none>`
- `000055c6`: `movt r2,#0xf` in `FUN_0000557c` @ `0000557c`
- `00005602`: `movt r2,#0xf` in `FUN_0000557c` @ `0000557c`
- `0000560e`: `movt r2,#0xf` in `FUN_0000557c` @ `0000557c`
- `0000561c`: `movt r3,#0xf` in `FUN_0000557c` @ `0000557c`
- `00005628`: `movt r3,#0xf` in `FUN_0000557c` @ `0000557c`
- `00005782`: `movt r2,#0xf` in `FUN_0000557c` @ `0000557c`
- `00005794`: `movt r2,#0xf` in `FUN_0000557c` @ `0000557c`
- `00006834`: `strb r2,[r3,#0xf]` in `<none>` @ `<none>`
- `000085f4`: `dsb #0xf` in `FUN_000085dc` @ `000085dc`
- `000085f8`: `isb #0xf` in `FUN_000085dc` @ `000085dc`
- `00020f88`: `movs r0,#0xf` in `FUN_00020f24` @ `00020f24`
- `00021b84`: `movs r7,#0xf` in `FUN_00021b70` @ `00021b70`
- `00025f1a`: `movs r2,#0xf` in `FUN_00025f14` @ `00025f14`
- `00025f2a`: `strb r5,[r3,#0xf]` in `FUN_00025f14` @ `00025f14`
- `0002ddc4`: `cmp r1,#0xf` in `FUN_0002ddc4` @ `0002ddc4`
- `00031eb8`: `movs r2,#0xf` in `FUN_00031b10` @ `00031b10`
- `00034690`: `movs r1,#0xf` in `FUN_0003465c` @ `0003465c`
- `00037da0`: `movs r1,#0xf` in `FUN_00037b1c` @ `00037b1c`
- `0003cc88`: `movs r1,#0xf` in `FUN_0003c994` @ `0003c994`
- `0003d964`: `movs r1,#0xf` in `FUN_0003d600` @ `0003d600`
- `0003f18c`: `lsls r4,r4,#0xf` in `FUN_0003f156` @ `0003f156`
- `0003f2e2`: `movs r3,#0xf` in `FUN_0003f156` @ `0003f156`
- `0003f61e`: `movs r3,#0xf` in `FUN_0003f156` @ `0003f156`
- `0003f640`: `movs r3,#0xf` in `FUN_0003f156` @ `0003f156`
- `0003f676`: `movs r3,#0xf` in `FUN_0003f156` @ `0003f156`
- `0003f6fc`: `movs r3,#0xf` in `FUN_0003f156` @ `0003f156`
- `0003f70c`: `movs r3,#0xf` in `FUN_0003f156` @ `0003f156`
- `0003f87a`: `movs r0,#0xf` in `FUN_0003f874` @ `0003f874`
- `0003f9b2`: `subs r3,#0xf` in `FUN_0003f96c` @ `0003f96c`
- `00042128`: `cmp r4,#0xf` in `FUN_00042030` @ `00042030`
- `000422fc`: `asrs r3,r3,#0xf` in `FUN_00042030` @ `00042030`
- `00042452`: `cmp r4,#0xf` in `FUN_00042030` @ `00042030`
- `000424d8`: `asrs r0,r3,#0xf` in `FUN_00042030` @ `00042030`
- `000424da`: `movs r3,#0xf` in `FUN_00042030` @ `00042030`
- `000431b4`: `movs r3,#0xf` in `FUN_00042fbc` @ `00042fbc`
- `000433e4`: `cmp r7,#0xf` in `FUN_000433c8` @ `000433c8`
- `00046810`: `movs r3,#0xf` in `FUN_0004677c` @ `0004677c`
- `00046bea`: `movs r5,#0xf` in `FUN_00046bb4` @ `00046bb4`
- `00046dc6`: `movs r3,#0xf` in `FUN_00046db4` @ `00046db4`
- `000470a4`: `cmp r3,#0xf` in `FUN_00046e7c` @ `00046e7c`
- `000470e4`: `cmp r3,#0xf` in `FUN_00046e7c` @ `00046e7c`
- `00047834`: `strb r6,[r5,#0xf]` in `FUN_000477e8` @ `000477e8`
- `000486e2`: `strb r3,[r2,#0xf]` in `FUN_0004862c` @ `0004862c`
- `000486e6`: `movs r1,#0xf` in `FUN_0004862c` @ `0004862c`
- `00048712`: `strb r2,[r1,#0xf]` in `FUN_0004862c` @ `0004862c`
- `00048714`: `movs r1,#0xf` in `FUN_0004862c` @ `0004862c`
- `000487e4`: `movs r1,#0xf` in `FUN_00048774` @ `00048774`
- `000487e6`: `strb r3,[r2,#0xf]` in `FUN_00048774` @ `00048774`
- `00048804`: `movs r1,#0xf` in `FUN_00048774` @ `00048774`
- `00048806`: `strb r2,[r3,#0xf]` in `FUN_00048774` @ `00048774`
- `00048820`: `movs r1,#0xf` in `FUN_00048774` @ `00048774`
- `00048822`: `strb r3,[r2,#0xf]` in `FUN_00048774` @ `00048774`
- `0004883e`: `movs r1,#0xf` in `FUN_00048774` @ `00048774`
- `00048840`: `strb r3,[r2,#0xf]` in `FUN_00048774` @ `00048774`
- `0004885a`: `strb r2,[r1,#0xf]` in `FUN_00048774` @ `00048774`
- `0004885e`: `movs r1,#0xf` in `FUN_00048774` @ `00048774`
- `00048874`: `strb r2,[r1,#0xf]` in `FUN_00048774` @ `00048774`
- `00048878`: `movs r1,#0xf` in `FUN_00048774` @ `00048774`
- `00048888`: `movs r1,#0xf` in `FUN_00048774` @ `00048774`
- `0004888a`: `strb r3,[r2,#0xf]` in `FUN_00048774` @ `00048774`
- `0004891e`: `strb r1,[r0,#0xf]` in `FUN_0004890c` @ `0004890c`
- `00048946`: `movs r6,#0xf` in `FUN_00048938` @ `00048938`
- `0004a118`: `asrs r3,r3,#0xf` in `FUN_0004a084` @ `0004a084`
- `0004a134`: `asrs r4,r4,#0xf` in `FUN_0004a084` @ `0004a084`
- `0004d0fe`: `movs r3,#0xf` in `FUN_0004ce98` @ `0004ce98`
- truncated

### `0x20005cb6`

- no scalar operands found

### `0x20005cb8`

- no scalar operands found

## Ranked Decompiled Hits

### `FUN_0002064c` @ `0002064c` score `76`

- reasons: exact 8f-ish constant, status high-nibble test, channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing, little-endian F0 08 false positive

```c

undefined4 FUN_0002064c(void)

{
  undefined1 *puVar1;
  undefined2 *puVar2;
  byte bVar3;
  int iVar4;
  int iVar5;
  ushort uVar6;
  ushort local_1a;
  
  bVar3 = FUN_0002dc30(0x17);
  iVar4 = FUN_0002dc30(1);
  if (iVar4 == 4) {
    iVar4 = FUN_0002da70(bVar3,&local_1a);
    puVar1 = DAT_00020750;
    if (iVar4 != 0) {
      *DAT_00020750 = 2;
      puVar1[1] = (char)((local_1a & 0xfff) >> 0xb);
      *(undefined2 *)(puVar1 + 2) = *(undefined2 *)(*DAT_00020754 + (uint)bVar3 * 6 + 4);
      *(short *)(puVar1 + 4) = (short)((local_1a & 0x7ff) >> 4);
      FUN_00020264(0,5);
      FUN_000202ec(0,3,0x2b,3,bVar3 + 0x2b,local_1a >> 4);
    }
  }
  else {
    iVar4 = FUN_0002dc30(1);
    if ((iVar4 == 6) &&
       (iVar5 = FUN_0002da70(bVar3,&local_1a), iVar4 = DAT_0002075c, puVar2 = DAT_00020758,
       iVar5 != 0)) {
      uVar6 = local_1a >> 7 & 0x7f;
      *DAT_00020758 = 0x8f0;
      *(undefined1 *)(puVar2 + 1) = *(undefined1 *)(iVar4 + 1);
      *(char *)((int)puVar2 + 7) = (char)(local_1a & 0x7f);
      *(undefined1 *)(puVar2 + 2) = 0x2d;
      *(undefined1 *)((int)puVar2 + 3) = 0x10;
      *(byte *)((int)puVar2 + 5) = bVar3;
      *(char *)(puVar2 + 3) = (char)uVar6;
      *(undefined1 *)(puVar2 + 4) = 0xf7;
      FUN_0002654c(0,puVar2,9);
      *puVar2 = 0x8f0;
      *(undefined1 *)(puVar2 + 1) = *(undefined1 *)(iVar4 + 1);
      *(undefined1 *)((int)puVar2 + 3) = 0x10;
      *(undefined1 *)(puVar2 + 2) = 0x2d;
      *(byte *)((int)puVar2 + 5) = bVar3;
      puVar2[3] = (local_1a & 0x7f) << 8 | uVar6;
      *(undefined1 *)(puVar2 + 4) = 0xf7;
      FUN_0002654c(2,puVar2,9);
    }
  }
  return 0;
}
```

### `FUN_00003ce8` @ `00003ce8` score `63`

- reasons: possible USB-MIDI note-off CIN, channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing, known RAM/control state

```c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_00003ce8(uint *param_1,uint *param_2,undefined2 *param_3)

{
  bool bVar1;
  char cVar2;
  ushort uVar3;
  short sVar4;
  uint *puVar5;
  short sVar6;
  int iVar7;
  int *piVar8;
  int iVar9;
  ushort *puVar10;
  ushort uVar11;
  int extraout_r1;
  int extraout_r1_00;
  int extraout_r1_01;
  byte bVar12;
  int iVar13;
  int extraout_r2;
  int extraout_r2_00;
  uint uVar14;
  uint extraout_r2_01;
  uint extraout_r2_02;
  uint extraout_r2_03;
  int iVar15;
  uint extraout_r3;
  int extraout_r3_00;
  uint uVar16;
  uint uVar17;
  uint extraout_r3_01;
  uint extraout_r3_02;
  uint extraout_r3_03;
  uint uVar18;
  uint *puVar19;
  uint uVar20;
  uint uVar21;
  ushort *puVar22;
  short *psVar23;
  uint uVar24;
  int iVar25;
  uint *extraout_r12;
  uint *extraout_r12_00;
  uint *extraout_r12_01;
  uint *puVar26;
  undefined8 uVar27;
  ulonglong uVar28;
  uint *local_a8;
  uint *local_a4;
  undefined2 *local_9c;
  ushort auStack_78 [3];
  ushort auStack_72 [4];
  undefined2 uStack_6a;
  undefined2 uStack_68;
  undefined2 uStack_66;
  undefined2 uStack_64;
  undefined2 uStack_62;
  ushort auStack_60 [30];
  
  iVar7 = (**(code **)(((undefined4 *)param_1[0x1f])[2] + 8))
                    (*(undefined4 *)param_1[0x1f],auStack_60);
  if (iVar7 == 6000) {
    return 6000;
  }
  if (iVar7 == 0x1772) {
    return 0x1772;
  }
  piVar8 = (int *)param_1[0x1e];
  local_a8 = (uint *)(uint)*(byte *)(piVar8 + 4);
  if (local_a8 == (uint *)0x0) {
    iVar7 = FUN_00003e3a();
    return iVar7;
  }
  bVar12 = *(byte *)(*(int *)(param_1[0x1f] + 4) + 5);
  if (bVar12 == 1) {
    uVar24 = 0;
    uVar16 = param_1[6];
    uVar17 = 0;
    puVar19 = local_a8;
    puVar26 = param_1;
    puVar5 = (uint *)*piVar8;
    local_a4 = local_a8;
    goto LAB_000042d8;
  }
  if ((~bVar12 & 3) != 0) {
    iVar7 = FUN_00003e3a();
    return iVar7;
  }
  iVar15 = *piVar8;
  iVar7 = 0;
  uVar24 = 0;
  puVar22 = (ushort *)0xafc7;
  do {
    while( true ) {
      iVar13 = (uint)*(byte *)(iVar15 + iVar7) * 4;
      uVar16 = (uint)auStack_60[(uint)*(byte *)(iVar15 + iVar7) * 2 + 1];
      if (44999 < uVar16) {
        FUN_00004602();
        iVar7 = extraout_r1;
        iVar13 = extraout_r2;
        uVar16 = extraout_r3;
      }
      iVar13 = uVar16 - *(ushort *)((int)auStack_60 + iVar13);
      if (0xfffc < iVar13 + 0x7ffeU) {
        FUN_0000474a();
        iVar7 = extraout_r1_00;
        iVar13 = extraout_r3_00;
      }
      sVar4 = (short)iVar13;
      iVar13 = uVar24 * 2;
      psVar23 = (short *)(param_1[6] + iVar13);
      sVar6 = *(short *)(param_1[6] + iVar13);
      if (sVar6 != 0) break;
      *psVar23 = sVar4;
FUN_00003d5c:
      uVar24 = uVar24 + 1;
      iVar7 = iVar7 + 6;
      if (local_a8 <= (uint *)(uVar24 & 0xff)) goto LAB_00003e34;
    }
    iVar9 = (int)(short)(sVar6 - *(short *)(param_1[4] + iVar13));
    iVar25 = (uint)*(ushort *)(param_1[5] + iVar13) + iVar9;
    if (iVar25 + 0x7fffU < 0xffff) {
      if (sVar4 < iVar9) {
        FUN_00004636();
        iVar7 = extraout_r1_01;
        iVar13 = extraout_r2_00;
      }
      if ((int)(short)iVar25 < (int)sVar4) {
        *(undefined2 *)(param_1[7] + iVar13) = 0;
        puVar19 = (uint *)(param_1[8] + iVar13);
        uVar11 = *(ushort *)(param_1[8] + iVar13);
        piVar8 = (int *)0xfffc;
        local_a4 = param_1;
        if (uVar11 < *(byte *)((int)param_1 + 0x2d)) {
          *(ushort *)puVar19 = uVar11 + 1;
          uVar28 = FUN_00003dde();
          uVar16 = extraout_r2_03;
          uVar17 = extraout_r3_03;
          puVar26 = extraout_r12_01;
          goto LAB_0000475e;
        }
        if ((int)(uVar24 - 0x20) < 0) {
          uVar16 = 1 >> (0x20 - uVar24 & 0xff);
        }
        else {
          uVar16 = 1 << (uVar24 - 0x20 & 0xff);
        }
        param_1[3] = param_1[3] & ~uVar16;
        param_1[2] = param_1[2] & ~(1 << (uVar24 & 0xff));
        uVar28 = FUN_00003dde();
        uVar16 = extraout_r2_01;
        uVar17 = extraout_r3_01;
        puVar26 = extraout_r12;
LAB_00004582:
        puVar22 = (ushort *)((int)&SVCall + 1);
        *(undefined2 *)(puVar26[7] + (int)param_1) = 0;
/* ... truncated ... */
```

### `FUN_00003d5c` @ `00003d5c` score `63`

- reasons: possible USB-MIDI note-off CIN, channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing, known RAM/control state

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4
FUN_00003d5c(undefined4 param_1,int param_2,undefined4 param_3,undefined4 param_4,uint param_5,
            uint param_6,undefined4 param_7,undefined2 *param_8,int param_9,undefined4 *param_10)

{
  bool bVar1;
  char cVar2;
  short sVar3;
  ushort uVar4;
  short sVar5;
  int iVar6;
  int iVar7;
  ushort *puVar8;
  ushort uVar9;
  int extraout_r1;
  int extraout_r1_00;
  int extraout_r1_01;
  undefined2 *puVar10;
  byte bVar11;
  int iVar12;
  int extraout_r2;
  int extraout_r2_00;
  uint uVar13;
  int extraout_r2_01;
  int extraout_r2_02;
  int extraout_r2_03;
  undefined2 uVar14;
  uint uVar15;
  uint extraout_r3;
  int extraout_r3_00;
  undefined4 uVar16;
  uint extraout_r3_01;
  uint extraout_r3_02;
  uint extraout_r3_03;
  short *psVar17;
  uint uVar18;
  uint uVar19;
  uint *puVar20;
  uint uVar21;
  uint uVar22;
  int unaff_r5;
  uint unaff_r7;
  int iVar23;
  uint uVar24;
  ushort *unaff_r8;
  int iVar25;
  int *piVar26;
  uint unaff_r11;
  int extraout_r12;
  int extraout_r12_00;
  int extraout_r12_01;
  undefined8 uVar27;
  ulonglong uVar28;
  undefined4 in_stack_00000030;
  ushort uStack00000034;
  ushort uStack00000036;
  ushort uStack00000038;
  undefined2 uStack0000003a;
  undefined2 uStack0000003c;
  undefined2 uStack0000003e;
  undefined2 uStack00000040;
  undefined2 uStack00000042;
  undefined2 uStack00000044;
  undefined2 uStack00000046;
  
  uVar19 = param_6;
code_r0x00003d5c:
  unaff_r7 = unaff_r7 + 1;
  if ((unaff_r7 & 0xff) < param_5) {
    while( true ) {
      param_2 = param_2 + 6;
      iVar12 = (uint)*(byte *)(unaff_r5 + param_2) * 4;
      uVar15 = (uint)*(ushort *)(&stack0x0000004a + iVar12);
      if ((int)unaff_r8 < (int)uVar15) {
        FUN_00004602();
        param_2 = extraout_r1;
        iVar12 = extraout_r2;
        uVar15 = extraout_r3;
      }
      iVar12 = uVar15 - *(ushort *)(&stack0x00000048 + iVar12);
      if (unaff_r11 < iVar12 + 0x7ffeU) {
        FUN_0000474a();
        param_2 = extraout_r1_00;
        iVar12 = extraout_r3_00;
      }
      sVar5 = (short)iVar12;
      iVar12 = unaff_r7 * 2;
      psVar17 = (short *)(*(int *)(param_6 + 0x18) + iVar12);
      sVar3 = *(short *)(*(int *)(param_6 + 0x18) + iVar12);
      if (sVar3 == 0) break;
      iVar6 = (int)(short)(sVar3 - *(short *)(*(int *)(param_6 + 0x10) + iVar12));
      iVar25 = (uint)*(ushort *)(*(int *)(param_6 + 0x14) + iVar12) + iVar6;
      if (iVar25 + 0x7fffU < 0xffff) {
        if (sVar5 < iVar6) {
          FUN_00004636();
          param_2 = extraout_r1_01;
          iVar12 = extraout_r2_00;
        }
        if ((int)(short)iVar25 < (int)sVar5) {
          *(undefined2 *)(*(int *)(param_6 + 0x1c) + iVar12) = 0;
          puVar20 = (uint *)(*(int *)(param_6 + 0x20) + iVar12);
          uVar9 = *(ushort *)(*(int *)(param_6 + 0x20) + iVar12);
          if (*(byte *)(param_6 + 0x2d) <= uVar9) {
            if ((int)(unaff_r7 - 0x20) < 0) {
              uVar15 = 1 >> (0x20 - unaff_r7 & 0xff);
            }
            else {
              uVar15 = 1 << (unaff_r7 - 0x20 & 0xff);
            }
            *(uint *)(param_6 + 0xc) = *(uint *)(param_6 + 0xc) & ~uVar15;
            *(uint *)(param_6 + 8) = *(uint *)(param_6 + 8) & ~(1 << (unaff_r7 & 0xff));
            uVar28 = FUN_00003dde();
            iVar12 = extraout_r2_01;
            uVar15 = extraout_r3_01;
            iVar6 = extraout_r12;
            goto LAB_00004582;
          }
          *(ushort *)puVar20 = uVar9 + 1;
          uVar28 = FUN_00003dde();
          iVar12 = extraout_r2_03;
          uVar15 = extraout_r3_03;
          iVar6 = extraout_r12_01;
          goto LAB_0000475e;
        }
      }
      if (*(short *)(param_6 + 0x2e) == 0) goto code_r0x00003d5c;
      iVar6 = *(int *)(param_6 + 0x28);
      uVar27 = CONCAT44(param_2,unaff_r7 * 4 + *(int *)(param_6 + 0x24));
      if ((int)(unaff_r7 - 0x20) < 0) {
        uVar15 = *(uint *)(param_6 + 8) >> (unaff_r7 & 0xff) |
                 *(int *)(param_6 + 0xc) << (0x20 - unaff_r7 & 0xff);
      }
      else {
        uVar15 = *(uint *)(param_6 + 0xc) >> (unaff_r7 - 0x20 & 0xff);
      }
      if ((uVar15 & 1) == 0) {
        uVar27 = FUN_00004606();
      }
      param_2 = (int)((ulonglong)uVar27 >> 0x20);
      *(undefined4 *)uVar27 = 0;
      unaff_r7 = unaff_r7 + 1;
      *(undefined2 *)(iVar12 + iVar6) = 0;
      if (param_5 <= (unaff_r7 & 0xff)) goto LAB_00003e34;
    }
    *psVar17 = sVar5;
    goto code_r0x00003d5c;
  }
LAB_00003e34:
  uVar16 = *(undefined4 *)(param_6 + 0xc);
  *param_10 = *(undefined4 *)(param_6 + 8);
  param_10[1] = uVar16;
  if (*(char *)(param_9 + 0x11) != '\0') {
    param_6 = 0;
    param_5 = 0;
    do {
      piVar26 = (int *)(*(int *)(param_9 + 4) + param_6 * 8);
      uVar15 = param_5 * 5 & 0xff;
/* ... truncated ... */
```

### `FUN_00003dde` @ `00003dde` score `63`

- reasons: possible USB-MIDI note-off CIN, channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing, known RAM/control state

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4
FUN_00003dde(undefined4 param_1,int param_2,int param_3,undefined4 param_4,uint param_5,uint param_6
            ,undefined4 param_7,undefined2 *param_8,int param_9,undefined4 *param_10)

{
  bool bVar1;
  char cVar2;
  short sVar3;
  ushort uVar4;
  short sVar5;
  int iVar6;
  ushort *puVar7;
  int iVar8;
  uint uVar9;
  ushort uVar10;
  int extraout_r1;
  int extraout_r1_00;
  int extraout_r1_01;
  undefined2 *puVar11;
  uint uVar12;
  byte bVar13;
  int extraout_r2;
  int extraout_r2_00;
  uint uVar14;
  uint uVar15;
  int extraout_r2_01;
  int extraout_r2_02;
  int extraout_r2_03;
  undefined2 uVar16;
  uint extraout_r3;
  int extraout_r3_00;
  undefined4 uVar17;
  uint extraout_r3_01;
  uint extraout_r3_02;
  uint extraout_r3_03;
  short *psVar18;
  int iVar19;
  int iVar20;
  uint uVar21;
  uint *puVar22;
  int unaff_r5;
  uint unaff_r7;
  int iVar23;
  uint uVar24;
  ushort *unaff_r8;
  int *piVar25;
  uint unaff_r11;
  int extraout_r12;
  int extraout_r12_00;
  int extraout_r12_01;
  uint uVar26;
  undefined8 uVar27;
  ulonglong uVar28;
  undefined4 in_stack_00000030;
  ushort uStack00000034;
  ushort uStack00000036;
  ushort uStack00000038;
  undefined2 uStack0000003a;
  undefined2 uStack0000003c;
  undefined2 uStack0000003e;
  undefined2 uStack00000040;
  undefined2 uStack00000042;
  undefined2 uStack00000044;
  undefined2 uStack00000046;
  
  uVar21 = param_6;
  do {
    do {
      uVar12 = unaff_r7;
      if (*(short *)(param_6 + 0x2e) != 0) {
        iVar19 = *(int *)(param_6 + 0x28);
        uVar27 = CONCAT44(param_2,unaff_r7 * 4 + *(int *)(param_6 + 0x24));
        if ((int)(unaff_r7 - 0x20) < 0) {
          uVar15 = *(uint *)(param_6 + 8) >> (unaff_r7 & 0xff) |
                   *(int *)(param_6 + 0xc) << (0x20 - unaff_r7 & 0xff);
        }
        else {
          uVar15 = *(uint *)(param_6 + 0xc) >> (unaff_r7 - 0x20 & 0xff);
        }
        if ((uVar15 & 1) == 0) {
          uVar27 = FUN_00004606();
        }
        param_2 = (int)((ulonglong)uVar27 >> 0x20);
        *(undefined4 *)uVar27 = 0;
        *(undefined2 *)(param_3 + iVar19) = 0;
      }
      while( true ) {
        unaff_r7 = uVar12 + 1;
        if (param_5 <= (unaff_r7 & 0xff)) {
          uVar17 = *(undefined4 *)(param_6 + 0xc);
          *param_10 = *(undefined4 *)(param_6 + 8);
          param_10[1] = uVar17;
          if (*(char *)(param_9 + 0x11) == '\0') goto LAB_000040de;
          param_6 = 0;
          param_5 = 0;
          goto LAB_00003e62;
        }
        param_2 = param_2 + 6;
        iVar19 = (uint)*(byte *)(unaff_r5 + param_2) * 4;
        uVar15 = (uint)*(ushort *)(&stack0x0000004a + iVar19);
        if ((int)unaff_r8 < (int)uVar15) {
          FUN_00004602();
          param_2 = extraout_r1;
          iVar19 = extraout_r2;
          uVar15 = extraout_r3;
        }
        iVar19 = uVar15 - *(ushort *)(&stack0x00000048 + iVar19);
        if (unaff_r11 < iVar19 + 0x7ffeU) {
          FUN_0000474a();
          param_2 = extraout_r1_00;
          iVar19 = extraout_r3_00;
        }
        sVar5 = (short)iVar19;
        param_3 = unaff_r7 * 2;
        psVar18 = (short *)(*(int *)(param_6 + 0x18) + param_3);
        sVar3 = *(short *)(*(int *)(param_6 + 0x18) + param_3);
        if (sVar3 != 0) break;
        *psVar18 = sVar5;
        uVar12 = unaff_r7;
      }
      iVar19 = (int)(short)(sVar3 - *(short *)(*(int *)(param_6 + 0x10) + param_3));
      iVar8 = (uint)*(ushort *)(*(int *)(param_6 + 0x14) + param_3) + iVar19;
    } while (0xfffe < iVar8 + 0x7fffU);
    if (sVar5 < iVar19) {
      FUN_00004636();
      param_2 = extraout_r1_01;
      param_3 = extraout_r2_00;
    }
  } while ((int)sVar5 <= (int)(short)iVar8);
  *(undefined2 *)(*(int *)(param_6 + 0x1c) + param_3) = 0;
  puVar22 = (uint *)(*(int *)(param_6 + 0x20) + param_3);
  uVar10 = *(ushort *)(*(int *)(param_6 + 0x20) + param_3);
  if (*(byte *)(param_6 + 0x2d) <= uVar10) {
    if ((int)(uVar12 - 0x1f) < 0) {
      uVar12 = 1 >> (0x20 - unaff_r7 & 0xff);
    }
    else {
      uVar12 = 1 << (uVar12 - 0x1f & 0xff);
    }
    *(uint *)(param_6 + 0xc) = *(uint *)(param_6 + 0xc) & ~uVar12;
    *(uint *)(param_6 + 8) = *(uint *)(param_6 + 8) & ~(1 << (unaff_r7 & 0xff));
    uVar28 = FUN_00003dde();
    iVar19 = extraout_r2_01;
    uVar12 = extraout_r3_01;
    iVar8 = extraout_r12;
    goto LAB_00004582;
  }
  *(ushort *)puVar22 = uVar10 + 1;
  uVar28 = FUN_00003dde();
  iVar19 = extraout_r2_03;
  uVar12 = extraout_r3_03;
  iVar8 = extraout_r12_01;
LAB_0000475e:
  *(short *)puVar22 = (short)psVar18 + 1;
LAB_0000431e:
  uVar15 = uVar12;
  if (*(short *)(iVar8 + 0x2e) == 0) goto LAB_000042ca;
/* ... truncated ... */
```

### `FUN_00002544` @ `00002544` score `55`

- reasons: channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing, known RAM/control state

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_00002544(uint param_1,short *param_2,uint param_3)

{
  char cVar1;
  short sVar2;
  short sVar3;
  uint uVar4;
  short *psVar5;
  uint uVar6;
  uint uVar7;
  int iVar8;
  int iVar9;
  int iVar10;
  undefined1 uVar11;
  int iVar12;
  
  if (DAT_20005a9e == '\0') {
    return 0x21;
  }
  if (((1 < param_1) || (param_2 == (short *)0x0)) || (param_3 == 0)) {
    return 3;
  }
  uVar4 = -param_1 & 0x4a;
  iVar8 = param_3 * 2;
  FUN_00009578(uVar4 + 0x20005aac,param_2,iVar8);
  iVar12 = DAT_000028f4;
  uVar6 = 0;
  psVar5 = param_2;
  do {
    iVar9 = (int)((int)*psVar5 * (uint)(byte)(&DAT_20005b40)[uVar6 + (-param_1 & 0xc)]) >> 7;
    if (iVar9 < iVar12) {
      iVar9 = DAT_000028f4;
    }
    if (0x7fff < iVar9) {
      iVar9 = 0x7fff;
    }
    uVar6 = uVar6 + 1;
    *psVar5 = (short)iVar9;
    psVar5 = psVar5 + 1;
  } while ((uVar6 & 0xff) < param_3);
  FUN_00009578(uVar4 + 0x20005ac0,param_2,iVar8);
  if (DAT_20005aa0 == '\0') {
    FUN_00009578(uVar4 + 0x20005ad4,param_2,iVar8);
    if ((DAT_20005aa2 == '\0') || ((&DAT_20005a9c)[param_1] != '\0')) {
      *(undefined1 *)(param_1 * 0x4a + 0x20005ae8) = 0;
      sVar3 = *param_2;
      if (param_3 == 1) {
        uVar11 = 0;
        goto LAB_00002664;
      }
    }
    else {
      if (param_3 == 1) goto LAB_0000287c;
LAB_0000271a:
      sVar3 = *param_2;
      uVar4 = 0;
      uVar6 = 1;
      psVar5 = param_2;
      do {
        psVar5 = psVar5 + 1;
        if (sVar3 < *psVar5) {
          uVar4 = uVar6;
          sVar3 = *psVar5;
        }
        uVar6 = uVar6 + 1 & 0xff;
      } while (uVar6 < param_3);
      if (uVar4 == 0) {
        cVar1 = '\0';
        if ((short)(sVar3 - param_2[1]) < _DAT_20005aa4) {
          cVar1 = param_2[1] < _DAT_20005aa6;
        }
      }
      else {
        if (uVar4 != param_3 - 1) {
          *(undefined1 *)(param_1 * 0x4a + 0x20005ae8) = 0;
          sVar3 = *param_2;
          goto LAB_00002646;
        }
        cVar1 = '\0';
        if ((short)(sVar3 - param_2[param_3 - 2]) < _DAT_20005aa4) {
          cVar1 = (param_2[param_3 - 2] < _DAT_20005aa6) << 1;
        }
      }
      *(char *)(param_1 * 0x4a + 0x20005ae8) = cVar1;
      sVar3 = *param_2;
    }
  }
  else {
    uVar6 = (uint)DAT_20005aa1;
    if (param_3 == 1) {
      FUN_00009578(uVar4 + 0x20005ad4,param_2,2);
      if (DAT_20005aa2 == '\0') {
        *(undefined1 *)(param_1 * 0x4a + 0x20005ae8) = 0;
        sVar3 = *param_2;
        uVar11 = 0;
        goto LAB_00002664;
      }
LAB_0000287c:
      *(undefined1 *)(param_1 * 0x4a + 0x20005ae8) = 0;
      sVar3 = *param_2;
      uVar11 = 0;
      goto LAB_00002664;
    }
    uVar7 = 0;
    psVar5 = param_2;
    do {
      iVar12 = (int)*psVar5 + (int)psVar5[1];
      if (0 < iVar12) {
        sVar3 = (short)((int)(uVar6 * iVar12) / 200);
        if ((int)*psVar5 < (int)sVar3) {
          *psVar5 = sVar3;
        }
        if ((int)psVar5[1] < (int)sVar3) {
          psVar5[1] = sVar3;
        }
      }
      uVar7 = uVar7 + 1 & 0xff;
      psVar5 = psVar5 + 1;
    } while ((param_3 - 1 & 0xff) != uVar7);
    FUN_00009578(uVar4 + 0x20005ad4,param_2,iVar8);
    if (DAT_20005aa2 == '\0') {
      *(undefined1 *)(param_1 * 0x4a + 0x20005ae8) = 0;
      sVar3 = *param_2;
    }
    else {
      if ((&DAT_20005a9c)[param_1] == '\0') goto LAB_0000271a;
      *(undefined1 *)(param_1 * 0x4a + 0x20005ae8) = 0;
      sVar3 = *param_2;
    }
  }
LAB_00002646:
  uVar4 = 0;
  uVar6 = 1;
  psVar5 = param_2;
  do {
    psVar5 = psVar5 + 1;
    if (sVar3 < *psVar5) {
      uVar4 = uVar6;
      sVar3 = *psVar5;
    }
    uVar11 = (undefined1)uVar4;
    uVar6 = uVar6 + 1 & 0xff;
  } while (uVar6 < param_3);
LAB_00002664:
  *(short *)(param_1 * 0x4a + 0x20005af0) = sVar3;
  *(undefined1 *)(param_1 * 0x4a + 0x20005ae9) = uVar11;
  iVar9 = 0;
  iVar8 = 0x7fff;
  uVar4 = 0;
  iVar12 = DAT_000028f4;
  do {
    sVar3 = *param_2;
    iVar10 = (int)sVar3;
    sVar2 = sVar3;
    if (iVar8 < iVar10) {
      sVar2 = (short)iVar8;
    }
/* ... truncated ... */
```

### `FUN_00004854` @ `00004854` score `55`

- reasons: MIDI status-class constant, status high-nibble test, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_00004854(undefined1 *param_1,byte *param_2)

{
  byte bVar1;
  bool bVar2;
  byte bVar3;
  byte *pbVar4;
  byte bVar5;
  undefined4 uVar6;
  undefined4 *puVar7;
  undefined4 *puVar8;
  byte *pbVar9;
  int iVar10;
  uint uVar11;
  byte *pbVar12;
  
  bVar3 = *param_2;
  *(byte **)(param_1 + 0x1c) = param_2;
  *(uint *)(param_1 + 0x20) = (bVar3 + 0x2003800) * 0x20;
  *param_1 = 0;
  *(undefined4 *)(param_1 + 0x24) = *(undefined4 *)(param_2 + 0x14);
  uVar6 = *(undefined4 *)(param_2 + 0x18);
  *(undefined4 *)(param_1 + 0x28) = 0;
  *(undefined4 *)(param_1 + 0x2c) = uVar6;
  param_1[2] = param_1[2] & 0xfc | (param_2[1] == 0) + 1U;
  iVar10 = (int)(char)param_2[0xb];
  bVar3 = param_2[10];
  FUN_000085dc(iVar10);
  FUN_000084f4(iVar10);
  FUN_0000854c(iVar10,bVar3,param_1);
  iVar10 = (int)(char)param_2[5];
  bVar3 = param_2[4];
  FUN_000085dc(iVar10);
  FUN_000084f4(iVar10);
  FUN_0000854c(iVar10,bVar3,param_1);
  iVar10 = (int)(char)param_2[7];
  bVar3 = param_2[6];
  FUN_000085dc(iVar10);
  FUN_000084f4(iVar10);
  FUN_0000854c(iVar10,bVar3,param_1);
  iVar10 = (int)(char)param_2[9];
  bVar3 = param_2[8];
  FUN_000085dc(iVar10);
  FUN_000084f4(iVar10);
  FUN_0000854c(iVar10,bVar3,param_1);
  puVar8 = *(undefined4 **)(param_2 + 0xc);
  if (puVar8 != (undefined4 *)0x0) {
    puVar7 = *(undefined4 **)puVar8[1];
    *puVar7 = 0x80000;
    iVar10 = *(int *)(param_1 + 0x20);
    puVar7[1] = iVar10 + 5;
    if (*(char *)(*(int *)(param_1 + 0x1c) + 1) == '\0') {
      *(byte *)((int)puVar7 + 3) = *(byte *)((int)puVar7 + 3) & 0xcf | 0x10;
      puVar7[1] = iVar10 + 0x10;
    }
    iVar10 = (**(code **)puVar8[2])(*puVar8);
    if (iVar10 != 0) {
      return iVar10;
    }
  }
  puVar8 = *(undefined4 **)(param_2 + 0x10);
  if (puVar8 != (undefined4 *)0x0) {
    puVar7 = *(undefined4 **)puVar8[1];
    *puVar7 = 0x8000000;
    iVar10 = *(int *)(param_1 + 0x20);
    puVar7[2] = iVar10 + 3;
    if (*(char *)(*(int *)(param_1 + 0x1c) + 1) == '\0') {
      *(byte *)((int)puVar7 + 3) = *(byte *)((int)puVar7 + 3) & 0xcf | 0x10;
      puVar7[2] = iVar10 + 0xe;
    }
    iVar10 = (**(code **)puVar8[2])(*puVar8);
    if (iVar10 != 0) {
      puVar8 = *(undefined4 **)(param_2 + 0xc);
      if (puVar8 == (undefined4 *)0x0) {
        return iVar10;
      }
      (**(code **)(puVar8[2] + 0x20))(*puVar8);
      return iVar10;
    }
  }
  uVar11 = 0;
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    uVar11 = isIRQinterruptsEnabled();
  }
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    enableIRQinterrupts(1);
  }
  _DAT_40047000 = _DAT_40047000 & ~(0x80000000U >> *param_2);
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    enableIRQinterrupts((uVar11 & 1) == 1);
  }
  pbVar9 = *(byte **)(param_1 + 0x20);
  bVar3 = *param_2;
  pbVar9[2] = 0;
  pbVar9[4] = 0;
  pbVar9[9] = 0;
  pbVar9[10] = 0;
  pbVar9[0xb] = 0;
  pbVar9[0x1a] = 0;
  pbVar9[0x1b] = 0;
  if ((0x207U >> bVar3 & 1) != 0) {
    pbVar9[0x13] = 0x40;
  }
  pbVar9[0x1c] = 6;
  bVar3 = param_2[1];
  bVar5 = param_2[2];
  bVar1 = param_2[3];
  pbVar12 = *(byte **)(param_2 + 0x1c);
  if (*param_2 == 0) {
    *(short *)(pbVar9 + 0x14) = (short)DAT_00004ab8;
  }
  bVar5 = bVar5 << 4 | bVar1 << 3;
  if (bVar3 == 3) {
    bVar5 = bVar5 | 0x40;
    bVar3 = 0xf2;
  }
  else {
    bVar3 = (-(bVar3 == 0) & 0xf0U) - 0xe;
  }
  *pbVar9 = bVar5;
  pbVar9[6] = bVar3;
  pbVar9[0xd] = (pbVar12[0xc] & 1) << 1;
  bVar5 = pbVar12[1] << 7 | (pbVar12[2] & 1) << 5;
  bVar3 = *pbVar12;
  pbVar9[8] = 0;
  if (bVar3 - 2 < 2) {
    pbVar9[1] = 0xff;
    if (bVar3 == 2) {
      bVar5 = bVar5 | 0x10;
    }
    pbVar9[7] = bVar5;
  }
  else {
    pbVar4 = *(byte **)(pbVar12 + 4);
    pbVar9[7] = bVar5;
    bVar5 = pbVar4[1];
    pbVar9[1] = pbVar4[2];
    *pbVar9 = *pbVar9 & 0xfc | bVar5 & 3;
    pbVar9[0x12] = pbVar4[3];
    pbVar9[7] = *pbVar4 & 0x5c | pbVar9[7] & 0xa3;
  }
  *(undefined4 *)(param_1 + 0xc) = 0;
  *(undefined4 *)(param_1 + 0x10) = 0;
  *(undefined4 *)(param_1 + 0x14) = 0;
  *(undefined4 *)(param_1 + 0x18) = 0;
  FUN_00008598((int)*(char *)(*(int *)(param_1 + 0x1c) + 5));
  FUN_00008598((int)*(char *)(*(int *)(param_1 + 0x1c) + 0xb));
  FUN_00008598((int)*(char *)(*(int *)(param_1 + 0x1c) + 7));
  FUN_00008598((int)*(char *)(*(int *)(param_1 + 0x1c) + 9));
  *(byte *)(*(int *)(param_1 + 0x20) + 2) = bVar3 & 3 | 0x70;
  *(undefined2 *)(param_1 + 8) = *(undefined2 *)(pbVar12 + 10);
  *(undefined4 *)(param_1 + 4) = 0x53434955;
  return 0;
}
```

### `FUN_00001b44` @ `00001b44` score `53`

- reasons: MIDI status-class constant, channel low-nibble test, zero/nonzero tests, byte packet indexing, known RAM/control state

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00001b44(void)

{
  short sVar1;
  int iVar2;
  byte bVar3;
  uint uVar4;
  int iVar5;
  
  bVar3 = DAT_20005a56;
  if (DAT_20005a58 == '\0') {
    return;
  }
  uVar4 = (uint)_DAT_20005a54;
  if (DAT_20005a56 == 0) {
    if (0xff < (uVar4 + 1 & 0xffff)) {
      _DAT_20005a54 = 0;
      DAT_20005a57 = 1;
      return;
    }
    _DAT_20005a54 = (short)(uVar4 + 1);
    return;
  }
  if (DAT_20005a57 == '\0') {
    iVar2 = (int)_DAT_20006494;
    *(short *)(uVar4 * 2 + 0x2000462c) = _DAT_20006494;
    _DAT_20005a2c = iVar2 + _DAT_20005a2c;
    if (bVar3 != 1) {
      iVar2 = (int)_DAT_20006496;
      *(short *)((uVar4 + 0x100) * 2 + 0x2000462c) = _DAT_20006496;
      _DAT_20005a30 = iVar2 + _DAT_20005a30;
      if (bVar3 != 2) {
        iVar2 = (int)_DAT_20006498;
        *(short *)((uVar4 + 0x200) * 2 + 0x2000462c) = _DAT_20006498;
        _DAT_20005a34 = iVar2 + _DAT_20005a34;
        if (bVar3 != 3) {
          iVar2 = (int)_DAT_2000649a;
          *(short *)((uVar4 + 0x300) * 2 + 0x2000462c) = _DAT_2000649a;
          _DAT_20005a38 = iVar2 + _DAT_20005a38;
          if (bVar3 != 4) {
            iVar2 = (int)_DAT_2000649c;
            *(short *)((uVar4 + 0x400) * 2 + 0x2000462c) = _DAT_2000649c;
            _DAT_20005a3c = iVar2 + _DAT_20005a3c;
            if (bVar3 != 5) {
              iVar2 = (int)_DAT_2000649e;
              *(short *)((uVar4 + 0x500) * 2 + 0x2000462c) = _DAT_2000649e;
              _DAT_20005a40 = iVar2 + _DAT_20005a40;
              if (bVar3 != 6) {
                iVar2 = (int)_DAT_200064a0;
                *(short *)((uVar4 + 0x600) * 2 + 0x2000462c) = _DAT_200064a0;
                _DAT_20005a44 = iVar2 + _DAT_20005a44;
                if (bVar3 != 7) {
                  iVar2 = (int)_DAT_200064a2;
                  *(short *)((uVar4 + 0x700) * 2 + 0x2000462c) = _DAT_200064a2;
                  _DAT_20005a48 = iVar2 + _DAT_20005a48;
                  if (bVar3 != 8) {
                    iVar2 = (int)_DAT_200064a4;
                    *(short *)((uVar4 + 0x800) * 2 + 0x2000462c) = _DAT_200064a4;
                    _DAT_20005a4c = iVar2 + _DAT_20005a4c;
                    if (bVar3 != 9) {
                      iVar2 = (int)_DAT_200064a6;
                      *(short *)((uVar4 + 0x900) * 2 + 0x2000462c) = _DAT_200064a6;
                      _DAT_20005a50 = iVar2 + _DAT_20005a50;
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    if ((uVar4 + 1 & 0xffff) < 0x100) {
      _DAT_20005a54 = (short)(uVar4 + 1);
      return;
    }
  }
  else {
    sVar1 = *(short *)(uVar4 * 2 + 0x2000462c);
    iVar2 = (int)_DAT_20006494;
    *(short *)(uVar4 * 2 + 0x2000462c) = _DAT_20006494;
    _DAT_20005a2c = iVar2 + (_DAT_20005a2c - sVar1);
    if (bVar3 != 1) {
      iVar5 = (uVar4 + 0x100) * 2;
      sVar1 = *(short *)(iVar5 + 0x2000462c);
      iVar2 = (int)_DAT_20006496;
      *(short *)(iVar5 + 0x2000462c) = _DAT_20006496;
      _DAT_20005a30 = iVar2 + (_DAT_20005a30 - sVar1);
      if (bVar3 != 2) {
        iVar5 = (uVar4 + 0x200) * 2;
        sVar1 = *(short *)(iVar5 + 0x2000462c);
        iVar2 = (int)_DAT_20006498;
        *(short *)(iVar5 + 0x2000462c) = _DAT_20006498;
        _DAT_20005a34 = iVar2 + (_DAT_20005a34 - sVar1);
        if (bVar3 != 3) {
          iVar5 = (uVar4 + 0x300) * 2;
          sVar1 = *(short *)(iVar5 + 0x2000462c);
          iVar2 = (int)_DAT_2000649a;
          *(short *)(iVar5 + 0x2000462c) = _DAT_2000649a;
          _DAT_20005a38 = iVar2 + (_DAT_20005a38 - sVar1);
          if (bVar3 != 4) {
            iVar5 = (uVar4 + 0x400) * 2;
            sVar1 = *(short *)(iVar5 + 0x2000462c);
            iVar2 = (int)_DAT_2000649c;
            *(short *)(iVar5 + 0x2000462c) = _DAT_2000649c;
            _DAT_20005a3c = iVar2 + (_DAT_20005a3c - sVar1);
            if (bVar3 != 5) {
              iVar5 = (uVar4 + 0x500) * 2;
              sVar1 = *(short *)(iVar5 + 0x2000462c);
              iVar2 = (int)_DAT_2000649e;
              *(short *)(iVar5 + 0x2000462c) = _DAT_2000649e;
              _DAT_20005a40 = iVar2 + (_DAT_20005a40 - sVar1);
              if (bVar3 != 6) {
                iVar5 = (uVar4 + 0x600) * 2;
                sVar1 = *(short *)(iVar5 + 0x2000462c);
                iVar2 = (int)_DAT_200064a0;
                *(short *)(iVar5 + 0x2000462c) = _DAT_200064a0;
                _DAT_20005a44 = iVar2 + (_DAT_20005a44 - sVar1);
                if (bVar3 != 7) {
                  iVar5 = (uVar4 + 0x700) * 2;
                  sVar1 = *(short *)(iVar5 + 0x2000462c);
                  iVar2 = (int)_DAT_200064a2;
                  *(short *)(iVar5 + 0x2000462c) = _DAT_200064a2;
                  _DAT_20005a48 = iVar2 + (_DAT_20005a48 - sVar1);
                  if (bVar3 != 8) {
                    iVar5 = (uVar4 + 0x800) * 2;
                    sVar1 = *(short *)(iVar5 + 0x2000462c);
                    iVar2 = (int)_DAT_200064a4;
                    *(short *)(iVar5 + 0x2000462c) = _DAT_200064a4;
                    _DAT_20005a4c = iVar2 + (_DAT_20005a4c - sVar1);
                    if (bVar3 != 9) {
                      iVar2 = (uVar4 + 0x900) * 2;
                      sVar1 = *(short *)(iVar2 + 0x2000462c);
                      iVar5 = (int)_DAT_200064a6;
                      *(short *)(iVar2 + 0x2000462c) = _DAT_200064a6;
                      _DAT_20005a50 = iVar5 + (_DAT_20005a50 - sVar1);
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    _DAT_20005a54 = (ushort)(uVar4 + 1);
    if ((uVar4 + 1 & 0xffff) < 0x100) goto LAB_00001e3e;
  }
  _DAT_20005a54 = 0;
  DAT_20005a57 = '\x01';
LAB_00001e3e:
  if ((short)((uint)_DAT_20005a2c >> 8) < -0x1e) {
    FUN_00001ac8(0);
    FUN_00009568(0x2000462c,0,0x200);
    _DAT_20005a2c = 0;
    bVar3 = DAT_20005a56;
  }
/* ... truncated ... */
```

### `FUN_00003e3a` @ `00003e3a` score `53`

- reasons: possible USB-MIDI note-off CIN, channel low-nibble test, zero/nonzero tests, byte packet indexing, known RAM/control state

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_00003e3a(int param_1)

{
  bool bVar1;
  char cVar2;
  short sVar3;
  short sVar4;
  int iVar5;
  int iVar6;
  uint uVar7;
  ushort uVar8;
  undefined2 *puVar9;
  uint uVar10;
  byte bVar11;
  short *psVar12;
  uint uVar13;
  uint uVar14;
  undefined2 uVar15;
  undefined4 uVar16;
  uint uVar17;
  int unaff_r4;
  int iVar18;
  undefined4 *unaff_r6;
  int iVar19;
  int iVar20;
  uint uVar21;
  int *piVar22;
  uint uVar23;
  uint uStack00000000;
  uint uStack00000004;
  undefined2 *in_stack_0000000c;
  undefined4 in_stack_00000030;
  ushort uStack00000034;
  ushort uStack00000036;
  ushort uStack00000038;
  undefined2 uStack0000003a;
  undefined2 uStack0000003c;
  undefined2 uStack0000003e;
  undefined2 uStack00000040;
  undefined2 uStack00000042;
  undefined2 uStack00000044;
  undefined2 uStack00000046;
  
  uVar16 = *(undefined4 *)(unaff_r4 + 0xc);
  *unaff_r6 = *(undefined4 *)(unaff_r4 + 8);
  unaff_r6[1] = uVar16;
  if (*(char *)(param_1 + 0x11) != '\0') {
    uStack00000004 = 0;
    uStack00000000 = 0;
    do {
      piVar22 = (int *)(*(int *)(param_1 + 4) + uStack00000004 * 8);
      uVar10 = uStack00000000 * 5 & 0xff;
      if ((char)piVar22[1] != '\0') {
        uVar7 = 0;
        psVar12 = (short *)&stack0x00000034;
        uVar14 = uVar10;
        do {
          iVar19 = *piVar22;
          sVar3 = *(short *)(&stack0x00000048 + (uint)*(byte *)(iVar19 + uVar7) * 2);
          *(short *)(uVar14 * 2 + 0x200064a8) = sVar3;
          sVar4 = FUN_00001aa8(*(undefined1 *)(iVar19 + uVar7));
          sVar3 = sVar3 - sVar4;
          *(short *)(&DAT_20006494 + uVar14 * 2) = sVar3;
          *psVar12 = sVar3;
          uVar7 = uVar7 + 1;
          uVar14 = uVar14 + 1;
          psVar12 = psVar12 + 1;
        } while ((uVar7 & 0xff) < (uint)*(byte *)(piVar22 + 1));
      }
      iVar19 = FUN_00002544(uStack00000000,&stack0x00000034);
      uVar14 = uStack00000004;
      uVar7 = (uint)*(byte *)(piVar22 + 1);
      if (((uVar7 == 0) || (*(ushort *)(uVar10 * 2 + 0x20006480) = uStack00000034, uVar7 == 1)) ||
         (*(ushort *)((uVar10 + 1) * 2 + 0x20006480) = uStack00000036, uVar7 == 2)) {
        if (iVar19 == 0) goto LAB_000043a4;
        uVar15 = *(undefined2 *)(*(int *)(unaff_r4 + 0x38) + uStack00000004 * 2);
      }
      else {
        *(ushort *)((uVar10 + 2) * 2 + 0x20006480) = uStack00000038;
        if ((((uVar7 == 3) ||
             (*(undefined2 *)((uVar10 + 3) * 2 + 0x20006480) = uStack0000003a, uVar7 == 4)) ||
            ((*(undefined2 *)((uVar10 + 4) * 2 + 0x20006480) = uStack0000003c, uVar7 == 5 ||
             ((*(undefined2 *)((uVar10 + 5) * 2 + 0x20006480) = uStack0000003e, uVar7 == 6 ||
              (*(undefined2 *)((uVar10 + 6) * 2 + 0x20006480) = uStack00000040, uVar7 == 7)))))) ||
           ((*(undefined2 *)((uVar10 + 7) * 2 + 0x20006480) = uStack00000042, uVar7 == 8 ||
            (*(undefined2 *)((uVar10 + 8) * 2 + 0x20006480) = uStack00000044, uVar7 == 9)))) {
          if (iVar19 != 0) goto LAB_00003fa6;
LAB_000043a4:
          iVar18 = uStack00000004 * 2;
          iVar6 = FUN_00002480(uStack00000000);
          if ((iVar6 != 0) && (*(char *)(iVar6 + 0x3c) != '\0')) {
            *(undefined2 *)(*(int *)(unaff_r4 + 0x38) + iVar18) = 0xffff;
          }
          uVar7 = (uint)*(byte *)(piVar22 + 1);
          if (2 < uVar7) goto LAB_00003fa6;
          in_stack_00000030._2_2_ = *(undefined2 *)(*(int *)(unaff_r4 + 0x38) + iVar18);
        }
        else {
          *(undefined2 *)((uVar10 + 9) * 2 + 0x20006480) = uStack00000046;
          if (iVar19 == 0) goto LAB_000043a4;
LAB_00003fa6:
          iVar20 = uVar14 * 2;
          iVar6 = (int)(short)uStack00000034;
          iVar18 = 0;
          uVar10 = 0;
          psVar12 = (short *)&stack0x00000034;
          do {
            iVar5 = (int)*psVar12;
            iVar18 = iVar18 + iVar5;
            if (iVar5 < iVar6) {
              iVar6 = iVar5;
            }
            uVar10 = uVar10 + 1 & 0xff;
            psVar12 = psVar12 + 1;
          } while (uVar10 < uVar7);
          uVar23 = (uint)*(ushort *)(*(int *)(unaff_r4 + 0x3c) + iVar20);
          uVar10 = FUN_0000099c(uStack00000000);
          if (*(short *)(*(int *)(unaff_r4 + 0x38) + iVar20) == -1) {
            uVar23 = uVar23 + uVar10;
            if (0xffff < uVar23) {
              uVar23 = 0xffff;
            }
          }
          else {
            uVar23 = uVar23 - uVar10 & -(uint)(uVar10 < uVar23);
          }
          if ((int)uVar23 < (int)(iVar18 - uVar7 * iVar6)) {
            uVar17 = uVar7 - 1;
            uVar23 = (uint)(short)uStack00000034;
            psVar12 = (short *)((int)&stack0x00000034 + 2);
            uVar21 = 0;
            uVar10 = 1;
            do {
              uVar13 = uVar21;
              if ((int)uVar23 < (int)*psVar12) {
                uVar21 = uVar10 & 0xff;
                uVar13 = uVar10;
                uVar23 = (int)*psVar12;
              }
              psVar12 = psVar12 + 1;
              bVar1 = (int)uVar10 < (int)uVar17;
              uVar10 = uVar10 + 1;
            } while (bVar1);
            if (uVar21 == 0) {
              uVar13 = (uint)uStack00000034 - (uint)uStack00000038 & 0xffff;
              uVar10 = (uint)uStack00000034 - (uint)uStack00000036 & 0xffff;
            }
            else if (uVar17 == uVar21) {
              iVar6 = (uVar7 + DAT_000047ec) * 2;
              uVar13 = (uint)*(ushort *)((int)&stack0x00000034 + iVar6) -
                       (uint)*(ushort *)((int)&stack0x00000030 + iVar6 + 2) & 0xffff;
              uVar10 = (uint)*(ushort *)((int)&stack0x00000034 + iVar6) -
                       (uint)*(ushort *)((int)&stack0x00000030 + iVar6) & 0xffff;
            }
            else {
              iVar6 = (uVar13 + DAT_000042c4) * 2;
              uVar13 = (uVar23 & 0xffff) - (uint)*(ushort *)((int)&stack0x00000034 + iVar6) & 0xffff
/* ... truncated ... */
```

### `FUN_0003ab58` @ `0003ab58` score `48`

- reasons: exact 8f-ish constant, MIDI status-class constant, zero/nonzero tests

```c

void FUN_0003ab58(int param_1,undefined1 *param_2)

{
  code *pcVar1;
  int iVar2;
  undefined1 auStack_20 [20];
  
  if (param_1 == 0) {
    FUN_000458e8(3,DAT_0003abd8,0x8f,DAT_0003abd0,DAT_0003abd4,DAT_0003abcc,DAT_0003abc8);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar2 = *(int *)(param_1 + 0x18);
  if (iVar2 != 0) {
    pcVar1 = *(code **)(iVar2 + 0x10);
    if (pcVar1 != (code *)0x0) {
      if (param_2 == (undefined1 *)0x0) {
        FUN_00044064(auStack_20,0,0,*(ushort *)(param_1 + 4) - 1,*(ushort *)(param_1 + 6) - 1);
        pcVar1 = *(code **)(iVar2 + 0x10);
        param_2 = auStack_20;
      }
      (*pcVar1)(param_1,param_2);
    }
    return;
  }
  FUN_000458e8(3,DAT_0003abd8,0x90,DAT_0003abd0,DAT_0003abd4,DAT_0003abdc,DAT_0003abc8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

### `FUN_00030730` @ `00030730` score `47`

- reasons: status high-nibble test, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

void FUN_00030730(int param_1,uint param_2)

{
  uint uVar1;
  int iVar2;
  uint uVar3;
  uint uVar4;
  undefined4 *puVar5;
  uint *puVar6;
  int iVar7;
  int iVar8;
  uint uVar9;
  uint uVar10;
  undefined4 *puVar11;
  char *pcVar12;
  int iVar13;
  undefined2 *puVar14;
  char cVar15;
  uint uVar16;
  
  uVar9 = (uint)*(ushort *)(param_1 + 0x28);
  if (uVar9 != param_2) {
    uVar1 = FUN_00035b60(param_1,uVar9,param_2);
    if (uVar1 == 0) {
      *(short *)(param_1 + 0x28) = (short)param_2;
    }
    else {
      FUN_00033298(param_1);
      *(short *)(param_1 + 0x28) = (short)param_2;
      FUN_00035e90(param_1);
      iVar2 = FUN_0004beb8(0x280);
      uVar10 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
      if (uVar10 != 0) {
        iVar7 = 0;
        iVar8 = 0;
        puVar11 = *(undefined4 **)(param_1 + 0xc);
LAB_000307a4:
        uVar3 = puVar11[1];
        if (((~param_2 & uVar3 & 0xffff) == 0) && ((*(byte *)((int)puVar11 + 7) & 2) == 0)) {
          uVar16 = (uint)*(byte *)((undefined4 *)*puVar11 + 2);
          pcVar12 = *(char **)*puVar11;
          if (uVar16 == 0xff) {
            for (; *pcVar12 != '\0'; pcVar12 = pcVar12 + 8) {
              if (*pcVar12 == 'h') {
                puVar5 = *(undefined4 **)(pcVar12 + 4);
                goto LAB_000307f4;
              }
            }
          }
          else if (uVar16 != 0) {
            uVar4 = 0;
LAB_000307e6:
            if (pcVar12[uVar4 + uVar16 * 4] != 'h') goto LAB_000307de;
            puVar5 = *(undefined4 **)(pcVar12 + uVar4 * 4);
LAB_000307f4:
            pcVar12 = (char *)*puVar5;
            cVar15 = *pcVar12;
            if (cVar15 == '\0') goto LAB_00030878;
            if (iVar7 == 0) goto LAB_000308b6;
            do {
              while( true ) {
                iVar13 = 0;
                puVar6 = (uint *)(iVar2 + 4);
                while ((((char)puVar6[1] != cVar15 || ((*puVar6 & 0xff0000) != (uVar3 & 0xff0000)))
                       || ((*puVar6 & 0xffff) < (uVar3 & 0xffff)))) {
                  iVar13 = iVar13 + 1;
                  puVar6 = puVar6 + 5;
                  if (iVar13 == iVar7) goto LAB_000308b6;
                }
                if (iVar7 == iVar13) break;
                pcVar12 = pcVar12 + 1;
                cVar15 = *pcVar12;
                if (cVar15 == '\0') goto LAB_0003085c;
              }
LAB_000308b6:
              puVar14 = (undefined2 *)(iVar2 + iVar7 * 0x14);
              iVar7 = iVar7 + 1;
              *puVar14 = (short)puVar5[3];
              puVar14[1] = (short)puVar5[4];
              *(undefined4 *)(puVar14 + 6) = puVar5[2];
              *(char *)(puVar14 + 4) = *pcVar12;
              *(undefined4 *)(puVar14 + 8) = puVar5[1];
              *(uint *)(puVar14 + 2) = uVar3 & 0xffffff;
              pcVar12 = pcVar12 + 1;
              cVar15 = *pcVar12;
            } while ((cVar15 != '\0') && (iVar7 != 0x20));
LAB_0003085c:
            if (uVar10 <= iVar8 + 1U) goto LAB_00030880;
            if (iVar7 == 0x20) goto LAB_000308fc;
            goto LAB_00030868;
          }
        }
LAB_00030878:
        if (iVar8 + 1U < uVar10) goto LAB_00030868;
        goto LAB_00030880;
      }
LAB_00030886:
      FUN_0004bedc(iVar2);
      if ((uVar1 & 0xfd) == 1) {
        FUN_000360c0(param_1,0xf0000,0xff);
      }
      else if (uVar1 == 2) {
        FUN_00033298(param_1);
        FUN_000323bc(param_1);
      }
    }
  }
  return;
LAB_000307de:
  uVar4 = uVar4 + 1;
  if (uVar16 <= uVar4) goto LAB_000308ee;
  goto LAB_000307e6;
LAB_000308ee:
  if (uVar10 <= iVar8 + 1U) {
LAB_00030880:
    if (iVar7 != 0) {
LAB_000308fc:
      iVar8 = iVar2;
      do {
        iVar13 = iVar8 + 0x14;
        FUN_00036498(param_1,*(uint *)(iVar8 + 4) & 0xff0000,uVar9,param_2,iVar8);
        iVar8 = iVar13;
      } while (iVar2 + iVar7 * 0x14 != iVar13);
    }
    goto LAB_00030886;
  }
LAB_00030868:
  iVar8 = iVar8 + 1;
  puVar11 = puVar11 + 2;
  goto LAB_000307a4;
}
```

### `FUN_00031790` @ `00031790` score `47`

- reasons: status high-nibble test, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

int * FUN_00031790(int *param_1,int param_2)

{
  short sVar1;
  uint uVar2;
  int *piVar3;
  undefined4 uVar4;
  int iVar5;
  int iVar6;
  uint uVar7;
  int *piVar8;
  int iVar9;
  undefined4 *puVar10;
  
  piVar3 = param_1;
  if (param_1 == (int *)0x0) {
    uVar2 = 0;
  }
  else {
    do {
      uVar7 = piVar3[8];
      uVar2 = uVar7 & DAT_00031890;
      if ((uVar7 & DAT_00031890) != 0) {
        uVar2 = (uVar7 & 0xfffff) >> 4;
        break;
      }
      piVar3 = (int *)*piVar3;
    } while (piVar3 != (int *)0x0);
  }
  piVar3 = (int *)FUN_0004beb8(uVar2);
  if (piVar3 != (int *)0x0) {
    *piVar3 = (int)param_1;
    piVar3[1] = param_2;
    if (param_2 != 0) {
      puVar10 = *(undefined4 **)(param_2 + 8);
      if (puVar10 == (undefined4 *)0x0) {
        FUN_0003167c(param_2);
        puVar10 = *(undefined4 **)(param_2 + 8);
      }
      sVar1 = *(short *)(puVar10 + 0xc);
      *(ushort *)(puVar10 + 0xc) = sVar1 + 1U;
      uVar4 = FUN_0004bef4(*puVar10,(uint)(ushort)(sVar1 + 1U) << 2);
      piVar8 = *(int **)(param_2 + 8);
      *puVar10 = uVar4;
      *(int **)(((uint)*(ushort *)(piVar8 + 0xc) + DAT_00031894) * 4 + *piVar8) = piVar3;
      return piVar3;
    }
    iVar5 = FUN_00039020();
    if (iVar5 != 0) {
      if (*(int *)(iVar5 + 700) == 0) {
        iVar6 = 4;
        *(undefined4 *)(iVar5 + 0x2d8) = 0;
      }
      else {
        iVar6 = (*(int *)(iVar5 + 0x2d8) + 1) * 4;
      }
      iVar6 = FUN_0004bef4(*(int *)(iVar5 + 700),iVar6);
      if (iVar6 != 0) {
        iVar9 = *(int *)(iVar5 + 0x2d8);
        *(int *)(iVar5 + 0x2d8) = iVar9 + 1;
        *(int *)(iVar5 + 700) = iVar6;
        *(int **)(iVar6 + iVar9 * 4) = piVar3;
        piVar3[5] = 0;
        piVar3[6] = 0;
        iVar5 = FUN_00039048(0);
        piVar3[7] = iVar5 + -1;
        iVar5 = FUN_00039070(0);
        piVar3[8] = iVar5 + -1;
        return piVar3;
      }
      FUN_000458e8(3,DAT_000318a0,0x47,DAT_0003189c,DAT_000318ac,DAT_000318a8,DAT_000318a4);
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    FUN_000458e8(2,DAT_000318a0,0x3d,DAT_0003189c,DAT_00031898);
    FUN_0004bedc(piVar3);
  }
  return (int *)0x0;
}
```

### `FUN_00031b10` @ `00031b10` score `47`

- reasons: status high-nibble test, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

void FUN_00031b10(undefined4 param_1,int param_2,undefined4 *param_3)

{
  undefined1 uVar1;
  byte bVar2;
  undefined3 uVar3;
  undefined4 uVar4;
  uint uVar5;
  int iVar6;
  uint uVar7;
  
  *param_3 = param_1;
  param_3[1] = param_2;
  if (param_3[4] == 0) {
    uVar7 = FUN_00035de8();
    if (param_2 == 0) goto LAB_00031b32;
  }
  else {
    uVar7 = (uint)*(byte *)(param_3[4] + 0x38);
    if (param_2 == 0) goto LAB_00031b32;
    uVar5 = FUN_00035ab8(param_1,param_2,0x62);
    uVar7 = (uVar5 & 0xff) * uVar7 >> 8;
  }
  if (uVar7 < 3) {
    *(undefined1 *)(param_3 + 8) = 0;
    *(undefined1 *)((int)param_3 + 0x3b) = 0;
    *(undefined1 *)(param_3 + 0x12) = 0;
    *(undefined1 *)(param_3 + 0x16) = 0;
    *(undefined1 *)(param_3 + 0x1b) = 0;
    return;
  }
LAB_00031b32:
  uVar4 = FUN_00035ab8(param_1,param_2,0xc);
  param_3[7] = uVar4;
  if (*(char *)(param_3 + 8) != '\0') {
    bVar2 = FUN_00035ab8(param_1,param_2,0x1d);
    *(byte *)(param_3 + 8) = bVar2;
    if (2 < bVar2) {
      uVar4 = FUN_00035ab8(param_1,param_2,0x1c);
      uVar3 = FUN_00035b58(param_1,param_2,uVar4);
      uVar4 = FUN_00031a74(param_1,param_2,param_3[4],uVar3);
      *(char *)((int)param_3 + 0x21) = (char)uVar4;
      *(char *)((int)param_3 + 0x23) = (char)((uint)uVar4 >> 0x10);
      *(char *)((int)param_3 + 0x22) = (char)((uint)uVar4 >> 8);
      iVar6 = FUN_00035ab8(param_1,param_2,0x26);
      if ((iVar6 == 0) || ((*(byte *)(iVar6 + 0xb) & 0xf) == 0)) {
        bVar2 = FUN_00035ab8(param_1,param_2,0x20);
        *(byte *)((int)param_3 + 0x2f) = *(byte *)((int)param_3 + 0x2f) & 0xf0 | bVar2 & 0xf;
        if ((bVar2 & 0xf) != 0) {
          FUN_0005aef8(param_3 + 9,(int)param_3 + 0x21,3);
          uVar4 = FUN_00035ab8(param_1,param_2,0x23);
          uVar3 = FUN_00035b58(param_1,param_2,uVar4);
          uVar4 = FUN_00031a74(param_1,param_2,param_3[4],uVar3);
          *(char *)((int)param_3 + 0x29) = (char)uVar4;
          *(char *)((int)param_3 + 0x2a) = (char)((uint)uVar4 >> 8);
          *(char *)((int)param_3 + 0x2b) = (char)((uint)uVar4 >> 0x10);
          uVar1 = FUN_00035ab8(param_1,param_2,0x21);
          *(undefined1 *)(param_3 + 10) = uVar1;
          uVar1 = FUN_00035ab8(param_1,param_2,0x22);
          *(undefined1 *)((int)param_3 + 0x2d) = uVar1;
          uVar1 = FUN_00035ab8(param_1,param_2,0x24);
          *(undefined1 *)((int)param_3 + 0x27) = uVar1;
          uVar1 = FUN_00035ab8(param_1,param_2,0x25);
          *(undefined1 *)(param_3 + 0xb) = uVar1;
        }
      }
      else {
        FUN_0004f328(param_3 + 9,iVar6,0xc);
      }
    }
  }
  if (*(char *)(param_3 + 0x12) != '\0') {
    iVar6 = FUN_00035ab8(param_1,param_2,0x30);
    param_3[0x11] = iVar6;
    if (iVar6 != 0) {
      bVar2 = FUN_00035ab8(param_1,param_2,0x32);
      *(byte *)(param_3 + 0x12) = bVar2;
      if (2 < bVar2) {
        bVar2 = FUN_00035ab8(param_1,param_2,0x34);
        *(byte *)((int)param_3 + 0x49) = *(byte *)((int)param_3 + 0x49) & 0xe0 | bVar2 & 0x1f;
        uVar4 = FUN_00035ab8(param_1,param_2,0x31);
        uVar4 = FUN_00035b58(param_1,param_2,uVar4);
        uVar4 = FUN_00031a74(param_1,param_2,param_3[4],uVar4);
        *(char *)((int)param_3 + 0x3e) = (char)uVar4;
        *(char *)((int)param_3 + 0x3f) = (char)((uint)uVar4 >> 8);
        *(char *)(param_3 + 0x10) = (char)((uint)uVar4 >> 0x10);
      }
    }
  }
  if (*(char *)(param_3 + 0x16) != '\0') {
    iVar6 = FUN_00035ab8(param_1,param_2,0x38);
    param_3[0x14] = iVar6;
    if (iVar6 != 0) {
      bVar2 = FUN_00035ab8(param_1,param_2,0x3a);
      *(byte *)(param_3 + 0x16) = bVar2;
      if (2 < bVar2) {
        uVar4 = FUN_00035ab8(param_1,param_2,0x3b);
        param_3[0x15] = uVar4;
        uVar4 = FUN_00035ab8(param_1,param_2,0x39);
        uVar4 = FUN_00035b58(param_1,param_2,uVar4);
        uVar4 = FUN_00031a74(param_1,param_2,param_3[4],uVar4);
        *(char *)((int)param_3 + 0x4a) = (char)uVar4;
        *(char *)((int)param_3 + 0x4b) = (char)((uint)uVar4 >> 8);
        *(char *)(param_3 + 0x13) = (char)((uint)uVar4 >> 0x10);
      }
    }
  }
  if (*(char *)((int)param_3 + 0x3b) != '\0') {
    iVar6 = FUN_00035ab8(param_1,param_2,0x28);
    param_3[0xc] = iVar6;
    if (iVar6 != 0) {
      bVar2 = FUN_00035ab8(param_1,param_2,0x29);
      *(byte *)((int)param_3 + 0x3b) = bVar2;
      if (2 < bVar2) {
        iVar6 = FUN_0003b6b0(param_3[0xc]);
        if (iVar6 == 2) {
          uVar4 = FUN_00035ab8(param_1,param_2,0x5a);
          param_3[0xd] = uVar4;
          uVar4 = FUN_00035ab8(param_1,param_2,0x58);
          uVar4 = FUN_00035b58(param_1,param_2,uVar4);
          uVar4 = FUN_00031a74(param_1,param_2,param_3[4],uVar4);
          *(char *)(param_3 + 0xe) = (char)uVar4;
          *(char *)((int)param_3 + 0x39) = (char)((uint)uVar4 >> 8);
          *(char *)((int)param_3 + 0x3a) = (char)((uint)uVar4 >> 0x10);
        }
        else {
          uVar4 = FUN_00035ab8(param_1,param_2,0x2a);
          uVar3 = FUN_00035b58(param_1,param_2,uVar4);
          uVar1 = FUN_00035ab8(param_1,param_2,0x2b);
          uVar5 = FUN_000319d8(param_1,param_2,param_3[4],uVar3,uVar1);
          *(char *)(param_3 + 0xf) = (char)(uVar5 >> 0x18);
          uVar4 = FUN_00044c94(uVar5 >> 0x10 & 0xff,uVar5 >> 8 & 0xff,uVar5 & 0xff);
          *(char *)(param_3 + 0xe) = (char)uVar4;
          *(char *)((int)param_3 + 0x39) = (char)((uint)uVar4 >> 8);
          *(char *)((int)param_3 + 0x3a) = (char)((uint)uVar4 >> 0x10);
          iVar6 = FUN_00035ab8(param_1,param_2,0x2c);
          *(char *)((int)param_3 + 0x3d) = '\x01' - (iVar6 == 0);
        }
      }
    }
  }
  if (*(char *)(param_3 + 0x1b) != '\0') {
    iVar6 = FUN_00035ab8(param_1,param_2,0x3c);
    param_3[0x17] = iVar6;
    if ((iVar6 != 0) && (2 < *(byte *)(param_3 + 0x1b))) {
      bVar2 = FUN_00035ab8(param_1,param_2,0x3e);
      *(byte *)(param_3 + 0x1b) = bVar2;
      if (2 < bVar2) {
        uVar4 = FUN_00035ab8(param_1,param_2,0x40);
        param_3[0x18] = uVar4;
        uVar4 = FUN_00035ab8(param_1,param_2,0x41);
        param_3[0x19] = uVar4;
        uVar4 = FUN_00035ab8(param_1,param_2,0x42);
        param_3[0x1a] = uVar4;
        uVar4 = FUN_00035ab8(param_1,param_2,0x3d);
        uVar4 = FUN_00035b58(param_1,param_2,uVar4);
        uVar4 = FUN_00031a74(param_1,param_2,param_3[4],uVar4);
        *(char *)((int)param_3 + 0x59) = (char)uVar4;
        *(char *)((int)param_3 + 0x5a) = (char)((uint)uVar4 >> 8);
/* ... truncated ... */
```

### `FUN_000355f0` @ `000355f0` score `47`

- reasons: status high-nibble test, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

int FUN_000355f0(int param_1,uint param_2)

{
  uint uVar1;
  undefined4 uVar2;
  uint uVar3;
  int iVar4;
  int iVar5;
  undefined4 *puVar6;
  undefined4 *puVar7;
  
  uVar1 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
  if (uVar1 == 0) {
    uVar1 = 1;
  }
  else {
    uVar3 = 0;
    iVar4 = *(int *)(param_1 + 0xc);
    do {
      if (((*(byte *)(iVar4 + 7) & 2) != 0) && ((*(uint *)(iVar4 + 4) & 0xffffff) == param_2))
      break;
      uVar3 = uVar3 + 1;
      iVar4 = iVar4 + 8;
    } while (uVar3 < uVar1);
    if (uVar1 != uVar3) {
      return uVar3 * 8 + *(int *)(param_1 + 0xc);
    }
    uVar1 = uVar1 + 1 & 0x3f;
  }
  uVar3 = *(ushort *)(param_1 + 0x2a) & DAT_000356c8;
  *(ushort *)(param_1 + 0x2a) = (ushort)uVar3 | (ushort)(uVar1 << 4);
  if ((uVar3 & 0x3f0) != 0 || uVar1 != 0) {
    iVar4 = FUN_0004bef4(*(undefined4 *)(param_1 + 0xc),uVar1 << 3);
    *(int *)(param_1 + 0xc) = iVar4;
    uVar1 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
    iVar5 = uVar1 - 1;
    if (uVar1 != 1) {
      FUN_0005ea24(iVar4 + ((iVar5 - uVar1) + 2) * 8,iVar4 + ((iVar5 - uVar1) + DAT_000356dc) * 8,
                   iVar5 * 8);
    }
    FUN_0004f350(iVar4,0,8);
    puVar7 = *(undefined4 **)(param_1 + 0xc);
    uVar2 = FUN_0004bea4(0xc);
    puVar6 = *(undefined4 **)(param_1 + 0xc);
    *puVar7 = uVar2;
    FUN_00046564(*puVar6);
    iVar4 = *(int *)(param_1 + 0xc);
    *(uint *)(iVar4 + 4) = (uint)(*(byte *)(iVar4 + 7) | 2) << 0x18 | param_2 & 0xffffff;
    return iVar4;
  }
  FUN_000458e8(3,DAT_000356d8,0x2e8,DAT_000356d4,DAT_000356d0,DAT_000356cc);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

### `FUN_00035738` @ `00035738` score `47`

- reasons: status high-nibble test, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

void FUN_00035738(int param_1,uint param_2,uint param_3,int *param_4)

{
  int *piVar1;
  undefined4 uVar2;
  int *piVar3;
  uint uVar4;
  undefined4 *puVar5;
  uint uVar6;
  
  uVar2 = DAT_00035810;
  piVar3 = (int *)FUN_000457fc(DAT_00035810);
  do {
    do {
      piVar1 = piVar3;
      if ((piVar1 == (int *)0x0) || (param_4 == piVar1)) {
        return;
      }
      piVar3 = (int *)FUN_0004580c(uVar2,piVar1);
    } while (((*piVar1 != param_1) || ((piVar1[2] != param_2 && (param_2 != 0xf0000)))) ||
            ((*(byte *)(piVar1 + 1) != param_3 && (param_3 != 0xff))));
    uVar4 = (uint)*(ushort *)(param_1 + 0x2a);
    uVar6 = 0;
    if ((uVar4 & 0x3ff) >> 4 != 0) {
      do {
        while ((puVar5 = (undefined4 *)(*(int *)(param_1 + 0xc) + uVar6 * 8),
               (*(byte *)((int)puVar5 + 7) & 2) != 0 &&
               ((param_2 == 0xf0000 || (param_2 == (puVar5[1] & 0xffffff)))))) {
          FUN_0004658c(*puVar5,(char)piVar1[1]);
          uVar4 = (uint)*(ushort *)(param_1 + 0x2a);
          uVar6 = uVar6 + 1;
          if ((uVar4 & 0x3ff) >> 4 <= uVar6) goto LAB_000357ea;
        }
        uVar6 = uVar6 + 1;
      } while (uVar6 < (uVar4 & 0x3ff) >> 4);
    }
LAB_000357ea:
    FUN_00043de8(piVar1,0);
    FUN_000457a4(uVar2,piVar1);
    FUN_0004bedc(piVar1);
  } while( true );
}
```

### `FUN_00035814` @ `00035814` score `47`

- reasons: status high-nibble test, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

bool FUN_00035814(int param_1,uint param_2,uint param_3,undefined4 *param_4)

{
  uint uVar1;
  undefined4 *puVar2;
  uint uVar3;
  undefined4 *puVar4;
  uint uVar5;
  uint uVar6;
  uint uVar7;
  uint uVar8;
  byte *pbVar9;
  uint local_3c;
  
  uVar7 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
  if (uVar7 == 0) {
    return false;
  }
  uVar5 = param_3 >> 2;
  if (0x1f < uVar5) {
    uVar5 = 0x1f;
  }
  uVar8 = 1 << (uVar5 & 0xff);
  uVar5 = 0;
  puVar4 = *(undefined4 **)(param_1 + 0xc);
LAB_0003586c:
  do {
    if ((*(byte *)((int)puVar4 + 7) & 2) == 0) {
      if (uVar7 <= uVar5) {
        return (bool)(*(byte *)((int)puVar4 + 7) & 2);
      }
      puVar4 = *(undefined4 **)(param_1 + 0xc) + uVar5 * 2;
      local_3c = 0xffffffff;
      do {
        puVar2 = (undefined4 *)*puVar4;
        if (((((puVar2[1] & uVar8) != 0) &&
             (uVar1 = puVar4[1], (param_2 & 0xff0000) == (uVar1 & 0xff0000))) &&
            ((uVar1 & 0xffff & ~(param_2 & 0xffff)) == 0)) &&
           ((int)local_3c < (int)(uVar1 & 0xffff))) {
          pbVar9 = (byte *)*puVar2;
          uVar3 = (uint)*(byte *)(puVar2 + 2);
          if (uVar3 == 0xff) {
            uVar3 = (uint)*pbVar9;
            if (uVar3 != 0) {
LAB_000359ce:
              if (param_3 != uVar3) goto LAB_000359c6;
              *param_4 = *(undefined4 *)(pbVar9 + 4);
LAB_00035982:
              local_3c = uVar1 & 0xffff;
              if ((param_2 & 0xffff) == (uVar1 & 0xffff)) {
                return true;
              }
            }
          }
          else if (uVar3 != 0) {
            uVar6 = 0;
            do {
              if (pbVar9[uVar6 + uVar3 * 4] == param_3) {
                *param_4 = *(undefined4 *)(pbVar9 + uVar6 * 4);
                goto LAB_00035982;
              }
              uVar6 = uVar6 + 1;
            } while (uVar6 < uVar3);
          }
        }
LAB_0003598c:
        uVar5 = uVar5 + 1;
        puVar4 = puVar4 + 2;
        if (uVar7 <= uVar5) {
          return local_3c != 0xffffffff;
        }
      } while( true );
    }
    if ((((*(byte *)(param_1 + 0x2a) & 8) == 0) && ((puVar4[1] & 0xff0000) == (param_2 & 0xff0000)))
       && (puVar2 = (undefined4 *)*puVar4, (puVar2[1] & uVar8) != 0)) {
      uVar1 = (uint)*(byte *)(puVar2 + 2);
      pbVar9 = (byte *)*puVar2;
      if (uVar1 == 0xff) {
        for (; *pbVar9 != 0; pbVar9 = pbVar9 + 8) {
          if (param_3 == *pbVar9) {
            *param_4 = *(undefined4 *)(pbVar9 + 4);
            return true;
          }
        }
      }
      else if (uVar1 != 0) {
        uVar3 = 0;
        do {
          if (pbVar9[uVar3 + uVar1 * 4] == param_3) {
            *param_4 = *(undefined4 *)(pbVar9 + uVar3 * 4);
            return true;
          }
          uVar3 = uVar3 + 1;
        } while (uVar3 < uVar1);
        uVar5 = uVar5 + 1;
        puVar4 = puVar4 + 2;
        if (uVar7 <= uVar5) {
          return false;
        }
        goto LAB_0003586c;
      }
    }
    uVar5 = uVar5 + 1;
    puVar4 = puVar4 + 2;
    if (uVar7 <= uVar5) {
      return false;
    }
  } while( true );
LAB_000359c6:
  uVar3 = (uint)pbVar9[8];
  pbVar9 = pbVar9 + 8;
  if (uVar3 == 0) goto LAB_0003598c;
  goto LAB_000359ce;
}
```

### `FUN_00035b18` @ `00035b18` score `47`

- reasons: status high-nibble test, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

undefined4 FUN_00035b18(int param_1,undefined4 param_2,undefined4 param_3,uint param_4)

{
  undefined4 *puVar1;
  undefined4 uVar2;
  uint uVar3;
  uint uVar4;
  
  uVar3 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
  if (uVar3 != 0) {
    uVar4 = 0;
    puVar1 = *(undefined4 **)(param_1 + 0xc);
    do {
      if (((*(byte *)((int)puVar1 + 7) & 1) != 0) && (param_4 == (puVar1[1] & 0xffffff))) {
        uVar2 = FUN_00046730(*puVar1,param_2,param_3);
        return uVar2;
      }
      uVar4 = uVar4 + 1;
      puVar1 = puVar1 + 2;
    } while (uVar4 < uVar3);
  }
  return 0;
}
```

### `FUN_00036110` @ `00036110` score `47`

- reasons: status high-nibble test, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

void FUN_00036110(int param_1,undefined4 param_2,undefined4 param_3,uint param_4)

{
  uint uVar1;
  undefined4 *puVar2;
  undefined4 uVar3;
  int iVar4;
  uint uVar5;
  undefined4 *puVar6;
  int iVar7;
  int iVar8;
  
  FUN_00035738(param_1,param_4 & 0xff0000,param_2,0);
  uVar1 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
  if (uVar1 == 0) {
    uVar1 = 1;
  }
  else {
    uVar5 = 0;
    puVar2 = *(undefined4 **)(param_1 + 0xc);
    do {
      if (((*(byte *)((int)puVar2 + 7) & 1) != 0) && (param_4 == (puVar2[1] & 0xffffff)))
      goto LAB_000361f0;
      uVar5 = uVar5 + 1;
      puVar2 = puVar2 + 2;
    } while (uVar5 < uVar1);
    uVar1 = uVar1 + 1 & 0x3f;
  }
  uVar5 = *(ushort *)(param_1 + 0x2a) & DAT_00036278;
  *(ushort *)(param_1 + 0x2a) = (ushort)uVar5 | (ushort)(uVar1 << 4);
  if ((uVar5 & 0x3f0) == 0 && uVar1 == 0) {
    FUN_000458e8(3,DAT_0003628c,DAT_00036290,DAT_00036288,DAT_00036284,DAT_00036280);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  puVar2 = (undefined4 *)FUN_0004bef4(*(undefined4 *)(param_1 + 0xc),uVar1 << 3);
  *(undefined4 **)(param_1 + 0xc) = puVar2;
  if (puVar2 == (undefined4 *)0x0) {
    FUN_000458e8(3,DAT_0003628c,0x2c4,DAT_00036288,DAT_0003629c,DAT_00036298,DAT_00036294);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  uVar1 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
  iVar4 = uVar1 - 1;
  if (uVar1 != 1) {
    puVar6 = puVar2 + (uVar1 - 2) * 2;
    do {
      if ((*(byte *)((int)puVar6 + 7) & 3) != 0) {
        puVar2 = puVar6 + 2;
        iVar4 = iVar4 << 3;
        goto LAB_000361bc;
      }
      iVar4 = iVar4 + -1;
      puVar6[2] = *puVar6;
      puVar6[3] = puVar6[1];
      puVar6 = puVar6 + -2;
    } while (iVar4 != 0);
  }
  iVar4 = 0;
LAB_000361bc:
  FUN_0004f350(puVar2,0,8);
  iVar8 = *(int *)(param_1 + 0xc);
  uVar3 = FUN_0004beb8(0xc);
  iVar7 = *(int *)(param_1 + 0xc);
  *(undefined4 *)(iVar8 + iVar4) = uVar3;
  FUN_00046564(*(undefined4 *)(iVar7 + iVar4));
  puVar2 = (undefined4 *)(*(int *)(param_1 + 0xc) + iVar4);
  puVar2[1] = (uint)(*(byte *)((int)puVar2 + 7) | 1) << 0x18 | param_4 & 0xffffff;
LAB_000361f0:
  uVar3 = *puVar2;
  if ((param_4 == 0) && (iVar4 = FUN_00046840(param_2), iVar4 << 0x1a < 0)) {
    FUN_00033298(param_1);
    FUN_0004663c(uVar3,param_2,param_3);
  }
  else {
    FUN_0004663c(uVar3,param_2,param_3);
  }
  if (*(char *)(DAT_0003627c + 0x24) != '\0') {
    FUN_00035f68(param_1,param_4,param_2);
  }
  return;
}
```

### `FUN_00036674` @ `00036674` score `47`

- reasons: status high-nibble test, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

void FUN_00036674(int *param_1,uint param_2)

{
  int iVar1;
  byte bVar2;
  uint uVar3;
  uint uVar4;
  undefined4 *puVar5;
  int iVar6;
  int iVar7;
  uint local_28;
  uint local_24 [2];
  
  iVar6 = *param_1;
  uVar4 = (*(ushort *)(iVar6 + 0x2a) & 0x3ff) >> 4;
  if (uVar4 != 0) {
    uVar3 = 0;
    puVar5 = *(undefined4 **)(iVar6 + 0xc);
    do {
      if (((*(byte *)((int)puVar5 + 7) & 2) != 0) && (param_1[2] == (puVar5[1] & 0xffffff))) {
        iVar7 = uVar3 * 8;
        bVar2 = *(byte *)(param_1 + 1);
        if (bVar2 < 0x79) {
          if (0x57 < bVar2) {
            if ((byte)(bVar2 + 0xa8) < 0x21) {
                    /* WARNING: Could not recover jumptable at 0x000366ca. Too many branches */
                    /* WARNING: Treating indirect jump as call */
              (**(code **)(DAT_0003680c + (uint)(byte)(bVar2 + 0xa8) * 4))();
              return;
            }
            goto LAB_00036752;
          }
          if (0x45 < bVar2) goto LAB_00036752;
          if (bVar2 < 0x31) {
            if ((bVar2 != 0x1c) && (bVar2 != 0x23)) goto LAB_00036752;
LAB_0003676e:
            if ((int)param_2 < 1) {
              local_28 = (uint)*(uint3 *)(param_1 + 3);
            }
            else if ((int)param_2 < 0xff) {
              local_28 = FUN_00044da4(param_1[4],param_1[3],param_2 & 0xff);
              local_28 = local_28 & 0xffffff;
              bVar2 = *(byte *)(param_1 + 1);
              puVar5 = (undefined4 *)(*(int *)(iVar6 + 0xc) + iVar7);
            }
            else {
              local_28 = (uint)*(uint3 *)(param_1 + 4);
            }
            goto LAB_00036706;
          }
          uVar4 = 1 << (uint)(byte)(bVar2 - 0x31);
          if ((uVar4 & DAT_00036810) != 0) goto LAB_0003676e;
          if ((uVar4 & 0x18) == 0) goto LAB_00036752;
          if ((int)param_2 < 0xff) goto LAB_00036702;
        }
        else {
LAB_00036752:
          if (param_2 == 0) {
LAB_00036702:
            local_28 = param_1[3];
            goto LAB_00036706;
          }
          if (param_2 != 0xff) {
            local_28 = ((int)(param_2 * (param_1[4] - param_1[3])) >> 8) + param_1[3];
            goto LAB_00036706;
          }
        }
        local_28 = param_1[4];
LAB_00036706:
        local_24[0] = 0;
        iVar1 = FUN_00046730(*puVar5,bVar2,local_24);
        if (((iVar1 == 0) || (local_28 != local_24[0])) ||
           (iVar1 = FUN_00044c54(local_28,local_28), uVar4 = local_24[0], iVar1 == 0)) {
          FUN_0004663c(*(undefined4 *)(*(int *)(iVar6 + 0xc) + iVar7),(char)param_1[1],local_28);
        }
        else {
          FUN_0004663c(*(undefined4 *)(*(int *)(iVar6 + 0xc) + iVar7),(char)param_1[1],local_28);
          if (local_28 == uVar4) {
            return;
          }
        }
        if (*param_1 != 0) {
          if (*(char *)(DAT_00036814 + 0x24) == '\0') {
            return;
          }
          FUN_00035f68(*param_1,param_1[2],(char)param_1[1]);
          return;
        }
        FUN_000458e8(3,DAT_00036824,0x115,DAT_0003681c,DAT_00036828,DAT_00036820,DAT_00036818);
        do {
                    /* WARNING: Do nothing block with infinite loop */
        } while( true );
      }
      uVar3 = uVar3 + 1;
      puVar5 = puVar5 + 2;
    } while (uVar3 < uVar4);
  }
  return;
}
```

### `FUN_0003682c` @ `0003682c` score `47`

- reasons: status high-nibble test, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

void FUN_0003682c(int param_1,int param_2,uint param_3)

{
  byte bVar1;
  bool bVar2;
  uint uVar3;
  undefined4 uVar4;
  int *piVar5;
  uint uVar6;
  uint uVar7;
  uint uVar8;
  uint uVar9;
  char cVar10;
  int iVar11;
  int iVar12;
  
  uVar7 = param_3 & 0xff0000;
  if (param_2 == 0) {
    cVar10 = -1;
  }
  else {
    cVar10 = -('\x01' - (*(char *)(param_2 + 8) == '\0'));
    if ((uVar7 == 0) && (iVar11 = FUN_000356e0(param_2), iVar11 != 0)) {
      FUN_00033298(param_1);
    }
  }
  uVar3 = DAT_0003697c;
  uVar6 = (uint)*(ushort *)(param_1 + 0x2a);
  if ((uVar6 & 0x3ff) >> 4 != 0) {
    bVar2 = false;
    uVar9 = 0;
    do {
      iVar12 = *(int *)(param_1 + 0xc);
      iVar11 = uVar9 * 8;
      piVar5 = (int *)(iVar12 + iVar11);
      if (((((param_3 & 0xffff) == uVar3) || ((piVar5[1] & 0xffffU) == (param_3 & 0xffff))) &&
          ((uVar7 == 0xf0000 || (uVar7 == (piVar5[1] & 0xff0000U))))) &&
         ((param_2 == 0 || (*piVar5 == param_2)))) {
        bVar1 = *(byte *)((int)piVar5 + 7);
        if ((bVar1 & 2) != 0) {
          FUN_00035738(param_1,uVar7,0xff,0);
          iVar12 = *(int *)(param_1 + 0xc);
          piVar5 = (int *)(iVar12 + iVar11);
          bVar1 = *(byte *)((int)piVar5 + 7);
        }
        if ((bVar1 & 3) != 0) {
          if (*piVar5 != 0) {
                    /* WARNING: Subroutine does not return */
            FUN_00046570();
          }
          FUN_0004bedc();
          iVar12 = *(int *)(param_1 + 0xc);
          *(undefined4 *)(iVar12 + iVar11) = 0;
        }
        uVar8 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
        uVar6 = uVar8 - 1;
        if (uVar9 < uVar6) {
          FUN_0005ea24(iVar12 + iVar11,iVar12 + iVar11 + 8,(uVar6 - uVar9) * 8);
        }
        uVar6 = uVar8 + 0x3f & 0x3f;
        *(ushort *)(param_1 + 0x2a) =
             (ushort)(uVar6 << 4) | *(ushort *)(param_1 + 0x2a) & (ushort)DAT_00036980;
        uVar4 = FUN_0004bef4(iVar12,uVar6 << 3);
        bVar2 = true;
        uVar6 = (uint)*(ushort *)(param_1 + 0x2a);
        *(undefined4 *)(param_1 + 0xc) = uVar4;
      }
      else {
        uVar9 = uVar9 + 1;
      }
    } while (uVar9 < (uVar6 & 0x3ff) >> 4);
    if (((bVar2) && (cVar10 != '\0')) && (*(char *)(DAT_00036984 + 0x24) != '\0')) {
      FUN_00035f68(param_1,uVar7,0xff);
    }
  }
  return;
}
```

### `FUN_00042030` @ `00042030` score `47`

- reasons: status high-nibble test, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

void FUN_00042030(undefined4 *param_1,undefined4 *param_2,uint param_3,byte param_4)

{
  char cVar1;
  char cVar2;
  int iVar3;
  int iVar4;
  undefined4 uVar5;
  undefined1 *puVar6;
  int *piVar7;
  int *piVar8;
  int iVar9;
  char cVar10;
  undefined4 uVar11;
  uint *puVar12;
  int iVar13;
  int iVar14;
  undefined2 *puVar15;
  int iVar16;
  char cVar17;
  undefined4 uVar18;
  int *piVar19;
  uint uVar20;
  uint uVar21;
  int iVar22;
  ushort *puVar23;
  uint uVar24;
  int iVar25;
  int iVar26;
  int *piVar27;
  int iVar28;
  char *pcVar29;
  int *piVar30;
  bool bVar31;
  int local_48 [4];
  uint local_38 [5];
  
  iVar3 = FUN_000448e4(param_2);
  iVar4 = FUN_000448f0(param_2);
  if (iVar4 < iVar3) {
    iVar3 = iVar4;
  }
  uVar21 = iVar3 >> 1;
  if ((int)param_3 < iVar3 >> 1) {
    uVar21 = param_3;
  }
  uVar5 = *param_2;
  uVar11 = param_2[2];
  uVar18 = param_2[3];
  param_1[3] = param_2[1];
  param_1[4] = uVar11;
  param_1[5] = uVar18;
  *(byte *)(param_1 + 7) = *(byte *)(param_1 + 7) & 0xfe | param_4 & 1;
  *param_1 = DAT_000423a8;
  uVar24 = (int)~uVar21 >> 0x1f & uVar21;
  param_1[2] = uVar5;
  param_1[6] = uVar24;
  *(undefined1 *)(param_1 + 1) = 2;
  iVar3 = DAT_000423ac;
  if ((int)uVar21 < 1) {
    param_1[8] = 0;
  }
  else {
    iVar4 = 0;
    puVar12 = (uint *)(DAT_000423ac + 0x160);
    do {
      iVar22 = (int)uVar24 >> 4;
      if (uVar24 == *puVar12) {
        iVar26 = iVar4 * 0x1c + DAT_000423ac;
        piVar30 = (int *)(iVar26 + 0x15c);
        *piVar30 = *piVar30 + 1;
        iVar25 = 1;
        if (0xf < (int)uVar21) {
          iVar25 = iVar22;
        }
        iVar25 = *(int *)(iVar26 + 0x158) + iVar25;
        if (1000 < iVar25) {
          iVar25 = 1000;
        }
        *(int *)(iVar3 + iVar4 * 0x1c + 0x158) = iVar25;
        param_1[8] = iVar3 + iVar4 * 0x1c + 0x148;
        return;
      }
      iVar4 = iVar4 + 1;
      puVar12 = puVar12 + 7;
    } while (iVar4 != 4);
    piVar30 = (int *)0x0;
    piVar19 = (int *)(DAT_000423ac + 0x148);
    piVar8 = (int *)(DAT_000423ac + 0x1b8);
    do {
      piVar27 = piVar19;
      if (piVar19[5] == 0) {
        piVar7 = piVar19;
        if (piVar30 == (int *)0x0) {
          piVar27 = piVar19 + 7;
          if (piVar27 == piVar8) break;
          piVar7 = piVar27;
          piVar30 = piVar19;
          if (piVar19[0xc] != 0) goto LAB_0004210a;
        }
        iVar3 = piVar30[4];
        piVar27 = piVar7 + 7;
        if (piVar7[4] < iVar3) goto LAB_000420e4;
        while( true ) {
          piVar7 = piVar30;
          if (piVar27 == piVar8) goto LAB_00042114;
          if (piVar27[5] != 0) break;
          while (piVar7 = piVar27, piVar27 = piVar7 + 7, piVar7[4] < iVar3) {
LAB_000420e4:
            if (piVar27 == piVar8) goto LAB_0004211c;
            piVar30 = piVar7;
            if (piVar27[5] != 0) goto LAB_0004210a;
            iVar3 = piVar7[4];
          }
        }
      }
LAB_0004210a:
      piVar19 = piVar27 + 7;
      piVar7 = piVar30;
    } while (piVar19 != piVar8);
LAB_00042114:
    if (piVar7 == (int *)0x0) {
      piVar7 = (int *)FUN_0004beb8(0x1c);
      if (piVar7 == (int *)0x0) {
        FUN_000458e8(3,DAT_0004254c,0x155,DAT_0004255c,DAT_00042550,DAT_00042558,DAT_00042540);
        do {
                    /* WARNING: Do nothing block with infinite loop */
        } while( true );
      }
      piVar7[4] = -1;
    }
    else {
LAB_0004211c:
      piVar7[5] = piVar7[5] + 1;
      iVar3 = 1;
      if ((0xf < (int)uVar21) && (iVar3 = iVar22, 1000 < iVar22)) {
        iVar3 = 1000;
      }
      piVar7[4] = iVar3;
    }
    iVar3 = *piVar7;
    param_1[8] = piVar7;
    piVar7[6] = uVar24;
    if (iVar3 != 0) {
      FUN_0004bedc();
    }
    iVar3 = uVar24 + 1;
    puVar6 = (undefined1 *)FUN_0004bea4(iVar3 * 6);
    *piVar7 = (int)puVar6;
    if (puVar6 == (undefined1 *)0x0) {
      FUN_000458e8(3,DAT_0004254c,0x438,DAT_00042544,DAT_00042550,DAT_00042548,DAT_00042540);
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    piVar7[1] = (int)puVar6;
    piVar7[3] = (int)(puVar6 + uVar24 * 2 + 2);
    uVar20 = uVar24 * 4;
    piVar7[2] = (int)(puVar6 + uVar20 + 4);
/* ... truncated ... */
```

### `FUN_0004d190` @ `0004d190` score `47`

- reasons: MIDI status-class constant, channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing

```c

/* WARNING: Type propagation algorithm not settling */

void FUN_0004d190(undefined4 *param_1)

{
  ushort uVar1;
  int iVar2;
  int iVar3;
  byte bVar4;
  uint uVar5;
  ushort *puVar6;
  int iVar7;
  ushort *puVar8;
  int iVar9;
  byte *pbVar10;
  int iVar11;
  uint uVar12;
  uint uVar13;
  uint uVar14;
  uint uVar15;
  int iVar16;
  int iVar17;
  int iVar18;
  ushort *puVar19;
  ushort *puVar20;
  int iVar21;
  ushort *puVar22;
  byte *pbVar23;
  int local_30;
  int local_2c;
  
  if (*(char *)(param_1 + 8) == '\x12') {
    iVar3 = param_1[2];
    iVar16 = param_1[1];
    uVar5 = (uint)*(byte *)((int)param_1 + 0x21);
    puVar6 = (ushort *)*param_1;
    iVar7 = param_1[3];
    puVar8 = (ushort *)param_1[6];
    iVar9 = param_1[7];
    pbVar10 = (byte *)param_1[4];
    iVar11 = param_1[5];
    if (*(char *)((int)param_1 + 0x22) == '\0') {
      if (pbVar10 == (byte *)0x0) {
        if (uVar5 < 0xfd) {
          if ((0 < iVar3) && (0 < iVar16)) {
            iVar11 = 0;
            puVar22 = puVar8 + iVar16;
            puVar19 = puVar6;
            puVar20 = puVar8;
            do {
              do {
                uVar1 = FUN_00044cdc(*puVar8,*puVar6,uVar5);
                puVar8 = puVar8 + 1;
                *puVar6 = uVar1;
                puVar6 = puVar6 + 1;
              } while (puVar22 != puVar8);
              puVar6 = (ushort *)((int)puVar19 + iVar7);
              puVar8 = (ushort *)((int)puVar20 + iVar9);
              iVar11 = iVar11 + 1;
              puVar22 = (ushort *)((int)puVar22 + iVar9);
              puVar19 = puVar6;
              puVar20 = puVar8;
            } while (iVar3 != iVar11);
          }
        }
        else if (0 < iVar3) {
          iVar11 = 0;
          do {
            FUN_0004f328(puVar6,puVar8,iVar16 << 1);
            iVar11 = iVar11 + 1;
            puVar6 = (ushort *)((int)puVar6 + iVar7);
            puVar8 = (ushort *)((int)puVar8 + iVar9);
          } while (iVar3 != iVar11);
        }
      }
      else if (uVar5 < 0xfd) {
        if ((0 < iVar3) && (0 < iVar16)) {
          puVar22 = puVar8 + iVar16;
          local_30 = 0;
          puVar19 = puVar6;
          puVar20 = puVar8;
          pbVar23 = pbVar10;
          do {
            do {
              uVar1 = FUN_00044cdc(*puVar8,*puVar6,uVar5 * *pbVar10 >> 8);
              puVar8 = puVar8 + 1;
              *puVar6 = uVar1;
              pbVar10 = pbVar10 + 1;
              puVar6 = puVar6 + 1;
            } while (puVar22 != puVar8);
            puVar6 = (ushort *)((int)puVar19 + iVar7);
            puVar8 = (ushort *)((int)puVar20 + iVar9);
            pbVar10 = pbVar23 + iVar11;
            puVar22 = (ushort *)((int)puVar22 + iVar9);
            local_30 = local_30 + 1;
            puVar19 = puVar6;
            puVar20 = puVar8;
            pbVar23 = pbVar10;
          } while (iVar3 != local_30);
        }
      }
      else if ((0 < iVar3) && (0 < iVar16)) {
        iVar21 = 0;
        puVar22 = puVar8 + iVar16;
        puVar19 = puVar6;
        puVar20 = puVar8;
        pbVar23 = pbVar10;
        do {
          do {
            uVar1 = FUN_00044cdc(*puVar8,*puVar6,*pbVar10);
            puVar8 = puVar8 + 1;
            *puVar6 = uVar1;
            pbVar10 = pbVar10 + 1;
            puVar6 = puVar6 + 1;
          } while (puVar22 != puVar8);
          puVar6 = (ushort *)((int)puVar19 + iVar7);
          puVar8 = (ushort *)((int)puVar20 + iVar9);
          pbVar10 = pbVar23 + iVar11;
          puVar22 = (ushort *)((int)puVar22 + iVar9);
          iVar21 = iVar21 + 1;
          puVar19 = puVar6;
          puVar20 = puVar8;
          pbVar23 = pbVar10;
        } while (iVar3 != iVar21);
      }
    }
    else if (0 < iVar3) {
      local_2c = 0;
      if (0 < iVar16) {
LAB_0004d2e8:
        do {
          bVar4 = *(byte *)((int)param_1 + 0x22);
          iVar21 = 0;
          puVar19 = puVar6;
          puVar20 = puVar8;
          if (bVar4 == 3) goto LAB_0004d382;
LAB_0004d2f6:
          if (bVar4 < 4) {
            if (bVar4 == 1) {
              if (*puVar20 == 0) goto LAB_0004d550;
              uVar12 = (uint)(*(byte *)((int)puVar19 + 1) >> 3) +
                       (uint)(*(byte *)((int)puVar20 + 1) >> 3);
              if (0x1f < uVar12) {
                uVar12 = 0x1f;
              }
              uVar13 = ((*puVar19 & 0x7ff) >> 5) + ((*puVar20 & 0x7ff) >> 5);
              if (0x3f < uVar13) {
                uVar13 = 0x3f;
              }
              iVar2 = uVar12 * 0x800 + uVar13 * 0x20;
              uVar12 = ((byte)*puVar19 & 0x1f) + ((byte)*puVar20 & 0x1f);
              if (uVar12 < 0x20) goto LAB_0004d3bc;
              uVar12 = 0x1f;
              goto LAB_0004d3bc;
            }
            if (bVar4 != 2) {
              bVar4 = 0;
              goto LAB_0004d690;
            }
/* ... truncated ... */
```

### `FUN_0004dbe4` @ `0004dbe4` score `47`

- reasons: MIDI status-class constant, channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing

```c

/* WARNING: Control flow encountered bad instruction data */

void FUN_0004dbe4(undefined4 *param_1)

{
  ushort uVar1;
  int iVar2;
  uint uVar3;
  byte bVar4;
  ushort *puVar5;
  int iVar6;
  uint uVar7;
  uint uVar8;
  int iVar9;
  uint uVar10;
  byte *extraout_r2;
  int iVar11;
  ushort *puVar12;
  int iVar13;
  ushort *puVar14;
  int iVar15;
  byte *pbVar16;
  int iVar17;
  uint uVar18;
  int iVar19;
  int extraout_r3;
  int extraout_r3_00;
  byte *pbVar20;
  ushort *puVar21;
  ushort *puVar22;
  uint uVar23;
  int iVar24;
  int local_40;
  int local_38;
  undefined2 local_2c;
  ushort local_2a [3];
  
  if (*(char *)(param_1 + 8) != '\x12') {
    if (*(char *)(param_1 + 8) == '\x1b') {
      iVar11 = param_1[1];
      iVar6 = param_1[2];
      iVar13 = param_1[7];
      uVar23 = (uint)*(byte *)((int)param_1 + 0x21);
      pbVar16 = (byte *)param_1[4];
      puVar14 = (ushort *)*param_1;
      iVar15 = param_1[5];
      iVar17 = param_1[3];
      puVar12 = (ushort *)param_1[6];
      if (*(char *)((int)param_1 + 0x22) == '\0') {
        if (pbVar16 == (byte *)0x0) {
          if (0xfc < uVar23) {
            if (iVar6 < 1) {
              FUN_0004dc14();
              return;
            }
            iVar15 = 0;
            do {
              FUN_0004f328(puVar14,puVar12,iVar11 << 1);
              iVar15 = iVar15 + 1;
              puVar14 = (ushort *)((int)puVar14 + iVar17);
              puVar12 = (ushort *)((int)puVar12 + iVar13);
            } while (iVar6 != iVar15);
            FUN_0004dc14();
            return;
          }
          if (iVar6 < 1) {
            FUN_0004dc14();
            return;
          }
          if (iVar11 < 1) {
            FUN_0004dc14();
            return;
          }
          iVar15 = 0;
          puVar22 = puVar14 + iVar11;
          puVar5 = puVar12;
          puVar21 = puVar14;
          do {
            do {
              uVar3 = FUN_00044cdc(*puVar12 << 8 | *puVar12 >> 8,*puVar14 << 8 | *puVar14 >> 8,
                                   uVar23);
              *puVar14 = (ushort)((uVar3 & 0xff) << 8) | (ushort)(uVar3 >> 8) & 0xff;
              puVar14 = puVar14 + 1;
              puVar12 = puVar12 + 1;
            } while (puVar22 != puVar14);
            puVar14 = (ushort *)((int)puVar21 + iVar17);
            puVar12 = (ushort *)((int)puVar5 + iVar13);
            puVar22 = (ushort *)((int)puVar22 + iVar17);
            iVar15 = iVar15 + 1;
            puVar5 = puVar12;
            puVar21 = puVar14;
          } while (iVar6 != iVar15);
          FUN_0004dc14();
          return;
        }
        if (uVar23 < 0xfd) {
          if (iVar6 < 1) {
            FUN_0004dc14();
            return;
          }
          if (iVar11 < 1) {
            FUN_0004dc14();
            return;
          }
          puVar22 = puVar14 + iVar11;
          local_40 = 0;
          puVar5 = puVar12;
          pbVar20 = pbVar16;
          puVar21 = puVar14;
          do {
            do {
              uVar3 = FUN_00044cdc(*puVar12 << 8 | *puVar12 >> 8,*puVar14 << 8 | *puVar14 >> 8,
                                   uVar23 * *pbVar16 >> 8);
              *puVar14 = (ushort)((uVar3 & 0xff) << 8) | (ushort)(uVar3 >> 8) & 0xff;
              puVar14 = puVar14 + 1;
              puVar12 = puVar12 + 1;
              pbVar16 = pbVar16 + 1;
            } while (puVar22 != puVar14);
            puVar14 = (ushort *)((int)puVar21 + iVar17);
            puVar12 = (ushort *)((int)puVar5 + iVar13);
            puVar22 = (ushort *)((int)puVar22 + iVar17);
            pbVar16 = pbVar20 + iVar15;
            local_40 = local_40 + 1;
            puVar5 = puVar12;
            pbVar20 = pbVar16;
            puVar21 = puVar14;
          } while (iVar6 != local_40);
          FUN_0004dc14();
          return;
        }
        if (iVar6 < 1) {
          FUN_0004dc14();
          return;
        }
        if (iVar11 < 1) {
          FUN_0004dc14();
          return;
        }
        puVar22 = puVar14 + iVar11;
        iVar11 = 0;
        puVar5 = puVar12;
        pbVar20 = pbVar16;
        puVar21 = puVar14;
        do {
          do {
            uVar23 = FUN_00044cdc(*puVar12 << 8 | *puVar12 >> 8,*puVar14 << 8 | *puVar14 >> 8,
                                  *pbVar16);
            *puVar14 = (ushort)((uVar23 & 0xff) << 8) | (ushort)(uVar23 >> 8) & 0xff;
            puVar14 = puVar14 + 1;
            puVar12 = puVar12 + 1;
            pbVar16 = pbVar16 + 1;
          } while (puVar22 != puVar14);
          puVar14 = (ushort *)((int)puVar21 + iVar17);
          puVar12 = (ushort *)((int)puVar5 + iVar13);
          puVar22 = (ushort *)((int)puVar22 + iVar17);
          pbVar16 = pbVar20 + iVar15;
          iVar11 = iVar11 + 1;
          puVar5 = puVar12;
          pbVar20 = pbVar16;
/* ... truncated ... */
```

### `FUN_0005b310` @ `0005b310` score `47`

- reasons: MIDI status-class constant, channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing

```c

int FUN_0005b310(code *param_1,undefined4 param_2,int param_3,undefined4 param_4,int param_5,
                uint param_6,int param_7,uint param_8,uint param_9)

{
  int iVar1;
  int iVar2;
  undefined4 uVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  undefined4 uVar6;
  uint uVar7;
  undefined8 uVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  longlong lVar11;
  undefined8 uVar12;
  undefined4 local_58;
  uint local_54;
  uint local_50;
  undefined4 local_4c;
  uint local_44;
  uint local_40;
  uint local_38;
  
  iVar1 = FUN_0005a9f2(param_5,param_6,param_5,param_6);
  local_54 = param_6;
  if (((iVar1 != 0) || (iVar1 = FUN_0005a9e8(param_5,param_6,0xffffffff,DAT_0005b6a0), iVar1 != 0))
     || (iVar1 = FUN_0005a9bc(param_5,param_6,0xffffffff,DAT_0005b6a4), iVar1 != 0))
  goto LAB_0005b3e2;
  iVar1 = FUN_0005a9bc(param_5,param_6,0,0);
  if (iVar1 == 0) {
  }
  else {
    local_54 = param_6 + 0x80000000;
  }
  uVar12 = CONCAT44(local_54,param_5);
  local_44 = param_9 & 0x800;
  if ((param_9 & 0x400) == 0) {
    if (local_54 != 0 || param_5 != 0) {
      param_7 = 6;
LAB_0005b450:
      uVar8 = FUN_0005aa14(((local_54 & 0x7fffffff) >> 0x14) + DAT_0005b6ac);
      uVar8 = FUN_0005a93e((int)uVar8,(int)((ulonglong)uVar8 >> 0x20),DAT_0005b6b0,DAT_0005b6b4);
      uVar8 = FUN_0005a900((int)uVar8,(int)((ulonglong)uVar8 >> 0x20),DAT_0005b6b8,DAT_0005b6bc);
      uVar9 = FUN_0005a8f6(param_5,DAT_0005b6c0 | local_54 & 0xfffff,0,DAT_0005b6c4);
      uVar9 = FUN_0005a93e((int)uVar9,(int)((ulonglong)uVar9 >> 0x20),DAT_0005b6c8,DAT_0005b6cc);
      FUN_0005a900((int)uVar8,(int)((ulonglong)uVar8 >> 0x20),(int)uVar9,
                   (int)((ulonglong)uVar9 >> 0x20));
      local_38 = FUN_0005aa44();
      uVar8 = FUN_0005aa14();
      uVar4 = (undefined4)((ulonglong)uVar8 >> 0x20);
      uVar9 = FUN_0005a93e((int)uVar8,uVar4,DAT_0005b6d0,DAT_0005b6d4);
      FUN_0005a900((int)uVar9,(int)((ulonglong)uVar9 >> 0x20),0,DAT_0005b6d8);
      iVar1 = FUN_0005aa44();
      uVar8 = FUN_0005a93e((int)uVar8,uVar4,DAT_0005b6dc,DAT_0005b6e0);
      uVar9 = FUN_0005aa14(iVar1);
      uVar9 = FUN_0005a93e((int)uVar9,(int)((ulonglong)uVar9 >> 0x20),DAT_0005b6e4,DAT_0005b6e8);
      uVar8 = FUN_0005a8f6((int)uVar8,(int)((ulonglong)uVar8 >> 0x20),(int)uVar9,
                           (int)((ulonglong)uVar9 >> 0x20));
      uVar5 = (undefined4)((ulonglong)uVar8 >> 0x20);
      uVar4 = (undefined4)uVar8;
      uVar8 = FUN_0005a93e(uVar4,uVar5,uVar4,uVar5);
      uVar6 = (undefined4)((ulonglong)uVar8 >> 0x20);
      uVar3 = (undefined4)uVar8;
      uVar8 = FUN_0005a900(uVar4,uVar5,uVar4,uVar5);
      uVar9 = FUN_0005a90a(uVar3,uVar6,0,DAT_0005b6ec);
      uVar9 = FUN_0005a900((int)uVar9,(int)((ulonglong)uVar9 >> 0x20),0,DAT_0005b6f0);
      uVar9 = FUN_0005a90a(uVar3,uVar6,(int)uVar9,(int)((ulonglong)uVar9 >> 0x20));
      uVar9 = FUN_0005a900((int)uVar9,(int)((ulonglong)uVar9 >> 0x20),0,DAT_0005b6f4);
      uVar9 = FUN_0005a90a(uVar3,uVar6,(int)uVar9,(int)((ulonglong)uVar9 >> 0x20));
      uVar10 = FUN_0005a8f6(0,0x40000000,uVar4,uVar5);
      uVar9 = FUN_0005a900((int)uVar9,(int)((ulonglong)uVar9 >> 0x20),(int)uVar10,
                           (int)((ulonglong)uVar10 >> 0x20));
      uVar8 = FUN_0005a90a((int)uVar8,(int)((ulonglong)uVar8 >> 0x20),(int)uVar9,
                           (int)((ulonglong)uVar9 >> 0x20));
      uVar8 = FUN_0005a900((int)uVar8,(int)((ulonglong)uVar8 >> 0x20),0,DAT_0005b6c0);
      lVar11 = FUN_0005a93e((int)uVar8,(int)((ulonglong)uVar8 >> 0x20),0,
                            (iVar1 + DAT_0005b6f8) * 0x100000);
      uVar4 = (undefined4)((ulonglong)lVar11 >> 0x20);
      iVar1 = FUN_0005a9e8((int)lVar11,uVar4,param_5,local_54);
      if (iVar1 != 0) {
        local_38 = local_38 - 1;
        lVar11 = FUN_0005a90a((int)lVar11,uVar4,0,DAT_0005b6f0);
      }
      local_4c = (undefined4)((ulonglong)lVar11 >> 0x20);
      local_50 = (uint)lVar11;
      uVar7 = local_50;
      if (local_38 + 99 < 199) {
        local_50 = param_9 & 2;
        if (local_44 != 0) {
          local_40 = 4;
          goto LAB_0005b772;
        }
        local_40 = 4;
        if (4 < param_8) {
          if (local_50 == 0) {
            local_44 = param_8 - 4;
            local_40 = 4;
          }
          else {
            local_40 = 4;
            local_50 = 2;
          }
        }
LAB_0005b5da:
        if (local_38 == 0) goto LAB_0005b5f0;
      }
      else {
        local_50 = param_9 & 2;
        if (local_44 != 0) {
          local_40 = 5;
LAB_0005b772:
          local_50 = param_9 & 2;
          if ((lVar11 == 0) ||
             ((iVar1 = FUN_0005a9d8(param_5,local_54,DAT_0005b830,DAT_0005b834), iVar1 != 0 &&
              (iVar1 = FUN_0005a9bc(param_5,local_54,0,DAT_0005b838), iVar1 != 0))))
          goto LAB_0005b410;
          if ((param_7 == 0) || ((param_9 & 0x400) == 0)) {
            local_44 = 0;
            if (local_40 < param_8) {
              if (local_50 == 0) goto LAB_0005b804;
              local_44 = 0;
              local_50 = 2;
            }
          }
          else {
            param_7 = param_7 + -1;
            local_44 = 0;
            if (local_40 < param_8) {
              if (local_50 == 0) {
LAB_0005b804:
                local_44 = param_8 - local_40;
              }
              else {
                local_50 = 2;
                local_44 = 0;
              }
            }
          }
          goto LAB_0005b5da;
        }
        local_40 = 5;
        if (5 < param_8) {
          if (local_50 == 0) {
            local_44 = param_8 - 5;
            local_40 = 5;
          }
          else {
            local_50 = 2;
            local_40 = 5;
          }
        }
      }
      uVar12 = FUN_0005a90a(param_5,local_54,uVar7,local_4c);
LAB_0005b5f0:
      local_54 = (uint)((ulonglong)uVar12 >> 0x20);
      local_58 = (undefined4)uVar12;
      iVar1 = FUN_0005a9bc(param_5,param_6,0,0);
      if (iVar1 != 0) {
/* ... truncated ... */
```

### `FUN_0005ea24` @ `0005ea24` score `47`

- reasons: status high-nibble test, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

void FUN_0005ea24(undefined4 *param_1,undefined4 *param_2,uint param_3)

{
  undefined4 *puVar1;
  undefined4 *puVar2;
  uint uVar3;
  uint uVar4;
  int iVar5;
  uint uVar6;
  undefined4 *puVar7;
  bool bVar8;
  
  if ((param_2 < param_1) && (puVar2 = (undefined4 *)((int)param_2 + param_3), param_1 < puVar2)) {
    uVar6 = (int)param_1 + param_3;
    if (3 < param_3) {
      uVar3 = param_3;
      if (((uVar6 | (uint)puVar2) & 3) != 0) goto LAB_0005ea44;
      do {
        *(undefined4 *)((int)param_1 + (uVar3 - 4)) = *(undefined4 *)((int)param_2 + (uVar3 - 4));
        uVar3 = uVar3 - 4;
      } while (3 < uVar3);
      iVar5 = (param_3 >> 2) - 1;
      param_3 = param_3 & 3;
      puVar2 = puVar2 + (-1 - iVar5);
      uVar6 = (uVar6 + iVar5 * -4) - 4;
    }
    if (param_3 == 0) {
      return;
    }
LAB_0005ea44:
    param_3 = param_3 - 1;
    uVar3 = ~param_3;
    do {
      *(undefined1 *)(uVar6 + uVar3 + param_3) = *(undefined1 *)((int)puVar2 + param_3 + uVar3);
      bVar8 = param_3 != 0;
      param_3 = param_3 - 1;
    } while (bVar8);
    return;
  }
  if (3 < param_3) {
    uVar6 = ((uint)param_2 | (uint)param_1) & 3;
    if ((((uint)param_2 | (uint)param_1) & 3) != 0) goto LAB_0005ea64;
    if (0xf < param_3) {
      iVar5 = (param_3 >> 4) - 1;
      puVar7 = param_1 + iVar5 * 4 + 4;
      puVar2 = param_2;
      do {
        *param_1 = *puVar2;
        param_1[1] = puVar2[1];
        param_1[2] = puVar2[2];
        puVar1 = puVar2 + 3;
        puVar2 = puVar2 + 4;
        param_1[3] = *puVar1;
        param_1 = param_1 + 4;
      } while (param_1 != puVar7);
      uVar3 = param_3 & 0xf;
      uVar4 = param_3 & 0xc;
      param_2 = param_2 + iVar5 * 4 + 4;
      param_3 = uVar3;
      if (uVar4 == 0) goto LAB_0005ea5e;
    }
    do {
      *(undefined4 *)((int)param_1 + uVar6) = *(undefined4 *)((int)param_2 + uVar6);
      uVar6 = uVar6 + 4;
    } while (3 < param_3 - uVar6);
    param_2 = param_2 + (param_3 >> 2);
    param_1 = param_1 + (param_3 >> 2);
    param_3 = param_3 & 3;
  }
LAB_0005ea5e:
  if (param_3 == 0) {
    return;
  }
LAB_0005ea64:
  uVar6 = 0;
  do {
    *(undefined1 *)((int)param_1 + uVar6) = *(undefined1 *)((int)param_2 + uVar6);
    uVar6 = uVar6 + 1;
  } while (param_3 != uVar6);
  return;
}
```

### `FUN_00001030` @ `00001030` score `45`

- reasons: channel low-nibble test, zero/nonzero tests, byte packet indexing, known RAM/control state

```c

void FUN_00001030(char *param_1,uint param_2,undefined4 param_3,undefined4 param_4)

{
  undefined1 uVar1;
  int iVar2;
  undefined4 extraout_r2;
  undefined4 extraout_r2_00;
  undefined4 uVar3;
  undefined1 *puVar4;
  uint uVar5;
  undefined1 *puVar6;
  
  iVar2 = FUN_00000e50();
  if (iVar2 == 0) {
    puVar4 = &DAT_000095f4;
  }
  else {
    puVar4 = &DAT_000095f8;
  }
  puVar6 = puVar4 + 4;
  do {
    uVar1 = *puVar4;
    puVar4 = puVar4 + 1;
    FUN_00000d6c(0x20004084,uVar1);
  } while (puVar4 != puVar6);
  if (param_2 != 0) {
    uVar5 = 0;
    uVar3 = extraout_r2;
    do {
      if (-1 < *param_1) {
        FUN_00000d6c(0x20004084,*param_1,uVar3,(int)*param_1,param_4);
        uVar3 = extraout_r2_00;
      }
      uVar5 = uVar5 + 1 & 0xff;
      param_1 = param_1 + 1;
    } while (param_2 != uVar5);
  }
  FUN_00000d6c(0x20004084,0xf7);
  return;
}
```

### `FUN_00002120` @ `00002120` score `45`

- reasons: channel low-nibble test, zero/nonzero tests, byte packet indexing, known RAM/control state

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00002120(int param_1)

{
  ushort uVar1;
  short sVar2;
  int iVar3;
  ushort uVar4;
  int iVar5;
  uint uVar6;
  uint uVar7;
  uint uVar8;
  uint uVar9;
  short sVar10;
  int *piVar11;
  uint uVar12;
  uint uVar13;
  uint uVar14;
  
  if (((DAT_20005a5c == '\0') || (param_1 == 0)) || (uVar14 = (uint)DAT_20005a61, uVar14 == 0)) {
    return;
  }
  uVar13 = 1;
  uVar12 = 0;
  piVar11 = (int *)&DAT_20005a64;
  do {
    while (uVar1 = *(ushort *)(param_1 + uVar12 * 2), (char)piVar11[6] != '\0') {
      if (0x3ff < uVar1) {
        *(undefined2 *)((int)piVar11 + 0x16) = 0x40;
        FUN_00009568(piVar11,0,0x14);
        *(undefined2 *)(piVar11 + 5) = 0;
        *(undefined1 *)(piVar11 + 6) = 0;
        sVar10 = *(short *)((int)piVar11 + 0x16);
LAB_0000219e:
        *(short *)((int)piVar11 + 0x16) = sVar10 + -1;
      }
LAB_000021a2:
      uVar12 = uVar12 + 1;
      piVar11 = piVar11 + 7;
      uVar13 = uVar13 + 5;
      if (uVar14 <= (uVar12 & 0xff)) {
        return;
      }
    }
    *(bool *)(piVar11 + 6) = uVar1 < 0x400;
    if (uVar1 < 0x400) goto LAB_000021a2;
    sVar10 = *(short *)((int)piVar11 + 0x16);
    if (sVar10 != 0) goto LAB_0000219e;
    sVar10 = *(short *)(&DAT_20006494 + uVar12 * 10);
    iVar5 = *piVar11;
    iVar3 = piVar11[1] + (int)*(short *)(&DAT_20006494 + uVar13 * 2);
    uVar6 = uVar13 + 1;
    sVar2 = *(short *)(&DAT_20006494 + uVar6 * 2);
    *piVar11 = sVar10 + iVar5;
    piVar11[2] = piVar11[2] + (int)sVar2;
    uVar1 = _DAT_20005a5e;
    uVar7 = uVar13 + 2;
    piVar11[3] = piVar11[3] + (int)*(short *)(&DAT_20006494 + uVar7 * 2);
    uVar8 = uVar13 + 3;
    sVar2 = *(short *)(&DAT_20006494 + uVar8 * 2);
    piVar11[1] = iVar3;
    piVar11[4] = piVar11[4] + (int)sVar2;
    uVar4 = (short)piVar11[5] + 1;
    *(ushort *)(piVar11 + 5) = uVar4;
    if (uVar4 < uVar1) goto LAB_000021a2;
    uVar9 = (uint)DAT_20005a60;
    uVar14 = uVar12 * 5 & 0xff;
    iVar5 = sVar10 + iVar5 >> uVar9;
    if (iVar5 < 0x15) {
      if (iVar5 < -0x14) {
        FUN_00001ac8(uVar14,0xfffffffb);
        iVar3 = piVar11[1];
        uVar9 = (uint)DAT_20005a60;
      }
    }
    else {
      FUN_00001ac8(uVar14,5);
      iVar3 = piVar11[1];
      uVar9 = (uint)DAT_20005a60;
    }
    *piVar11 = 0;
    if (iVar3 >> uVar9 < 0x15) {
      if (iVar3 >> uVar9 < -0x14) {
        FUN_00001ac8(uVar13 & 0xff,0xfffffffb);
        uVar9 = (uint)DAT_20005a60;
      }
    }
    else {
      FUN_00001ac8(uVar13 & 0xff,5);
      uVar9 = (uint)DAT_20005a60;
    }
    piVar11[1] = 0;
    if (piVar11[2] >> uVar9 < 0x15) {
      if (piVar11[2] >> uVar9 < -0x14) {
        FUN_00001ac8(uVar6 & 0xff,0xfffffffb);
        uVar9 = (uint)DAT_20005a60;
      }
    }
    else {
      FUN_00001ac8(uVar6 & 0xff,5);
      uVar9 = (uint)DAT_20005a60;
    }
    piVar11[2] = 0;
    if (piVar11[3] >> uVar9 < 0x15) {
      if (piVar11[3] >> uVar9 < -0x14) {
        FUN_00001ac8(uVar7 & 0xff,0xfffffffb);
        uVar9 = (uint)DAT_20005a60;
      }
    }
    else {
      FUN_00001ac8(uVar7 & 0xff,5);
      uVar9 = (uint)DAT_20005a60;
    }
    piVar11[3] = 0;
    if (piVar11[4] >> uVar9 < 0x15) {
      if (piVar11[4] >> uVar9 < -0x14) {
        FUN_00001ac8(uVar8 & 0xff,0xfffffffb);
      }
    }
    else {
      FUN_00001ac8(uVar8 & 0xff,5);
    }
    piVar11[4] = 0;
    *(undefined2 *)(piVar11 + 5) = 0;
    uVar14 = (uint)DAT_20005a61;
    uVar12 = uVar12 + 1;
    piVar11 = piVar11 + 7;
    uVar13 = uVar13 + 5;
    if (uVar14 <= (uVar12 & 0xff)) {
      return;
    }
  } while( true );
}
```

### `FUN_0000190c` @ `0000190c` score `41`

- reasons: MIDI status-class constant, zero/nonzero tests, byte packet indexing, known RAM/control state

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_0000190c(void)

{
  undefined4 uVar1;
  int *piVar2;
  int iVar3;
  char cVar4;
  uint local_48;
  uint local_44;
  uint local_40;
  uint local_3c;
  uint local_38;
  uint local_34;
  uint local_30;
  uint local_2c;
  uint local_28;
  uint local_24;
  
  piVar2 = DAT_00009cf4;
  if (DAT_2000462b == '\0') {
    iVar3 = 0x21;
  }
  else {
    iVar3 = 7;
    if (*DAT_00009cf4 == 0x43545355) {
      FUN_00009568(&local_48,0,0x28);
      uVar1 = DAT_00009c74;
      cVar4 = -0x80;
      do {
        iVar3 = FUN_000038e8(uVar1);
        if (iVar3 != 0) {
          return iVar3;
        }
        do {
        } while (DAT_20006465 == '\0');
        DAT_20006465 = '\0';
        iVar3 = FUN_00003ce8(uVar1,0,0,0);
        if (iVar3 != 0) {
          return iVar3;
        }
        iVar3 = piVar2[0xc];
        if (((((((DAT_20004628 != '\0') &&
                (local_48 = local_48 + *(ushort *)(iVar3 + 2), DAT_20004628 != '\x01')) &&
               (local_44 = local_44 + *(ushort *)(iVar3 + 6), DAT_20004628 != '\x02')) &&
              ((local_40 = local_40 + *(ushort *)(iVar3 + 10), DAT_20004628 != '\x03' &&
               (local_3c = local_3c + *(ushort *)(iVar3 + 0xe), DAT_20004628 != '\x04')))) &&
             ((local_38 = local_38 + *(ushort *)(iVar3 + 0x12), DAT_20004628 != '\x05' &&
              ((local_34 = local_34 + *(ushort *)(iVar3 + 0x16), DAT_20004628 != '\x06' &&
               (local_30 = local_30 + *(ushort *)(iVar3 + 0x1a), DAT_20004628 != '\a')))))) &&
            (local_2c = local_2c + *(ushort *)(iVar3 + 0x1e), DAT_20004628 != '\b')) &&
           (local_28 = local_28 + *(ushort *)(iVar3 + 0x22), DAT_20004628 != '\t')) {
          local_24 = local_24 + *(ushort *)(iVar3 + 0x26);
        }
        cVar4 = cVar4 + -1;
      } while (cVar4 != '\0');
      if (((((DAT_20004628 != '\0') && (_DAT_20004600 = local_48 >> 7, DAT_20004628 != '\x01')) &&
           (_DAT_20004604 = local_44 >> 7, DAT_20004628 != '\x02')) &&
          (((_DAT_20004608 = local_40 >> 7, DAT_20004628 != '\x03' &&
            (_DAT_2000460c = local_3c >> 7, DAT_20004628 != '\x04')) &&
           ((_DAT_20004610 = local_38 >> 7, DAT_20004628 != '\x05' &&
            ((_DAT_20004614 = local_34 >> 7, DAT_20004628 != '\x06' &&
             (_DAT_20004618 = local_30 >> 7, DAT_20004628 != '\a')))))))) &&
         ((_DAT_2000461c = local_2c >> 7, DAT_20004628 != '\b' &&
          (_DAT_20004620 = local_28 >> 7, DAT_20004628 != '\t')))) {
        _DAT_20004624 = local_24 >> 7;
      }
      DAT_20004629 = 1;
      iVar3 = 0;
    }
  }
  return iVar3;
}
```

### `FUN_00008944` @ `00008944` score `41`

- reasons: MIDI status-class constant, zero/nonzero tests, byte packet indexing, known RAM/control state

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00008944(void)

{
  bool bVar1;
  undefined4 uVar2;
  int iVar3;
  undefined4 *puVar4;
  undefined1 local_e0;
  undefined1 local_df;
  undefined1 local_de;
  undefined2 local_dc;
  undefined2 local_da;
  undefined1 local_d8;
  undefined1 auStack_d4 [16];
  undefined1 auStack_c4 [20];
  undefined4 auStack_b0 [2];
  undefined1 local_a6;
  char local_a5;
  undefined1 local_a4 [10];
  undefined1 local_9a;
  char local_99;
  undefined1 auStack_98 [132];
  
  iVar3 = FUN_00002fc8();
  uVar2 = DAT_00009c74;
  if (iVar3 != 0) {
    iVar3 = FUN_000038e8(DAT_00009c74);
    if (iVar3 != 0) {
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    do {
    } while (DAT_20006465 == '\0');
    DAT_20006465 = '\0';
    FUN_00003ce8(uVar2,0,&DAT_200064d4);
    FUN_00001b44();
    FUN_00002120(&DAT_200064d4);
    FUN_0000079c();
    iVar3 = FUN_00000864();
    uVar2 = DAT_00009b80;
    if ((iVar3 != 0) && (*(char *)(iVar3 + 0x68) != '\0')) {
      _DAT_2000646c = *(undefined2 *)(iVar3 + 6);
      _DAT_2000646e = *(undefined2 *)(iVar3 + 0x10);
      _DAT_20006470 = *(undefined2 *)(iVar3 + 0x1a);
      _DAT_20006472 = *(undefined2 *)(iVar3 + 0x24);
      _DAT_20006474 = *(undefined2 *)(iVar3 + 0x2e);
      _DAT_20006476 = *(undefined2 *)(iVar3 + 0x38);
      _DAT_20006478 = *(undefined2 *)(iVar3 + 0x42);
      _DAT_2000647a = *(undefined2 *)(iVar3 + 0x4c);
      _DAT_2000647c = *(undefined2 *)(iVar3 + 0x56);
      _DAT_2000647e = *(undefined2 *)(iVar3 + 0x60);
      _DAT_20006468 = *(undefined4 *)(iVar3 + 100);
    }
    iVar3 = FUN_000038e8(DAT_00009b80);
    if (iVar3 == 0) {
      do {
      } while (DAT_20006465 == '\0');
      DAT_20006465 = 0;
      FUN_00003ce8(uVar2,&DAT_200064d8,0);
      iVar3 = FUN_0000308c(0,0x200064a8,&DAT_20006494,0x20006480,auStack_98,0x80);
      if (iVar3 != 0) {
        FUN_00001030(auStack_98,iVar3);
      }
      iVar3 = FUN_00000e50();
      if (iVar3 != 0) {
        return;
      }
      FUN_00008448(1,4000);
      iVar3 = FUN_0000308c(1,DAT_00008e0c,DAT_00008e14,DAT_00008e10,auStack_98,0x80);
      if (iVar3 == 0) {
        return;
      }
      FUN_00001030(auStack_98,iVar3);
      return;
    }
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar3 = FUN_000038e8(DAT_00009c74);
  if (iVar3 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar3 = FUN_00003ce8(uVar2,0,&DAT_200064d4);
  if (iVar3 != 0) goto LAB_00008a54;
  FUN_00001b44();
  FUN_00002120(&DAT_200064d4);
  iVar3 = FUN_00000e50();
  if (iVar3 == 0) {
    if (_DAT_200064d4 < 0x400) {
      _DAT_200064c2 = 0x3ff - _DAT_200064d4;
      if (1000 < _DAT_200064c2) {
        _DAT_200064c2 = 0x3ff;
      }
      DAT_200064bd = '\x01';
      _DAT_200040fc = 4;
    }
    else if (_DAT_200040fc == 0) {
      DAT_200064bd = '\0';
    }
    else {
      _DAT_200040fc = _DAT_200040fc + -1;
    }
    if (_DAT_200064d6 < 0x400) {
      _DAT_200064c0 = _DAT_200064d6;
      if (1000 < (short)_DAT_200064d6) {
        _DAT_200064c0 = 0x3ff;
      }
      DAT_200064bc = '\x01';
      _DAT_200040f8 = 4;
      goto LAB_00008a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00008a54;
    }
  }
  else {
    if (_DAT_200064d4 < 0x400) {
      _DAT_200064c0 = _DAT_200064d4;
      if (1000 < (short)_DAT_200064d4) {
        _DAT_200064c0 = 0x3ff;
      }
      DAT_200064bc = '\x01';
      _DAT_200040f8 = 4;
      goto LAB_00008a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00008a54;
    }
  }
  DAT_200064bc = (char)_DAT_200040f8;
LAB_00008a54:
  uVar2 = DAT_00009b80;
  iVar3 = FUN_000038e8(DAT_00009b80);
  if (iVar3 == 0) {
    do {
    } while (DAT_20006465 == '\0');
    DAT_20006465 = 0;
    FUN_00003ce8(uVar2,&DAT_200064d8,0);
    if (DAT_200064bc != '\0') {
      _DAT_200064d8 = _DAT_200064d8 | 0x200;
    }
    if (DAT_200064bd != '\0') {
      _DAT_200064d8 = _DAT_200064d8 | 0x400;
    }
    FUN_0000134c();
    FUN_0000140c();
    FUN_00001618(&DAT_200064c0);
    FUN_00001288(&DAT_200064c0);
/* ... truncated ... */
```

### `FUN_0000557c` @ `0000557c` score `39`

- reasons: channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_0000557c(undefined4 *param_1,char *param_2)

{
  char cVar1;
  int iVar2;
  uint uVar3;
  uint uVar4;
  uint uVar5;
  int local_14;
  
  cVar1 = *param_2;
  param_1[1] = param_2;
  if (cVar1 != '\0') {
    FUN_00008600((int)param_2[0x11],param_2[0x10],param_1);
  }
  *(undefined1 *)(param_1 + 0xd) = 0;
  iVar2 = _DAT_20006244;
  uVar3 = (_DAT_4001e020 & 0x7ffffff) >> 0x18;
  uVar5 = (uint)(_DAT_20006244 << uVar3) >> uVar3;
  param_1[3] = uVar5;
  uVar3 = _DAT_4001e020;
  if (uVar5 < 4000000) {
    if (((uVar5 != 1000000) && (uVar5 != 2000000)) && (uVar5 != 3000000)) {
      return 0x1f6;
    }
    uVar3 = (_DAT_4001e020 & 0x7ffffff) >> 0x18;
    uVar3 = (uint)(iVar2 << uVar3) >> uVar3;
    param_1[3] = (uVar5 + 999999) / 1000000;
  }
  else {
    uVar4 = (uVar5 + 999999) / 1000000;
    param_1[3] = uVar4;
    if ((32999999 < uVar5 + 999999) && ((int)(uVar4 << 0x1f) < 0)) {
      param_1[3] = uVar4 + 1;
    }
    uVar3 = (uVar3 & 0x7ffffff) >> 0x18;
    uVar3 = (uint)(iVar2 << uVar3) >> uVar3;
  }
  uVar3 = (uVar3 + 999999) / 1000000;
  param_1[4] = (uVar3 * 0x583) / 6;
  param_1[5] = (uVar3 * 0x376) / 6;
  param_1[6] = (uVar3 * 0x58) / 6;
  param_1[7] = (uVar3 * 0x56ab8) / 6;
  param_1[8] = (uVar3 * 0x7b0c0) / 6;
  param_1[9] = (uVar3 * 0x22ed68) / 6;
  param_1[2] = uVar3;
  DAT_407effc0 = 0;
  if (DAT_407ec090 != '\x01') {
    DAT_407ec090 = '\x01';
    FUN_00005138(6,uVar3);
  }
  _DAT_407effb0 = (short)DAT_00005800;
  FUN_00005138(6,uVar3);
  _DAT_407ec180 = 0xa5;
  DAT_407ec100 = 0x10;
  FUN_00005138(3,param_1[2]);
  if (*(char *)param_1[1] != '\0') {
    FUN_00008598((int)((char *)param_1[1])[0x11]);
  }
  uVar3 = param_1[3];
  if (uVar3 < 0x20) {
    _DAT_407ec1d8 = _DAT_407ec1d8 & 0xffffffc0 | uVar3 - 1 & 0x1f;
  }
  else {
    _DAT_407ec1d8 = (uVar3 - 0x20 >> 1) + 0x1f & 0x3f | _DAT_407ec1d8 & 0xffffffc0;
  }
  local_14 = 0x4b00;
  _DAT_407ec180 = 0xa5;
  DAT_407ec100 = 8;
  FUN_00005138(0x10,param_1[2]);
  _DAT_407effb0 = (short)DAT_00005804;
  while( true ) {
    if (_DAT_407effb0 == 0) {
      *param_1 = 0x4f50454e;
      return 0;
    }
    if (local_14 == 0) break;
    local_14 = local_14 + -1;
  }
  return 0x14;
}
```

### `FUN_00024b84` @ `00024b84` score `39`

- reasons: channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing

```c

undefined4 FUN_00024b84(short param_1)

{
  char cVar1;
  char *pcVar2;
  undefined1 *puVar3;
  int iVar4;
  int *piVar5;
  ushort uVar6;
  ushort uVar7;
  byte bVar8;
  ushort uVar9;
  ushort *puVar10;
  undefined2 uVar11;
  ushort uVar12;
  uint uVar13;
  short sVar14;
  byte *pbVar15;
  ushort *puVar16;
  ushort *puVar17;
  
  puVar16 = DAT_00024d34;
  pcVar2 = DAT_00024d14;
  if ((*DAT_00024d14 == '\x01') &&
     (uVar6 = *DAT_00024d34, *DAT_00024d34 = uVar6 + param_1, 1999 < (ushort)(uVar6 + param_1))) {
    *puVar16 = 0;
    *pcVar2 = '\0';
  }
  uVar6 = FUN_00025eb8();
  piVar5 = DAT_00024d2c;
  puVar16 = DAT_00024d28;
  iVar4 = DAT_00024d1c;
  puVar3 = DAT_00024d18;
  if ((short)uVar6 < 0) {
    if (*DAT_00024d28 != 0) {
      uVar13 = 0;
      pbVar15 = DAT_00024d20;
      puVar17 = DAT_00024d24;
      do {
        *puVar3 = 0;
        puVar10 = DAT_00024d30;
        uVar12 = *(ushort *)(uVar13 * 2 + *piVar5);
        uVar9 = uVar6 & 0x7fff ^ uVar12;
        uVar7 = uVar9 & 0x3800;
        if ((uVar9 & 0x3800) == 0) {
          if ((uVar12 & ~(uVar6 & 0x7fff | 0x3800)) == 0) {
            if ((*pbVar15 == 0) && (uVar12 = *DAT_00024d30, uVar12 < 2)) {
              *pbVar15 = 2;
              *puVar3 = 1;
              *puVar17 = uVar7;
              uVar12 = uVar12 + 1;
              uVar7 = 2;
              goto LAB_00024cce;
            }
          }
          else if (*pbVar15 != 0) {
            *puVar3 = 1;
            puVar10 = DAT_00024d30;
            *pbVar15 = 0;
            uVar12 = *puVar10 - 1;
LAB_00024cce:
            *puVar10 = uVar12;
            iVar4 = DAT_00024d1c;
            *(ushort *)(DAT_00024d1c + 4) = uVar7;
            *(short *)(iVar4 + 2) = (short)uVar13;
            FUN_00020264(2,0);
          }
        }
        uVar13 = uVar13 + 1;
        pbVar15 = pbVar15 + 1;
        puVar17 = puVar17 + 1;
      } while ((uVar13 & 0xffff) < (uint)*puVar16);
    }
  }
  else {
    sVar14 = 0;
    pbVar15 = DAT_00024d20;
    puVar16 = DAT_00024d24;
    do {
      while( true ) {
        *puVar3 = 0;
        uVar13 = (uint)*pbVar15;
        if (uVar13 != 2) break;
        uVar6 = *puVar16 + param_1;
        cVar1 = *pcVar2;
        *puVar16 = uVar6;
        if (cVar1 == '\x01') {
          if (uVar6 < 0x7d1) goto LAB_00024bc6;
          uVar11 = 1;
          bVar8 = 1;
        }
        else {
          if (uVar6 < 0x3e9) goto LAB_00024bc6;
          bVar8 = 3;
          uVar11 = 3;
        }
LAB_00024bf4:
        *pbVar15 = bVar8;
        *puVar3 = 1;
        *(short *)(iVar4 + 2) = sVar14;
        sVar14 = sVar14 + 1;
        *puVar16 = 0;
        *(undefined2 *)(iVar4 + 4) = uVar11;
        pbVar15 = pbVar15 + 1;
        FUN_00020264(2,0);
        puVar16 = puVar16 + 1;
        if (sVar14 == 200) {
          return 0;
        }
      }
      if (uVar13 < 3) {
        if (uVar13 == 1) {
          *pbVar15 = 0;
        }
      }
      else if ((uVar13 - 3 < 2) &&
              (uVar6 = *puVar16, *puVar16 = uVar6 + param_1, 0x28 < (ushort)(uVar6 + param_1))) {
        bVar8 = 4;
        uVar11 = 4;
        goto LAB_00024bf4;
      }
LAB_00024bc6:
      sVar14 = sVar14 + 1;
      pbVar15 = pbVar15 + 1;
      puVar16 = puVar16 + 1;
    } while (sVar14 != 200);
  }
  return 0;
}
```

### `FUN_00046e7c` @ `00046e7c` score `39`

- reasons: channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing

```c

uint FUN_00046e7c(char *param_1,uint param_2,int param_3,int param_4,int param_5,int *param_6,
                 byte param_7)

{
  uint uVar1;
  int iVar2;
  uint uVar3;
  uint uVar4;
  uint uVar5;
  int iVar6;
  undefined4 uVar7;
  int iVar8;
  char *pcVar9;
  uint uVar10;
  uint uVar11;
  uint uVar12;
  int iVar13;
  int iVar14;
  int iVar15;
  int iVar16;
  int iVar17;
  uint uVar18;
  char cVar19;
  int local_68;
  uint local_54;
  int local_50;
  uint local_4c;
  int local_44;
  uint local_34;
  int local_30;
  int local_2c [2];
  
  iVar8 = DAT_000471a4;
  uVar12 = (uint)param_7;
  if ((param_7 & 3) == 0) {
    uVar18 = 0;
    local_4c = 0;
    cVar19 = '\0';
    local_44 = 0;
    local_34 = uVar12 & 3;
    do {
      uVar3 = uVar18;
      uVar1 = local_34;
      if (((param_2 <= uVar18) || (pcVar9 = param_1 + uVar18, param_1[uVar18] == '\0')) ||
         (param_5 < 1)) goto joined_r0x0004704a;
      local_54 = uVar12;
      if (uVar18 == 0) {
        local_54 = uVar12 | 4;
      }
      if (param_3 == 0) goto joined_r0x0004704a;
      local_30 = 0;
      uVar4 = FUN_00046bb4(pcVar9,&local_30);
      local_2c[0] = local_30;
      if (*pcVar9 == '\0') {
        iVar6 = local_30;
        local_50 = 0;
      }
      else {
        iVar13 = 0;
        local_50 = 0;
        local_68 = 0;
        iVar14 = 0;
        iVar16 = -1;
        do {
          local_30 = local_2c[0];
          uVar5 = FUN_00046bb4(pcVar9,local_2c);
          iVar15 = iVar14 + 1;
          iVar17 = iVar16;
          if ((local_54 & 8) == 0) {
LAB_00046f98:
            iVar6 = FUN_000436fc(param_3,uVar4,uVar5);
            iVar13 = iVar13 + iVar6;
            if (iVar6 != 0) {
              iVar13 = iVar13 + param_4;
            }
            if (((iVar16 != -1) || (iVar13 - param_4 <= param_5)) ||
               (iVar17 = local_68, -1 < (int)(local_54 << 0x1d))) {
              iVar6 = iVar17;
              uVar1 = local_34;
              if (uVar4 == 10) {
LAB_00046fe6:
                if (local_68 == 0) {
                  if (iVar17 != -1) goto LAB_00047112;
                  iVar6 = local_30;
                  local_50 = iVar13;
                  if (iVar14 == 0) goto LAB_00047004;
                  local_44 = local_44 + iVar13;
                  goto joined_r0x0004704a;
                }
                if (iVar17 != -1) goto LAB_00047112;
                iVar6 = local_30;
                if (iVar14 == 0) goto LAB_00047004;
              }
              else {
                if (uVar4 != 0xd) {
                  uVar11 = 0;
                  uVar10 = 0x20;
                  do {
                    if (uVar10 == uVar4) goto LAB_00046fe6;
                    uVar11 = uVar11 + 1 & 0xff;
                    uVar10 = (uint)*(byte *)(iVar8 + uVar11);
                  } while (uVar10 != 0);
                  if (((uVar5 == 0) ||
                      (((0x51ff < uVar5 + DAT_000471a8 && (0x5d < uVar5 + DAT_000471ac)) &&
                       ((0xff < uVar5 + DAT_000471b0 &&
                        ((((0x7f < uVar5 + DAT_000471b4 && (0x2f < uVar5 + DAT_000471b8)) &&
                          (0xf < uVar5 + DAT_000471bc)) && (0x1f < uVar5 + DAT_000471c0)))))))) &&
                     ((uVar4 == 0 ||
                      (((0x51ff < uVar4 + DAT_000471a8 && (0x5d < uVar4 + DAT_000471ac)) &&
                       ((((0xff < uVar4 + DAT_000471b0 &&
                          ((0x7f < uVar4 + DAT_000471b4 && (0x2f < uVar4 + DAT_000471b8)))) &&
                         (0xf < uVar4 + DAT_000471bc)) && (0x1f < uVar4 + DAT_000471c0)))))))) {
                    if (iVar17 == -1) {
                      local_50 = iVar13;
                    }
                    goto LAB_000470f8;
                  }
                  iVar6 = local_30;
                  local_50 = iVar13;
                  if ((iVar17 == -1) || (iVar6 = iVar17, (int)(local_54 << 0x1d) < 0))
                  goto LAB_00047004;
                  goto joined_r0x0004704a;
                }
                if (local_68 == 0) {
                  if (iVar17 != -1) goto LAB_00047112;
                  iVar6 = local_30;
                  local_50 = iVar13;
                  if ((iVar14 == 0) || (uVar5 == 10)) goto LAB_00047004;
                  local_44 = local_44 + iVar13;
                  uVar3 = local_34;
                  goto joined_r0x0004704a;
                }
                if (iVar17 != -1) goto LAB_00047112;
                iVar6 = local_30;
                if ((iVar14 == 0) || (uVar5 == 10)) goto LAB_00047004;
              }
              local_44 = local_44 + local_50;
              goto LAB_00047014;
            }
            iVar6 = local_68;
            if (((local_68 != -1) || (iVar6 = local_30, iVar15 == 0)) ||
               ((uVar4 == 0xd && (uVar5 == 10)))) goto LAB_00047004;
            local_44 = local_44 + local_50;
            local_68 = iVar16;
            goto LAB_00047014;
          }
          if (uVar4 == 0x23) {
            cVar19 = local_4c != 2;
            local_4c = (uint)(byte)cVar19;
          }
          else {
            if (cVar19 != '\x01') goto LAB_00046f98;
            if (uVar4 == 0x20) {
              local_4c = 2;
              cVar19 = '\x02';
            }
          }
LAB_000470f8:
          iVar2 = local_30;
/* ... truncated ... */
```

### `FUN_0005dc60` @ `0005dc60` score `39`

- reasons: channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing

```c

undefined4 FUN_0005dc60(int *param_1,undefined4 param_2,uint param_3,uint param_4)

{
  uint uVar1;
  undefined4 uVar2;
  uint uVar3;
  
  uVar3 = (uint)*(ushort *)(param_1 + 1);
  uVar1 = param_3 - param_4 & 0xffff;
  if (param_3 < param_4) {
    uVar1 = uVar1 + uVar3 * 2 & 0xffff;
  }
  uVar2 = 0;
  if (uVar1 != 0) {
    if (uVar3 < uVar1) {
      if (param_3 < uVar3) {
        param_3 = uVar3 + param_3;
        *(short *)((int)param_1 + 10) = (short)param_3;
      }
      else {
        param_3 = param_3 - uVar3;
        *(short *)((int)param_1 + 10) = (short)param_3;
      }
      param_4 = param_3 & 0xffff;
    }
    for (; uVar3 <= param_4; param_4 = param_4 - uVar3 & 0xffff) {
    }
    FUN_0005aef8(param_2,*param_1 + (*(ushort *)((int)param_1 + 6) & 0x7fff) * param_4);
    uVar2 = 1;
  }
  return uVar2;
}
```

### `FUN_0005dcb4` @ `0005dcb4` score `39`

- reasons: channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing

```c

uint FUN_0005dcb4(int *param_1,int param_2,uint param_3,uint param_4,ushort param_5)

{
  int iVar1;
  ushort uVar2;
  uint uVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  uint uVar7;
  
  uVar4 = (uint)param_5;
  uVar7 = (uint)*(ushort *)(param_1 + 1);
  uVar5 = param_4 - uVar4 & 0xffff;
  if (param_4 < uVar4) {
    uVar5 = uVar5 + uVar7 * 2 & 0xffff;
  }
  uVar6 = 0;
  if (uVar5 != 0) {
    if (uVar7 < uVar5) {
      uVar5 = uVar7;
      if (uVar7 <= param_4) {
        uVar5 = -uVar7;
      }
      uVar4 = uVar5 + param_4 & 0xffff;
      *(short *)((int)param_1 + 10) = (short)(uVar5 + param_4);
      uVar5 = uVar7;
    }
    uVar2 = (ushort)uVar5;
    if (param_3 < uVar5) {
      uVar2 = (ushort)param_3;
    }
    uVar6 = (uint)uVar2;
    for (; uVar7 <= uVar4; uVar4 = uVar4 - uVar7 & 0xffff) {
    }
    uVar5 = *(ushort *)((int)param_1 + 6) & 0x7fff;
    uVar3 = uVar7 - uVar4 & 0xffff;
    iVar1 = *param_1 + uVar4 * uVar5;
    if (uVar3 < uVar6) {
      uVar3 = uVar5 * uVar3 & 0xffff;
      FUN_0005aef8(param_2,iVar1,uVar3);
      FUN_0005aef8(param_2 + uVar3,*param_1,uVar5 * (uVar4 + (uVar6 - uVar7)) & 0xffff);
    }
    else {
      FUN_0005aef8(param_2,iVar1,uVar6 * uVar5);
    }
  }
  return uVar6;
}
```

### `FUN_0005df68` @ `0005df68` score `39`

- reasons: channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing

```c

uint FUN_0005df68(int *param_1,int param_2,uint param_3)

{
  ushort uVar1;
  uint uVar2;
  uint uVar3;
  uint uVar4;
  int iVar5;
  uint uVar6;
  uint uVar7;
  int local_2c;
  
  if (param_3 == 0) {
    return 0;
  }
  if (param_1[3] != 0) {
    FUN_0005efe8(param_1[3],0xffffffff);
  }
  uVar3 = (uint)*(ushort *)(param_1 + 2);
  uVar7 = (uint)*(ushort *)(param_1 + 1);
  uVar4 = (uint)*(ushort *)((int)param_1 + 10);
  if (*(char *)((int)param_1 + 7) < '\0') {
    if (param_3 < uVar7) {
      if (uVar3 < uVar4) {
        iVar5 = uVar7 * 2 - uVar4;
      }
      else {
        iVar5 = -uVar4;
      }
      uVar2 = uVar7 * 2;
      local_2c = param_3 - uVar7;
      if ((int)((uVar3 + iVar5 & 0xffff) + param_3) < (int)uVar2) goto LAB_0005dfc2;
      uVar6 = uVar4 + uVar7 & 0xffff;
      uVar3 = uVar6 - param_3 & 0xffff;
      if ((uVar3 < uVar4) || (uVar2 - uVar3 == 0 || uVar2 < uVar3)) {
        uVar3 = uVar3 + uVar7 * -2 & 0xffff;
        uVar6 = param_3 + uVar3 & 0xffff;
      }
      uVar2 = (uint)*(ushort *)((int)param_1 + 6);
      uVar4 = uVar3;
    }
    else {
      if (uVar7 == 0) goto LAB_0005e010;
      uVar2 = (uint)*(ushort *)((int)param_1 + 6);
      param_2 = param_2 + (param_3 - uVar7) * (uVar2 & 0x7fff);
      uVar6 = uVar4 + uVar7 & 0xffff;
      local_2c = 0;
      uVar3 = uVar4;
      param_3 = uVar7;
    }
  }
  else {
    if (uVar3 < uVar4) {
      iVar5 = uVar7 * 2 - uVar4;
    }
    else {
      iVar5 = -uVar4;
    }
    uVar4 = uVar3 + iVar5 & 0xffff;
    if (uVar7 <= uVar4) {
      uVar7 = 0;
      goto LAB_0005e010;
    }
    uVar4 = uVar7 - uVar4;
    uVar1 = (ushort)uVar4;
    if (param_3 < (uVar4 & 0xffff)) {
      uVar1 = (ushort)param_3;
    }
    param_3 = (uint)uVar1;
    local_2c = param_3 - uVar7;
LAB_0005dfc2:
    uVar6 = param_3 + uVar3 & 0xffff;
    uVar2 = (uint)*(ushort *)((int)param_1 + 6);
    uVar4 = uVar3;
  }
  for (; uVar7 <= uVar4; uVar4 = uVar4 - uVar7 & 0xffff) {
  }
  uVar2 = uVar2 & 0x7fff;
  uVar7 = uVar7 - uVar4 & 0xffff;
  iVar5 = *param_1 + uVar4 * uVar2;
  if (uVar7 < param_3) {
    uVar7 = uVar2 * uVar7 & 0xffff;
    FUN_0005aef8(iVar5,param_2,uVar7);
    FUN_0005aef8(*param_1,param_2 + uVar7,uVar2 * (uVar4 + local_2c) & 0xffff);
  }
  else {
    FUN_0005aef8(iVar5,param_2,param_3 * uVar2);
  }
  if ((uVar6 < uVar3) || ((uint)*(ushort *)(param_1 + 1) * 2 <= uVar6)) {
    uVar6 = uVar6 + (uint)*(ushort *)(param_1 + 1) * -2;
  }
  *(short *)(param_1 + 2) = (short)uVar6;
  uVar7 = param_3;
LAB_0005e010:
  if (param_1[3] != 0) {
    FUN_0005ef98();
  }
  return uVar7;
}
```

### `FUN_0005e274` @ `0005e274` score `39`

- reasons: channel low-nibble test, velocity/value 127, zero/nonzero tests, byte packet indexing

```c

int * FUN_0005e274(undefined4 *param_1,uint param_2)

{
  uint *puVar1;
  uint uVar2;
  int *piVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  uint uVar7;
  uint uVar8;
  int iVar9;
  int *piVar10;
  int *piVar11;
  int *piVar12;
  uint uVar13;
  int iVar14;
  uint uVar15;
  uint uVar16;
  uint uVar17;
  int iVar18;
  uint *local_30;
  
  uVar16 = param_2 + 0xb;
  if (uVar16 < 0x17) {
    if (0x10 < param_2) {
LAB_0005e434:
      *param_1 = 0xc;
      return (int *)0x0;
    }
    FUN_0005e7d8();
    uVar17 = 0x10;
    iVar9 = 0x18;
    uVar16 = 2;
  }
  else {
    uVar17 = uVar16 & 0xfffffff8;
    if (((int)uVar17 < 0) || (uVar17 < param_2)) goto LAB_0005e434;
    FUN_0005e7d8();
    if (0x1f7 < uVar17) {
      uVar5 = uVar16 >> 9;
      if (uVar5 == 0) {
        uVar15 = 0x3f;
        uVar5 = 0x40;
        iVar9 = 0x200;
      }
      else if (uVar5 < 5) {
        uVar15 = (uVar16 >> 6) + 0x38;
        uVar5 = (uVar16 >> 6) + 0x39;
        iVar9 = uVar5 * 8;
      }
      else if (uVar5 < 0x15) {
        uVar15 = uVar5 + 0x5b;
        uVar5 = uVar5 + 0x5c;
        iVar9 = uVar5 * 8;
      }
      else if (uVar5 < 0x55) {
        uVar15 = (uVar16 >> 0xc) + 0x6e;
        uVar5 = (uVar16 >> 0xc) + 0x6f;
        iVar9 = uVar5 * 8;
      }
      else if (uVar5 < 0x155) {
        uVar15 = (uVar16 >> 0xf) + 0x77;
        uVar5 = (uVar16 >> 0xf) + 0x78;
        iVar9 = uVar5 * 8;
      }
      else if (DAT_0005e7d4 < uVar5) {
        uVar5 = 0x7f;
        uVar15 = 0x7e;
        iVar9 = 0x3f8;
      }
      else {
        uVar15 = (uVar16 >> 0x12) + 0x7c;
        uVar5 = (uVar16 >> 0x12) + 0x7d;
        iVar9 = uVar5 * 8;
      }
      iVar14 = *(int *)(DAT_0005e5c4 + iVar9 + 4);
      do {
        iVar18 = iVar14;
        uVar16 = uVar5;
        if (DAT_0005e5c4 + iVar9 + -8 == iVar18) goto LAB_0005e340;
        uVar2 = *(uint *)(iVar18 + 4) & 0xfffffffc;
        uVar16 = uVar15;
        if (0xf < (int)(uVar2 - uVar17)) goto LAB_0005e340;
        iVar14 = *(int *)(iVar18 + 0xc);
      } while ((int)(uVar2 - uVar17) < 0);
      iVar9 = *(int *)(iVar18 + 8);
      *(int *)(iVar9 + 0xc) = iVar14;
      *(int *)(iVar14 + 8) = iVar9;
      goto LAB_0005e2ba;
    }
    uVar16 = uVar16 >> 3;
    iVar9 = uVar17 + 8;
  }
  iVar9 = DAT_0005e5c4 + iVar9;
  iVar18 = *(int *)(iVar9 + 4);
  if (iVar18 == iVar9 + -8) {
    iVar18 = *(int *)(iVar9 + 0xc);
    uVar16 = uVar16 + 2;
    if (iVar9 == iVar18) {
LAB_0005e340:
      uVar5 = DAT_0005e5c4;
      iVar18 = *(int *)(DAT_0005e5c4 + 0x10);
      iVar9 = DAT_0005e5c4 + 8;
      if (iVar18 == iVar9) {
        uVar15 = *(uint *)(DAT_0005e5c4 + 4);
      }
      else {
        uVar13 = *(uint *)(iVar18 + 4);
        uVar2 = uVar13 & 0xfffffffc;
        uVar15 = uVar2 - uVar17;
        if (0xf < (int)uVar15) {
          iVar14 = iVar18 + uVar17;
          *(uint *)(iVar18 + 4) = uVar17 | 1;
          *(int *)(uVar5 + 0x10) = iVar14;
          *(int *)(uVar5 + 0x14) = iVar14;
          *(int *)(iVar14 + 0xc) = iVar9;
          *(int *)(iVar14 + 8) = iVar9;
          *(uint *)(iVar14 + 4) = uVar15 | 1;
          *(uint *)(iVar18 + uVar2) = uVar15;
          FUN_0005e7e8(param_1);
          return (int *)(iVar18 + 8);
        }
        *(int *)(DAT_0005e5c4 + 0x10) = iVar9;
        *(int *)(uVar5 + 0x14) = iVar9;
        if (-1 < (int)uVar15) goto LAB_0005e2ba;
        uVar15 = *(uint *)(uVar5 + 4);
        if (uVar2 < 0x200) {
          uVar15 = uVar15 | 1 << (uVar13 >> 5 & 0xff);
          iVar14 = (uVar13 & 0xfffffff8) + uVar5;
          iVar9 = *(int *)(iVar14 + 8);
          *(uint *)(uVar5 + 4) = uVar15;
          *(int *)(iVar18 + 0xc) = iVar14;
          *(int *)(iVar18 + 8) = iVar9;
          *(int *)(iVar14 + 8) = iVar18;
          *(int *)(iVar9 + 0xc) = iVar18;
        }
        else {
          uVar7 = uVar13 >> 9;
          if (uVar7 < 5) {
            iVar9 = (uVar13 >> 6) + 0x38;
            iVar14 = ((uVar13 >> 6) + 0x39) * 8;
          }
          else if (uVar7 < 0x15) {
            iVar9 = uVar7 + 0x5b;
            iVar14 = (uVar7 + 0x5c) * 8;
          }
          else if (uVar7 < 0x55) {
            iVar9 = (uVar13 >> 0xc) + 0x6e;
            iVar14 = ((uVar13 >> 0xc) + 0x6f) * 8;
          }
          else if (uVar7 < 0x155) {
            iVar9 = (uVar13 >> 0xf) + 0x77;
            iVar14 = ((uVar13 >> 0xf) + 0x78) * 8;
          }
          else if (DAT_0005e7d4 < uVar7) {
            iVar9 = 0x7e;
            iVar14 = 0x3f8;
          }
/* ... truncated ... */
```

### `FUN_00000eec` @ `00000eec` score `38`

- reasons: channel low-nibble test, velocity/value 127, known RAM/control state

```c

void FUN_00000eec(uint param_1,uint param_2,undefined4 param_3,undefined4 param_4)

{
  undefined4 extraout_r2;
  undefined4 extraout_r2_00;
  undefined4 extraout_r2_01;
  undefined4 uVar1;
  uint uVar2;
  uint extraout_r3;
  uint extraout_r3_00;
  
  uVar2 = (uint)DAT_20004081;
  if (uVar2 != param_1) {
    DAT_20004081 = (byte)param_1;
    FUN_00000d6c(0x20004084,param_1 - 0x50 & 0xff,param_3,uVar2,param_4);
    uVar2 = extraout_r3;
    param_3 = extraout_r2;
  }
  FUN_00000d6c(0x20004084,0x16,param_3,uVar2,param_4);
  FUN_00000d6c(0x20004084,(int)param_2 >> 7 & 0x7f);
  uVar2 = (uint)DAT_20004081;
  uVar1 = extraout_r2_00;
  if (uVar2 != param_1) {
    DAT_20004081 = (byte)param_1;
    FUN_00000d6c(0x20004084,param_1 - 0x50 & 0xff,extraout_r2_00,uVar2,param_4);
    uVar2 = extraout_r3_00;
    uVar1 = extraout_r2_01;
  }
  FUN_00000d6c(0x20004084,0x36,uVar1,uVar2,param_4);
  FUN_00000d6c(0x20004084,param_2 & 0x7f);
  return;
}
```

### `FUN_000047f0` @ `000047f0` score `37`

- reasons: MIDI status-class constant, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

int FUN_000047f0(int param_1,ushort *param_2,int param_3,undefined4 param_4)

{
  int iVar1;
  uint uVar2;
  uint uVar3;
  uint uVar4;
  int iVar5;
  undefined4 *puVar6;
  
  iVar1 = *(int *)(param_1 + 0x20);
  uVar4 = (uint)*(byte *)(param_1 + 2);
  iVar5 = *(int *)(param_1 + 0x1c);
  *(byte *)(iVar1 + 2) = *(byte *)(iVar1 + 2) & 0x7b;
  uVar3 = uVar4 & 3;
  puVar6 = *(undefined4 **)(iVar5 + 0x10);
  uVar2 = param_3 - uVar3;
  *(uint *)(param_1 + 0x10) = uVar2;
  *(undefined1 **)(param_1 + 0xc) = (undefined1 *)((int)param_2 + uVar3);
  if ((puVar6 != (undefined4 *)0x0) && (uVar2 != 0)) {
    iVar1 = puVar6[2];
    *(undefined4 *)(param_1 + 0x10) = 0;
    iVar1 = (**(code **)(iVar1 + 8))
                      (*puVar6,(undefined1 *)((int)param_2 + uVar3),0,
                       uVar2 >> (uVar3 - 1 & 0xff) & 0xffff,param_4);
    if (iVar1 != 0) {
      return iVar1;
    }
    iVar1 = *(int *)(param_1 + 0x20);
    uVar4 = (uint)*(byte *)(param_1 + 2);
  }
  *(byte *)(iVar1 + 2) = *(byte *)(iVar1 + 2) | 0x80;
  if ((uVar4 & 3) == 2) {
    *(ushort *)(iVar1 + 0xe) = *param_2 | 0xfe00;
  }
  else {
    *(char *)(iVar1 + 3) = (char)*param_2;
  }
  return 0;
}
```

### `FUN_00004e18` @ `00004e18` score `37`

- reasons: MIDI status-class constant, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00004e18(short *param_1)

{
  short sVar1;
  bool bVar2;
  uint *puVar3;
  short sVar4;
  uint uVar5;
  uint uVar6;
  int iVar7;
  
  uVar6 = DAT_00004eec;
  uVar5 = 0;
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    uVar5 = isIRQinterruptsEnabled();
  }
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    enableIRQinterrupts(1);
  }
  if (_DAT_200061b8 == 0) {
    DAT_40040d03 = 0x40;
  }
  _DAT_200061b8 = _DAT_200061b8 + 1;
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    enableIRQinterrupts((uVar5 & 1) == 1);
  }
  sVar1 = *param_1;
  if (sVar1 != 0) {
    sVar4 = 0;
    puVar3 = *(uint **)(param_1 + 2);
    do {
      uVar5 = *puVar3;
      iVar7 = ((uint)(ushort)((ushort)puVar3[1] >> 8) * 0x10 + ((ushort)puVar3[1] & 0xff)) * 4;
      if ((uVar5 & 0x10000) != 0) {
        *(uint *)(&DAT_40040800 + iVar7) = *(uint *)(&DAT_40040800 + iVar7) & uVar6;
        *(uint *)(&DAT_40040800 + iVar7) = uVar5 & uVar6;
      }
      sVar4 = sVar4 + 1;
      *(uint *)(&DAT_40040800 + iVar7) = uVar5;
      puVar3 = puVar3 + 2;
    } while (sVar4 != sVar1);
  }
  uVar6 = 0;
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    uVar6 = isIRQinterruptsEnabled();
  }
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    enableIRQinterrupts(1);
  }
  if (_DAT_200061b8 != 0) {
    _DAT_200061b8 = _DAT_200061b8 + -1;
  }
  if (_DAT_200061b8 == 0) {
    DAT_40040d03 = 0x80;
  }
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    enableIRQinterrupts((uVar6 & 1) == 1);
  }
  return;
}
```

### `FUN_00004f2c` @ `00004f2c` score `37`

- reasons: MIDI status-class constant, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_00004f2c(undefined4 *param_1,char *param_2)

{
  char cVar1;
  byte bVar2;
  bool bVar3;
  int iVar4;
  int iVar5;
  uint uVar6;
  undefined4 uVar7;
  undefined4 *puVar8;
  int iVar9;
  
  uVar6 = (uint)(byte)param_2[0x10];
  param_1[3] = 1 << uVar6;
  *(char *)(param_1 + 4) = '\x01' - (uVar6 == 0);
  param_1[2] = (uVar6 + 0x400780) * 0x100;
  iVar9 = *(int *)(param_2 + 0x1c);
  param_1[5] = *(undefined4 *)(param_2 + 0x14);
  uVar7 = *(undefined4 *)(param_2 + 0x18);
  param_1[1] = param_2;
  param_1[7] = uVar7;
  param_1[6] = 0;
  uVar6 = 0;
  bVar3 = (bool)isCurrentModePrivileged();
  if (bVar3) {
    uVar6 = isIRQinterruptsEnabled();
  }
  bVar3 = (bool)isCurrentModePrivileged();
  if (bVar3) {
    enableIRQinterrupts(1);
  }
  _DAT_40047008 = (-(uint)(param_2[0x10] != '\0') & 0xffffffe0) - 0x21 & _DAT_40047008;
  bVar3 = (bool)isCurrentModePrivileged();
  if (bVar3) {
    enableIRQinterrupts((uVar6 & 1) == 1);
  }
  puVar8 = (undefined4 *)param_1[2];
  cVar1 = *param_2;
  *puVar8 = &DAT_0000a500;
  puVar8[0xb] = 0;
  puVar8[0xf] = 0;
  puVar8[0x12] = 0;
  iVar4 = *(int *)(param_2 + 4);
  uVar6 = (uint)((byte)param_2[8] >> 1) << 0x18;
  if (cVar1 == '\x03') {
    uVar6 = uVar6 | 0x10000;
  }
  puVar8[0xb] = uVar6;
  puVar8[4] = 0x80000000;
  puVar8[5] = 0x80000000;
  puVar8[6] = 0x80000000;
  puVar8[9] = 0;
  puVar8[10] = 0;
  puVar8[7] = *(undefined4 *)(iVar9 + 0x18);
  puVar8[8] = *(undefined4 *)(iVar9 + 0x1c);
  iVar5 = param_1[1];
  puVar8[0x1a] = iVar4 + -1;
  iVar5 = *(int *)(iVar5 + 0x1c);
  puVar8[0x19] = iVar4 + -1;
  bVar2 = *(byte *)(iVar5 + 0x30);
  uVar6 = *(uint *)(iVar9 + 0x38);
  if ((int)((uint)bVar2 << 0x1f) < 0) {
    puVar8[0x13] = *(int *)(iVar5 + 0x28) + -1;
  }
  if ((int)((uint)bVar2 << 0x1e) < 0) {
    puVar8[0x14] = *(int *)(iVar5 + 0x2c) + -1;
  }
  puVar8[0xe] = 0;
  puVar8[0x22] = 0;
  if (uVar6 == 0) {
    uVar6 = (uint)*(byte *)(iVar9 + 0x20) << 0xd | (uint)*(byte *)(iVar9 + 0x21) << 0x1d;
  }
  puVar8[0x10] = (-(uint)(*(char *)(iVar9 + 0x30) != '\0') & 0xfffb0000) + 0x550000;
  puVar8[0xd] = uVar6;
  puVar8[0xc] = 3;
  puVar8[0xc] = 1;
  puVar8[3] = param_1[3];
  FUN_00004f20((int)param_2[0x12],param_2[0x11],param_1);
  FUN_00004f20((int)*(char *)(iVar9 + 0x24),*(undefined1 *)(iVar9 + 0x22),param_1);
  FUN_00004f20((int)*(char *)(iVar9 + 0x25),*(undefined1 *)(iVar9 + 0x23),param_1);
  *param_1 = 0x475054;
  return 0;
}
```

### `FUN_00038de4` @ `00038de4` score `37`

- reasons: MIDI status-class constant, channel low-nibble test, zero/nonzero tests, byte packet indexing

```c

int * FUN_00038de4(int param_1,int param_2)

{
  int *piVar1;
  int iVar2;
  int iVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  int *piVar6;
  undefined4 local_20;
  undefined1 uStack_1d;
  undefined4 local_1c;
  
  piVar1 = (int *)FUN_00045704(DAT_00038ff4);
  if (piVar1 == (int *)0x0) {
    FUN_000458e8(3,DAT_00039010,0x41,DAT_00039008,DAT_00039014,DAT_00039018,DAT_00039004);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  FUN_0004f350(piVar1,0,0x324);
  piVar1[2] = -1;
  piVar1[3] = -1;
  piVar1[4] = 0;
  piVar1[5] = 0;
  piVar1[6] = 0x82;
  *piVar1 = param_1;
  *(ushort *)((int)piVar1 + 0x3e) = *(ushort *)((int)piVar1 + 0x3e) & 0xfe00 | 3;
  piVar1[1] = param_2;
  *(undefined1 *)(piVar1 + 0x10) = 0x12;
  iVar2 = FUN_0004bea4(0x58);
  piVar1[0xac] = iVar2;
  if (iVar2 == 0) {
    FUN_000458e8(3,DAT_00039010,0x58,DAT_00039008,DAT_00039014,DAT_0003900c,DAT_00039004);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  FUN_0003a2e0();
  if ((code *)piVar1[0xad] != (code *)0x0) {
    (*(code *)piVar1[0xad])(piVar1,piVar1[0xac]);
  }
  iVar2 = piVar1[0xac];
  *(undefined4 *)(iVar2 + 4) = 0;
  *(undefined4 *)(iVar2 + 8) = 0;
  *(int *)(iVar2 + 0x10) = param_2 + -1;
  *(int *)(iVar2 + 0xc) = param_1 + -1;
  *(char *)(iVar2 + 0x14) = (char)piVar1[0x10];
  piVar1[0x9a] = 1;
  iVar2 = FUN_0004afac();
  piVar1[0xc3] = iVar2;
  FUN_000456f4(piVar1 + 0x9b,0x10);
  uVar4 = DAT_00038ffc;
  iVar2 = DAT_00038ff8;
  piVar6 = *(int **)(DAT_00038ff8 + 0x14);
  *(int **)(DAT_00038ff8 + 0x14) = piVar1;
  iVar3 = FUN_000477e8(uVar4,0x21,piVar1);
  piVar1[0xc2] = iVar3;
  if (iVar3 == 0) {
    FUN_000458e8(3,DAT_00039010,0x6d,DAT_00039008,DAT_00039014,DAT_0003901c,DAT_00039004);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar3 = FUN_00051af4();
  if (iVar3 == 0) {
    uVar4 = FUN_00045cdc(5);
    uVar5 = FUN_00045cdc(0);
    local_1c = CONCAT22(CONCAT11(local_1c._3_1_,(char)((uint)uVar5 >> 0x10)),(short)uVar5);
    iVar3 = FUN_000503b8(piVar1,CONCAT22(CONCAT11(uStack_1d,(char)((uint)uVar4 >> 0x10)),
                                         (short)uVar4),local_1c,1,0);
  }
  else {
    iVar3 = FUN_00051ad4();
  }
  piVar1[0xc1] = iVar3;
  iVar3 = FUN_000312b4(0);
  piVar1[0xb3] = iVar3;
  iVar3 = FUN_000312b4(0);
  piVar1[0xb2] = iVar3;
  iVar3 = FUN_000312b4(0);
  piVar1[0xb1] = iVar3;
  iVar3 = FUN_000312b4(0);
  piVar1[0xb0] = iVar3;
  FUN_00036988(piVar1[0xb3]);
  FUN_00036988(piVar1[0xb1]);
  FUN_00036988(piVar1[0xb0]);
  FUN_000313cc(piVar1[0xb1],2);
  FUN_000313cc(piVar1[0xb0],2);
  FUN_000341c0(piVar1[0xb3],0);
  FUN_000341c0(piVar1[0xb1],0);
  FUN_000341c0(piVar1[0xb0],0);
  FUN_00033298(piVar1[0xb2]);
  if (piVar6 == (int *)0x0) {
    piVar6 = piVar1;
  }
  *(int **)(iVar2 + 0x14) = piVar6;
  FUN_000450b8(piVar1 + 0xba,DAT_00039000,0x38,0);
  FUN_0004793c(piVar1[0xc2]);
  return piVar1;
}
```

