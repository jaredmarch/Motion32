# Motion 32 Constant Set Probe

## Function Constant Sets

### `native transport tap/rec/play/stop`

- no function matches

### `pre-native transport symptom`

- no function matches

### `native nav`

- no function matches

### `native pad endpoints`

- `FUN_00022484` @ `00022484`

```c

undefined4 FUN_00022484(void)

{
  char *pcVar1;
  undefined3 uVar2;
  int iVar3;
  undefined4 uVar4;
  int iVar5;
  int iVar6;
  
  iVar5 = DAT_0002269c;
  pcVar1 = DAT_00022698;
  if (*DAT_00022694 == '\0') {
    uVar4 = 2;
  }
  else {
    if (*DAT_00022698 != '\0') {
      if (*(int *)(DAT_0002269c + 400) != 0) {
        FUN_0004a750(*(int *)(DAT_0002269c + 400),DAT_000226a0);
      }
      if (*(int *)(iVar5 + 0x19c) != 0) {
        FUN_0004a750(*(int *)(iVar5 + 0x19c),DAT_000226a4);
      }
      if (*(int *)(iVar5 + 0x1a8) != 0) {
        FUN_0004a750(*(int *)(iVar5 + 0x1a8),DAT_000226a8);
      }
      if (*(int *)(iVar5 + 0x1b4) != 0) {
        FUN_0004a750(*(int *)(iVar5 + 0x1b4),DAT_000226ac);
      }
      if (*(int *)(iVar5 + 0x1c8) != 0) {
        FUN_0004a750(*(int *)(iVar5 + 0x1c8),DAT_000226b0);
      }
      if (*(int *)(iVar5 + 0x1d4) != 0) {
        FUN_0004a750(*(int *)(iVar5 + 0x1d4),DAT_000226b4);
      }
      if (*(int *)(iVar5 + 0x1e0) != 0) {
        FUN_0004a750(*(int *)(iVar5 + 0x1e0),DAT_000226b8);
      }
      if (*(int *)(iVar5 + 0x1ec) != 0) {
        FUN_0004a750(*(int *)(iVar5 + 0x1ec),DAT_000226bc);
      }
      *pcVar1 = '\0';
    }
    iVar3 = FUN_0002ec30(0x43);
    iVar6 = *(int *)(iVar5 + 0x194);
    if (iVar3 == 0) {
      if (iVar6 != 0) {
        uVar2 = FUN_00045c78(*(undefined4 *)(DAT_00022828 + 0x5c));
        FUN_00037ee4(iVar6,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1a0);
      if (iVar3 != 0) {
        uVar2 = FUN_00045c78(*(undefined4 *)(DAT_00022828 + 0x5c));
        FUN_00037ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1ac);
      if (iVar3 != 0) {
        uVar2 = FUN_00045c78(*(undefined4 *)(DAT_00022828 + 0x5c));
        FUN_00037ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1b8);
      if (iVar3 != 0) {
        uVar2 = FUN_00045c78(*(undefined4 *)(DAT_00022828 + 0x5c));
        FUN_00037ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1cc);
      if (iVar3 != 0) {
        uVar2 = FUN_00045c78(*(undefined4 *)(DAT_00022828 + 0x5c));
        FUN_00037ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1d8);
      if (iVar3 != 0) {
        uVar2 = FUN_00045c78(*(undefined4 *)(DAT_00022828 + 0x5c));
        FUN_00037ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1e4);
      if (iVar3 != 0) {
        uVar2 = FUN_00045c78(*(undefined4 *)(DAT_00022828 + 0x5c));
        FUN_00037ee4(iVar3,uVar2,0);
/* ... truncated ... */
```

- `FUN_00043fbc` @ `00043fbc`

```c

void FUN_00043fbc(int param_1,int param_2)

{
  int iVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  int *piVar4;
  byte bVar5;
  int iVar6;
  int iVar7;
  uint uVar8;
  uint uVar9;
  int iVar10;
  int local_16c;
  int local_160;
  int iStack_15c;
  int local_158;
  int local_154;
  int local_150;
  int local_14c;
  undefined1 *local_148;
  undefined1 *local_144;
  undefined1 *local_140;
  int local_138;
  int local_134;
  int local_12c;
  undefined1 auStack_128 [4];
  int local_124;
  int local_11c;
  int local_118;
  int local_114;
  int local_110;
  int local_10c;
  int local_108;
  int local_104;
  undefined1 *local_100;
  int local_fc;
  undefined1 local_f4;
  undefined1 *local_f0;
  byte local_ec;
  undefined1 auStack_eb [3];
  int local_e8;
  undefined1 local_e4;
  undefined1 *local_e0;
  undefined1 uStack_d8;
  undefined1 auStack_d0 [56];
  undefined1 auStack_98 [56];
  undefined1 auStack_60 [60];
  
  local_150 = *(int *)(param_2 + 0x2c);
  iVar10 = *(int *)(param_2 + 0x24);
  iVar7 = *(int *)(param_2 + 0x1c);
  local_158 = local_150;
  if (iVar10 < local_150) {
    local_158 = iVar10;
  }
  if (iVar7 < local_158) {
    local_158 = iVar7;
  }
  iVar6 = *(int *)(param_2 + 0x28);
  local_14c = *(int *)(param_2 + 0x30);
  iVar1 = *(int *)(param_2 + 0x20);
  local_154 = local_14c;
  if (iVar6 < local_14c) {
    local_154 = iVar6;
  }
  if (iVar1 < local_154) {
    local_154 = iVar1;
  }
  if (local_150 < iVar10) {
    local_150 = iVar10;
  }
  if (local_150 < iVar7) {
    local_150 = iVar7;
  }
  if (local_14c < iVar6) {
    local_14c = iVar6;
  }
  if (local_14c < iVar1) {
/* ... truncated ... */
```


### `native pad lane starts`

- `FUN_0000240c` @ `0000240c`

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
/* ... truncated ... */
```

- `FUN_000041fc` @ `000041fc`

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
/* ... truncated ... */
```

- `FUN_00004914` @ `00004914`

```c

int FUN_00004914(int param_1,int *param_2)

{
  char cVar1;
  int iVar2;
  uint uVar3;
  int iVar4;
  ushort *puVar5;
  int iVar6;
  int iVar7;
  undefined2 *puVar8;
  undefined2 uVar9;
  uint uVar10;
  ushort local_58 [4];
  ushort local_50;
  ushort local_4e;
  ushort local_4c;
  ushort local_4a;
  ushort local_48;
  ushort local_46;
  ushort local_44;
  ushort local_42;
  ushort local_40;
  ushort local_3e;
  ushort local_3c;
  ushort local_3a;
  ushort local_38;
  ushort local_36;
  ushort local_34;
  ushort local_32;
  ushort local_30;
  ushort local_2e;
  ushort local_2c;
  ushort local_2a;
  ushort local_28;
  ushort local_26;
  ushort local_24;
  ushort local_22;
  
  puVar5 = local_58;
  iVar2 = (**(code **)((*(undefined4 **)(param_1 + 0x7c))[2] + 8))
                    (**(undefined4 **)(param_1 + 0x7c),local_58);
  if ((iVar2 != 6000) && (iVar2 != 0x1772)) {
    uVar3 = (uint)*(byte *)(*(int *)(param_1 + 0x78) + 0x10);
    if (uVar3 != 0) {
      cVar1 = *(char *)(*(int *)(*(int *)(param_1 + 0x7c) + 4) + 5);
      if (cVar1 == '\x01') {
        iVar2 = *(int *)(param_1 + 0x18);
        iVar6 = *param_2;
        uVar10 = 0;
        do {
          iVar4 = uVar10 * 2;
          iVar7 = (uint)*puVar5 - (uint)*(ushort *)(iVar2 + iVar4);
          uVar9 = 0;
          if (-1 < iVar7) {
            uVar9 = (undefined2)
                    ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar7) /
                    (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + iVar4));
          }
          uVar10 = uVar10 + 1;
          *(undefined2 *)(iVar4 + iVar6) = uVar9;
          puVar5 = puVar5 + 1;
        } while ((uVar10 & 0xff) < uVar3);
        return 0;
      }
      if (cVar1 == '\x03') {
        puVar5 = *(ushort **)(param_1 + 0x18);
        iVar2 = (uint)*puVar5 - ((uint)local_58[1] - (uint)local_58[0]);
        uVar9 = 0;
        puVar8 = (undefined2 *)*param_2;
        if (-1 < iVar2) {
          uVar9 = (undefined2)
                  ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                  (int)(uint)**(ushort **)(param_1 + 0x10));
        }
        *puVar8 = uVar9;
        if (uVar3 != 1) {
          iVar2 = (uint)puVar5[1] - ((uint)local_58[3] - (uint)local_58[2]);
          uVar9 = 0;
/* ... truncated ... */
```

