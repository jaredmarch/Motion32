# Motion 32 Flag/Queue Probe

## Functions

### `00003f54` `<none>`

```asm
00003e70: cbz r1,0x00003e8c
00003e72: ldrb r3,[r0,#0x0]
00003e74: cmp r3,#0x41
00003e76: bhi 0x00003e8c
00003e78: ldr r2,[0x00003f84]
00003e7a: lsls r3,r3,#0x2
00003e7c: ldr r3,[r2,r3]
00003e7e: mov pc,r3
00003e8c: add sp,#0xc
00003e8e: pop {pc}
00003f88: movw r0,#0x2e6d
00003f8c: push {r4,lr}
00003f8e: movt r0,#0x0
00003f92: bl 0x00002098
00003f96: pop {r4,pc}
00003f98: movw r3,#0x5cb8
00003f9c: movt r3,#0x2000
00003fa0: ldrb r0,[r3,#0x0]
00003fa2: uxtb r0,r0
00003fa4: bx lr
00003fa8: movw r3,#0x5cb6
```

### `00003f88` `FUN_00003f88`

```c

void FUN_00003f88(void)

{
  FUN_00002098(0x2e6d);
  return;
}
```

Callers:
- `FUN_00001e5c` @ `00001e5c` from `00001e88` type=UNCONDITIONAL_CALL

### `00003f98` `FUN_00003f98`

```c

undefined1 FUN_00003f98(void)

{
  return DAT_20005cb8;
}
```

Callers:
- `FUN_00009e1c` @ `00009e1c` from `00009e20` type=UNCONDITIONAL_CALL

### `00003fa8` `FUN_00003fa8`

```c

undefined1 FUN_00003fa8(void)

{
  return DAT_20005cb6;
}
```

Callers:
- `FUN_00009e1c` @ `00009e1c` from `00009ec4` type=UNCONDITIONAL_CALL

### `00003fb8` `FUN_00003fb8`

```c

void FUN_00003fb8(void)

{
  DAT_20005cb6 = 1;
  return;
}
```

Callers:
- `FUN_00009e1c` @ `00009e1c` from `00009eec` type=UNCONDITIONAL_CALL

### `00003fc8` `FUN_00003fc8`

```c

undefined1 FUN_00003fc8(void)

{
  return DAT_20005cb7;
}
```

Callers:
- `FUN_00009944` @ `00009944` from `00009948` type=UNCONDITIONAL_CALL

### `00003fd8` `FUN_00003fd8`

```c

char FUN_00003fd8(void)

{
  char cVar1;
  
  cVar1 = DAT_20005cb4;
  if (DAT_20005cb4 != '\0') {
    DAT_20005cb4 = '\0';
  }
  return cVar1;
}
```

Callers:
- `FUN_00009944` @ `00009944` from `00009ac8` type=UNCONDITIONAL_CALL

### `00003fec` `FUN_00003fec`

```c

char FUN_00003fec(void)

{
  char cVar1;
  
  cVar1 = DAT_20005cb3;
  if (DAT_20005cb3 != '\0') {
    DAT_20005cb3 = '\0';
  }
  return cVar1;
}
```

Callers:
- `FUN_00009944` @ `00009944` from `00009abe` type=UNCONDITIONAL_CALL

### `00004000` `FUN_00004000`

```c

char FUN_00004000(void)

{
  char cVar1;
  
  cVar1 = DAT_20005cb1;
  if (DAT_20005cb1 != '\0') {
    DAT_20005cb1 = '\0';
  }
  return cVar1;
}
```

Callers:
- `FUN_00009944` @ `00009944` from `00009adc` type=UNCONDITIONAL_CALL
- `FUN_00033498` @ `00033498` from `0003353a` type=PARAM

### `00004014` `FUN_00004014`

```c

char FUN_00004014(void)

{
  char cVar1;
  
  cVar1 = DAT_20005cb0;
  if (DAT_20005cb0 != '\0') {
    DAT_20005cb0 = '\0';
  }
  return cVar1;
}
```

Callers:
- `FUN_00009944` @ `00009944` from `00009ae6` type=UNCONDITIONAL_CALL

### `00004028` `FUN_00004028`

```c

undefined1 FUN_00004028(void)

{
  return DAT_20005cae;
}
```

Callers:
- `FUN_00009944` @ `00009944` from `00009d1c` type=UNCONDITIONAL_CALL

### `00004034` `FUN_00004034`

```c

char FUN_00004034(void)

{
  char cVar1;
  
  cVar1 = DAT_20005caf;
  if (DAT_20005caf != '\0') {
    DAT_20005caf = '\0';
  }
  return cVar1;
}
```

Callers:
- `FUN_00009e1c` @ `00009e1c` from `00009e2a` type=UNCONDITIONAL_CALL

### `00004048` `FUN_00004048`

```c

undefined4 FUN_00004048(undefined1 *param_1,uint param_2)

{
  undefined4 uVar1;
  
  if ((param_1 == (undefined1 *)0x0) || (param_2 < 6)) {
    uVar1 = 0;
  }
  else {
    *param_1 = 0x31;
    if ((((uint)(param_1 + 1) & 3) == 0) && ((undefined1 *)0x2 < param_1 + -0x9680)) {
      *(undefined4 *)(param_1 + 1) = 0x2e302e31;
    }
    else {
      param_1[1] = 0x31;
      param_1[2] = 0x2e;
      param_1[3] = 0x30;
      param_1[4] = 0x2e;
    }
    param_1[5] = 0x30;
    uVar1 = 6;
  }
  return uVar1;
}
```

Callers:
- `FUN_00009e1c` @ `00009e1c` from `00009edc` type=UNCONDITIONAL_CALL

### `0000408c` `FUN_0000408c`

```c

undefined4
FUN_0000408c(uint param_1,ushort *param_2,ushort *param_3,ushort *param_4,char *param_5,byte param_6
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

Callers:
- `FUN_00009944` @ `00009944` from `00009b32` type=UNCONDITIONAL_CALL
- `FUN_00009944` @ `00009944` from `00009b5e` type=UNCONDITIONAL_CALL

### `000041fc` `FUN_000041fc`

```c

undefined4
FUN_000041fc(byte *param_1,ushort *param_2,undefined1 *param_3,byte *param_4,undefined1 *param_5,
            byte param_6)

{
  byte bVar1;
  ushort uVar2;
  undefined4 uVar3;
  
  if ((((param_5 == (undefined1 *)0x0) || (param_1 == (byte *)0x0)) || (param_2 == (ushort *)0x0))
     || (((param_3 == (undefined1 *)0x0 || (param_4 == (byte *)0x0)) || (param_6 < 0x6d)))) {
    uVar3 = 0;
  }
  else {
    *param_5 = 0x21;
    bVar1 = *param_1;
    param_5[1] = bVar1 & 0x7f;
    param_5[2] = bVar1 >> 7;
    bVar1 = param_1[1];
    param_5[3] = bVar1 & 0x7f;
    param_5[4] = bVar1 >> 7;
    uVar2 = *(ushort *)(param_1 + 2);
    param_5[5] = (byte)uVar2 & 0x7f;
    param_5[6] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[7] = (byte)(uVar2 >> 0xe);
    bVar1 = param_1[4];
    param_5[8] = bVar1 & 0x7f;
    param_5[9] = bVar1 >> 7;
    uVar2 = *(ushort *)(param_1 + 6);
    param_5[10] = (byte)uVar2 & 0x7f;
    param_5[0xb] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0xc] = (byte)(uVar2 >> 0xe);
    uVar2 = *(ushort *)(param_1 + 8);
    param_5[0xd] = (byte)uVar2 & 0x7f;
    param_5[0xe] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0xf] = (byte)(uVar2 >> 0xe);
    uVar2 = *(ushort *)(param_1 + 10);
    param_5[0x10] = (byte)uVar2 & 0x7f;
    param_5[0x12] = (byte)(uVar2 >> 0xe);
    param_5[0x11] = (byte)(uVar2 >> 7) & 0x7f;
    uVar2 = *(ushort *)(param_1 + 0xc);
    param_5[0x13] = (byte)uVar2 & 0x7f;
    param_5[0x14] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x15] = (byte)(uVar2 >> 0xe);
    uVar2 = *param_2;
    param_5[0x16] = (byte)uVar2 & 0x7f;
    param_5[0x17] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x18] = (byte)(uVar2 >> 0xe);
    uVar2 = param_2[1];
    param_5[0x19] = (byte)uVar2 & 0x7f;
    param_5[0x1a] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x1b] = (byte)(uVar2 >> 0xe);
    uVar2 = param_2[2];
    param_5[0x1c] = (byte)uVar2 & 0x7f;
    param_5[0x1d] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x1e] = (byte)(uVar2 >> 0xe);
    uVar2 = param_2[3];
    param_5[0x1f] = (byte)uVar2 & 0x7f;
    param_5[0x20] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x21] = (byte)(uVar2 >> 0xe);
    uVar2 = param_2[4];
    param_5[0x22] = (byte)uVar2 & 0x7f;
    param_5[0x23] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x24] = (byte)(uVar2 >> 0xe);
    uVar2 = param_2[5];
    param_5[0x25] = (byte)uVar2 & 0x7f;
    param_5[0x26] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x27] = (byte)(uVar2 >> 0xe);
    uVar2 = param_2[6];
    param_5[0x28] = (byte)uVar2 & 0x7f;
    param_5[0x29] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x2a] = (byte)(uVar2 >> 0xe);
    uVar2 = param_2[7];
    param_5[0x2b] = (byte)uVar2 & 0x7f;
    param_5[0x2c] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x2d] = (byte)(uVar2 >> 0xe);
    uVar2 = param_2[8];
    param_5[0x2e] = (byte)uVar2 & 0x7f;
    param_5[0x2f] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x30] = (byte)(uVar2 >> 0xe);
    uVar2 = param_2[9];
    param_5[0x31] = (byte)uVar2 & 0x7f;
    param_5[0x32] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x33] = (byte)(uVar2 >> 0xe);
    param_5[0x34] = *param_3;
    bVar1 = param_3[1];
    param_5[0x35] = bVar1 & 0x7f;
    param_5[0x36] = bVar1 >> 7;
    param_5[0x37] = param_3[2];
    uVar2 = *(ushort *)(param_3 + 4);
    param_5[0x38] = (byte)uVar2 & 0x7f;
    param_5[0x39] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x3a] = (byte)(uVar2 >> 0xe);
    uVar2 = *(ushort *)(param_3 + 6);
    param_5[0x3b] = (byte)uVar2 & 0x7f;
    param_5[0x3c] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x3d] = (byte)(uVar2 >> 0xe);
    param_5[0x3e] = param_3[8];
    bVar1 = *param_4;
    param_5[0x3f] = bVar1 & 0x7f;
    param_5[0x40] = bVar1 >> 7;
    bVar1 = param_4[1];
    param_5[0x41] = bVar1 & 0x7f;
    param_5[0x42] = bVar1 >> 7;
    bVar1 = param_4[2];
    param_5[0x43] = bVar1 & 0x7f;
    param_5[0x44] = bVar1 >> 7;
    bVar1 = param_4[3];
    param_5[0x45] = bVar1 & 0x7f;
    param_5[0x46] = bVar1 >> 7;
    bVar1 = param_4[4];
    param_5[0x47] = bVar1 & 0x7f;
    param_5[0x48] = bVar1 >> 7;
    bVar1 = param_4[5];
    param_5[0x49] = bVar1 & 0x7f;
    param_5[0x4a] = bVar1 >> 7;
    bVar1 = param_4[6];
    param_5[0x4b] = bVar1 & 0x7f;
    param_5[0x4c] = bVar1 >> 7;
    bVar1 = param_4[7];
    param_5[0x4d] = bVar1 & 0x7f;
    param_5[0x4e] = bVar1 >> 7;
    bVar1 = param_4[8];
    param_5[0x4f] = bVar1 & 0x7f;
    param_5[0x50] = bVar1 >> 7;
    bVar1 = param_4[9];
    param_5[0x51] = bVar1 & 0x7f;
    param_5[0x52] = bVar1 >> 7;
    bVar1 = param_4[10];
    param_5[0x53] = bVar1 & 0x7f;
    param_5[0x54] = bVar1 >> 7;
    param_5[0x55] = param_4[0xb];
    bVar1 = param_4[0xc];
    param_5[0x56] = bVar1 & 0x7f;
    param_5[0x57] = bVar1 >> 7;
    bVar1 = param_4[0xd];
    param_5[0x58] = bVar1 & 0x7f;
    param_5[0x59] = bVar1 >> 7;
    bVar1 = param_4[0xe];
    param_5[0x5a] = bVar1 & 0x7f;
    param_5[0x5b] = bVar1 >> 7;
    bVar1 = param_4[0xf];
    param_5[0x5c] = bVar1 & 0x7f;
    param_5[0x5d] = bVar1 >> 7;
    bVar1 = param_4[0x10];
    param_5[0x5e] = bVar1 & 0x7f;
    param_5[0x5f] = bVar1 >> 7;
    bVar1 = param_4[0x11];
    param_5[0x60] = bVar1 & 0x7f;
    param_5[0x61] = bVar1 >> 7;
    bVar1 = param_4[0x12];
    param_5[0x62] = bVar1 & 0x7f;
    param_5[99] = bVar1 >> 7;
    bVar1 = param_4[0x13];
    param_5[100] = bVar1 & 0x7f;
    param_5[0x65] = bVar1 >> 7;
    bVar1 = param_4[0x14];
    param_5[0x66] = bVar1 & 0x7f;
    param_5[0x67] = bVar1 >> 7;
    bVar1 = param_4[0x15];
    param_5[0x68] = bVar1 & 0x7f;
    param_5[0x69] = bVar1 >> 7;
    bVar1 = param_4[0x16];
    param_5[0x6a] = bVar1 & 0x7f;
    param_5[0x6b] = bVar1 >> 7;
    uVar3 = 0x6d;
    param_5[0x6c] = param_4[0x17];
  }
  return uVar3;
}
```

Callers:
- `FUN_00009944` @ `00009944` from `00009de0` type=UNCONDITIONAL_CALL

### `0000455c` `FUN_0000455c`

```c

undefined4 FUN_0000455c(uint *param_1,undefined1 *param_2,uint param_3)

{
  ushort uVar1;
  undefined4 uVar2;
  uint uVar3;
  
  uVar2 = 0;
  if (((param_2 != (undefined1 *)0x0) && (param_1 != (uint *)0x0)) && (10 < param_3)) {
    *param_2 = 0x30;
    uVar3 = *param_1 & 0xffff;
    param_2[1] = (byte)*param_1 & 0x7f;
    param_2[3] = (char)(uVar3 >> 0xe);
    param_2[2] = (byte)(uVar3 >> 7) & 0x7f;
    uVar1 = *(ushort *)((int)param_1 + 2);
    param_2[4] = (byte)uVar1 & 0x7f;
    param_2[5] = (byte)(uVar1 >> 7) & 0x7f;
    param_2[6] = (byte)(uVar1 >> 0xe);
    uVar1 = (ushort)param_1[1];
    param_2[7] = (byte)uVar1 & 0x7f;
    param_2[8] = (byte)(uVar1 >> 7) & 0x7f;
    uVar2 = 0xb;
    param_2[9] = (byte)(uVar1 >> 0xe);
    param_2[10] = *(byte *)((int)param_1 + 6) & 0x7f;
  }
  return uVar2;
}
```

Callers:
- `FUN_00009944` @ `00009944` from `00009c0a` type=UNCONDITIONAL_CALL

### `000045b0` `FUN_000045b0`

```c

undefined1 FUN_000045b0(void)

{
  return DAT_20005cb2;
}
```

Callers:
- `FUN_00009944` @ `00009944` from `00009ad2` type=UNCONDITIONAL_CALL

### `000045c0` `FUN_000045c0`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_000045c0(int param_1,undefined4 *param_2,int param_3,int param_4)

{
  undefined4 *puVar1;
  undefined4 uVar2;
  uint uVar3;
  int iVar4;
  
  if ((((param_1 == 0) || (param_2 == (undefined4 *)0x0)) || (param_3 == 0)) || (param_4 == 0)) {
    uVar2 = 1;
  }
  else if (DAT_20005cb2 == '\0') {
    uVar2 = 0x22;
  }
  else {
    iVar4 = param_4;
    FUN_0000a578(param_1,0x20005ca0,0xe,DAT_20005cb2,param_4);
    puVar1 = DAT_00004680;
    if ((((uint)param_2 & 3) == 0) && (param_2 != DAT_00004680)) {
      *param_2 = *(undefined4 *)((int)DAT_00004680 + -2);
      param_2[1] = *(undefined4 *)((int)puVar1 + 2);
      param_2[2] = *(undefined4 *)((int)puVar1 + 6);
      param_2[3] = *(undefined4 *)((int)puVar1 + 10);
      uVar3 = *(uint *)((int)puVar1 + 0xe);
      param_2[4] = uVar3;
    }
    else {
      *(undefined2 *)param_2 = _DAT_20005c8c;
      *(undefined2 *)((int)param_2 + 2) = _DAT_20005c8e;
      *(undefined2 *)(param_2 + 1) = _DAT_20005c90;
      *(undefined2 *)((int)param_2 + 6) = _DAT_20005c92;
      *(undefined2 *)(param_2 + 2) = _DAT_20005c94;
      *(undefined2 *)((int)param_2 + 10) = _DAT_20005c96;
      *(undefined2 *)(param_2 + 3) = _DAT_20005c98;
      *(undefined2 *)((int)param_2 + 0xe) = _DAT_20005c9a;
      *(undefined2 *)(param_2 + 4) = _DAT_20005c9c;
      uVar3 = (uint)_DAT_20005c9e;
      *(ushort *)((int)param_2 + 0x12) = _DAT_20005c9e;
    }
    FUN_0000a578(param_3,0x20005c80,10,uVar3,iVar4);
    FUN_0000a578(param_4,0x20005c68,0xc);
    FUN_0000a578(param_4 + 0xc,0x20005c74,0xc);
    uVar2 = 0;
    DAT_20005cb2 = '\0';
  }
  return uVar2;
}
```

Callers:
- `FUN_00009944` @ `00009944` from `00009c2a` type=UNCONDITIONAL_CALL

## RAM References

### `20005caf`

- from `0000403c` in `FUN_00004034` @ `00004034` type=READ
- from `00004044` in `FUN_00004034` @ `00004034` type=WRITE

#### `FUN_00004034` @ `00004034`

Site `0000403c`:

```asm
00004024: strb r2,[r3,#0x0]
00004026: bx lr
00004028: movw r3,#0x5cae
0000402c: movt r3,#0x2000
00004030: ldrb r0,[r3,#0x0]
00004032: bx lr
00004034: movw r3,#0x5caf
00004038: movt r3,#0x2000
0000403c: ldrb r2,[r3,#0x0]
0000403e: uxtb r0,r2
00004040: cbz r2,0x00004046
00004042: movs r2,#0x0
00004044: strb r2,[r3,#0x0]
00004046: bx lr
00004048: cbz r0,0x00004078
0000404a: cmp r1,#0x5
0000404c: bls 0x00004078
```

Site `00004044`:

```asm
00004030: ldrb r0,[r3,#0x0]
00004032: bx lr
00004034: movw r3,#0x5caf
00004038: movt r3,#0x2000
0000403c: ldrb r2,[r3,#0x0]
0000403e: uxtb r0,r2
00004040: cbz r2,0x00004046
00004042: movs r2,#0x0
00004044: strb r2,[r3,#0x0]
00004046: bx lr
00004048: cbz r0,0x00004078
0000404a: cmp r1,#0x5
0000404c: bls 0x00004078
0000404e: movs r3,#0x31
00004050: adds r2,r0,#0x1
00004052: strb r3,[r0,#0x0]
00004054: lsls r3,r2,#0x1e
```

