# Motion 32 Native Command Effects Probe

## Focus Functions

### `00001e5c` `FUN_00001e5c`

```c

void FUN_00001e5c(void)

{
  undefined1 local_9;
  
  FUN_00005df4(0x20005cbc,0x204,&local_9);
  DAT_20004291 = local_9;
  FUN_00003a14(9);
  FUN_00003f88();
  FUN_0000a058();
  FUN_00005f2c(0x20005d04,&LAB_00009818);
  FUN_00005f14(0x20005d04);
  FUN_000026f4();
  do {
    FUN_000027d4();
  } while( true );
}
```

Callers:
- none

### `00001e50` `FUN_00001e50`

```c

undefined1 FUN_00001e50(void)

{
  return DAT_20004291;
}
```

Callers:
- `FUN_000098c4` @ `000098c4` from `000098c6` type=UNCONDITIONAL_CALL
- `FUN_000098e4` @ `000098e4` from `000098e6` type=UNCONDITIONAL_CALL
- `FUN_00009904` @ `00009904` from `00009906` type=UNCONDITIONAL_CALL
- `FUN_00009924` @ `00009924` from `00009926` type=UNCONDITIONAL_CALL
- `FUN_000026f4` @ `000026f4` from `000026f6` type=UNCONDITIONAL_CALL
- `FUN_00001bf0` @ `00001bf0` from `00001c20` type=UNCONDITIONAL_CALL
- `FUN_000028d0` @ `000028d0` from `000028e4` type=UNCONDITIONAL_CALL
- `FUN_00002b08` @ `00002b08` from `00002b1c` type=UNCONDITIONAL_CALL
- `FUN_000030cc` @ `000030cc` from `000030de` type=UNCONDITIONAL_CALL
- `FUN_00003370` @ `00003370` from `00003376` type=UNCONDITIONAL_CALL
- `FUN_000020a4` @ `000020a4` from `00002102` type=UNCONDITIONAL_CALL
- `FUN_00009944` @ `00009944` from `00009b3c` type=UNCONDITIONAL_CALL
- `FUN_00009944` @ `00009944` from `00009b7c` type=UNCONDITIONAL_CALL
- `FUN_00002030` @ `00002030` from `00002036` type=UNCONDITIONAL_CALL
- `FUN_0000234c` @ `0000234c` from `00002386` type=UNCONDITIONAL_CALL
- `FUN_0000234c` @ `0000234c` from `000023a8` type=UNCONDITIONAL_CALL
- `FUN_0000240c` @ `0000240c` from `000024f8` type=UNCONDITIONAL_CALL
- `FUN_0000240c` @ `0000240c` from `00002514` type=UNCONDITIONAL_CALL
- `FUN_0000240c` @ `0000240c` from `00002534` type=UNCONDITIONAL_CALL
- `FUN_0000240c` @ `0000240c` from `00002554` type=UNCONDITIONAL_CALL
- `FUN_0000240c` @ `0000240c` from `00002574` type=UNCONDITIONAL_CALL
- `FUN_0000240c` @ `0000240c` from `0000259a` type=UNCONDITIONAL_CALL
- `FUN_0000240c` @ `0000240c` from `000025ba` type=UNCONDITIONAL_CALL
- `FUN_0000240c` @ `0000240c` from `000025da` type=UNCONDITIONAL_CALL
- `FUN_0000240c` @ `0000240c` from `000025f8` type=UNCONDITIONAL_CALL
- `FUN_00009e1c` @ `00009e1c` from `00009efe` type=UNCONDITIONAL_CALL

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
- `FUN_00001e5c` @ `00001e5c` from `00001e84` type=UNCONDITIONAL_CALL

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

### `00003ab8` `FUN_00003ab8`

```c

undefined4 FUN_00003ab8(void)

{
  return 0x200040a0;
}
```

Callers:
- `FUN_000020a4` @ `000020a4` from `000020aa` type=UNCONDITIONAL_CALL

### `00005df4` `FUN_00005df4`

```c

undefined4 FUN_00005df4(undefined4 param_1,uint param_2,undefined1 *param_3)

{
  *param_3 = (char)((*(uint *)(&DAT_40040800 + ((param_2 >> 8) * 0x10 + (param_2 & 0xff)) * 4) & 3)
                   >> 1);
  return 0;
}
```

Callers:
- `FUN_00001e5c` @ `00001e5c` from `00001e72` type=UNCONDITIONAL_CALL
- `FUN_000026f4` @ `000026f4` from `0000273a` type=UNCONDITIONAL_CALL

### `00005f2c` `FUN_00005f2c`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_00005f2c(undefined4 *param_1,char *param_2)

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
  *puVar8 = 0xa500;
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
  FUN_00005f20((int)param_2[0x12],param_2[0x11],param_1);
  FUN_00005f20((int)*(char *)(iVar9 + 0x24),*(undefined1 *)(iVar9 + 0x22),param_1);
  FUN_00005f20((int)*(char *)(iVar9 + 0x25),*(undefined1 *)(iVar9 + 0x23),param_1);
  *param_1 = 0x475054;
  return 0;
}
```

Callers:
- `FUN_00001e5c` @ `00001e5c` from `00001ea0` type=UNCONDITIONAL_CALL

### `00005f14` `FUN_00005f14`

```c

undefined4 FUN_00005f14(int param_1)

{
  *(undefined4 *)(*(int *)(param_1 + 8) + 4) = *(undefined4 *)(param_1 + 0xc);
  return 0;
}
```

Callers:
- `FUN_00001e5c` @ `00001e5c` from `00001eac` type=UNCONDITIONAL_CALL

### `00005854` `FUN_00005854`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_00005854(undefined1 *param_1,byte *param_2)

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
  FUN_000095dc(iVar10);
  FUN_000094f4(iVar10);
  FUN_0000954c(iVar10,bVar3,param_1);
  iVar10 = (int)(char)param_2[5];
  bVar3 = param_2[4];
  FUN_000095dc(iVar10);
  FUN_000094f4(iVar10);
  FUN_0000954c(iVar10,bVar3,param_1);
  iVar10 = (int)(char)param_2[7];
  bVar3 = param_2[6];
  FUN_000095dc(iVar10);
  FUN_000094f4(iVar10);
  FUN_0000954c(iVar10,bVar3,param_1);
  iVar10 = (int)(char)param_2[9];
  bVar3 = param_2[8];
  FUN_000095dc(iVar10);
  FUN_000094f4(iVar10);
  FUN_0000954c(iVar10,bVar3,param_1);
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
    *(short *)(pbVar9 + 0x14) = (short)DAT_00005ab8;
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
  FUN_00009598((int)*(char *)(*(int *)(param_1 + 0x1c) + 5));
  FUN_00009598((int)*(char *)(*(int *)(param_1 + 0x1c) + 0xb));
  FUN_00009598((int)*(char *)(*(int *)(param_1 + 0x1c) + 7));
  FUN_00009598((int)*(char *)(*(int *)(param_1 + 0x1c) + 9));
  *(byte *)(*(int *)(param_1 + 0x20) + 2) = bVar3 & 3 | 0x70;
  *(undefined2 *)(param_1 + 8) = *(undefined2 *)(pbVar12 + 10);
  *(undefined4 *)(param_1 + 4) = 0x53434955;
  return 0;
}
```

Callers:
- `FUN_00003a14` @ `00003a14` from `00003a44` type=UNCONDITIONAL_CALL
- `FUN_00003a14` @ `00003a14` from `00003a5a` type=UNCONDITIONAL_CALL