- `FUN_00005f2c` @ `00005f2c`

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
/* ... truncated ... */
```

- `FUN_0000657c` @ `0000657c`

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
/* ... truncated ... */
```

- `FUN_00021f24` @ `00021f24`

```c

undefined4 FUN_00021f24(void)

{
  char cVar1;
  undefined1 uVar2;
  undefined3 uVar3;
  undefined4 uVar4;
  uint uVar5;
  int iVar6;
  undefined4 uVar7;
  int iVar8;
  undefined4 local_28;
  
  cVar1 = FUN_0002ec30(0x2d);
  iVar6 = DAT_000222a4;
  if (*DAT_000222a0 == '\0') {
    uVar4 = FUN_0002ec30(0x3b);
    uVar5 = FUN_0002ece0(cVar1,uVar4,8);
    iVar6 = DAT_00022478;
    uVar7 = *(undefined4 *)(DAT_00022478 + 0x3b8);
    uVar4 = FUN_0002ec30(0x3b);
    FUN_0005f244(uVar4,&local_28,10);
    FUN_0004a750(uVar7,&local_28);
    FUN_0004b63c(*(undefined4 *)(iVar6 + 0x3c8),uVar5 & 0xff);
    uVar4 = *(undefined4 *)(iVar6 + 0x3c0);
    FUN_0005f244(uVar5,&local_28,10);
    FUN_0004a750(uVar4,&local_28);
    iVar8 = *(int *)(iVar6 + 0x3bc);
    uVar4 = FUN_0002ec30(0x2d);
    uVar7 = FUN_0002ec30(0x3b);
    uVar4 = FUN_0002ecb8(uVar4,uVar7);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0x3c8);
    uVar4 = FUN_0002ec30(0x3b);
    uVar5 = FUN_0002ece0(cVar1,uVar4,0);
    if (iVar8 != 0) {
      uVar4 = FUN_00045c78(*(undefined4 *)(DAT_0002247c + (uVar5 & 0xff) * 8 + 4));
      local_28 = CONCAT22(CONCAT11(local_28._3_1_,(char)((uint)uVar4 >> 0x10)),(short)uVar4);
      FUN_00037ec8(iVar8,local_28,0x20000);
    }
    iVar6 = *(int *)(iVar6 + 0x3c4);
  }
  else {
    iVar8 = *(int *)(DAT_000222a4 + 0x50);
    uVar4 = FUN_0002ec74(0xc);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0x54);
    uVar4 = FUN_0002ec74(0xd);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0x58);
    uVar4 = FUN_0002ec74(0xe);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0x5c);
    uVar4 = FUN_0002ec74(0xf);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0xf4);
    uVar4 = FUN_0002ec74(0x10);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0xf8);
    uVar4 = FUN_0002ec74(0x11);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0xfc);
    uVar4 = FUN_0002ec74(0x12);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
/* ... truncated ... */
```

- `FUN_00022484` @ `00022484`

```c

undefined4 FUN_00022484(void)

{
  char *pcVar1;
  undefined3 uVar2;
  int iVar3;
  undefined4 uVar4;
  int iVar5;
  int iVar6;
  
  iVar5 = DAT_0002269c;
  pcVar1 = DAT_00022698;
  if (*DAT_00022694 == '\0') {
    uVar4 = 2;
  }
  else {
    if (*DAT_00022698 != '\0') {
      if (*(int *)(DAT_0002269c + 400) != 0) {
        FUN_0004a750(*(int *)(DAT_0002269c + 400),DAT_000226a0);
      }
      if (*(int *)(iVar5 + 0x19c) != 0) {
        FUN_0004a750(*(int *)(iVar5 + 0x19c),DAT_000226a4);
      }
      if (*(int *)(iVar5 + 0x1a8) != 0) {
        FUN_0004a750(*(int *)(iVar5 + 0x1a8),DAT_000226a8);
      }
      if (*(int *)(iVar5 + 0x1b4) != 0) {
        FUN_0004a750(*(int *)(iVar5 + 0x1b4),DAT_000226ac);
      }
      if (*(int *)(iVar5 + 0x1c8) != 0) {
        FUN_0004a750(*(int *)(iVar5 + 0x1c8),DAT_000226b0);
      }
      if (*(int *)(iVar5 + 0x1d4) != 0) {
        FUN_0004a750(*(int *)(iVar5 + 0x1d4),DAT_000226b4);
      }
      if (*(int *)(iVar5 + 0x1e0) != 0) {
        FUN_0004a750(*(int *)(iVar5 + 0x1e0),DAT_000226b8);
      }
      if (*(int *)(iVar5 + 0x1ec) != 0) {
        FUN_0004a750(*(int *)(iVar5 + 0x1ec),DAT_000226bc);
      }
      *pcVar1 = '\0';
    }
    iVar3 = FUN_0002ec30(0x43);
    iVar6 = *(int *)(iVar5 + 0x194);
    if (iVar3 == 0) {
      if (iVar6 != 0) {
        uVar2 = FUN_00045c78(*(undefined4 *)(DAT_00022828 + 0x5c));
        FUN_00037ee4(iVar6,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1a0);
      if (iVar3 != 0) {
        uVar2 = FUN_00045c78(*(undefined4 *)(DAT_00022828 + 0x5c));
        FUN_00037ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1ac);
      if (iVar3 != 0) {
        uVar2 = FUN_00045c78(*(undefined4 *)(DAT_00022828 + 0x5c));
        FUN_00037ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1b8);
      if (iVar3 != 0) {
        uVar2 = FUN_00045c78(*(undefined4 *)(DAT_00022828 + 0x5c));
        FUN_00037ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1cc);
      if (iVar3 != 0) {
        uVar2 = FUN_00045c78(*(undefined4 *)(DAT_00022828 + 0x5c));
        FUN_00037ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1d8);
      if (iVar3 != 0) {
        uVar2 = FUN_00045c78(*(undefined4 *)(DAT_00022828 + 0x5c));
        FUN_00037ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1e4);
      if (iVar3 != 0) {
        uVar2 = FUN_00045c78(*(undefined4 *)(DAT_00022828 + 0x5c));
        FUN_00037ee4(iVar3,uVar2,0);
/* ... truncated ... */
```

- `FUN_00031730` @ `00031730`

```c

void FUN_00031730(int param_1,uint param_2)

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
    uVar1 = FUN_00036b60(param_1,uVar9,param_2);
    if (uVar1 == 0) {
      *(short *)(param_1 + 0x28) = (short)param_2;
    }
    else {
      FUN_00034298(param_1);
      *(short *)(param_1 + 0x28) = (short)param_2;
      FUN_00036e90(param_1);
      iVar2 = FUN_0004ceb8(0x280);
      uVar10 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
      if (uVar10 != 0) {
        iVar7 = 0;
        iVar8 = 0;
        puVar11 = *(undefined4 **)(param_1 + 0xc);
LAB_000317a4:
        uVar3 = puVar11[1];
        if (((~param_2 & uVar3 & 0xffff) == 0) && ((*(byte *)((int)puVar11 + 7) & 2) == 0)) {
          uVar16 = (uint)*(byte *)((undefined4 *)*puVar11 + 2);
          pcVar12 = *(char **)*puVar11;
          if (uVar16 == 0xff) {
            for (; *pcVar12 != '\0'; pcVar12 = pcVar12 + 8) {
              if (*pcVar12 == 'h') {
                puVar5 = *(undefined4 **)(pcVar12 + 4);
                goto LAB_000317f4;
              }
            }
          }
          else if (uVar16 != 0) {
            uVar4 = 0;
LAB_000317e6:
            if (pcVar12[uVar4 + uVar16 * 4] != 'h') goto LAB_000317de;
            puVar5 = *(undefined4 **)(pcVar12 + uVar4 * 4);
LAB_000317f4:
            pcVar12 = (char *)*puVar5;
            cVar15 = *pcVar12;
            if (cVar15 == '\0') goto LAB_00031878;
            if (iVar7 == 0) goto LAB_000318b6;
            do {
              while( true ) {
                iVar13 = 0;
                puVar6 = (uint *)(iVar2 + 4);
                while ((((char)puVar6[1] != cVar15 || ((*puVar6 & 0xff0000) != (uVar3 & 0xff0000)))
                       || ((*puVar6 & 0xffff) < (uVar3 & 0xffff)))) {
                  iVar13 = iVar13 + 1;
                  puVar6 = puVar6 + 5;
                  if (iVar13 == iVar7) goto LAB_000318b6;
                }
                if (iVar7 == iVar13) break;
                pcVar12 = pcVar12 + 1;
                cVar15 = *pcVar12;
                if (cVar15 == '\0') goto LAB_0003185c;
              }
LAB_000318b6:
              puVar14 = (undefined2 *)(iVar2 + iVar7 * 0x14);
              iVar7 = iVar7 + 1;
              *puVar14 = (short)puVar5[3];
              puVar14[1] = (short)puVar5[4];
/* ... truncated ... */
```

