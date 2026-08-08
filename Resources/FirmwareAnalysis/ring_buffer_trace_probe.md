# Motion 32 Ring Buffer Trace Probe

## Functions

### `000017c0` `FUN_0000179c`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_0000179c(void)

{
  int iVar1;
  undefined4 uVar2;
  ushort uVar3;
  int iVar4;
  short sVar5;
  int iVar6;
  ushort *puVar7;
  
  if (DAT_200041ac == '\0') {
    uVar2 = 0x21;
  }
  else {
    puVar7 = (ushort *)&DAT_20004140;
    iVar6 = 0;
    sVar5 = 0;
    do {
      *(char *)(puVar7 + 4) = (char)sVar5;
      iVar1 = FUN_00002aa8();
      if (_DAT_d0f52828 == 0) {
        *puVar7 = 0;
        if (_DAT_d0f5282c == 0) goto LAB_00001838;
LAB_000017e2:
        iVar4 = (uint)*(ushort *)(_DAT_d0f5282c + iVar6) - iVar1;
        puVar7[1] = (ushort)iVar4 & (short)~(ushort)((uint)iVar4 >> 0x10) >> 0xf;
        if (_DAT_d0f52830 != 0) goto LAB_000017f4;
LAB_00001842:
        uVar3 = 0;
      }
      else {
        iVar4 = (uint)*(ushort *)(_DAT_d0f52828 + iVar6) - iVar1;
        *puVar7 = (ushort)iVar4 & (short)~(ushort)((uint)iVar4 >> 0x10) >> 0xf;
        if (_DAT_d0f5282c != 0) goto LAB_000017e2;
LAB_00001838:
        puVar7[1] = 0;
        if (_DAT_d0f52830 == 0) goto LAB_00001842;
LAB_000017f4:
        iVar1 = (uint)*(ushort *)(_DAT_d0f52830 + iVar6 * 2 + 2) - iVar1;
        uVar3 = (ushort)iVar1 & (short)~(ushort)((uint)iVar1 >> 0x10) >> 0xf;
      }
      iVar1 = _DAT_d0f52824;
      puVar7[2] = uVar3;
      uVar3 = 0;
      if (iVar1 != 0) {
        uVar3 = (ushort)*(undefined4 *)(iVar6 * 2 + iVar1) & 0x3ff;
      }
      sVar5 = sVar5 + 1;
      puVar7[3] = uVar3;
      iVar6 = iVar6 + 2;
      puVar7 = puVar7 + 5;
    } while (sVar5 != 10);
    uVar2 = 0;
    DAT_200041a8 = 1;
    _DAT_200041a4 = _DAT_200041a4 + 1;
  }
  return uVar2;
}
```

Callers:
- none

### `000017f8` `FUN_0000179c`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_0000179c(void)

{
  int iVar1;
  undefined4 uVar2;
  ushort uVar3;
  int iVar4;
  short sVar5;
  int iVar6;
  ushort *puVar7;
  
  if (DAT_200041ac == '\0') {
    uVar2 = 0x21;
  }
  else {
    puVar7 = (ushort *)&DAT_20004140;
    iVar6 = 0;
    sVar5 = 0;
    do {
      *(char *)(puVar7 + 4) = (char)sVar5;
      iVar1 = FUN_00002aa8();
      if (_DAT_d0f52828 == 0) {
        *puVar7 = 0;
        if (_DAT_d0f5282c == 0) goto LAB_00001838;
LAB_000017e2:
        iVar4 = (uint)*(ushort *)(_DAT_d0f5282c + iVar6) - iVar1;
        puVar7[1] = (ushort)iVar4 & (short)~(ushort)((uint)iVar4 >> 0x10) >> 0xf;
        if (_DAT_d0f52830 != 0) goto LAB_000017f4;
LAB_00001842:
        uVar3 = 0;
      }
      else {
        iVar4 = (uint)*(ushort *)(_DAT_d0f52828 + iVar6) - iVar1;
        *puVar7 = (ushort)iVar4 & (short)~(ushort)((uint)iVar4 >> 0x10) >> 0xf;
        if (_DAT_d0f5282c != 0) goto LAB_000017e2;
LAB_00001838:
        puVar7[1] = 0;
        if (_DAT_d0f52830 == 0) goto LAB_00001842;
LAB_000017f4:
        iVar1 = (uint)*(ushort *)(_DAT_d0f52830 + iVar6 * 2 + 2) - iVar1;
        uVar3 = (ushort)iVar1 & (short)~(ushort)((uint)iVar1 >> 0x10) >> 0xf;
      }
      iVar1 = _DAT_d0f52824;
      puVar7[2] = uVar3;
      uVar3 = 0;
      if (iVar1 != 0) {
        uVar3 = (ushort)*(undefined4 *)(iVar6 * 2 + iVar1) & 0x3ff;
      }
      sVar5 = sVar5 + 1;
      puVar7[3] = uVar3;
      iVar6 = iVar6 + 2;
      puVar7 = puVar7 + 5;
    } while (sVar5 != 10);
    uVar2 = 0;
    DAT_200041a8 = 1;
    _DAT_200041a4 = _DAT_200041a4 + 1;
  }
  return uVar2;
}
```

