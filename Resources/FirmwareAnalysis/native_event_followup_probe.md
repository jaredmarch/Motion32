# Motion 32 Native Event Follow-Up Probe

## Focus Functions

### `00000e5c` `FUN_00000e5c`

References to this address:
- from `00003686` in `FUN_00003684` @ `00003684` type=UNCONDITIONAL_CALL

Instructions near `00000e5c`:

```asm
00000e34: cmp r5,r4
00000e36: bne 0x00000e3a
00000e38: str r6,[sp,#0x4]
00000e3a: ldr r4,[sp,#0x4]
00000e3c: ldr r4,[sp,#0x4]
00000e3e: adds r1,#0x1
00000e40: str r4,[r3,#0x4]
00000e42: cmp r1,r0
00000e44: bne 0x00000e24
00000e46: b 0x00000e14
00000e48: movs r0,r2
00000e4a: b 0x00000e14
00000e4c: movs r0,#0x0
00000e4e: b 0x00000e14
00000e50: movw r3,#0x4291
00000e54: movt r3,#0x2000
00000e58: ldrb r0,[r3,#0x0]
00000e5a: bx lr
00000e5c: push {r4,lr}
00000e5e: sub sp,#0x8
00000e60: mov r3,sp
00000e62: movw r0,#0x5cbc
00000e66: adds r4,r3,#0x7
00000e68: movw r1,#0x204
00000e6c: movs r2,r4
00000e6e: movt r0,#0x2000
00000e72: bl 0x00004df4
00000e76: movw r3,#0x4291
00000e7a: ldrb r2,[r4,#0x0]
00000e7c: movt r3,#0x2000
00000e80: movs r0,#0x9
00000e82: strb r2,[r3,#0x0]
00000e84: bl 0x00002a14
00000e88: bl 0x00002f88
00000e8c: bl 0x00009058
00000e90: movw r1,#0x9818
00000e94: movw r0,#0x5d04
```

```c

void FUN_00000e5c(void)

{
  undefined1 local_9;
  
  FUN_00004df4(0x20005cbc,0x204,&local_9);
  DAT_20004291 = local_9;
  FUN_00002a14(9);
  FUN_00002f88();
  FUN_00009058();
  FUN_00004f2c(0x20005d04,PROBE_00009818);
  FUN_00004f14(0x20005d04);
  FUN_000016f4();
  do {
    FUN_000017d4();
  } while( true );
}
```

### `00002a14` `FUN_00002a14`

References to this address:
- from `00000e84` in `FUN_00000e5c` @ `00000e5c` type=UNCONDITIONAL_CALL

Instructions near `00002a14`:

```asm
000029a4: b 0x0000298c
000029a6: movw r3,#0xffff
000029aa: cmp r4,r3
000029ac: beq 0x000029be
000029ae: movs r3,#0x1
000029b0: rsbs r3,r3
000029b2: strh r3,[r1,#0x0]
000029b4: movw r4,#0xffff
000029b8: movs r1,#0x0
000029ba: movs r3,#0x0
000029bc: b 0x00002966
000029be: movs r1,#0x0
000029c0: movs r3,#0x0
000029c2: b 0x00002966
000029c8: movw r3,#0x5b58
000029cc: movt r3,#0x2000
000029d0: ldr r0,[r3,#0x0]
000029d2: bx lr
00002a14: push {r4,lr}
00002a16: movs r4,r0
00002a18: movw r0,#0x40a0
00002a1c: movt r0,#0x2000
00002a20: bl 0x00000d28
00002a24: movw r3,#0x5b60
00002a28: movs r2,#0x1
00002a2a: movt r3,#0x2000
00002a2e: strb r2,[r3,#0x0]
00002a30: cmp r4,#0x1
00002a32: beq 0x00002a4a
00002a34: movw r1,#0x9874
00002a38: movw r0,#0x5d24
00002a3c: movt r1,#0x0
00002a40: movt r0,#0x2000
00002a44: bl 0x00004854
00002a48: pop {r4,pc}
00002a4a: movw r1,#0x97e4
00002a4e: movw r0,#0x5cd4
```

```c

void FUN_00002a14(int param_1)

{
  FUN_00000d28(0x200040a0);
  DAT_20005b60 = 1;
  if (param_1 == 1) {
    FUN_00004854(0x20005cd4,PROBE_000097e4);
  }
  else {
    FUN_00004854(0x20005d24,PROBE_00009874);
  }
  return;
}
```

### `00002a60` `FUN_00002a60`

References to this address:
- from `0000102a` in `FUN_00000ff4` @ `00000ff4` type=UNCONDITIONAL_CALL

Instructions near `00002a60`:

```asm
00002a24: movw r3,#0x5b60
00002a28: movs r2,#0x1
00002a2a: movt r3,#0x2000
00002a2e: strb r2,[r3,#0x0]
00002a30: cmp r4,#0x1
00002a32: beq 0x00002a4a
00002a34: movw r1,#0x9874
00002a38: movw r0,#0x5d24
00002a3c: movt r1,#0x0
00002a40: movt r0,#0x2000
00002a44: bl 0x00004854
00002a48: pop {r4,pc}
00002a4a: movw r1,#0x97e4
00002a4e: movw r0,#0x5cd4
00002a52: movt r1,#0x0
00002a56: movt r0,#0x2000
00002a5a: bl 0x00004854
00002a5e: b 0x00002a48
00002a60: movw r3,#0x4240
00002a64: push {r4,r5,r6,lr}
00002a66: movw r5,#0x5b60
00002a6a: movt r3,#0xf
00002a6e: movt r5,#0x2000
00002a72: b 0x00002a78
00002a74: subs r3,#0x1
00002a76: cbz r3,0x00002ab0
00002a78: ldrb r4,[r5,#0x0]
00002a7a: cmp r4,#0x0
00002a7c: beq 0x00002a74
00002a7e: movs r3,#0x0
00002a80: strb r3,[r5,#0x0]
00002a82: cmp r2,#0x1
00002a84: beq 0x00002a9e
00002a86: movs r2,r1
00002a88: movs r1,r0
00002a8a: movw r0,#0x5d24
00002a8e: movt r0,#0x2000
```

```c

int FUN_00002a60(undefined4 param_1,undefined4 param_2,int param_3)

{
  int iVar1;
  
  iVar1 = 1000000;
  while (DAT_20005b60 == '\0') {
    iVar1 = iVar1 + -1;
    if (iVar1 == 0) {
      DAT_20005b60 = 1;
      return 0x14;
    }
  }
  DAT_20005b60 = 0;
  if (param_3 == 1) {
    iVar1 = FUN_000047f0(0x20005cd4,param_1,param_2);
  }
  else {
    iVar1 = FUN_000047f0(0x20005d24,param_1,param_2);
  }
  if (iVar1 == 0) {
    return 0;
  }
  DAT_20005b60 = 1;
  return iVar1;
}
```

### `00002ab8` `FUN_00002ab8`

References to this address:
- from `000010aa` in `FUN_000010a4` @ `000010a4` type=UNCONDITIONAL_CALL

Instructions near `00002ab8`:

```asm
00002a88: movs r1,r0
00002a8a: movw r0,#0x5d24
00002a8e: movt r0,#0x2000
00002a92: bl 0x000047f0
00002a96: cbz r0,0x00002a9c
00002a98: movs r3,#0x1
00002a9a: strb r3,[r5,#0x0]
00002a9c: pop {r4,r5,r6,pc}
00002a9e: movs r2,r1
00002aa0: movs r1,r0
00002aa2: movw r0,#0x5cd4
00002aa6: movt r0,#0x2000
00002aaa: bl 0x000047f0
00002aae: b 0x00002a96
00002ab0: adds r3,#0x1
00002ab2: movs r0,#0x14
00002ab4: strb r3,[r5,#0x0]
00002ab6: b 0x00002a9c
00002ab8: movw r0,#0x40a0
00002abc: movt r0,#0x2000
00002ac0: bx lr
00002af0: push {r4,r5,r6,r7,lr}
00002af2: mov lr,r8
00002af4: movs r4,#0x7f
00002af6: push {lr}
00002af8: ldrb r6,[r0,#0x0]
00002afa: ldrb r7,[r0,#0x1]
00002afc: ands r6,r4
00002afe: lsls r7,r7,#0x7
00002b00: orrs r6,r7
00002b02: strb r6,[r1,#0x0]
00002b04: ldrb r6,[r0,#0x2]
00002b06: ldrb r7,[r0,#0x3]
00002b08: ands r6,r4
00002b0a: lsls r7,r7,#0x7
00002b0c: orrs r6,r7
00002b0e: strb r6,[r1,#0x1]
```

```c

undefined4 FUN_00002ab8(void)

{
  return 0x200040a0;
}
```

### `00002ac4` `<none>`

References to this address:
- none