- `FUN_00032300` @ `00032300`

```c

void FUN_00032300(int param_1,uint param_2)

{
  int iVar1;
  int iVar2;
  undefined1 auStack_38 [16];
  undefined1 auStack_28 [20];
  
  if (param_1 != 0) {
    if (param_2 != (*(uint *)(param_1 + 0x24) & param_2)) {
      iVar1 = FUN_00033af0();
      if ((int)(param_2 << 0x1f) < 0) {
        FUN_00034298(param_1);
        *(uint *)(param_1 + 0x24) = *(uint *)(param_1 + 0x24) | param_2;
        if ((((int)((uint)*(ushort *)(param_1 + 0x28) << 0x1e) < 0) && (*(int *)(param_1 + 8) != 0))
           && (iVar2 = *(int *)(*(int *)(param_1 + 8) + 4), iVar2 != 0)) {
          FUN_00031414(iVar2);
          iVar2 = FUN_000316a8(iVar2);
          if (iVar2 != 0) {
            FUN_00034298();
          }
        }
      }
      else {
        *(uint *)(param_1 + 0x24) = *(uint *)(param_1 + 0x24) | param_2;
      }
      iVar2 = FUN_00033af0(param_1);
      if ((iVar1 != iVar2) || ((param_2 & 0x1800000) != 0)) {
        FUN_00038184(param_1);
        FUN_00033b28();
        FUN_00033b28(param_1);
      }
      if ((int)(param_2 << 0x1b) < 0) {
        FUN_00035d20(param_1,auStack_38,auStack_28);
        FUN_00034208(param_1,auStack_38);
        FUN_00034208(param_1,auStack_28);
      }
    }
    return;
  }
  FUN_000468e8(3,DAT_000323c8,0xe9,DAT_000323c0,DAT_000323c4,DAT_000323bc,DAT_000323b8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

- `FUN_00032b10` @ `00032b10`

```c