```c

char FUN_00004034(void)

{
  char cVar1;
  
  cVar1 = DAT_20005caf;
  if (DAT_20005caf != '\0') {
    DAT_20005caf = '\0';
  }
  return cVar1;
}
```

### `20005cb0`

- from `0000401c` in `FUN_00004014` @ `00004014` type=READ
- from `00004024` in `FUN_00004014` @ `00004014` type=WRITE

#### `FUN_00004014` @ `00004014`

Site `0000401c`:

```asm
00004008: ldrb r2,[r3,#0x0]
0000400a: uxtb r0,r2
0000400c: cbz r2,0x00004012
0000400e: movs r2,#0x0
00004010: strb r2,[r3,#0x0]
00004012: bx lr
00004014: movw r3,#0x5cb0
00004018: movt r3,#0x2000
0000401c: ldrb r2,[r3,#0x0]
0000401e: uxtb r0,r2
00004020: cbz r2,0x00004026
00004022: movs r2,#0x0
00004024: strb r2,[r3,#0x0]
00004026: bx lr
00004028: movw r3,#0x5cae
0000402c: movt r3,#0x2000
00004030: ldrb r0,[r3,#0x0]
```

Site `00004024`:

```asm
00004010: strb r2,[r3,#0x0]
00004012: bx lr
00004014: movw r3,#0x5cb0
00004018: movt r3,#0x2000
0000401c: ldrb r2,[r3,#0x0]
0000401e: uxtb r0,r2
00004020: cbz r2,0x00004026
00004022: movs r2,#0x0
00004024: strb r2,[r3,#0x0]
00004026: bx lr
00004028: movw r3,#0x5cae
0000402c: movt r3,#0x2000
00004030: ldrb r0,[r3,#0x0]
00004032: bx lr
00004034: movw r3,#0x5caf
00004038: movt r3,#0x2000
0000403c: ldrb r2,[r3,#0x0]
```

```c

char FUN_00004014(void)

{
  char cVar1;
  
  cVar1 = DAT_20005cb0;
  if (DAT_20005cb0 != '\0') {
    DAT_20005cb0 = '\0';
  }
  return cVar1;
}
```

### `20005cb1`

- from `00004008` in `FUN_00004000` @ `00004000` type=READ
- from `00004010` in `FUN_00004000` @ `00004000` type=WRITE

#### `FUN_00004000` @ `00004000`

Site `00004008`:

```asm
00003ff4: ldrb r2,[r3,#0x0]
00003ff6: uxtb r0,r2
00003ff8: cbz r2,0x00003ffe
00003ffa: movs r2,#0x0
00003ffc: strb r2,[r3,#0x0]
00003ffe: bx lr
00004000: movw r3,#0x5cb1
00004004: movt r3,#0x2000
00004008: ldrb r2,[r3,#0x0]
0000400a: uxtb r0,r2
0000400c: cbz r2,0x00004012
0000400e: movs r2,#0x0
00004010: strb r2,[r3,#0x0]
00004012: bx lr
00004014: movw r3,#0x5cb0
00004018: movt r3,#0x2000
0000401c: ldrb r2,[r3,#0x0]
```

Site `00004010`:

```asm
00003ffc: strb r2,[r3,#0x0]
00003ffe: bx lr
00004000: movw r3,#0x5cb1
00004004: movt r3,#0x2000
00004008: ldrb r2,[r3,#0x0]
0000400a: uxtb r0,r2
0000400c: cbz r2,0x00004012
0000400e: movs r2,#0x0
00004010: strb r2,[r3,#0x0]
00004012: bx lr
00004014: movw r3,#0x5cb0
00004018: movt r3,#0x2000
0000401c: ldrb r2,[r3,#0x0]
0000401e: uxtb r0,r2
00004020: cbz r2,0x00004026
00004022: movs r2,#0x0
00004024: strb r2,[r3,#0x0]
```

```c

char FUN_00004000(void)

{
  char cVar1;
  
  cVar1 = DAT_20005cb1;
  if (DAT_20005cb1 != '\0') {
    DAT_20005cb1 = '\0';
  }
  return cVar1;
}
```

### `20005cb2`

- from `000045b8` in `FUN_000045b0` @ `000045b0` type=READ
- from `000045d8` in `FUN_000045c0` @ `000045c0` type=READ
- from `00004640` in `FUN_000045c0` @ `000045c0` type=WRITE

#### `FUN_000045b0` @ `000045b0`

Site `000045b8`:

```asm
000045a4: lsrs r2,r2,#0xe
000045a6: strb r2,[r1,#0x9]
000045a8: ldrb r2,[r4,#0x6]
000045aa: ands r3,r2
000045ac: strb r3,[r1,#0xa]
000045ae: pop {r4,pc}
000045b0: movw r3,#0x5cb2
000045b4: movt r3,#0x2000
000045b8: ldrb r0,[r3,#0x0]
000045ba: uxtb r0,r0
000045bc: bx lr
000045c0: push {r3,r4,r5,r6,r7,lr}
000045c2: movs r4,r1
000045c4: movs r7,r2
000045c6: movs r5,r3
000045c8: cbz r0,0x00004644
000045ca: cbz r1,0x00004644
```

```c

undefined1 FUN_000045b0(void)

{
  return DAT_20005cb2;
}
```

#### `FUN_000045c0` @ `000045c0`

Site `000045d8`:

```asm
000045c4: movs r7,r2
000045c6: movs r5,r3
000045c8: cbz r0,0x00004644
000045ca: cbz r1,0x00004644
000045cc: cbz r2,0x00004644
000045ce: cbz r3,0x00004644
000045d0: movw r6,#0x5cb2
000045d4: movt r6,#0x2000
000045d8: ldrb r3,[r6,#0x0]
000045da: cmp r3,#0x0
000045dc: beq 0x00004648
000045de: movw r1,#0x5ca0
000045e2: movs r2,#0xe
000045e4: movt r1,#0x2000
000045e8: bl 0x0000a578
000045ec: lsls r3,r4,#0x1e
000045ee: bne 0x0000464c
```

Site `00004640`:

```asm
0000462e: movs r0,r5
00004630: movs r1,r4
00004632: movs r2,#0xc
00004634: adds r0,#0xc
00004636: adds r1,#0xc
00004638: bl 0x0000a578
0000463c: movs r3,#0x0
0000463e: movs r0,#0x0
00004640: strb r3,[r6,#0x0]
00004642: b 0x00004646
00004644: movs r0,#0x1
00004646: pop {r3,r4,r5,r6,r7,pc}
00004648: movs r0,#0x22
0000464a: b 0x00004646
0000464c: movw r3,#0x5c8c
00004650: movt r3,#0x2000
00004654: ldrh r2,[r3,#0x0]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_000045c0(int param_1,undefined4 *param_2,int param_3,int param_4)

{
  undefined4 *puVar1;
  undefined4 uVar2;
  uint uVar3;
  int iVar4;
  
  if ((((param_1 == 0) || (param_2 == (undefined4 *)0x0)) || (param_3 == 0)) || (param_4 == 0)) {
    uVar2 = 1;
  }
  else if (DAT_20005cb2 == '\0') {
    uVar2 = 0x22;
  }
  else {
    iVar4 = param_4;
    FUN_0000a578(param_1,0x20005ca0,0xe,DAT_20005cb2,param_4);
    puVar1 = DAT_00004680;
    if ((((uint)param_2 & 3) == 0) && (param_2 != DAT_00004680)) {
      *param_2 = *(undefined4 *)((int)DAT_00004680 + -2);
      param_2[1] = *(undefined4 *)((int)puVar1 + 2);
      param_2[2] = *(undefined4 *)((int)puVar1 + 6);
      param_2[3] = *(undefined4 *)((int)puVar1 + 10);
      uVar3 = *(uint *)((int)puVar1 + 0xe);
      param_2[4] = uVar3;
    }
    else {
      *(undefined2 *)param_2 = _DAT_20005c8c;
      *(undefined2 *)((int)param_2 + 2) = _DAT_20005c8e;
      *(undefined2 *)(param_2 + 1) = _DAT_20005c90;
      *(undefined2 *)((int)param_2 + 6) = _DAT_20005c92;
      *(undefined2 *)(param_2 + 2) = _DAT_20005c94;
      *(undefined2 *)((int)param_2 + 10) = _DAT_20005c96;
      *(undefined2 *)(param_2 + 3) = _DAT_20005c98;
      *(undefined2 *)((int)param_2 + 0xe) = _DAT_20005c9a;
      *(undefined2 *)(param_2 + 4) = _DAT_20005c9c;
      uVar3 = (uint)_DAT_20005c9e;
      *(ushort *)((int)param_2 + 0x12) = _DAT_20005c9e;
    }
    FUN_0000a578(param_3,0x20005c80,10,uVar3,iVar4);
    FUN_0000a578(param_4,0x20005c68,0xc);
    FUN_0000a578(param_4 + 0xc,0x20005c74,0xc);
    uVar2 = 0;
    DAT_20005cb2 = '\0';
  }
  return uVar2;
}
```

### `20005cb3`

- from `00003ff4` in `FUN_00003fec` @ `00003fec` type=READ
- from `00003ffc` in `FUN_00003fec` @ `00003fec` type=WRITE

#### `FUN_00003fec` @ `00003fec`

Site `00003ff4`:

```asm
00003fe0: ldrb r2,[r3,#0x0]
00003fe2: uxtb r0,r2
00003fe4: cbz r2,0x00003fea
00003fe6: movs r2,#0x0
00003fe8: strb r2,[r3,#0x0]
00003fea: bx lr
00003fec: movw r3,#0x5cb3
00003ff0: movt r3,#0x2000
00003ff4: ldrb r2,[r3,#0x0]
00003ff6: uxtb r0,r2
00003ff8: cbz r2,0x00003ffe
00003ffa: movs r2,#0x0
00003ffc: strb r2,[r3,#0x0]
00003ffe: bx lr
00004000: movw r3,#0x5cb1
00004004: movt r3,#0x2000
00004008: ldrb r2,[r3,#0x0]
```

Site `00003ffc`:

```asm
00003fe8: strb r2,[r3,#0x0]
00003fea: bx lr
00003fec: movw r3,#0x5cb3
00003ff0: movt r3,#0x2000
00003ff4: ldrb r2,[r3,#0x0]
00003ff6: uxtb r0,r2
00003ff8: cbz r2,0x00003ffe
00003ffa: movs r2,#0x0
00003ffc: strb r2,[r3,#0x0]
00003ffe: bx lr
00004000: movw r3,#0x5cb1
00004004: movt r3,#0x2000
00004008: ldrb r2,[r3,#0x0]
0000400a: uxtb r0,r2
0000400c: cbz r2,0x00004012
0000400e: movs r2,#0x0
00004010: strb r2,[r3,#0x0]
```

```c

char FUN_00003fec(void)

{
  char cVar1;
  
  cVar1 = DAT_20005cb3;
  if (DAT_20005cb3 != '\0') {
    DAT_20005cb3 = '\0';
  }
  return cVar1;
}
```

### `20006465`

- from `0000a0dc` in `FUN_0000a058` @ `0000a058` type=READ
- from `0000a0e6` in `FUN_0000a058` @ `0000a058` type=WRITE
- from `00002984` in `FUN_0000290c` @ `0000290c` type=READ
- from `0000298e` in `FUN_0000290c` @ `0000290c` type=WRITE
- from `0000996c` in `FUN_00009944` @ `00009944` type=READ
- from `00009980` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009af6` in `FUN_00009944` @ `00009944` type=READ
- from `00009b0a` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009a2a` in `FUN_00009944` @ `00009944` type=READ
- from `00009a40` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009a6a` in `FUN_00009944` @ `00009944` type=READ
- from `00009a72` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009e52` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009e68` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `00009e8c` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009e94` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `0000175e` in `FUN_000016b8` @ `000016b8` type=READ
- from `00001768` in `FUN_000016b8` @ `000016b8` type=WRITE

#### `FUN_0000a058` @ `0000a058`

Site `0000a0dc`:

```asm
0000a0ca: beq 0x0000a0f6
0000a0cc: subs r5,#0x1
0000a0ce: uxth r5,r5
0000a0d0: cbz r5,0x0000a0f6
0000a0d2: movs r0,r6
0000a0d4: bl 0x000048e8
0000a0d8: cmp r0,#0x0
0000a0da: bne 0x0000a0c6
0000a0dc: ldrb r3,[r4,#0x0]
0000a0de: cmp r3,#0x0
0000a0e0: beq 0x0000a0dc
0000a0e2: mov r3,r8
0000a0e4: movs r2,#0x0
0000a0e6: strb r3,[r4,#0x0]
0000a0e8: movs r1,#0x0
0000a0ea: movs r3,#0x0
0000a0ec: movs r0,r6
```

Site `0000a0e6`:

```asm
0000a0d4: bl 0x000048e8
0000a0d8: cmp r0,#0x0
0000a0da: bne 0x0000a0c6
0000a0dc: ldrb r3,[r4,#0x0]
0000a0de: cmp r3,#0x0
0000a0e0: beq 0x0000a0dc
0000a0e2: mov r3,r8
0000a0e4: movs r2,#0x0
0000a0e6: strb r3,[r4,#0x0]
0000a0e8: movs r1,#0x0
0000a0ea: movs r3,#0x0
0000a0ec: movs r0,r6
0000a0ee: bl 0x00004ce8
0000a0f2: b 0x0000a0c6
0000a0f4: b 0x0000a0f4
0000a0f6: bl 0x000028d0
0000a0fa: bl 0x0000290c
```