Instructions near `00002ac4`:

```asm
00002a92: bl 0x000047f0
00002a96: cbz r0,0x00002a9c
00002a98: movs r3,#0x1
00002a9a: strb r3,[r5,#0x0]
00002a9c: pop {r4,r5,r6,pc}
00002a9e: movs r2,r1
00002aa0: movs r1,r0
00002aa2: movw r0,#0x5cd4
00002aa6: movt r0,#0x2000
00002aaa: bl 0x000047f0
00002aae: b 0x00002a96
00002ab0: adds r3,#0x1
00002ab2: movs r0,#0x14
00002ab4: strb r3,[r5,#0x0]
00002ab6: b 0x00002a9c
00002ab8: movw r0,#0x40a0
00002abc: movt r0,#0x2000
00002ac0: bx lr
00002af0: push {r4,r5,r6,r7,lr}
00002af2: mov lr,r8
00002af4: movs r4,#0x7f
00002af6: push {lr}
00002af8: ldrb r6,[r0,#0x0]
00002afa: ldrb r7,[r0,#0x1]
00002afc: ands r6,r4
00002afe: lsls r7,r7,#0x7
00002b00: orrs r6,r7
00002b02: strb r6,[r1,#0x0]
00002b04: ldrb r6,[r0,#0x2]
00002b06: ldrb r7,[r0,#0x3]
00002b08: ands r6,r4
00002b0a: lsls r7,r7,#0x7
00002b0c: orrs r6,r7
00002b0e: strb r6,[r1,#0x1]
00002b10: movw r6,#0x3f80
00002b14: ldrb r7,[r0,#0x5]
00002b16: mov r8,r3
```

### `00002af0` `FUN_00002af0`

References to this address:
- from `00002f1a` in `<none>` @ `<none>` type=UNCONDITIONAL_CALL

Instructions near `00002af0`:

```asm
00002a92: bl 0x000047f0
00002a96: cbz r0,0x00002a9c
00002a98: movs r3,#0x1
00002a9a: strb r3,[r5,#0x0]
00002a9c: pop {r4,r5,r6,pc}
00002a9e: movs r2,r1
00002aa0: movs r1,r0
00002aa2: movw r0,#0x5cd4
00002aa6: movt r0,#0x2000
00002aaa: bl 0x000047f0
00002aae: b 0x00002a96
00002ab0: adds r3,#0x1
00002ab2: movs r0,#0x14
00002ab4: strb r3,[r5,#0x0]
00002ab6: b 0x00002a9c
00002ab8: movw r0,#0x40a0
00002abc: movt r0,#0x2000
00002ac0: bx lr
00002af0: push {r4,r5,r6,r7,lr}
00002af2: mov lr,r8
00002af4: movs r4,#0x7f
00002af6: push {lr}
00002af8: ldrb r6,[r0,#0x0]
00002afa: ldrb r7,[r0,#0x1]
00002afc: ands r6,r4
00002afe: lsls r7,r7,#0x7
00002b00: orrs r6,r7
00002b02: strb r6,[r1,#0x0]
00002b04: ldrb r6,[r0,#0x2]
00002b06: ldrb r7,[r0,#0x3]
00002b08: ands r6,r4
00002b0a: lsls r7,r7,#0x7
00002b0c: orrs r6,r7
00002b0e: strb r6,[r1,#0x1]
00002b10: movw r6,#0x3f80
00002b14: ldrb r7,[r0,#0x5]
00002b16: mov r8,r3
```

```c

undefined4 FUN_00002af0(byte *param_1,byte *param_2,ushort *param_3,char *param_4,byte *param_5)

{
  *param_2 = *param_1 & 0x7f | param_1[1] << 7;
  param_2[1] = param_1[2] & 0x7f | param_1[3] << 7;
  *(ushort *)(param_2 + 2) =
       param_1[4] & 0x7f | (param_1[5] & 0x7f) << 7 | (ushort)param_1[6] << 0xe;
  param_2[4] = param_1[7] & 0x7f | param_1[8] << 7;
  *(ushort *)(param_2 + 6) =
       param_1[9] & 0x7f | (param_1[10] & 0x7f) << 7 | (ushort)param_1[0xb] << 0xe;
  *(ushort *)(param_2 + 8) =
       param_1[0xc] & 0x7f | (param_1[0xd] & 0x7f) << 7 | (ushort)param_1[0xe] << 0xe;
  *(ushort *)(param_2 + 10) =
       param_1[0xf] & 0x7f | (param_1[0x10] & 0x7f) << 7 | (ushort)param_1[0x11] << 0xe;
  *(ushort *)(param_2 + 0xc) =
       param_1[0x12] & 0x7f | (param_1[0x13] & 0x7f) << 7 | (ushort)param_1[0x14] << 0xe;
  *param_3 = param_1[0x15] & 0x7f | (param_1[0x16] & 0x7f) << 7 | (ushort)param_1[0x17] << 0xe;
  param_3[1] = param_1[0x18] & 0x7f | (param_1[0x19] & 0x7f) << 7 | (ushort)param_1[0x1a] << 0xe;
  param_3[2] = param_1[0x1b] & 0x7f | (param_1[0x1c] & 0x7f) << 7 | (ushort)param_1[0x1d] << 0xe;
  param_3[3] = param_1[0x1e] & 0x7f | (param_1[0x1f] & 0x7f) << 7 | (ushort)param_1[0x20] << 0xe;
  param_3[4] = param_1[0x21] & 0x7f | (param_1[0x22] & 0x7f) << 7 | (ushort)param_1[0x23] << 0xe;
  param_3[5] = param_1[0x24] & 0x7f | (param_1[0x25] & 0x7f) << 7 | (ushort)param_1[0x26] << 0xe;
  param_3[6] = param_1[0x27] & 0x7f | (param_1[0x28] & 0x7f) << 7 | (ushort)param_1[0x29] << 0xe;
  param_3[7] = param_1[0x2a] & 0x7f | (param_1[0x2b] & 0x7f) << 7 | (ushort)param_1[0x2c] << 0xe;
  param_3[8] = param_1[0x2d] & 0x7f | (param_1[0x2e] & 0x7f) << 7 | (ushort)param_1[0x2f] << 0xe;
  param_3[9] = param_1[0x30] & 0x7f | (param_1[0x31] & 0x7f) << 7 | (ushort)param_1[0x32] << 0xe;
  *param_4 = '\x01' - (param_1[0x33] == 0);
  param_4[1] = param_1[0x34] & 0x7f | param_1[0x35] << 7;
  param_4[2] = '\x01' - (param_1[0x36] == 0);
  *(ushort *)(param_4 + 4) =
       param_1[0x37] & 0x7f | (param_1[0x38] & 0x7f) << 7 | (ushort)param_1[0x39] << 0xe;
  *(ushort *)(param_4 + 6) =
       param_1[0x3a] & 0x7f | (param_1[0x3b] & 0x7f) << 7 | (ushort)param_1[0x3c] << 0xe;
  param_4[8] = '\x01' - (param_1[0x3d] == 0);
  *param_5 = param_1[0x3e] & 0x7f | param_1[0x3f] << 7;
  param_5[1] = param_1[0x40] & 0x7f | param_1[0x41] << 7;
  param_5[2] = param_1[0x42] & 0x7f | param_1[0x43] << 7;
  param_5[3] = param_1[0x44] & 0x7f | param_1[0x45] << 7;
  param_5[4] = param_1[0x46] & 0x7f | param_1[0x47] << 7;
  param_5[5] = param_1[0x48] & 0x7f | param_1[0x49] << 7;
  param_5[6] = param_1[0x4a] & 0x7f | param_1[0x4b] << 7;
  param_5[7] = param_1[0x4c] & 0x7f | param_1[0x4d] << 7;
  param_5[8] = param_1[0x4e] & 0x7f | param_1[0x4f] << 7;
  param_5[9] = param_1[0x50] & 0x7f | param_1[0x51] << 7;
  param_5[10] = param_1[0x52] & 0x7f | param_1[0x53] << 7;
  param_5[0xb] = 1 - (param_1[0x54] == 0);
  param_5[0xc] = param_1[0x55] & 0x7f | param_1[0x56] << 7;
  param_5[0xd] = param_1[0x57] & 0x7f | param_1[0x58] << 7;
  param_5[0xe] = param_1[0x59] & 0x7f | param_1[0x5a] << 7;
  param_5[0xf] = param_1[0x5b] & 0x7f | param_1[0x5c] << 7;
  param_5[0x10] = param_1[0x5d] & 0x7f | param_1[0x5e] << 7;
  param_5[0x11] = param_1[0x5f] & 0x7f | param_1[0x60] << 7;
  param_5[0x12] = param_1[0x61] & 0x7f | param_1[0x62] << 7;
  param_5[0x13] = param_1[99] & 0x7f | param_1[100] << 7;
  param_5[0x14] = param_1[0x65] & 0x7f | param_1[0x66] << 7;
  param_5[0x15] = param_1[0x67] & 0x7f | param_1[0x68] << 7;
  param_5[0x16] = param_1[0x69] & 0x7f | param_1[0x6a] << 7;
  param_5[0x17] = 1 - (param_1[0x6b] == 0);
  return 0;
}
```

