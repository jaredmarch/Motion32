# Motion 32 — the emitters and the config selector

Program: `motion32_fw_payload_0x1000.bin`  
Image base: `00000000`

Only useful against the **payload** import; these are payload addresses.

## 1. The six roots, decompiled, with callers and writers

### `FUN_00000e50` @ `00000e50`

```c

undefined1 FUN_00000e50(void)

{
  return DAT_20004291;
}


```

**Callers:**

```text
FUN_00000bf0 @ 00000bf0   [UNCONDITIONAL_CALL from 00000c20]
FUN_00001030 @ 00001030   [UNCONDITIONAL_CALL from 00001036]
FUN_000010a4 @ 000010a4   [UNCONDITIONAL_CALL from 00001102]
FUN_0000134c @ 0000134c   [UNCONDITIONAL_CALL from 00001386]
FUN_0000134c @ 0000134c   [UNCONDITIONAL_CALL from 000013a8]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 000014f8]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 00001514]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 00001534]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 00001554]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 00001574]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 0000159a]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 000015ba]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 000015da]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 000015f8]
FUN_000016f4 @ 000016f4   [UNCONDITIONAL_CALL from 000016f6]
FUN_000018d0 @ 000018d0   [UNCONDITIONAL_CALL from 000018e4]
FUN_00001b08 @ 00001b08   [UNCONDITIONAL_CALL from 00001b1c]
FUN_000020cc @ 000020cc   [UNCONDITIONAL_CALL from 000020de]
FUN_00002370 @ 00002370   [UNCONDITIONAL_CALL from 00002376]
FUN_000088c4 @ 000088c4   [UNCONDITIONAL_CALL from 000088c6]
FUN_000088e4 @ 000088e4   [UNCONDITIONAL_CALL from 000088e6]
FUN_00008904 @ 00008904   [UNCONDITIONAL_CALL from 00008906]
FUN_00008924 @ 00008924   [UNCONDITIONAL_CALL from 00008926]
FUN_00008944 @ 00008944   [UNCONDITIONAL_CALL from 00008b3c]
FUN_00008944 @ 00008944   [UNCONDITIONAL_CALL from 00008b7c]
FUN_00008e1c @ 00008e1c   [UNCONDITIONAL_CALL from 00008efe]
```

**Globals this function touches, and who else WRITES them:**

```text
  20004291  =   (uninitialised)
      written by FUN_00000e5c @ 00000e5c  at 00000e82
```

### `FUN_00000fb0` @ `00000fb0`

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

**Callers:**

```text
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 0000150c]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 0000152c]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 0000154c]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 0000156c]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 0000158c]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 000015b2]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 000015d2]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 000015f2]
FUN_0000140c @ 0000140c   [UNCONDITIONAL_CALL from 00001610]
```

**Globals this function touches, and who else WRITES them:**

```text
  20004081  =   (uninitialised)
      written by FUN_00000eec @ 00000eec  at 00000f08
      written by FUN_00000eec @ 00000eec  at 00000f40
      written by FUN_00000f6c @ 00000f6c  at 00000f7e
      written by FUN_00000fb0 @ 00000fb0  at 00000fc4
```

### `FUN_00000eec` @ `00000eec`

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

**Callers:**

```text
FUN_00001288 @ 00001288   [UNCONDITIONAL_CALL from 0000131e]
FUN_00001288 @ 00001288   [UNCONDITIONAL_CALL from 0000133c]
```

**Globals this function touches, and who else WRITES them:**

```text
  20004081  =   (uninitialised)
      written by FUN_00000eec @ 00000eec  at 00000f08
      written by FUN_00000eec @ 00000eec  at 00000f40
      written by FUN_00000f6c @ 00000f6c  at 00000f7e
      written by FUN_00000fb0 @ 00000fb0  at 00000fc4
```

### `FUN_000016f4` @ `000016f4`

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

**Callers:**

```text
FUN_00000e5c @ 00000e5c   [UNCONDITIONAL_CALL from 00000eb0]
```

**Globals this function touches, and who else WRITES them:**

```text
  200045cc  =   (uninitialised)
      written by FUN_000016f4 @ 000016f4  at 0000170a
  200045cb  =   (uninitialised)
      written by FUN_000016f4 @ 000016f4  at 00001716
  200045ca  =   (uninitialised)
      written by FUN_000016f4 @ 000016f4  at 00001728
  0000179c  = 0x20004540
  20004540  =   (uninitialised)
  000095fc  = 0x02050206
  00009600  = 0x090f0407
  00000407  = 0x0ffffcff
  20004542  =   (uninitialised)
      written by FUN_000016f4 @ 000016f4  at 00001742
      written by (no function)  at 00001266
  00001201  = 0xccf244b5
  000011f5  = 0xfdf7ffb5
```