```c

void FUN_0000a058(void)

{
  int iVar1;
  undefined4 *puVar2;
  short sVar3;
  
  FUN_000019c0();
  iVar1 = FUN_000014e4();
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar1 = FUN_00003370();
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  FUN_000019e8();
  FUN_00001bf0();
  puVar2 = (undefined4 *)FUN_00001780();
  if (puVar2 == (undefined4 *)0x0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar1 = FUN_00004690(*puVar2,puVar2[1]);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar1 = FUN_00004690(0xf240bb40,0x883331ff);
  if (iVar1 == 0) {
    if (DAT_d0f52807 != '\x01') {
      sVar3 = 100;
      do {
        iVar1 = FUN_000048e8(0x2b007de3);
        if (iVar1 == 0) {
          do {
          } while (DAT_20006465 == '\0');
          DAT_20006465 = '\0';
          FUN_00004ce8(0x2b007de3,0,0,0);
        }
      } while ((DAT_d0f52807 != '\x01') && (sVar3 = sVar3 + -1, sVar3 != 0));
    }
    FUN_000028d0();
    FUN_0000290c();
    FUN_00002b08();
    FUN_000030cc();
    FUN_000027a0(0x200064c4,&DAT_00008e1d);
    FUN_000027ac(0x200064c4);
    return;
  }
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

#### `FUN_0000290c` @ `0000290c`

Site `00002984`:

```asm
0000296c: movw r10,#0x28
00002970: movt r3,#0x0
00002974: ldr r6,[r3,#0x0]
00002976: movt r4,#0x2000
0000297a: movs r0,r6
0000297c: bl 0x000048e8
00002980: cmp r0,#0x0
00002982: bne 0x00002948
00002984: ldrb r3,[r4,#0x0]
00002986: cmp r3,#0x0
00002988: beq 0x00002984
0000298a: mov r3,r9
0000298c: movs r2,#0x0
0000298e: strb r3,[r4,#0x0]
00002990: movs r1,#0x0
00002992: movs r3,#0x0
00002994: movs r0,r6
```

Site `0000298e`:

```asm
0000297c: bl 0x000048e8
00002980: cmp r0,#0x0
00002982: bne 0x00002948
00002984: ldrb r3,[r4,#0x0]
00002986: cmp r3,#0x0
00002988: beq 0x00002984
0000298a: mov r3,r9
0000298c: movs r2,#0x0
0000298e: strb r3,[r4,#0x0]
00002990: movs r1,#0x0
00002992: movs r3,#0x0
00002994: movs r0,r6
00002996: bl 0x00004ce8
0000299a: cmp r0,#0x0
0000299c: bne 0x00002948
0000299e: mov r3,r8
000029a0: ldr r2,[r3,#0x30]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_0000290c(void)

{
  int iVar1;
  char cVar2;
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
  
  if (DAT_2000462b == '\0') {
    iVar1 = 0x21;
  }
  else {
    iVar1 = 7;
    if (_DAT_d0f52800 == 0x43545355) {
      FUN_0000a568(&local_48,0,0x28);
      cVar2 = -0x80;
      do {
        iVar1 = FUN_000048e8(0x2b007de3);
        if (iVar1 != 0) {
          return iVar1;
        }
        do {
        } while (DAT_20006465 == '\0');
        DAT_20006465 = '\0';
        iVar1 = FUN_00004ce8(0x2b007de3,0,0,0);
        if (iVar1 != 0) {
          return iVar1;
        }
        if (((((((DAT_20004628 != '\0') &&
                (local_48 = local_48 + *(ushort *)(_DAT_d0f52830 + 2), DAT_20004628 != '\x01')) &&
               (local_44 = local_44 + *(ushort *)(_DAT_d0f52830 + 6), DAT_20004628 != '\x02')) &&
              ((local_40 = local_40 + *(ushort *)(_DAT_d0f52830 + 10), DAT_20004628 != '\x03' &&
               (local_3c = local_3c + *(ushort *)(_DAT_d0f52830 + 0xe), DAT_20004628 != '\x04'))))
             && ((local_38 = local_38 + *(ushort *)(_DAT_d0f52830 + 0x12), DAT_20004628 != '\x05' &&
                 ((local_34 = local_34 + *(ushort *)(_DAT_d0f52830 + 0x16), DAT_20004628 != '\x06'
                  && (local_30 = local_30 + *(ushort *)(_DAT_d0f52830 + 0x1a), DAT_20004628 != '\a')
                  ))))) &&
            (local_2c = local_2c + *(ushort *)(_DAT_d0f52830 + 0x1e), DAT_20004628 != '\b')) &&
           (local_28 = local_28 + *(ushort *)(_DAT_d0f52830 + 0x22), DAT_20004628 != '\t')) {
          local_24 = local_24 + *(ushort *)(_DAT_d0f52830 + 0x26);
        }
        cVar2 = cVar2 + -1;
      } while (cVar2 != '\0');
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
      iVar1 = 0;
    }
  }
  return iVar1;
}
```

#### `FUN_00009944` @ `00009944`

Site `0000996c`:

```asm
00009956: cmp r0,#0x0
00009958: beq 0x00009a18
0000995a: movs r0,r5
0000995c: bl 0x000048e8
00009960: cmp r0,#0x0
00009962: bne 0x00009a16
00009964: movw r4,#0x6465
00009968: movt r4,#0x2000
0000996c: ldrb r3,[r4,#0x0]
0000996e: cmp r3,#0x0
00009970: beq 0x0000996c
00009972: movw r2,#0x64d4
00009976: movs r3,#0x0
00009978: movs r1,#0x0
0000997a: movt r2,#0x2000
0000997e: movs r0,r5
00009980: strb r3,[r4,#0x0]
```

Site `00009980`:

```asm
0000996c: ldrb r3,[r4,#0x0]
0000996e: cmp r3,#0x0
00009970: beq 0x0000996c
00009972: movw r2,#0x64d4
00009976: movs r3,#0x0
00009978: movs r1,#0x0
0000997a: movt r2,#0x2000
0000997e: movs r0,r5
00009980: strb r3,[r4,#0x0]
00009982: bl 0x00004ce8
00009986: bl 0x00002b44
0000998a: movw r0,#0x64d4
0000998e: movt r0,#0x2000
00009992: bl 0x00003120
00009996: bl 0x0000179c
0000999a: bl 0x00001864
0000999e: cbz r0,0x000099fe
```

Site `00009af6`:

```asm
00009ae4: b 0x00009bf8
00009ae6: bl 0x00004014
00009aea: cmp r0,#0x0
00009aec: beq 0x00009af0
00009aee: b 0x00009d1c
00009af0: add sp,#0xd4
00009af2: pop {r4,r5,r6,r7,pc}
00009af4: b 0x00009af4
00009af6: ldrb r3,[r4,#0x0]
00009af8: cmp r3,#0x0
00009afa: beq 0x00009af6
00009afc: movw r1,#0x64d8
00009b00: movs r3,#0x0
00009b02: movs r2,#0x0
00009b04: movt r1,#0x2000
00009b08: movs r0,r5
00009b0a: strb r3,[r4,#0x0]
```

Site `00009b0a`:

```asm
00009af6: ldrb r3,[r4,#0x0]
00009af8: cmp r3,#0x0
00009afa: beq 0x00009af6
00009afc: movw r1,#0x64d8
00009b00: movs r3,#0x0
00009b02: movs r2,#0x0
00009b04: movt r1,#0x2000
00009b08: movs r0,r5
00009b0a: strb r3,[r4,#0x0]
00009b0c: bl 0x00004ce8
00009b10: movs r3,#0x80
00009b12: str r3,[sp,#0x4]
00009b14: add r3,sp,#0x50
00009b16: movw r2,#0x6494
00009b1a: movw r1,#0x64a8
00009b1e: str r3,[sp,#0x0]
00009b20: movw r3,#0x6480
```

Site `00009a2a`:

```asm
00009a14: b 0x00009a14
00009a16: b 0x00009a16
00009a18: movs r0,r5
00009a1a: bl 0x000048e8
00009a1e: cmp r0,#0x0
00009a20: bne 0x00009af4
00009a22: movw r4,#0x6465
00009a26: movt r4,#0x2000
00009a2a: ldrb r3,[r4,#0x0]
00009a2c: cmp r3,#0x0
00009a2e: beq 0x00009a2a
00009a30: movw r6,#0x64d4
00009a34: movs r3,#0x0
00009a36: movt r6,#0x2000
00009a3a: movs r2,r6
00009a3c: movs r1,#0x0
00009a3e: movs r0,r5
```

Site `00009a40`:

```asm
00009a2c: cmp r3,#0x0
00009a2e: beq 0x00009a2a
00009a30: movw r6,#0x64d4
00009a34: movs r3,#0x0
00009a36: movt r6,#0x2000
00009a3a: movs r2,r6
00009a3c: movs r1,#0x0
00009a3e: movs r0,r5
00009a40: strb r3,[r4,#0x0]
00009a42: bl 0x00004ce8
00009a46: cmp r0,#0x0
00009a48: bne 0x00009a4c
00009a4a: b 0x00009b72
00009a4c: movw r5,#0x64bc
00009a50: movt r5,#0x2000
00009a54: movw r3,#0x9b80
00009a58: movt r3,#0x0
```

Site `00009a6a`:

```asm
00009a54: movw r3,#0x9b80
00009a58: movt r3,#0x0
00009a5c: ldr r6,[r3,#0x0]
00009a5e: movs r0,r6
00009a60: bl 0x000048e8
00009a64: cmp r0,#0x0
00009a66: beq 0x00009a6a
00009a68: b 0x00009b70
00009a6a: ldrb r3,[r4,#0x0]
00009a6c: cmp r3,#0x0
00009a6e: beq 0x00009a6a
00009a70: movs r3,#0x0
00009a72: strb r3,[r4,#0x0]
00009a74: movw r4,#0x64d8
00009a78: movt r4,#0x2000
00009a7c: movs r2,#0x0
00009a7e: movs r1,r4
```

Site `00009a72`:

```asm
00009a60: bl 0x000048e8
00009a64: cmp r0,#0x0
00009a66: beq 0x00009a6a
00009a68: b 0x00009b70
00009a6a: ldrb r3,[r4,#0x0]
00009a6c: cmp r3,#0x0
00009a6e: beq 0x00009a6a
00009a70: movs r3,#0x0
00009a72: strb r3,[r4,#0x0]
00009a74: movw r4,#0x64d8
00009a78: movt r4,#0x2000
00009a7c: movs r2,#0x0
00009a7e: movs r1,r4
00009a80: movs r0,r6
00009a82: bl 0x00004ce8
00009a86: ldrb r3,[r5,#0x0]
00009a88: ldr r0,[r4,#0x0]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009944(void)

{
  bool bVar1;
  int iVar2;
  undefined4 *puVar3;
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
  
  iVar2 = FUN_00003fc8();
  if (iVar2 != 0) {
    iVar2 = FUN_000048e8(0x2b007de3);
    if (iVar2 != 0) {
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    do {
    } while (DAT_20006465 == '\0');
    DAT_20006465 = '\0';
    FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    FUN_0000179c();
    iVar2 = FUN_00001864();
    if ((iVar2 != 0) && (*(char *)(iVar2 + 0x68) != '\0')) {
      _DAT_2000646c = *(undefined2 *)(iVar2 + 6);
      _DAT_2000646e = *(undefined2 *)(iVar2 + 0x10);
      _DAT_20006470 = *(undefined2 *)(iVar2 + 0x1a);
      _DAT_20006472 = *(undefined2 *)(iVar2 + 0x24);
      _DAT_20006474 = *(undefined2 *)(iVar2 + 0x2e);
      _DAT_20006476 = *(undefined2 *)(iVar2 + 0x38);
      _DAT_20006478 = *(undefined2 *)(iVar2 + 0x42);
      _DAT_2000647a = *(undefined2 *)(iVar2 + 0x4c);
      _DAT_2000647c = *(undefined2 *)(iVar2 + 0x56);
      _DAT_2000647e = *(undefined2 *)(iVar2 + 0x60);
      _DAT_20006468 = *(undefined4 *)(iVar2 + 100);
    }
    iVar2 = FUN_000048e8(0xf240bb40);
    if (iVar2 == 0) {
      do {
      } while (DAT_20006465 == '\0');
      DAT_20006465 = 0;
      FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
      iVar2 = FUN_0000408c(0,0x200064a8,&DAT_20006494,0x20006480,auStack_98,0x80);
      if (iVar2 != 0) {
        FUN_00002030(auStack_98,iVar2);
      }
      iVar2 = FUN_00001e50();
      if (iVar2 != 0) {
        return;
      }
      FUN_00009448(1,4000);
      iVar2 = FUN_0000408c(1,DAT_00009e0c,DAT_00009e14,DAT_00009e10,auStack_98,0x80);
      if (iVar2 == 0) {
        return;
      }
      FUN_00002030(auStack_98,iVar2);
      return;
    }
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar2 = FUN_000048e8(0x2b007de3);
  if (iVar2 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar2 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar2 != 0) goto LAB_00009a54;
  FUN_00002b44();
  FUN_00003120(&DAT_200064d4);
  iVar2 = FUN_00001e50();
  if (iVar2 == 0) {
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
    }
  }
  DAT_200064bc = (char)_DAT_200040f8;
LAB_00009a54:
/* ... truncated ... */
```

#### `FUN_00009e1c` @ `00009e1c`

Site `00009e52`:

```asm
00009e3a: movt r3,#0x0
00009e3e: ldr r5,[r3,#0x0]
00009e40: movs r0,r5
00009e42: bl 0x000048e8
00009e46: cmp r0,#0x0
00009e48: bne 0x00009ed6
00009e4a: movw r4,#0x6465
00009e4e: movt r4,#0x2000
00009e52: ldrb r3,[r4,#0x0]
00009e54: cmp r3,#0x0
00009e56: beq 0x00009e52
00009e58: movw r6,#0x64d4
00009e5c: movs r3,#0x0
00009e5e: movt r6,#0x2000
00009e62: movs r2,r6
00009e64: movs r1,#0x0
00009e66: movs r0,r5
```

Site `00009e68`:

```asm
00009e54: cmp r3,#0x0
00009e56: beq 0x00009e52
00009e58: movw r6,#0x64d4
00009e5c: movs r3,#0x0
00009e5e: movt r6,#0x2000
00009e62: movs r2,r6
00009e64: movs r1,#0x0
00009e66: movs r0,r5
00009e68: strb r3,[r4,#0x0]
00009e6a: bl 0x00004ce8
00009e6e: cmp r0,#0x0
00009e70: beq 0x00009ef4
00009e72: movw r5,#0x64bc
00009e76: movt r5,#0x2000
00009e7a: movw r3,#0x9b80
00009e7e: movt r3,#0x0
00009e82: ldr r6,[r3,#0x0]
```

Site `00009e8c`:

```asm
00009e72: movw r5,#0x64bc
00009e76: movt r5,#0x2000
00009e7a: movw r3,#0x9b80
00009e7e: movt r3,#0x0
00009e82: ldr r6,[r3,#0x0]
00009e84: movs r0,r6
00009e86: bl 0x000048e8
00009e8a: cbnz r0,0x00009ef2
00009e8c: ldrb r3,[r4,#0x0]
00009e8e: cmp r3,#0x0
00009e90: beq 0x00009e8c
00009e92: movs r3,#0x0
00009e94: strb r3,[r4,#0x0]
00009e96: movw r4,#0x64d8
00009e9a: movt r4,#0x2000
00009e9e: movs r2,#0x0
00009ea0: movs r1,r4
```

Site `00009e94`:

```asm
00009e82: ldr r6,[r3,#0x0]
00009e84: movs r0,r6
00009e86: bl 0x000048e8
00009e8a: cbnz r0,0x00009ef2
00009e8c: ldrb r3,[r4,#0x0]
00009e8e: cmp r3,#0x0
00009e90: beq 0x00009e8c
00009e92: movs r3,#0x0
00009e94: strb r3,[r4,#0x0]
00009e96: movw r4,#0x64d8
00009e9a: movt r4,#0x2000
00009e9e: movs r2,#0x0
00009ea0: movs r1,r4
00009ea2: movs r0,r6
00009ea4: bl 0x00004ce8
00009ea8: ldrb r3,[r5,#0x0]
00009eaa: cbz r3,0x00009eb6
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009e1c(void)

{
  int iVar1;
  undefined1 auStack_20 [16];
  
  iVar1 = FUN_00003f98();
  if (iVar1 != 0) {
    FUN_00009944();
    goto LAB_00009e2a;
  }
  iVar1 = FUN_000048e8(0x2b007de3);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar1 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar1 == 0) {
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    iVar1 = FUN_00001e50();
    if (iVar1 == 0) {
      if (_DAT_200064d4 < 0x400) {
        _DAT_200064c2 = 0x3ff - _DAT_200064d4;
        if (1000 < (short)_DAT_200064c2) {
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
      }
      else if (_DAT_200040f8 == 0) {
LAB_00009fe8:
        DAT_200064bc = (char)_DAT_200040f8;
      }
      else {
        _DAT_200040f8 = _DAT_200040f8 + -1;
      }
    }
    else if (_DAT_200064d4 < 0x400) {
      _DAT_200064c0 = _DAT_200064d4;
      if (1000 < (short)_DAT_200064d4) {
        _DAT_200064c0 = 0x3ff;
      }
      DAT_200064bc = '\x01';
      _DAT_200040f8 = 4;
    }
    else {
      if (_DAT_200040f8 == 0) goto LAB_00009fe8;
      _DAT_200040f8 = _DAT_200040f8 + -1;
    }
  }
  iVar1 = FUN_000048e8(0xf240bb40);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
  if (DAT_200064bc != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x200;
  }
  if (DAT_200064bd != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x400;
  }
  iVar1 = FUN_00003fa8();
  if (iVar1 == 0) {
    DAT_20006466 = '\0';
  }
  else {
    if (DAT_20006466 == '\0') {
      _DAT_200064c0 = 0;
      _DAT_200064d8 = 0;
      _DAT_200064dc = 0;
      DAT_200064bc = DAT_20006466;
      DAT_200064bd = DAT_20006466;
      _DAT_200064c2 = _DAT_200064c0;
    }
    DAT_20006466 = '\x01';
    FUN_0000234c(_DAT_200064d8,_DAT_200064dc);
    FUN_0000240c();
    FUN_00002618(&DAT_200064c0);
    FUN_00002288(&DAT_200064c0);
  }
LAB_00009e2a:
  iVar1 = FUN_00004034();
  if ((iVar1 != 0) && (iVar1 = FUN_00004048(auStack_20,0x10), iVar1 != 0)) {
    FUN_00002030(auStack_20,iVar1);
    FUN_00003fb8();
  }
  return;
}
```

#### `FUN_000016b8` @ `000016b8`

Site `0000175e`:

```asm
0000174c: beq 0x000016e2
0000174e: subs r5,#0x1
00001750: uxth r5,r5
00001752: cbz r5,0x0000177a
00001754: movs r0,r7
00001756: bl 0x000048e8
0000175a: cmp r0,#0x0
0000175c: bne 0x00001746
0000175e: ldrb r3,[r6,#0x0]
00001760: cmp r3,#0x0
00001762: beq 0x0000175e
00001764: mov r3,r9
00001766: movs r2,#0x0
00001768: strb r3,[r6,#0x0]
0000176a: movs r1,#0x0
0000176c: movs r3,#0x0
0000176e: movs r0,r7
```

Site `00001768`:

```asm
00001756: bl 0x000048e8
0000175a: cmp r0,#0x0
0000175c: bne 0x00001746
0000175e: ldrb r3,[r6,#0x0]
00001760: cmp r3,#0x0
00001762: beq 0x0000175e
00001764: mov r3,r9
00001766: movs r2,#0x0
00001768: strb r3,[r6,#0x0]
0000176a: movs r1,#0x0
0000176c: movs r3,#0x0
0000176e: movs r0,r7
00001770: bl 0x00004ce8
00001774: b 0x00001746
00001776: movs r4,#0x21
00001778: b 0x000016e2
0000177a: movs r4,#0x14
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_000016b8(void)

{
  int iVar1;
  short sVar2;
  
  if (DAT_200041ac == '\0') {
    iVar1 = 0x21;
  }
  else {
    iVar1 = FUN_00004c98(0xf240bb40);
    if ((((iVar1 == 0) && (iVar1 = FUN_00004c98(_DAT_200041b0), iVar1 == 0)) &&
        (iVar1 = FUN_00004690(_DAT_200041b0,_DAT_200041b4), iVar1 == 0)) &&
       ((iVar1 = FUN_00004690(0xf240bb40,0x883331ff), iVar1 == 0 && (DAT_d0f52807 != '\x01')))) {
      sVar2 = 100;
      do {
        iVar1 = FUN_000048e8(0x2b007de3);
        if (iVar1 == 0) {
          do {
          } while (DAT_20006465 == '\0');
          DAT_20006465 = '\0';
          FUN_00004ce8(0x2b007de3,0,0,0);
        }
        if (DAT_d0f52807 == '\x01') {
          return 0;
        }
        sVar2 = sVar2 + -1;
      } while (sVar2 != 0);
      iVar1 = 0x14;
    }
  }
  return iVar1;
}
```

### `20006466`

- from `00009ed2` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `00009ecc` in `FUN_00009e1c` @ `00009e1c` type=PARAM
- from `00009f46` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009f50` in `FUN_00009e1c` @ `00009e1c` type=WRITE

#### `FUN_00009e1c` @ `00009e1c`

Site `00009ed2`:

```asm
00009eba: movw r2,#0x400
00009ebe: ldr r3,[r4,#0x0]
00009ec0: orrs r3,r2
00009ec2: str r3,[r4,#0x0]
00009ec4: bl 0x00003fa8
00009ec8: movw r3,#0x6466
00009ecc: movt r3,#0x2000
00009ed0: cbnz r0,0x00009f46
00009ed2: strb r0,[r3,#0x0]
00009ed4: b 0x00009e2a
00009ed6: b 0x00009ed6
00009ed8: movs r1,#0x10
00009eda: mov r0,sp
00009edc: bl 0x00004048
00009ee0: movs r1,r0
00009ee2: cmp r0,#0x0
00009ee4: beq 0x00009e32
```

Site `00009ecc`:

```asm
00009eb6: ldrb r3,[r5,#0x1]
00009eb8: cbz r3,0x00009ec4
00009eba: movw r2,#0x400
00009ebe: ldr r3,[r4,#0x0]
00009ec0: orrs r3,r2
00009ec2: str r3,[r4,#0x0]
00009ec4: bl 0x00003fa8
00009ec8: movw r3,#0x6466
00009ecc: movt r3,#0x2000
00009ed0: cbnz r0,0x00009f46
00009ed2: strb r0,[r3,#0x0]
00009ed4: b 0x00009e2a
00009ed6: b 0x00009ed6
00009ed8: movs r1,#0x10
00009eda: mov r0,sp
00009edc: bl 0x00004048
00009ee0: movs r1,r0
```

Site `00009f46`:

```asm
00009f36: bls 0x00009fec
00009f38: ldr r2,[r3,#0x0]
00009f3a: cmp r2,#0x0
00009f3c: beq 0x00009fe8
00009f3e: ldr r2,[r3,#0x0]
00009f40: subs r2,#0x1
00009f42: str r2,[r3,#0x0]
00009f44: b 0x00009e7a
00009f46: ldrb r2,[r3,#0x0]
00009f48: cbz r2,0x00009f92
00009f4a: ldr r0,[r4,#0x0]
00009f4c: ldr r1,[r4,#0x4]
00009f4e: movs r2,#0x1
00009f50: strb r2,[r3,#0x0]
00009f52: bl 0x0000234c
00009f56: bl 0x0000240c
00009f5a: movw r0,#0x64c0
```

Site `00009f50`:

```asm
00009f40: subs r2,#0x1
00009f42: str r2,[r3,#0x0]
00009f44: b 0x00009e7a
00009f46: ldrb r2,[r3,#0x0]
00009f48: cbz r2,0x00009f92
00009f4a: ldr r0,[r4,#0x0]
00009f4c: ldr r1,[r4,#0x4]
00009f4e: movs r2,#0x1
00009f50: strb r2,[r3,#0x0]
00009f52: bl 0x0000234c
00009f56: bl 0x0000240c
00009f5a: movw r0,#0x64c0
00009f5e: movt r0,#0x2000
00009f62: bl 0x00002618
00009f66: movw r0,#0x64c0
00009f6a: movt r0,#0x2000
00009f6e: bl 0x00002288
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009e1c(void)

{
  int iVar1;
  undefined1 auStack_20 [16];
  
  iVar1 = FUN_00003f98();
  if (iVar1 != 0) {
    FUN_00009944();
    goto LAB_00009e2a;
  }
  iVar1 = FUN_000048e8(0x2b007de3);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar1 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar1 == 0) {
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    iVar1 = FUN_00001e50();
    if (iVar1 == 0) {
      if (_DAT_200064d4 < 0x400) {
        _DAT_200064c2 = 0x3ff - _DAT_200064d4;
        if (1000 < (short)_DAT_200064c2) {
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
      }
      else if (_DAT_200040f8 == 0) {
LAB_00009fe8:
        DAT_200064bc = (char)_DAT_200040f8;
      }
      else {
        _DAT_200040f8 = _DAT_200040f8 + -1;
      }
    }
    else if (_DAT_200064d4 < 0x400) {
      _DAT_200064c0 = _DAT_200064d4;
      if (1000 < (short)_DAT_200064d4) {
        _DAT_200064c0 = 0x3ff;
      }
      DAT_200064bc = '\x01';
      _DAT_200040f8 = 4;
    }
    else {
      if (_DAT_200040f8 == 0) goto LAB_00009fe8;
      _DAT_200040f8 = _DAT_200040f8 + -1;
    }
  }
  iVar1 = FUN_000048e8(0xf240bb40);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
  if (DAT_200064bc != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x200;
  }
  if (DAT_200064bd != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x400;
  }
  iVar1 = FUN_00003fa8();
  if (iVar1 == 0) {
    DAT_20006466 = '\0';
  }
  else {
    if (DAT_20006466 == '\0') {
      _DAT_200064c0 = 0;
      _DAT_200064d8 = 0;
      _DAT_200064dc = 0;
      DAT_200064bc = DAT_20006466;
      DAT_200064bd = DAT_20006466;
      _DAT_200064c2 = _DAT_200064c0;
    }
    DAT_20006466 = '\x01';
    FUN_0000234c(_DAT_200064d8,_DAT_200064dc);
    FUN_0000240c();
    FUN_00002618(&DAT_200064c0);
    FUN_00002288(&DAT_200064c0);
  }
LAB_00009e2a:
  iVar1 = FUN_00004034();
  if ((iVar1 != 0) && (iVar1 = FUN_00004048(auStack_20,0x10), iVar1 != 0)) {
    FUN_00002030(auStack_20,iVar1);
    FUN_00003fb8();
  }
  return;
}
```

### `200064bc`

- from `00009d82` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009a86` in `FUN_00009944` @ `00009944` type=READ
- from `00009d62` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009d4a` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009ea8` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009f9a` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `00009fe8` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `0000a008` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `00009fd0` in `FUN_00009e1c` @ `00009e1c` type=WRITE

#### `FUN_00009944` @ `00009944`

Site `00009d82`:

```asm
00009d70: movt r2,#0x2000
00009d74: strh r1,[r2,#0x0]
00009d76: ldrh r1,[r2,#0x0]
00009d78: sxth r1,r1
00009d7a: cmp r1,r6
00009d7c: ble 0x00009d80
00009d7e: strh r0,[r2,#0x0]
00009d80: movs r2,#0x1
00009d82: strb r2,[r5,#0x0]
00009d84: adds r2,#0x3
00009d86: str r2,[r3,#0x0]
00009d88: b 0x00009a54
00009d8a: movw r2,#0x3ff
00009d8e: subs r2,r2,r3
00009d90: movw r3,#0x64c0
00009d94: movw r0,#0x3e8
00009d98: sxth r2,r2
```

Site `00009a86`:

```asm
00009a70: movs r3,#0x0
00009a72: strb r3,[r4,#0x0]
00009a74: movw r4,#0x64d8
00009a78: movt r4,#0x2000
00009a7c: movs r2,#0x0
00009a7e: movs r1,r4
00009a80: movs r0,r6
00009a82: bl 0x00004ce8
00009a86: ldrb r3,[r5,#0x0]
00009a88: ldr r0,[r4,#0x0]
00009a8a: cmp r3,#0x0
00009a8c: beq 0x00009a90
00009a8e: b 0x00009bc8
00009a90: ldr r1,[r4,#0x4]
00009a92: ldrb r3,[r5,#0x1]
00009a94: cbz r3,0x00009a9e
00009a96: movw r3,#0x400
```

Site `00009d62`:

```asm
00009d4a: strb r3,[r5,#0x0]
00009d4c: movw r3,#0x40f8
00009d50: movs r2,#0x4
00009d52: movt r3,#0x2000
00009d56: str r2,[r3,#0x0]
00009d58: b 0x00009a54
00009d5a: movw r5,#0x64bc
00009d5e: movt r5,#0x2000
00009d62: strb r2,[r5,#0x0]
00009d64: b 0x00009a54
00009d66: movw r2,#0x64c0
00009d6a: movw r6,#0x3e8
00009d6e: sxth r1,r1
00009d70: movt r2,#0x2000
00009d74: strh r1,[r2,#0x0]
00009d76: ldrh r1,[r2,#0x0]
00009d78: sxth r1,r1
```

Site `00009d4a`:

```asm
00009d36: ldrh r2,[r3,#0x0]
00009d38: sxth r2,r2
00009d3a: cmp r2,r0
00009d3c: ble 0x00009d40
00009d3e: strh r1,[r3,#0x0]
00009d40: movw r5,#0x64bc
00009d44: movs r3,#0x1
00009d46: movt r5,#0x2000
00009d4a: strb r3,[r5,#0x0]
00009d4c: movw r3,#0x40f8
00009d50: movs r2,#0x4
00009d52: movt r3,#0x2000
00009d56: str r2,[r3,#0x0]
00009d58: b 0x00009a54
00009d5a: movw r5,#0x64bc
00009d5e: movt r5,#0x2000
00009d62: strb r2,[r5,#0x0]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009944(void)

{
  bool bVar1;
  int iVar2;
  undefined4 *puVar3;
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
  
  iVar2 = FUN_00003fc8();
  if (iVar2 != 0) {
    iVar2 = FUN_000048e8(0x2b007de3);
    if (iVar2 != 0) {
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    do {
    } while (DAT_20006465 == '\0');
    DAT_20006465 = '\0';
    FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    FUN_0000179c();
    iVar2 = FUN_00001864();
    if ((iVar2 != 0) && (*(char *)(iVar2 + 0x68) != '\0')) {
      _DAT_2000646c = *(undefined2 *)(iVar2 + 6);
      _DAT_2000646e = *(undefined2 *)(iVar2 + 0x10);
      _DAT_20006470 = *(undefined2 *)(iVar2 + 0x1a);
      _DAT_20006472 = *(undefined2 *)(iVar2 + 0x24);
      _DAT_20006474 = *(undefined2 *)(iVar2 + 0x2e);
      _DAT_20006476 = *(undefined2 *)(iVar2 + 0x38);
      _DAT_20006478 = *(undefined2 *)(iVar2 + 0x42);
      _DAT_2000647a = *(undefined2 *)(iVar2 + 0x4c);
      _DAT_2000647c = *(undefined2 *)(iVar2 + 0x56);
      _DAT_2000647e = *(undefined2 *)(iVar2 + 0x60);
      _DAT_20006468 = *(undefined4 *)(iVar2 + 100);
    }
    iVar2 = FUN_000048e8(0xf240bb40);
    if (iVar2 == 0) {
      do {
      } while (DAT_20006465 == '\0');
      DAT_20006465 = 0;
      FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
      iVar2 = FUN_0000408c(0,0x200064a8,&DAT_20006494,0x20006480,auStack_98,0x80);
      if (iVar2 != 0) {
        FUN_00002030(auStack_98,iVar2);
      }
      iVar2 = FUN_00001e50();
      if (iVar2 != 0) {
        return;
      }
      FUN_00009448(1,4000);
      iVar2 = FUN_0000408c(1,DAT_00009e0c,DAT_00009e14,DAT_00009e10,auStack_98,0x80);
      if (iVar2 == 0) {
        return;
      }
      FUN_00002030(auStack_98,iVar2);
      return;
    }
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar2 = FUN_000048e8(0x2b007de3);
  if (iVar2 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar2 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar2 != 0) goto LAB_00009a54;
  FUN_00002b44();
  FUN_00003120(&DAT_200064d4);
  iVar2 = FUN_00001e50();
  if (iVar2 == 0) {
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
    }
  }
  DAT_200064bc = (char)_DAT_200040f8;
LAB_00009a54:
/* ... truncated ... */
```

#### `FUN_00009e1c` @ `00009e1c`

Site `00009ea8`:

```asm
00009e92: movs r3,#0x0
00009e94: strb r3,[r4,#0x0]
00009e96: movw r4,#0x64d8
00009e9a: movt r4,#0x2000
00009e9e: movs r2,#0x0
00009ea0: movs r1,r4
00009ea2: movs r0,r6
00009ea4: bl 0x00004ce8
00009ea8: ldrb r3,[r5,#0x0]
00009eaa: cbz r3,0x00009eb6
00009eac: movw r2,#0x200
00009eb0: ldr r3,[r4,#0x0]
00009eb2: orrs r3,r2
00009eb4: str r3,[r4,#0x0]
00009eb6: ldrb r3,[r5,#0x1]
00009eb8: cbz r3,0x00009ec4
00009eba: movw r2,#0x400
```

Site `00009f9a`:

```asm
00009f86: ldr r2,[r3,#0x0]
00009f88: cbz r2,0x00009fe0
00009f8a: ldr r2,[r3,#0x0]
00009f8c: subs r2,#0x1
00009f8e: str r2,[r3,#0x0]
00009f90: b 0x00009e72
00009f92: movw r1,#0x64c0
00009f96: movt r1,#0x2000
00009f9a: strb r2,[r5,#0x0]
00009f9c: movs r0,#0x0
00009f9e: strb r2,[r5,#0x1]
00009fa0: strh r2,[r1,#0x0]
00009fa2: strh r2,[r1,#0x2]
00009fa4: movs r1,#0x0
00009fa6: str r0,[r4,#0x0]
00009fa8: str r1,[r4,#0x4]
00009faa: b 0x00009f4e
```

Site `00009fe8`:

```asm
00009fd0: strb r3,[r5,#0x0]
00009fd2: movw r3,#0x40f8
00009fd6: movs r2,#0x4
00009fd8: movt r3,#0x2000
00009fdc: str r2,[r3,#0x0]
00009fde: b 0x00009e7a
00009fe0: movw r5,#0x64bc
00009fe4: movt r5,#0x2000
00009fe8: strb r2,[r5,#0x0]
00009fea: b 0x00009e7a
00009fec: movw r2,#0x64c0
00009ff0: movw r6,#0x3e8
00009ff4: sxth r1,r1
00009ff6: movt r2,#0x2000
00009ffa: strh r1,[r2,#0x0]
00009ffc: ldrh r1,[r2,#0x0]
00009ffe: sxth r1,r1
```

Site `0000a008`:

```asm
00009ff6: movt r2,#0x2000
00009ffa: strh r1,[r2,#0x0]
00009ffc: ldrh r1,[r2,#0x0]
00009ffe: sxth r1,r1
0000a000: cmp r1,r6
0000a002: ble 0x0000a006
0000a004: strh r0,[r2,#0x0]
0000a006: movs r2,#0x1
0000a008: strb r2,[r5,#0x0]
0000a00a: adds r2,#0x3
0000a00c: str r2,[r3,#0x0]
0000a00e: b 0x00009e7a
0000a010: movw r2,#0x3ff
0000a014: subs r2,r2,r3
0000a016: movw r3,#0x64c0
0000a01a: movw r0,#0x3e8
0000a01e: sxth r2,r2
```

Site `00009fd0`:

```asm
00009fbc: ldrh r2,[r3,#0x0]
00009fbe: sxth r2,r2
00009fc0: cmp r2,r0
00009fc2: ble 0x00009fc6
00009fc4: strh r1,[r3,#0x0]
00009fc6: movw r5,#0x64bc
00009fca: movs r3,#0x1
00009fcc: movt r5,#0x2000
00009fd0: strb r3,[r5,#0x0]
00009fd2: movw r3,#0x40f8
00009fd6: movs r2,#0x4
00009fd8: movt r3,#0x2000
00009fdc: str r2,[r3,#0x0]
00009fde: b 0x00009e7a
00009fe0: movw r5,#0x64bc
00009fe4: movt r5,#0x2000
00009fe8: strb r2,[r5,#0x0]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009e1c(void)

{
  int iVar1;
  undefined1 auStack_20 [16];
  
  iVar1 = FUN_00003f98();
  if (iVar1 != 0) {
    FUN_00009944();
    goto LAB_00009e2a;
  }
  iVar1 = FUN_000048e8(0x2b007de3);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar1 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar1 == 0) {
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    iVar1 = FUN_00001e50();
    if (iVar1 == 0) {
      if (_DAT_200064d4 < 0x400) {
        _DAT_200064c2 = 0x3ff - _DAT_200064d4;
        if (1000 < (short)_DAT_200064c2) {
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
      }
      else if (_DAT_200040f8 == 0) {
LAB_00009fe8:
        DAT_200064bc = (char)_DAT_200040f8;
      }
      else {
        _DAT_200040f8 = _DAT_200040f8 + -1;
      }
    }
    else if (_DAT_200064d4 < 0x400) {
      _DAT_200064c0 = _DAT_200064d4;
      if (1000 < (short)_DAT_200064d4) {
        _DAT_200064c0 = 0x3ff;
      }
      DAT_200064bc = '\x01';
      _DAT_200040f8 = 4;
    }
    else {
      if (_DAT_200040f8 == 0) goto LAB_00009fe8;
      _DAT_200040f8 = _DAT_200040f8 + -1;
    }
  }
  iVar1 = FUN_000048e8(0xf240bb40);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
  if (DAT_200064bc != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x200;
  }
  if (DAT_200064bd != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x400;
  }
  iVar1 = FUN_00003fa8();
  if (iVar1 == 0) {
    DAT_20006466 = '\0';
  }
  else {
    if (DAT_20006466 == '\0') {
      _DAT_200064c0 = 0;
      _DAT_200064d8 = 0;
      _DAT_200064dc = 0;
      DAT_200064bc = DAT_20006466;
      DAT_200064bd = DAT_20006466;
      _DAT_200064c2 = _DAT_200064c0;
    }
    DAT_20006466 = '\x01';
    FUN_0000234c(_DAT_200064d8,_DAT_200064dc);
    FUN_0000240c();
    FUN_00002618(&DAT_200064c0);
    FUN_00002288(&DAT_200064c0);
  }
LAB_00009e2a:
  iVar1 = FUN_00004034();
  if ((iVar1 != 0) && (iVar1 = FUN_00004048(auStack_20,0x10), iVar1 != 0)) {
    FUN_00002030(auStack_20,iVar1);
    FUN_00003fb8();
  }
  return;
}
```

### `200064bd`

- from `00009db4` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009a92` in `FUN_00009944` @ `00009944` type=READ
- from `00009dcc` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009eb6` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009f9e` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `0000a03a` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `0000a052` in `FUN_00009e1c` @ `00009e1c` type=WRITE

#### `FUN_00009944` @ `00009944`

Site `00009db4`:

```asm
00009da0: ldrh r2,[r3,#0x2]
00009da2: sxth r2,r2
00009da4: cmp r2,r0
00009da6: ble 0x00009daa
00009da8: strh r1,[r3,#0x2]
00009daa: movw r5,#0x64bc
00009dae: movs r3,#0x1
00009db0: movt r5,#0x2000
00009db4: strb r3,[r5,#0x1]
00009db6: movw r3,#0x40f8
00009dba: movs r2,#0x4
00009dbc: movt r3,#0x2000
00009dc0: str r2,[r3,#0x4]
00009dc2: b 0x00009bac
00009dc4: movw r5,#0x64bc
00009dc8: movt r5,#0x2000
00009dcc: strb r2,[r5,#0x1]
```

Site `00009a92`:

```asm
00009a80: movs r0,r6
00009a82: bl 0x00004ce8
00009a86: ldrb r3,[r5,#0x0]
00009a88: ldr r0,[r4,#0x0]
00009a8a: cmp r3,#0x0
00009a8c: beq 0x00009a90
00009a8e: b 0x00009bc8
00009a90: ldr r1,[r4,#0x4]
00009a92: ldrb r3,[r5,#0x1]
00009a94: cbz r3,0x00009a9e
00009a96: movw r3,#0x400
00009a9a: orrs r0,r3
00009a9c: stmia r4!,{r0,r1}
00009a9e: bl 0x0000234c
00009aa2: bl 0x0000240c
00009aa6: movw r0,#0x64c0
00009aaa: movt r0,#0x2000
```

Site `00009dcc`:

```asm
00009db4: strb r3,[r5,#0x1]
00009db6: movw r3,#0x40f8
00009dba: movs r2,#0x4
00009dbc: movt r3,#0x2000
00009dc0: str r2,[r3,#0x4]
00009dc2: b 0x00009bac
00009dc4: movw r5,#0x64bc
00009dc8: movt r5,#0x2000
00009dcc: strb r2,[r5,#0x1]
00009dce: b 0x00009bac
00009dd0: movs r3,#0x80
00009dd2: add r5,sp,#0x50
00009dd4: str r3,[sp,#0x4]
00009dd6: add r1,sp,#0x24
00009dd8: movs r3,r4
00009dda: movs r2,r6
00009ddc: str r5,[sp,#0x0]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009944(void)

{
  bool bVar1;
  int iVar2;
  undefined4 *puVar3;
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
  
  iVar2 = FUN_00003fc8();
  if (iVar2 != 0) {
    iVar2 = FUN_000048e8(0x2b007de3);
    if (iVar2 != 0) {
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    do {
    } while (DAT_20006465 == '\0');
    DAT_20006465 = '\0';
    FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    FUN_0000179c();
    iVar2 = FUN_00001864();
    if ((iVar2 != 0) && (*(char *)(iVar2 + 0x68) != '\0')) {
      _DAT_2000646c = *(undefined2 *)(iVar2 + 6);
      _DAT_2000646e = *(undefined2 *)(iVar2 + 0x10);
      _DAT_20006470 = *(undefined2 *)(iVar2 + 0x1a);
      _DAT_20006472 = *(undefined2 *)(iVar2 + 0x24);
      _DAT_20006474 = *(undefined2 *)(iVar2 + 0x2e);
      _DAT_20006476 = *(undefined2 *)(iVar2 + 0x38);
      _DAT_20006478 = *(undefined2 *)(iVar2 + 0x42);
      _DAT_2000647a = *(undefined2 *)(iVar2 + 0x4c);
      _DAT_2000647c = *(undefined2 *)(iVar2 + 0x56);
      _DAT_2000647e = *(undefined2 *)(iVar2 + 0x60);
      _DAT_20006468 = *(undefined4 *)(iVar2 + 100);
    }
    iVar2 = FUN_000048e8(0xf240bb40);
    if (iVar2 == 0) {
      do {
      } while (DAT_20006465 == '\0');
      DAT_20006465 = 0;
      FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
      iVar2 = FUN_0000408c(0,0x200064a8,&DAT_20006494,0x20006480,auStack_98,0x80);
      if (iVar2 != 0) {
        FUN_00002030(auStack_98,iVar2);
      }
      iVar2 = FUN_00001e50();
      if (iVar2 != 0) {
        return;
      }
      FUN_00009448(1,4000);
      iVar2 = FUN_0000408c(1,DAT_00009e0c,DAT_00009e14,DAT_00009e10,auStack_98,0x80);
      if (iVar2 == 0) {
        return;
      }
      FUN_00002030(auStack_98,iVar2);
      return;
    }
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar2 = FUN_000048e8(0x2b007de3);
  if (iVar2 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar2 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar2 != 0) goto LAB_00009a54;
  FUN_00002b44();
  FUN_00003120(&DAT_200064d4);
  iVar2 = FUN_00001e50();
  if (iVar2 == 0) {
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
    }
  }
  DAT_200064bc = (char)_DAT_200040f8;
LAB_00009a54:
/* ... truncated ... */
```

#### `FUN_00009e1c` @ `00009e1c`

Site `00009eb6`:

```asm
00009ea2: movs r0,r6
00009ea4: bl 0x00004ce8
00009ea8: ldrb r3,[r5,#0x0]
00009eaa: cbz r3,0x00009eb6
00009eac: movw r2,#0x200
00009eb0: ldr r3,[r4,#0x0]
00009eb2: orrs r3,r2
00009eb4: str r3,[r4,#0x0]
00009eb6: ldrb r3,[r5,#0x1]
00009eb8: cbz r3,0x00009ec4
00009eba: movw r2,#0x400
00009ebe: ldr r3,[r4,#0x0]
00009ec0: orrs r3,r2
00009ec2: str r3,[r4,#0x0]
00009ec4: bl 0x00003fa8
00009ec8: movw r3,#0x6466
00009ecc: movt r3,#0x2000
```

Site `00009f9e`:

```asm
00009f8a: ldr r2,[r3,#0x0]
00009f8c: subs r2,#0x1
00009f8e: str r2,[r3,#0x0]
00009f90: b 0x00009e72
00009f92: movw r1,#0x64c0
00009f96: movt r1,#0x2000
00009f9a: strb r2,[r5,#0x0]
00009f9c: movs r0,#0x0
00009f9e: strb r2,[r5,#0x1]
00009fa0: strh r2,[r1,#0x0]
00009fa2: strh r2,[r1,#0x2]
00009fa4: movs r1,#0x0
00009fa6: str r0,[r4,#0x0]
00009fa8: str r1,[r4,#0x4]
00009faa: b 0x00009f4e
00009fac: movw r3,#0x64c0
00009fb0: movw r0,#0x3e8
```

Site `0000a03a`:

```asm
0000a026: ldrh r2,[r3,#0x2]
0000a028: sxth r2,r2
0000a02a: cmp r2,r0
0000a02c: ble 0x0000a030
0000a02e: strh r1,[r3,#0x2]
0000a030: movw r5,#0x64bc
0000a034: movs r3,#0x1
0000a036: movt r5,#0x2000
0000a03a: strb r3,[r5,#0x1]
0000a03c: movw r3,#0x40f8
0000a040: movs r2,#0x4
0000a042: movt r3,#0x2000
0000a046: str r2,[r3,#0x4]
0000a048: b 0x00009f2e
0000a04a: movw r5,#0x64bc
0000a04e: movt r5,#0x2000
0000a052: strb r2,[r5,#0x1]
```

Site `0000a052`:

```asm
0000a03a: strb r3,[r5,#0x1]
0000a03c: movw r3,#0x40f8
0000a040: movs r2,#0x4
0000a042: movt r3,#0x2000
0000a046: str r2,[r3,#0x4]
0000a048: b 0x00009f2e
0000a04a: movw r5,#0x64bc
0000a04e: movt r5,#0x2000
0000a052: strb r2,[r5,#0x1]
0000a054: b 0x00009f2e
0000a058: push {r4,r5,r6,r7,lr}
0000a05a: mov lr,r8
0000a05c: push {lr}
0000a05e: bl 0x000019c0
0000a062: bl 0x000014e4
0000a066: cbz r0,0x0000a06a
0000a068: b 0x0000a068
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009e1c(void)

{
  int iVar1;
  undefined1 auStack_20 [16];
  
  iVar1 = FUN_00003f98();
  if (iVar1 != 0) {
    FUN_00009944();
    goto LAB_00009e2a;
  }
  iVar1 = FUN_000048e8(0x2b007de3);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar1 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar1 == 0) {
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    iVar1 = FUN_00001e50();
    if (iVar1 == 0) {
      if (_DAT_200064d4 < 0x400) {
        _DAT_200064c2 = 0x3ff - _DAT_200064d4;
        if (1000 < (short)_DAT_200064c2) {
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
      }
      else if (_DAT_200040f8 == 0) {
LAB_00009fe8:
        DAT_200064bc = (char)_DAT_200040f8;
      }
      else {
        _DAT_200040f8 = _DAT_200040f8 + -1;
      }
    }
    else if (_DAT_200064d4 < 0x400) {
      _DAT_200064c0 = _DAT_200064d4;
      if (1000 < (short)_DAT_200064d4) {
        _DAT_200064c0 = 0x3ff;
      }
      DAT_200064bc = '\x01';
      _DAT_200040f8 = 4;
    }
    else {
      if (_DAT_200040f8 == 0) goto LAB_00009fe8;
      _DAT_200040f8 = _DAT_200040f8 + -1;
    }
  }
  iVar1 = FUN_000048e8(0xf240bb40);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
  if (DAT_200064bc != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x200;
  }
  if (DAT_200064bd != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x400;
  }
  iVar1 = FUN_00003fa8();
  if (iVar1 == 0) {
    DAT_20006466 = '\0';
  }
  else {
    if (DAT_20006466 == '\0') {
      _DAT_200064c0 = 0;
      _DAT_200064d8 = 0;
      _DAT_200064dc = 0;
      DAT_200064bc = DAT_20006466;
      DAT_200064bd = DAT_20006466;
      _DAT_200064c2 = _DAT_200064c0;
    }
    DAT_20006466 = '\x01';
    FUN_0000234c(_DAT_200064d8,_DAT_200064dc);
    FUN_0000240c();
    FUN_00002618(&DAT_200064c0);
    FUN_00002288(&DAT_200064c0);
  }
LAB_00009e2a:
  iVar1 = FUN_00004034();
  if ((iVar1 != 0) && (iVar1 = FUN_00004048(auStack_20,0x10), iVar1 != 0)) {
    FUN_00002030(auStack_20,iVar1);
    FUN_00003fb8();
  }
  return;
}
```

### `200064d4`

- from `00009b86` in `FUN_00009944` @ `00009944` type=READ
- from `00009bd8` in `FUN_00009944` @ `00009944` type=READ
- from `00009a3a` in `FUN_00009944` @ `00009944` type=PARAM
- from `00009e62` in `FUN_00009e1c` @ `00009e1c` type=PARAM
- from `00009ef8` in `FUN_00009e1c` @ `00009e1c` type=PARAM
- from `00009f08` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009f78` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `0000997a` in `FUN_00009944` @ `00009944` type=PARAM
- from `0000998e` in `FUN_00009944` @ `00009944` type=PARAM
- from `00009b76` in `FUN_00009944` @ `00009944` type=PARAM

#### `FUN_00009944` @ `00009944`

Site `00009b86`:

```asm
00009b6e: b 0x00009af0
00009b70: b 0x00009b70
00009b72: bl 0x00002b44
00009b76: movs r0,r6
00009b78: bl 0x00003120
00009b7c: bl 0x00001e50
00009b80: cbnz r0,0x00009bd4
00009b82: movw r1,#0x3ff
00009b86: ldrh r3,[r6,#0x0]
00009b88: cmp r3,r1
00009b8a: bhi 0x00009b8e
00009b8c: b 0x00009d8a
00009b8e: movw r3,#0x40f8
00009b92: movt r3,#0x2000
00009b96: ldr r2,[r3,#0x4]
00009b98: cmp r2,#0x0
00009b9a: bne 0x00009b9e
```

Site `00009bd8`:

```asm
00009bc4: str r2,[r3,#0x0]
00009bc6: b 0x00009a54
00009bc8: movw r3,#0x200
00009bcc: orrs r0,r3
00009bce: ldr r1,[r4,#0x4]
00009bd0: str r0,[r4,#0x0]
00009bd2: b 0x00009a92
00009bd4: movw r1,#0x3ff
00009bd8: ldrh r2,[r6,#0x0]
00009bda: cmp r2,r1
00009bdc: bhi 0x00009be0
00009bde: b 0x00009d26
00009be0: movw r3,#0x40f8
00009be4: movt r3,#0x2000
00009be8: ldr r2,[r3,#0x0]
00009bea: cmp r2,#0x0
00009bec: bne 0x00009bf0
```

Site `00009a3a`:

```asm
00009a22: movw r4,#0x6465
00009a26: movt r4,#0x2000
00009a2a: ldrb r3,[r4,#0x0]
00009a2c: cmp r3,#0x0
00009a2e: beq 0x00009a2a
00009a30: movw r6,#0x64d4
00009a34: movs r3,#0x0
00009a36: movt r6,#0x2000
00009a3a: movs r2,r6
00009a3c: movs r1,#0x0
00009a3e: movs r0,r5
00009a40: strb r3,[r4,#0x0]
00009a42: bl 0x00004ce8
00009a46: cmp r0,#0x0
00009a48: bne 0x00009a4c
00009a4a: b 0x00009b72
00009a4c: movw r5,#0x64bc
```

Site `0000997a`:

```asm
00009964: movw r4,#0x6465
00009968: movt r4,#0x2000
0000996c: ldrb r3,[r4,#0x0]
0000996e: cmp r3,#0x0
00009970: beq 0x0000996c
00009972: movw r2,#0x64d4
00009976: movs r3,#0x0
00009978: movs r1,#0x0
0000997a: movt r2,#0x2000
0000997e: movs r0,r5
00009980: strb r3,[r4,#0x0]
00009982: bl 0x00004ce8
00009986: bl 0x00002b44
0000998a: movw r0,#0x64d4
0000998e: movt r0,#0x2000
00009992: bl 0x00003120
00009996: bl 0x0000179c
```

Site `0000998e`:

```asm
00009976: movs r3,#0x0
00009978: movs r1,#0x0
0000997a: movt r2,#0x2000
0000997e: movs r0,r5
00009980: strb r3,[r4,#0x0]
00009982: bl 0x00004ce8
00009986: bl 0x00002b44
0000998a: movw r0,#0x64d4
0000998e: movt r0,#0x2000
00009992: bl 0x00003120
00009996: bl 0x0000179c
0000999a: bl 0x00001864
0000999e: cbz r0,0x000099fe
000099a0: movs r3,#0x68
000099a2: ldrb r3,[r0,r3]
000099a4: cbz r3,0x000099fe
000099a6: movw r3,#0x646c
```

Site `00009b76`:

```asm
00009b62: movs r1,r0
00009b64: cmp r0,#0x0
00009b66: beq 0x00009af0
00009b68: add r0,sp,#0x50
00009b6a: bl 0x00002030
00009b6e: b 0x00009af0
00009b70: b 0x00009b70
00009b72: bl 0x00002b44
00009b76: movs r0,r6
00009b78: bl 0x00003120
00009b7c: bl 0x00001e50
00009b80: cbnz r0,0x00009bd4
00009b82: movw r1,#0x3ff
00009b86: ldrh r3,[r6,#0x0]
00009b88: cmp r3,r1
00009b8a: bhi 0x00009b8e
00009b8c: b 0x00009d8a
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009944(void)

{
  bool bVar1;
  int iVar2;
  undefined4 *puVar3;
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
  
  iVar2 = FUN_00003fc8();
  if (iVar2 != 0) {
    iVar2 = FUN_000048e8(0x2b007de3);
    if (iVar2 != 0) {
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    do {
    } while (DAT_20006465 == '\0');
    DAT_20006465 = '\0';
    FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    FUN_0000179c();
    iVar2 = FUN_00001864();
    if ((iVar2 != 0) && (*(char *)(iVar2 + 0x68) != '\0')) {
      _DAT_2000646c = *(undefined2 *)(iVar2 + 6);
      _DAT_2000646e = *(undefined2 *)(iVar2 + 0x10);
      _DAT_20006470 = *(undefined2 *)(iVar2 + 0x1a);
      _DAT_20006472 = *(undefined2 *)(iVar2 + 0x24);
      _DAT_20006474 = *(undefined2 *)(iVar2 + 0x2e);
      _DAT_20006476 = *(undefined2 *)(iVar2 + 0x38);
      _DAT_20006478 = *(undefined2 *)(iVar2 + 0x42);
      _DAT_2000647a = *(undefined2 *)(iVar2 + 0x4c);
      _DAT_2000647c = *(undefined2 *)(iVar2 + 0x56);
      _DAT_2000647e = *(undefined2 *)(iVar2 + 0x60);
      _DAT_20006468 = *(undefined4 *)(iVar2 + 100);
    }
    iVar2 = FUN_000048e8(0xf240bb40);
    if (iVar2 == 0) {
      do {
      } while (DAT_20006465 == '\0');
      DAT_20006465 = 0;
      FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
      iVar2 = FUN_0000408c(0,0x200064a8,&DAT_20006494,0x20006480,auStack_98,0x80);
      if (iVar2 != 0) {
        FUN_00002030(auStack_98,iVar2);
      }
      iVar2 = FUN_00001e50();
      if (iVar2 != 0) {
        return;
      }
      FUN_00009448(1,4000);
      iVar2 = FUN_0000408c(1,DAT_00009e0c,DAT_00009e14,DAT_00009e10,auStack_98,0x80);
      if (iVar2 == 0) {
        return;
      }
      FUN_00002030(auStack_98,iVar2);
      return;
    }
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar2 = FUN_000048e8(0x2b007de3);
  if (iVar2 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar2 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar2 != 0) goto LAB_00009a54;
  FUN_00002b44();
  FUN_00003120(&DAT_200064d4);
  iVar2 = FUN_00001e50();
  if (iVar2 == 0) {
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
    }
  }
  DAT_200064bc = (char)_DAT_200040f8;
LAB_00009a54:
/* ... truncated ... */
```

#### `FUN_00009e1c` @ `00009e1c`

Site `00009e62`:

```asm
00009e4a: movw r4,#0x6465
00009e4e: movt r4,#0x2000
00009e52: ldrb r3,[r4,#0x0]
00009e54: cmp r3,#0x0
00009e56: beq 0x00009e52
00009e58: movw r6,#0x64d4
00009e5c: movs r3,#0x0
00009e5e: movt r6,#0x2000
00009e62: movs r2,r6
00009e64: movs r1,#0x0
00009e66: movs r0,r5
00009e68: strb r3,[r4,#0x0]
00009e6a: bl 0x00004ce8
00009e6e: cmp r0,#0x0
00009e70: beq 0x00009ef4
00009e72: movw r5,#0x64bc
00009e76: movt r5,#0x2000
```

Site `00009ef8`:

```asm
00009ee2: cmp r0,#0x0
00009ee4: beq 0x00009e32
00009ee6: mov r0,sp
00009ee8: bl 0x00002030
00009eec: bl 0x00003fb8
00009ef0: b 0x00009e32
00009ef2: b 0x00009ef2
00009ef4: bl 0x00002b44
00009ef8: movs r0,r6
00009efa: bl 0x00003120
00009efe: bl 0x00001e50
00009f02: cbnz r0,0x00009f74
00009f04: movw r1,#0x3ff
00009f08: ldrh r3,[r6,#0x0]
00009f0a: cmp r3,r1
00009f0c: bhi 0x00009f10
00009f0e: b 0x0000a010
```

Site `00009f08`:

```asm
00009ef0: b 0x00009e32
00009ef2: b 0x00009ef2
00009ef4: bl 0x00002b44
00009ef8: movs r0,r6
00009efa: bl 0x00003120
00009efe: bl 0x00001e50
00009f02: cbnz r0,0x00009f74
00009f04: movw r1,#0x3ff
00009f08: ldrh r3,[r6,#0x0]
00009f0a: cmp r3,r1
00009f0c: bhi 0x00009f10
00009f0e: b 0x0000a010
00009f10: movw r3,#0x40f8
00009f14: movt r3,#0x2000
00009f18: ldr r2,[r3,#0x4]
00009f1a: cmp r2,#0x0
00009f1c: bne 0x00009f20
```

Site `00009f78`:

```asm
00009f5a: movw r0,#0x64c0
00009f5e: movt r0,#0x2000
00009f62: bl 0x00002618
00009f66: movw r0,#0x64c0
00009f6a: movt r0,#0x2000
00009f6e: bl 0x00002288
00009f72: b 0x00009e2a
00009f74: movw r1,#0x3ff
00009f78: ldrh r2,[r6,#0x0]
00009f7a: cmp r2,r1
00009f7c: bls 0x00009fac
00009f7e: movw r3,#0x40f8
00009f82: movt r3,#0x2000
00009f86: ldr r2,[r3,#0x0]
00009f88: cbz r2,0x00009fe0
00009f8a: ldr r2,[r3,#0x0]
00009f8c: subs r2,#0x1
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009e1c(void)

{
  int iVar1;
  undefined1 auStack_20 [16];
  
  iVar1 = FUN_00003f98();
  if (iVar1 != 0) {
    FUN_00009944();
    goto LAB_00009e2a;
  }
  iVar1 = FUN_000048e8(0x2b007de3);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar1 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar1 == 0) {
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    iVar1 = FUN_00001e50();
    if (iVar1 == 0) {
      if (_DAT_200064d4 < 0x400) {
        _DAT_200064c2 = 0x3ff - _DAT_200064d4;
        if (1000 < (short)_DAT_200064c2) {
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
      }
      else if (_DAT_200040f8 == 0) {
LAB_00009fe8:
        DAT_200064bc = (char)_DAT_200040f8;
      }
      else {
        _DAT_200040f8 = _DAT_200040f8 + -1;
      }
    }
    else if (_DAT_200064d4 < 0x400) {
      _DAT_200064c0 = _DAT_200064d4;
      if (1000 < (short)_DAT_200064d4) {
        _DAT_200064c0 = 0x3ff;
      }
      DAT_200064bc = '\x01';
      _DAT_200040f8 = 4;
    }
    else {
      if (_DAT_200040f8 == 0) goto LAB_00009fe8;
      _DAT_200040f8 = _DAT_200040f8 + -1;
    }
  }
  iVar1 = FUN_000048e8(0xf240bb40);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
  if (DAT_200064bc != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x200;
  }
  if (DAT_200064bd != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x400;
  }
  iVar1 = FUN_00003fa8();
  if (iVar1 == 0) {
    DAT_20006466 = '\0';
  }
  else {
    if (DAT_20006466 == '\0') {
      _DAT_200064c0 = 0;
      _DAT_200064d8 = 0;
      _DAT_200064dc = 0;
      DAT_200064bc = DAT_20006466;
      DAT_200064bd = DAT_20006466;
      _DAT_200064c2 = _DAT_200064c0;
    }
    DAT_20006466 = '\x01';
    FUN_0000234c(_DAT_200064d8,_DAT_200064dc);
    FUN_0000240c();
    FUN_00002618(&DAT_200064c0);
    FUN_00002288(&DAT_200064c0);
  }
LAB_00009e2a:
  iVar1 = FUN_00004034();
  if ((iVar1 != 0) && (iVar1 = FUN_00004048(auStack_20,0x10), iVar1 != 0)) {
    FUN_00002030(auStack_20,iVar1);
    FUN_00003fb8();
  }
  return;
}
```

### `200064d6`

- from `00009bb0` in `FUN_00009944` @ `00009944` type=READ
- from `00009f32` in `FUN_00009e1c` @ `00009e1c` type=READ

#### `FUN_00009944` @ `00009944`

Site `00009bb0`:

```asm
00009b9a: bne 0x00009b9e
00009b9c: b 0x00009dc4
00009b9e: movw r5,#0x64bc
00009ba2: ldr r2,[r3,#0x4]
00009ba4: movt r5,#0x2000
00009ba8: subs r2,#0x1
00009baa: str r2,[r3,#0x4]
00009bac: movw r0,#0x3ff
00009bb0: ldrh r1,[r6,#0x2]
00009bb2: cmp r1,r0
00009bb4: bhi 0x00009bb8
00009bb6: b 0x00009d66
00009bb8: ldr r2,[r3,#0x0]
00009bba: cmp r2,#0x0
00009bbc: bne 0x00009bc0
00009bbe: b 0x00009d62
00009bc0: ldr r2,[r3,#0x0]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009944(void)

{
  bool bVar1;
  int iVar2;
  undefined4 *puVar3;
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
  
  iVar2 = FUN_00003fc8();
  if (iVar2 != 0) {
    iVar2 = FUN_000048e8(0x2b007de3);
    if (iVar2 != 0) {
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    do {
    } while (DAT_20006465 == '\0');
    DAT_20006465 = '\0';
    FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    FUN_0000179c();
    iVar2 = FUN_00001864();
    if ((iVar2 != 0) && (*(char *)(iVar2 + 0x68) != '\0')) {
      _DAT_2000646c = *(undefined2 *)(iVar2 + 6);
      _DAT_2000646e = *(undefined2 *)(iVar2 + 0x10);
      _DAT_20006470 = *(undefined2 *)(iVar2 + 0x1a);
      _DAT_20006472 = *(undefined2 *)(iVar2 + 0x24);
      _DAT_20006474 = *(undefined2 *)(iVar2 + 0x2e);
      _DAT_20006476 = *(undefined2 *)(iVar2 + 0x38);
      _DAT_20006478 = *(undefined2 *)(iVar2 + 0x42);
      _DAT_2000647a = *(undefined2 *)(iVar2 + 0x4c);
      _DAT_2000647c = *(undefined2 *)(iVar2 + 0x56);
      _DAT_2000647e = *(undefined2 *)(iVar2 + 0x60);
      _DAT_20006468 = *(undefined4 *)(iVar2 + 100);
    }
    iVar2 = FUN_000048e8(0xf240bb40);
    if (iVar2 == 0) {
      do {
      } while (DAT_20006465 == '\0');
      DAT_20006465 = 0;
      FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
      iVar2 = FUN_0000408c(0,0x200064a8,&DAT_20006494,0x20006480,auStack_98,0x80);
      if (iVar2 != 0) {
        FUN_00002030(auStack_98,iVar2);
      }
      iVar2 = FUN_00001e50();
      if (iVar2 != 0) {
        return;
      }
      FUN_00009448(1,4000);
      iVar2 = FUN_0000408c(1,DAT_00009e0c,DAT_00009e14,DAT_00009e10,auStack_98,0x80);
      if (iVar2 == 0) {
        return;
      }
      FUN_00002030(auStack_98,iVar2);
      return;
    }
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar2 = FUN_000048e8(0x2b007de3);
  if (iVar2 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar2 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar2 != 0) goto LAB_00009a54;
  FUN_00002b44();
  FUN_00003120(&DAT_200064d4);
  iVar2 = FUN_00001e50();
  if (iVar2 == 0) {
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
    }
  }
  DAT_200064bc = (char)_DAT_200040f8;
LAB_00009a54:
/* ... truncated ... */
```

#### `FUN_00009e1c` @ `00009e1c`

Site `00009f32`:

```asm
00009f1c: bne 0x00009f20
00009f1e: b 0x0000a04a
00009f20: movw r5,#0x64bc
00009f24: ldr r2,[r3,#0x4]
00009f26: movt r5,#0x2000
00009f2a: subs r2,#0x1
00009f2c: str r2,[r3,#0x4]
00009f2e: movw r0,#0x3ff
00009f32: ldrh r1,[r6,#0x2]
00009f34: cmp r1,r0
00009f36: bls 0x00009fec
00009f38: ldr r2,[r3,#0x0]
00009f3a: cmp r2,#0x0
00009f3c: beq 0x00009fe8
00009f3e: ldr r2,[r3,#0x0]
00009f40: subs r2,#0x1
00009f42: str r2,[r3,#0x0]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009e1c(void)

{
  int iVar1;
  undefined1 auStack_20 [16];
  
  iVar1 = FUN_00003f98();
  if (iVar1 != 0) {
    FUN_00009944();
    goto LAB_00009e2a;
  }
  iVar1 = FUN_000048e8(0x2b007de3);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar1 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar1 == 0) {
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    iVar1 = FUN_00001e50();
    if (iVar1 == 0) {
      if (_DAT_200064d4 < 0x400) {
        _DAT_200064c2 = 0x3ff - _DAT_200064d4;
        if (1000 < (short)_DAT_200064c2) {
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
      }
      else if (_DAT_200040f8 == 0) {
LAB_00009fe8:
        DAT_200064bc = (char)_DAT_200040f8;
      }
      else {
        _DAT_200040f8 = _DAT_200040f8 + -1;
      }
    }
    else if (_DAT_200064d4 < 0x400) {
      _DAT_200064c0 = _DAT_200064d4;
      if (1000 < (short)_DAT_200064d4) {
        _DAT_200064c0 = 0x3ff;
      }
      DAT_200064bc = '\x01';
      _DAT_200040f8 = 4;
    }
    else {
      if (_DAT_200040f8 == 0) goto LAB_00009fe8;
      _DAT_200040f8 = _DAT_200040f8 + -1;
    }
  }
  iVar1 = FUN_000048e8(0xf240bb40);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
  if (DAT_200064bc != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x200;
  }
  if (DAT_200064bd != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x400;
  }
  iVar1 = FUN_00003fa8();
  if (iVar1 == 0) {
    DAT_20006466 = '\0';
  }
  else {
    if (DAT_20006466 == '\0') {
      _DAT_200064c0 = 0;
      _DAT_200064d8 = 0;
      _DAT_200064dc = 0;
      DAT_200064bc = DAT_20006466;
      DAT_200064bd = DAT_20006466;
      _DAT_200064c2 = _DAT_200064c0;
    }
    DAT_20006466 = '\x01';
    FUN_0000234c(_DAT_200064d8,_DAT_200064dc);
    FUN_0000240c();
    FUN_00002618(&DAT_200064c0);
    FUN_00002288(&DAT_200064c0);
  }
LAB_00009e2a:
  iVar1 = FUN_00004034();
  if ((iVar1 != 0) && (iVar1 = FUN_00004048(auStack_20,0x10), iVar1 != 0)) {
    FUN_00002030(auStack_20,iVar1);
    FUN_00003fb8();
  }
  return;
}
```

### `200064d8`

- from `00009a88` in `FUN_00009944` @ `00009944` type=READ
- from `00009bd0` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009a9c` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009ea0` in `FUN_00009e1c` @ `00009e1c` type=PARAM
- from `00009eb0` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009eb4` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `00009ebe` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009ec2` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `00009f4a` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009fa6` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `00009b04` in `FUN_00009944` @ `00009944` type=PARAM
- from `00009a7e` in `FUN_00009944` @ `00009944` type=PARAM

#### `FUN_00009944` @ `00009944`

Site `00009a88`:

```asm
00009a72: strb r3,[r4,#0x0]
00009a74: movw r4,#0x64d8
00009a78: movt r4,#0x2000
00009a7c: movs r2,#0x0
00009a7e: movs r1,r4
00009a80: movs r0,r6
00009a82: bl 0x00004ce8
00009a86: ldrb r3,[r5,#0x0]
00009a88: ldr r0,[r4,#0x0]
00009a8a: cmp r3,#0x0
00009a8c: beq 0x00009a90
00009a8e: b 0x00009bc8
00009a90: ldr r1,[r4,#0x4]
00009a92: ldrb r3,[r5,#0x1]
00009a94: cbz r3,0x00009a9e
00009a96: movw r3,#0x400
00009a9a: orrs r0,r3
```

Site `00009bd0`:

```asm
00009bbe: b 0x00009d62
00009bc0: ldr r2,[r3,#0x0]
00009bc2: subs r2,#0x1
00009bc4: str r2,[r3,#0x0]
00009bc6: b 0x00009a54
00009bc8: movw r3,#0x200
00009bcc: orrs r0,r3
00009bce: ldr r1,[r4,#0x4]
00009bd0: str r0,[r4,#0x0]
00009bd2: b 0x00009a92
00009bd4: movw r1,#0x3ff
00009bd8: ldrh r2,[r6,#0x0]
00009bda: cmp r2,r1
00009bdc: bhi 0x00009be0
00009bde: b 0x00009d26
00009be0: movw r3,#0x40f8
00009be4: movt r3,#0x2000
```

Site `00009a9c`:

```asm
00009a8a: cmp r3,#0x0
00009a8c: beq 0x00009a90
00009a8e: b 0x00009bc8
00009a90: ldr r1,[r4,#0x4]
00009a92: ldrb r3,[r5,#0x1]
00009a94: cbz r3,0x00009a9e
00009a96: movw r3,#0x400
00009a9a: orrs r0,r3
00009a9c: stmia r4!,{r0,r1}
00009a9e: bl 0x0000234c
00009aa2: bl 0x0000240c
00009aa6: movw r0,#0x64c0
00009aaa: movt r0,#0x2000
00009aae: bl 0x00002618
00009ab2: movw r0,#0x64c0
00009ab6: movt r0,#0x2000
00009aba: bl 0x00002288
```

Site `00009b04`:

```asm
00009af2: pop {r4,r5,r6,r7,pc}
00009af4: b 0x00009af4
00009af6: ldrb r3,[r4,#0x0]
00009af8: cmp r3,#0x0
00009afa: beq 0x00009af6
00009afc: movw r1,#0x64d8
00009b00: movs r3,#0x0
00009b02: movs r2,#0x0
00009b04: movt r1,#0x2000
00009b08: movs r0,r5
00009b0a: strb r3,[r4,#0x0]
00009b0c: bl 0x00004ce8
00009b10: movs r3,#0x80
00009b12: str r3,[sp,#0x4]
00009b14: add r3,sp,#0x50
00009b16: movw r2,#0x6494
00009b1a: movw r1,#0x64a8
```

Site `00009a7e`:

```asm
00009a6a: ldrb r3,[r4,#0x0]
00009a6c: cmp r3,#0x0
00009a6e: beq 0x00009a6a
00009a70: movs r3,#0x0
00009a72: strb r3,[r4,#0x0]
00009a74: movw r4,#0x64d8
00009a78: movt r4,#0x2000
00009a7c: movs r2,#0x0
00009a7e: movs r1,r4
00009a80: movs r0,r6
00009a82: bl 0x00004ce8
00009a86: ldrb r3,[r5,#0x0]
00009a88: ldr r0,[r4,#0x0]
00009a8a: cmp r3,#0x0
00009a8c: beq 0x00009a90
00009a8e: b 0x00009bc8
00009a90: ldr r1,[r4,#0x4]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009944(void)

{
  bool bVar1;
  int iVar2;
  undefined4 *puVar3;
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
  
  iVar2 = FUN_00003fc8();
  if (iVar2 != 0) {
    iVar2 = FUN_000048e8(0x2b007de3);
    if (iVar2 != 0) {
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    do {
    } while (DAT_20006465 == '\0');
    DAT_20006465 = '\0';
    FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    FUN_0000179c();
    iVar2 = FUN_00001864();
    if ((iVar2 != 0) && (*(char *)(iVar2 + 0x68) != '\0')) {
      _DAT_2000646c = *(undefined2 *)(iVar2 + 6);
      _DAT_2000646e = *(undefined2 *)(iVar2 + 0x10);
      _DAT_20006470 = *(undefined2 *)(iVar2 + 0x1a);
      _DAT_20006472 = *(undefined2 *)(iVar2 + 0x24);
      _DAT_20006474 = *(undefined2 *)(iVar2 + 0x2e);
      _DAT_20006476 = *(undefined2 *)(iVar2 + 0x38);
      _DAT_20006478 = *(undefined2 *)(iVar2 + 0x42);
      _DAT_2000647a = *(undefined2 *)(iVar2 + 0x4c);
      _DAT_2000647c = *(undefined2 *)(iVar2 + 0x56);
      _DAT_2000647e = *(undefined2 *)(iVar2 + 0x60);
      _DAT_20006468 = *(undefined4 *)(iVar2 + 100);
    }
    iVar2 = FUN_000048e8(0xf240bb40);
    if (iVar2 == 0) {
      do {
      } while (DAT_20006465 == '\0');
      DAT_20006465 = 0;
      FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
      iVar2 = FUN_0000408c(0,0x200064a8,&DAT_20006494,0x20006480,auStack_98,0x80);
      if (iVar2 != 0) {
        FUN_00002030(auStack_98,iVar2);
      }
      iVar2 = FUN_00001e50();
      if (iVar2 != 0) {
        return;
      }
      FUN_00009448(1,4000);
      iVar2 = FUN_0000408c(1,DAT_00009e0c,DAT_00009e14,DAT_00009e10,auStack_98,0x80);
      if (iVar2 == 0) {
        return;
      }
      FUN_00002030(auStack_98,iVar2);
      return;
    }
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar2 = FUN_000048e8(0x2b007de3);
  if (iVar2 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar2 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar2 != 0) goto LAB_00009a54;
  FUN_00002b44();
  FUN_00003120(&DAT_200064d4);
  iVar2 = FUN_00001e50();
  if (iVar2 == 0) {
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
    }
  }
  DAT_200064bc = (char)_DAT_200040f8;
LAB_00009a54:
/* ... truncated ... */
```

#### `FUN_00009e1c` @ `00009e1c`

Site `00009ea0`:

```asm
00009e8c: ldrb r3,[r4,#0x0]
00009e8e: cmp r3,#0x0
00009e90: beq 0x00009e8c
00009e92: movs r3,#0x0
00009e94: strb r3,[r4,#0x0]
00009e96: movw r4,#0x64d8
00009e9a: movt r4,#0x2000
00009e9e: movs r2,#0x0
00009ea0: movs r1,r4
00009ea2: movs r0,r6
00009ea4: bl 0x00004ce8
00009ea8: ldrb r3,[r5,#0x0]
00009eaa: cbz r3,0x00009eb6
00009eac: movw r2,#0x200
00009eb0: ldr r3,[r4,#0x0]
00009eb2: orrs r3,r2
00009eb4: str r3,[r4,#0x0]
```

Site `00009eb0`:

```asm
00009e9a: movt r4,#0x2000
00009e9e: movs r2,#0x0
00009ea0: movs r1,r4
00009ea2: movs r0,r6
00009ea4: bl 0x00004ce8
00009ea8: ldrb r3,[r5,#0x0]
00009eaa: cbz r3,0x00009eb6
00009eac: movw r2,#0x200
00009eb0: ldr r3,[r4,#0x0]
00009eb2: orrs r3,r2
00009eb4: str r3,[r4,#0x0]
00009eb6: ldrb r3,[r5,#0x1]
00009eb8: cbz r3,0x00009ec4
00009eba: movw r2,#0x400
00009ebe: ldr r3,[r4,#0x0]
00009ec0: orrs r3,r2
00009ec2: str r3,[r4,#0x0]
```

Site `00009eb4`:

```asm
00009ea0: movs r1,r4
00009ea2: movs r0,r6
00009ea4: bl 0x00004ce8
00009ea8: ldrb r3,[r5,#0x0]
00009eaa: cbz r3,0x00009eb6
00009eac: movw r2,#0x200
00009eb0: ldr r3,[r4,#0x0]
00009eb2: orrs r3,r2
00009eb4: str r3,[r4,#0x0]
00009eb6: ldrb r3,[r5,#0x1]
00009eb8: cbz r3,0x00009ec4
00009eba: movw r2,#0x400
00009ebe: ldr r3,[r4,#0x0]
00009ec0: orrs r3,r2
00009ec2: str r3,[r4,#0x0]
00009ec4: bl 0x00003fa8
00009ec8: movw r3,#0x6466
```

Site `00009ebe`:

```asm
00009eaa: cbz r3,0x00009eb6
00009eac: movw r2,#0x200
00009eb0: ldr r3,[r4,#0x0]
00009eb2: orrs r3,r2
00009eb4: str r3,[r4,#0x0]
00009eb6: ldrb r3,[r5,#0x1]
00009eb8: cbz r3,0x00009ec4
00009eba: movw r2,#0x400
00009ebe: ldr r3,[r4,#0x0]
00009ec0: orrs r3,r2
00009ec2: str r3,[r4,#0x0]
00009ec4: bl 0x00003fa8
00009ec8: movw r3,#0x6466
00009ecc: movt r3,#0x2000
00009ed0: cbnz r0,0x00009f46
00009ed2: strb r0,[r3,#0x0]
00009ed4: b 0x00009e2a
```

Site `00009ec2`:

```asm
00009eb0: ldr r3,[r4,#0x0]
00009eb2: orrs r3,r2
00009eb4: str r3,[r4,#0x0]
00009eb6: ldrb r3,[r5,#0x1]
00009eb8: cbz r3,0x00009ec4
00009eba: movw r2,#0x400
00009ebe: ldr r3,[r4,#0x0]
00009ec0: orrs r3,r2
00009ec2: str r3,[r4,#0x0]
00009ec4: bl 0x00003fa8
00009ec8: movw r3,#0x6466
00009ecc: movt r3,#0x2000
00009ed0: cbnz r0,0x00009f46
00009ed2: strb r0,[r3,#0x0]
00009ed4: b 0x00009e2a
00009ed6: b 0x00009ed6
00009ed8: movs r1,#0x10
```

Site `00009f4a`:

```asm
00009f3a: cmp r2,#0x0
00009f3c: beq 0x00009fe8
00009f3e: ldr r2,[r3,#0x0]
00009f40: subs r2,#0x1
00009f42: str r2,[r3,#0x0]
00009f44: b 0x00009e7a
00009f46: ldrb r2,[r3,#0x0]
00009f48: cbz r2,0x00009f92
00009f4a: ldr r0,[r4,#0x0]
00009f4c: ldr r1,[r4,#0x4]
00009f4e: movs r2,#0x1
00009f50: strb r2,[r3,#0x0]
00009f52: bl 0x0000234c
00009f56: bl 0x0000240c
00009f5a: movw r0,#0x64c0
00009f5e: movt r0,#0x2000
00009f62: bl 0x00002618
```

Site `00009fa6`:

```asm
00009f92: movw r1,#0x64c0
00009f96: movt r1,#0x2000
00009f9a: strb r2,[r5,#0x0]
00009f9c: movs r0,#0x0
00009f9e: strb r2,[r5,#0x1]
00009fa0: strh r2,[r1,#0x0]
00009fa2: strh r2,[r1,#0x2]
00009fa4: movs r1,#0x0
00009fa6: str r0,[r4,#0x0]
00009fa8: str r1,[r4,#0x4]
00009faa: b 0x00009f4e
00009fac: movw r3,#0x64c0
00009fb0: movw r0,#0x3e8
00009fb4: sxth r2,r2
00009fb6: movt r3,#0x2000
00009fba: strh r2,[r3,#0x0]
00009fbc: ldrh r2,[r3,#0x0]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009e1c(void)

{
  int iVar1;
  undefined1 auStack_20 [16];
  
  iVar1 = FUN_00003f98();
  if (iVar1 != 0) {
    FUN_00009944();
    goto LAB_00009e2a;
  }
  iVar1 = FUN_000048e8(0x2b007de3);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar1 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar1 == 0) {
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    iVar1 = FUN_00001e50();
    if (iVar1 == 0) {
      if (_DAT_200064d4 < 0x400) {
        _DAT_200064c2 = 0x3ff - _DAT_200064d4;
        if (1000 < (short)_DAT_200064c2) {
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
      }
      else if (_DAT_200040f8 == 0) {
LAB_00009fe8:
        DAT_200064bc = (char)_DAT_200040f8;
      }
      else {
        _DAT_200040f8 = _DAT_200040f8 + -1;
      }
    }
    else if (_DAT_200064d4 < 0x400) {
      _DAT_200064c0 = _DAT_200064d4;
      if (1000 < (short)_DAT_200064d4) {
        _DAT_200064c0 = 0x3ff;
      }
      DAT_200064bc = '\x01';
      _DAT_200040f8 = 4;
    }
    else {
      if (_DAT_200040f8 == 0) goto LAB_00009fe8;
      _DAT_200040f8 = _DAT_200040f8 + -1;
    }
  }
  iVar1 = FUN_000048e8(0xf240bb40);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
  if (DAT_200064bc != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x200;
  }
  if (DAT_200064bd != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x400;
  }
  iVar1 = FUN_00003fa8();
  if (iVar1 == 0) {
    DAT_20006466 = '\0';
  }
  else {
    if (DAT_20006466 == '\0') {
      _DAT_200064c0 = 0;
      _DAT_200064d8 = 0;
      _DAT_200064dc = 0;
      DAT_200064bc = DAT_20006466;
      DAT_200064bd = DAT_20006466;
      _DAT_200064c2 = _DAT_200064c0;
    }
    DAT_20006466 = '\x01';
    FUN_0000234c(_DAT_200064d8,_DAT_200064dc);
    FUN_0000240c();
    FUN_00002618(&DAT_200064c0);
    FUN_00002288(&DAT_200064c0);
  }
LAB_00009e2a:
  iVar1 = FUN_00004034();
  if ((iVar1 != 0) && (iVar1 = FUN_00004048(auStack_20,0x10), iVar1 != 0)) {
    FUN_00002030(auStack_20,iVar1);
    FUN_00003fb8();
  }
  return;
}
```

### `200064dc`

- from `00009bce` in `FUN_00009944` @ `00009944` type=READ
- from `00009a9c` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009a90` in `FUN_00009944` @ `00009944` type=READ
- from `00009f4c` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009fa8` in `FUN_00009e1c` @ `00009e1c` type=WRITE

#### `FUN_00009944` @ `00009944`

Site `00009bce`:

```asm
00009bbc: bne 0x00009bc0
00009bbe: b 0x00009d62
00009bc0: ldr r2,[r3,#0x0]
00009bc2: subs r2,#0x1
00009bc4: str r2,[r3,#0x0]
00009bc6: b 0x00009a54
00009bc8: movw r3,#0x200
00009bcc: orrs r0,r3
00009bce: ldr r1,[r4,#0x4]
00009bd0: str r0,[r4,#0x0]
00009bd2: b 0x00009a92
00009bd4: movw r1,#0x3ff
00009bd8: ldrh r2,[r6,#0x0]
00009bda: cmp r2,r1
00009bdc: bhi 0x00009be0
00009bde: b 0x00009d26
00009be0: movw r3,#0x40f8
```

Site `00009a9c`:

```asm
00009a8a: cmp r3,#0x0
00009a8c: beq 0x00009a90
00009a8e: b 0x00009bc8
00009a90: ldr r1,[r4,#0x4]
00009a92: ldrb r3,[r5,#0x1]
00009a94: cbz r3,0x00009a9e
00009a96: movw r3,#0x400
00009a9a: orrs r0,r3
00009a9c: stmia r4!,{r0,r1}
00009a9e: bl 0x0000234c
00009aa2: bl 0x0000240c
00009aa6: movw r0,#0x64c0
00009aaa: movt r0,#0x2000
00009aae: bl 0x00002618
00009ab2: movw r0,#0x64c0
00009ab6: movt r0,#0x2000
00009aba: bl 0x00002288
```

Site `00009a90`:

```asm
00009a7e: movs r1,r4
00009a80: movs r0,r6
00009a82: bl 0x00004ce8
00009a86: ldrb r3,[r5,#0x0]
00009a88: ldr r0,[r4,#0x0]
00009a8a: cmp r3,#0x0
00009a8c: beq 0x00009a90
00009a8e: b 0x00009bc8
00009a90: ldr r1,[r4,#0x4]
00009a92: ldrb r3,[r5,#0x1]
00009a94: cbz r3,0x00009a9e
00009a96: movw r3,#0x400
00009a9a: orrs r0,r3
00009a9c: stmia r4!,{r0,r1}
00009a9e: bl 0x0000234c
00009aa2: bl 0x0000240c
00009aa6: movw r0,#0x64c0
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009944(void)

{
  bool bVar1;
  int iVar2;
  undefined4 *puVar3;
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
  
  iVar2 = FUN_00003fc8();
  if (iVar2 != 0) {
    iVar2 = FUN_000048e8(0x2b007de3);
    if (iVar2 != 0) {
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    do {
    } while (DAT_20006465 == '\0');
    DAT_20006465 = '\0';
    FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    FUN_0000179c();
    iVar2 = FUN_00001864();
    if ((iVar2 != 0) && (*(char *)(iVar2 + 0x68) != '\0')) {
      _DAT_2000646c = *(undefined2 *)(iVar2 + 6);
      _DAT_2000646e = *(undefined2 *)(iVar2 + 0x10);
      _DAT_20006470 = *(undefined2 *)(iVar2 + 0x1a);
      _DAT_20006472 = *(undefined2 *)(iVar2 + 0x24);
      _DAT_20006474 = *(undefined2 *)(iVar2 + 0x2e);
      _DAT_20006476 = *(undefined2 *)(iVar2 + 0x38);
      _DAT_20006478 = *(undefined2 *)(iVar2 + 0x42);
      _DAT_2000647a = *(undefined2 *)(iVar2 + 0x4c);
      _DAT_2000647c = *(undefined2 *)(iVar2 + 0x56);
      _DAT_2000647e = *(undefined2 *)(iVar2 + 0x60);
      _DAT_20006468 = *(undefined4 *)(iVar2 + 100);
    }
    iVar2 = FUN_000048e8(0xf240bb40);
    if (iVar2 == 0) {
      do {
      } while (DAT_20006465 == '\0');
      DAT_20006465 = 0;
      FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
      iVar2 = FUN_0000408c(0,0x200064a8,&DAT_20006494,0x20006480,auStack_98,0x80);
      if (iVar2 != 0) {
        FUN_00002030(auStack_98,iVar2);
      }
      iVar2 = FUN_00001e50();
      if (iVar2 != 0) {
        return;
      }
      FUN_00009448(1,4000);
      iVar2 = FUN_0000408c(1,DAT_00009e0c,DAT_00009e14,DAT_00009e10,auStack_98,0x80);
      if (iVar2 == 0) {
        return;
      }
      FUN_00002030(auStack_98,iVar2);
      return;
    }
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar2 = FUN_000048e8(0x2b007de3);
  if (iVar2 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar2 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar2 != 0) goto LAB_00009a54;
  FUN_00002b44();
  FUN_00003120(&DAT_200064d4);
  iVar2 = FUN_00001e50();
  if (iVar2 == 0) {
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
    }
  }
  DAT_200064bc = (char)_DAT_200040f8;
LAB_00009a54:
/* ... truncated ... */
```

#### `FUN_00009e1c` @ `00009e1c`

Site `00009f4c`:

```asm
00009f3c: beq 0x00009fe8
00009f3e: ldr r2,[r3,#0x0]
00009f40: subs r2,#0x1
00009f42: str r2,[r3,#0x0]
00009f44: b 0x00009e7a
00009f46: ldrb r2,[r3,#0x0]
00009f48: cbz r2,0x00009f92
00009f4a: ldr r0,[r4,#0x0]
00009f4c: ldr r1,[r4,#0x4]
00009f4e: movs r2,#0x1
00009f50: strb r2,[r3,#0x0]
00009f52: bl 0x0000234c
00009f56: bl 0x0000240c
00009f5a: movw r0,#0x64c0
00009f5e: movt r0,#0x2000
00009f62: bl 0x00002618
00009f66: movw r0,#0x64c0
```

Site `00009fa8`:

```asm
00009f96: movt r1,#0x2000
00009f9a: strb r2,[r5,#0x0]
00009f9c: movs r0,#0x0
00009f9e: strb r2,[r5,#0x1]
00009fa0: strh r2,[r1,#0x0]
00009fa2: strh r2,[r1,#0x2]
00009fa4: movs r1,#0x0
00009fa6: str r0,[r4,#0x0]
00009fa8: str r1,[r4,#0x4]
00009faa: b 0x00009f4e
00009fac: movw r3,#0x64c0
00009fb0: movw r0,#0x3e8
00009fb4: sxth r2,r2
00009fb6: movt r3,#0x2000
00009fba: strh r2,[r3,#0x0]
00009fbc: ldrh r2,[r3,#0x0]
00009fbe: sxth r2,r2
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009e1c(void)

{
  int iVar1;
  undefined1 auStack_20 [16];
  
  iVar1 = FUN_00003f98();
  if (iVar1 != 0) {
    FUN_00009944();
    goto LAB_00009e2a;
  }
  iVar1 = FUN_000048e8(0x2b007de3);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar1 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar1 == 0) {
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    iVar1 = FUN_00001e50();
    if (iVar1 == 0) {
      if (_DAT_200064d4 < 0x400) {
        _DAT_200064c2 = 0x3ff - _DAT_200064d4;
        if (1000 < (short)_DAT_200064c2) {
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
      }
      else if (_DAT_200040f8 == 0) {
LAB_00009fe8:
        DAT_200064bc = (char)_DAT_200040f8;
      }
      else {
        _DAT_200040f8 = _DAT_200040f8 + -1;
      }
    }
    else if (_DAT_200064d4 < 0x400) {
      _DAT_200064c0 = _DAT_200064d4;
      if (1000 < (short)_DAT_200064d4) {
        _DAT_200064c0 = 0x3ff;
      }
      DAT_200064bc = '\x01';
      _DAT_200040f8 = 4;
    }
    else {
      if (_DAT_200040f8 == 0) goto LAB_00009fe8;
      _DAT_200040f8 = _DAT_200040f8 + -1;
    }
  }
  iVar1 = FUN_000048e8(0xf240bb40);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
  if (DAT_200064bc != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x200;
  }
  if (DAT_200064bd != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x400;
  }
  iVar1 = FUN_00003fa8();
  if (iVar1 == 0) {
    DAT_20006466 = '\0';
  }
  else {
    if (DAT_20006466 == '\0') {
      _DAT_200064c0 = 0;
      _DAT_200064d8 = 0;
      _DAT_200064dc = 0;
      DAT_200064bc = DAT_20006466;
      DAT_200064bd = DAT_20006466;
      _DAT_200064c2 = _DAT_200064c0;
    }
    DAT_20006466 = '\x01';
    FUN_0000234c(_DAT_200064d8,_DAT_200064dc);
    FUN_0000240c();
    FUN_00002618(&DAT_200064c0);
    FUN_00002288(&DAT_200064c0);
  }
LAB_00009e2a:
  iVar1 = FUN_00004034();
  if ((iVar1 != 0) && (iVar1 = FUN_00004048(auStack_20,0x10), iVar1 != 0)) {
    FUN_00002030(auStack_20,iVar1);
    FUN_00003fb8();
  }
  return;
}
```

### `200040f8`

- from `00009d86` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009bb8` in `FUN_00009944` @ `00009944` type=READ
- from `00009bc0` in `FUN_00009944` @ `00009944` type=READ
- from `00009bc4` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009d56` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009be8` in `FUN_00009944` @ `00009944` type=READ
- from `00009bf0` in `FUN_00009944` @ `00009944` type=READ
- from `00009bf4` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009f38` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009f3e` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009f42` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `0000a00c` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `00009f86` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009f8a` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009f8e` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `00009fdc` in `FUN_00009e1c` @ `00009e1c` type=WRITE

#### `FUN_00009944` @ `00009944`

Site `00009d86`:

```asm
00009d76: ldrh r1,[r2,#0x0]
00009d78: sxth r1,r1
00009d7a: cmp r1,r6
00009d7c: ble 0x00009d80
00009d7e: strh r0,[r2,#0x0]
00009d80: movs r2,#0x1
00009d82: strb r2,[r5,#0x0]
00009d84: adds r2,#0x3
00009d86: str r2,[r3,#0x0]
00009d88: b 0x00009a54
00009d8a: movw r2,#0x3ff
00009d8e: subs r2,r2,r3
00009d90: movw r3,#0x64c0
00009d94: movw r0,#0x3e8
00009d98: sxth r2,r2
00009d9a: movt r3,#0x2000
00009d9e: strh r2,[r3,#0x2]
```

Site `00009bb8`:

```asm
00009ba4: movt r5,#0x2000
00009ba8: subs r2,#0x1
00009baa: str r2,[r3,#0x4]
00009bac: movw r0,#0x3ff
00009bb0: ldrh r1,[r6,#0x2]
00009bb2: cmp r1,r0
00009bb4: bhi 0x00009bb8
00009bb6: b 0x00009d66
00009bb8: ldr r2,[r3,#0x0]
00009bba: cmp r2,#0x0
00009bbc: bne 0x00009bc0
00009bbe: b 0x00009d62
00009bc0: ldr r2,[r3,#0x0]
00009bc2: subs r2,#0x1
00009bc4: str r2,[r3,#0x0]
00009bc6: b 0x00009a54
00009bc8: movw r3,#0x200
```

Site `00009bc0`:

```asm
00009bb0: ldrh r1,[r6,#0x2]
00009bb2: cmp r1,r0
00009bb4: bhi 0x00009bb8
00009bb6: b 0x00009d66
00009bb8: ldr r2,[r3,#0x0]
00009bba: cmp r2,#0x0
00009bbc: bne 0x00009bc0
00009bbe: b 0x00009d62
00009bc0: ldr r2,[r3,#0x0]
00009bc2: subs r2,#0x1
00009bc4: str r2,[r3,#0x0]
00009bc6: b 0x00009a54
00009bc8: movw r3,#0x200
00009bcc: orrs r0,r3
00009bce: ldr r1,[r4,#0x4]
00009bd0: str r0,[r4,#0x0]
00009bd2: b 0x00009a92
```

Site `00009bc4`:

```asm
00009bb4: bhi 0x00009bb8
00009bb6: b 0x00009d66
00009bb8: ldr r2,[r3,#0x0]
00009bba: cmp r2,#0x0
00009bbc: bne 0x00009bc0
00009bbe: b 0x00009d62
00009bc0: ldr r2,[r3,#0x0]
00009bc2: subs r2,#0x1
00009bc4: str r2,[r3,#0x0]
00009bc6: b 0x00009a54
00009bc8: movw r3,#0x200
00009bcc: orrs r0,r3
00009bce: ldr r1,[r4,#0x4]
00009bd0: str r0,[r4,#0x0]
00009bd2: b 0x00009a92
00009bd4: movw r1,#0x3ff
00009bd8: ldrh r2,[r6,#0x0]
```

Site `00009d56`:

```asm
00009d3e: strh r1,[r3,#0x0]
00009d40: movw r5,#0x64bc
00009d44: movs r3,#0x1
00009d46: movt r5,#0x2000
00009d4a: strb r3,[r5,#0x0]
00009d4c: movw r3,#0x40f8
00009d50: movs r2,#0x4
00009d52: movt r3,#0x2000
00009d56: str r2,[r3,#0x0]
00009d58: b 0x00009a54
00009d5a: movw r5,#0x64bc
00009d5e: movt r5,#0x2000
00009d62: strb r2,[r5,#0x0]
00009d64: b 0x00009a54
00009d66: movw r2,#0x64c0
00009d6a: movw r6,#0x3e8
00009d6e: sxth r1,r1
```

Site `00009be8`:

```asm
00009bd2: b 0x00009a92
00009bd4: movw r1,#0x3ff
00009bd8: ldrh r2,[r6,#0x0]
00009bda: cmp r2,r1
00009bdc: bhi 0x00009be0
00009bde: b 0x00009d26
00009be0: movw r3,#0x40f8
00009be4: movt r3,#0x2000
00009be8: ldr r2,[r3,#0x0]
00009bea: cmp r2,#0x0
00009bec: bne 0x00009bf0
00009bee: b 0x00009d5a
00009bf0: ldr r2,[r3,#0x0]
00009bf2: subs r2,#0x1
00009bf4: str r2,[r3,#0x0]
00009bf6: b 0x00009a4c
00009bf8: add r0,sp,#0x38
```

Site `00009bf0`:

```asm
00009bdc: bhi 0x00009be0
00009bde: b 0x00009d26
00009be0: movw r3,#0x40f8
00009be4: movt r3,#0x2000
00009be8: ldr r2,[r3,#0x0]
00009bea: cmp r2,#0x0
00009bec: bne 0x00009bf0
00009bee: b 0x00009d5a
00009bf0: ldr r2,[r3,#0x0]
00009bf2: subs r2,#0x1
00009bf4: str r2,[r3,#0x0]
00009bf6: b 0x00009a4c
00009bf8: add r0,sp,#0x38
00009bfa: bl 0x00001cfc
00009bfe: cmp r0,#0x0
00009c00: beq 0x00009c04
00009c02: b 0x00009ae6
```

Site `00009bf4`:

```asm
00009be0: movw r3,#0x40f8
00009be4: movt r3,#0x2000
00009be8: ldr r2,[r3,#0x0]
00009bea: cmp r2,#0x0
00009bec: bne 0x00009bf0
00009bee: b 0x00009d5a
00009bf0: ldr r2,[r3,#0x0]
00009bf2: subs r2,#0x1
00009bf4: str r2,[r3,#0x0]
00009bf6: b 0x00009a4c
00009bf8: add r0,sp,#0x38
00009bfa: bl 0x00001cfc
00009bfe: cmp r0,#0x0
00009c00: beq 0x00009c04
00009c02: b 0x00009ae6
00009c04: add r1,sp,#0x50
00009c06: movs r2,#0x80
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009944(void)

{
  bool bVar1;
  int iVar2;
  undefined4 *puVar3;
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
  
  iVar2 = FUN_00003fc8();
  if (iVar2 != 0) {
    iVar2 = FUN_000048e8(0x2b007de3);
    if (iVar2 != 0) {
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    do {
    } while (DAT_20006465 == '\0');
    DAT_20006465 = '\0';
    FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    FUN_0000179c();
    iVar2 = FUN_00001864();
    if ((iVar2 != 0) && (*(char *)(iVar2 + 0x68) != '\0')) {
      _DAT_2000646c = *(undefined2 *)(iVar2 + 6);
      _DAT_2000646e = *(undefined2 *)(iVar2 + 0x10);
      _DAT_20006470 = *(undefined2 *)(iVar2 + 0x1a);
      _DAT_20006472 = *(undefined2 *)(iVar2 + 0x24);
      _DAT_20006474 = *(undefined2 *)(iVar2 + 0x2e);
      _DAT_20006476 = *(undefined2 *)(iVar2 + 0x38);
      _DAT_20006478 = *(undefined2 *)(iVar2 + 0x42);
      _DAT_2000647a = *(undefined2 *)(iVar2 + 0x4c);
      _DAT_2000647c = *(undefined2 *)(iVar2 + 0x56);
      _DAT_2000647e = *(undefined2 *)(iVar2 + 0x60);
      _DAT_20006468 = *(undefined4 *)(iVar2 + 100);
    }
    iVar2 = FUN_000048e8(0xf240bb40);
    if (iVar2 == 0) {
      do {
      } while (DAT_20006465 == '\0');
      DAT_20006465 = 0;
      FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
      iVar2 = FUN_0000408c(0,0x200064a8,&DAT_20006494,0x20006480,auStack_98,0x80);
      if (iVar2 != 0) {
        FUN_00002030(auStack_98,iVar2);
      }
      iVar2 = FUN_00001e50();
      if (iVar2 != 0) {
        return;
      }
      FUN_00009448(1,4000);
      iVar2 = FUN_0000408c(1,DAT_00009e0c,DAT_00009e14,DAT_00009e10,auStack_98,0x80);
      if (iVar2 == 0) {
        return;
      }
      FUN_00002030(auStack_98,iVar2);
      return;
    }
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar2 = FUN_000048e8(0x2b007de3);
  if (iVar2 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar2 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar2 != 0) goto LAB_00009a54;
  FUN_00002b44();
  FUN_00003120(&DAT_200064d4);
  iVar2 = FUN_00001e50();
  if (iVar2 == 0) {
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
    }
  }
  DAT_200064bc = (char)_DAT_200040f8;
LAB_00009a54:
/* ... truncated ... */
```

#### `FUN_00009e1c` @ `00009e1c`

Site `00009f38`:

```asm
00009f24: ldr r2,[r3,#0x4]
00009f26: movt r5,#0x2000
00009f2a: subs r2,#0x1
00009f2c: str r2,[r3,#0x4]
00009f2e: movw r0,#0x3ff
00009f32: ldrh r1,[r6,#0x2]
00009f34: cmp r1,r0
00009f36: bls 0x00009fec
00009f38: ldr r2,[r3,#0x0]
00009f3a: cmp r2,#0x0
00009f3c: beq 0x00009fe8
00009f3e: ldr r2,[r3,#0x0]
00009f40: subs r2,#0x1
00009f42: str r2,[r3,#0x0]
00009f44: b 0x00009e7a
00009f46: ldrb r2,[r3,#0x0]
00009f48: cbz r2,0x00009f92
```

Site `00009f3e`:

```asm
00009f2c: str r2,[r3,#0x4]
00009f2e: movw r0,#0x3ff
00009f32: ldrh r1,[r6,#0x2]
00009f34: cmp r1,r0
00009f36: bls 0x00009fec
00009f38: ldr r2,[r3,#0x0]
00009f3a: cmp r2,#0x0
00009f3c: beq 0x00009fe8
00009f3e: ldr r2,[r3,#0x0]
00009f40: subs r2,#0x1
00009f42: str r2,[r3,#0x0]
00009f44: b 0x00009e7a
00009f46: ldrb r2,[r3,#0x0]
00009f48: cbz r2,0x00009f92
00009f4a: ldr r0,[r4,#0x0]
00009f4c: ldr r1,[r4,#0x4]
00009f4e: movs r2,#0x1
```

Site `00009f42`:

```asm
00009f32: ldrh r1,[r6,#0x2]
00009f34: cmp r1,r0
00009f36: bls 0x00009fec
00009f38: ldr r2,[r3,#0x0]
00009f3a: cmp r2,#0x0
00009f3c: beq 0x00009fe8
00009f3e: ldr r2,[r3,#0x0]
00009f40: subs r2,#0x1
00009f42: str r2,[r3,#0x0]
00009f44: b 0x00009e7a
00009f46: ldrb r2,[r3,#0x0]
00009f48: cbz r2,0x00009f92
00009f4a: ldr r0,[r4,#0x0]
00009f4c: ldr r1,[r4,#0x4]
00009f4e: movs r2,#0x1
00009f50: strb r2,[r3,#0x0]
00009f52: bl 0x0000234c
```

Site `0000a00c`:

```asm
00009ffc: ldrh r1,[r2,#0x0]
00009ffe: sxth r1,r1
0000a000: cmp r1,r6
0000a002: ble 0x0000a006
0000a004: strh r0,[r2,#0x0]
0000a006: movs r2,#0x1
0000a008: strb r2,[r5,#0x0]
0000a00a: adds r2,#0x3
0000a00c: str r2,[r3,#0x0]
0000a00e: b 0x00009e7a
0000a010: movw r2,#0x3ff
0000a014: subs r2,r2,r3
0000a016: movw r3,#0x64c0
0000a01a: movw r0,#0x3e8
0000a01e: sxth r2,r2
0000a020: movt r3,#0x2000
0000a024: strh r2,[r3,#0x2]
```

Site `00009f86`:

```asm
00009f6e: bl 0x00002288
00009f72: b 0x00009e2a
00009f74: movw r1,#0x3ff
00009f78: ldrh r2,[r6,#0x0]
00009f7a: cmp r2,r1
00009f7c: bls 0x00009fac
00009f7e: movw r3,#0x40f8
00009f82: movt r3,#0x2000
00009f86: ldr r2,[r3,#0x0]
00009f88: cbz r2,0x00009fe0
00009f8a: ldr r2,[r3,#0x0]
00009f8c: subs r2,#0x1
00009f8e: str r2,[r3,#0x0]
00009f90: b 0x00009e72
00009f92: movw r1,#0x64c0
00009f96: movt r1,#0x2000
00009f9a: strb r2,[r5,#0x0]
```

Site `00009f8a`:

```asm
00009f74: movw r1,#0x3ff
00009f78: ldrh r2,[r6,#0x0]
00009f7a: cmp r2,r1
00009f7c: bls 0x00009fac
00009f7e: movw r3,#0x40f8
00009f82: movt r3,#0x2000
00009f86: ldr r2,[r3,#0x0]
00009f88: cbz r2,0x00009fe0
00009f8a: ldr r2,[r3,#0x0]
00009f8c: subs r2,#0x1
00009f8e: str r2,[r3,#0x0]
00009f90: b 0x00009e72
00009f92: movw r1,#0x64c0
00009f96: movt r1,#0x2000
00009f9a: strb r2,[r5,#0x0]
00009f9c: movs r0,#0x0
00009f9e: strb r2,[r5,#0x1]
```

Site `00009f8e`:

```asm
00009f7a: cmp r2,r1
00009f7c: bls 0x00009fac
00009f7e: movw r3,#0x40f8
00009f82: movt r3,#0x2000
00009f86: ldr r2,[r3,#0x0]
00009f88: cbz r2,0x00009fe0
00009f8a: ldr r2,[r3,#0x0]
00009f8c: subs r2,#0x1
00009f8e: str r2,[r3,#0x0]
00009f90: b 0x00009e72
00009f92: movw r1,#0x64c0
00009f96: movt r1,#0x2000
00009f9a: strb r2,[r5,#0x0]
00009f9c: movs r0,#0x0
00009f9e: strb r2,[r5,#0x1]
00009fa0: strh r2,[r1,#0x0]
00009fa2: strh r2,[r1,#0x2]
```

Site `00009fdc`:

```asm
00009fc4: strh r1,[r3,#0x0]
00009fc6: movw r5,#0x64bc
00009fca: movs r3,#0x1
00009fcc: movt r5,#0x2000
00009fd0: strb r3,[r5,#0x0]
00009fd2: movw r3,#0x40f8
00009fd6: movs r2,#0x4
00009fd8: movt r3,#0x2000
00009fdc: str r2,[r3,#0x0]
00009fde: b 0x00009e7a
00009fe0: movw r5,#0x64bc
00009fe4: movt r5,#0x2000
00009fe8: strb r2,[r5,#0x0]
00009fea: b 0x00009e7a
00009fec: movw r2,#0x64c0
00009ff0: movw r6,#0x3e8
00009ff4: sxth r1,r1
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009e1c(void)

{
  int iVar1;
  undefined1 auStack_20 [16];
  
  iVar1 = FUN_00003f98();
  if (iVar1 != 0) {
    FUN_00009944();
    goto LAB_00009e2a;
  }
  iVar1 = FUN_000048e8(0x2b007de3);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar1 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar1 == 0) {
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    iVar1 = FUN_00001e50();
    if (iVar1 == 0) {
      if (_DAT_200064d4 < 0x400) {
        _DAT_200064c2 = 0x3ff - _DAT_200064d4;
        if (1000 < (short)_DAT_200064c2) {
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
      }
      else if (_DAT_200040f8 == 0) {
LAB_00009fe8:
        DAT_200064bc = (char)_DAT_200040f8;
      }
      else {
        _DAT_200040f8 = _DAT_200040f8 + -1;
      }
    }
    else if (_DAT_200064d4 < 0x400) {
      _DAT_200064c0 = _DAT_200064d4;
      if (1000 < (short)_DAT_200064d4) {
        _DAT_200064c0 = 0x3ff;
      }
      DAT_200064bc = '\x01';
      _DAT_200040f8 = 4;
    }
    else {
      if (_DAT_200040f8 == 0) goto LAB_00009fe8;
      _DAT_200040f8 = _DAT_200040f8 + -1;
    }
  }
  iVar1 = FUN_000048e8(0xf240bb40);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
  if (DAT_200064bc != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x200;
  }
  if (DAT_200064bd != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x400;
  }
  iVar1 = FUN_00003fa8();
  if (iVar1 == 0) {
    DAT_20006466 = '\0';
  }
  else {
    if (DAT_20006466 == '\0') {
      _DAT_200064c0 = 0;
      _DAT_200064d8 = 0;
      _DAT_200064dc = 0;
      DAT_200064bc = DAT_20006466;
      DAT_200064bd = DAT_20006466;
      _DAT_200064c2 = _DAT_200064c0;
    }
    DAT_20006466 = '\x01';
    FUN_0000234c(_DAT_200064d8,_DAT_200064dc);
    FUN_0000240c();
    FUN_00002618(&DAT_200064c0);
    FUN_00002288(&DAT_200064c0);
  }
LAB_00009e2a:
  iVar1 = FUN_00004034();
  if ((iVar1 != 0) && (iVar1 = FUN_00004048(auStack_20,0x10), iVar1 != 0)) {
    FUN_00002030(auStack_20,iVar1);
    FUN_00003fb8();
  }
  return;
}
```

### `200040fc`

- from `00009dc0` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009b96` in `FUN_00009944` @ `00009944` type=READ
- from `00009ba2` in `FUN_00009944` @ `00009944` type=READ
- from `00009baa` in `FUN_00009944` @ `00009944` type=WRITE
- from `0000a046` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `00009f18` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009f24` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009f2c` in `FUN_00009e1c` @ `00009e1c` type=WRITE

#### `FUN_00009944` @ `00009944`

Site `00009dc0`:

```asm
00009da8: strh r1,[r3,#0x2]
00009daa: movw r5,#0x64bc
00009dae: movs r3,#0x1
00009db0: movt r5,#0x2000
00009db4: strb r3,[r5,#0x1]
00009db6: movw r3,#0x40f8
00009dba: movs r2,#0x4
00009dbc: movt r3,#0x2000
00009dc0: str r2,[r3,#0x4]
00009dc2: b 0x00009bac
00009dc4: movw r5,#0x64bc
00009dc8: movt r5,#0x2000
00009dcc: strb r2,[r5,#0x1]
00009dce: b 0x00009bac
00009dd0: movs r3,#0x80
00009dd2: add r5,sp,#0x50
00009dd4: str r3,[sp,#0x4]
```

Site `00009b96`:

```asm
00009b80: cbnz r0,0x00009bd4
00009b82: movw r1,#0x3ff
00009b86: ldrh r3,[r6,#0x0]
00009b88: cmp r3,r1
00009b8a: bhi 0x00009b8e
00009b8c: b 0x00009d8a
00009b8e: movw r3,#0x40f8
00009b92: movt r3,#0x2000
00009b96: ldr r2,[r3,#0x4]
00009b98: cmp r2,#0x0
00009b9a: bne 0x00009b9e
00009b9c: b 0x00009dc4
00009b9e: movw r5,#0x64bc
00009ba2: ldr r2,[r3,#0x4]
00009ba4: movt r5,#0x2000
00009ba8: subs r2,#0x1
00009baa: str r2,[r3,#0x4]
```

Site `00009ba2`:

```asm
00009b8c: b 0x00009d8a
00009b8e: movw r3,#0x40f8
00009b92: movt r3,#0x2000
00009b96: ldr r2,[r3,#0x4]
00009b98: cmp r2,#0x0
00009b9a: bne 0x00009b9e
00009b9c: b 0x00009dc4
00009b9e: movw r5,#0x64bc
00009ba2: ldr r2,[r3,#0x4]
00009ba4: movt r5,#0x2000
00009ba8: subs r2,#0x1
00009baa: str r2,[r3,#0x4]
00009bac: movw r0,#0x3ff
00009bb0: ldrh r1,[r6,#0x2]
00009bb2: cmp r1,r0
00009bb4: bhi 0x00009bb8
00009bb6: b 0x00009d66
```

Site `00009baa`:

```asm
00009b96: ldr r2,[r3,#0x4]
00009b98: cmp r2,#0x0
00009b9a: bne 0x00009b9e
00009b9c: b 0x00009dc4
00009b9e: movw r5,#0x64bc
00009ba2: ldr r2,[r3,#0x4]
00009ba4: movt r5,#0x2000
00009ba8: subs r2,#0x1
00009baa: str r2,[r3,#0x4]
00009bac: movw r0,#0x3ff
00009bb0: ldrh r1,[r6,#0x2]
00009bb2: cmp r1,r0
00009bb4: bhi 0x00009bb8
00009bb6: b 0x00009d66
00009bb8: ldr r2,[r3,#0x0]
00009bba: cmp r2,#0x0
00009bbc: bne 0x00009bc0
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009944(void)

{
  bool bVar1;
  int iVar2;
  undefined4 *puVar3;
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
  
  iVar2 = FUN_00003fc8();
  if (iVar2 != 0) {
    iVar2 = FUN_000048e8(0x2b007de3);
    if (iVar2 != 0) {
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    do {
    } while (DAT_20006465 == '\0');
    DAT_20006465 = '\0';
    FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    FUN_0000179c();
    iVar2 = FUN_00001864();
    if ((iVar2 != 0) && (*(char *)(iVar2 + 0x68) != '\0')) {
      _DAT_2000646c = *(undefined2 *)(iVar2 + 6);
      _DAT_2000646e = *(undefined2 *)(iVar2 + 0x10);
      _DAT_20006470 = *(undefined2 *)(iVar2 + 0x1a);
      _DAT_20006472 = *(undefined2 *)(iVar2 + 0x24);
      _DAT_20006474 = *(undefined2 *)(iVar2 + 0x2e);
      _DAT_20006476 = *(undefined2 *)(iVar2 + 0x38);
      _DAT_20006478 = *(undefined2 *)(iVar2 + 0x42);
      _DAT_2000647a = *(undefined2 *)(iVar2 + 0x4c);
      _DAT_2000647c = *(undefined2 *)(iVar2 + 0x56);
      _DAT_2000647e = *(undefined2 *)(iVar2 + 0x60);
      _DAT_20006468 = *(undefined4 *)(iVar2 + 100);
    }
    iVar2 = FUN_000048e8(0xf240bb40);
    if (iVar2 == 0) {
      do {
      } while (DAT_20006465 == '\0');
      DAT_20006465 = 0;
      FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
      iVar2 = FUN_0000408c(0,0x200064a8,&DAT_20006494,0x20006480,auStack_98,0x80);
      if (iVar2 != 0) {
        FUN_00002030(auStack_98,iVar2);
      }
      iVar2 = FUN_00001e50();
      if (iVar2 != 0) {
        return;
      }
      FUN_00009448(1,4000);
      iVar2 = FUN_0000408c(1,DAT_00009e0c,DAT_00009e14,DAT_00009e10,auStack_98,0x80);
      if (iVar2 == 0) {
        return;
      }
      FUN_00002030(auStack_98,iVar2);
      return;
    }
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar2 = FUN_000048e8(0x2b007de3);
  if (iVar2 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar2 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar2 != 0) goto LAB_00009a54;
  FUN_00002b44();
  FUN_00003120(&DAT_200064d4);
  iVar2 = FUN_00001e50();
  if (iVar2 == 0) {
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
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
      goto LAB_00009a54;
    }
    if (_DAT_200040f8 != 0) {
      _DAT_200040f8 = _DAT_200040f8 + -1;
      goto LAB_00009a54;
    }
  }
  DAT_200064bc = (char)_DAT_200040f8;
LAB_00009a54:
/* ... truncated ... */
```

#### `FUN_00009e1c` @ `00009e1c`

Site `0000a046`:

```asm
0000a02e: strh r1,[r3,#0x2]
0000a030: movw r5,#0x64bc
0000a034: movs r3,#0x1
0000a036: movt r5,#0x2000
0000a03a: strb r3,[r5,#0x1]
0000a03c: movw r3,#0x40f8
0000a040: movs r2,#0x4
0000a042: movt r3,#0x2000
0000a046: str r2,[r3,#0x4]
0000a048: b 0x00009f2e
0000a04a: movw r5,#0x64bc
0000a04e: movt r5,#0x2000
0000a052: strb r2,[r5,#0x1]
0000a054: b 0x00009f2e
0000a058: push {r4,r5,r6,r7,lr}
0000a05a: mov lr,r8
0000a05c: push {lr}
```

Site `00009f18`:

```asm
00009f02: cbnz r0,0x00009f74
00009f04: movw r1,#0x3ff
00009f08: ldrh r3,[r6,#0x0]
00009f0a: cmp r3,r1
00009f0c: bhi 0x00009f10
00009f0e: b 0x0000a010
00009f10: movw r3,#0x40f8
00009f14: movt r3,#0x2000
00009f18: ldr r2,[r3,#0x4]
00009f1a: cmp r2,#0x0
00009f1c: bne 0x00009f20
00009f1e: b 0x0000a04a
00009f20: movw r5,#0x64bc
00009f24: ldr r2,[r3,#0x4]
00009f26: movt r5,#0x2000
00009f2a: subs r2,#0x1
00009f2c: str r2,[r3,#0x4]
```

Site `00009f24`:

```asm
00009f0e: b 0x0000a010
00009f10: movw r3,#0x40f8
00009f14: movt r3,#0x2000
00009f18: ldr r2,[r3,#0x4]
00009f1a: cmp r2,#0x0
00009f1c: bne 0x00009f20
00009f1e: b 0x0000a04a
00009f20: movw r5,#0x64bc
00009f24: ldr r2,[r3,#0x4]
00009f26: movt r5,#0x2000
00009f2a: subs r2,#0x1
00009f2c: str r2,[r3,#0x4]
00009f2e: movw r0,#0x3ff
00009f32: ldrh r1,[r6,#0x2]
00009f34: cmp r1,r0
00009f36: bls 0x00009fec
00009f38: ldr r2,[r3,#0x0]
```

Site `00009f2c`:

```asm
00009f18: ldr r2,[r3,#0x4]
00009f1a: cmp r2,#0x0
00009f1c: bne 0x00009f20
00009f1e: b 0x0000a04a
00009f20: movw r5,#0x64bc
00009f24: ldr r2,[r3,#0x4]
00009f26: movt r5,#0x2000
00009f2a: subs r2,#0x1
00009f2c: str r2,[r3,#0x4]
00009f2e: movw r0,#0x3ff
00009f32: ldrh r1,[r6,#0x2]
00009f34: cmp r1,r0
00009f36: bls 0x00009fec
00009f38: ldr r2,[r3,#0x0]
00009f3a: cmp r2,#0x0
00009f3c: beq 0x00009fe8
00009f3e: ldr r2,[r3,#0x0]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00009e1c(void)

{
  int iVar1;
  undefined1 auStack_20 [16];
  
  iVar1 = FUN_00003f98();
  if (iVar1 != 0) {
    FUN_00009944();
    goto LAB_00009e2a;
  }
  iVar1 = FUN_000048e8(0x2b007de3);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  iVar1 = FUN_00004ce8(0x2b007de3,0,&DAT_200064d4);
  if (iVar1 == 0) {
    FUN_00002b44();
    FUN_00003120(&DAT_200064d4);
    iVar1 = FUN_00001e50();
    if (iVar1 == 0) {
      if (_DAT_200064d4 < 0x400) {
        _DAT_200064c2 = 0x3ff - _DAT_200064d4;
        if (1000 < (short)_DAT_200064c2) {
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
      }
      else if (_DAT_200040f8 == 0) {
LAB_00009fe8:
        DAT_200064bc = (char)_DAT_200040f8;
      }
      else {
        _DAT_200040f8 = _DAT_200040f8 + -1;
      }
    }
    else if (_DAT_200064d4 < 0x400) {
      _DAT_200064c0 = _DAT_200064d4;
      if (1000 < (short)_DAT_200064d4) {
        _DAT_200064c0 = 0x3ff;
      }
      DAT_200064bc = '\x01';
      _DAT_200040f8 = 4;
    }
    else {
      if (_DAT_200040f8 == 0) goto LAB_00009fe8;
      _DAT_200040f8 = _DAT_200040f8 + -1;
    }
  }
  iVar1 = FUN_000048e8(0xf240bb40);
  if (iVar1 != 0) {
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  do {
  } while (DAT_20006465 == '\0');
  DAT_20006465 = '\0';
  FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
  if (DAT_200064bc != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x200;
  }
  if (DAT_200064bd != '\0') {
    _DAT_200064d8 = _DAT_200064d8 | 0x400;
  }
  iVar1 = FUN_00003fa8();
  if (iVar1 == 0) {
    DAT_20006466 = '\0';
  }
  else {
    if (DAT_20006466 == '\0') {
      _DAT_200064c0 = 0;
      _DAT_200064d8 = 0;
      _DAT_200064dc = 0;
      DAT_200064bc = DAT_20006466;
      DAT_200064bd = DAT_20006466;
      _DAT_200064c2 = _DAT_200064c0;
    }
    DAT_20006466 = '\x01';
    FUN_0000234c(_DAT_200064d8,_DAT_200064dc);
    FUN_0000240c();
    FUN_00002618(&DAT_200064c0);
    FUN_00002288(&DAT_200064c0);
  }
LAB_00009e2a:
  iVar1 = FUN_00004034();
  if ((iVar1 != 0) && (iVar1 = FUN_00004048(auStack_20,0x10), iVar1 != 0)) {
    FUN_00002030(auStack_20,iVar1);
    FUN_00003fb8();
  }
  return;
}
```