### `00000d28` `FUN_00000d28`

References to this address:
- from `00002a20` in `FUN_00002a14` @ `00002a14` type=UNCONDITIONAL_CALL

Instructions near `00000d28`:

```asm
00000cf8: movs r0,#0x21
00000cfa: b 0x00000cd2
00000cfc: movw r3,#0x4290
00000d00: movt r3,#0x2000
00000d04: ldrb r3,[r3,#0x0]
00000d06: push {r4,lr}
00000d08: cbz r3,0x00000d22
00000d0a: cbz r0,0x00000d1e
00000d0c: movw r1,#0x400
00000d10: movs r2,#0x8
00000d12: movt r1,#0x4010
00000d16: bl 0x00009578
00000d1a: movs r0,#0x0
00000d1c: pop {r4,pc}
00000d1e: movs r0,#0x1
00000d20: b 0x00000d1c
00000d22: movs r0,#0x21
00000d24: b 0x00000d1c
00000d28: ldr r3,[r0,#0x10]
00000d2a: push {r4,lr}
00000d2c: movs r4,r0
00000d2e: cbz r3,0x00000d32
00000d30: blx r3
00000d32: ldr r2,[r4,#0x8]
00000d34: subs r3,r2,#0x1
00000d36: cbz r2,0x00000d42
00000d38: movs r1,#0x0
00000d3a: ldr r2,[r4,#0x14]
00000d3c: strb r1,[r2,r3]
00000d3e: subs r3,#0x1
00000d40: bcs 0x00000d3a
00000d42: movs r3,#0x1
00000d44: str r3,[r4,#0x0]
00000d46: movs r3,#0x0
00000d48: str r3,[r4,#0x4]
00000d4a: ldr r3,[r4,#0xc]
00000d4c: cbz r3,0x00000d50
```

```c

void FUN_00000d28(undefined4 *param_1)

{
  int iVar1;
  
  if ((code *)param_1[4] != (code *)0x0) {
    (*(code *)param_1[4])();
  }
  iVar1 = param_1[2];
  while (iVar1 != 0) {
    iVar1 = iVar1 + -1;
    *(undefined1 *)(param_1[5] + iVar1) = 0;
  }
  *param_1 = 1;
  param_1[1] = 0;
  if ((code *)param_1[3] != (code *)0x0) {
    (*(code *)param_1[3])();
  }
  return;
}
```

### `00000d54` `FUN_00000d54`

References to this address:
- from `000010ca` in `FUN_000010a4` @ `000010a4` type=UNCONDITIONAL_CALL
- from `0000112a` in `FUN_000010a4` @ `000010a4` type=UNCONDITIONAL_CALL
- from `00000ffe` in `FUN_00000ff4` @ `00000ff4` type=UNCONDITIONAL_CALL

Instructions near `00000d54`:

```asm
00000d2e: cbz r3,0x00000d32
00000d30: blx r3
00000d32: ldr r2,[r4,#0x8]
00000d34: subs r3,r2,#0x1
00000d36: cbz r2,0x00000d42
00000d38: movs r1,#0x0
00000d3a: ldr r2,[r4,#0x14]
00000d3c: strb r1,[r2,r3]
00000d3e: subs r3,#0x1
00000d40: bcs 0x00000d3a
00000d42: movs r3,#0x1
00000d44: str r3,[r4,#0x0]
00000d46: movs r3,#0x0
00000d48: str r3,[r4,#0x4]
00000d4a: ldr r3,[r4,#0xc]
00000d4c: cbz r3,0x00000d50
00000d4e: blx r3
00000d50: pop {r4,pc}
00000d54: ldr r1,[r0,#0x0]
00000d56: ldr r3,[r0,#0x4]
00000d58: ldr r2,[r0,#0x8]
00000d5a: subs r0,r3,r1
00000d5c: cmp r1,r3
00000d5e: bls 0x00000d66
00000d60: adds r3,r2,r3
00000d62: adds r3,#0x1
00000d64: subs r0,r3,r1
00000d66: subs r0,r2,r0
00000d68: bx lr
00000d6c: ldr r3,[r0,#0x0]
00000d6e: sub sp,#0x8
00000d70: str r3,[sp,#0x4]
00000d72: ldr r3,[r0,#0x8]
00000d74: ldr r2,[sp,#0x4]
00000d76: adds r3,#0x1
00000d78: cmp r3,r2
00000d7a: bne 0x00000d80
```

```c

int FUN_00000d54(uint *param_1)

{
  int iVar1;
  uint uVar2;
  uint uVar3;
  
  uVar2 = *param_1;
  uVar3 = param_1[1];
  iVar1 = uVar3 - uVar2;
  if (uVar3 < uVar2) {
    iVar1 = (param_1[2] + uVar3 + 1) - uVar2;
  }
  return param_1[2] - iVar1;
}
```

### `00000d6c` `FUN_00000d6c`

References to this address:
- from `00000f16` in `FUN_00000eec` @ `00000eec` type=UNCONDITIONAL_CALL
- from `00000f24` in `FUN_00000eec` @ `00000eec` type=UNCONDITIONAL_CALL
- from `00000f32` in `FUN_00000eec` @ `00000eec` type=UNCONDITIONAL_CALL
- from `00000f4a` in `FUN_00000eec` @ `00000eec` type=UNCONDITIONAL_CALL
- from `00000f58` in `FUN_00000eec` @ `00000eec` type=UNCONDITIONAL_CALL
- from `00000f66` in `FUN_00000eec` @ `00000eec` type=UNCONDITIONAL_CALL
- from `00001052` in `FUN_00001030` @ `00001030` type=UNCONDITIONAL_CALL
- from `00001070` in `FUN_00001030` @ `00001030` type=UNCONDITIONAL_CALL
- from `00001088` in `FUN_00001030` @ `00001030` type=UNCONDITIONAL_CALL
- from `00000f8c` in `FUN_00000f6c` @ `00000f6c` type=UNCONDITIONAL_CALL
- from `00000f9a` in `FUN_00000f6c` @ `00000f6c` type=UNCONDITIONAL_CALL
- from `00000fa8` in `FUN_00000f6c` @ `00000f6c` type=UNCONDITIONAL_CALL
- from `00000fd2` in `FUN_00000fb0` @ `00000fb0` type=UNCONDITIONAL_CALL
- from `00000fe0` in `FUN_00000fb0` @ `00000fb0` type=UNCONDITIONAL_CALL
- from `00000fee` in `FUN_00000fb0` @ `00000fb0` type=UNCONDITIONAL_CALL

Instructions near `00000d6c`:

```asm
00000d44: str r3,[r4,#0x0]
00000d46: movs r3,#0x0
00000d48: str r3,[r4,#0x4]
00000d4a: ldr r3,[r4,#0xc]
00000d4c: cbz r3,0x00000d50
00000d4e: blx r3
00000d50: pop {r4,pc}
00000d54: ldr r1,[r0,#0x0]
00000d56: ldr r3,[r0,#0x4]
00000d58: ldr r2,[r0,#0x8]
00000d5a: subs r0,r3,r1
00000d5c: cmp r1,r3
00000d5e: bls 0x00000d66
00000d60: adds r3,r2,r3
00000d62: adds r3,#0x1
00000d64: subs r0,r3,r1
00000d66: subs r0,r2,r0
00000d68: bx lr
00000d6c: ldr r3,[r0,#0x0]
00000d6e: sub sp,#0x8
00000d70: str r3,[sp,#0x4]
00000d72: ldr r3,[r0,#0x8]
00000d74: ldr r2,[sp,#0x4]
00000d76: adds r3,#0x1
00000d78: cmp r3,r2
00000d7a: bne 0x00000d80
00000d7c: movs r3,#0x0
00000d7e: str r3,[sp,#0x4]
00000d80: ldr r3,[sp,#0x4]
00000d82: ldr r2,[r0,#0x14]
00000d84: strb r1,[r2,r3]
00000d86: ldr r3,[sp,#0x4]
00000d88: adds r3,#0x1
00000d8a: str r3,[sp,#0x4]
00000d8c: ldr r3,[sp,#0x4]
00000d8e: str r3,[r0,#0x0]
00000d90: add sp,#0x8
```

```c

void FUN_00000d6c(int *param_1,undefined1 param_2)

{
  int local_4;
  
  local_4 = *param_1;
  if (param_1[2] + 1 == local_4) {
    local_4 = 0;
  }
  *(undefined1 *)(param_1[5] + local_4) = param_2;
  *param_1 = local_4 + 1;
  return;
}
```