Callers:
- none

### `00001c8c` `FUN_00001c8c`

```c

int FUN_00001c8c(undefined1 param_1)

{
  undefined4 uVar1;
  int iVar2;
  undefined4 local_18;
  undefined2 local_14;
  undefined1 local_12;
  undefined1 local_11;
  
  uVar1 = DAT_000098c0;
  if (DAT_20004290 == '\0') {
    iVar2 = 0x21;
  }
  else {
    local_18 = 0xdeadbeef;
    local_14 = 1;
    local_11 = 0;
    local_12 = param_1;
    iVar2 = FUN_00006b00(DAT_000098c0,&DAT_40100400,1);
    if ((iVar2 == 0) && (iVar2 = FUN_00006cb4(uVar1,&local_18,&DAT_40100400,8), iVar2 == 0)) {
      DAT_20004080 = param_1;
    }
  }
  return iVar2;
}
```

Callers:
- `FUN_00009944` @ `00009944`

### `00001cfc` `FUN_00001cfc`

```c

undefined4 FUN_00001cfc(int param_1)

{
  undefined4 uVar1;
  
  if (DAT_20004290 == '\0') {
    uVar1 = 0x21;
  }
  else if (param_1 == 0) {
    uVar1 = 1;
  }
  else {
    FUN_0000a578(param_1,&DAT_40100400,8);
    uVar1 = 0;
  }
  return uVar1;
}
```

Callers:
- `FUN_00009944` @ `00009944`

### `00001d28` `FUN_00001d28`

```c

void FUN_00001d28(undefined4 *param_1)

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

Callers:
- `FUN_00003a14` @ `00003a14`

### `00001d54` `FUN_00001d54`

```c

int FUN_00001d54(uint *param_1)

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

Callers:
- `FUN_000020a4` @ `000020a4`

### `00001d6c` `FUN_00001d6c`

```c

void FUN_00001d6c(int *param_1,undefined1 param_2)

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

Callers:
- `FUN_00001eec` @ `00001eec`
- `FUN_00002030` @ `00002030`
- `FUN_00001f6c` @ `00001f6c`
- `FUN_00001fb0` @ `00001fb0`

### `00001d94` `FUN_00001d94`

```c

undefined1 FUN_00001d94(int param_1)

{
  undefined1 uVar1;
  undefined4 local_4;
  
  local_4 = *(int *)(param_1 + 4) + 1;
  if (*(int *)(param_1 + 8) + 1 == local_4) {
    local_4 = 0;
  }
  uVar1 = *(undefined1 *)(*(int *)(param_1 + 0x14) + local_4);
  *(int *)(param_1 + 4) = local_4;
  return uVar1;
}
```

Callers:
- `FUN_000020a4` @ `000020a4`

### `00001dc0` `FUN_00001dc0`

```c

int FUN_00001dc0(uint *param_1,int param_2,int param_3)

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

Callers:
- none

### `00003ab8` `FUN_00003ab8`

```c

undefined4 FUN_00003ab8(void)

{
  return 0x200040a0;
}
```

Callers:
- `FUN_000020a4` @ `000020a4`

### `00003a14` `FUN_00003a14`

```c

void FUN_00003a14(int param_1)

{
  FUN_00001d28(0x200040a0);
  DAT_20005b60 = 1;
  if (param_1 == 1) {
    FUN_00005854(0x20005cd4,&LAB_000097e4);
  }
  else {
    FUN_00005854(0x20005d24,&LAB_00009874);
  }
  return;
}
```

Callers:
- `FUN_00001e5c` @ `00001e5c`

### `00003ac4` `PROBE_00003ac4`

```c

void PROBE_00003ac4(int param_1)

{
  if (*(char *)(param_1 + 4) == '\x02') {
    DAT_20005b60 = 1;
  }
  else if (*(char *)(param_1 + 4) == '\x04') {
    FUN_00001d6c(0x200040a0,*(undefined1 *)(param_1 + 8));
  }
  return;
}
```

Callers:
- none

### `00003af0` `PROBE_00003af0`

```c

undefined4 PROBE_00003af0(byte *param_1,byte *param_2,ushort *param_3,char *param_4,byte *param_5)

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

Callers:
- none

### `00003f54` `PROBE_00003f54`

```c

void PROBE_00003f54(void)