### `0000657c` `FUN_0000657c`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_0000657c(undefined4 *param_1,char *param_2)

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
    FUN_00009600((int)param_2[0x11],param_2[0x10],param_1);
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
    FUN_00006138(6,uVar3);
  }
  _DAT_407effb0 = (short)DAT_00006800;
  FUN_00006138(6,uVar3);
  _DAT_407ec180 = 0xa5;
  DAT_407ec100 = 0x10;
  FUN_00006138(3,param_1[2]);
  if (*(char *)param_1[1] != '\0') {
    FUN_00009598((int)((char *)param_1[1])[0x11]);
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
  FUN_00006138(0x10,param_1[2]);
  _DAT_407effb0 = (short)DAT_00006804;
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

Callers:
- `FUN_000019c0` @ `000019c0` from `000019cc` type=UNCONDITIONAL_CALL

### `000097e4` `PROBE_000097e4`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_000097e4(undefined4 param_1,uint param_2,undefined4 param_3,int param_4)

{
  bool bVar1;
  code *pcVar2;
  int iVar3;
  int *unaff_r5;
  undefined4 *puVar4;
  undefined2 unaff_r6;
  
  *(undefined4 *)(param_4 + 8) = param_3;
  bVar1 = (bool)isCurrentModePrivileged();
  if (bVar1) {
    enableIRQinterrupts((param_2 & 1) == 1);
  }
  FUN_000096b4(1,param_2,param_3,*(undefined4 *)(param_4 + 8));
  FUN_00001ebc(1);
  _DAT_40000d00 = (undefined2)DAT_000098a0;
  _DAT_40000d0c = *unaff_r5;
  _DAT_40000d08 = _DAT_40000d0c + DAT_000098a4;
  _DAT_40006120 = 0x1000;
  _DAT_40000d04 = unaff_r6;
  FUN_0000a568(0x20004120,0,0x23c0);
  FUN_0000a578(&DAT_20004080,0x9e78,0x88);
  puVar4 = (undefined4 *)&DAT_20004100;
  iVar3 = 0;
  do {
    pcVar2 = (code *)*puVar4;
    puVar4 = puVar4 + 1;
    iVar3 = iVar3 + 1;
    (*pcVar2)();
  } while (iVar3 < 1);
  FUN_00009304();
  FUN_0000942c();
  FUN_00001ebc(2);
  func_0x0000968c();
  FUN_0000943c(0);
  return;
}
```

Callers:
- `FUN_00003a14` @ `00003a14` from `00003a52` type=PARAM

### `00009818` `PROBE_000097e4`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_000097e4(undefined4 param_1,uint param_2,undefined4 param_3,int param_4)

{
  bool bVar1;
  code *pcVar2;
  int iVar3;
  int *unaff_r5;
  undefined4 *puVar4;
  undefined2 unaff_r6;
  
  *(undefined4 *)(param_4 + 8) = param_3;
  bVar1 = (bool)isCurrentModePrivileged();
  if (bVar1) {
    enableIRQinterrupts((param_2 & 1) == 1);
  }
  FUN_000096b4(1,param_2,param_3,*(undefined4 *)(param_4 + 8));
  FUN_00001ebc(1);
  _DAT_40000d00 = (undefined2)DAT_000098a0;
  _DAT_40000d0c = *unaff_r5;
  _DAT_40000d08 = _DAT_40000d0c + DAT_000098a4;
  _DAT_40006120 = 0x1000;
  _DAT_40000d04 = unaff_r6;
  FUN_0000a568(0x20004120,0,0x23c0);
  FUN_0000a578(&DAT_20004080,0x9e78,0x88);
  puVar4 = (undefined4 *)&DAT_20004100;
  iVar3 = 0;
  do {
    pcVar2 = (code *)*puVar4;
    puVar4 = puVar4 + 1;
    iVar3 = iVar3 + 1;
    (*pcVar2)();
  } while (iVar3 < 1);
  FUN_00009304();
  FUN_0000942c();
  FUN_00001ebc(2);
  func_0x0000968c();
  FUN_0000943c(0);
  return;
}
```

Callers:
- `FUN_00001e5c` @ `00001e5c` from `00001e98` type=PARAM

### `00009874` `PROBE_000097e4`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_000097e4(undefined4 param_1,uint param_2,undefined4 param_3,int param_4)

{
  bool bVar1;
  code *pcVar2;
  int iVar3;
  int *unaff_r5;
  undefined4 *puVar4;
  undefined2 unaff_r6;
  
  *(undefined4 *)(param_4 + 8) = param_3;
  bVar1 = (bool)isCurrentModePrivileged();
  if (bVar1) {
    enableIRQinterrupts((param_2 & 1) == 1);
  }
  FUN_000096b4(1,param_2,param_3,*(undefined4 *)(param_4 + 8));
  FUN_00001ebc(1);
  _DAT_40000d00 = (undefined2)DAT_000098a0;
  _DAT_40000d0c = *unaff_r5;
  _DAT_40000d08 = _DAT_40000d0c + DAT_000098a4;
  _DAT_40006120 = 0x1000;
  _DAT_40000d04 = unaff_r6;
  FUN_0000a568(0x20004120,0,0x23c0);
  FUN_0000a578(&DAT_20004080,0x9e78,0x88);
  puVar4 = (undefined4 *)&DAT_20004100;
  iVar3 = 0;
  do {
    pcVar2 = (code *)*puVar4;
    puVar4 = puVar4 + 1;
    iVar3 = iVar3 + 1;
    (*pcVar2)();
  } while (iVar3 < 1);
  FUN_00009304();
  FUN_0000942c();
  FUN_00001ebc(2);
  func_0x0000968c();
  FUN_0000943c(0);
  return;
}
```

Callers:
- `FUN_00003a14` @ `00003a14` from `00003a3c` type=PARAM
- `PROBE_000097e4` @ `000097e4` from `0000987c` type=CONDITIONAL_JUMP

### `000098c4` `FUN_000098c4`

```c

undefined4 FUN_000098c4(void)

{
  int iVar1;
  undefined4 uVar2;
  
  iVar1 = FUN_00001e50();
  if (iVar1 == 1) {
    uVar2 = 0x9e38;
  }
  else {
    uVar2 = 0x9dfc;
  }
  return uVar2;
}
```

Callers:
- `FUN_000014e4` @ `000014e4` from `000014ea` type=UNCONDITIONAL_CALL
- `FUN_000019c0` @ `000019c0` from `000019ca` type=READ

### `000098c8` `FUN_000098c4`

```c

undefined4 FUN_000098c4(void)

{
  int iVar1;
  undefined4 uVar2;
  
  iVar1 = FUN_00001e50();
  if (iVar1 == 1) {
    uVar2 = 0x9e38;
  }
  else {
    uVar2 = 0x9dfc;
  }
  return uVar2;
}
```

Callers:
- none

### `000020a4` `FUN_000020a4`

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

Callers:
- none

### `00002098` `FUN_00002098`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00002098(undefined4 param_1)

{
  _DAT_20004298 = param_1;
  return;
}
```

Callers:
- `FUN_00003f88` @ `00003f88` from `00003f92` type=UNCONDITIONAL_CALL

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

### `000026f4` `FUN_000026f4`

```c

void FUN_000026f4(void)

{
  int iVar1;
  undefined4 in_r3;
  undefined1 *puVar2;
  byte *pbVar3;
  undefined2 *puVar4;
  
  iVar1 = FUN_00001e50();
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
  puVar4 = (undefined2 *)0x95fc;
  pbVar3 = DAT_0000279c;
  do {
    FUN_00005df4(0x20005cbc,*puVar4,pbVar3,puVar2,in_r3);
    iVar1 = iVar1 + 1;
    *(ushort *)(pbVar3 + 2) = (ushort)*pbVar3;
    puVar2 = (undefined1 *)(uint)DAT_200045cc;
    puVar4 = puVar4 + 2;
    pbVar3 = pbVar3 + 0x10;
  } while (iVar1 < (int)puVar2);
  FUN_000027a0(0x200045e0,&DAT_00001201);
  FUN_00002834(500,0,0x200045e0);
  FUN_000027a0(0x200045d0,&DAT_000011f5);
  FUN_000027ac(0x200045d0);
  return;
}
```

Callers:
- `FUN_00001e5c` @ `00001e5c` from `00001eb0` type=UNCONDITIONAL_CALL

### `0000240c` `FUN_0000240c`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0000240c(void)

{
  int iVar1;
  int iVar2;
  
  if (DAT_200045cc != 0) {
    if (_DAT_20004538 != _DAT_2000453c) {
      iVar2 = (int)(char)((char)_DAT_20004538 - (char)_DAT_2000453c);
      _DAT_2000453c = _DAT_20004538;
      if (iVar2 != 0) {
        iVar1 = FUN_00001e50();
        FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x9664),iVar2);
      }
    }
    if (1 < DAT_200045cc) {
      if (_DAT_20004548 != _DAT_2000454c) {
        iVar2 = (int)(char)((char)_DAT_20004548 - (char)_DAT_2000454c);
        _DAT_2000454c = _DAT_20004548;
        if (iVar2 != 0) {
          iVar1 = FUN_00001e50();
          FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x9665),iVar2);
        }
      }
      if (2 < DAT_200045cc) {
        if (_DAT_20004558 != _DAT_2000455c) {
          iVar2 = (int)(char)((char)_DAT_20004558 - (char)_DAT_2000455c);
          _DAT_2000455c = _DAT_20004558;
          if (iVar2 != 0) {
            iVar1 = FUN_00001e50();
            FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x9666),iVar2);
          }
        }
        if (3 < DAT_200045cc) {
          if (_DAT_20004568 != _DAT_2000456c) {
            iVar2 = (int)(char)((char)_DAT_20004568 - (char)_DAT_2000456c);
            _DAT_2000456c = _DAT_20004568;
            if (iVar2 != 0) {
              iVar1 = FUN_00001e50();
              FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x9667),iVar2);
            }
          }
          if (4 < DAT_200045cc) {
            if (_DAT_20004578 != _DAT_2000457c) {
              iVar2 = (int)(char)((char)_DAT_20004578 - (char)_DAT_2000457c);
              _DAT_2000457c = _DAT_20004578;
              if (iVar2 != 0) {
                iVar1 = FUN_00001e50();
                FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x9668),iVar2);
              }
            }
            if (5 < DAT_200045cc) {
              if ((_DAT_20004588 != _DAT_2000458c) &&
                 (iVar2 = (int)(char)((char)_DAT_20004588 - (char)_DAT_2000458c),
                 _DAT_2000458c = _DAT_20004588, iVar2 != 0)) {
                iVar1 = FUN_00001e50();
                FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x9669),iVar2);
              }
              if (6 < DAT_200045cc) {
                if (_DAT_20004598 != _DAT_2000459c) {
                  iVar2 = (int)(char)((char)_DAT_20004598 - (char)_DAT_2000459c);
                  _DAT_2000459c = _DAT_20004598;
                  if (iVar2 != 0) {
                    iVar1 = FUN_00001e50();
                    FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x966a),iVar2);
                  }
                }
                if (7 < DAT_200045cc) {
                  if (_DAT_200045a8 != _DAT_200045ac) {
                    iVar2 = (int)(char)((char)_DAT_200045a8 - (char)_DAT_200045ac);
                    _DAT_200045ac = _DAT_200045a8;
                    if (iVar2 != 0) {
                      iVar1 = FUN_00001e50();
                      FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x966b),iVar2);
                    }
                  }
                  if ((8 < DAT_200045cc) && (_DAT_200045b8 != _DAT_200045bc)) {
                    iVar2 = (int)(char)((char)_DAT_200045b8 - (char)_DAT_200045bc);
                    _DAT_200045bc = _DAT_200045b8;
                    if (iVar2 != 0) {
                      iVar1 = FUN_00001e50();
                      FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x966c),iVar2);
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

Callers:
- `FUN_00009944` @ `00009944` from `00009aa2` type=UNCONDITIONAL_CALL
- `FUN_00009e1c` @ `00009e1c` from `00009f56` type=UNCONDITIONAL_CALL

### `000027d4` `FUN_000027d4`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_000027d4(void)