### `00000dc0` `FUN_00000dc0`

References to this address:
- from `0000101a` in `FUN_00000ff4` @ `00000ff4` type=UNCONDITIONAL_CALL

Instructions near `00000dc0`:

```asm
00000d9a: ldr r2,[sp,#0x4]
00000d9c: movs r3,r0
00000d9e: adds r2,#0x1
00000da0: str r2,[sp,#0x4]
00000da2: ldr r2,[r0,#0x8]
00000da4: ldr r1,[sp,#0x4]
00000da6: adds r2,#0x1
00000da8: cmp r2,r1
00000daa: bne 0x00000db0
00000dac: movs r2,#0x0
00000dae: str r2,[sp,#0x4]
00000db0: ldr r2,[sp,#0x4]
00000db2: ldr r1,[r3,#0x14]
00000db4: ldrb r0,[r1,r2]
00000db6: ldr r2,[sp,#0x4]
00000db8: str r2,[r3,#0x4]
00000dba: add sp,#0x8
00000dbc: bx lr
00000dc0: push {r4,r5,r6,r7,lr}
00000dc2: ldr r6,[r0,#0x0]
00000dc4: ldr r4,[r0,#0x4]
00000dc6: movs r3,r0
00000dc8: ldr r5,[r0,#0x8]
00000dca: sub sp,#0xc
00000dcc: subs r0,r4,r6
00000dce: cmp r6,r4
00000dd0: bls 0x00000dd8
00000dd2: adds r4,r5,r4
00000dd4: adds r4,#0x1
00000dd6: subs r0,r4,r6
00000dd8: subs r0,r5,r0
00000dda: cbz r1,0x00000e18
00000ddc: cbz r0,0x00000e14
00000dde: cmp r2,#0x0
00000de0: beq 0x00000e4c
00000de2: movs r4,#0x0
00000de4: movs r7,#0x0
```

```c

int FUN_00000dc0(uint *param_1,int param_2,int param_3)

{
  undefined1 uVar1;
  int iVar2;
  uint uVar3;
  int iVar4;
  uint uVar5;
  uint uVar6;
  uint local_20;
  uint local_1c;
  
  uVar6 = *param_1;
  uVar3 = param_1[1];
  uVar5 = param_1[2];
  iVar2 = uVar3 - uVar6;
  if (uVar3 < uVar6) {
    iVar2 = (uVar5 + uVar3 + 1) - uVar6;
  }
  iVar2 = uVar5 - iVar2;
  if (param_2 == 0) {
    if (iVar2 == 0) {
      return 0;
    }
    iVar4 = 0;
    if (param_3 != 0) {
      while( true ) {
        local_1c = param_1[1] + 1;
        if (uVar5 + 1 == local_1c) {
          local_1c = 0;
        }
        iVar4 = iVar4 + 1;
        param_1[1] = local_1c;
        if (iVar4 == iVar2) break;
        if (param_3 == iVar4) {
          return param_3;
        }
      }
      return iVar2;
    }
  }
  else {
    if (iVar2 == 0) {
      return 0;
    }
    if (param_3 != 0) {
      iVar4 = 0;
      while( true ) {
        local_20 = param_1[1] + 1;
        if (uVar5 + 1 == local_20) {
          local_20 = 0;
        }
        uVar1 = *(undefined1 *)(param_1[5] + local_20);
        param_1[1] = local_20;
        *(undefined1 *)(param_2 + iVar4) = uVar1;
        iVar4 = iVar4 + 1;
        if (iVar4 == iVar2) break;
        if (param_3 == iVar4) {
          return param_3;
        }
        uVar5 = param_1[2];
      }
      return iVar2;
    }
  }
  return 0;
}
```

### `00000eec` `FUN_00000eec`

References to this address:
- from `0000131e` in `FUN_00001288` @ `00001288` type=UNCONDITIONAL_CALL
- from `0000133c` in `FUN_00001288` @ `00001288` type=UNCONDITIONAL_CALL

Instructions near `00000eec`:

```asm
00000eb4: bl 0x000017d4
00000eb8: b 0x00000eb4
00000ebc: push {r4,lr}
00000ebe: cbnz r0,0x00000ed0
00000ec0: movw r3,#0xc000
00000ec4: movs r2,#0x90
00000ec6: movs r1,#0x1
00000ec8: movt r3,#0x407e
00000ecc: strb r1,[r3,r2]
00000ece: pop {r4,pc}
00000ed0: cmp r0,#0x2
00000ed2: bne 0x00000ece
00000ed4: movw r1,#0x98e0
00000ed8: movw r0,#0x5cbc
00000edc: movt r1,#0x0
00000ee0: movt r0,#0x2000
00000ee4: bl 0x00004ef0
00000ee8: b 0x00000ece
00000eec: push {r3,r4,r5,r6,r7,lr}
00000eee: movw r5,#0x4081
00000ef2: movs r7,#0x7f
00000ef4: movt r5,#0x2000
00000ef8: ldrb r3,[r5,#0x0]
00000efa: asrs r6,r1,#0x7
00000efc: ands r6,r7
00000efe: movs r4,r0
00000f00: ands r7,r1
00000f02: cmp r3,r0
00000f04: beq 0x00000f1a
00000f06: movs r1,r0
00000f08: strb r0,[r5,#0x0]
00000f0a: movw r0,#0x4084
00000f0e: subs r1,#0x50
00000f10: uxtb r1,r1
00000f12: movt r0,#0x2000
00000f16: bl 0x00000d6c
00000f1a: movw r0,#0x4084
```

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

### `00000f6c` `FUN_00000f6c`

References to this address:
- from `000013ca` in `FUN_0000134c` @ `0000134c` type=UNCONDITIONAL_CALL
- from `000013f6` in `FUN_0000134c` @ `0000134c` type=UNCONDITIONAL_CALL

Instructions near `00000f6c`:

```asm
00000f36: ldrb r3,[r5,#0x0]
00000f38: cmp r3,r4
00000f3a: beq 0x00000f4e
00000f3c: movw r0,#0x4084
00000f40: strb r4,[r5,#0x0]
00000f42: subs r4,#0x50
00000f44: uxtb r1,r4
00000f46: movt r0,#0x2000
00000f4a: bl 0x00000d6c
00000f4e: movw r0,#0x4084
00000f52: movs r1,#0x36
00000f54: movt r0,#0x2000
00000f58: bl 0x00000d6c
00000f5c: movw r0,#0x4084
00000f60: movs r1,r7
00000f62: movt r0,#0x2000
00000f66: bl 0x00000d6c
00000f6a: pop {r3,r4,r5,r6,r7,pc}
00000f6c: movw r3,#0x4081
00000f70: push {r4,lr}
00000f72: movt r3,#0x2000
00000f76: ldrb r2,[r3,#0x0]
00000f78: movs r4,r1
00000f7a: cmp r2,r0
00000f7c: beq 0x00000f90
00000f7e: strb r0,[r3,#0x0]
00000f80: subs r0,#0x50
00000f82: uxtb r1,r0
00000f84: movw r0,#0x4084
00000f88: movt r0,#0x2000
00000f8c: bl 0x00000d6c
00000f90: movw r0,#0x4084
00000f94: movs r1,#0x14
00000f96: movt r0,#0x2000
00000f9a: bl 0x00000d6c
00000f9e: movw r0,#0x4084
00000fa2: movs r1,r4
```

```c

void FUN_00000f6c(uint param_1,undefined4 param_2)

{
  if (DAT_20004081 != param_1) {
    DAT_20004081 = (byte)param_1;
    FUN_00000d6c(0x20004084,param_1 - 0x50 & 0xff);
  }
  FUN_00000d6c(0x20004084,0x14);
  FUN_00000d6c(0x20004084,param_2);
  return;
}
```

### `00000fb0` `FUN_00000fb0`

References to this address:
- from `0000150c` in `FUN_0000140c` @ `0000140c` type=UNCONDITIONAL_CALL
- from `0000152c` in `FUN_0000140c` @ `0000140c` type=UNCONDITIONAL_CALL
- from `0000154c` in `FUN_0000140c` @ `0000140c` type=UNCONDITIONAL_CALL
- from `0000156c` in `FUN_0000140c` @ `0000140c` type=UNCONDITIONAL_CALL
- from `0000158c` in `FUN_0000140c` @ `0000140c` type=UNCONDITIONAL_CALL
- from `000015b2` in `FUN_0000140c` @ `0000140c` type=UNCONDITIONAL_CALL
- from `000015d2` in `FUN_0000140c` @ `0000140c` type=UNCONDITIONAL_CALL
- from `000015f2` in `FUN_0000140c` @ `0000140c` type=UNCONDITIONAL_CALL
- from `00001610` in `FUN_0000140c` @ `0000140c` type=UNCONDITIONAL_CALL