void FUN_00032b10(undefined4 param_1,int param_2,undefined4 *param_3)

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
    uVar7 = FUN_00036de8();
    if (param_2 == 0) goto LAB_00032b32;
  }
  else {
    uVar7 = (uint)*(byte *)(param_3[4] + 0x38);
    if (param_2 == 0) goto LAB_00032b32;
    uVar5 = FUN_00036ab8(param_1,param_2,0x62);
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
LAB_00032b32:
  uVar4 = FUN_00036ab8(param_1,param_2,0xc);
  param_3[7] = uVar4;
  if (*(char *)(param_3 + 8) != '\0') {
    bVar2 = FUN_00036ab8(param_1,param_2,0x1d);
    *(byte *)(param_3 + 8) = bVar2;
    if (2 < bVar2) {
      uVar4 = FUN_00036ab8(param_1,param_2,0x1c);
      uVar3 = FUN_00036b58(param_1,param_2,uVar4);
      uVar4 = FUN_00032a74(param_1,param_2,param_3[4],uVar3);
      *(char *)((int)param_3 + 0x21) = (char)uVar4;
      *(char *)((int)param_3 + 0x23) = (char)((uint)uVar4 >> 0x10);
      *(char *)((int)param_3 + 0x22) = (char)((uint)uVar4 >> 8);
      iVar6 = FUN_00036ab8(param_1,param_2,0x26);
      if ((iVar6 == 0) || ((*(byte *)(iVar6 + 0xb) & 0xf) == 0)) {
        bVar2 = FUN_00036ab8(param_1,param_2,0x20);
        *(byte *)((int)param_3 + 0x2f) = *(byte *)((int)param_3 + 0x2f) & 0xf0 | bVar2 & 0xf;
        if ((bVar2 & 0xf) != 0) {
          FUN_0005bef8(param_3 + 9,(int)param_3 + 0x21,3);
          uVar4 = FUN_00036ab8(param_1,param_2,0x23);
          uVar3 = FUN_00036b58(param_1,param_2,uVar4);
          uVar4 = FUN_00032a74(param_1,param_2,param_3[4],uVar3);
          *(char *)((int)param_3 + 0x29) = (char)uVar4;
          *(char *)((int)param_3 + 0x2a) = (char)((uint)uVar4 >> 8);
          *(char *)((int)param_3 + 0x2b) = (char)((uint)uVar4 >> 0x10);
          uVar1 = FUN_00036ab8(param_1,param_2,0x21);
          *(undefined1 *)(param_3 + 10) = uVar1;
          uVar1 = FUN_00036ab8(param_1,param_2,0x22);
          *(undefined1 *)((int)param_3 + 0x2d) = uVar1;
          uVar1 = FUN_00036ab8(param_1,param_2,0x24);
          *(undefined1 *)((int)param_3 + 0x27) = uVar1;
          uVar1 = FUN_00036ab8(param_1,param_2,0x25);
          *(undefined1 *)(param_3 + 0xb) = uVar1;
        }
      }
      else {
        FUN_00050328(param_3 + 9,iVar6,0xc);
      }
    }
  }
  if (*(char *)(param_3 + 0x12) != '\0') {
    iVar6 = FUN_00036ab8(param_1,param_2,0x30);
    param_3[0x11] = iVar6;
    if (iVar6 != 0) {
      bVar2 = FUN_00036ab8(param_1,param_2,0x32);
      *(byte *)(param_3 + 0x12) = bVar2;
      if (2 < bVar2) {
        bVar2 = FUN_00036ab8(param_1,param_2,0x34);
/* ... truncated ... */
```

- `FUN_000348a4` @ `000348a4`

```c

undefined4 FUN_000348a4(int param_1)

{
  char cVar1;
  int iVar2;
  int iVar3;
  uint uVar4;
  int iVar5;
  undefined4 uVar6;
  int iVar7;
  uint uVar8;
  int iVar9;
  int iVar10;
  uint uVar11;
  int iVar12;
  int iVar13;
  int iVar14;
  uint local_6c;
  uint local_68;
  uint local_64;
  uint local_60;
  undefined4 local_48;
  undefined4 local_44;
  undefined4 local_40;
  undefined4 local_3c;
  uint local_38;
  uint local_34;
  
  if (param_1 == 0) {
    FUN_000468e8(3,DAT_000350c4,0x59,DAT_000350bc,DAT_000350c0,DAT_000350b8,DAT_000350b4);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  if (((*(byte *)(param_1 + 0x2b) & 0xc) == 0xc) || (iVar2 = FUN_00038184(), iVar2 == 0)) {
LAB_00034a82:
    uVar6 = 0;
  }
  else {
    if ((*(byte *)(param_1 + 0x2b) & 8) == 0) {
      uVar4 = FUN_00036ab8(param_1,0,1);
      local_38 = uVar4;
      if (((uVar4 & 0x60000000) == 0x20000000) &&
         (uVar8 = DAT_00034cb0 & uVar4, uVar8 != DAT_00034cb4)) {
        iVar3 = FUN_00033c28(iVar2);
        if (uVar4 == DAT_00034cac) {
LAB_00034b5e:
          iVar5 = FUN_00035248(param_1);
          if (*(int *)(param_1 + 8) != 0) {
            *(undefined4 *)(*(int *)(param_1 + 8) + 0x20) = 0;
          }
          local_64 = FUN_00036ab8(param_1,0,0x13);
          local_38 = local_64;
          uVar4 = FUN_00036ab8(param_1,0,0x30);
          local_38 = uVar4;
          local_38 = FUN_00036ab8(param_1,0,0x34);
          if ((int)(local_38 << 0x1c) < 0) {
            local_64 = local_64 + uVar4;
          }
          local_68 = FUN_00036ab8(param_1,0,0x12);
          local_38 = local_68;
          uVar4 = FUN_00036ab8(param_1,0,0x30);
          local_38 = uVar4;
          iVar7 = FUN_00036ab8(param_1,0,0x34);
          if (iVar7 << 0x1d < 0) {
            local_68 = local_68 + uVar4;
          }
          local_38 = 0;
          local_34 = DAT_00034cbc;
          FUN_00033498(param_1,0x34,&local_38);
          uVar8 = local_38 + local_68 + local_64;
          iVar7 = FUN_000381e8(param_1);
          local_38 = FUN_00036ab8(param_1,0,0x27);
          uVar4 = uVar8;
          if ((local_38 & 0xff) == 1) {
            if (iVar7 != 0) {
              iVar9 = 0;
              local_6c = DAT_000350ac;
              do {
/* ... truncated ... */
```

- `FUN_00035278` @ `00035278`

```c

int FUN_00035278(int param_1)

{
  int iVar1;
  int iVar2;
  int iVar3;
  uint uVar4;
  int iVar5;
  int iVar6;
  int iVar7;
  
  if (param_1 != 0) {
    iVar1 = FUN_000381e8();
    iVar6 = DAT_0003538c;
    if (iVar1 != 0) {
      iVar2 = 0;
      do {
        iVar5 = *(int *)(iVar2 * 4 + **(int **)(param_1 + 8));
        iVar3 = FUN_000325b0(iVar5,DAT_00035390);
        if (iVar3 == 0) {
          iVar7 = *(int *)(iVar5 + 0x20);
          iVar3 = FUN_00036ab8(iVar5,0,0x19);
          iVar7 = iVar7 + iVar3;
          if (iVar6 < iVar7) {
            iVar6 = iVar7;
          }
        }
        iVar2 = iVar2 + 1;
      } while (iVar1 != iVar2);
    }
    iVar1 = FUN_00036ab8(param_1,0,0x10);
    iVar2 = FUN_00036ab8(param_1,0,0x30);
    iVar3 = FUN_00036ab8(param_1,0,0x34);
    if (iVar3 << 0x1e < 0) {
      iVar1 = iVar1 + iVar2;
    }
    iVar2 = FUN_00036ab8(param_1,0,0x11);
    uVar4 = FUN_00036ab8(param_1,0,0x30);
    iVar3 = FUN_00036ab8(param_1,0,0x34);
    iVar2 = (uVar4 & (iVar3 << 0x1f) >> 0x1f) + iVar2;
    if (iVar6 != DAT_0003538c) {
      iVar6 = iVar6 - (*(int *)(param_1 + 0x20) - iVar2);
    }
    iVar3 = FUN_00033ebc(param_1);
    iVar5 = FUN_00033be4(param_1);
    iVar3 = iVar3 - ((iVar5 - iVar1) - iVar2);
    if (*(int *)(param_1 + 8) != 0) {
      iVar3 = iVar3 + *(int *)(*(int *)(param_1 + 8) + 0x24);
    }
    if (iVar6 < iVar3) {
      iVar6 = iVar3;
    }
    return iVar6;
  }
  FUN_000468e8(3,DAT_000353a4,0x8a,DAT_0003539c,DAT_000353a0,DAT_00035398,DAT_00035394);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

- `FUN_00035d20` @ `00035d20`

```c

void FUN_00035d20(int param_1,undefined4 *param_2,int *param_3)

{
  char cVar1;
  byte bVar2;
  uint uVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  int iVar7;
  int iVar8;
  uint uVar9;
  int iVar10;
  int iVar11;
  int iVar12;
  int iVar13;
  byte bVar14;
  uint uVar15;
  int local_5c;
  
  FUN_00045064(param_2,0,0,0xffffffff,0xffffffff);
  FUN_00045064(param_3,0,0,0xffffffff,0xffffffff);
  uVar3 = FUN_00032568(param_1,0x10);
  if (uVar3 == 0) {
    return;
  }
  if (*(int *)(param_1 + 8) == 0) {
    iVar12 = FUN_0004bd28(0);
    bVar14 = 3;
  }
  else {
    bVar2 = *(byte *)(*(int *)(param_1 + 8) + 0x32);
    bVar14 = bVar2 & 3;
    if ((bVar2 & 3) == 0) {
      return;
    }
    iVar12 = FUN_0004bd28(0);
    if (bVar14 == 2) {
      while( true ) {
        if (iVar12 == 0) {
          return;
        }
        iVar4 = FUN_0004bdc4(iVar12);
        if (param_1 == iVar4) break;
        iVar12 = FUN_0004bd28(iVar12);
      }
    }
  }
  if (*(int *)(param_1 + 8) == 0) {
    local_5c = 0;
  }
  else {
    local_5c = -*(int *)(*(int *)(param_1 + 8) + 0x24);
  }
  iVar4 = FUN_00035278(param_1);
  iVar5 = FUN_000353a8(param_1);
  iVar6 = FUN_0003550c(param_1);
  uVar15 = uVar3;
  if (*(int *)(param_1 + 8) == 0) {
    if (bVar14 == 1) goto LAB_00035e48;
    if (bVar14 == 3) {
      if ((0 < local_5c) || (0 < iVar4)) {
LAB_00036196:
        uVar3 = (uint)((iVar6 >> 0x1f) - iVar6 | (iVar5 >> 0x1f) - iVar5) >> 0x1f;
        goto LAB_00035e48;
      }
LAB_00035e36:
      if ((iVar5 < 1) && (iVar6 < 1)) {
        return;
      }
    }
    else {
      iVar13 = FUN_0004bda4(iVar12);
      if (iVar13 == 0xc) {
LAB_0003613c:
        iVar12 = FUN_0004bda4(iVar12);
        uVar3 = (uint)(iVar12 == 3);
        goto LAB_00035e48;
      }
/* ... truncated ... */
```

- `FUN_000386c0` @ `000386c0`

```c

void FUN_000386c0(int param_1)

{
  int iVar1;
  int iVar2;
  int *piVar3;
  undefined4 uVar4;
  int local_20;
  int local_1c;
  int local_18;
  int local_14;
  
  piVar3 = *(int **)(param_1 + 0x2b0);
  iVar2 = piVar3[0x11];
  while (iVar2 != 0) {
    FUN_0003b1d8();
    FUN_0003b0b8();
    iVar2 = piVar3[0x11];
  }
  iVar2 = FUN_0003a334(param_1);
  if (iVar2 != 0) {
    FUN_000385fc(*(undefined4 *)(DAT_000387a0 + 0x10));
  }
  *(undefined4 *)(param_1 + 0x34) = 1;
  if ((*(int *)(param_1 + 0x3c) << 0x1f < 0) && (*(int *)(param_1 + 0x3c) << 0x1e < 0)) {
    *(undefined4 *)(param_1 + 0x38) = 1;
  }
  else {
    *(undefined4 *)(param_1 + 0x38) = 0;
  }
  iVar2 = *(int *)(param_1 + 0x38);
  if (*(int *)(param_1 + 0x2c) != 0) {
    uVar4 = *(undefined4 *)(*piVar3 + 0x10);
    local_20 = *(int *)(param_1 + 0x310) + *(int *)(param_1 + 0x10);
    local_1c = *(int *)(param_1 + 0x314) + *(int *)(param_1 + 0x14);
    local_18 = *(int *)(param_1 + 0x318) + *(int *)(param_1 + 0x10);
    local_14 = *(int *)(param_1 + 0x31c) + *(int *)(param_1 + 0x14);
    FUN_0003a9d4(param_1,0x3d,&local_20);
    (**(code **)(param_1 + 0x2c))(param_1,&local_20,uVar4);
    FUN_0003a9d4(param_1,0x3e,&local_20);
  }
  iVar1 = FUN_0003a334(param_1);
  if ((iVar1 != 0) && ((*(char *)(param_1 + 0x3d) != '\x01' || (iVar2 != 0)))) {
    iVar2 = *(int *)(param_1 + 0x1c);
    if (*(int *)(param_1 + 0x28) == iVar2) {
      *(int *)(param_1 + 0x28) = *(int *)(param_1 + 0x20);
    }
    else if (*(int *)(param_1 + 0x28) == *(int *)(param_1 + 0x20)) {
      if (*(int *)(param_1 + 0x24) == 0) {
        *(int *)(param_1 + 0x28) = iVar2;
      }
      else {
        *(int *)(param_1 + 0x28) = *(int *)(param_1 + 0x24);
      }
    }
    else {
      *(int *)(param_1 + 0x28) = iVar2;
    }
  }
  return;
}
```

- `FUN_00038b1c` @ `00038b1c`

```c

/* WARNING: Restarted to delay deadcode elimination for space: stack */

void FUN_00038b1c(int param_1,int param_2)

{
  undefined1 uVar1;
  uint uVar2;
  undefined4 uVar3;
  int iVar4;
  uint uVar5;
  uint uVar6;
  uint uVar7;
  int iVar8;
  int iVar9;
  int iVar10;
  uint uVar11;
  uint uVar12;
  uint local_100;
  uint local_d4;
  uint *local_d0;
  undefined4 local_cc;
  int local_c8;
  uint local_c4;
  undefined4 uStack_c0;
  undefined4 uStack_bc;
  undefined4 local_b8;
  uint local_b4;
  uint *puStack_b0;
  undefined4 uStack_ac;
  int local_a8;
  uint local_a4;
  uint *local_a0;
  undefined4 local_9c;
  int local_98;
  uint local_94;
  uint *local_90;
  undefined4 uStack_8c;
  int local_88;
  int local_78;
  uint local_64;
  uint local_60;
  uint local_5c;
  uint local_58;
  uint local_54;
  int local_50;
  int local_4c;
  undefined1 uStack_44;
  byte bStack_43;
  uint local_3c;
  undefined4 uStack_38;
  undefined4 uStack_34;
  undefined4 local_30;
  uint local_2c;
  
  uVar2 = FUN_00036ab8(param_2,0,99);
  if ((uVar2 & 0xff) < 3) {
    return;
  }
  uVar11 = *(uint *)(param_1 + 0x38);
  uVar1 = *(undefined1 *)(param_1 + 0x3c);
  local_94 = uVar2;
  local_94 = FUN_00036ab8(param_2,0,0x62);
  if ((local_94 & 0xff) < 0xfd) {
    *(char *)(param_1 + 0x38) = (char)((local_94 & 0xff) * (uVar11 & 0xff) >> 8);
  }
  uVar3 = FUN_00037bf4(param_2,0,*(undefined4 *)(param_1 + 0x39));
  *(char *)(param_1 + 0x39) = (char)uVar3;
  *(char *)(param_1 + 0x3a) = (char)((uint)uVar3 >> 8);
  *(char *)(param_1 + 0x3c) = (char)((uint)uVar3 >> 0x18);
  *(char *)(param_1 + 0x3b) = (char)((uint)uVar3 >> 0x10);
  iVar4 = FUN_0003344c(param_2);
  if (iVar4 == 0) {
    FUN_00038814(param_1,param_2);
  }
  else {
    uVar3 = FUN_0003343c(param_2);
    FUN_00033b50(param_2,&local_c4);
    FUN_0004509c(&local_c4,uVar3,uVar3);
    if (iVar4 != 2) {
/* ... truncated ... */
```

- `FUN_000391d4` @ `000391d4`

```c

void FUN_000391d4(int *param_1,int param_2)

{
  byte bVar1;
  int iVar2;
  uint uVar3;
  uint uVar4;
  undefined4 uVar5;
  int *piVar6;
  undefined2 uVar7;
  int iVar8;
  int *piVar9;
  int iVar10;
  uint uVar11;
  int iVar12;
  int *piVar13;
  int iVar14;
  int *piVar15;
  undefined1 auStack_38 [12];
  int local_2c;
  
  iVar8 = DAT_00039414;
  iVar2 = *(int *)(DAT_00039414 + 0x10);
  piVar13 = *(int **)(iVar2 + 0x2b0);
  *piVar13 = *(int *)(iVar2 + 0x28);
  iVar10 = param_1[1];
  iVar14 = param_1[2];
  piVar13[6] = *param_1;
  piVar13[7] = iVar10;
  piVar13[8] = iVar14;
  piVar13[9] = param_1[3];
  iVar10 = param_1[1];
  iVar14 = param_1[2];
  piVar13[10] = *param_1;
  piVar13[0xb] = iVar10;
  piVar13[0xc] = iVar14;
  piVar13[0xd] = param_1[3];
  piVar13[0x10] = param_2;
  if (*(byte *)(iVar2 + 0x3d) == 0) {
    iVar2 = param_1[1];
    iVar10 = param_1[2];
    piVar13[1] = *param_1;
    piVar13[2] = iVar2;
    piVar13[3] = iVar10;
    piVar13[4] = param_1[3];
    FUN_000387a4(piVar13,0);
  }
  else if (*(byte *)(iVar2 + 0x3d) - 1 < 2) {
    piVar13[1] = 0;
    piVar13[2] = 0;
    iVar2 = FUN_0003acb4();
    if (iVar2 == 0) {
      iVar2 = FUN_0003a048(*(undefined4 *)(iVar8 + 0x10));
      piVar13[3] = iVar2 + -1;
      iVar2 = FUN_0003a070(*(undefined4 *)(iVar8 + 0x10));
    }
    else {
      iVar2 = FUN_0003a098(*(undefined4 *)(iVar8 + 0x10));
      piVar13[3] = iVar2 + -1;
      iVar2 = FUN_0003a0b0(*(undefined4 *)(iVar8 + 0x10));
    }
    bVar1 = *(byte *)(*(int *)(iVar8 + 0x10) + 0x3f);
    uVar7 = 0;
    piVar13[4] = iVar2 + -1;
    if (-1 < (int)((uint)bVar1 << 0x1e)) {
      uVar7 = *(undefined2 *)(*piVar13 + 8);
    }
    FUN_000387a4(piVar13,uVar7);
  }
  FUN_000458f0(param_1);
  if (3 < *(byte *)(piVar13 + 5) - 7) {
    uVar3 = FUN_0005b480(*(undefined4 *)(*piVar13 + 0xc),
                         (*(ushort *)(*(int *)(iVar8 + 0x10) + 0x3e) & 0x1ff) >> 1);
    iVar2 = FUN_00045088(param_1);
    iVar10 = FUN_00045c38((char)piVar13[5]);
    uVar11 = iVar10 * iVar2 + (uVar3 - 1);
    uVar4 = FUN_0005b480(uVar11,uVar3);
    uVar5 = FUN_000458f0(param_1);
    if (uVar4 != 1) {
/* ... truncated ... */
```

- `FUN_00039590` @ `00039590`

```c

void FUN_00039590(int param_1)

{
  char cVar1;
  int iVar2;
  int iVar3;
  undefined4 *puVar4;
  undefined4 uVar5;
  undefined4 *puVar6;
  uint uVar7;
  int iVar8;
  int iVar9;
  int iVar10;
  int iVar11;
  int iVar12;
  uint uVar13;
  uint uVar14;
  int iVar15;
  undefined4 uVar16;
  int iVar17;
  int iVar18;
  bool bVar19;
  undefined4 local_78;
  int local_74;
  int local_70;
  int local_6c;
  undefined4 local_68;
  int local_64;
  int local_60;
  int local_5c;
  
  iVar12 = DAT_000398e4;
  if (param_1 == 0) {
    iVar3 = FUN_0003a020();
    iVar12 = DAT_000398e4;
    *(int *)(DAT_000398e4 + 0x10) = iVar3;
  }
  else {
    *(undefined4 *)(DAT_000398e4 + 0x10) = *(undefined4 *)(param_1 + 0xc);
    FUN_0004889c();
    iVar3 = *(int *)(iVar12 + 0x10);
  }
  if (iVar3 == 0) {
    FUN_000468e8(2,DAT_00039c40,0x172,DAT_00039c3c,DAT_00039c38);
  }
  else {
    iVar10 = *(int *)(iVar3 + 0x28);
    if (((iVar10 == 0) || (*(int *)(iVar10 + 0x10) == 0)) || (*(int *)(iVar10 + 0xc) == 0)) {
      FUN_000468e8(2,DAT_000398f0,0x179,DAT_000398ec,DAT_000398e8);
    }
    else {
      FUN_0003a9d4(iVar3,0x39,0);
      FUN_00035164(*(undefined4 *)(*(int *)(iVar12 + 0x10) + 0x2c8));
      iVar3 = *(int *)(iVar12 + 0x10);
      if (*(int *)(iVar3 + 0x2d0) != 0) {
        FUN_00035164();
        iVar3 = *(int *)(iVar12 + 0x10);
      }
      FUN_00035164(*(undefined4 *)(iVar3 + 0x2cc));
      FUN_00035164(*(undefined4 *)(*(int *)(iVar12 + 0x10) + 0x2c4));
      FUN_00035164(*(undefined4 *)(*(int *)(iVar12 + 0x10) + 0x2c0));
      iVar3 = *(int *)(iVar12 + 0x10);
      if (*(int *)(iVar3 + 0x2c8) == 0) {
        *(undefined4 *)(iVar3 + 0x264) = 0;
        FUN_000468e8(2,DAT_00039c40,0x18d,DAT_00039c3c,DAT_00039c44);
      }
      else {
        uVar7 = *(uint *)(iVar3 + 0x264);
        if (uVar7 != 0) {
          cVar1 = *(char *)(iVar3 + 0x244);
          uVar14 = 0;
          while( true ) {
            if (cVar1 == '\0') {
              uVar13 = 0;
              iVar10 = uVar14 * 0x10 + 0x44;
              do {
                if ((*(char *)(iVar3 + uVar13 + 0x244) == '\0') && (uVar14 != uVar13)) {
                  iVar18 = uVar13 * 0x10 + 0x44;
                  iVar2 = FUN_00045434(iVar3 + iVar10,iVar3 + iVar18);
/* ... truncated ... */
```

- `FUN_0003bf98` @ `0003bf98`

```c

void FUN_0003bf98(int param_1,int param_2)

{
  ushort uVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  uint uVar5;
  int iVar6;
  undefined4 local_40;
  undefined4 local_3c;
  int local_38;
  int local_34;
  undefined4 local_30;
  int local_2c;
  int local_24;
  
  if (param_1 != 0) {
    uVar1 = *(ushort *)(param_1 + 8);
    if (param_2 == 0) {
      iVar2 = *(int *)(param_1 + 0x10);
      uVar5 = *(byte *)(param_1 + 1) - 7 & 0xff;
      if (uVar5 < 4) {
        iVar2 = iVar2 + *(int *)(uVar5 * 4 + DAT_0003c094);
      }
      FUN_00050350(iVar2,0,(uint)uVar1 * (uint)*(ushort *)(param_1 + 6));
      FUN_0003bb58(param_1,0);
    }
    else {
      local_40 = 0;
      local_3c = 0;
      local_38 = *(ushort *)(param_1 + 4) - 1;
      local_34 = *(ushort *)(param_1 + 6) - 1;
      iVar2 = FUN_000450d4(&local_30,param_2,&local_40);
      if (((iVar2 != 0) && (iVar2 = FUN_000458e4(&local_30), 0 < iVar2)) &&
         (iVar2 = FUN_000458f0(&local_30), 0 < iVar2)) {
        iVar2 = FUN_0003bf18(param_1,local_30,local_2c);
        iVar3 = FUN_00045bcc(*(undefined1 *)(param_1 + 1));
        iVar4 = FUN_000458e4(&local_30);
        if (local_2c <= local_24) {
          iVar6 = local_2c;
          do {
            FUN_00050350(iVar2,0,iVar3 * iVar4 + 7 >> 3);
            iVar6 = iVar6 + 1;
            iVar2 = iVar2 + (uint)uVar1;
          } while (iVar6 <= local_24);
        }
        FUN_0003bb58(param_1,param_2);
      }
    }
    return;
  }
  FUN_000468e8(3,DAT_0003c090,0xa5,DAT_0003c088,DAT_0003c08c,DAT_0003c084,DAT_0003c080);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

- `FUN_0003c6cc` @ `0003c6cc`

```c

void FUN_0003c6cc(undefined4 param_1,int param_2,int *param_3,int param_4)

{
  int iVar1;
  int iVar2;
  int iVar3;
  uint uVar4;
  int iVar5;
  uint uVar6;
  int local_a8;
  int local_a4;
  int local_a0;
  int local_9c;
  undefined4 local_94;
  undefined4 uStack_90;
  undefined4 uStack_8c;
  undefined4 local_88;
  undefined1 auStack_84 [16];
  undefined1 auStack_74 [80];
  
  if (param_4 == 0) {
    FUN_000468e8(2,DAT_0003c804,0xf9,DAT_0003c800,DAT_0003c808);
  }
  else {
    iVar1 = FUN_0003e060(auStack_74,*(undefined4 *)(param_2 + 0x1c),0);
    if (iVar1 == 1) {
      uVar6 = (uint)*(ushort *)(param_2 + 0x24);
      uVar4 = (uint)*(ushort *)(param_2 + 0x26);
      iVar1 = FUN_000458e4((int *)(param_2 + 0x58));
      if (iVar1 < 0) {
        local_a8 = *param_3;
        local_a4 = param_3[1];
        local_a0 = param_3[2];
        local_9c = param_3[3];
      }
      else {
        local_a8 = *(int *)(param_2 + 0x58);
        local_a4 = *(int *)(param_2 + 0x5c);
        local_a0 = *(int *)(param_2 + 0x60);
        local_9c = *(int *)(param_2 + 100);
      }
      FUN_00045070(&local_a8,uVar6);
      FUN_0004507c(&local_a8,uVar4);
      iVar1 = local_a8;
      local_94 = *DAT_0003c7f8;
      uStack_90 = DAT_0003c7f8[1];
      uStack_8c = DAT_0003c7f8[2];
      local_88 = DAT_0003c7f8[3];
      iVar2 = param_3[3];
      if (local_a4 <= iVar2) {
        iVar3 = param_3[2];
        iVar5 = uVar6 + local_a8 + -1;
        do {
          local_a8 = iVar1;
          if (iVar1 <= iVar3) {
            do {
              iVar2 = FUN_000450d4(auStack_84,&local_a8,param_3);
              if (iVar2 != 0) {
                FUN_0003c550(param_1,param_2,auStack_74,&local_94,&local_a8,auStack_84,param_4);
              }
              local_a0 = local_a0 + uVar6;
              iVar3 = param_3[2];
              local_a8 = uVar6 + local_a8;
            } while (local_a8 <= iVar3);
            iVar2 = param_3[3];
          }
          local_a4 = local_a4 + uVar4;
          local_9c = local_9c + uVar4;
          local_a0 = iVar5;
        } while (local_a4 <= iVar2);
      }
      local_a8 = iVar1;
      FUN_0003e180(auStack_74);
    }
    else {
      FUN_000468e8(3,DAT_0003c804,0x100,DAT_0003c800,DAT_0003c7fc);
    }
  }
  return;
/* ... truncated ... */
```

- `FUN_0003cc44` @ `0003cc44`

```c

void FUN_0003cc44(int param_1,int param_2,int *param_3,int param_4)

{
  undefined4 uVar1;
  undefined4 uVar2;
  int iVar3;
  int local_8c;
  int local_88;
  int local_84;
  int local_80;
  undefined1 auStack_7c [16];
  undefined1 auStack_6c [80];
  
  if (param_4 == 0) {
    FUN_000468e8(2,DAT_0003cd3c,0xd1,DAT_0003cd38,DAT_0003cd40);
  }
  else {
    local_80 = param_3[3];
    local_88 = param_3[1];
    local_8c = *param_3;
    local_84 = param_3[2];
    if (((*(int *)(param_2 + 0x30) != 0) || (*(int *)(param_2 + 0x34) != 0x100)) ||
       (*(int *)(param_2 + 0x38) != 0x100)) {
      uVar1 = FUN_000458e4(param_3);
      uVar2 = FUN_000458f0(param_3);
      FUN_0003c80c(&local_8c,uVar1,uVar2,*(undefined4 *)(param_2 + 0x30),
                   *(undefined2 *)(param_2 + 0x34),*(undefined2 *)(param_2 + 0x38),param_2 + 0x44);
      local_8c = local_8c + *param_3;
      local_88 = local_88 + param_3[1];
      local_84 = local_84 + *param_3;
      local_80 = local_80 + param_3[1];
    }
    iVar3 = FUN_000450d4(auStack_7c,&local_8c,param_1 + 0x38);
    if (iVar3 != 0) {
      iVar3 = FUN_0003e060(auStack_6c,*(undefined4 *)(param_2 + 0x1c),0);
      if (iVar3 == 1) {
        FUN_0003c550(param_1,param_2,auStack_6c,0,param_3,auStack_7c,param_4);
        FUN_0003e180(auStack_6c);
      }
      else {
        FUN_000468e8(3,DAT_0003cd3c,0xec,DAT_0003cd38,DAT_0003cd34);
      }
    }
  }
  return;
}
```

- truncated after 20 matches

### `standalone pad endpoints`

- `FUN_00038b1c` @ `00038b1c`

```c

/* WARNING: Restarted to delay deadcode elimination for space: stack */

void FUN_00038b1c(int param_1,int param_2)

{
  undefined1 uVar1;
  uint uVar2;
  undefined4 uVar3;
  int iVar4;
  uint uVar5;
  uint uVar6;
  uint uVar7;
  int iVar8;
  int iVar9;
  int iVar10;
  uint uVar11;
  uint uVar12;
  uint local_100;
  uint local_d4;
  uint *local_d0;
  undefined4 local_cc;
  int local_c8;
  uint local_c4;
  undefined4 uStack_c0;
  undefined4 uStack_bc;
  undefined4 local_b8;
  uint local_b4;
  uint *puStack_b0;
  undefined4 uStack_ac;
  int local_a8;
  uint local_a4;
  uint *local_a0;
  undefined4 local_9c;
  int local_98;
  uint local_94;
  uint *local_90;
  undefined4 uStack_8c;
  int local_88;
  int local_78;
  uint local_64;
  uint local_60;
  uint local_5c;
  uint local_58;
  uint local_54;
  int local_50;
  int local_4c;
  undefined1 uStack_44;
  byte bStack_43;
  uint local_3c;
  undefined4 uStack_38;
  undefined4 uStack_34;
  undefined4 local_30;
  uint local_2c;
  
  uVar2 = FUN_00036ab8(param_2,0,99);
  if ((uVar2 & 0xff) < 3) {
    return;
  }
  uVar11 = *(uint *)(param_1 + 0x38);
  uVar1 = *(undefined1 *)(param_1 + 0x3c);
  local_94 = uVar2;
  local_94 = FUN_00036ab8(param_2,0,0x62);
  if ((local_94 & 0xff) < 0xfd) {
    *(char *)(param_1 + 0x38) = (char)((local_94 & 0xff) * (uVar11 & 0xff) >> 8);
  }
  uVar3 = FUN_00037bf4(param_2,0,*(undefined4 *)(param_1 + 0x39));
  *(char *)(param_1 + 0x39) = (char)uVar3;
  *(char *)(param_1 + 0x3a) = (char)((uint)uVar3 >> 8);
  *(char *)(param_1 + 0x3c) = (char)((uint)uVar3 >> 0x18);
  *(char *)(param_1 + 0x3b) = (char)((uint)uVar3 >> 0x10);
  iVar4 = FUN_0003344c(param_2);
  if (iVar4 == 0) {
    FUN_00038814(param_1,param_2);
  }
  else {
    uVar3 = FUN_0003343c(param_2);
    FUN_00033b50(param_2,&local_c4);
    FUN_0004509c(&local_c4,uVar3,uVar3);
    if (iVar4 != 2) {
/* ... truncated ... */
```

- `FUN_0005cbe8` @ `0005cbe8`

```c

/* WARNING: Removing unreachable block (ram,0x0005d00e) */
/* WARNING: Removing unreachable block (ram,0x0005cff4) */
/* WARNING: Removing unreachable block (ram,0x0005d068) */
/* WARNING: Removing unreachable block (ram,0x0005d04e) */

uint FUN_0005cbe8(code *param_1,int param_2,uint param_3,byte *param_4,uint *param_5)

{
  char *pcVar1;
  byte bVar2;
  byte *pbVar3;
  int iVar4;
  int iVar5;
  byte *pbVar6;
  char cVar7;
  uint uVar8;
  byte *pbVar9;
  int iVar10;
  uint uVar11;
  char *pcVar12;
  char *pcVar13;
  uint uVar14;
  byte *pbVar15;
  uint uVar16;
  uint uVar17;
  uint *puVar18;
  undefined4 uVar19;
  uint *local_54;
  uint local_50;
  uint local_48;
  uint local_44;
  
  iVar5 = DAT_0005cf14;
  iVar4 = DAT_0005cf10;
  if (param_2 == 0) {
    bVar2 = *param_4;
    param_1 = DAT_0005d2b8;
  }
  else {
    bVar2 = *param_4;
  }
  uVar8 = (uint)bVar2;
  if (uVar8 == 0) {
    uVar17 = 0;
  }
  else {
    local_54 = param_5;
    uVar16 = 0;
    do {
      pbVar15 = param_4 + 1;
      if (uVar8 == 0x25) {
        uVar17 = 0;
        uVar8 = (uint)*pbVar15;
        pbVar9 = param_4 + 2;
        uVar14 = uVar8 - 0x20 & 0xff;
        if (uVar14 < 0x11) {
                    /* WARNING: Could not recover jumptable at 0x0005cc56. Too many branches */
                    /* WARNING: Treating indirect jump as call */
          uVar8 = (**(code **)(iVar4 + uVar14 * 4))();
          return uVar8;
        }
        if (uVar8 - 0x30 < 10) {
          uVar14 = 0;
          while( true ) {
            iVar10 = uVar14 * 10 + uVar8;
            uVar8 = (uint)*pbVar9;
            uVar14 = iVar10 - 0x30;
            if (9 < uVar8 - 0x30) break;
            pbVar9 = pbVar9 + 1;
          }
          pbVar6 = pbVar9 + 1;
          pbVar3 = pbVar9;
        }
        else {
          uVar14 = 0;
          pbVar6 = pbVar9;
          pbVar3 = pbVar15;
          if (uVar8 == 0x2a) {
            uVar14 = *local_54;
/* ... truncated ... */
```


### `encoder plus wheel`

- `FUN_0000408c` @ `0000408c`

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
/* ... truncated ... */
```

- `FUN_000041fc` @ `000041fc`

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
/* ... truncated ... */
```

- `FUN_000501dc` @ `000501dc`

```c

void FUN_000501dc(undefined4 *param_1,undefined4 *param_2,uint param_3)

{
  undefined4 *puVar1;
  undefined1 *puVar2;
  undefined1 uVar3;
  undefined4 *puVar4;
  undefined4 *puVar5;
  uint uVar6;
  
  if (((uint)param_1 & 3) == ((uint)param_2 & 3)) {
    if (((uint)param_1 & 3) != 0) {
      uVar6 = (uint)param_1 & 0xfffffffc;
      do {
        if (param_3 == 0) {
          return;
        }
        param_3 = param_3 - 1;
        *(undefined1 *)param_1 = *(undefined1 *)param_2;
        param_1 = (undefined4 *)((int)param_1 + 1);
        param_2 = (undefined4 *)((int)param_2 + 1);
      } while (param_1 != (undefined4 *)(uVar6 + 4));
    }
    if (0x20 < param_3) {
      uVar6 = param_3 - 0x21 >> 5;
      puVar5 = param_1;
      puVar4 = param_2;
      do {
        *puVar5 = *puVar4;
        puVar5[1] = puVar4[1];
        puVar5[2] = puVar4[2];
        puVar5[3] = puVar4[3];
        puVar5[4] = puVar4[4];
        puVar5[5] = puVar4[5];
        puVar5[6] = puVar4[6];
        puVar1 = puVar4 + 7;
        puVar4 = puVar4 + 8;
        puVar5[7] = *puVar1;
        puVar5 = puVar5 + 8;
      } while (puVar4 != param_2 + (uVar6 + 1) * 8);
      param_3 = (param_3 - 0x20) + uVar6 * -0x20;
      param_1 = param_1 + uVar6 * 8 + 8;
      param_2 = param_2 + uVar6 * 8 + 8;
    }
    if (param_3 != 0) {
      puVar5 = (undefined4 *)((int)param_2 + param_3);
      do {
        uVar3 = *(undefined1 *)param_2;
        param_2 = (undefined4 *)((int)param_2 + 1);
        *(undefined1 *)param_1 = uVar3;
        param_1 = (undefined4 *)((int)param_1 + 1);
      } while (param_2 != puVar5);
    }
  }
  else {
    if (0x20 < param_3) {
      uVar6 = param_3 - 0x21 >> 5;
      puVar5 = param_1;
      puVar4 = param_2;
      do {
        *(undefined1 *)puVar5 = *(undefined1 *)puVar4;
        *(undefined1 *)((int)puVar5 + 1) = *(undefined1 *)((int)puVar4 + 1);
        *(undefined1 *)((int)puVar5 + 2) = *(undefined1 *)((int)puVar4 + 2);
        *(undefined1 *)((int)puVar5 + 3) = *(undefined1 *)((int)puVar4 + 3);
        *(undefined1 *)(puVar5 + 1) = *(undefined1 *)(puVar4 + 1);
        *(undefined1 *)((int)puVar5 + 5) = *(undefined1 *)((int)puVar4 + 5);
        *(undefined1 *)((int)puVar5 + 6) = *(undefined1 *)((int)puVar4 + 6);
        *(undefined1 *)((int)puVar5 + 7) = *(undefined1 *)((int)puVar4 + 7);
        *(undefined1 *)(puVar5 + 2) = *(undefined1 *)(puVar4 + 2);
        *(undefined1 *)((int)puVar5 + 9) = *(undefined1 *)((int)puVar4 + 9);
        *(undefined1 *)((int)puVar5 + 10) = *(undefined1 *)((int)puVar4 + 10);
        *(undefined1 *)((int)puVar5 + 0xb) = *(undefined1 *)((int)puVar4 + 0xb);
        *(undefined1 *)(puVar5 + 3) = *(undefined1 *)(puVar4 + 3);
        *(undefined1 *)((int)puVar5 + 0xd) = *(undefined1 *)((int)puVar4 + 0xd);
        *(undefined1 *)((int)puVar5 + 0xe) = *(undefined1 *)((int)puVar4 + 0xe);
        *(undefined1 *)((int)puVar5 + 0xf) = *(undefined1 *)((int)puVar4 + 0xf);
        *(undefined1 *)(puVar5 + 4) = *(undefined1 *)(puVar4 + 4);
        *(undefined1 *)((int)puVar5 + 0x11) = *(undefined1 *)((int)puVar4 + 0x11);
        *(undefined1 *)((int)puVar5 + 0x12) = *(undefined1 *)((int)puVar4 + 0x12);
/* ... truncated ... */
```

- `FUN_00054b48` @ `00054b48`

```c

void FUN_00054b48(uint param_1)

{
  byte bVar1;
  ushort uVar2;
  byte bVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  int iVar7;
  int iVar8;
  int iVar9;
  uint uVar10;
  int iVar11;
  int iVar12;
  undefined4 uVar13;
  uint extraout_r1;
  int extraout_r2;
  uint uVar14;
  uint uVar15;
  uint uVar16;
  int *piVar17;
  int *piVar18;
  uint extraout_r3;
  int iVar19;
  uint uVar20;
  uint uVar21;
  uint unaff_r10;
  undefined8 uVar22;
  int *piStack_dc;
  undefined4 local_d8;
  uint local_d4;
  int local_d0;
  uint uStack_cc;
  uint local_bc;
  uint uStack_b8;
  uint local_b4;
  int *local_b0;
  int iStack_ac;
  code *pcStack_a8;
  code *pcStack_a4;
  int iStack_a0;
  int iStack_9c;
  uint uStack_98;
  code *pcStack_94;
  code *pcStack_90;
  code *pcStack_8c;
  code *pcStack_88;
  uint uStack_84;
  code *pcStack_80;
  uint uStack_7c;
  uint uStack_78;
  uint local_74;
  ushort uStack_6c;
  undefined1 local_6a;
  byte local_69;
  int local_68;
  int local_64;
  uint local_60;
  int iStack_5c;
  int iStack_58;
  uint uStack_54;
  undefined4 uStack_50;
  undefined4 uStack_4c;
  undefined4 uStack_48;
  uint local_44;
  int iStack_40;
  int iStack_3c;
  undefined4 uStack_38;
  int *piStack_34;
  uint uStack_30;
  byte bStack_2c;
  
  local_44 = FUN_00036ab8(param_1,0,0x7a);
  local_69 = (byte)(((int)(local_44 & 0xff) >> 2 & 1U) << 1) | ~(byte)local_44 & 1 |
             (byte)(((int)(local_44 & 0xff) >> 3 & 1U) << 2) | local_69 & 0xf8;
  local_44 = FUN_00036ab8(param_1,0,0x7b);
  uVar20 = local_44 & 0xff;
  local_44 = FUN_00036ab8(param_1,0,0x7c);
/* ... truncated ... */
```


### `noteoff ch16 decoded`

- `FUN_00022b70` @ `00022b70`

```c

undefined4 FUN_00022b70(void)

{
  undefined1 *puVar1;
  int *piVar2;
  int iVar3;
  undefined1 *puVar4;
  undefined1 uVar5;
  undefined1 uVar6;
  byte bVar7;
  uint uVar8;
  int iVar9;
  byte *pbVar10;
  undefined1 *puVar11;
  char cVar12;
  int iVar13;
  char cVar14;
  short sVar15;
  
  uVar5 = FUN_0002ec30(0x2c);
  puVar1 = DAT_00022c44;
  cVar14 = '\x0f';
  DAT_00022c44[4] = 0xf;
  puVar1[2] = 6;
  cVar12 = '\b';
  uVar6 = FUN_0002ec30(0x30);
  *puVar1 = uVar6;
  puVar4 = puVar1;
  do {
    puVar11 = puVar4;
    puVar11[1] = cVar12;
    cVar14 = cVar14 + '\x10';
    puVar11[9] = cVar14;
    puVar11[7] = 6;
    uVar6 = FUN_0002ec30(0x30);
    cVar12 = cVar12 + '\b';
    puVar11[5] = uVar6;
    puVar4 = puVar11 + 5;
  } while (cVar12 != -0x80);
  puVar11[6] = 0x7f;
  piVar2 = DAT_00022c48;
  sVar15 = 0;
  pbVar10 = puVar1 + 0x50;
  iVar13 = DAT_00022c4c;
  do {
    while( true ) {
      pbVar10[4] = 0xff;
      pbVar10[3] = (byte)*(undefined2 *)(*piVar2 + iVar13 + 0x14);
      bVar7 = FUN_0002edc4(uVar5,sVar15,3);
      *pbVar10 = bVar7;
      uVar8 = FUN_0002ec30(0x30);
      iVar3 = DAT_00022c50;
      if (uVar8 != bVar7) break;
      sVar15 = sVar15 + 1;
      iVar9 = *piVar2 + iVar13;
      iVar13 = iVar13 + 0x16;
      pbVar10[2] = (byte)*(undefined2 *)(iVar9 + 0x14);
      pbVar10 = pbVar10 + 5;
      if (iVar13 == iVar3) {
        return 0;
      }
    }
    bVar7 = FUN_0002edc4(uVar5,sVar15,0);
    iVar3 = DAT_00022c50;
    iVar13 = iVar13 + 0x16;
    pbVar10[2] = bVar7;
    sVar15 = sVar15 + 1;
    pbVar10 = pbVar10 + 5;
  } while (iVar13 != iVar3);
  return 0;
}
```

- `FUN_0005f274` @ `0005f274`

```c

int * FUN_0005f274(undefined4 *param_1,uint param_2)

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
LAB_0005f434:
      *param_1 = 0xc;
      return (int *)0x0;
    }
    FUN_0005f7d8();
    uVar17 = 0x10;
    iVar9 = 0x18;
    uVar16 = 2;
  }
  else {
    uVar17 = uVar16 & 0xfffffff8;
    if (((int)uVar17 < 0) || (uVar17 < param_2)) goto LAB_0005f434;
    FUN_0005f7d8();
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
      else if (DAT_0005f7d4 < uVar5) {
        uVar5 = 0x7f;
        uVar15 = 0x7e;
        iVar9 = 0x3f8;
      }
      else {
        uVar15 = (uVar16 >> 0x12) + 0x7c;
        uVar5 = (uVar16 >> 0x12) + 0x7d;
        iVar9 = uVar5 * 8;
      }
      iVar14 = *(int *)(DAT_0005f5c4 + iVar9 + 4);
      do {
        iVar18 = iVar14;
/* ... truncated ... */
```


### `midi status classes`

- no function matches

### `fender global settings sysex`

- no function matches

## Data Proximity Windows

### `native transport tap/rec/play/stop`

- no non-executable data windows

### `pre-native transport symptom`

- no non-executable data windows

### `native nav`

- no non-executable data windows

### `native pad endpoints`

- no non-executable data windows

### `native pad lane starts`

- no non-executable data windows

### `standalone pad endpoints`

- no non-executable data windows

### `encoder plus wheel`

- no non-executable data windows

### `noteoff ch16 decoded`

- no non-executable data windows

### `midi status classes`

- no non-executable data windows

### `fender global settings sysex`

- no non-executable data windows