### `FUN_0000140c` @ `0000140c`

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

**Callers:**

```text
FUN_00008944 @ 00008944   [UNCONDITIONAL_CALL from 00008aa2]
FUN_00008e1c @ 00008e1c   [UNCONDITIONAL_CALL from 00008f56]
```

**Globals this function touches, and who else WRITES them:**

```text
  200045cc  =   (uninitialised)
      written by FUN_000016f4 @ 000016f4  at 0000170a
  20004538  =   (uninitialised)
      written by (no function)  at 00001276
      written by (no function)  at 00001228
  2000453c  =   (uninitialised)
      written by FUN_0000140c @ 0000140c  at 00001430
  20004548  =   (uninitialised)
  2000454c  =   (uninitialised)
      written by FUN_0000140c @ 0000140c  at 00001446
  20004558  =   (uninitialised)
  2000455c  =   (uninitialised)
      written by FUN_0000140c @ 0000140c  at 0000145c
  20004568  =   (uninitialised)
  2000456c  =   (uninitialised)
      written by FUN_0000140c @ 0000140c  at 00001472
  20004578  =   (uninitialised)
  2000457c  =   (uninitialised)
      written by FUN_0000140c @ 0000140c  at 0000148a
  20004588  =   (uninitialised)
  2000458c  =   (uninitialised)
      written by FUN_0000140c @ 0000140c  at 000014a2
  20004598  =   (uninitialised)
  2000459c  =   (uninitialised)
      written by FUN_0000140c @ 0000140c  at 000014ba
  200045a8  =   (uninitialised)
  200045ac  =   (uninitialised)
      written by FUN_0000140c @ 0000140c  at 000014d2
  200045b8  =   (uninitialised)
  200045bc  =   (uninitialised)
      written by FUN_0000140c @ 0000140c  at 000014ee
  00009664  = 0x07050300
  00009665  = 0x01070503
  00009666  = 0x02010705
  00009667  = 0x04020107
  00009668  = 0x06040201
  0000966a  = 0x02080604
  0000966b  = 0x08020806
  0000966c  = 0x06080208
  00009669  = 0x08060402
```

### `FUN_00001288` @ `00001288`

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

**Callers:**

```text
FUN_00008944 @ 00008944   [UNCONDITIONAL_CALL from 00008aba]
FUN_00008e1c @ 00008e1c   [UNCONDITIONAL_CALL from 00008f6e]
```

**Globals this function touches, and who else WRITES them:**

```text
  200045ca  =   (uninitialised)
      written by FUN_000016f4 @ 000016f4  at 00001728
  200045c8  =   (uninitialised)
      written by FUN_0000134c @ 0000134c  at 00001406
  200045c9  =   (uninitialised)
      written by FUN_00001288 @ 00001288  at 00001344
      written by FUN_0000134c @ 0000134c  at 000013e0
  20004536  =   (uninitialised)
      written by FUN_00001288 @ 00001288  at 00001318
  20004534  =   (uninitialised)
      written by FUN_00001288 @ 00001288  at 00001318
```

## 1b. Queue users, found via MOVW/MOVT rather than references

`getReferencesTo` and a literal-pool scan both return nothing for these
addresses because ARMv7-M builds 32-bit constants with MOVW/MOVT immediates,
so the address never exists as bytes anywhere. Both anchors are real.

### Inbound queue `0x200040a0` — the command parser

- `00002ad4` is not inside a defined function

### `FUN_00002a14` @ `00002a14`

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

**Callers:**

```text
FUN_00000e5c @ 00000e5c
```

**Every constant `<= 0x7f` — the candidate command ids:**

```text
0x01  (00002a28  movs r2,#0x1)
0x01  (00002a30  cmp r4,#0x1)
```

### `FUN_00002ab8` @ `00002ab8`

```c

undefined4 FUN_00002ab8(void)

{
  return 0x200040a0;
}


```

**Callers:**

```text
FUN_000010a4 @ 000010a4
```

**Every constant `<= 0x7f` — the candidate command ids:**

```text
```

### Outbound ring `0x20004084` — remaining event emitters


### `FUN_00000f6c` @ `00000f6c`

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

**Callers:**

```text
FUN_0000134c @ 0000134c
```

### `FUN_00000ff4` @ `00000ff4`

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

**Callers:**

```text
(none)
```

### `FUN_00001030` @ `00001030`

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

**Callers:**

```text
FUN_00008944 @ 00008944
FUN_00008e1c @ 00008e1c
```

## 2. One level down

Distinct callees: **5**

### `FUN_00000d6c` @ `00000d6c`

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

### `FUN_00004df4` @ `00004df4`

```c

undefined4 FUN_00004df4(undefined4 param_1,uint param_2,undefined1 *param_3)

{
  *param_3 = (char)((*(uint *)(&DAT_40040800 + ((param_2 >> 8) * 0x10 + (param_2 & 0xff)) * 4) & 3)
                   >> 1);
  return 0;
}


```