Instructions near `00000fb0`:

```asm
00000f78: movs r4,r1
00000f7a: cmp r2,r0
00000f7c: beq 0x00000f90
00000f7e: strb r0,[r3,#0x0]
00000f80: subs r0,#0x50
00000f82: uxtb r1,r0
00000f84: movw r0,#0x4084
00000f88: movt r0,#0x2000
00000f8c: bl 0x00000d6c
00000f90: movw r0,#0x4084
00000f94: movs r1,#0x14
00000f96: movt r0,#0x2000
00000f9a: bl 0x00000d6c
00000f9e: movw r0,#0x4084
00000fa2: movs r1,r4
00000fa4: movt r0,#0x2000
00000fa8: bl 0x00000d6c
00000fac: pop {r4,pc}
00000fb0: movw r3,#0x4081
00000fb4: push {r4,lr}
00000fb6: movt r3,#0x2000
00000fba: ldrb r2,[r3,#0x0]
00000fbc: adds r1,#0x40
00000fbe: uxtb r4,r1
00000fc0: cmp r2,r0
00000fc2: beq 0x00000fd6
00000fc4: strb r0,[r3,#0x0]
00000fc6: subs r0,#0x50
00000fc8: uxtb r1,r0
00000fca: movw r0,#0x4084
00000fce: movt r0,#0x2000
00000fd2: bl 0x00000d6c
00000fd6: movw r0,#0x4084
00000fda: movs r1,#0x15
00000fdc: movt r0,#0x2000
00000fe0: bl 0x00000d6c
00000fe4: movw r0,#0x4084
```

```c

void FUN_00000fb0(uint param_1,char param_2)

{
  if (DAT_20004081 != param_1) {
    DAT_20004081 = (byte)param_1;
    FUN_00000d6c(0x20004084,param_1 - 0x50 & 0xff);
  }
  FUN_00000d6c(0x20004084,0x15);
  FUN_00000d6c(0x20004084,param_2 + '@');
  return;
}
```

### `00000ff4` `FUN_00000ff4`

References to this address:
- from `000011f6` in `<none>` @ `<none>` type=UNCONDITIONAL_CALL

Instructions near `00000ff4`:

```asm
00000fbe: uxtb r4,r1
00000fc0: cmp r2,r0
00000fc2: beq 0x00000fd6
00000fc4: strb r0,[r3,#0x0]
00000fc6: subs r0,#0x50
00000fc8: uxtb r1,r0
00000fca: movw r0,#0x4084
00000fce: movt r0,#0x2000
00000fd2: bl 0x00000d6c
00000fd6: movw r0,#0x4084
00000fda: movs r1,#0x15
00000fdc: movt r0,#0x2000
00000fe0: bl 0x00000d6c
00000fe4: movw r0,#0x4084
00000fe8: movs r1,r4
00000fea: movt r0,#0x2000
00000fee: bl 0x00000d6c
00000ff2: pop {r4,pc}
00000ff4: movw r0,#0x4084
00000ff8: push {r4,lr}
00000ffa: movt r0,#0x2000
00000ffe: bl 0x00000d54
00001002: movs r4,r0
00001004: cbnz r0,0x00001008
00001006: pop {r4,pc}
00001008: movs r2,r0
0000100a: movw r1,#0x4324
0000100e: movw r0,#0x4084
00001012: movt r1,#0x2000
00001016: movt r0,#0x2000
0000101a: bl 0x00000dc0
0000101e: movw r0,#0x4324
00001022: movs r2,#0x9
00001024: movs r1,r4
00001026: movt r0,#0x2000
0000102a: bl 0x00002a60
0000102e: b 0x00001006
```

```c

void FUN_00000ff4(void)

{
  int iVar1;
  
  iVar1 = FUN_00000d54(0x20004084);
  if (iVar1 != 0) {
    FUN_00000dc0(0x20004084,0x20004324,iVar1);
    FUN_00002a60(0x20004324,iVar1,9);
  }
  return;
}
```

### `00001030` `FUN_00001030`

References to this address:
- from `00008b6a` in `FUN_00008944` @ `00008944` type=UNCONDITIONAL_CALL
- from `00008c18` in `FUN_00008944` @ `00008944` type=UNCONDITIONAL_CALL
- from `00008d16` in `FUN_00008944` @ `00008944` type=UNCONDITIONAL_CALL
- from `00008dee` in `FUN_00008944` @ `00008944` type=UNCONDITIONAL_CALL
- from `00008ee8` in `FUN_00008e1c` @ `00008e1c` type=UNCONDITIONAL_CALL

Instructions near `00001030`:

```asm
00000ff8: push {r4,lr}
00000ffa: movt r0,#0x2000
00000ffe: bl 0x00000d54
00001002: movs r4,r0
00001004: cbnz r0,0x00001008
00001006: pop {r4,pc}
00001008: movs r2,r0
0000100a: movw r1,#0x4324
0000100e: movw r0,#0x4084
00001012: movt r1,#0x2000
00001016: movt r0,#0x2000
0000101a: bl 0x00000dc0
0000101e: movw r0,#0x4324
00001022: movs r2,#0x9
00001024: movs r1,r4
00001026: movt r0,#0x2000
0000102a: bl 0x00002a60
0000102e: b 0x00001006
00001030: push {r3,r4,r5,r6,r7,lr}
00001032: movs r5,r0
00001034: movs r6,r1
00001036: bl 0x00000e50
0000103a: cbnz r0,0x0000108e
0000103c: movw r4,#0x95f4
00001040: movt r4,#0x0
00001044: adds r7,r4,#0x4
00001046: movw r0,#0x4084
0000104a: ldrb r1,[r4,#0x0]
0000104c: movt r0,#0x2000
00001050: adds r4,#0x1
00001052: bl 0x00000d6c
00001056: cmp r4,r7
00001058: bne 0x00001046
0000105a: cbz r6,0x0000107e
0000105c: movs r4,#0x0
0000105e: movs r3,#0x0
00001060: ldrsb r3,[r5,r3]
```

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

### `00001288` `FUN_00001288`

References to this address:
- from `00008aba` in `FUN_00008944` @ `00008944` type=UNCONDITIONAL_CALL
- from `00008f6e` in `FUN_00008e1c` @ `00008e1c` type=UNCONDITIONAL_CALL

Instructions near `00001288`:

```asm
00001262: rsbs r1,r3
00001264: adcs r3,r1
00001266: strh r3,[r4,#0xa]
00001268: ldr r3,[r4,#0x0]
0000126a: cmp r2,#0x1
0000126c: bne 0x00001222
0000126e: ldrb r2,[r4,#0x9]
00001270: cmp r2,#0x0
00001272: bne 0x00001226
00001274: adds r3,#0x1
00001276: str r3,[r4,#0x0]
00001278: ldrb r3,[r7,#0x0]
0000127a: adds r6,#0x1
0000127c: adds r5,#0x4
0000127e: adds r4,#0x10
00001280: cmp r3,r6
00001282: bgt 0x00001236
00001284: pop {r3,r4,r5,r6,r7,pc}
00001288: push {r4,r5,r6,r7,lr}
0000128a: mov r5,r8
0000128c: movw r8,#0x45ca
00001290: mov lr,r11
00001292: mov r7,r10
00001294: mov r6,r9
00001296: movt r8,#0x2000
0000129a: mov r3,r8
0000129c: push {r5,r6,r7,lr}
0000129e: ldrb r1,[r3,#0x0]
000012a0: sub sp,#0xc
000012a2: cmp r1,#0x0
000012a4: beq 0x00001328
000012a6: movw r3,#0x45c8
000012aa: movw r6,#0x4534
000012ae: movt r3,#0x2000
000012b2: movs r4,r0
000012b4: movs r5,#0x0
000012b6: movw r9,#0xc
```

```c

void FUN_00001288(short *param_1)

{
  byte bVar1;
  byte bVar2;
  short *psVar3;
  int iVar4;
  char *local_2c;
  
  if (DAT_200045ca != 0) {
    bVar2 = 0;
    iVar4 = 0xc;
    psVar3 = (short *)&DAT_20004534;
    local_2c = &DAT_200045c8;
    bVar1 = DAT_200045ca;
    do {
      if ((*param_1 < 0xc) || (0x3f4 < *param_1)) {
        iVar4 = 2;
      }
      if ((*psVar3 + iVar4 < (int)*param_1) || ((int)*param_1 < *psVar3 - iVar4)) {
        *psVar3 = *param_1;
        FUN_00000eec(bVar2,(int)*param_1);
        bVar1 = DAT_200045ca;
      }
      else if (*local_2c != '\0') {
        FUN_00000eec(bVar2,(int)*param_1);
        *local_2c = '\0';
        bVar1 = DAT_200045ca;
      }
      bVar2 = bVar2 + 1;
      local_2c = local_2c + 1;
      param_1 = param_1 + 1;
      psVar3 = psVar3 + 1;
    } while (bVar2 < bVar1);
  }
  return;
}
```