{
  int iVar1;
  
  for (iVar1 = _DAT_200045fc; iVar1 != 0; iVar1 = *(int *)(iVar1 + 8)) {
    (**(code **)(iVar1 + 0xc))();
  }
  return;
}
```

Callers:
- `FUN_00001e5c` @ `00001e5c` from `00001eb4` type=UNCONDITIONAL_CALL

### `000019c0` `FUN_000019c0`

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

Callers:
- `FUN_0000a058` @ `0000a058` from `0000a05e` type=UNCONDITIONAL_CALL

### `000019e8` `FUN_000019e8`

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

Callers:
- `FUN_0000a058` @ `0000a058` from `0000a072` type=UNCONDITIONAL_CALL

### `00001b30` `FUN_00001b30`

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

Callers:
- `FUN_00009944` @ `00009944` from `00009c7c` type=UNCONDITIONAL_CALL
- `FUN_00009944` @ `00009944` from `00009ca4` type=UNCONDITIONAL_CALL

### `00001bf0` `FUN_00001bf0`

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

Callers:
- `FUN_0000a058` @ `0000a058` from `0000a076` type=UNCONDITIONAL_CALL

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
- `FUN_00009944` @ `00009944` from `00009d20` type=UNCONDITIONAL_CALL

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
- `FUN_00009944` @ `00009944` from `00009bfa` type=UNCONDITIONAL_CALL

## Address References

### `20004291`

- from `00001e82` in `FUN_00001e5c` @ `00001e5c` type=WRITE
- from `00001e7c` in `FUN_00001e5c` @ `00001e5c` type=PARAM
- from `00001e58` in `FUN_00001e50` @ `00001e50` type=READ

#### `FUN_00001e5c` @ `00001e5c`

Site `00001e82`:

```asm
00001e68: movw r1,#0x204
00001e6c: movs r2,r4
00001e6e: movt r0,#0x2000
00001e72: bl 0x00005df4
00001e76: movw r3,#0x4291
00001e7a: ldrb r2,[r4,#0x0]
00001e7c: movt r3,#0x2000
00001e80: movs r0,#0x9
00001e82: strb r2,[r3,#0x0]
00001e84: bl 0x00003a14
00001e88: bl 0x00003f88
00001e8c: bl 0x0000a058
00001e90: movw r1,#0x9818
00001e94: movw r0,#0x5d04
00001e98: movt r1,#0x0
00001e9c: movt r0,#0x2000
00001ea0: bl 0x00005f2c
```

Site `00001e7c`:

```asm
00001e62: movw r0,#0x5cbc
00001e66: adds r4,r3,#0x7
00001e68: movw r1,#0x204
00001e6c: movs r2,r4
00001e6e: movt r0,#0x2000
00001e72: bl 0x00005df4
00001e76: movw r3,#0x4291
00001e7a: ldrb r2,[r4,#0x0]
00001e7c: movt r3,#0x2000
00001e80: movs r0,#0x9
00001e82: strb r2,[r3,#0x0]
00001e84: bl 0x00003a14
00001e88: bl 0x00003f88
00001e8c: bl 0x0000a058
00001e90: movw r1,#0x9818
00001e94: movw r0,#0x5d04
00001e98: movt r1,#0x0
```

#### `FUN_00001e50` @ `00001e50`

Site `00001e58`:

```asm
00001e44: bne 0x00001e24
00001e46: b 0x00001e14
00001e48: movs r0,r2
00001e4a: b 0x00001e14
00001e4c: movs r0,#0x0
00001e4e: b 0x00001e14
00001e50: movw r3,#0x4291
00001e54: movt r3,#0x2000
00001e58: ldrb r0,[r3,#0x0]
00001e5a: bx lr
00001e5c: push {r4,lr}
00001e5e: sub sp,#0x8
00001e60: mov r3,sp
00001e62: movw r0,#0x5cbc
00001e66: adds r4,r3,#0x7
00001e68: movw r1,#0x204
00001e6c: movs r2,r4
```

### `20004292`

- from `00002128` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `00002122` in `FUN_000020a4` @ `000020a4` type=PARAM
- from `000021b4` in `FUN_000020a4` @ `000020a4` type=READ

#### `FUN_000020a4` @ `000020a4`

Site `00002128`:

```asm
00002110: bne 0x000021e8
00002112: movw r2,#0x95f4
00002116: movt r2,#0x0
0000211a: str r2,[r3,#0x0]
0000211c: movw r3,#0x4292
00002120: movs r2,#0x4
00002122: movt r3,#0x2000
00002126: movs r0,r4
00002128: strb r2,[r3,#0x0]
0000212a: bl 0x00001d54
0000212e: cmp r0,#0x0
00002130: bne 0x000020d0
00002132: pop {r7}
00002134: mov r8,r7
00002136: pop {r4,r5,r6,r7,pc}
00002138: ldrb r2,[r6,#0x0]
0000213a: ldr r1,[r7,#0x0]
```

Site `00002122`:

```asm
0000210a: movt r3,#0x2000
0000210e: cmp r0,#0x0
00002110: bne 0x000021e8
00002112: movw r2,#0x95f4
00002116: movt r2,#0x0
0000211a: str r2,[r3,#0x0]
0000211c: movw r3,#0x4292
00002120: movs r2,#0x4
00002122: movt r3,#0x2000
00002126: movs r0,r4
00002128: strb r2,[r3,#0x0]
0000212a: bl 0x00001d54
0000212e: cmp r0,#0x0
00002130: bne 0x000020d0
00002132: pop {r7}
00002134: mov r8,r7
00002136: pop {r4,r5,r6,r7,pc}
```

Site `000021b4`:

```asm
000021a0: movs r3,#0x0
000021a2: mov r2,r8
000021a4: strb r3,[r5,#0x0]
000021a6: strb r3,[r2,#0x0]
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

### `20004294`

- from `0000211a` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `0000213a` in `FUN_000020a4` @ `000020a4` type=READ

#### `FUN_000020a4` @ `000020a4`

Site `0000211a`:

```asm
00002100: strb r3,[r2,#0x0]
00002102: bl 0x00001e50
00002106: movw r3,#0x4294
0000210a: movt r3,#0x2000
0000210e: cmp r0,#0x0
00002110: bne 0x000021e8
00002112: movw r2,#0x95f4
00002116: movt r2,#0x0
0000211a: str r2,[r3,#0x0]
0000211c: movw r3,#0x4292
00002120: movs r2,#0x4
00002122: movt r3,#0x2000
00002126: movs r0,r4
00002128: strb r2,[r3,#0x0]
0000212a: bl 0x00001d54
0000212e: cmp r0,#0x0
00002130: bne 0x000020d0
```

Site `0000213a`:

```asm
00002128: strb r2,[r3,#0x0]
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
00002146: movs r3,#0x0
00002148: strb r3,[r5,#0x0]
0000214a: b 0x000020c8
```

### `20004298`

- from `000020a0` in `FUN_00002098` @ `00002098` type=WRITE
- from `0000218a` in `FUN_000020a4` @ `000020a4` type=READ

#### `FUN_00002098` @ `00002098`

Site `000020a0`:

```asm
00002084: movt r0,#0x2000
00002088: bl 0x00001d6c
0000208c: pop {r3,r4,r5,r6,r7,pc}
0000208e: movw r4,#0x95f8
00002092: movt r4,#0x0
00002096: b 0x00002044
00002098: movw r3,#0x4298
0000209c: movt r3,#0x2000
000020a0: str r0,[r3,#0x0]
000020a2: bx lr
000020a4: push {r4,r5,r6,r7,lr}
000020a6: mov lr,r8
000020a8: push {lr}
000020aa: bl 0x00003ab8
000020ae: movw r5,#0x4321
000020b2: movw r6,#0x4320
000020b6: movw r7,#0x4294
```

#### `FUN_000020a4` @ `000020a4`

Site `0000218a`:

```asm
00002170: strb r3,[r1,#0x0]
00002172: movw r3,#0x42a0
00002176: movt r3,#0x2000
0000217a: strb r0,[r3,r2]
0000217c: b 0x000020c8
0000217e: movw r3,#0x4298
00002182: movw r8,#0x429c
00002186: movt r3,#0x2000
0000218a: ldr r3,[r3,#0x0]
0000218c: movt r8,#0x2000
00002190: cbz r3,0x000021a0
00002192: mov r2,r8
00002194: movw r0,#0x42a0
00002198: ldrb r1,[r2,#0x0]
0000219a: movt r0,#0x2000
0000219e: blx r3
000021a0: movs r3,#0x0
```

### `20004084`

- no direct references found

### `200040a0`

- no direct references found

### `20004538`

- from `00002424` in `FUN_0000240c` @ `0000240c` type=READ

#### `FUN_0000240c` @ `0000240c`

Site `00002424`:

```asm
0000240c: push {r4,r5,r6,lr}
0000240e: movw r5,#0x45cc
00002412: movt r5,#0x2000
00002416: ldrb r3,[r5,#0x0]
00002418: cmp r3,#0x0
0000241a: beq 0x000024f6
0000241c: movw r4,#0x4538
00002420: movt r4,#0x2000
00002424: ldr r1,[r4,#0x0]
00002426: ldr r2,[r4,#0x4]
00002428: cmp r1,r2
0000242a: beq 0x00002436
0000242c: subs r2,r1,r2
0000242e: sxtb r6,r2
00002430: str r1,[r4,#0x4]
00002432: cmp r6,#0x0
00002434: bne 0x000024f8
```

### `200045ca`

- from `0000229e` in `FUN_00002288` @ `00002288` type=READ
- from `00002324` in `FUN_00002288` @ `00002288` type=READ
- from `000022de` in `FUN_00002288` @ `00002288` type=DATA
- from `00002348` in `FUN_00002288` @ `00002288` type=READ
- from `00002728` in `FUN_000026f4` @ `000026f4` type=WRITE
- from `00002722` in `FUN_000026f4` @ `000026f4` type=PARAM

#### `FUN_00002288` @ `00002288`

Site `0000229e`:

```asm
0000228a: mov r5,r8
0000228c: movw r8,#0x45ca
00002290: mov lr,r11
00002292: mov r7,r10
00002294: mov r6,r9
00002296: movt r8,#0x2000
0000229a: mov r3,r8
0000229c: push {r5,r6,r7,lr}
0000229e: ldrb r1,[r3,#0x0]
000022a0: sub sp,#0xc
000022a2: cmp r1,#0x0
000022a4: beq 0x00002328
000022a6: movw r3,#0x45c8
000022aa: movw r6,#0x4534
000022ae: movt r3,#0x2000
000022b2: movs r4,r0
000022b4: movs r5,#0x0
```

Site `00002324`:

```asm
00002312: bge 0x000022ca
00002314: ldrh r3,[r4,#0x0]
00002316: movs r0,r5
00002318: strh r3,[r6,#0x0]
0000231a: ldrh r1,[r4,#0x0]
0000231c: sxth r1,r1
0000231e: bl 0x00001eec
00002322: mov r3,r8
00002324: ldrb r1,[r3,#0x0]
00002326: b 0x000022d2
00002328: add sp,#0xc
0000232a: pop {r4,r5,r6,r7}
0000232c: mov r11,r7
0000232e: mov r10,r6
00002330: mov r9,r5
00002332: mov r8,r4
00002334: pop {r4,r5,r6,r7,pc}
```

Site `000022de`:

```asm
000022ce: cmp r3,#0x0
000022d0: bne 0x00002336
000022d2: ldr r3,[sp,#0x4]
000022d4: adds r5,#0x1
000022d6: adds r3,#0x1
000022d8: uxtb r5,r5
000022da: adds r4,#0x2
000022dc: adds r6,#0x2
000022de: str r3,[sp,#0x4]
000022e0: cmp r5,r1
000022e2: bcs 0x00002328
000022e4: ldrh r3,[r4,#0x0]
000022e6: sxth r3,r3
000022e8: cmp r3,#0xb
000022ea: ble 0x000022f6
000022ec: ldrh r3,[r4,#0x0]
000022ee: mov r0,r9
```

Site `00002348`:

```asm
00002336: ldrh r1,[r4,#0x0]
00002338: movs r0,r5
0000233a: sxth r1,r1
0000233c: bl 0x00001eec
00002340: mov r3,r11
00002342: ldr r2,[sp,#0x4]
00002344: strb r3,[r2,#0x0]
00002346: mov r3,r8
00002348: ldrb r1,[r3,#0x0]
0000234a: b 0x000022d2
0000234c: push {r3,r4,r5,r6,r7,lr}
0000234e: mov r7,r8
00002350: mov lr,r9
00002352: push {r7,lr}
00002354: movw r7,#0x4532
00002358: movt r7,#0x2000
0000235c: ldrh r3,[r7,#0x0]
```

#### `FUN_000026f4` @ `000026f4`

Site `00002728`:

```asm
00002710: movs r1,#0xb
00002712: movt r3,#0x2000
00002716: strb r1,[r3,#0x0]
00002718: movw r3,#0x45ca
0000271c: movw r5,#0x95fc
00002720: movs r6,#0x0
00002722: movt r3,#0x2000
00002726: ldr r4,[0x0000279c]
00002728: strb r2,[r3,#0x0]
0000272a: movt r5,#0x0
0000272e: movw r0,#0x5cbc
00002732: movs r2,r4
00002734: ldrh r1,[r5,#0x0]
00002736: movt r0,#0x2000
0000273a: bl 0x00005df4
0000273e: ldrb r3,[r4,#0x0]
00002740: adds r6,#0x1
```

Site `00002722`:

```asm
0000270a: strb r3,[r7,#0x0]
0000270c: movw r3,#0x45cb
00002710: movs r1,#0xb
00002712: movt r3,#0x2000
00002716: strb r1,[r3,#0x0]
00002718: movw r3,#0x45ca
0000271c: movw r5,#0x95fc
00002720: movs r6,#0x0
00002722: movt r3,#0x2000
00002726: ldr r4,[0x0000279c]
00002728: strb r2,[r3,#0x0]
0000272a: movt r5,#0x0
0000272e: movw r0,#0x5cbc
00002732: movs r2,r4
00002734: ldrh r1,[r5,#0x0]
00002736: movt r0,#0x2000
0000273a: bl 0x00005df4
```

### `200045cc`

- from `00002416` in `FUN_0000240c` @ `0000240c` type=READ
- from `00002570` in `FUN_0000240c` @ `0000240c` type=READ
- from `00002590` in `FUN_0000240c` @ `0000240c` type=READ
- from `00002614` in `FUN_0000240c` @ `0000240c` type=READ
- from `000025b6` in `FUN_0000240c` @ `0000240c` type=READ
- from `000025d6` in `FUN_0000240c` @ `0000240c` type=READ
- from `00002550` in `FUN_0000240c` @ `0000240c` type=READ
- from `00002530` in `FUN_0000240c` @ `0000240c` type=READ
- from `00002510` in `FUN_0000240c` @ `0000240c` type=READ
- from `0000270a` in `FUN_000026f4` @ `000026f4` type=WRITE
- from `00002744` in `FUN_000026f4` @ `000026f4` type=READ

#### `FUN_0000240c` @ `0000240c`

Site `00002416`:

```asm
000023fc: movw r3,#0x45c8
00002400: movs r2,#0x1
00002402: movt r3,#0x2000
00002406: strb r2,[r3,#0x0]
00002408: b 0x0000237c
0000240c: push {r4,r5,r6,lr}
0000240e: movw r5,#0x45cc
00002412: movt r5,#0x2000
00002416: ldrb r3,[r5,#0x0]
00002418: cmp r3,#0x0
0000241a: beq 0x000024f6
0000241c: movw r4,#0x4538
00002420: movt r4,#0x2000
00002424: ldr r1,[r4,#0x0]
00002426: ldr r2,[r4,#0x4]
00002428: cmp r1,r2
0000242a: beq 0x00002436
```

Site `00002570`:

```asm
0000255c: movt r2,#0x0
00002560: mov r12,r2
00002562: lsls r3,r0,#0x3
00002564: adds r3,r3,r0
00002566: add r3,r12
00002568: ldrb r0,[r3,#0x3]
0000256a: movs r1,r6
0000256c: bl 0x00001fb0
00002570: ldrb r3,[r5,#0x0]
00002572: b 0x0000247a
00002574: bl 0x00001e50
00002578: movw r2,#0x9664
0000257c: movt r2,#0x0
00002580: mov r12,r2
00002582: lsls r3,r0,#0x3
00002584: adds r3,r3,r0
00002586: add r3,r12
```

Site `00002590`:

```asm
0000257c: movt r2,#0x0
00002580: mov r12,r2
00002582: lsls r3,r0,#0x3
00002584: adds r3,r3,r0
00002586: add r3,r12
00002588: ldrb r0,[r3,#0x4]
0000258a: movs r1,r6
0000258c: bl 0x00001fb0
00002590: ldrb r3,[r5,#0x0]
00002592: cmp r3,#0x5
00002594: bls 0x00002598
00002596: b 0x00002496
00002598: b 0x000024f6
0000259a: bl 0x00001e50
0000259e: movw r2,#0x9664
000025a2: movt r2,#0x0
000025a6: mov r12,r2
```

Site `00002614`:

```asm
00002600: movt r2,#0x0
00002604: mov r12,r2
00002606: lsls r3,r0,#0x3
00002608: adds r3,r3,r0
0000260a: add r3,r12
0000260c: ldrb r0,[r3,#0x5]
0000260e: movs r1,r6
00002610: bl 0x00001fb0
00002614: ldrb r3,[r5,#0x0]
00002616: b 0x000024aa
00002618: movw r3,#0x4530
0000261c: push {r4,r5,r6,lr}
0000261e: movt r3,#0x2000
00002622: ldrh r1,[r0,#0x0]
00002624: ldrb r2,[r3,#0x0]
00002626: sxth r1,r1
00002628: cbz r2,0x0000266e
```

Site `000025b6`:

```asm
000025a2: movt r2,#0x0
000025a6: mov r12,r2
000025a8: lsls r3,r0,#0x3
000025aa: adds r3,r3,r0
000025ac: add r3,r12
000025ae: ldrb r0,[r3,#0x6]
000025b0: movs r1,r6
000025b2: bl 0x00001fb0
000025b6: ldrb r3,[r5,#0x0]
000025b8: b 0x000024c2
000025ba: bl 0x00001e50
000025be: movw r2,#0x9664
000025c2: movt r2,#0x0
000025c6: mov r12,r2
000025c8: lsls r3,r0,#0x3
000025ca: adds r3,r3,r0
000025cc: add r3,r12
```

Site `000025d6`:

```asm
000025c2: movt r2,#0x0
000025c6: mov r12,r2
000025c8: lsls r3,r0,#0x3
000025ca: adds r3,r3,r0
000025cc: add r3,r12
000025ce: ldrb r0,[r3,#0x7]
000025d0: movs r1,r6
000025d2: bl 0x00001fb0
000025d6: ldrb r3,[r5,#0x0]
000025d8: b 0x000024da
000025da: bl 0x00001e50
000025de: movw r2,#0x9664
000025e2: movt r2,#0x0
000025e6: mov r12,r2
000025e8: lsls r3,r0,#0x3
000025ea: adds r3,r3,r0
000025ec: add r3,r12
```

Site `00002550`:

```asm
0000253c: movt r2,#0x0
00002540: mov r12,r2
00002542: lsls r3,r0,#0x3
00002544: adds r3,r3,r0
00002546: add r3,r12
00002548: ldrb r0,[r3,#0x2]
0000254a: movs r1,r6
0000254c: bl 0x00001fb0
00002550: ldrb r3,[r5,#0x0]
00002552: b 0x00002462
00002554: bl 0x00001e50
00002558: movw r2,#0x9664
0000255c: movt r2,#0x0
00002560: mov r12,r2
00002562: lsls r3,r0,#0x3
00002564: adds r3,r3,r0
00002566: add r3,r12
```

Site `00002530`:

```asm
0000251c: movt r2,#0x0
00002520: mov r12,r2
00002522: lsls r3,r0,#0x3
00002524: adds r3,r3,r0
00002526: add r3,r12
00002528: ldrb r0,[r3,#0x1]
0000252a: movs r1,r6
0000252c: bl 0x00001fb0
00002530: ldrb r3,[r5,#0x0]
00002532: b 0x0000244c
00002534: bl 0x00001e50
00002538: movw r2,#0x9664
0000253c: movt r2,#0x0
00002540: mov r12,r2
00002542: lsls r3,r0,#0x3
00002544: adds r3,r3,r0
00002546: add r3,r12
```

Site `00002510`:

```asm
000024f8: bl 0x00001e50
000024fc: movw r3,#0x9664
00002500: lsls r2,r0,#0x3
00002502: movt r3,#0x0
00002506: adds r2,r2,r0
00002508: ldrb r0,[r2,r3]
0000250a: movs r1,r6
0000250c: bl 0x00001fb0
00002510: ldrb r3,[r5,#0x0]
00002512: b 0x00002436
00002514: bl 0x00001e50
00002518: movw r2,#0x9664
0000251c: movt r2,#0x0
00002520: mov r12,r2
00002522: lsls r3,r0,#0x3
00002524: adds r3,r3,r0
00002526: add r3,r12
```

#### `FUN_000026f4` @ `000026f4`

Site `0000270a`:

```asm
000026f4: push {r3,r4,r5,r6,r7,lr}
000026f6: bl 0x00001e50
000026fa: cmp r0,#0x0
000026fc: bne 0x00002796
000026fe: movs r3,#0x8
00002700: movs r2,#0x2
00002702: movw r7,#0x45cc
00002706: movt r7,#0x2000
0000270a: strb r3,[r7,#0x0]
0000270c: movw r3,#0x45cb
00002710: movs r1,#0xb
00002712: movt r3,#0x2000
00002716: strb r1,[r3,#0x0]
00002718: movw r3,#0x45ca
0000271c: movw r5,#0x95fc
00002720: movs r6,#0x0
00002722: movt r3,#0x2000
```

Site `00002744`:

```asm
0000272e: movw r0,#0x5cbc
00002732: movs r2,r4
00002734: ldrh r1,[r5,#0x0]
00002736: movt r0,#0x2000
0000273a: bl 0x00005df4
0000273e: ldrb r3,[r4,#0x0]
00002740: adds r6,#0x1
00002742: strh r3,[r4,#0x2]
00002744: ldrb r3,[r7,#0x0]
00002746: adds r5,#0x4
00002748: adds r4,#0x10
0000274a: cmp r6,r3
0000274c: blt 0x0000272e
0000274e: movw r1,#0x1201
00002752: movw r0,#0x45e0
00002756: movt r1,#0x0
0000275a: movt r0,#0x2000
```

### `20005cbc`

- no direct references found

### `20005cd4`

- no direct references found

### `20005d04`

- no direct references found

### `20005d24`

- no direct references found

### `000097e4`

- from `00003a52` in `FUN_00003a14` @ `00003a14` type=PARAM

#### `FUN_00003a14` @ `00003a14`

Site `00003a52`:

```asm
00003a34: movw r1,#0x9874
00003a38: movw r0,#0x5d24
00003a3c: movt r1,#0x0
00003a40: movt r0,#0x2000
00003a44: bl 0x00005854
00003a48: pop {r4,pc}
00003a4a: movw r1,#0x97e4
00003a4e: movw r0,#0x5cd4
00003a52: movt r1,#0x0
00003a56: movt r0,#0x2000
00003a5a: bl 0x00005854
00003a5e: b 0x00003a48
00003ab8: movw r0,#0x40a0
00003abc: movt r0,#0x2000
00003ac0: bx lr
00003ac4: push {r4,lr}
00003ac6: ldrb r3,[r0,#0x4]
```

### `00009818`

- from `00001e98` in `FUN_00001e5c` @ `00001e5c` type=PARAM

#### `FUN_00001e5c` @ `00001e5c`

Site `00001e98`:

```asm
00001e7c: movt r3,#0x2000
00001e80: movs r0,#0x9
00001e82: strb r2,[r3,#0x0]
00001e84: bl 0x00003a14
00001e88: bl 0x00003f88
00001e8c: bl 0x0000a058
00001e90: movw r1,#0x9818
00001e94: movw r0,#0x5d04
00001e98: movt r1,#0x0
00001e9c: movt r0,#0x2000
00001ea0: bl 0x00005f2c
00001ea4: movw r0,#0x5d04
00001ea8: movt r0,#0x2000
00001eac: bl 0x00005f14
00001eb0: bl 0x000026f4
00001eb4: bl 0x000027d4
00001eb8: b 0x00001eb4
```

### `00009874`

- from `00003a3c` in `FUN_00003a14` @ `00003a14` type=PARAM
- from `0000987c` in `PROBE_000097e4` @ `000097e4` type=CONDITIONAL_JUMP

#### `FUN_00003a14` @ `00003a14`

Site `00003a3c`:

```asm
00003a24: movw r3,#0x5b60
00003a28: movs r2,#0x1
00003a2a: movt r3,#0x2000
00003a2e: strb r2,[r3,#0x0]
00003a30: cmp r4,#0x1
00003a32: beq 0x00003a4a
00003a34: movw r1,#0x9874
00003a38: movw r0,#0x5d24
00003a3c: movt r1,#0x0
00003a40: movt r0,#0x2000
00003a44: bl 0x00005854
00003a48: pop {r4,pc}
00003a4a: movw r1,#0x97e4
00003a4e: movw r0,#0x5cd4
00003a52: movt r1,#0x0
00003a56: movt r0,#0x2000
00003a5a: bl 0x00005854
```

#### `PROBE_000097e4` @ `000097e4`

Site `0000987c`:

```asm
0000986c: asrs r6,r3,#0x2
0000986e: cmp r3,#0x0
00009870: ble 0x0000987e
00009872: movs r4,#0x0
00009874: ldmia r5!,{r3}
00009876: adds r4,#0x1
00009878: blx r3
0000987a: cmp r6,r4
0000987c: bgt 0x00009874
0000987e: bl 0x00009304
00009882: bl 0x0000942c
00009886: movs r0,#0x2
00009888: bl 0x00001ebc
0000988c: bl 0x0000968c
00009890: movs r0,#0x0
00009892: bl 0x0000943c
00009896: add sp,#0xc
```

### `000098c4`

- from `000014ea` in `FUN_000014e4` @ `000014e4` type=UNCONDITIONAL_CALL
- from `000019ca` in `FUN_000019c0` @ `000019c0` type=READ

#### `FUN_000014e4` @ `000014e4`

Site `000014ea`:

```asm
00001086: movs r0,r0
00001088: movs r0,r0
0000108a: movs r0,r0
0000108c: movs r0,r0
0000108e: movs r0,r0
000014e4: push {r4,r5,r6,r7,lr}
000014e6: mov lr,r8
000014e8: push {lr}
000014ea: bl 0x000098c4
000014ee: movs r4,r0
000014f0: bl 0x000098e4
000014f4: movw r5,#0x4254
000014f8: movs r7,r0
000014fa: bl 0x00009904
000014fe: movs r1,r4
00001500: movw r4,#0x4214
00001504: movt r5,#0x2000
```

#### `FUN_000019c0` @ `000019c0`

Site `000019ca`:

```asm
000019b0: movw r2,#0x413c
000019b4: lsls r3,r3,#0x1
000019b6: movt r2,#0x2000
000019ba: ldrh r0,[r3,r2]
000019bc: bx lr
000019c0: movw r3,#0x98c0
000019c4: movt r3,#0x0
000019c8: push {r4,lr}
000019ca: ldmia r3!,{r0,r1}
000019cc: bl 0x0000657c
000019d0: cbz r0,0x000019d8
000019d2: cmp r0,#0xe
000019d4: beq 0x000019d8
000019d6: pop {r4,pc}
000019d8: movw r3,#0x4290
000019dc: movs r2,#0x1
000019de: movt r3,#0x2000
```

### `000098c8`

- no direct references found

## Scalar/Immediate Hits

### `0x204`

- `00001e68: movw r1,#0x204` in `FUN_00001e5c` @ `00001e5c`

### `0x8f`

- `000216f2: movs r5,#0x8f` in `FUN_0002164c` @ `0002164c`
- `0003bba4: movs r2,#0x8f` in `FUN_0003bb58` @ `0003bb58`
- `0003e7b8: movs r3,#0x8f` in `FUN_0003e600` @ `0003e600`

### `0x7f`

- `00001ef2: movs r7,#0x7f` in `FUN_00001eec` @ `00001eec`
- `000040c6: movs r0,#0x7f` in `FUN_0000408c` @ `0000408c`
- `00005af4: movs r3,#0x7f` in `FUN_00005abc` @ `00005abc`
- `000069ee: movs r1,#0x7f` in `FUN_00006808` @ `00006808`
- `00006bfa: movs r1,#0x7f` in `FUN_00006b00` @ `00006b00`
- `00006d60: movw r12,#0x7f` in `FUN_00006cb4` @ `00006cb4`
- `000216f0: movs r3,#0x7f` in `FUN_0002164c` @ `0002164c`
- `00022bba: movs r3,#0x7f` in `FUN_00022b70` @ `00022b70`
- `00043834: movs r1,#0x7f` in `FUN_000437a8` @ `000437a8`
- `0004384a: movs r0,#0x7f` in `FUN_000437a8` @ `000437a8`
- `000439ea: movs r2,#0x7f` in `FUN_000437a8` @ `000437a8`
- `00043d58: movs r1,#0x7f` in `<none>` @ `<none>`
- `00043d70: movs r0,#0x7f` in `<none>` @ `<none>`
- `00043e02: movs r2,#0x7f` in `<none>` @ `<none>`
- `00048094: cmp r3,#0x7f` in `FUN_00047e7c` @ `00047e7c`
- `000480d4: cmp r3,#0x7f` in `FUN_00047e7c` @ `00047e7c`
- `0005065a: cmp r4,#0x7f` in `FUN_0005064c` @ `0005064c`
- `00050718: cmp r1,#0x7f` in `FUN_0005070c` @ `0005070c`
- `000509a2: cmp r3,#0x7f` in `FUN_00050978` @ `00050978`
- `00050d96: cmp r2,#0x7f` in `FUN_00050d0c` @ `00050d0c`
- `000518ec: movs r1,#0x7f` in `FUN_000518aa` @ `000518aa`
- `00051948: movs r1,#0x7f` in `FUN_00051912` @ `00051912`
- `00051b22: movs r1,#0x7f` in `FUN_00051b20` @ `00051b20`
- `00052a08: movs r1,#0x7f` in `FUN_000529d2` @ `000529d2`
- `0005d6d6: movs r2,#0x7f` in `FUN_0005d6d0` @ `0005d6d0`
- `0005f7b8: movs r1,#0x7f` in `FUN_0005f274` @ `0005f274`

### `0x0`

- `00001002: movs r0,#0x0` in `<none>` @ `<none>`
- `00001530: movt r1,#0x0` in `FUN_000014e4` @ `000014e4`
- `0000154a: movt r1,#0x0` in `FUN_000014e4` @ `000014e4`
- `00001566: str r3,[r0,#0x0]` in `FUN_000014e4` @ `000014e4`
- `00001574: movt r3,#0x0` in `FUN_000014e4` @ `000014e4`
- `00001590: movt r2,#0x0` in `FUN_000014e4` @ `000014e4`
- `00001596: ldr r0,[r2,#0x0]` in `FUN_000014e4` @ `000014e4`
- `000015a6: str r0,[r3,#0x0]` in `FUN_000014e4` @ `000014e4`
- `000015ae: movt r2,#0x0` in `FUN_000014e4` @ `000014e4`
- `000015b2: ldr r0,[r2,#0x0]` in `FUN_000014e4` @ `000014e4`
- `000015b8: str r0,[r3,#0x0]` in `FUN_000014e4` @ `000014e4`
- `000015c4: movs r1,#0x0` in `FUN_000014e4` @ `000014e4`
- `000015ee: movs r0,#0x0` in `FUN_000014e4` @ `000014e4`
- `000015f0: strb r2,[r3,#0x0]` in `FUN_000014e4` @ `000014e4`
- `000015fe: cmp r0,#0x0` in `FUN_000015fc` @ `000015fc`
- `0000160a: ldrb r3,[r3,#0x0]` in `FUN_000015fc` @ `000015fc`
- `0000160c: cmp r3,#0x0` in `FUN_000015fc` @ `000015fc`
- `00001612: ldrh r2,[r0,#0x0]` in `FUN_000015fc` @ `000015fc`
- `00001660: str r4,[r0,#0x0]` in `FUN_000015fc` @ `000015fc`
- `00001678: movs r0,#0x0` in `FUN_000015fc` @ `000015fc`
- `000016a4: str r4,[r1,#0x0]` in `FUN_000015fc` @ `000015fc`
- `000016c6: ldrb r3,[r3,#0x0]` in `FUN_000016b8` @ `000016b8`
- `000016ca: cmp r3,#0x0` in `FUN_000016b8` @ `000016b8`
- `000016d2: movt r5,#0x0` in `FUN_000016b8` @ `000016b8`
- `000016d6: ldr r7,[r5,#0x0]` in `FUN_000016b8` @ `000016b8`
- `000016f4: ldr r0,[r6,#0x0]` in `FUN_000016b8` @ `000016b8`
- `000016fc: cmp r0,#0x0` in `FUN_000016b8` @ `000016b8`
- `00001708: cmp r0,#0x0` in `FUN_000016b8` @ `000016b8`
- `00001716: cmp r0,#0x0` in `FUN_000016b8` @ `000016b8`
- `0000171e: movt r3,#0x0` in `FUN_000016b8` @ `000016b8`
- `00001722: ldr r3,[r3,#0x0]` in `FUN_000016b8` @ `000016b8`
- `00001734: movt r3,#0x0` in `FUN_000016b8` @ `000016b8`
- `0000173a: movw r9,#0x0` in `FUN_000016b8` @ `000016b8`
- `0000173e: ldr r7,[r3,#0x0]` in `FUN_000016b8` @ `000016b8`
- `0000175a: cmp r0,#0x0` in `FUN_000016b8` @ `000016b8`
- `0000175e: ldrb r3,[r6,#0x0]` in `FUN_000016b8` @ `000016b8`
- `00001760: cmp r3,#0x0` in `FUN_000016b8` @ `000016b8`
- `00001766: movs r2,#0x0` in `FUN_000016b8` @ `000016b8`
- `00001768: strb r3,[r6,#0x0]` in `FUN_000016b8` @ `000016b8`
- `0000176a: movs r1,#0x0` in `FUN_000016b8` @ `000016b8`
- `0000176c: movs r3,#0x0` in `FUN_000016b8` @ `000016b8`
- `00001788: ldrb r3,[r3,#0x0]` in `FUN_00001780` @ `00001780`
- `00001796: movs r0,#0x0` in `FUN_00001780` @ `00001780`
- `000017aa: ldrb r3,[r3,#0x0]` in `FUN_0000179c` @ `0000179c`
- `000017ae: cmp r3,#0x0` in `FUN_0000179c` @ `0000179c`
- `000017ba: movt r3,#0x0` in `FUN_0000179c` @ `0000179c`
- `000017c4: movs r6,#0x0` in `FUN_0000179c` @ `0000179c`
- `000017c6: movs r5,#0x0` in `FUN_0000179c` @ `0000179c`
- `000017cc: ldr r7,[r3,#0x0]` in `FUN_0000179c` @ `0000179c`
- `000017dc: strh r3,[r4,#0x0]` in `FUN_0000179c` @ `0000179c`
- `0000182a: cmp r3,#0x0` in `FUN_0000179c` @ `0000179c`
- `0000182e: movs r3,#0x0` in `FUN_0000179c` @ `0000179c`
- `00001830: strh r3,[r4,#0x0]` in `FUN_0000179c` @ `0000179c`
- `00001834: cmp r3,#0x0` in `FUN_0000179c` @ `0000179c`
- `00001838: movs r3,#0x0` in `FUN_0000179c` @ `0000179c`
- `0000183e: cmp r3,#0x0` in `FUN_0000179c` @ `0000179c`
- `00001842: movs r0,#0x0` in `FUN_0000179c` @ `0000179c`
- `0000184c: movs r0,#0x0` in `FUN_0000179c` @ `0000179c`
- `0000186c: ldrb r3,[r3,#0x0]` in `FUN_00001864` @ `00001864`
- `0000187a: movs r0,#0x0` in `FUN_00001864` @ `00001864`
- `00001888: ldrb r3,[r3,#0x0]` in `FUN_00001880` @ `00001880`
- `00001898: strh r2,[r0,#0x0]` in `FUN_00001880` @ `00001880`
- `000018c6: ldrh r3,[r3,#0x0]` in `FUN_00001880` @ `00001880`
- `000018ca: movs r0,#0x0` in `FUN_00001880` @ `00001880`
- `000018da: cmp r0,#0x0` in `FUN_000018d8` @ `000018d8`
- `000018e6: ldrb r3,[r3,#0x0]` in `FUN_000018d8` @ `000018d8`
- `000018e8: cmp r3,#0x0` in `FUN_000018d8` @ `000018d8`
- `000018f0: movt r3,#0x0` in `FUN_000018d8` @ `000018d8`
- `000018f4: ldr r3,[r3,#0x0]` in `FUN_000018d8` @ `000018d8`
- `000018fe: ldr r1,[r2,#0x0]` in `FUN_000018d8` @ `000018d8`
- `00001902: strh r1,[r0,#0x0]` in `FUN_000018d8` @ `000018d8`
- `0000193a: movs r0,#0x0` in `FUN_000018d8` @ `000018d8`
- `0000193e: movs r1,#0x0` in `FUN_000018d8` @ `000018d8`
- `0000195a: ldrb r3,[r3,#0x0]` in `FUN_00001950` @ `00001950`
- `00001962: ldrh r2,[r0,#0x0]` in `FUN_00001950` @ `00001950`
- `0000198c: movs r0,#0x0` in `FUN_00001950` @ `00001950`
- `000019a4: ldrb r2,[r2,#0x0]` in `FUN_0000199c` @ `0000199c`
- `000019a8: movs r0,#0x0` in `FUN_0000199c` @ `0000199c`
- `000019c4: movt r3,#0x0` in `FUN_000019c0` @ `000019c0`
- `000019e2: movs r0,#0x0` in `FUN_000019c0` @ `000019c0`
- ... truncated after 80 hits

### `0x9`

- `00001a1a: cmp r3,#0x9` in `FUN_000019e8` @ `000019e8`
- `00001a34: movs r3,#0x9` in `FUN_000019e8` @ `000019e8`
- `00001b5a: movs r3,#0x9` in `FUN_00001b30` @ `00001b30`
- `00001e80: movs r0,#0x9` in `FUN_00001e5c` @ `00001e5c`
- `000023ce: cmp r4,#0x9` in `FUN_0000234c` @ `0000234c`
- `00002796: movs r3,#0x9` in `FUN_000026f4` @ `000026f4`
- `00002a24: cmp r3,#0x9` in `FUN_0000290c` @ `0000290c`
- `00002a90: cmp r3,#0x9` in `FUN_0000290c` @ `0000290c`
- `00002c66: cmp r2,#0x9` in `FUN_00002b44` @ `00002b44`
- `00002e02: cmp r2,#0x9` in `FUN_00002b44` @ `00002b44`
- `00002f0e: cmp r2,#0x9` in `FUN_00002b44` @ `00002b44`
- `00002f26: movs r0,#0x9` in `FUN_00002b44` @ `00002b44`
- `00003442: cmp r3,#0x9` in `FUN_00003428` @ `00003428`
- `00004100: strb r5,[r4,#0x9]` in `FUN_0000408c` @ `0000408c`
- `00004270: strb r7,[r4,#0x9]` in `FUN_000041fc` @ `000041fc`
- `00004478: ldrb r2,[r3,#0x9]` in `FUN_000041fc` @ `000041fc`
- `000045a6: strb r2,[r1,#0x9]` in `FUN_0000455c` @ `0000455c`
- `000046ce: cmp r2,#0x9` in `FUN_00004690` @ `00004690`
- `00004ad4: cmp r0,#0x9` in `FUN_00004914` @ `00004914`
- `00004f88: cmp r5,#0x9` in `FUN_00004e3a` @ `00004e3a`
- `00004f94: adds r4,#0x9` in `FUN_00004e3a` @ `00004e3a`
- `000058da: movs r6,#0x9` in `FUN_00005854` @ `00005854`
- `000059a2: strb r2,[r3,#0x9]` in `FUN_00005854` @ `00005854`
- `00005a62: movs r0,#0x9` in `FUN_00005854` @ `00005854`
- `00005e5e: lsls r3,r3,#0x9` in `FUN_00005e18` @ `00005e18`
- `00005fb6: lsls r6,r6,#0x9` in `FUN_00005f2c` @ `00005f2c`
- `0000a1a8: lsls r3,r3,#0x9` in `FUN_0000a174` @ `0000a174`
- `0000a4e6: lsls r2,r2,#0x9` in `FUN_0000a210` @ `0000a210`
- `00021724: movs r2,#0x9` in `FUN_0002164c` @ `0002164c`
- `00021746: movs r2,#0x9` in `FUN_0002164c` @ `0002164c`
- `00022ba6: strb r7,[r5,#0x9]` in `FUN_00022b70` @ `00022b70`
- `000271f2: strb r7,[r0,#0x9]` in `FUN_000271c8` @ `000271c8`
- `00027224: ldrb r3,[r4,#0x9]` in `FUN_0002720c` @ `0002720c`
- `00027dda: lsls r2,r2,#0x9` in `FUN_00027d74` @ `00027d74`
- `00027e8a: movs r3,#0x9` in `FUN_00027d74` @ `00027d74`
- `00027f36: lsls r3,r3,#0x9` in `FUN_00027ecc` @ `00027ecc`
- `00030136: adds r6,#0x9` in `FUN_0003009c` @ `0003009c`
- `000338ce: movs r1,#0x9` in `FUN_000338c0` @ `000338c0`
- `00034498: movs r2,#0x9` in `FUN_00034478` @ `00034478`
- `0003455e: cmp r0,#0x9` in `FUN_00034478` @ `00034478`
- `00034ddc: movs r2,#0x9` in `FUN_000348a4` @ `000348a4`
- `00035e4c: lsls r1,r1,#0x9` in `FUN_00035d20` @ `00035d20`
- `00035e5a: lsls r1,r1,#0x9` in `FUN_00035d20` @ `00035d20`
- `00035e6c: lsls r1,r1,#0x9` in `FUN_00035d20` @ `00035d20`
- `00035e7c: lsls r1,r1,#0x9` in `FUN_00035d20` @ `00035d20`
- `00035e8c: lsls r1,r1,#0x9` in `FUN_00035d20` @ `00035d20`
- `00035e9c: lsls r1,r1,#0x9` in `FUN_00035d20` @ `00035d20`
- `00035ea8: lsls r1,r1,#0x9` in `FUN_00035d20` @ `00035d20`
- `00035ee4: lsls r1,r1,#0x9` in `FUN_00035d20` @ `00035d20`
- `00036114: lsls r1,r1,#0x9` in `FUN_00035d20` @ `00035d20`
- `00037032: lsls r3,r3,#0x9` in `FUN_00036f68` @ `00036f68`
- `00037d0c: movs r1,#0x9` in `FUN_00037d04` @ `00037d04`
- `00039e1e: lsrs r3,r3,#0x9` in `FUN_00039de4` @ `00039de4`
- `00039e20: lsls r3,r3,#0x9` in `FUN_00039de4` @ `00039de4`
- `0003c584: lsrs r3,r3,#0x9` in `FUN_0003c550` @ `0003c550`
- `0003c588: lsls r3,r3,#0x9` in `FUN_0003c550` @ `0003c550`
- `0003db2c: movs r2,#0x9` in `FUN_0003d994` @ `0003d994`
- `0003de44: movs r2,#0x9` in `FUN_0003d994` @ `0003d994`
- `000407a0: ldrb r3,[r4,#0x9]` in `FUN_0004077c` @ `0004077c`
- `0004163e: movs r2,#0x9` in `FUN_00041554` @ `00041554`
- `00042446: asrs r1,r1,#0x9` in `FUN_00042388` @ `00042388`
- `000425b0: asrs r5,r5,#0x9` in `FUN_00042388` @ `00042388`
- `000426ae: asrs r5,r5,#0x9` in `FUN_00042388` @ `00042388`
- `00042748: asrs r7,r2,#0x9` in `FUN_00042388` @ `00042388`
- `0004279a: asrs r1,r1,#0x9` in `FUN_00042388` @ `00042388`
- `000428b4: asrs r7,r7,#0x9` in `FUN_00042388` @ `00042388`
- `000446c0: lsrs r3,r3,#0x9` in `FUN_000445e4` @ `000445e4`
- `000446c2: lsls r3,r3,#0x9` in `FUN_000445e4` @ `000445e4`
- `00045f44: lsls r3,r3,#0x9` in `FUN_00045f30` @ `00045f30`
- `00046024: lsls r1,r1,#0x9` in `FUN_00045fb8` @ `00045fb8`
- `00046140: lsls r7,r7,#0x9` in `FUN_00046124` @ `00046124`
- `00046342: movs r0,#0x9` in `FUN_0004620c` @ `0004620c`
- `000463ba: movs r5,#0x9` in `FUN_00046370` @ `00046370`
- `000464de: movs r7,#0x9` in `FUN_000463c0` @ `000463c0`
- `00046608: movs r0,#0x9` in `FUN_000465b8` @ `000465b8`
- `00046c42: cmp r3,#0x9` in `FUN_00046bb0` @ `00046bb0`
- `00046c5a: cmp r3,#0x9` in `FUN_00046bb0` @ `00046bb0`
- `0004f9ba: cmp r1,#0x9` in `FUN_0004f960` @ `0004f960`
- `0004fa7e: cmp r2,#0x9` in `FUN_0004fa04` @ `0004fa04`
- `0004fb74: cmp r3,#0x9` in `FUN_0004fad4` @ `0004fad4`
- ... truncated after 80 hits

### `0x8`

- `00001598: ldr r2,[r2,#0x8]` in `FUN_000014e4` @ `000014e4`
- `0000159e: str r2,[r3,#0x8]` in `FUN_000014e4` @ `000014e4`
- `000015be: ldr r2,[r2,#0x8]` in `FUN_000014e4` @ `000014e4`
- `000015c2: str r2,[r3,#0x8]` in `FUN_000014e4` @ `000014e4`
- `00001616: ldrh r3,[r0,#0x8]` in `FUN_000015fc` @ `000015fc`
- `0000164e: strh r1,[r3,#0x8]` in `FUN_000015fc` @ `000015fc`
- `00001822: strb r0,[r4,#0x8]` in `FUN_0000179c` @ `0000179c`
- `000018c8: strh r3,[r0,#0x8]` in `FUN_00001880` @ `00001880`
- `0000190a: ldr r1,[r2,#0x8]` in `FUN_000018d8` @ `000018d8`
- `0000191a: strh r1,[r0,#0x8]` in `FUN_000018d8` @ `000018d8`
- `0000196c: strh r2,[r3,#0x8]` in `FUN_00001950` @ `00001950`
- `00001976: ldrh r2,[r0,#0x8]` in `FUN_00001950` @ `00001950`
- `00001b5e: strh r3,[r2,#0x8]` in `FUN_00001b30` @ `00001b30`
- `00001bfc: sub sp,#0x8` in `FUN_00001bf0` @ `00001bf0`
- `00001c52: add sp,#0x8` in `FUN_00001bf0` @ `00001bf0`
- `00001c5a: movs r3,#0x8` in `FUN_00001bf0` @ `00001bf0`
- `00001cda: movs r3,#0x8` in `FUN_00001c8c` @ `00001c8c`
- `00001d10: movs r2,#0x8` in `FUN_00001cfc` @ `00001cfc`
- `00001d32: ldr r2,[r4,#0x8]` in `FUN_00001d28` @ `00001d28`
- `00001d58: ldr r2,[r0,#0x8]` in `FUN_00001d54` @ `00001d54`
- `00001d6e: sub sp,#0x8` in `FUN_00001d6c` @ `00001d6c`
- `00001d72: ldr r3,[r0,#0x8]` in `FUN_00001d6c` @ `00001d6c`
- `00001d90: add sp,#0x8` in `FUN_00001d6c` @ `00001d6c`
- `00001d96: sub sp,#0x8` in `FUN_00001d94` @ `00001d94`
- `00001da2: ldr r2,[r0,#0x8]` in `FUN_00001d94` @ `00001d94`
- `00001dba: add sp,#0x8` in `FUN_00001d94` @ `00001d94`
- `00001dc8: ldr r5,[r0,#0x8]` in `FUN_00001dc0` @ `00001dc0`
- `00001dec: ldr r5,[r3,#0x8]` in `FUN_00001dc0` @ `00001dc0`
- `00001e5e: sub sp,#0x8` in `FUN_00001e5c` @ `00001e5c`
- `000024da: cmp r3,#0x8` in `FUN_0000240c` @ `0000240c`
- `000025f0: ldrb r0,[r3,#0x8]` in `FUN_0000240c` @ `0000240c`
- `000026c6: asrs r1,r1,#0x8` in `FUN_00002618` @ `00002618`
- `000026ea: asrs r1,r1,#0x8` in `FUN_00002618` @ `00002618`
- `000026fe: movs r3,#0x8` in `FUN_000026f4` @ `000026f4`
- `000027a6: str r3,[r0,#0x8]` in `FUN_000027a0` @ `000027a0`
- `000027ba: ldr r2,[r3,#0x8]` in `FUN_000027ac` @ `000027ac`
- `000027c6: str r0,[r3,#0x8]` in `FUN_000027ac` @ `000027ac`
- `000027c8: str r2,[r0,#0x8]` in `FUN_000027ac` @ `000027ac`
- `000027ce: str r3,[r0,#0x8]` in `FUN_000027ac` @ `000027ac`
- `000027e6: ldr r4,[r4,#0x8]` in `FUN_000027d4` @ `000027d4`
- `0000286e: ldr r1,[r3,#0x8]` in `FUN_00002834` @ `00002834`
- `00002890: str r3,[r4,#0x8]` in `FUN_00002834` @ `00002834`
- `00002894: str r4,[r3,#0x8]` in `FUN_00002834` @ `00002834`
- `00002896: str r1,[r4,#0x8]` in `FUN_00002834` @ `00002834`
- `000029ca: ldr r1,[sp,#0x8]` in `FUN_0000290c` @ `0000290c`
- `000029ce: str r1,[sp,#0x8]` in `FUN_0000290c` @ `0000290c`
- `00002a16: cmp r3,#0x8` in `FUN_0000290c` @ `0000290c`
- `00002a4e: ldr r2,[sp,#0x8]` in `FUN_0000290c` @ `0000290c`
- `00002a52: str r2,[r7,#0x8]` in `FUN_0000290c` @ `0000290c`
- `00002a86: cmp r3,#0x8` in `FUN_0000290c` @ `0000290c`
- `00002bec: ldrh r0,[r1,#0x8]` in `FUN_00002b44` @ `00002b44`
- `00002c4c: cmp r2,#0x8` in `FUN_00002b44` @ `00002b44`
- `00002d50: ldrh r0,[r1,#0x8]` in `FUN_00002b44` @ `00002b44`
- `00002dda: cmp r2,#0x8` in `FUN_00002b44` @ `00002b44`
- `00002e44: asrs r1,r1,#0x8` in `FUN_00002b44` @ `00002b44`
- `00002e5c: asrs r1,r1,#0x8` in `FUN_00002b44` @ `00002b44`
- `00002e74: asrs r1,r1,#0x8` in `FUN_00002b44` @ `00002b44`
- `00002e8c: asrs r1,r1,#0x8` in `FUN_00002b44` @ `00002b44`
- `00002ea4: asrs r1,r1,#0x8` in `FUN_00002b44` @ `00002b44`
- `00002ebc: asrs r1,r1,#0x8` in `FUN_00002b44` @ `00002b44`
- `00002ed2: asrs r1,r1,#0x8` in `FUN_00002b44` @ `00002b44`
- `00002eea: asrs r1,r1,#0x8` in `FUN_00002b44` @ `00002b44`
- `00002ef6: cmp r2,#0x8` in `FUN_00002b44` @ `00002b44`
- `00002f02: asrs r1,r1,#0x8` in `FUN_00002b44` @ `00002b44`
- `00002f1a: asrs r1,r1,#0x8` in `FUN_00002b44` @ `00002b44`
- `0000306c: movs r0,#0x8` in `FUN_00002b44` @ `00002b44`
- `000031ee: str r3,[sp,#0x8]` in `FUN_00003120` @ `00003120`
- `000031f4: ldr r2,[r4,#0x8]` in `FUN_00003120` @ `00003120`
- `000031fa: str r2,[r4,#0x8]` in `FUN_00003120` @ `00003120`
- `0000323e: ldr r3,[sp,#0x8]` in `FUN_00003120` @ `00003120`
- `00003260: ldr r3,[r4,#0x8]` in `FUN_00003120` @ `00003120`
- `0000326e: str r3,[r4,#0x8]` in `FUN_00003120` @ `00003120`
- `000034e8: strb r0,[r3,#0x8]` in `FUN_000034e0` @ `000034e0`
- `000037ca: str r3,[sp,#0x8]` in `FUN_00003544` @ `00003544`
- `000037fc: ldr r3,[sp,#0x8]` in `FUN_00003544` @ `00003544`
- `0000394c: ldrb r3,[r3,#0x8]` in `FUN_00003918` @ `00003918`
- `00003ad2: ldrb r1,[r0,#0x8]` in `PROBE_00003ac4` @ `00003ac4`
- `000040fa: strb r6,[r4,#0x8]` in `FUN_0000408c` @ `0000408c`
- `000041ae: ldrh r1,[r1,#0x8]` in `FUN_0000408c` @ `0000408c`
- `000041c6: ldrh r2,[r2,#0x8]` in `FUN_0000408c` @ `0000408c`
- ... truncated after 80 hits

## Decompiled Function Scan

Functions whose decompiled C mentions the config key or mode/effect globals.

### `FUN_00001e50` @ `00001e50`

```c

undefined1 FUN_00001e50(void)

{
  return DAT_20004291;
}
```

### `FUN_00001e5c` @ `00001e5c`

```c

void FUN_00001e5c(void)

{
  undefined1 local_9;
  
  FUN_00005df4(0x20005cbc,0x204,&local_9);
  DAT_20004291 = local_9;
  FUN_00003a14(9);
  FUN_00003f88();
  FUN_0000a058();
  FUN_00005f2c(0x20005d04,0x9818);
  FUN_00005f14(0x20005d04);
  FUN_000026f4();
  do {
    FUN_000027d4();
  } while( true );
}
```

### `FUN_00002288` @ `00002288`

```c

void FUN_00002288(short *param_1)

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
        FUN_00001eec(bVar2,(int)*param_1);
        bVar1 = DAT_200045ca;
      }
      else if (*local_2c != '\0') {
        FUN_00001eec(bVar2,(int)*param_1);
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

### `FUN_0000240c` @ `0000240c`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0000240c(void)

{
  int iVar1;
  int iVar2;
  
  if (DAT_200045cc != 0) {
    if (_DAT_20004538 != _DAT_2000453c) {
      iVar2 = (int)(char)((char)_DAT_20004538 - (char)_DAT_2000453c);
      _DAT_2000453c = _DAT_20004538;
      if (iVar2 != 0) {
        iVar1 = FUN_00001e50();
        FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x9664),iVar2);
      }
    }
    if (1 < DAT_200045cc) {
      if (_DAT_20004548 != _DAT_2000454c) {
        iVar2 = (int)(char)((char)_DAT_20004548 - (char)_DAT_2000454c);
        _DAT_2000454c = _DAT_20004548;
        if (iVar2 != 0) {
          iVar1 = FUN_00001e50();
          FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x9665),iVar2);
        }
      }
      if (2 < DAT_200045cc) {
        if (_DAT_20004558 != _DAT_2000455c) {
          iVar2 = (int)(char)((char)_DAT_20004558 - (char)_DAT_2000455c);
          _DAT_2000455c = _DAT_20004558;
          if (iVar2 != 0) {
            iVar1 = FUN_00001e50();
            FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x9666),iVar2);
          }
        }
        if (3 < DAT_200045cc) {
          if (_DAT_20004568 != _DAT_2000456c) {
            iVar2 = (int)(char)((char)_DAT_20004568 - (char)_DAT_2000456c);
            _DAT_2000456c = _DAT_20004568;
            if (iVar2 != 0) {
              iVar1 = FUN_00001e50();
              FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x9667),iVar2);
            }
          }
          if (4 < DAT_200045cc) {
            if (_DAT_20004578 != _DAT_2000457c) {
              iVar2 = (int)(char)((char)_DAT_20004578 - (char)_DAT_2000457c);
              _DAT_2000457c = _DAT_20004578;
              if (iVar2 != 0) {
                iVar1 = FUN_00001e50();
                FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x9668),iVar2);
              }
            }
            if (5 < DAT_200045cc) {
              if ((_DAT_20004588 != _DAT_2000458c) &&
                 (iVar2 = (int)(char)((char)_DAT_20004588 - (char)_DAT_2000458c),
                 _DAT_2000458c = _DAT_20004588, iVar2 != 0)) {
                iVar1 = FUN_00001e50();
                FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x9669),iVar2);
              }
              if (6 < DAT_200045cc) {
                if (_DAT_20004598 != _DAT_2000459c) {
                  iVar2 = (int)(char)((char)_DAT_20004598 - (char)_DAT_2000459c);
                  _DAT_2000459c = _DAT_20004598;
                  if (iVar2 != 0) {
                    iVar1 = FUN_00001e50();
                    FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x966a),iVar2);
                  }
                }
                if (7 < DAT_200045cc) {
                  if (_DAT_200045a8 != _DAT_200045ac) {
                    iVar2 = (int)(char)((char)_DAT_200045a8 - (char)_DAT_200045ac);
                    _DAT_200045ac = _DAT_200045a8;
                    if (iVar2 != 0) {
                      iVar1 = FUN_00001e50();
                      FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x966b),iVar2);
                    }
                  }
                  if ((8 < DAT_200045cc) && (_DAT_200045b8 != _DAT_200045bc)) {
                    iVar2 = (int)(char)((char)_DAT_200045b8 - (char)_DAT_200045bc);
                    _DAT_200045bc = _DAT_200045b8;
                    if (iVar2 != 0) {
                      iVar1 = FUN_00001e50();
                      FUN_00001fb0(*(undefined1 *)(iVar1 * 9 + 0x966c),iVar2);
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

### `FUN_000026f4` @ `000026f4`

```c

void FUN_000026f4(void)

{
  int iVar1;
  undefined4 in_r3;
  undefined1 *puVar2;
  byte *pbVar3;
  undefined2 *puVar4;
  
  iVar1 = FUN_00001e50();
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
  puVar4 = (undefined2 *)0x95fc;
  pbVar3 = DAT_0000279c;
  do {
    FUN_00005df4(0x20005cbc,*puVar4,pbVar3,puVar2,in_r3);
    iVar1 = iVar1 + 1;
    *(ushort *)(pbVar3 + 2) = (ushort)*pbVar3;
    puVar2 = (undefined1 *)(uint)DAT_200045cc;
    puVar4 = puVar4 + 2;
    pbVar3 = pbVar3 + 0x10;
  } while (iVar1 < (int)puVar2);
  FUN_000027a0(0x200045e0,&DAT_00001201);
  FUN_00002834(500,0,0x200045e0);
  FUN_000027a0(0x200045d0,&DAT_000011f5);
  FUN_000027ac(0x200045d0);
  return;
}
```

### `FUN_00003a14` @ `00003a14`

```c

void FUN_00003a14(int param_1)

{
  FUN_00001d28(0x200040a0);
  DAT_20005b60 = 1;
  if (param_1 == 1) {
    FUN_00005854(0x20005cd4,PROBE_000097e4);
  }
  else {
    FUN_00005854(0x20005d24,0x9874);
  }
  return;
}
```

### `FUN_00003ab8` @ `00003ab8`

```c

undefined4 FUN_00003ab8(void)

{
  return 0x200040a0;
}
```

### `PROBE_00003ac4` @ `00003ac4`

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