{
  return;
}
```

Callers:
- none

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
- `FUN_00009944` @ `00009944`

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
- `FUN_00009e1c` @ `00009e1c`

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
- `FUN_00009e1c` @ `00009e1c`

## RAM References

### `20004080`

- from `00001c76` in `FUN_00001bf0` @ `00001bf0` type=WRITE
- from `00001c86` in `FUN_00001bf0` @ `00001bf0` type=WRITE
- from `00001cf4` in `FUN_00001c8c` @ `00001c8c` type=WRITE
- from `00009848` in `<none>` @ `<none>` type=PARAM

#### Function `FUN_00001bf0` @ `00001bf0`

Site `00001c76`:

```asm
00001c64: bl 0x00006cb4
00001c68: cmp r0,#0x0
00001c6a: bne 0x00001c52
00001c6c: movw r3,#0x4080
00001c70: movs r2,#0x42
00001c72: movt r3,#0x2000
00001c76: strb r2,[r3,#0x0]
00001c78: b 0x00001c52
00001c7a: movs r0,#0x21
00001c7c: b 0x00001c52
00001c7e: movw r3,#0x4080
00001c82: movt r3,#0x2000
00001c86: strb r0,[r3,#0x0]
```

Site `00001c86`:

```asm
00001c76: strb r2,[r3,#0x0]
00001c78: b 0x00001c52
00001c7a: movs r0,#0x21
00001c7c: b 0x00001c52
00001c7e: movw r3,#0x4080
00001c82: movt r3,#0x2000
00001c86: strb r0,[r3,#0x0]
00001c88: movs r0,#0x0
00001c8a: b 0x00001c52
00001c8c: movw r3,#0x4290
00001c90: push {r4,r5,lr}
00001c92: movt r3,#0x2000
00001c96: ldrb r3,[r3,#0x0]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_00001bf0(void)

{
  undefined4 uVar1;
  int iVar2;
  undefined4 local_10;
  undefined4 local_c;
  
  if (DAT_20004290 == '\0') {
    iVar2 = 0x21;
  }
  else if ((_DAT_40100400 == -0x21524111) && (_DAT_40100404 == 1)) {
    iVar2 = 0;
    DAT_20004080 = DAT_40100406;
  }
  else {
    FUN_00001e50();
    uVar1 = DAT_000098c0;
    local_10 = 0xdeadbeef;
    local_c = 0x420001;
    iVar2 = FUN_00006b00(DAT_000098c0,&DAT_40100400,1);
    if ((iVar2 == 0) && (iVar2 = FUN_00006cb4(uVar1,&local_10,&DAT_40100400,8), iVar2 == 0)) {
      DAT_20004080 = 0x42;
    }
  }
  return iVar2;
}
```

#### Function `FUN_00001c8c` @ `00001c8c`

Site `00001cf4`:

```asm
00001ce0: movt r2,#0x4010
00001ce4: bl 0x00006cb4
00001ce8: cmp r0,#0x0
00001cea: bne 0x00001cd2
00001cec: movw r3,#0x4080
00001cf0: movt r3,#0x2000
00001cf4: strb r4,[r3,#0x0]
00001cf6: b 0x00001cd2
00001cf8: movs r0,#0x21
00001cfa: b 0x00001cd2
00001cfc: movw r3,#0x4290
00001d00: movt r3,#0x2000
00001d04: ldrb r3,[r3,#0x0]
```

```c

int FUN_00001c8c(undefined1 param_1)

{
  undefined4 uVar1;
  int iVar2;
  undefined4 local_18;
  undefined2 local_14;
  undefined1 local_12;
  undefined1 local_11;
  
  uVar1 = DAT_000098c0;
  if (DAT_20004290 == '\0') {
    iVar2 = 0x21;
  }
  else {
    local_18 = 0xdeadbeef;
    local_14 = 1;
    local_11 = 0;
    local_12 = param_1;
    iVar2 = FUN_00006b00(DAT_000098c0,&DAT_40100400,1);
    if ((iVar2 == 0) && (iVar2 = FUN_00006cb4(uVar1,&local_18,&DAT_40100400,8), iVar2 == 0)) {
      DAT_20004080 = param_1;
    }
  }
  return iVar2;
}
```

### `20004081`

- from `00001ef8` in `FUN_00001eec` @ `00001eec` type=READ
- from `00001f08` in `FUN_00001eec` @ `00001eec` type=WRITE
- from `00001f36` in `FUN_00001eec` @ `00001eec` type=READ
- from `00001f40` in `FUN_00001eec` @ `00001eec` type=WRITE
- from `00001f76` in `FUN_00001f6c` @ `00001f6c` type=READ
- from `00001f7e` in `FUN_00001f6c` @ `00001f6c` type=WRITE
- from `00001f72` in `FUN_00001f6c` @ `00001f6c` type=PARAM
- from `00001fba` in `FUN_00001fb0` @ `00001fb0` type=READ
- from `00001fc4` in `FUN_00001fb0` @ `00001fb0` type=WRITE
- from `00001fb6` in `FUN_00001fb0` @ `00001fb0` type=PARAM

#### Function `FUN_00001eec` @ `00001eec`

Site `00001ef8`:

```asm
00001ee4: bl 0x00005ef0
00001ee8: b 0x00001ece
00001eec: push {r3,r4,r5,r6,r7,lr}
00001eee: movw r5,#0x4081
00001ef2: movs r7,#0x7f
00001ef4: movt r5,#0x2000
00001ef8: ldrb r3,[r5,#0x0]
00001efa: asrs r6,r1,#0x7
00001efc: ands r6,r7
00001efe: movs r4,r0
00001f00: ands r7,r1
00001f02: cmp r3,r0
00001f04: beq 0x00001f1a
```

Site `00001f08`:

```asm
00001efc: ands r6,r7
00001efe: movs r4,r0
00001f00: ands r7,r1
00001f02: cmp r3,r0
00001f04: beq 0x00001f1a
00001f06: movs r1,r0
00001f08: strb r0,[r5,#0x0]
00001f0a: movw r0,#0x4084
00001f0e: subs r1,#0x50
00001f10: uxtb r1,r1
00001f12: movt r0,#0x2000
00001f16: bl 0x00001d6c
00001f1a: movw r0,#0x4084
```

Site `00001f36`:

```asm
00001f20: movt r0,#0x2000
00001f24: bl 0x00001d6c
00001f28: movw r0,#0x4084
00001f2c: movs r1,r6
00001f2e: movt r0,#0x2000
00001f32: bl 0x00001d6c
00001f36: ldrb r3,[r5,#0x0]
00001f38: cmp r3,r4
00001f3a: beq 0x00001f4e
00001f3c: movw r0,#0x4084
00001f40: strb r4,[r5,#0x0]
00001f42: subs r4,#0x50
00001f44: uxtb r1,r4
```

Site `00001f40`:

```asm
00001f2e: movt r0,#0x2000
00001f32: bl 0x00001d6c
00001f36: ldrb r3,[r5,#0x0]
00001f38: cmp r3,r4
00001f3a: beq 0x00001f4e
00001f3c: movw r0,#0x4084
00001f40: strb r4,[r5,#0x0]
00001f42: subs r4,#0x50
00001f44: uxtb r1,r4
00001f46: movt r0,#0x2000
00001f4a: bl 0x00001d6c
00001f4e: movw r0,#0x4084
00001f52: movs r1,#0x36
```

```c

void FUN_00001eec(uint param_1,uint param_2,undefined4 param_3,undefined4 param_4)

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
    FUN_00001d6c(0x20004084,param_1 - 0x50 & 0xff,param_3,uVar2,param_4);
    uVar2 = extraout_r3;
    param_3 = extraout_r2;
  }
  FUN_00001d6c(0x20004084,0x16,param_3,uVar2,param_4);
  FUN_00001d6c(0x20004084,(int)param_2 >> 7 & 0x7f);
  uVar2 = (uint)DAT_20004081;
  uVar1 = extraout_r2_00;
  if (uVar2 != param_1) {
    DAT_20004081 = (byte)param_1;
    FUN_00001d6c(0x20004084,param_1 - 0x50 & 0xff,extraout_r2_00,uVar2,param_4);
    uVar2 = extraout_r3_00;
    uVar1 = extraout_r2_01;
  }
  FUN_00001d6c(0x20004084,0x36,uVar1,uVar2,param_4);
  FUN_00001d6c(0x20004084,param_2 & 0x7f);
  return;
}
```

#### Function `FUN_00001f6c` @ `00001f6c`

Site `00001f76`:

```asm
00001f62: movt r0,#0x2000
00001f66: bl 0x00001d6c
00001f6a: pop {r3,r4,r5,r6,r7,pc}
00001f6c: movw r3,#0x4081
00001f70: push {r4,lr}
00001f72: movt r3,#0x2000
00001f76: ldrb r2,[r3,#0x0]
00001f78: movs r4,r1
00001f7a: cmp r2,r0
00001f7c: beq 0x00001f90
00001f7e: strb r0,[r3,#0x0]
00001f80: subs r0,#0x50
00001f82: uxtb r1,r0
```

Site `00001f7e`:

```asm
00001f70: push {r4,lr}
00001f72: movt r3,#0x2000
00001f76: ldrb r2,[r3,#0x0]
00001f78: movs r4,r1
00001f7a: cmp r2,r0
00001f7c: beq 0x00001f90
00001f7e: strb r0,[r3,#0x0]
00001f80: subs r0,#0x50
00001f82: uxtb r1,r0
00001f84: movw r0,#0x4084
00001f88: movt r0,#0x2000
00001f8c: bl 0x00001d6c
00001f90: movw r0,#0x4084
```

Site `00001f72`:

```asm
00001f60: movs r1,r7
00001f62: movt r0,#0x2000
00001f66: bl 0x00001d6c
00001f6a: pop {r3,r4,r5,r6,r7,pc}
00001f6c: movw r3,#0x4081
00001f70: push {r4,lr}
00001f72: movt r3,#0x2000
00001f76: ldrb r2,[r3,#0x0]
00001f78: movs r4,r1
00001f7a: cmp r2,r0
00001f7c: beq 0x00001f90
00001f7e: strb r0,[r3,#0x0]
00001f80: subs r0,#0x50
```

```c

void FUN_00001f6c(uint param_1,undefined4 param_2)

{
  if (DAT_20004081 != param_1) {
    DAT_20004081 = (byte)param_1;
    FUN_00001d6c(0x20004084,param_1 - 0x50 & 0xff);
  }
  FUN_00001d6c(0x20004084,0x14);
  FUN_00001d6c(0x20004084,param_2);
  return;
}
```

#### Function `FUN_00001fb0` @ `00001fb0`

Site `00001fba`:

```asm
00001fa4: movt r0,#0x2000
00001fa8: bl 0x00001d6c
00001fac: pop {r4,pc}
00001fb0: movw r3,#0x4081
00001fb4: push {r4,lr}
00001fb6: movt r3,#0x2000
00001fba: ldrb r2,[r3,#0x0]
00001fbc: adds r1,#0x40
00001fbe: uxtb r4,r1
00001fc0: cmp r2,r0
00001fc2: beq 0x00001fd6
00001fc4: strb r0,[r3,#0x0]
00001fc6: subs r0,#0x50
```

Site `00001fc4`:

```asm
00001fb6: movt r3,#0x2000
00001fba: ldrb r2,[r3,#0x0]
00001fbc: adds r1,#0x40
00001fbe: uxtb r4,r1
00001fc0: cmp r2,r0
00001fc2: beq 0x00001fd6
00001fc4: strb r0,[r3,#0x0]
00001fc6: subs r0,#0x50
00001fc8: uxtb r1,r0
00001fca: movw r0,#0x4084
00001fce: movt r0,#0x2000
00001fd2: bl 0x00001d6c
00001fd6: movw r0,#0x4084
```

Site `00001fb6`:

```asm
00001fa2: movs r1,r4
00001fa4: movt r0,#0x2000
00001fa8: bl 0x00001d6c
00001fac: pop {r4,pc}
00001fb0: movw r3,#0x4081
00001fb4: push {r4,lr}
00001fb6: movt r3,#0x2000
00001fba: ldrb r2,[r3,#0x0]
00001fbc: adds r1,#0x40
00001fbe: uxtb r4,r1
00001fc0: cmp r2,r0
00001fc2: beq 0x00001fd6
00001fc4: strb r0,[r3,#0x0]
```

```c

void FUN_00001fb0(uint param_1,char param_2)

{
  if (DAT_20004081 != param_1) {
    DAT_20004081 = (byte)param_1;
    FUN_00001d6c(0x20004084,param_1 - 0x50 & 0xff);
  }
  FUN_00001d6c(0x20004084,0x15);
  FUN_00001d6c(0x20004084,param_2 + '@');
  return;
}
```

### `20004084`

- no direct references found

### `20004098`

- no direct references found

### `200040a0`

- no direct references found

### `200040b4`

- no direct references found

### `20004290`

- from `000019e4` in `FUN_000019c0` @ `000019c0` type=WRITE
- from `000019f2` in `FUN_000019e8` @ `000019e8` type=READ
- from `000019ee` in `FUN_000019e8` @ `000019e8` type=PARAM
- from `00001b3a` in `FUN_00001b30` @ `00001b30` type=READ
- from `00001bfa` in `FUN_00001bf0` @ `00001bf0` type=READ
- from `00001c96` in `FUN_00001c8c` @ `00001c8c` type=READ
- from `00001d04` in `FUN_00001cfc` @ `00001cfc` type=READ

#### Function `FUN_000019c0` @ `000019c0`

Site `000019e4`:

```asm
000019d4: beq 0x000019d8
000019d6: pop {r4,pc}
000019d8: movw r3,#0x4290
000019dc: movs r2,#0x1
000019de: movt r3,#0x2000
000019e2: movs r0,#0x0
000019e4: strb r2,[r3,#0x0]
000019e6: b 0x000019d6
000019e8: movw r3,#0x4290
000019ec: push {r4,r5,r6,lr}
000019ee: movt r3,#0x2000
000019f2: ldrb r6,[r3,#0x0]
000019f4: sub sp,#0x48
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_000019c0(undefined4 param_1,undefined4 param_2,undefined4 param_3)

{
  int iVar1;
  
  iVar1 = FUN_0000657c(DAT_000098c0,_FUN_000098c4,param_3,0x98c8);
  if ((iVar1 == 0) || (iVar1 == 0xe)) {
    iVar1 = 0;
    DAT_20004290 = 1;
  }
  return iVar1;
}
```

#### Function `FUN_000019e8` @ `000019e8`

Site `000019f2`:

```asm
000019e2: movs r0,#0x0
000019e4: strb r2,[r3,#0x0]
000019e6: b 0x000019d6
000019e8: movw r3,#0x4290
000019ec: push {r4,r5,r6,lr}
000019ee: movt r3,#0x2000
000019f2: ldrb r6,[r3,#0x0]
000019f4: sub sp,#0x48
000019f6: cmp r6,#0x0
000019f8: beq 0x00001aae
000019fa: movs r1,#0x0
000019fc: add r5,sp,#0x4
000019fe: movs r2,#0x44
```

Site `000019ee`:

```asm
000019de: movt r3,#0x2000
000019e2: movs r0,#0x0
000019e4: strb r2,[r3,#0x0]
000019e6: b 0x000019d6
000019e8: movw r3,#0x4290
000019ec: push {r4,r5,r6,lr}
000019ee: movt r3,#0x2000
000019f2: ldrb r6,[r3,#0x0]
000019f4: sub sp,#0x48
000019f6: cmp r6,#0x0
000019f8: beq 0x00001aae
000019fa: movs r1,#0x0
000019fc: add r5,sp,#0x4
```

```c

int FUN_000019e8(void)

{
  undefined4 uVar1;
  int iVar2;
  char cVar3;
  int local_54;
  short local_50;
  undefined1 auStack_4e [2];
  undefined1 auStack_4c [14];
  undefined1 local_3e;
  undefined1 local_3d;
  undefined1 local_3c;
  undefined2 local_3a;
  undefined2 local_38;
  undefined1 local_36;
  undefined1 auStack_34 [10];
  undefined1 uStack_2a;
  char cStack_29;
  undefined1 auStack_28 [10];
  undefined1 uStack_1e;
  char cStack_1d;
  
  cVar3 = DAT_20004290;
  if (DAT_20004290 == '\0') {
    iVar2 = 0x21;
  }
  else {
    FUN_0000a578(&local_54,0x40100000,0x44);
    if ((local_54 == -0x35014542) && (local_50 == 9)) {
      iVar2 = FUN_000015fc(auStack_4c);
      if (iVar2 == 0) {
        FUN_000034a8(local_3e);
        FUN_000034b4(local_3d);
        FUN_000034d4(local_3c);
        FUN_000034c4(local_3a,local_38);
        FUN_000034e0(local_36);
        if (cStack_29 != '\0') {
          FUN_00003428(0,auStack_34,uStack_2a);
        }
        if (cStack_1d != '\0') {
          FUN_00003428(1,auStack_28,uStack_1e);
        }
      }
    }
    else {
      FUN_0000a568(auStack_4e,0,0x3e);
      local_54 = -0x35014542;
      local_50 = 9;
      iVar2 = FUN_00001880(auStack_4c);
      if (iVar2 == 0) {
        iVar2 = FUN_000034ec();
        if (iVar2 != 0) {
          FUN_0000a578(&local_3e,iVar2,10);
        }
        iVar2 = FUN_00003508(0,auStack_34);
        cStack_29 = cVar3;
        if (iVar2 != 0) {
          FUN_0000a568(auStack_34,0,10);
          uStack_2a = 5;
          cStack_29 = '\0';
        }
        iVar2 = FUN_00003508(1,auStack_28);
        if (iVar2 != 0) {
          FUN_0000a568(auStack_28,0,10);
          cVar3 = '\0';
          uStack_1e = 5;
        }
        uVar1 = DAT_000098c0;
        cStack_1d = cVar3;
        iVar2 = FUN_00006b00(DAT_000098c0,0x40100000,1);
        if (iVar2 == 0) {
          iVar2 = FUN_00006cb4(uVar1,&local_54,0x40100000,0x44);
        }
      }
    }
  }
  return iVar2;
}
```

#### Function `FUN_00001b30` @ `00001b30`

Site `00001b3a`:

```asm
00001b28: movs r0,#0x0
00001b2a: bl 0x00003428
00001b2e: b 0x00001ae4
00001b30: movw r3,#0x4290
00001b34: push {r4,lr}
00001b36: movt r3,#0x2000
00001b3a: ldrb r3,[r3,#0x0]
00001b3c: sub sp,#0x48
00001b3e: cmp r3,#0x0
00001b40: beq 0x00001bbe
00001b42: movs r0,#0xa
00001b44: movs r2,#0x3e
00001b46: movs r1,#0x0
```

```c

int FUN_00001b30(void)

{
  undefined4 uVar1;
  int iVar2;
  undefined4 local_4c;
  undefined2 local_48;
  undefined1 auStack_46 [2];
  undefined1 auStack_44 [14];
  undefined1 auStack_36 [10];
  undefined1 auStack_2c [10];
  undefined1 uStack_22;
  undefined1 auStack_20 [10];
  undefined1 uStack_16;
  
  if (DAT_20004290 == '\0') {
    iVar2 = 0x21;
  }
  else {
    FUN_0000a568(auStack_46,0,0x3e);
    local_4c = 0xcafebabe;
    local_48 = 9;
    iVar2 = FUN_00001880(auStack_44);
    if (iVar2 == 0) {
      iVar2 = FUN_000034ec();
      if (iVar2 != 0) {
        FUN_0000a578(auStack_36,iVar2,10);
      }
      iVar2 = FUN_00003508(0,auStack_2c);
      if (iVar2 != 0) {
        FUN_0000a568(auStack_2c,0,0xc);
        uStack_22 = 5;
      }
      iVar2 = FUN_00003508(1,auStack_20);
      if (iVar2 != 0) {
        FUN_0000a568(auStack_20,0,0xc);
        uStack_16 = 5;
      }
      uVar1 = DAT_000098c0;
      iVar2 = FUN_00006b00(DAT_000098c0,0x40100000,1);
      if (iVar2 == 0) {
        iVar2 = FUN_00006cb4(uVar1,&local_4c,0x40100000,0x44);
      }
    }
  }
  return iVar2;
}
```

#### Function `FUN_00001bf0` @ `00001bf0`

Site `00001bfa`:

```asm
00001be8: adds r1,#0x4
00001bea: strb r2,[r1,r3]
00001bec: b 0x00001b86
00001bf0: movw r3,#0x4290
00001bf4: push {r4,lr}
00001bf6: movt r3,#0x2000
00001bfa: ldrb r3,[r3,#0x0]
00001bfc: sub sp,#0x8
00001bfe: cmp r3,#0x0
00001c00: beq 0x00001c7a
00001c02: movw r3,#0x400
00001c06: movw r2,#0xbeef
00001c0a: movt r3,#0x4010
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_00001bf0(void)

{
  undefined4 uVar1;
  int iVar2;
  undefined4 local_10;
  undefined4 local_c;
  
  if (DAT_20004290 == '\0') {
    iVar2 = 0x21;
  }
  else if ((_DAT_40100400 == -0x21524111) && (_DAT_40100404 == 1)) {
    iVar2 = 0;
    DAT_20004080 = DAT_40100406;
  }
  else {
    FUN_00001e50();
    uVar1 = DAT_000098c0;
    local_10 = 0xdeadbeef;
    local_c = 0x420001;
    iVar2 = FUN_00006b00(DAT_000098c0,&DAT_40100400,1);
    if ((iVar2 == 0) && (iVar2 = FUN_00006cb4(uVar1,&local_10,&DAT_40100400,8), iVar2 == 0)) {
      DAT_20004080 = 0x42;
    }
  }
  return iVar2;
}
```

#### Function `FUN_00001c8c` @ `00001c8c`

Site `00001c96`:

```asm
00001c86: strb r0,[r3,#0x0]
00001c88: movs r0,#0x0
00001c8a: b 0x00001c52
00001c8c: movw r3,#0x4290
00001c90: push {r4,r5,lr}
00001c92: movt r3,#0x2000
00001c96: ldrb r3,[r3,#0x0]
00001c98: movs r4,r0
00001c9a: sub sp,#0xc
00001c9c: cmp r3,#0x0
00001c9e: beq 0x00001cf8
00001ca0: movw r3,#0xbeef
00001ca4: movt r3,#0xdead
```

```c

int FUN_00001c8c(undefined1 param_1)

{
  undefined4 uVar1;
  int iVar2;
  undefined4 local_18;
  undefined2 local_14;
  undefined1 local_12;
  undefined1 local_11;
  
  uVar1 = DAT_000098c0;
  if (DAT_20004290 == '\0') {
    iVar2 = 0x21;
  }
  else {
    local_18 = 0xdeadbeef;
    local_14 = 1;
    local_11 = 0;
    local_12 = param_1;
    iVar2 = FUN_00006b00(DAT_000098c0,&DAT_40100400,1);
    if ((iVar2 == 0) && (iVar2 = FUN_00006cb4(uVar1,&local_18,&DAT_40100400,8), iVar2 == 0)) {
      DAT_20004080 = param_1;
    }
  }
  return iVar2;
}
```

#### Function `FUN_00001cfc` @ `00001cfc`

Site `00001d04`:

```asm
00001cf4: strb r4,[r3,#0x0]
00001cf6: b 0x00001cd2
00001cf8: movs r0,#0x21
00001cfa: b 0x00001cd2
00001cfc: movw r3,#0x4290
00001d00: movt r3,#0x2000
00001d04: ldrb r3,[r3,#0x0]
00001d06: push {r4,lr}
00001d08: cbz r3,0x00001d22
00001d0a: cbz r0,0x00001d1e
00001d0c: movw r1,#0x400
00001d10: movs r2,#0x8
00001d12: movt r1,#0x4010
```

```c

undefined4 FUN_00001cfc(int param_1)

{
  undefined4 uVar1;
  
  if (DAT_20004290 == '\0') {
    uVar1 = 0x21;
  }
  else if (param_1 == 0) {
    uVar1 = 1;
  }
  else {
    FUN_0000a578(param_1,&DAT_40100400,8);
    uVar1 = 0;
  }
  return uVar1;
}
```

### `20004320`

- from `000020fa` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `000021e4` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `00002138` in `FUN_000020a4` @ `000020a4` type=READ
- from `000021c6` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `000021b8` in `FUN_000020a4` @ `000020a4` type=WRITE

#### Function `FUN_000020a4` @ `000020a4`

Site `000020fa`:

```asm
000020e6: bne 0x000020c8
000020e8: movw r2,#0x4320
000020ec: movw r8,#0x429c
000020f0: movs r1,#0x1
000020f2: movt r2,#0x2000
000020f6: movt r8,#0x2000
000020fa: strb r1,[r2,#0x0]
000020fc: mov r2,r8
000020fe: strb r1,[r5,#0x0]
00002100: strb r3,[r2,#0x0]
00002102: bl 0x00001e50
00002106: movw r3,#0x4294
0000210a: movt r3,#0x2000
```

Site `000021e4`:

```asm
000021d4: strb r3,[r2,#0x0]
000021d6: b 0x000020c8
000021d8: movw r3,#0x4320
000021dc: movs r2,#0x1
000021de: movt r3,#0x2000
000021e2: strb r2,[r5,#0x0]
000021e4: strb r2,[r3,#0x0]
000021e6: b 0x000021c8
000021e8: movw r2,#0x95f8
000021ec: movt r2,#0x0
000021f0: b 0x0000211a
00002288: push {r4,r5,r6,r7,lr}
0000228a: mov r5,r8
```

Site `00002138`:

```asm
0000212a: bl 0x00001d54
0000212e: cmp r0,#0x0
00002130: bne 0x000020d0
00002132: pop {r7}
00002134: mov r8,r7
00002136: pop {r4,r5,r6,r7,pc}
00002138: ldrb r2,[r6,#0x0]
0000213a: ldr r1,[r7,#0x0]
0000213c: ldrb r1,[r1,r2]
0000213e: cmp r1,r0
00002140: beq 0x000021aa
00002142: cmp r0,#0xf0
00002144: beq 0x000021c6
```

Site `000021c6`:

```asm
000021ba: cmp r3,r2
000021bc: bls 0x000021c0
000021be: b 0x000020c8
000021c0: movs r3,#0x2
000021c2: strb r3,[r5,#0x0]
000021c4: b 0x000020c8
000021c6: strb r3,[r6,#0x0]
000021c8: movw r8,#0x429c
000021cc: movt r8,#0x2000
000021d0: movs r3,#0x0
000021d2: mov r2,r8
000021d4: strb r3,[r2,#0x0]
000021d6: b 0x000020c8
```

Site `000021b8`:

```asm
000021a8: b 0x000020c8
000021aa: movw r3,#0x4292
000021ae: movt r3,#0x2000
000021b2: adds r2,#0x1
000021b4: ldrb r3,[r3,#0x0]
000021b6: uxtb r2,r2
000021b8: strb r2,[r6,#0x0]
000021ba: cmp r3,r2
000021bc: bls 0x000021c0
000021be: b 0x000020c8
000021c0: movs r3,#0x2
000021c2: strb r3,[r5,#0x0]
000021c4: b 0x000020c8
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_000020a4(void)

{
  byte bVar1;
  undefined4 uVar2;
  int iVar3;
  uint uVar4;
  uint uVar5;
  
  uVar2 = FUN_00003ab8();
LAB_000020c8:
  iVar3 = FUN_00001d54(uVar2);
  do {
    if (iVar3 == 0) {
      return;
    }
    uVar4 = FUN_00001d94(uVar2);
    bVar1 = DAT_20004321;
    if (DAT_20004321 == 1) {
      if (*(byte *)(_DAT_20004294 + (uint)DAT_20004320) == uVar4) {
        uVar4 = DAT_20004320 + 1;
        DAT_20004320 = (byte)uVar4;
        if ((uint)DAT_20004292 <= (uVar4 & 0xff)) {
          DAT_20004321 = 2;
        }
      }
      else if (uVar4 == 0xf0) {
LAB_000021c8:
        DAT_2000429c = 0;
        DAT_20004320 = DAT_20004321;
      }
      else {
LAB_00002146:
        DAT_20004321 = 0;
      }
      goto LAB_000020c8;
    }
    if (DAT_20004321 == 2) {
      if (uVar4 == 0xf7) {
        if (_DAT_20004298 != (code *)0x0) {
          (*_DAT_20004298)(0x200042a0,DAT_2000429c);
        }
      }
      else {
        if (uVar4 == 0xf0) {
          DAT_20004321 = 1;
          goto LAB_000021c8;
        }
        if ((-1 < (int)(uVar4 << 0x18)) && (uVar5 = (uint)DAT_2000429c, -1 < (char)DAT_2000429c)) {
          DAT_2000429c = DAT_2000429c + 1;
          *(char *)(uVar5 + 0x200042a0) = (char)uVar4;
          goto LAB_000020c8;
        }
      }
      DAT_20004321 = 0;
      DAT_2000429c = 0;
      goto LAB_000020c8;
    }
    if (DAT_20004321 != 0) goto LAB_00002146;
    if (uVar4 != 0xf0) goto LAB_000020c8;
    DAT_20004320 = 1;
    DAT_20004321 = 1;
    DAT_2000429c = bVar1;
    iVar3 = FUN_00001e50();
    if (iVar3 == 0) {
      _DAT_20004294 = 0x95f4;
    }
    else {
      _DAT_20004294 = 0x95f8;
    }
    DAT_20004292 = 4;
    iVar3 = FUN_00001d54(uVar2);
  } while( true );
}
```