### `0000140c` `FUN_0000140c`

References to this address:
- from `00008aa2` in `FUN_00008944` @ `00008944` type=UNCONDITIONAL_CALL
- from `00008f56` in `FUN_00008e1c` @ `00008e1c` type=UNCONDITIONAL_CALL

Instructions near `0000140c`:

```asm
000013e0: strb r2,[r3,#0x1]
000013e2: b 0x0000137c
000013e4: strh r6,[r7,#0x0]
000013e6: pop {r6,r7}
000013e8: mov r9,r7
000013ea: mov r8,r6
000013ec: pop {r3,r4,r5,r6,r7,pc}
000013ee: tst r2,r3
000013f0: beq 0x0000137c
000013f2: movs r1,#0x0
000013f4: mov r0,r9
000013f6: bl 0x00000f6c
000013fa: b 0x0000137c
000013fc: movw r3,#0x45c8
00001400: movs r2,#0x1
00001402: movt r3,#0x2000
00001406: strb r2,[r3,#0x0]
00001408: b 0x0000137c
0000140c: push {r4,r5,r6,lr}
0000140e: movw r5,#0x45cc
00001412: movt r5,#0x2000
00001416: ldrb r3,[r5,#0x0]
00001418: cmp r3,#0x0
0000141a: beq 0x000014f6
0000141c: movw r4,#0x4538
00001420: movt r4,#0x2000
00001424: ldr r1,[r4,#0x0]
00001426: ldr r2,[r4,#0x4]
00001428: cmp r1,r2
0000142a: beq 0x00001436
0000142c: subs r2,r1,r2
0000142e: sxtb r6,r2
00001430: str r1,[r4,#0x4]
00001432: cmp r6,#0x0
00001434: bne 0x000014f8
00001436: cmp r3,#0x1
00001438: bls 0x000014f6
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0000140c(void)

{
  int iVar1;
  int iVar2;
  
  if (DAT_200045cc != 0) {
    if (_DAT_20004538 != _DAT_2000453c) {
      iVar2 = (int)(char)((char)_DAT_20004538 - (char)_DAT_2000453c);
      _DAT_2000453c = _DAT_20004538;
      if (iVar2 != 0) {
        iVar1 = FUN_00000e50();
        FUN_00000fb0((&DAT_00009664)[iVar1 * 9],iVar2);
      }
    }
    if (1 < DAT_200045cc) {
      if (_DAT_20004548 != _DAT_2000454c) {
        iVar2 = (int)(char)((char)_DAT_20004548 - (char)_DAT_2000454c);
        _DAT_2000454c = _DAT_20004548;
        if (iVar2 != 0) {
          iVar1 = FUN_00000e50();
          FUN_00000fb0((&DAT_00009665)[iVar1 * 9],iVar2);
        }
      }
      if (2 < DAT_200045cc) {
        if (_DAT_20004558 != _DAT_2000455c) {
          iVar2 = (int)(char)((char)_DAT_20004558 - (char)_DAT_2000455c);
          _DAT_2000455c = _DAT_20004558;
          if (iVar2 != 0) {
            iVar1 = FUN_00000e50();
            FUN_00000fb0((&DAT_00009666)[iVar1 * 9],iVar2);
          }
        }
        if (3 < DAT_200045cc) {
          if (_DAT_20004568 != _DAT_2000456c) {
            iVar2 = (int)(char)((char)_DAT_20004568 - (char)_DAT_2000456c);
            _DAT_2000456c = _DAT_20004568;
            if (iVar2 != 0) {
              iVar1 = FUN_00000e50();
              FUN_00000fb0((&DAT_00009667)[iVar1 * 9],iVar2);
            }
          }
          if (4 < DAT_200045cc) {
            if (_DAT_20004578 != _DAT_2000457c) {
              iVar2 = (int)(char)((char)_DAT_20004578 - (char)_DAT_2000457c);
              _DAT_2000457c = _DAT_20004578;
              if (iVar2 != 0) {
                iVar1 = FUN_00000e50();
                FUN_00000fb0((&DAT_00009668)[iVar1 * 9],iVar2);
              }
            }
            if (5 < DAT_200045cc) {
              if ((_DAT_20004588 != _DAT_2000458c) &&
                 (iVar2 = (int)(char)((char)_DAT_20004588 - (char)_DAT_2000458c),
                 _DAT_2000458c = _DAT_20004588, iVar2 != 0)) {
                iVar1 = FUN_00000e50();
                FUN_00000fb0((&DAT_00009669)[iVar1 * 9],iVar2);
              }
              if (6 < DAT_200045cc) {
                if (_DAT_20004598 != _DAT_2000459c) {
                  iVar2 = (int)(char)((char)_DAT_20004598 - (char)_DAT_2000459c);
                  _DAT_2000459c = _DAT_20004598;
                  if (iVar2 != 0) {
                    iVar1 = FUN_00000e50();
                    FUN_00000fb0((&DAT_0000966a)[iVar1 * 9],iVar2);
                  }
                }
                if (7 < DAT_200045cc) {
                  if (_DAT_200045a8 != _DAT_200045ac) {
                    iVar2 = (int)(char)((char)_DAT_200045a8 - (char)_DAT_200045ac);
                    _DAT_200045ac = _DAT_200045a8;
                    if (iVar2 != 0) {
                      iVar1 = FUN_00000e50();
                      FUN_00000fb0((&DAT_0000966b)[iVar1 * 9],iVar2);
                    }
                  }
                  if ((8 < DAT_200045cc) && (_DAT_200045b8 != _DAT_200045bc)) {
                    iVar2 = (int)(char)((char)_DAT_200045b8 - (char)_DAT_200045bc);
                    _DAT_200045bc = _DAT_200045b8;
                    if (iVar2 != 0) {
                      iVar1 = FUN_00000e50();
                      FUN_00000fb0((&DAT_0000966c)[iVar1 * 9],iVar2);
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  return;
}
```

### `000016f4` `FUN_000016f4`

References to this address:
- from `00000eb0` in `FUN_00000e5c` @ `00000e5c` type=UNCONDITIONAL_CALL

Instructions near `000016f4`:

```asm
000016ce: ldrh r3,[r0,#0x2]
000016d0: adds r1,#0xb4
000016d2: sxth r3,r3
000016d4: cmp r3,r1
000016d6: bgt 0x00001666
000016d8: movs r1,#0x2
000016da: ldrsh r3,[r4,r1]
000016dc: movs r1,#0x72
000016de: muls r1,r3
000016e0: movs r3,#0x8e
000016e2: ldrh r5,[r0,#0x2]
000016e4: sxth r5,r5
000016e6: muls r3,r5
000016e8: adds r1,r1,r3
000016ea: asrs r1,r1,#0x8
000016ec: sxth r1,r1
000016ee: strh r1,[r4,#0x2]
000016f0: b 0x0000169a
000016f4: push {r3,r4,r5,r6,r7,lr}
000016f6: bl 0x00000e50
000016fa: cmp r0,#0x0
000016fc: bne 0x00001796
000016fe: movs r3,#0x8
00001700: movs r2,#0x2
00001702: movw r7,#0x45cc
00001706: movt r7,#0x2000
0000170a: strb r3,[r7,#0x0]
0000170c: movw r3,#0x45cb
00001710: movs r1,#0xb
00001712: movt r3,#0x2000
00001716: strb r1,[r3,#0x0]
00001718: movw r3,#0x45ca
0000171c: movw r5,#0x95fc
00001720: movs r6,#0x0
00001722: movt r3,#0x2000
00001726: ldr r4,[0x0000179c]
00001728: strb r2,[r3,#0x0]
```

```c

void FUN_000016f4(void)

{
  int iVar1;
  undefined4 in_r3;
  undefined1 *puVar2;
  byte *pbVar3;
  undefined2 *puVar4;
  
  iVar1 = FUN_00000e50();
  if (iVar1 == 0) {
    DAT_200045cc = 8;
    DAT_200045ca = 2;
  }
  else {
    DAT_200045cc = 9;
    DAT_200045ca = 1;
  }
  DAT_200045cb = 0xb;
  iVar1 = 0;
  puVar2 = &DAT_200045ca;
  puVar4 = &DAT_000095fc;
  pbVar3 = DAT_0000179c;
  do {
    FUN_00004df4(0x20005cbc,*puVar4,pbVar3,puVar2,in_r3);
    iVar1 = iVar1 + 1;
    *(ushort *)(pbVar3 + 2) = (ushort)*pbVar3;
    puVar2 = (undefined1 *)(uint)DAT_200045cc;
    puVar4 = puVar4 + 2;
    pbVar3 = pbVar3 + 0x10;
  } while (iVar1 < (int)puVar2);
  FUN_000017a0(0x200045e0,&LAB_00001200_1);
  FUN_00001834(500,0,0x200045e0);
  FUN_000017a0(0x200045d0,&LAB_000011f4_1);
  FUN_000017ac(0x200045d0);
  return;
}
```