### `FUN_00001834` @ `00001834`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00001834(uint param_1,uint param_2,uint *param_3)

{
  uint *puVar1;
  uint uVar2;
  uint *puVar3;
  uint uVar4;
  
  param_1 = param_1 / 500;
  *param_3 = param_1;
  uVar4 = param_2 / 500 & -(uint)(param_2 / 500 < param_1);
  uVar2 = FUN_000029c8();
  puVar1 = _DAT_200045f4;
  uVar2 = uVar2 - param_1 * (uVar2 / param_1);
  if (uVar4 < uVar2) {
    param_3[1] = (param_1 + uVar4) - uVar2;
  }
  else {
    param_3[1] = uVar4 - uVar2;
  }
  if (puVar1 == (uint *)0x0) {
    _DAT_200045f4 = param_3;
    param_3[2] = 0;
  }
  else {
    do {
      puVar3 = puVar1;
      if (puVar3 == param_3) {
        return;
      }
      puVar1 = (uint *)puVar3[2];
    } while ((uint *)puVar3[2] != (uint *)0x0);
    puVar3[2] = (uint)param_3;
    param_3[2] = 0;
  }
  return;
}


```

### `FUN_000017a0` @ `000017a0`

```c

void FUN_000017a0(undefined4 *param_1,undefined4 param_2)

{
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  param_1[3] = param_2;
  return;
}


```

### `FUN_000017ac` @ `000017ac`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_000017ac(int param_1)

{
  int iVar1;
  int iVar2;
  
  iVar1 = _DAT_200045fc;
  if (_DAT_200045fc == 0) {
    _DAT_200045fc = param_1;
    *(undefined4 *)(param_1 + 8) = 0;
  }
  else {
    do {
      iVar2 = iVar1;
      if (iVar2 == param_1) {
        return;
      }
      iVar1 = *(int *)(iVar2 + 8);
    } while (*(int *)(iVar2 + 8) != 0);
    *(int *)(iVar2 + 8) = param_1;
    *(undefined4 *)(param_1 + 8) = 0;
  }
  return;
}


```

## 3. Peripheral vs RAM, per root

Cortex-M map: `0x40000000-0x5fffffff` peripheral, `0x20000000-0x3fffffff` SRAM,
`0x00000000-0x1fffffff` flash. A selector reading peripheral or flash is strapped;
one reading SRAM is set by software and therefore potentially reachable.

### `FUN_00000e50`

```text
  SRAM           20004291
```

### `FUN_00000fb0`

```text
  SRAM           20004081
```

### `FUN_00000eec`

```text
  SRAM           20004081
```

### `FUN_000016f4`

```text
  SRAM           200045cc
  SRAM           200045cb
  SRAM           200045ca
  FLASH/RODATA   0000179c
  SRAM           20004540
  FLASH/RODATA   000095fc
  FLASH/RODATA   00009600
  FLASH/RODATA   00000407
  SRAM           20004542
  FLASH/RODATA   00001201
  FLASH/RODATA   000011f5
```

### `FUN_0000140c`

```text
  SRAM           200045cc
  SRAM           20004538
  SRAM           2000453c
  SRAM           20004548
  SRAM           2000454c
  SRAM           20004558
  SRAM           2000455c
  SRAM           20004568
  SRAM           2000456c
  SRAM           20004578
  SRAM           2000457c
  SRAM           20004588
  SRAM           2000458c
  SRAM           20004598
  SRAM           2000459c
  SRAM           200045a8
  SRAM           200045ac
  SRAM           200045b8
  SRAM           200045bc
  FLASH/RODATA   00009664
  FLASH/RODATA   00009665
  FLASH/RODATA   00009666
  FLASH/RODATA   00009667
  FLASH/RODATA   00009668
  FLASH/RODATA   0000966a
  FLASH/RODATA   0000966b
  FLASH/RODATA   0000966c
  FLASH/RODATA   00009669
```

### `FUN_00001288`

```text
  SRAM           200045ca
  FLASH/RODATA   Stack[-0x2c]
  SRAM           200045c8
  SRAM           200045c9
  SRAM           20004536
  SRAM           20004534
```


---

## Reading order

1. `FUN_00000e50`. A read of a GPIO input register or an OTP/flash word means
   configuration is strapped at boot and no handshake can change it. A read of
   plain RAM means something writes it, and section 1 lists the writers.
2. `FUN_00000fb0` and `FUN_00000eec`. Any branch on a global inside these is
   the host-takeover switch. Its writers are the native-mode entry path.
3. Section 3 classifies every global each root touches as peripheral vs RAM,
   so question 1 can be answered without reading ARM by hand.