### `000017d4` `FUN_000017d4`

References to this address:
- from `00000eb4` in `FUN_00000e5c` @ `00000e5c` type=UNCONDITIONAL_CALL

Instructions near `000017d4`:

```asm
000017aa: bx lr
000017ac: movw r2,#0x45fc
000017b0: movt r2,#0x2000
000017b4: ldr r3,[r2,#0x0]
000017b6: cbnz r3,0x000017c0
000017b8: b 0x000017cc
000017ba: ldr r2,[r3,#0x8]
000017bc: cbz r2,0x000017c6
000017be: movs r3,r2
000017c0: cmp r3,r0
000017c2: bne 0x000017ba
000017c4: bx lr
000017c6: str r0,[r3,#0x8]
000017c8: str r2,[r0,#0x8]
000017ca: b 0x000017c4
000017cc: str r0,[r2,#0x0]
000017ce: str r3,[r0,#0x8]
000017d0: b 0x000017c4
000017d4: movw r3,#0x45fc
000017d8: movt r3,#0x2000
000017dc: push {r4,lr}
000017de: ldr r4,[r3,#0x0]
000017e0: cbz r4,0x000017ec
000017e2: ldr r3,[r4,#0xc]
000017e4: blx r3
000017e6: ldr r4,[r4,#0x8]
000017e8: cmp r4,#0x0
000017ea: bne 0x000017e2
000017ec: pop {r4,pc}
00001834: movw r3,#0x1f4
00001838: push {r4,r5,r6,lr}
0000183a: udiv r5,r0,r3
0000183e: udiv r6,r1,r3
00001842: cmp r6,r5
00001844: sbcs r3,r3
00001846: str r5,[r2,#0x0]
00001848: ands r6,r3
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_000017d4(void)

{
  int iVar1;
  
  for (iVar1 = _DAT_200045fc; iVar1 != 0; iVar1 = *(int *)(iVar1 + 8)) {
    (**(code **)(iVar1 + 0xc))();
  }
  return;
}
```

### `0000190c` `FUN_0000190c`

References to this address:
- from `000090fa` in `FUN_00009058` @ `00009058` type=UNCONDITIONAL_CALL
- from `00001afe` in `FUN_00001ae8` @ `00001ae8` type=UNCONDITIONAL_CALL

Instructions near `0000190c`:

```asm
000018e8: movs r3,#0x2a
000018ea: strb r0,[r4,r3]
000018ec: subs r3,r0,#0x1
000018ee: sbcs r0,r3
000018f0: movs r3,#0x4
000018f2: movs r2,#0x1
000018f4: rsbs r0,r0
000018f6: bics r0,r3
000018f8: adds r0,#0xa
000018fa: adds r3,#0x24
000018fc: strb r0,[r4,r3]
000018fe: adds r3,#0x3
00001900: strb r2,[r4,r3]
00001902: movs r2,#0x0
00001904: subs r3,#0x2
00001906: movs r0,#0x0
00001908: strb r2,[r4,r3]
0000190a: pop {r4,pc}
0000190c: push {r4,r5,r6,r7,lr}
0000190e: mov r7,r9
00001910: mov lr,r10
00001912: mov r6,r8
00001914: push {r6,r7,lr}
00001916: movw r7,#0x4600
0000191a: movs r3,#0x2b
0000191c: movt r7,#0x2000
00001920: ldrb r3,[r7,r3]
00001922: sub sp,#0x28
00001924: cmp r3,#0x0
00001926: bne 0x0000192a
00001928: b 0x00001aa2
0000192a: movw r3,#0x9cf4
0000192e: movt r3,#0x0
00001932: ldr r3,[r3,#0x0]
00001934: movs r0,#0x7
00001936: mov r8,r3
00001938: mov r2,r8
```

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

### `00002120` `FUN_00002120`

References to this address:
- from `00008992` in `FUN_00008944` @ `00008944` type=UNCONDITIONAL_CALL
- from `00008b78` in `FUN_00008944` @ `00008944` type=UNCONDITIONAL_CALL
- from `00008efa` in `FUN_00008e1c` @ `00008e1c` type=UNCONDITIONAL_CALL

Instructions near `00002120`:

```asm
000020ee: movt r3,#0x2000
000020f2: strb r0,[r3,#0x0]
000020f4: movw r3,#0x5a61
000020f8: movt r3,#0x2000
000020fc: strb r1,[r3,#0x0]
000020fe: movw r3,#0x5a5e
00002102: movt r3,#0x2000
00002106: strh r2,[r3,#0x0]
00002108: movw r3,#0x5a5c
0000210c: movs r2,#0x1
0000210e: movt r3,#0x2000
00002112: movs r0,#0x0
00002114: strb r2,[r3,#0x0]
00002116: pop {r4,pc}
00002118: movs r2,#0x20
0000211a: movs r0,#0x5
0000211c: movs r1,#0x1
0000211e: b 0x000020ea
00002120: push {r4,r5,r6,r7,lr}
00002122: mov r7,r10
00002124: mov lr,r11
00002126: mov r6,r9
00002128: mov r5,r8
0000212a: movw r3,#0x5a5c
0000212e: push {r5,r6,r7,lr}
00002130: movt r3,#0x2000
00002134: ldrb r3,[r3,#0x0]
00002136: mov r10,r0
00002138: sub sp,#0x1c
0000213a: cmp r3,#0x0
0000213c: bne 0x00002140
0000213e: b 0x000022a6
00002140: cmp r0,#0x0
00002142: bne 0x00002146
00002144: b 0x000022a6
00002146: movw r8,#0x5a61
0000214a: movt r8,#0x2000
```

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

### `0000308c` `FUN_0000308c`

References to this address:
- from `00008b32` in `FUN_00008944` @ `00008944` type=UNCONDITIONAL_CALL
- from `00008b5e` in `FUN_00008944` @ `00008944` type=UNCONDITIONAL_CALL

Instructions near `0000308c`:

```asm
00003064: bls 0x0000307c
00003066: movw r3,#0x2e31
0000306a: movt r3,#0x2e30
0000306e: str r3,[r2,#0x0]
00003070: movs r3,#0x30
00003072: strb r3,[r0,#0x5]
00003074: movs r0,#0x6
00003076: bx lr
00003078: movs r0,#0x0
0000307a: b 0x00003076
0000307c: movs r3,#0x31
0000307e: movs r2,#0x30
00003080: strb r3,[r0,#0x1]
00003082: subs r3,#0x3
00003084: strb r3,[r0,#0x2]
00003086: strb r2,[r0,#0x3]
00003088: strb r3,[r0,#0x4]
0000308a: b 0x00003070
0000308c: push {r4,r5,r6,r7,lr}
0000308e: add r5,sp,#0x14
00003090: ldmia r5!,{r4}
00003092: movs r6,r0
00003094: ldrb r5,[r5,#0x0]
00003096: cmp r4,#0x0
00003098: bne 0x0000309c
0000309a: b 0x000031f6
0000309c: cmp r1,#0x0
0000309e: bne 0x000030a2
000030a0: b 0x000031f6
000030a2: cmp r2,#0x0
000030a4: bne 0x000030a8
000030a6: b 0x000031f6
000030a8: movs r0,#0x0
000030aa: cmp r3,#0x0
000030ac: bne 0x000030b0
000030ae: b 0x000031f4
000030b0: cmp r6,#0x1
```

```c

undefined4
FUN_0000308c(uint param_1,ushort *param_2,ushort *param_3,ushort *param_4,char *param_5,byte param_6
            )

{
  ushort uVar1;
  undefined4 uVar2;
  
  if (((param_5 == (char *)0x0) || (param_2 == (ushort *)0x0)) || (param_3 == (ushort *)0x0)) {
    uVar2 = 0;
  }
  else {
    uVar2 = 0;
    if (((param_4 != (ushort *)0x0) && (param_1 < 2)) && (0x2d < param_6)) {
      *param_5 = (param_1 == 0) * -0x10 + ' ';
      uVar1 = *param_2;
      param_5[1] = (byte)uVar1 & 0x7f;
      param_5[2] = (byte)(uVar1 >> 7) & 0x7f;
      param_5[3] = (byte)(uVar1 >> 0xe);
      uVar1 = *param_3;
      param_5[4] = (byte)uVar1 & 0x7f;
      param_5[5] = (byte)(uVar1 >> 7) & 0x7f;
      param_5[6] = (byte)(uVar1 >> 0xe);
      uVar1 = *param_4;
      param_5[7] = (byte)uVar1 & 0x7f;
      param_5[8] = (byte)(uVar1 >> 7) & 0x7f;
      param_5[9] = (byte)(uVar1 >> 0xe);
      uVar1 = param_2[1];
      param_5[10] = (byte)uVar1 & 0x7f;
      param_5[0xb] = (byte)(uVar1 >> 7) & 0x7f;
      param_5[0xc] = (byte)(uVar1 >> 0xe);
      uVar1 = param_3[1];
      param_5[0xd] = (byte)uVar1 & 0x7f;
      param_5[0xe] = (byte)(uVar1 >> 7) & 0x7f;
      param_5[0xf] = (byte)(uVar1 >> 0xe);
      uVar1 = param_4[1];
      param_5[0x10] = (byte)uVar1 & 0x7f;
      param_5[0x11] = (byte)(uVar1 >> 7) & 0x7f;
      param_5[0x12] = (byte)(uVar1 >> 0xe);
      uVar1 = param_2[2];
      param_5[0x13] = (byte)uVar1 & 0x7f;
      param_5[0x14] = (byte)(uVar1 >> 7) & 0x7f;
      param_5[0x15] = (byte)(uVar1 >> 0xe);
      uVar1 = param_3[2];
      param_5[0x16] = (byte)uVar1 & 0x7f;
      param_5[0x17] = (byte)(uVar1 >> 7) & 0x7f;
      param_5[0x18] = (byte)(uVar1 >> 0xe);
      uVar1 = param_4[2];
      param_5[0x19] = (byte)uVar1 & 0x7f;
      param_5[0x1a] = (byte)(uVar1 >> 7) & 0x7f;
      param_5[0x1b] = (byte)(uVar1 >> 0xe);
      uVar1 = param_2[3];
      param_5[0x1c] = (byte)uVar1 & 0x7f;
      param_5[0x1d] = (byte)(uVar1 >> 7) & 0x7f;
      param_5[0x1e] = (byte)(uVar1 >> 0xe);
      uVar1 = param_3[3];
      param_5[0x1f] = (byte)uVar1 & 0x7f;
      param_5[0x20] = (byte)(uVar1 >> 7) & 0x7f;
      param_5[0x21] = (byte)(uVar1 >> 0xe);
      uVar1 = param_4[3];
      param_5[0x22] = (byte)uVar1 & 0x7f;
      param_5[0x23] = (byte)(uVar1 >> 7) & 0x7f;
      param_5[0x24] = (byte)(uVar1 >> 0xe);
      uVar1 = param_2[4];
      param_5[0x25] = (byte)uVar1 & 0x7f;
      param_5[0x26] = (byte)(uVar1 >> 7) & 0x7f;
      param_5[0x27] = (byte)(uVar1 >> 0xe);
      uVar1 = param_3[4];
      param_5[0x28] = (byte)uVar1 & 0x7f;
      param_5[0x29] = (byte)(uVar1 >> 7) & 0x7f;
      param_5[0x2a] = (byte)(uVar1 >> 0xe);
      uVar1 = param_4[4];
      param_5[0x2b] = (byte)uVar1 & 0x7f;
      param_5[0x2c] = (byte)(uVar1 >> 7) & 0x7f;
      uVar2 = 0x2e;
      param_5[0x2d] = (byte)(uVar1 >> 0xe);
    }
  }
  return uVar2;
}
```

### `00008944` `FUN_00008944`

References to this address:
- from `00008e26` in `FUN_00008e1c` @ `00008e1c` type=UNCONDITIONAL_CALL

Instructions near `00008944`:

```asm
0000890a: cmp r0,#0x1
0000890c: beq 0x00008918
0000890e: movw r0,#0x9cc4
00008912: movt r0,#0x0
00008916: pop {r4,pc}
00008918: movw r0,#0x9cd4
0000891c: movt r0,#0x0
00008920: b 0x00008916
00008924: push {r4,lr}
00008926: bl 0x00000e50
0000892a: cmp r0,#0x1
0000892c: beq 0x00008938
0000892e: movw r0,#0x9cbc
00008932: movt r0,#0x0
00008936: pop {r4,pc}
00008938: movw r0,#0x9cc0
0000893c: movt r0,#0x0
00008940: b 0x00008936
00008944: push {r4,r5,r6,r7,lr}
00008946: sub sp,#0xd4
00008948: bl 0x00002fc8
0000894c: movw r3,#0x9c74
00008950: movt r3,#0x0
00008954: ldr r5,[r3,#0x0]
00008956: cmp r0,#0x0
00008958: beq 0x00008a18
0000895a: movs r0,r5
0000895c: bl 0x000038e8
00008960: cmp r0,#0x0
00008962: bne 0x00008a16
00008964: movw r4,#0x6465
00008968: movt r4,#0x2000
0000896c: ldrb r3,[r4,#0x0]
0000896e: cmp r3,#0x0
00008970: beq 0x0000896c
00008972: movw r2,#0x64d4
00008976: movs r3,#0x0
```

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
    iVar3 = FUN_00002fec();
    if (((iVar3 != 0) && (iVar3 = FUN_00000880(auStack_d4), iVar3 == 0)) &&
       (iVar3 = FUN_000008d8(auStack_c4), iVar3 == 0)) {
      iVar3 = FUN_000024ec();
      if (iVar3 != 0) {
        FUN_00009578(&local_e0,iVar3,10);
      }
      bVar1 = false;
      iVar3 = FUN_00002508(0,auStack_b0);
      puVar4 = auStack_b0;
      while( true ) {
        if (iVar3 != 0) {
          *(undefined1 *)((int)puVar4 + 10) = 5;
          *(undefined1 *)((int)puVar4 + 0xb) = 0;
          *puVar4 = 0x80808080;
          puVar4[1] = 0x80808080;
          *(short *)(puVar4 + 2) = (short)DAT_00008e18;
        }
        puVar4 = puVar4 + 3;
        if (bVar1) break;
/* ... truncated ... */
```

## Data Ranges

### `000095f4` len `16`

```
000095f4: f0 08 26 05 f0 08 24 05 06 02 05 02 07 04 0f 09  ..&...$.........
```

### `000095fc` len `32`

```
000095fc: 06 02 05 02 07 04 0f 09 0b 04 0a 04 00 04 01 04  ................
0000960c: 08 02 07 02 0e 09 0d 09 09 04 08 04 02 04 03 04  ................
```

### `00009664` len `32`

```
00009664: 00 03 05 07 01 02 04 06 08 02 08 06 05 01 00 07  ................
00009674: 04 03 ff ff 64 8c 8c 8c 64 00 00 00 31 2e 30 2e  ....d...d...1.0.
```

### `00002ac0` len `48`

```
00002ac0: 70 47 c0 46 10 b5 03 79 02 2b 0a d0 04 2b 00 d0  pG.F...y.+...+..
00002ad0: 10 bd 01 7a 44 f2 a0 00 c2 f2 00 00 fe f7 46 f9  ...zD.........F.
00002ae0: f6 e7 45 f6 60 33 01 22 c2 f2 00 03 1a 70 ef e7  ..E.`3.".....p..
```

### `000097e4` len `192`

```
000097e4: 01 02 00 00 02 00 02 01 02 02 02 03 00 00 00 00  ................
000097f4: 00 00 00 00 00 00 00 00 00 00 00 00 04 98 00 00  ................
00009804: 00 01 00 00 d8 40 00 20 0f 00 ff ff 00 00 00 00  .....@. ........
00009814: ff ff 00 00 00 00 00 00 c0 5d 00 00 00 00 00 00  .........]......
00009824: e0 2e 00 00 00 02 08 00 d5 29 00 00 00 00 00 00  .........)......
00009834: 38 98 00 00 00 00 00 00 00 00 00 00 00 00 00 00  8...............
00009844: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00009854: 00 00 00 00 00 00 ff ff df df 00 00 00 00 00 00  ................
00009864: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00009874: 09 02 00 00 02 04 02 05 02 06 02 07 00 00 00 00  ................
00009884: a8 98 00 00 c5 2a 00 00 00 00 00 00 94 98 00 00  .....*..........
00009894: 00 01 00 00 dc 40 00 20 0f 00 ff ff 00 00 00 00  .....@. ........
```

### `00009874` len `64`

```
00009874: 09 02 00 00 02 04 02 05 02 06 02 07 00 00 00 00  ................
00009884: a8 98 00 00 c5 2a 00 00 00 00 00 00 94 98 00 00  .....*..........
00009894: 00 01 00 00 dc 40 00 20 0f 00 ff ff 00 00 00 00  .....@. ........
000098a4: ff ff 00 00 54 5d 00 20 b4 98 00 00 18 9b 00 00  ....T]. ........
```

