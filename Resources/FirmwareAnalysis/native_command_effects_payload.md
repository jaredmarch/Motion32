# Motion 32 Native Command Effects Probe

## Focus Functions

### `00001e5c` `FUN_00001b44`

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
  if (1 < bVar3) {
    if ((short)((uint)_DAT_20005a30 >> 8) < -0x1e) {
      FUN_00001ac8(1);
      FUN_00009568(0x2000482c,0,0x200);
      _DAT_20005a30 = 0;
      bVar3 = DAT_20005a56;
    }
    if (2 < bVar3) {
      if ((short)((uint)_DAT_20005a34 >> 8) < -0x1e) {
        FUN_00001ac8(2);
        FUN_00009568(0x20004a2c,0,0x200);
        _DAT_20005a34 = 0;
        bVar3 = DAT_20005a56;
      }
      if (3 < bVar3) {
        if ((short)((uint)_DAT_20005a38 >> 8) < -0x1e) {
          FUN_00001ac8(3);
          FUN_00009568(0x20004c2c,0,0x200);
          _DAT_20005a38 = 0;
          bVar3 = DAT_20005a56;
        }
        if (4 < bVar3) {
          if ((short)((uint)_DAT_20005a3c >> 8) < -0x1e) {
            FUN_00001ac8(4);
            FUN_00009568(0x20004e2c,0,0x200);
            _DAT_20005a3c = 0;
            bVar3 = DAT_20005a56;
          }
          if (5 < bVar3) {
            if ((short)((uint)_DAT_20005a40 >> 8) < -0x1e) {
              FUN_00001ac8(5);
              FUN_00009568(0x2000502c,0,0x200);
              _DAT_20005a40 = 0;
              bVar3 = DAT_20005a56;
            }
            if (6 < bVar3) {
              if ((short)((uint)_DAT_20005a44 >> 8) < -0x1e) {
                FUN_00001ac8(6);
                FUN_00009568(0x2000522c,0,0x200);
                _DAT_20005a44 = 0;
                bVar3 = DAT_20005a56;
              }
              if (7 < bVar3) {
                if ((short)((uint)_DAT_20005a48 >> 8) < -0x1e) {
                  FUN_00001ac8(7);
                  FUN_00009568(0x2000542c,0,0x200);
                  _DAT_20005a48 = 0;
                  bVar3 = DAT_20005a56;
                }
                if (8 < bVar3) {
                  if ((short)((uint)_DAT_20005a4c >> 8) < -0x1e) {
                    FUN_00001ac8(8);
                    FUN_00009568(0x2000562c,0,0x200);
                    _DAT_20005a4c = 0;
                    bVar3 = DAT_20005a56;
                  }
                  if ((9 < bVar3) && ((short)((uint)_DAT_20005a50 >> 8) < -0x1e)) {
                    FUN_00001ac8(9);
                    FUN_00009568(0x2000582c,0,0x200);
                    _DAT_20005a50 = 0;
/* ... truncated ... */
```

Callers:
- none

### `00001e50` `FUN_00001b44`

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
  if (1 < bVar3) {
    if ((short)((uint)_DAT_20005a30 >> 8) < -0x1e) {
      FUN_00001ac8(1);
      FUN_00009568(0x2000482c,0,0x200);
      _DAT_20005a30 = 0;
      bVar3 = DAT_20005a56;
    }
    if (2 < bVar3) {
      if ((short)((uint)_DAT_20005a34 >> 8) < -0x1e) {
        FUN_00001ac8(2);
        FUN_00009568(0x20004a2c,0,0x200);
        _DAT_20005a34 = 0;
        bVar3 = DAT_20005a56;
      }
      if (3 < bVar3) {
        if ((short)((uint)_DAT_20005a38 >> 8) < -0x1e) {
          FUN_00001ac8(3);
          FUN_00009568(0x20004c2c,0,0x200);
          _DAT_20005a38 = 0;
          bVar3 = DAT_20005a56;
        }
        if (4 < bVar3) {
          if ((short)((uint)_DAT_20005a3c >> 8) < -0x1e) {
            FUN_00001ac8(4);
            FUN_00009568(0x20004e2c,0,0x200);
            _DAT_20005a3c = 0;
            bVar3 = DAT_20005a56;
          }
          if (5 < bVar3) {
            if ((short)((uint)_DAT_20005a40 >> 8) < -0x1e) {
              FUN_00001ac8(5);
              FUN_00009568(0x2000502c,0,0x200);
              _DAT_20005a40 = 0;
              bVar3 = DAT_20005a56;
            }
            if (6 < bVar3) {
              if ((short)((uint)_DAT_20005a44 >> 8) < -0x1e) {
                FUN_00001ac8(6);
                FUN_00009568(0x2000522c,0,0x200);
                _DAT_20005a44 = 0;
                bVar3 = DAT_20005a56;
              }
              if (7 < bVar3) {
                if ((short)((uint)_DAT_20005a48 >> 8) < -0x1e) {
                  FUN_00001ac8(7);
                  FUN_00009568(0x2000542c,0,0x200);
                  _DAT_20005a48 = 0;
                  bVar3 = DAT_20005a56;
                }
                if (8 < bVar3) {
                  if ((short)((uint)_DAT_20005a4c >> 8) < -0x1e) {
                    FUN_00001ac8(8);
                    FUN_00009568(0x2000562c,0,0x200);
                    _DAT_20005a4c = 0;
                    bVar3 = DAT_20005a56;
                  }
                  if ((9 < bVar3) && ((short)((uint)_DAT_20005a50 >> 8) < -0x1e)) {
                    FUN_00001ac8(9);
                    FUN_00009568(0x2000582c,0,0x200);
                    _DAT_20005a50 = 0;
/* ... truncated ... */
```

Callers:
- `FUN_00001b44` @ `00001b44` from `00001e4c` type=CONDITIONAL_JUMP
- `FUN_00001b44` @ `00001b44` from `00001f78` type=UNCONDITIONAL_JUMP

### `00003a14` `FUN_00003914`

```c

int FUN_00003914(int param_1,int *param_2)

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
          if (-1 < iVar2) {
            uVar9 = (undefined2)
                    ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                    (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 2));
          }
          puVar8[1] = uVar9;
          if (uVar3 != 2) {
            iVar2 = (uint)puVar5[2] - ((uint)local_4e - (uint)local_50);
            uVar9 = 0;
            if (-1 < iVar2) {
              uVar9 = (undefined2)
                      ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                      (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 4));
            }
            puVar8[2] = uVar9;
            if (uVar3 != 3) {
              iVar2 = (uint)puVar5[3] - ((uint)local_4a - (uint)local_4c);
              uVar9 = 0;
              if (-1 < iVar2) {
                uVar9 = (undefined2)
                        ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                        (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 6));
              }
              puVar8[3] = uVar9;
              if (uVar3 != 4) {
                iVar2 = (uint)puVar5[4] - ((uint)local_46 - (uint)local_48);
                uVar9 = 0;
                if (-1 < iVar2) {
                  uVar9 = (undefined2)
                          ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                          (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 8));
                }
                puVar8[4] = uVar9;
                if (uVar3 != 5) {
                  iVar2 = (uint)puVar5[5] - ((uint)local_42 - (uint)local_44);
                  uVar9 = 0;
                  if (-1 < iVar2) {
                    uVar9 = (undefined2)
                            ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                            (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 10));
                  }
                  puVar8[5] = uVar9;
                  if (uVar3 != 6) {
                    iVar2 = (uint)puVar5[6] - ((uint)local_3e - (uint)local_40);
                    uVar9 = 0;
                    if (-1 < iVar2) {
                      uVar9 = (undefined2)
                              ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                              (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0xc));
                    }
                    puVar8[6] = uVar9;
                    if (uVar3 != 7) {
                      iVar2 = (uint)puVar5[7] - ((uint)local_3a - (uint)local_3c);
                      uVar9 = 0;
                      if (-1 < iVar2) {
                        uVar9 = (undefined2)
                                ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0xe));
                      }
                      puVar8[7] = uVar9;
                      if (uVar3 != 8) {
                        iVar2 = (uint)puVar5[8] - ((uint)local_36 - (uint)local_38);
                        uVar9 = 0;
                        if (-1 < iVar2) {
                          uVar9 = (undefined2)
                                  ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                  (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x10));
                        }
                        puVar8[8] = uVar9;
                        if (uVar3 != 9) {
                          iVar2 = (uint)puVar5[9] - ((uint)local_32 - (uint)local_34);
                          uVar9 = 0;
                          if (-1 < iVar2) {
                            uVar9 = (undefined2)
                                    ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                    (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x12));
                          }
                          puVar8[9] = uVar9;
                          if (uVar3 != 10) {
                            iVar2 = (uint)puVar5[10] - ((uint)local_2e - (uint)local_30);
                            uVar9 = 0;
                            if (-1 < iVar2) {
                              uVar9 = (undefined2)
                                      ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                      (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x14));
                            }
                            puVar8[10] = uVar9;
                            if (uVar3 != 0xb) {
                              iVar2 = (uint)puVar5[0xb] - ((uint)local_2a - (uint)local_2c);
                              uVar9 = 0;
                              if (-1 < iVar2) {
                                uVar9 = (undefined2)
                                        ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                        (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x16));
                              }
                              puVar8[0xb] = uVar9;
                              if (uVar3 != 0xc) {
                                iVar2 = (uint)puVar5[0xc] - ((uint)local_26 - (uint)local_28);
                                uVar9 = 0;
                                if (-1 < iVar2) {
                                  uVar9 = (undefined2)
                                          ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                          (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x18));
                                }
                                puVar8[0xc] = uVar9;
                                if (uVar3 != 0xd) {
                                  iVar2 = (uint)puVar5[0xd] - ((uint)local_22 - (uint)local_24);
                                  uVar9 = 0;
                                  if (-1 < iVar2) {
                                    uVar9 = (undefined2)
                                            ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                            (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x1a))
                                    ;
                                  }
                                  puVar8[0xd] = uVar9;
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
            }
          }
        }
      }
    }
    iVar2 = 0;
  }
  return iVar2;
}
```

Callers:
- none

### `00003ac4` `FUN_00003914`

```c

int FUN_00003914(int param_1,int *param_2)

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
          if (-1 < iVar2) {
            uVar9 = (undefined2)
                    ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                    (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 2));
          }
          puVar8[1] = uVar9;
          if (uVar3 != 2) {
            iVar2 = (uint)puVar5[2] - ((uint)local_4e - (uint)local_50);
            uVar9 = 0;
            if (-1 < iVar2) {
              uVar9 = (undefined2)
                      ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                      (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 4));
            }
            puVar8[2] = uVar9;
            if (uVar3 != 3) {
              iVar2 = (uint)puVar5[3] - ((uint)local_4a - (uint)local_4c);
              uVar9 = 0;
              if (-1 < iVar2) {
                uVar9 = (undefined2)
                        ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                        (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 6));
              }
              puVar8[3] = uVar9;
              if (uVar3 != 4) {
                iVar2 = (uint)puVar5[4] - ((uint)local_46 - (uint)local_48);
                uVar9 = 0;
                if (-1 < iVar2) {
                  uVar9 = (undefined2)
                          ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                          (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 8));
                }
                puVar8[4] = uVar9;
                if (uVar3 != 5) {
                  iVar2 = (uint)puVar5[5] - ((uint)local_42 - (uint)local_44);
                  uVar9 = 0;
                  if (-1 < iVar2) {
                    uVar9 = (undefined2)
                            ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                            (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 10));
                  }
                  puVar8[5] = uVar9;
                  if (uVar3 != 6) {
                    iVar2 = (uint)puVar5[6] - ((uint)local_3e - (uint)local_40);
                    uVar9 = 0;
                    if (-1 < iVar2) {
                      uVar9 = (undefined2)
                              ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                              (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0xc));
                    }
                    puVar8[6] = uVar9;
                    if (uVar3 != 7) {
                      iVar2 = (uint)puVar5[7] - ((uint)local_3a - (uint)local_3c);
                      uVar9 = 0;
                      if (-1 < iVar2) {
                        uVar9 = (undefined2)
                                ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0xe));
                      }
                      puVar8[7] = uVar9;
                      if (uVar3 != 8) {
                        iVar2 = (uint)puVar5[8] - ((uint)local_36 - (uint)local_38);
                        uVar9 = 0;
                        if (-1 < iVar2) {
                          uVar9 = (undefined2)
                                  ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                  (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x10));
                        }
                        puVar8[8] = uVar9;
                        if (uVar3 != 9) {
                          iVar2 = (uint)puVar5[9] - ((uint)local_32 - (uint)local_34);
                          uVar9 = 0;
                          if (-1 < iVar2) {
                            uVar9 = (undefined2)
                                    ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                    (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x12));
                          }
                          puVar8[9] = uVar9;
                          if (uVar3 != 10) {
                            iVar2 = (uint)puVar5[10] - ((uint)local_2e - (uint)local_30);
                            uVar9 = 0;
                            if (-1 < iVar2) {
                              uVar9 = (undefined2)
                                      ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                      (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x14));
                            }
                            puVar8[10] = uVar9;
                            if (uVar3 != 0xb) {
                              iVar2 = (uint)puVar5[0xb] - ((uint)local_2a - (uint)local_2c);
                              uVar9 = 0;
                              if (-1 < iVar2) {
                                uVar9 = (undefined2)
                                        ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                        (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x16));
                              }
                              puVar8[0xb] = uVar9;
                              if (uVar3 != 0xc) {
                                iVar2 = (uint)puVar5[0xc] - ((uint)local_26 - (uint)local_28);
                                uVar9 = 0;
                                if (-1 < iVar2) {
                                  uVar9 = (undefined2)
                                          ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                          (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x18));
                                }
                                puVar8[0xc] = uVar9;
                                if (uVar3 != 0xd) {
                                  iVar2 = (uint)puVar5[0xd] - ((uint)local_22 - (uint)local_24);
                                  uVar9 = 0;
                                  if (-1 < iVar2) {
                                    uVar9 = (undefined2)
                                            ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                            (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x1a))
                                    ;
                                  }
                                  puVar8[0xd] = uVar9;
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
            }
          }
        }
      }
    }
    iVar2 = 0;
  }
  return iVar2;
}
```

Callers:
- none

### `00003ab8` `FUN_00003914`

```c

int FUN_00003914(int param_1,int *param_2)

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
          if (-1 < iVar2) {
            uVar9 = (undefined2)
                    ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                    (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 2));
          }
          puVar8[1] = uVar9;
          if (uVar3 != 2) {
            iVar2 = (uint)puVar5[2] - ((uint)local_4e - (uint)local_50);
            uVar9 = 0;
            if (-1 < iVar2) {
              uVar9 = (undefined2)
                      ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                      (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 4));
            }
            puVar8[2] = uVar9;
            if (uVar3 != 3) {
              iVar2 = (uint)puVar5[3] - ((uint)local_4a - (uint)local_4c);
              uVar9 = 0;
              if (-1 < iVar2) {
                uVar9 = (undefined2)
                        ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                        (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 6));
              }
              puVar8[3] = uVar9;
              if (uVar3 != 4) {
                iVar2 = (uint)puVar5[4] - ((uint)local_46 - (uint)local_48);
                uVar9 = 0;
                if (-1 < iVar2) {
                  uVar9 = (undefined2)
                          ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                          (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 8));
                }
                puVar8[4] = uVar9;
                if (uVar3 != 5) {
                  iVar2 = (uint)puVar5[5] - ((uint)local_42 - (uint)local_44);
                  uVar9 = 0;
                  if (-1 < iVar2) {
                    uVar9 = (undefined2)
                            ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                            (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 10));
                  }
                  puVar8[5] = uVar9;
                  if (uVar3 != 6) {
                    iVar2 = (uint)puVar5[6] - ((uint)local_3e - (uint)local_40);
                    uVar9 = 0;
                    if (-1 < iVar2) {
                      uVar9 = (undefined2)
                              ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                              (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0xc));
                    }
                    puVar8[6] = uVar9;
                    if (uVar3 != 7) {
                      iVar2 = (uint)puVar5[7] - ((uint)local_3a - (uint)local_3c);
                      uVar9 = 0;
                      if (-1 < iVar2) {
                        uVar9 = (undefined2)
                                ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0xe));
                      }
                      puVar8[7] = uVar9;
                      if (uVar3 != 8) {
                        iVar2 = (uint)puVar5[8] - ((uint)local_36 - (uint)local_38);
                        uVar9 = 0;
                        if (-1 < iVar2) {
                          uVar9 = (undefined2)
                                  ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                  (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x10));
                        }
                        puVar8[8] = uVar9;
                        if (uVar3 != 9) {
                          iVar2 = (uint)puVar5[9] - ((uint)local_32 - (uint)local_34);
                          uVar9 = 0;
                          if (-1 < iVar2) {
                            uVar9 = (undefined2)
                                    ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                    (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x12));
                          }
                          puVar8[9] = uVar9;
                          if (uVar3 != 10) {
                            iVar2 = (uint)puVar5[10] - ((uint)local_2e - (uint)local_30);
                            uVar9 = 0;
                            if (-1 < iVar2) {
                              uVar9 = (undefined2)
                                      ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                      (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x14));
                            }
                            puVar8[10] = uVar9;
                            if (uVar3 != 0xb) {
                              iVar2 = (uint)puVar5[0xb] - ((uint)local_2a - (uint)local_2c);
                              uVar9 = 0;
                              if (-1 < iVar2) {
                                uVar9 = (undefined2)
                                        ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                        (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x16));
                              }
                              puVar8[0xb] = uVar9;
                              if (uVar3 != 0xc) {
                                iVar2 = (uint)puVar5[0xc] - ((uint)local_26 - (uint)local_28);
                                uVar9 = 0;
                                if (-1 < iVar2) {
                                  uVar9 = (undefined2)
                                          ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                          (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x18));
                                }
                                puVar8[0xc] = uVar9;
                                if (uVar3 != 0xd) {
                                  iVar2 = (uint)puVar5[0xd] - ((uint)local_22 - (uint)local_24);
                                  uVar9 = 0;
                                  if (-1 < iVar2) {
                                    uVar9 = (undefined2)
                                            ((int)((uint)*(ushort *)((int)param_2 + 6) * iVar2) /
                                            (int)(uint)*(ushort *)(*(int *)(param_1 + 0x10) + 0x1a))
                                    ;
                                  }
                                  puVar8[0xd] = uVar9;
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
            }
          }
        }
      }
    }
    iVar2 = 0;
  }
  return iVar2;
}
```

Callers:
- none

### `00005df4` `FUN_00005cb4`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_00005cb4(int param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)

{
  undefined1 uVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  int local_34;
  int local_30;
  int local_2c;
  
  *(undefined4 *)(param_1 + 0x30) = param_4;
  *(undefined4 *)(param_1 + 0x2c) = param_3;
  uVar1 = **(undefined1 **)(param_1 + 4);
  *(undefined4 *)(param_1 + 0x28) = param_2;
  *(undefined1 *)(param_1 + 0x34) = uVar1;
  _DAT_407effb0 = (short)DAT_00006010;
  FUN_00005138(6,*(undefined4 *)(param_1 + 8));
  _DAT_407ec180 = 0xa5;
  DAT_407ec100 = 0x10;
  FUN_00005138(3,*(undefined4 *)(param_1 + 8));
  if (**(char **)(param_1 + 4) == '\0') {
    iVar2 = *(int *)(param_1 + 0x2c) + -0x42100000;
    _DAT_407ec110 = (undefined2)((uint)iVar2 >> 0x10);
    _DAT_407ec108 = (undefined2)iVar2;
    _DAT_407ec130 = (uint)**(byte **)(param_1 + 0x28);
  }
  else {
    FUN_00008598((int)(*(char **)(param_1 + 4))[0x11]);
    iVar2 = *(int *)(param_1 + 0x2c) + -0x42100000;
    _DAT_407ec110 = (undefined2)((uint)iVar2 >> 0x10);
    _DAT_407ec108 = (undefined2)iVar2;
    _DAT_407ec130 = (uint)**(byte **)(param_1 + 0x28);
    if (**(char **)(param_1 + 4) != '\0') {
      DAT_407ec104 = 0;
      DAT_407ec114 = 0x81;
      return 0;
    }
  }
  DAT_407ec104 = 0;
  do {
    DAT_407ec114 = 0x81;
    iVar2 = *(int *)(param_1 + 0x14);
    while (-1 < _DAT_407ec12c << 0x19) {
      if (iVar2 == 0) goto LAB_00005d8a;
      iVar2 = iVar2 + -1;
    }
    DAT_407ec114 = 0;
    iVar2 = *(int *)(param_1 + 0x14);
    while (_DAT_407ec12c << 0x19 < 0) {
      if (iVar2 == 0) {
LAB_00005d8a:
        *(undefined1 *)(param_1 + 0x34) = 0;
        if (_DAT_407effb0 == 0) {
          _DAT_407effb0 = (short)DAT_00006070;
          FUN_00005138(6,*(undefined4 *)(param_1 + 8));
          _DAT_407ec180 = 0xa5;
          DAT_407ec100 = 0x10;
          FUN_00005138(3,*(undefined4 *)(param_1 + 8));
          if (**(char **)(param_1 + 4) != '\0') {
            FUN_00008598((int)(*(char **)(param_1 + 4))[0x11]);
          }
        }
        _DAT_407ec124 = 0;
        local_34 = 0x4b00;
        _DAT_407ec180 = 0xa5;
        DAT_407ec100 = 8;
        FUN_00005138(0x10,*(undefined4 *)(param_1 + 8));
        for (; ((short)DAT_00006014 != 0 && (local_34 != 0)); local_34 = local_34 + -1) {
        }
        _DAT_407effb0 = (short)DAT_00006014;
        return 0x14;
      }
      iVar2 = iVar2 + -1;
    }
    if ((_DAT_407ec1f0 & 0x12) != 0) {
      *(undefined1 *)(param_1 + 0x34) = 0;
      if (_DAT_407effb0 == 0) {
        _DAT_407effb0 = (short)DAT_00006010;
        FUN_00005138(6,*(undefined4 *)(param_1 + 8));
        _DAT_407ec180 = 0xa5;
        DAT_407ec100 = 0x10;
        FUN_00005138(3,*(undefined4 *)(param_1 + 8));
        if (**(char **)(param_1 + 4) != '\0') {
          FUN_00008598((int)(*(char **)(param_1 + 4))[0x11]);
        }
      }
      _DAT_407ec124 = 0;
      local_30 = 0x4b00;
      _DAT_407ec180 = 0xa5;
      DAT_407ec100 = 8;
      FUN_00005138(0x10,*(undefined4 *)(param_1 + 8));
      for (; ((short)DAT_00006014 != 0 && (local_30 != 0)); local_30 = local_30 + -1) {
      }
      _DAT_407effb0 = (short)DAT_00006014;
      return 0x18;
    }
    iVar3 = *(int *)(param_1 + 0x28);
    *(int *)(param_1 + 0x28) = iVar3 + 1;
    iVar2 = *(int *)(param_1 + 0x2c);
    *(int *)(param_1 + 0x2c) = iVar2 + 1;
    iVar4 = *(int *)(param_1 + 0x30) + -1;
    *(int *)(param_1 + 0x30) = iVar4;
    if (iVar4 == 0) {
      local_2c = 0x4b00;
      _DAT_407ec180 = 0xa5;
      DAT_407ec100 = 8;
      FUN_00005138(0x10,*(undefined4 *)(param_1 + 8));
      for (; ((short)DAT_00006014 != 0 && (local_2c != 0)); local_2c = local_2c + -1) {
      }
      _DAT_407effb0 = (short)DAT_00006014;
      return 0;
    }
    iVar2 = iVar2 + -0x420fffff;
    _DAT_407ec110 = (undefined2)((uint)iVar2 >> 0x10);
    _DAT_407ec108 = (undefined2)iVar2;
    _DAT_407ec130 = (uint)*(byte *)(iVar3 + 1);
  } while( true );
}
```

Callers:
- none

### `00005f2c` `FUN_00005cb4`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_00005cb4(int param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)

{
  undefined1 uVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  int local_34;
  int local_30;
  int local_2c;
  
  *(undefined4 *)(param_1 + 0x30) = param_4;
  *(undefined4 *)(param_1 + 0x2c) = param_3;
  uVar1 = **(undefined1 **)(param_1 + 4);
  *(undefined4 *)(param_1 + 0x28) = param_2;
  *(undefined1 *)(param_1 + 0x34) = uVar1;
  _DAT_407effb0 = (short)DAT_00006010;
  FUN_00005138(6,*(undefined4 *)(param_1 + 8));
  _DAT_407ec180 = 0xa5;
  DAT_407ec100 = 0x10;
  FUN_00005138(3,*(undefined4 *)(param_1 + 8));
  if (**(char **)(param_1 + 4) == '\0') {
    iVar2 = *(int *)(param_1 + 0x2c) + -0x42100000;
    _DAT_407ec110 = (undefined2)((uint)iVar2 >> 0x10);
    _DAT_407ec108 = (undefined2)iVar2;
    _DAT_407ec130 = (uint)**(byte **)(param_1 + 0x28);
  }
  else {
    FUN_00008598((int)(*(char **)(param_1 + 4))[0x11]);
    iVar2 = *(int *)(param_1 + 0x2c) + -0x42100000;
    _DAT_407ec110 = (undefined2)((uint)iVar2 >> 0x10);
    _DAT_407ec108 = (undefined2)iVar2;
    _DAT_407ec130 = (uint)**(byte **)(param_1 + 0x28);
    if (**(char **)(param_1 + 4) != '\0') {
      DAT_407ec104 = 0;
      DAT_407ec114 = 0x81;
      return 0;
    }
  }
  DAT_407ec104 = 0;
  do {
    DAT_407ec114 = 0x81;
    iVar2 = *(int *)(param_1 + 0x14);
    while (-1 < _DAT_407ec12c << 0x19) {
      if (iVar2 == 0) goto LAB_00005d8a;
      iVar2 = iVar2 + -1;
    }
    DAT_407ec114 = 0;
    iVar2 = *(int *)(param_1 + 0x14);
    while (_DAT_407ec12c << 0x19 < 0) {
      if (iVar2 == 0) {
LAB_00005d8a:
        *(undefined1 *)(param_1 + 0x34) = 0;
        if (_DAT_407effb0 == 0) {
          _DAT_407effb0 = (short)DAT_00006070;
          FUN_00005138(6,*(undefined4 *)(param_1 + 8));
          _DAT_407ec180 = 0xa5;
          DAT_407ec100 = 0x10;
          FUN_00005138(3,*(undefined4 *)(param_1 + 8));
          if (**(char **)(param_1 + 4) != '\0') {
            FUN_00008598((int)(*(char **)(param_1 + 4))[0x11]);
          }
        }
        _DAT_407ec124 = 0;
        local_34 = 0x4b00;
        _DAT_407ec180 = 0xa5;
        DAT_407ec100 = 8;
        FUN_00005138(0x10,*(undefined4 *)(param_1 + 8));
        for (; ((short)DAT_00006014 != 0 && (local_34 != 0)); local_34 = local_34 + -1) {
        }
        _DAT_407effb0 = (short)DAT_00006014;
        return 0x14;
      }
      iVar2 = iVar2 + -1;
    }
    if ((_DAT_407ec1f0 & 0x12) != 0) {
      *(undefined1 *)(param_1 + 0x34) = 0;
      if (_DAT_407effb0 == 0) {
        _DAT_407effb0 = (short)DAT_00006010;
        FUN_00005138(6,*(undefined4 *)(param_1 + 8));
        _DAT_407ec180 = 0xa5;
        DAT_407ec100 = 0x10;
        FUN_00005138(3,*(undefined4 *)(param_1 + 8));
        if (**(char **)(param_1 + 4) != '\0') {
          FUN_00008598((int)(*(char **)(param_1 + 4))[0x11]);
        }
      }
      _DAT_407ec124 = 0;
      local_30 = 0x4b00;
      _DAT_407ec180 = 0xa5;
      DAT_407ec100 = 8;
      FUN_00005138(0x10,*(undefined4 *)(param_1 + 8));
      for (; ((short)DAT_00006014 != 0 && (local_30 != 0)); local_30 = local_30 + -1) {
      }
      _DAT_407effb0 = (short)DAT_00006014;
      return 0x18;
    }
    iVar3 = *(int *)(param_1 + 0x28);
    *(int *)(param_1 + 0x28) = iVar3 + 1;
    iVar2 = *(int *)(param_1 + 0x2c);
    *(int *)(param_1 + 0x2c) = iVar2 + 1;
    iVar4 = *(int *)(param_1 + 0x30) + -1;
    *(int *)(param_1 + 0x30) = iVar4;
    if (iVar4 == 0) {
      local_2c = 0x4b00;
      _DAT_407ec180 = 0xa5;
      DAT_407ec100 = 8;
      FUN_00005138(0x10,*(undefined4 *)(param_1 + 8));
      for (; ((short)DAT_00006014 != 0 && (local_2c != 0)); local_2c = local_2c + -1) {
      }
      _DAT_407effb0 = (short)DAT_00006014;
      return 0;
    }
    iVar2 = iVar2 + -0x420fffff;
    _DAT_407ec110 = (undefined2)((uint)iVar2 >> 0x10);
    _DAT_407ec108 = (undefined2)iVar2;
    _DAT_407ec130 = (uint)*(byte *)(iVar3 + 1);
  } while( true );
}
```

Callers:
- none

### `00005f14` `FUN_00005cb4`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_00005cb4(int param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)

{
  undefined1 uVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  int local_34;
  int local_30;
  int local_2c;
  
  *(undefined4 *)(param_1 + 0x30) = param_4;
  *(undefined4 *)(param_1 + 0x2c) = param_3;
  uVar1 = **(undefined1 **)(param_1 + 4);
  *(undefined4 *)(param_1 + 0x28) = param_2;
  *(undefined1 *)(param_1 + 0x34) = uVar1;
  _DAT_407effb0 = (short)DAT_00006010;
  FUN_00005138(6,*(undefined4 *)(param_1 + 8));
  _DAT_407ec180 = 0xa5;
  DAT_407ec100 = 0x10;
  FUN_00005138(3,*(undefined4 *)(param_1 + 8));
  if (**(char **)(param_1 + 4) == '\0') {
    iVar2 = *(int *)(param_1 + 0x2c) + -0x42100000;
    _DAT_407ec110 = (undefined2)((uint)iVar2 >> 0x10);
    _DAT_407ec108 = (undefined2)iVar2;
    _DAT_407ec130 = (uint)**(byte **)(param_1 + 0x28);
  }
  else {
    FUN_00008598((int)(*(char **)(param_1 + 4))[0x11]);
    iVar2 = *(int *)(param_1 + 0x2c) + -0x42100000;
    _DAT_407ec110 = (undefined2)((uint)iVar2 >> 0x10);
    _DAT_407ec108 = (undefined2)iVar2;
    _DAT_407ec130 = (uint)**(byte **)(param_1 + 0x28);
    if (**(char **)(param_1 + 4) != '\0') {
      DAT_407ec104 = 0;
      DAT_407ec114 = 0x81;
      return 0;
    }
  }
  DAT_407ec104 = 0;
  do {
    DAT_407ec114 = 0x81;
    iVar2 = *(int *)(param_1 + 0x14);
    while (-1 < _DAT_407ec12c << 0x19) {
      if (iVar2 == 0) goto LAB_00005d8a;
      iVar2 = iVar2 + -1;
    }
    DAT_407ec114 = 0;
    iVar2 = *(int *)(param_1 + 0x14);
    while (_DAT_407ec12c << 0x19 < 0) {
      if (iVar2 == 0) {
LAB_00005d8a:
        *(undefined1 *)(param_1 + 0x34) = 0;
        if (_DAT_407effb0 == 0) {
          _DAT_407effb0 = (short)DAT_00006070;
          FUN_00005138(6,*(undefined4 *)(param_1 + 8));
          _DAT_407ec180 = 0xa5;
          DAT_407ec100 = 0x10;
          FUN_00005138(3,*(undefined4 *)(param_1 + 8));
          if (**(char **)(param_1 + 4) != '\0') {
            FUN_00008598((int)(*(char **)(param_1 + 4))[0x11]);
          }
        }
        _DAT_407ec124 = 0;
        local_34 = 0x4b00;
        _DAT_407ec180 = 0xa5;
        DAT_407ec100 = 8;
        FUN_00005138(0x10,*(undefined4 *)(param_1 + 8));
        for (; ((short)DAT_00006014 != 0 && (local_34 != 0)); local_34 = local_34 + -1) {
        }
        _DAT_407effb0 = (short)DAT_00006014;
        return 0x14;
      }
      iVar2 = iVar2 + -1;
    }
    if ((_DAT_407ec1f0 & 0x12) != 0) {
      *(undefined1 *)(param_1 + 0x34) = 0;
      if (_DAT_407effb0 == 0) {
        _DAT_407effb0 = (short)DAT_00006010;
        FUN_00005138(6,*(undefined4 *)(param_1 + 8));
        _DAT_407ec180 = 0xa5;
        DAT_407ec100 = 0x10;
        FUN_00005138(3,*(undefined4 *)(param_1 + 8));
        if (**(char **)(param_1 + 4) != '\0') {
          FUN_00008598((int)(*(char **)(param_1 + 4))[0x11]);
        }
      }
      _DAT_407ec124 = 0;
      local_30 = 0x4b00;
      _DAT_407ec180 = 0xa5;
      DAT_407ec100 = 8;
      FUN_00005138(0x10,*(undefined4 *)(param_1 + 8));
      for (; ((short)DAT_00006014 != 0 && (local_30 != 0)); local_30 = local_30 + -1) {
      }
      _DAT_407effb0 = (short)DAT_00006014;
      return 0x18;
    }
    iVar3 = *(int *)(param_1 + 0x28);
    *(int *)(param_1 + 0x28) = iVar3 + 1;
    iVar2 = *(int *)(param_1 + 0x2c);
    *(int *)(param_1 + 0x2c) = iVar2 + 1;
    iVar4 = *(int *)(param_1 + 0x30) + -1;
    *(int *)(param_1 + 0x30) = iVar4;
    if (iVar4 == 0) {
      local_2c = 0x4b00;
      _DAT_407ec180 = 0xa5;
      DAT_407ec100 = 8;
      FUN_00005138(0x10,*(undefined4 *)(param_1 + 8));
      for (; ((short)DAT_00006014 != 0 && (local_2c != 0)); local_2c = local_2c + -1) {
      }
      _DAT_407effb0 = (short)DAT_00006014;
      return 0;
    }
    iVar2 = iVar2 + -0x420fffff;
    _DAT_407ec110 = (undefined2)((uint)iVar2 >> 0x10);
    _DAT_407ec108 = (undefined2)iVar2;
    _DAT_407ec130 = (uint)*(byte *)(iVar3 + 1);
  } while( true );
}
```

Callers:
- none

### `00005854` `FUN_00005808`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_00005808(int param_1,int param_2,int param_3,undefined1 *param_4)

{
  int iVar1;
  uint uVar2;
  undefined4 uVar3;
  int local_28;
  int local_24;
  
  *(byte *)(param_1 + 0x34) = (-(**(char **)(param_1 + 4) == '\0') & 0xfdU) + 3;
  _DAT_407effb0 = (short)DAT_00005af8;
  FUN_00005138(6,*(undefined4 *)(param_1 + 8));
  _DAT_407ec180 = 0xa5;
  DAT_407ec100 = 0x10;
  FUN_00005138(3,*(undefined4 *)(param_1 + 8));
  if (**(char **)(param_1 + 4) == '\0') {
    param_2 = param_2 + -0x42100000;
    _DAT_407ec110 = (undefined2)((uint)param_2 >> 0x10);
    uVar2 = param_3 + -1 + param_2;
    _DAT_407ec108 = (undefined2)param_2;
    _DAT_407ec120 = uVar2 >> 0x10;
    _DAT_407ec118 = (undefined2)uVar2;
  }
  else {
    FUN_00008598((int)(*(char **)(param_1 + 4))[0x11]);
    param_2 = param_2 + -0x42100000;
    DAT_407ec104 = 0;
    _DAT_407ec110 = (undefined2)((uint)param_2 >> 0x10);
    uVar2 = param_3 + -1 + param_2;
    _DAT_407ec108 = (undefined2)param_2;
    _DAT_407ec120 = uVar2 >> 0x10;
    _DAT_407ec118 = (undefined2)uVar2;
    DAT_407ec114 = 0x83;
    if (**(char **)(param_1 + 4) != '\0') {
      *param_4 = 2;
      return 0;
    }
  }
  DAT_407ec104 = 0;
  DAT_407ec114 = 0x83;
  param_3 = param_3 * *(int *)(param_1 + 0x18);
  iVar1 = param_3;
  while (-1 < _DAT_407ec12c << 0x19) {
    if (iVar1 == 0) goto LAB_000058ec;
    iVar1 = iVar1 + -1;
  }
  DAT_407ec114 = 0;
  while (_DAT_407ec12c << 0x19 < 0) {
    if (param_3 == 0) goto LAB_000058ec;
    param_3 = param_3 + -1;
  }
  if (-1 < _DAT_407ec1f0 << 0x1b) {
    *param_4 = (char)((_DAT_407ec128 & 0xf) >> 3);
    local_28 = 0x4b00;
    _DAT_407ec180 = 0xa5;
    DAT_407ec100 = 8;
    FUN_00005138(0x10,*(undefined4 *)(param_1 + 8));
    for (; ((short)DAT_00005afc != 0 && (local_28 != 0)); local_28 = local_28 + -1) {
    }
    _DAT_407effb0 = (short)DAT_00005afc;
    return 0;
  }
  FUN_00005244(param_1);
  uVar3 = 0x1f8;
LAB_000058f4:
  *(undefined1 *)(param_1 + 0x34) = 0;
  if (_DAT_407effb0 == 0) {
    _DAT_407effb0 = (short)DAT_00005af8;
    FUN_00005138(6,*(undefined4 *)(param_1 + 8));
    _DAT_407ec180 = 0xa5;
    DAT_407ec100 = 0x10;
    FUN_00005138(3,*(undefined4 *)(param_1 + 8));
    if (**(char **)(param_1 + 4) != '\0') {
      FUN_00008598((int)(*(char **)(param_1 + 4))[0x11]);
    }
  }
  _DAT_407ec124 = 0;
  local_24 = 0x4b00;
  _DAT_407ec180 = 0xa5;
  DAT_407ec100 = 8;
  FUN_00005138(0x10,*(undefined4 *)(param_1 + 8));
  for (; ((short)DAT_00005afc != 0 && (local_24 != 0)); local_24 = local_24 + -1) {
  }
  _DAT_407effb0 = (short)DAT_00005afc;
  return uVar3;
LAB_000058ec:
  FUN_00005244(param_1);
  uVar3 = 0x14;
  goto LAB_000058f4;
}
```

Callers:
- none

### `0000657c` `FUN_000064dc`

```c

void FUN_000064dc(int param_1)

{
  byte bVar1;
  ushort uVar2;
  ushort uVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  undefined1 *puVar7;
  int iVar8;
  uint uVar9;
  byte *pbVar10;
  int iVar11;
  uint *local_30;
  
  uVar6 = 0;
  uVar5 = 0;
  if (*(short *)(param_1 + 8) != 0) {
    do {
      puVar7 = (undefined1 *)(*(int *)(param_1 + 0x10) + uVar6);
      if (*(char *)(*(int *)(param_1 + 0x10) + uVar6) == '\0') {
        pbVar10 = (byte *)(*(int *)(param_1 + 0x14) + uVar6);
        bVar1 = *(byte *)(*(int *)(param_1 + 0x14) + uVar6);
        if ((bVar1 & 1) != 0) goto LAB_000064fa;
        if (*(char *)(param_1 + 6) == '\x01') {
          uVar2 = *(ushort *)(param_1 + 0x88);
          uVar3 = *(ushort *)(*(int *)(param_1 + 0x2c) + uVar6 * 2);
        }
        else {
          uVar3 = *(ushort *)(*(int *)(param_1 + 0x38) + uVar6 * 2);
          uVar2 = *(ushort *)(param_1 + 0x8a);
        }
        iVar8 = uVar6 * 4;
        local_30 = (uint *)(*(int *)(param_1 + 0x24) + iVar8);
        uVar9 = *local_30 >> 10;
        iVar11 = (uVar9 & 0xff) + 1;
        iVar11 = (int)((uint)uVar3 - (iVar11 * (uint)(uVar2 >> 1) >> 3 & 0xffff)) /
                 (iVar11 * 0xf >> *(sbyte *)(param_1 + 0x68));
        uVar4 = iVar11 + (*local_30 & 0x3ff);
        if ((int)uVar4 < 0) {
          *pbVar10 = bVar1 + 1;
          local_30 = (uint *)(*(int *)(param_1 + 0x24) + iVar8);
          uVar4 = 0;
          pbVar10 = (byte *)(*(int *)(param_1 + 0x14) + uVar6);
          uVar9 = *local_30 >> 10;
        }
        else if ((int)uVar4 < 0x400) {
          if (iVar11 == 0) {
            *pbVar10 = bVar1 + 1;
            local_30 = (uint *)(*(int *)(param_1 + 0x24) + iVar8);
            pbVar10 = (byte *)(*(int *)(param_1 + 0x14) + uVar6);
            uVar9 = *local_30 >> 10;
          }
        }
        else {
          *pbVar10 = bVar1 + 1;
          local_30 = (uint *)(*(int *)(param_1 + 0x24) + iVar8);
          pbVar10 = (byte *)(*(int *)(param_1 + 0x14) + uVar6);
          uVar4 = 0x3ff;
          uVar9 = *local_30 >> 10;
        }
        *local_30 = uVar9 << 10 | uVar4;
        if ((*pbVar10 & 1) != 0) {
          puVar7 = (undefined1 *)(*(int *)(param_1 + 0x10) + uVar6);
          goto LAB_000064fa;
        }
      }
      else {
LAB_000064fa:
        uVar5 = uVar5 + 1;
        *puVar7 = 1;
      }
      uVar6 = uVar6 + 1;
    } while ((uVar6 & 0xffff) < (uint)*(ushort *)(param_1 + 8));
    if (*(ushort *)(param_1 + 8) != uVar5) {
      return;
    }
  }
  *(undefined1 *)(param_1 + 7) = 1;
  return;
}
```

Callers:
- none

### `000097e4` `PROBE_000097e4`

```c

/* WARNING: Control flow encountered bad instruction data */

void PROBE_000097e4(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}
```

Callers:
- `FUN_00002a14` @ `00002a14` from `00002a52` type=PARAM

### `00009818` `PROBE_00009818`

```c

/* WARNING: Control flow encountered bad instruction data */

void PROBE_00009818(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}
```

Callers:
- `FUN_00000e5c` @ `00000e5c` from `00000e98` type=PARAM

### `00009874` `PROBE_00009874`

```c

/* WARNING: Control flow encountered bad instruction data */

void PROBE_00009874(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}
```

Callers:
- `FUN_00002a14` @ `00002a14` from `00002a3c` type=PARAM

### `000098c4` `<none>`

```asm
0000987e: lsls r2,r0,#0x1c
00009880: movs r0,r0
00009882: movs r0,r0
00009884: ldr r0,[sp,#0x2a0]
00009886: movs r0,r0
00009888: cmp r2,#0xc5
0000988a: movs r0,r0
0000988c: movs r0,r0
0000988e: movs r0,r0
00009890: ldr r0,[sp,#0x250]
00009892: movs r0,r0
00009894: lsls r0,r0,#0x4
00009896: movs r0,r0
00009898: lsrs r4,r3
0000989a: movs r0,#0x0
0000989c: movs r7,r1
000200ea: ldr r1,[0x00020168]
000200ec: str r0,[r1,#0x0]
000200ee: ldmia r0!,{r1,r2}
000200f0: msr msp,r1
000200f4: bx r2
000200fe: ldr r0,[0x00020164]
00020100: b 0x000200ea
00020264: ldr r3,[0x000202a0]
00020266: push {r4,r5,r6,lr}
00020268: movs r5,r0
0002026a: ldrh r0,[r3,#0x0]
0002026c: movs r4,r1
0002026e: movs r6,r2
00020270: cmp r0,#0x0
00020272: beq 0x0002029a
00020274: ldr r3,[0x000202a4]
00020276: mov r12,r3
```

### `000098c8` `PROBE_000098c8`

```c

/* WARNING: Control flow encountered bad instruction data */

void PROBE_000098c8(void)

{
  software_interrupt(0xff);
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}
```

Callers:
- `FUN_000009c0` @ `000009c0` from `000009ca` type=PARAM

### `000020a4` `FUN_00002090`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00002090(void)

{
  if (DAT_20005a58 != '\0') {
    FUN_00009568(0x2000462c,0,0x1400);
    FUN_00009568(&DAT_20005a2c,0,0x28);
    _DAT_20005a54 = 0;
    DAT_20005a57 = 0;
  }
  return;
}
```

Callers:
- none

### `00002098` `FUN_00002090`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00002090(void)

{
  if (DAT_20005a58 != '\0') {
    FUN_00009568(0x2000462c,0,0x1400);
    FUN_00009568(&DAT_20005a2c,0,0x28);
    _DAT_20005a54 = 0;
    DAT_20005a57 = 0;
  }
  return;
}
```

Callers:
- none

### `00003f88` `FUN_00003e3a`

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
              ;
              uVar10 = (uVar23 & 0xffff) - (uint)*(ushort *)((int)&stack0x00000038 + iVar6) & 0xffff
              ;
            }
            uVar8 = (ushort)uVar13;
            if (uVar13 == 0) {
              uVar8 = 1;
            }
            uVar10 = 0x18f9c / ((uVar10 * 100) / (uint)uVar8 + 100 & 0xffff) + uVar21 * 0x3ff &
                     0xffff;
            in_stack_00000030._2_2_ = 1;
            if (uVar10 != 0) {
              uVar23 = uVar17 * 0x3ff & 0xffff;
              if (uVar10 < uVar23) {
                if (uVar10 < 0x400) {
                  if ((0x1fe < uVar10) && (uVar10 = uVar10 + DAT_000047e8 & 0xffff, uVar10 != 0)) {
                    in_stack_00000030._2_2_ = (undefined2)((uVar10 << 1) / uVar7);
                  }
                }
                else {
LAB_00004392:
                  in_stack_00000030._2_2_ = (undefined2)(uVar10 / uVar7);
                }
              }
              else {
                uVar10 = uVar10 * 2 - uVar23 & 0xffff;
                in_stack_00000030._2_2_ = 0x3ff;
                if (uVar10 <= uVar7 * 0x3ff) goto LAB_00004392;
              }
            }
          }
          else {
            in_stack_00000030._2_2_ = 0xffff;
          }
          *(undefined2 *)(*(int *)(unaff_r4 + 0x38) + iVar20) = in_stack_00000030._2_2_;
          uVar15 = in_stack_00000030._2_2_;
          if (iVar19 != 0) goto LAB_000040bc;
        }
        FUN_00002918(uStack00000000,(int)&stack0x00000030 + 2);
        *(undefined2 *)(*(int *)(unaff_r4 + 0x38) + uVar14 * 2) = in_stack_00000030._2_2_;
        uVar15 = in_stack_00000030._2_2_;
      }
LAB_000040bc:
      *in_stack_0000000c = uVar15;
      in_stack_0000000c = in_stack_0000000c + 1;
      param_1 = *(int *)(unaff_r4 + 0x78);
      uStack00000004 = uStack00000004 + 1;
      uStack00000000 = uStack00000004 & 0xff;
    } while (uStack00000000 < *(byte *)(param_1 + 0x11));
  }
  cVar2 = *(char *)(param_1 + 0x1a);
  if (cVar2 == '\0') {
    uVar14 = 4;
    uVar21 = 3;
    uVar23 = 2;
    uVar7 = 1;
    uVar10 = 0;
  }
  else {
    uVar10 = (uint)_DAT_20005d98;
/* ... truncated ... */
```

Callers:
- none

### `000026f4` `FUN_00002544`

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
    iVar8 = (int)sVar2;
    if (iVar10 < iVar12) {
      sVar3 = (short)iVar12;
    }
    uVar4 = uVar4 + 1 & 0xff;
    iVar12 = (int)sVar3;
    iVar9 = iVar9 + iVar10;
    param_2 = param_2 + 1;
  } while (param_3 != uVar4);
  iVar12 = param_1 * 0x4a;
  *(short *)(iVar12 + 0x20005af2) = sVar2;
  *(short *)(iVar12 + 0x20005af0) = sVar3;
  *(short *)(iVar12 + 0x20005af4) = (short)(iVar9 / (int)param_3);
  return 0;
}
```

Callers:
- `FUN_00002544` @ `00002544` from `00002566` type=UNCONDITIONAL_JUMP

### `0000240c` `FUN_00002370`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_00002370(void)

{
  int iVar1;
  
  iVar1 = FUN_00000e50();
  FUN_00009568(&DAT_20005b40,0,0x18);
  FUN_00009568(0x20005aac,0,0x94);
  _DAT_20005a9c = 0;
  if (iVar1 == 1) {
    _DAT_20005b40 = DAT_00009678;
    DAT_20005b44 = DAT_0000967c;
    DAT_20005b4a = 5;
    DAT_20005b50 = DAT_0000967c;
    _DAT_20005b4c = DAT_00009678;
    _DAT_20005aa0 = DAT_00009694;
    _DAT_20005aa4 = DAT_00009698;
    _DAT_20005aa8 = DAT_0000969c;
  }
  else {
    _DAT_20005b40 = DAT_000096a0;
    DAT_20005b44 = DAT_000096a4;
    DAT_20005b4a = 5;
    FUN_00009578(&DAT_20005b4c,&DAT_000096a5,5);
    _DAT_20005aa0 = DAT_00009688;
    _DAT_20005aa4 = DAT_0000968c;
    _DAT_20005aa8 = DAT_00009690;
  }
  DAT_20005b56 = 5;
  DAT_20005a9e = 1;
  return 0;
}
```

Callers:
- none

### `000027d4` `FUN_00002544`

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
    iVar8 = (int)sVar2;
    if (iVar10 < iVar12) {
      sVar3 = (short)iVar12;
    }
    uVar4 = uVar4 + 1 & 0xff;
    iVar12 = (int)sVar3;
    iVar9 = iVar9 + iVar10;
    param_2 = param_2 + 1;
  } while (param_3 != uVar4);
  iVar12 = param_1 * 0x4a;
  *(short *)(iVar12 + 0x20005af2) = sVar2;
  *(short *)(iVar12 + 0x20005af0) = sVar3;
  *(short *)(iVar12 + 0x20005af4) = (short)(iVar9 / (int)param_3);
  return 0;
}
```

Callers:
- none

### `000019c0` `FUN_0000190c`

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

Callers:
- none

### `000019e8` `FUN_0000190c`

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

Callers:
- none

### `00001b30` `FUN_00001b08`

```c

undefined4 FUN_00001b08(void)

{
  int iVar1;
  
  FUN_00009568(0x2000462c,0,0x1430);
  iVar1 = FUN_00000e50();
  DAT_20005a56 = (-('\x01' - (iVar1 == 0)) & 0xfbU) + 10;
  DAT_20005a58 = 1;
  return 0;
}
```

Callers:
- none

### `00001bf0` `FUN_00001b44`

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
  if (1 < bVar3) {
    if ((short)((uint)_DAT_20005a30 >> 8) < -0x1e) {
      FUN_00001ac8(1);
      FUN_00009568(0x2000482c,0,0x200);
      _DAT_20005a30 = 0;
      bVar3 = DAT_20005a56;
    }
    if (2 < bVar3) {
      if ((short)((uint)_DAT_20005a34 >> 8) < -0x1e) {
        FUN_00001ac8(2);
        FUN_00009568(0x20004a2c,0,0x200);
        _DAT_20005a34 = 0;
        bVar3 = DAT_20005a56;
      }
      if (3 < bVar3) {
        if ((short)((uint)_DAT_20005a38 >> 8) < -0x1e) {
          FUN_00001ac8(3);
          FUN_00009568(0x20004c2c,0,0x200);
          _DAT_20005a38 = 0;
          bVar3 = DAT_20005a56;
        }
        if (4 < bVar3) {
          if ((short)((uint)_DAT_20005a3c >> 8) < -0x1e) {
            FUN_00001ac8(4);
            FUN_00009568(0x20004e2c,0,0x200);
            _DAT_20005a3c = 0;
            bVar3 = DAT_20005a56;
          }
          if (5 < bVar3) {
            if ((short)((uint)_DAT_20005a40 >> 8) < -0x1e) {
              FUN_00001ac8(5);
              FUN_00009568(0x2000502c,0,0x200);
              _DAT_20005a40 = 0;
              bVar3 = DAT_20005a56;
            }
            if (6 < bVar3) {
              if ((short)((uint)_DAT_20005a44 >> 8) < -0x1e) {
                FUN_00001ac8(6);
                FUN_00009568(0x2000522c,0,0x200);
                _DAT_20005a44 = 0;
                bVar3 = DAT_20005a56;
              }
              if (7 < bVar3) {
                if ((short)((uint)_DAT_20005a48 >> 8) < -0x1e) {
                  FUN_00001ac8(7);
                  FUN_00009568(0x2000542c,0,0x200);
                  _DAT_20005a48 = 0;
                  bVar3 = DAT_20005a56;
                }
                if (8 < bVar3) {
                  if ((short)((uint)_DAT_20005a4c >> 8) < -0x1e) {
                    FUN_00001ac8(8);
                    FUN_00009568(0x2000562c,0,0x200);
                    _DAT_20005a4c = 0;
                    bVar3 = DAT_20005a56;
                  }
                  if ((9 < bVar3) && ((short)((uint)_DAT_20005a50 >> 8) < -0x1e)) {
                    FUN_00001ac8(9);
                    FUN_00009568(0x2000582c,0,0x200);
                    _DAT_20005a50 = 0;
/* ... truncated ... */
```

Callers:
- none

### `00001c8c` `FUN_00001b44`

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
  if (1 < bVar3) {
    if ((short)((uint)_DAT_20005a30 >> 8) < -0x1e) {
      FUN_00001ac8(1);
      FUN_00009568(0x2000482c,0,0x200);
      _DAT_20005a30 = 0;
      bVar3 = DAT_20005a56;
    }
    if (2 < bVar3) {
      if ((short)((uint)_DAT_20005a34 >> 8) < -0x1e) {
        FUN_00001ac8(2);
        FUN_00009568(0x20004a2c,0,0x200);
        _DAT_20005a34 = 0;
        bVar3 = DAT_20005a56;
      }
      if (3 < bVar3) {
        if ((short)((uint)_DAT_20005a38 >> 8) < -0x1e) {
          FUN_00001ac8(3);
          FUN_00009568(0x20004c2c,0,0x200);
          _DAT_20005a38 = 0;
          bVar3 = DAT_20005a56;
        }
        if (4 < bVar3) {
          if ((short)((uint)_DAT_20005a3c >> 8) < -0x1e) {
            FUN_00001ac8(4);
            FUN_00009568(0x20004e2c,0,0x200);
            _DAT_20005a3c = 0;
            bVar3 = DAT_20005a56;
          }
          if (5 < bVar3) {
            if ((short)((uint)_DAT_20005a40 >> 8) < -0x1e) {
              FUN_00001ac8(5);
              FUN_00009568(0x2000502c,0,0x200);
              _DAT_20005a40 = 0;
              bVar3 = DAT_20005a56;
            }
            if (6 < bVar3) {
              if ((short)((uint)_DAT_20005a44 >> 8) < -0x1e) {
                FUN_00001ac8(6);
                FUN_00009568(0x2000522c,0,0x200);
                _DAT_20005a44 = 0;
                bVar3 = DAT_20005a56;
              }
              if (7 < bVar3) {
                if ((short)((uint)_DAT_20005a48 >> 8) < -0x1e) {
                  FUN_00001ac8(7);
                  FUN_00009568(0x2000542c,0,0x200);
                  _DAT_20005a48 = 0;
                  bVar3 = DAT_20005a56;
                }
                if (8 < bVar3) {
                  if ((short)((uint)_DAT_20005a4c >> 8) < -0x1e) {
                    FUN_00001ac8(8);
                    FUN_00009568(0x2000562c,0,0x200);
                    _DAT_20005a4c = 0;
                    bVar3 = DAT_20005a56;
                  }
                  if ((9 < bVar3) && ((short)((uint)_DAT_20005a50 >> 8) < -0x1e)) {
                    FUN_00001ac8(9);
                    FUN_00009568(0x2000582c,0,0x200);
                    _DAT_20005a50 = 0;
/* ... truncated ... */
```

Callers:
- none

### `00001cfc` `FUN_00001b44`

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
  if (1 < bVar3) {
    if ((short)((uint)_DAT_20005a30 >> 8) < -0x1e) {
      FUN_00001ac8(1);
      FUN_00009568(0x2000482c,0,0x200);
      _DAT_20005a30 = 0;
      bVar3 = DAT_20005a56;
    }
    if (2 < bVar3) {
      if ((short)((uint)_DAT_20005a34 >> 8) < -0x1e) {
        FUN_00001ac8(2);
        FUN_00009568(0x20004a2c,0,0x200);
        _DAT_20005a34 = 0;
        bVar3 = DAT_20005a56;
      }
      if (3 < bVar3) {
        if ((short)((uint)_DAT_20005a38 >> 8) < -0x1e) {
          FUN_00001ac8(3);
          FUN_00009568(0x20004c2c,0,0x200);
          _DAT_20005a38 = 0;
          bVar3 = DAT_20005a56;
        }
        if (4 < bVar3) {
          if ((short)((uint)_DAT_20005a3c >> 8) < -0x1e) {
            FUN_00001ac8(4);
            FUN_00009568(0x20004e2c,0,0x200);
            _DAT_20005a3c = 0;
            bVar3 = DAT_20005a56;
          }
          if (5 < bVar3) {
            if ((short)((uint)_DAT_20005a40 >> 8) < -0x1e) {
              FUN_00001ac8(5);
              FUN_00009568(0x2000502c,0,0x200);
              _DAT_20005a40 = 0;
              bVar3 = DAT_20005a56;
            }
            if (6 < bVar3) {
              if ((short)((uint)_DAT_20005a44 >> 8) < -0x1e) {
                FUN_00001ac8(6);
                FUN_00009568(0x2000522c,0,0x200);
                _DAT_20005a44 = 0;
                bVar3 = DAT_20005a56;
              }
              if (7 < bVar3) {
                if ((short)((uint)_DAT_20005a48 >> 8) < -0x1e) {
                  FUN_00001ac8(7);
                  FUN_00009568(0x2000542c,0,0x200);
                  _DAT_20005a48 = 0;
                  bVar3 = DAT_20005a56;
                }
                if (8 < bVar3) {
                  if ((short)((uint)_DAT_20005a4c >> 8) < -0x1e) {
                    FUN_00001ac8(8);
                    FUN_00009568(0x2000562c,0,0x200);
                    _DAT_20005a4c = 0;
                    bVar3 = DAT_20005a56;
                  }
                  if ((9 < bVar3) && ((short)((uint)_DAT_20005a50 >> 8) < -0x1e)) {
                    FUN_00001ac8(9);
                    FUN_00009568(0x2000582c,0,0x200);
                    _DAT_20005a50 = 0;
/* ... truncated ... */
```

Callers:
- none

## Address References

### `20004291`

- from `00000e82` in `FUN_00000e5c` @ `00000e5c` type=WRITE
- from `00000e7c` in `FUN_00000e5c` @ `00000e5c` type=PARAM
- from `00000e58` in `FUN_00000e50` @ `00000e50` type=READ

#### `FUN_00000e5c` @ `00000e5c`

Site `00000e82`:

```asm
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
00000e98: movt r1,#0x0
00000e9c: movt r0,#0x2000
00000ea0: bl 0x00004f2c
```

Site `00000e7c`:

```asm
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
00000e98: movt r1,#0x0
```

#### `FUN_00000e50` @ `00000e50`

Site `00000e58`:

```asm
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
```

### `20004292`

- from `00001128` in `FUN_000010a4` @ `000010a4` type=WRITE
- from `00001122` in `FUN_000010a4` @ `000010a4` type=PARAM
- from `000011b4` in `FUN_000010a4` @ `000010a4` type=READ

#### `FUN_000010a4` @ `000010a4`

Site `00001128`:

```asm
00001110: bne 0x000011e8
00001112: movw r2,#0x95f4
00001116: movt r2,#0x0
0000111a: str r2,[r3,#0x0]
0000111c: movw r3,#0x4292
00001120: movs r2,#0x4
00001122: movt r3,#0x2000
00001126: movs r0,r4
00001128: strb r2,[r3,#0x0]
0000112a: bl 0x00000d54
0000112e: cmp r0,#0x0
00001130: bne 0x000010d0
00001132: pop {r7}
00001134: mov r8,r7
00001136: pop {r4,r5,r6,r7,pc}
00001138: ldrb r2,[r6,#0x0]
0000113a: ldr r1,[r7,#0x0]
```

Site `00001122`:

```asm
0000110a: movt r3,#0x2000
0000110e: cmp r0,#0x0
00001110: bne 0x000011e8
00001112: movw r2,#0x95f4
00001116: movt r2,#0x0
0000111a: str r2,[r3,#0x0]
0000111c: movw r3,#0x4292
00001120: movs r2,#0x4
00001122: movt r3,#0x2000
00001126: movs r0,r4
00001128: strb r2,[r3,#0x0]
0000112a: bl 0x00000d54
0000112e: cmp r0,#0x0
00001130: bne 0x000010d0
00001132: pop {r7}
00001134: mov r8,r7
00001136: pop {r4,r5,r6,r7,pc}
```

Site `000011b4`:

```asm
000011a0: movs r3,#0x0
000011a2: mov r2,r8
000011a4: strb r3,[r5,#0x0]
000011a6: strb r3,[r2,#0x0]
000011a8: b 0x000010c8
000011aa: movw r3,#0x4292
000011ae: movt r3,#0x2000
000011b2: adds r2,#0x1
000011b4: ldrb r3,[r3,#0x0]
000011b6: uxtb r2,r2
000011b8: strb r2,[r6,#0x0]
000011ba: cmp r3,r2
000011bc: bls 0x000011c0
000011be: b 0x000010c8
000011c0: movs r3,#0x2
000011c2: strb r3,[r5,#0x0]
000011c4: b 0x000010c8
```

### `20004294`

- from `0000111a` in `FUN_000010a4` @ `000010a4` type=WRITE
- from `0000113a` in `FUN_000010a4` @ `000010a4` type=READ

#### `FUN_000010a4` @ `000010a4`

Site `0000111a`:

```asm
00001100: strb r3,[r2,#0x0]
00001102: bl 0x00000e50
00001106: movw r3,#0x4294
0000110a: movt r3,#0x2000
0000110e: cmp r0,#0x0
00001110: bne 0x000011e8
00001112: movw r2,#0x95f4
00001116: movt r2,#0x0
0000111a: str r2,[r3,#0x0]
0000111c: movw r3,#0x4292
00001120: movs r2,#0x4
00001122: movt r3,#0x2000
00001126: movs r0,r4
00001128: strb r2,[r3,#0x0]
0000112a: bl 0x00000d54
0000112e: cmp r0,#0x0
00001130: bne 0x000010d0
```

Site `0000113a`:

```asm
00001128: strb r2,[r3,#0x0]
0000112a: bl 0x00000d54
0000112e: cmp r0,#0x0
00001130: bne 0x000010d0
00001132: pop {r7}
00001134: mov r8,r7
00001136: pop {r4,r5,r6,r7,pc}
00001138: ldrb r2,[r6,#0x0]
0000113a: ldr r1,[r7,#0x0]
0000113c: ldrb r1,[r1,r2]
0000113e: cmp r1,r0
00001140: beq 0x000011aa
00001142: cmp r0,#0xf0
00001144: beq 0x000011c6
00001146: movs r3,#0x0
00001148: strb r3,[r5,#0x0]
0000114a: b 0x000010c8
```

### `20004298`

- from `000010a0` in `FUN_00001098` @ `00001098` type=WRITE
- from `0000118a` in `FUN_000010a4` @ `000010a4` type=READ

#### `FUN_00001098` @ `00001098`

Site `000010a0`:

```asm
00001084: movt r0,#0x2000
00001088: bl 0x00000d6c
0000108c: pop {r3,r4,r5,r6,r7,pc}
0000108e: movw r4,#0x95f8
00001092: movt r4,#0x0
00001096: b 0x00001044
00001098: movw r3,#0x4298
0000109c: movt r3,#0x2000
000010a0: str r0,[r3,#0x0]
000010a2: bx lr
000010a4: push {r4,r5,r6,r7,lr}
000010a6: mov lr,r8
000010a8: push {lr}
000010aa: bl 0x00002ab8
000010ae: movw r5,#0x4321
000010b2: movw r6,#0x4320
000010b6: movw r7,#0x4294
```

#### `FUN_000010a4` @ `000010a4`

Site `0000118a`:

```asm
00001170: strb r3,[r1,#0x0]
00001172: movw r3,#0x42a0
00001176: movt r3,#0x2000
0000117a: strb r0,[r3,r2]
0000117c: b 0x000010c8
0000117e: movw r3,#0x4298
00001182: movw r8,#0x429c
00001186: movt r3,#0x2000
0000118a: ldr r3,[r3,#0x0]
0000118c: movt r8,#0x2000
00001190: cbz r3,0x000011a0
00001192: mov r2,r8
00001194: movw r0,#0x42a0
00001198: ldrb r1,[r2,#0x0]
0000119a: movt r0,#0x2000
0000119e: blx r3
000011a0: movs r3,#0x0
```

### `20004084`

- no direct references found

### `200040a0`

- no direct references found

### `20004538`

- from `00001424` in `FUN_0000140c` @ `0000140c` type=READ
- from `00001268` in `<none>` @ `<none>` type=READ
- from `00001276` in `<none>` @ `<none>` type=WRITE
- from `00001228` in `<none>` @ `<none>` type=WRITE

#### `FUN_0000140c` @ `0000140c`

Site `00001424`:

```asm
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
```

### `200045ca`

- from `0000129e` in `FUN_00001288` @ `00001288` type=READ
- from `00001324` in `FUN_00001288` @ `00001288` type=READ
- from `000012de` in `FUN_00001288` @ `00001288` type=DATA
- from `00001348` in `FUN_00001288` @ `00001288` type=READ
- from `00001728` in `FUN_000016f4` @ `000016f4` type=WRITE
- from `00001722` in `FUN_000016f4` @ `000016f4` type=PARAM

#### `FUN_00001288` @ `00001288`

Site `0000129e`:

```asm
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
```

Site `00001324`:

```asm
00001312: bge 0x000012ca
00001314: ldrh r3,[r4,#0x0]
00001316: movs r0,r5
00001318: strh r3,[r6,#0x0]
0000131a: ldrh r1,[r4,#0x0]
0000131c: sxth r1,r1
0000131e: bl 0x00000eec
00001322: mov r3,r8
00001324: ldrb r1,[r3,#0x0]
00001326: b 0x000012d2
00001328: add sp,#0xc
0000132a: pop {r4,r5,r6,r7}
0000132c: mov r11,r7
0000132e: mov r10,r6
00001330: mov r9,r5
00001332: mov r8,r4
00001334: pop {r4,r5,r6,r7,pc}
```

Site `000012de`:

```asm
000012ce: cmp r3,#0x0
000012d0: bne 0x00001336
000012d2: ldr r3,[sp,#0x4]
000012d4: adds r5,#0x1
000012d6: adds r3,#0x1
000012d8: uxtb r5,r5
000012da: adds r4,#0x2
000012dc: adds r6,#0x2
000012de: str r3,[sp,#0x4]
000012e0: cmp r5,r1
000012e2: bcs 0x00001328
000012e4: ldrh r3,[r4,#0x0]
000012e6: sxth r3,r3
000012e8: cmp r3,#0xb
000012ea: ble 0x000012f6
000012ec: ldrh r3,[r4,#0x0]
000012ee: mov r0,r9
```

Site `00001348`:

```asm
00001336: ldrh r1,[r4,#0x0]
00001338: movs r0,r5
0000133a: sxth r1,r1
0000133c: bl 0x00000eec
00001340: mov r3,r11
00001342: ldr r2,[sp,#0x4]
00001344: strb r3,[r2,#0x0]
00001346: mov r3,r8
00001348: ldrb r1,[r3,#0x0]
0000134a: b 0x000012d2
0000134c: push {r3,r4,r5,r6,r7,lr}
0000134e: mov r7,r8
00001350: mov lr,r9
00001352: push {r7,lr}
00001354: movw r7,#0x4532
00001358: movt r7,#0x2000
0000135c: ldrh r3,[r7,#0x0]
```

#### `FUN_000016f4` @ `000016f4`

Site `00001728`:

```asm
00001710: movs r1,#0xb
00001712: movt r3,#0x2000
00001716: strb r1,[r3,#0x0]
00001718: movw r3,#0x45ca
0000171c: movw r5,#0x95fc
00001720: movs r6,#0x0
00001722: movt r3,#0x2000
00001726: ldr r4,[0x0000179c]
00001728: strb r2,[r3,#0x0]
0000172a: movt r5,#0x0
0000172e: movw r0,#0x5cbc
00001732: movs r2,r4
00001734: ldrh r1,[r5,#0x0]
00001736: movt r0,#0x2000
0000173a: bl 0x00004df4
0000173e: ldrb r3,[r4,#0x0]
00001740: adds r6,#0x1
```

Site `00001722`:

```asm
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
0000172a: movt r5,#0x0
0000172e: movw r0,#0x5cbc
00001732: movs r2,r4
00001734: ldrh r1,[r5,#0x0]
00001736: movt r0,#0x2000
0000173a: bl 0x00004df4
```

### `200045cc`

- from `00001416` in `FUN_0000140c` @ `0000140c` type=READ
- from `00001570` in `FUN_0000140c` @ `0000140c` type=READ
- from `00001590` in `FUN_0000140c` @ `0000140c` type=READ
- from `00001614` in `FUN_0000140c` @ `0000140c` type=READ
- from `000015b6` in `FUN_0000140c` @ `0000140c` type=READ
- from `000015d6` in `FUN_0000140c` @ `0000140c` type=READ
- from `00001550` in `FUN_0000140c` @ `0000140c` type=READ
- from `00001530` in `FUN_0000140c` @ `0000140c` type=READ
- from `00001510` in `FUN_0000140c` @ `0000140c` type=READ
- from `0000170a` in `FUN_000016f4` @ `000016f4` type=WRITE
- from `00001744` in `FUN_000016f4` @ `000016f4` type=READ
- from `0000120a` in `<none>` @ `<none>` type=READ
- from `00001278` in `<none>` @ `<none>` type=READ
- from `0000122a` in `<none>` @ `<none>` type=READ

#### `FUN_0000140c` @ `0000140c`

Site `00001416`:

```asm
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
```

Site `00001570`:

```asm
0000155c: movt r2,#0x0
00001560: mov r12,r2
00001562: lsls r3,r0,#0x3
00001564: adds r3,r3,r0
00001566: add r3,r12
00001568: ldrb r0,[r3,#0x3]
0000156a: movs r1,r6
0000156c: bl 0x00000fb0
00001570: ldrb r3,[r5,#0x0]
00001572: b 0x0000147a
00001574: bl 0x00000e50
00001578: movw r2,#0x9664
0000157c: movt r2,#0x0
00001580: mov r12,r2
00001582: lsls r3,r0,#0x3
00001584: adds r3,r3,r0
00001586: add r3,r12
```

Site `00001590`:

```asm
0000157c: movt r2,#0x0
00001580: mov r12,r2
00001582: lsls r3,r0,#0x3
00001584: adds r3,r3,r0
00001586: add r3,r12
00001588: ldrb r0,[r3,#0x4]
0000158a: movs r1,r6
0000158c: bl 0x00000fb0
00001590: ldrb r3,[r5,#0x0]
00001592: cmp r3,#0x5
00001594: bls 0x00001598
00001596: b 0x00001496
00001598: b 0x000014f6
0000159a: bl 0x00000e50
0000159e: movw r2,#0x9664
000015a2: movt r2,#0x0
000015a6: mov r12,r2
```

Site `00001614`:

```asm
00001600: movt r2,#0x0
00001604: mov r12,r2
00001606: lsls r3,r0,#0x3
00001608: adds r3,r3,r0
0000160a: add r3,r12
0000160c: ldrb r0,[r3,#0x5]
0000160e: movs r1,r6
00001610: bl 0x00000fb0
00001614: ldrb r3,[r5,#0x0]
00001616: b 0x000014aa
00001618: movw r3,#0x4530
0000161c: push {r4,r5,r6,lr}
0000161e: movt r3,#0x2000
00001622: ldrh r1,[r0,#0x0]
00001624: ldrb r2,[r3,#0x0]
00001626: sxth r1,r1
00001628: cbz r2,0x0000166e
```

Site `000015b6`:

```asm
000015a2: movt r2,#0x0
000015a6: mov r12,r2
000015a8: lsls r3,r0,#0x3
000015aa: adds r3,r3,r0
000015ac: add r3,r12
000015ae: ldrb r0,[r3,#0x6]
000015b0: movs r1,r6
000015b2: bl 0x00000fb0
000015b6: ldrb r3,[r5,#0x0]
000015b8: b 0x000014c2
000015ba: bl 0x00000e50
000015be: movw r2,#0x9664
000015c2: movt r2,#0x0
000015c6: mov r12,r2
000015c8: lsls r3,r0,#0x3
000015ca: adds r3,r3,r0
000015cc: add r3,r12
```

Site `000015d6`:

```asm
000015c2: movt r2,#0x0
000015c6: mov r12,r2
000015c8: lsls r3,r0,#0x3
000015ca: adds r3,r3,r0
000015cc: add r3,r12
000015ce: ldrb r0,[r3,#0x7]
000015d0: movs r1,r6
000015d2: bl 0x00000fb0
000015d6: ldrb r3,[r5,#0x0]
000015d8: b 0x000014da
000015da: bl 0x00000e50
000015de: movw r2,#0x9664
000015e2: movt r2,#0x0
000015e6: mov r12,r2
000015e8: lsls r3,r0,#0x3
000015ea: adds r3,r3,r0
000015ec: add r3,r12
```

Site `00001550`:

```asm
0000153c: movt r2,#0x0
00001540: mov r12,r2
00001542: lsls r3,r0,#0x3
00001544: adds r3,r3,r0
00001546: add r3,r12
00001548: ldrb r0,[r3,#0x2]
0000154a: movs r1,r6
0000154c: bl 0x00000fb0
00001550: ldrb r3,[r5,#0x0]
00001552: b 0x00001462
00001554: bl 0x00000e50
00001558: movw r2,#0x9664
0000155c: movt r2,#0x0
00001560: mov r12,r2
00001562: lsls r3,r0,#0x3
00001564: adds r3,r3,r0
00001566: add r3,r12
```

Site `00001530`:

```asm
0000151c: movt r2,#0x0
00001520: mov r12,r2
00001522: lsls r3,r0,#0x3
00001524: adds r3,r3,r0
00001526: add r3,r12
00001528: ldrb r0,[r3,#0x1]
0000152a: movs r1,r6
0000152c: bl 0x00000fb0
00001530: ldrb r3,[r5,#0x0]
00001532: b 0x0000144c
00001534: bl 0x00000e50
00001538: movw r2,#0x9664
0000153c: movt r2,#0x0
00001540: mov r12,r2
00001542: lsls r3,r0,#0x3
00001544: adds r3,r3,r0
00001546: add r3,r12
```

Site `00001510`:

```asm
000014f8: bl 0x00000e50
000014fc: movw r3,#0x9664
00001500: lsls r2,r0,#0x3
00001502: movt r3,#0x0
00001506: adds r2,r2,r0
00001508: ldrb r0,[r2,r3]
0000150a: movs r1,r6
0000150c: bl 0x00000fb0
00001510: ldrb r3,[r5,#0x0]
00001512: b 0x00001436
00001514: bl 0x00000e50
00001518: movw r2,#0x9664
0000151c: movt r2,#0x0
00001520: mov r12,r2
00001522: lsls r3,r0,#0x3
00001524: adds r3,r3,r0
00001526: add r3,r12
```

#### `FUN_000016f4` @ `000016f4`

Site `0000170a`:

```asm
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
```

Site `00001744`:

```asm
0000172e: movw r0,#0x5cbc
00001732: movs r2,r4
00001734: ldrh r1,[r5,#0x0]
00001736: movt r0,#0x2000
0000173a: bl 0x00004df4
0000173e: ldrb r3,[r4,#0x0]
00001740: adds r6,#0x1
00001742: strh r3,[r4,#0x2]
00001744: ldrb r3,[r7,#0x0]
00001746: adds r5,#0x4
00001748: adds r4,#0x10
0000174a: cmp r6,r3
0000174c: blt 0x0000172e
0000174e: movw r1,#0x1201
00001752: movw r0,#0x45e0
00001756: movt r1,#0x0
0000175a: movt r0,#0x2000
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

- from `00002a52` in `FUN_00002a14` @ `00002a14` type=PARAM

#### `FUN_00002a14` @ `00002a14`

Site `00002a52`:

```asm
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
```

### `00009818`

- from `00000e98` in `FUN_00000e5c` @ `00000e5c` type=PARAM

#### `FUN_00000e5c` @ `00000e5c`

Site `00000e98`:

```asm
00000e7c: movt r3,#0x2000
00000e80: movs r0,#0x9
00000e82: strb r2,[r3,#0x0]
00000e84: bl 0x00002a14
00000e88: bl 0x00002f88
00000e8c: bl 0x00009058
00000e90: movw r1,#0x9818
00000e94: movw r0,#0x5d04
00000e98: movt r1,#0x0
00000e9c: movt r0,#0x2000
00000ea0: bl 0x00004f2c
00000ea4: movw r0,#0x5d04
00000ea8: movt r0,#0x2000
00000eac: bl 0x00004f14
00000eb0: bl 0x000016f4
00000eb4: bl 0x000017d4
00000eb8: b 0x00000eb4
```

### `00009874`

- from `00002a3c` in `FUN_00002a14` @ `00002a14` type=PARAM

#### `FUN_00002a14` @ `00002a14`

Site `00002a3c`:

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
```

### `000098c4`

- from `000009ca` in `FUN_000009c0` @ `000009c0` type=READ

#### `FUN_000009c0` @ `000009c0`

Site `000009ca`:

```asm
000009b0: movw r2,#0x413c
000009b4: lsls r3,r3,#0x1
000009b6: movt r2,#0x2000
000009ba: ldrh r0,[r3,r2]
000009bc: bx lr
000009c0: movw r3,#0x98c0
000009c4: movt r3,#0x0
000009c8: push {r4,lr}
000009ca: ldmia r3!,{r0,r1}
000009cc: bl 0x0000557c
000009d0: cbz r0,0x000009d8
000009d2: cmp r0,#0xe
000009d4: beq 0x000009d8
000009d6: pop {r4,pc}
000009d8: movw r3,#0x4290
000009dc: movs r2,#0x1
000009de: movt r3,#0x2000
```

### `000098c8`

- from `000009ca` in `FUN_000009c0` @ `000009c0` type=PARAM

#### `FUN_000009c0` @ `000009c0`

Site `000009ca`:

```asm
000009b0: movw r2,#0x413c
000009b4: lsls r3,r3,#0x1
000009b6: movt r2,#0x2000
000009ba: ldrh r0,[r3,r2]
000009bc: bx lr
000009c0: movw r3,#0x98c0
000009c4: movt r3,#0x0
000009c8: push {r4,lr}
000009ca: ldmia r3!,{r0,r1}
000009cc: bl 0x0000557c
000009d0: cbz r0,0x000009d8
000009d2: cmp r0,#0xe
000009d4: beq 0x000009d8
000009d6: pop {r4,pc}
000009d8: movw r3,#0x4290
000009dc: movs r2,#0x1
000009de: movt r3,#0x2000
```

## Scalar/Immediate Hits

### `0x204`

- `00000e68: movw r1,#0x204` in `FUN_00000e5c` @ `00000e5c`

### `0x8f`

- `000206f2: movs r5,#0x8f` in `FUN_0002064c` @ `0002064c`
- `0003aba4: movs r2,#0x8f` in `FUN_0003ab58` @ `0003ab58`
- `0003d7b8: movs r3,#0x8f` in `FUN_0003d600` @ `0003d600`

### `0x7f`

- `00000ef2: movs r7,#0x7f` in `FUN_00000eec` @ `00000eec`
- `00002af4: movs r4,#0x7f` in `FUN_00002af0` @ `00002af0`
- `000030c6: movs r0,#0x7f` in `FUN_0000308c` @ `0000308c`
- `00004af4: movs r3,#0x7f` in `FUN_00004abc` @ `00004abc`
- `000059ee: movs r1,#0x7f` in `FUN_00005808` @ `00005808`
- `00005bfa: movs r1,#0x7f` in `FUN_00005b00` @ `00005b00`
- `00005d60: movw r12,#0x7f` in `FUN_00005cb4` @ `00005cb4`
- `000206f0: movs r3,#0x7f` in `FUN_0002064c` @ `0002064c`
- `00021bba: movs r3,#0x7f` in `FUN_00021b70` @ `00021b70`
- `00042834: movs r1,#0x7f` in `FUN_000427a8` @ `000427a8`
- `0004284a: movs r0,#0x7f` in `FUN_000427a8` @ `000427a8`
- `000429ea: movs r2,#0x7f` in `FUN_000427a8` @ `000427a8`
- `00042d58: movs r1,#0x7f` in `<none>` @ `<none>`
- `00042d70: movs r0,#0x7f` in `<none>` @ `<none>`
- `00042e02: movs r2,#0x7f` in `<none>` @ `<none>`
- `00047094: cmp r3,#0x7f` in `FUN_00046e7c` @ `00046e7c`
- `000470d4: cmp r3,#0x7f` in `FUN_00046e7c` @ `00046e7c`
- `0004f65a: cmp r4,#0x7f` in `FUN_0004f64c` @ `0004f64c`
- `0004f718: cmp r1,#0x7f` in `FUN_0004f70c` @ `0004f70c`
- `0004f9a2: cmp r3,#0x7f` in `FUN_0004f978` @ `0004f978`
- `0004fd96: cmp r2,#0x7f` in `FUN_0004fd0c` @ `0004fd0c`
- `000508ec: movs r1,#0x7f` in `FUN_000508aa` @ `000508aa`
- `00050948: movs r1,#0x7f` in `FUN_00050912` @ `00050912`
- `00050b22: movs r1,#0x7f` in `FUN_00050b20` @ `00050b20`
- `00051a08: movs r1,#0x7f` in `FUN_000519d2` @ `000519d2`
- `0005c6d6: movs r2,#0x7f` in `FUN_0005c6d0` @ `0005c6d0`
- `0005e7b8: movs r1,#0x7f` in `FUN_0005e274` @ `0005e274`

### `0x0`

- `00000452: movw r3,#0x0` in `FUN_0000043c` @ `0000043c`
- `00000456: movt r3,#0x0` in `FUN_0000043c` @ `0000043c`
- `0000047e: movw r3,#0x0` in `FUN_00000460` @ `00000460`
- `00000482: movt r3,#0x0` in `FUN_00000460` @ `00000460`
- `00000496: ldrb r3,[r4,#0x0]` in `FUN_0000048c` @ `0000048c`
- `0000049e: movw r3,#0x0` in `FUN_0000048c` @ `0000048c`
- `000004a2: movt r3,#0x0` in `FUN_0000048c` @ `0000048c`
- `000004ac: movt r0,#0x0` in `FUN_0000048c` @ `0000048c`
- `000004b6: strb r3,[r4,#0x0]` in `FUN_0000048c` @ `0000048c`
- `000004c0: movt r3,#0x0` in `<none>` @ `<none>`
- `000004d4: movt r0,#0x0` in `<none>` @ `<none>`
- `00000530: movt r1,#0x0` in `FUN_000004e4` @ `000004e4`
- `0000054a: movt r1,#0x0` in `FUN_000004e4` @ `000004e4`
- `00000566: str r3,[r0,#0x0]` in `FUN_000004e4` @ `000004e4`
- `00000574: movt r3,#0x0` in `FUN_000004e4` @ `000004e4`
- `00000590: movt r2,#0x0` in `FUN_000004e4` @ `000004e4`
- `00000596: ldr r0,[r2,#0x0]` in `FUN_000004e4` @ `000004e4`
- `000005a6: str r0,[r3,#0x0]` in `FUN_000004e4` @ `000004e4`
- `000005ae: movt r2,#0x0` in `FUN_000004e4` @ `000004e4`
- `000005b2: ldr r0,[r2,#0x0]` in `FUN_000004e4` @ `000004e4`
- `000005b8: str r0,[r3,#0x0]` in `FUN_000004e4` @ `000004e4`
- `000005c4: movs r1,#0x0` in `FUN_000004e4` @ `000004e4`
- `000005ee: movs r0,#0x0` in `FUN_000004e4` @ `000004e4`
- `000005f0: strb r2,[r3,#0x0]` in `FUN_000004e4` @ `000004e4`
- `000005fe: cmp r0,#0x0` in `FUN_000005fc` @ `000005fc`
- `0000060a: ldrb r3,[r3,#0x0]` in `FUN_000005fc` @ `000005fc`
- `0000060c: cmp r3,#0x0` in `FUN_000005fc` @ `000005fc`
- `00000612: ldrh r2,[r0,#0x0]` in `FUN_000005fc` @ `000005fc`
- `00000660: str r4,[r0,#0x0]` in `FUN_000005fc` @ `000005fc`
- `00000678: movs r0,#0x0` in `FUN_000005fc` @ `000005fc`
- `000006a4: str r4,[r1,#0x0]` in `FUN_000005fc` @ `000005fc`
- `000006c6: ldrb r3,[r3,#0x0]` in `FUN_000006b8` @ `000006b8`
- `000006ca: cmp r3,#0x0` in `FUN_000006b8` @ `000006b8`
- `000006d2: movt r5,#0x0` in `FUN_000006b8` @ `000006b8`
- `000006d6: ldr r7,[r5,#0x0]` in `FUN_000006b8` @ `000006b8`
- `000006f4: ldr r0,[r6,#0x0]` in `FUN_000006b8` @ `000006b8`
- `000006fc: cmp r0,#0x0` in `FUN_000006b8` @ `000006b8`
- `00000708: cmp r0,#0x0` in `FUN_000006b8` @ `000006b8`
- `00000716: cmp r0,#0x0` in `FUN_000006b8` @ `000006b8`
- `0000071e: movt r3,#0x0` in `FUN_000006b8` @ `000006b8`
- `00000722: ldr r3,[r3,#0x0]` in `FUN_000006b8` @ `000006b8`
- `00000734: movt r3,#0x0` in `FUN_000006b8` @ `000006b8`
- `0000073a: movw r9,#0x0` in `FUN_000006b8` @ `000006b8`
- `0000073e: ldr r7,[r3,#0x0]` in `FUN_000006b8` @ `000006b8`
- `0000075a: cmp r0,#0x0` in `FUN_000006b8` @ `000006b8`
- `0000075e: ldrb r3,[r6,#0x0]` in `FUN_000006b8` @ `000006b8`
- `00000760: cmp r3,#0x0` in `FUN_000006b8` @ `000006b8`
- `00000766: movs r2,#0x0` in `FUN_000006b8` @ `000006b8`
- `00000768: strb r3,[r6,#0x0]` in `FUN_000006b8` @ `000006b8`
- `0000076a: movs r1,#0x0` in `FUN_000006b8` @ `000006b8`
- `0000076c: movs r3,#0x0` in `FUN_000006b8` @ `000006b8`
- `00000788: ldrb r3,[r3,#0x0]` in `FUN_00000780` @ `00000780`
- `00000796: movs r0,#0x0` in `FUN_00000780` @ `00000780`
- `000007aa: ldrb r3,[r3,#0x0]` in `FUN_0000079c` @ `0000079c`
- `000007ae: cmp r3,#0x0` in `FUN_0000079c` @ `0000079c`
- `000007ba: movt r3,#0x0` in `FUN_0000079c` @ `0000079c`
- `000007c4: movs r6,#0x0` in `FUN_0000079c` @ `0000079c`
- `000007c6: movs r5,#0x0` in `FUN_0000079c` @ `0000079c`
- `000007cc: ldr r7,[r3,#0x0]` in `FUN_0000079c` @ `0000079c`
- `000007dc: strh r3,[r4,#0x0]` in `FUN_0000079c` @ `0000079c`
- `0000082a: cmp r3,#0x0` in `FUN_0000079c` @ `0000079c`
- `0000082e: movs r3,#0x0` in `FUN_0000079c` @ `0000079c`
- `00000830: strh r3,[r4,#0x0]` in `FUN_0000079c` @ `0000079c`
- `00000834: cmp r3,#0x0` in `FUN_0000079c` @ `0000079c`
- `00000838: movs r3,#0x0` in `FUN_0000079c` @ `0000079c`
- `0000083e: cmp r3,#0x0` in `FUN_0000079c` @ `0000079c`
- `00000842: movs r0,#0x0` in `FUN_0000079c` @ `0000079c`
- `0000084c: movs r0,#0x0` in `FUN_0000079c` @ `0000079c`
- `0000086c: ldrb r3,[r3,#0x0]` in `FUN_00000864` @ `00000864`
- `0000087a: movs r0,#0x0` in `FUN_00000864` @ `00000864`
- `00000888: ldrb r3,[r3,#0x0]` in `FUN_00000880` @ `00000880`
- `00000898: strh r2,[r0,#0x0]` in `FUN_00000880` @ `00000880`
- `000008c6: ldrh r3,[r3,#0x0]` in `FUN_00000880` @ `00000880`
- `000008ca: movs r0,#0x0` in `FUN_00000880` @ `00000880`
- `000008da: cmp r0,#0x0` in `FUN_000008d8` @ `000008d8`
- `000008e6: ldrb r3,[r3,#0x0]` in `FUN_000008d8` @ `000008d8`
- `000008e8: cmp r3,#0x0` in `FUN_000008d8` @ `000008d8`
- `000008f0: movt r3,#0x0` in `FUN_000008d8` @ `000008d8`
- `000008f4: ldr r3,[r3,#0x0]` in `FUN_000008d8` @ `000008d8`
- `000008fe: ldr r1,[r2,#0x0]` in `FUN_000008d8` @ `000008d8`
- ... truncated after 80 hits

### `0x9`

- `00000a1a: cmp r3,#0x9` in `FUN_000009e8` @ `000009e8`
- `00000a34: movs r3,#0x9` in `FUN_000009e8` @ `000009e8`
- `00000b5a: movs r3,#0x9` in `FUN_00000b30` @ `00000b30`
- `00000e80: movs r0,#0x9` in `FUN_00000e5c` @ `00000e5c`
- `00001022: movs r2,#0x9` in `FUN_00000ff4` @ `00000ff4`
- `00001222: ldrb r2,[r4,#0x9]` in `<none>` @ `<none>`
- `0000124e: adds r2,#0x9` in `<none>` @ `<none>`
- `0000126e: ldrb r2,[r4,#0x9]` in `<none>` @ `<none>`
- `000013ce: cmp r4,#0x9` in `FUN_0000134c` @ `0000134c`
- `00001796: movs r3,#0x9` in `FUN_000016f4` @ `000016f4`
- `00001a24: cmp r3,#0x9` in `FUN_0000190c` @ `0000190c`
- `00001a90: cmp r3,#0x9` in `FUN_0000190c` @ `0000190c`
- `00001c66: cmp r2,#0x9` in `FUN_00001b44` @ `00001b44`
- `00001e02: cmp r2,#0x9` in `FUN_00001b44` @ `00001b44`
- `00001f0e: cmp r2,#0x9` in `FUN_00001b44` @ `00001b44`
- `00001f26: movs r0,#0x9` in `FUN_00001b44` @ `00001b44`
- `00002442: cmp r3,#0x9` in `FUN_00002428` @ `00002428`
- `00002b46: ldrb r7,[r0,#0x9]` in `FUN_00002af0` @ `00002af0`
- `00002d8c: strb r3,[r5,#0x9]` in `FUN_00002af0` @ `00002af0`
- `00003100: strb r5,[r4,#0x9]` in `FUN_0000308c` @ `0000308c`
- `00003270: strb r7,[r4,#0x9]` in `FUN_000031fc` @ `000031fc`
- `00003478: ldrb r2,[r3,#0x9]` in `FUN_000031fc` @ `000031fc`
- `000035a6: strb r2,[r1,#0x9]` in `FUN_0000355c` @ `0000355c`
- `000036ce: cmp r2,#0x9` in `FUN_00003690` @ `00003690`
- `00003ad4: cmp r0,#0x9` in `FUN_00003914` @ `00003914`
- `00003f88: cmp r5,#0x9` in `FUN_00003e3a` @ `00003e3a`
- `00003f94: adds r4,#0x9` in `FUN_00003e3a` @ `00003e3a`
- `000048da: movs r6,#0x9` in `FUN_00004854` @ `00004854`
- `000049a2: strb r2,[r3,#0x9]` in `FUN_00004854` @ `00004854`
- `00004a62: movs r0,#0x9` in `FUN_00004854` @ `00004854`
- `00004e5e: lsls r3,r3,#0x9` in `FUN_00004e18` @ `00004e18`
- `00004fb6: lsls r6,r6,#0x9` in `FUN_00004f2c` @ `00004f2c`
- `0000618e: lsls r3,r3,#0x9` in `<none>` @ `<none>`
- `0000619a: lsls r3,r3,#0x9` in `<none>` @ `<none>`
- `00006390: cmp r3,#0x9` in `FUN_00006360` @ `00006360`
- `000063d0: cmp r2,#0x9` in `FUN_00006360` @ `00006360`
- `000067f4: cmp r1,#0x9` in `<none>` @ `<none>`
- `00006810: lsls r2,r2,#0x9` in `<none>` @ `<none>`
- `000068ba: lsls r2,r2,#0x9` in `<none>` @ `<none>`
- `00006cb4: movs r5,#0x9` in `FUN_00006a94` @ `00006a94`
- `00006d14: cmp r0,#0x9` in `FUN_00006cc0` @ `00006cc0`
- `000091a8: lsls r3,r3,#0x9` in `FUN_00009174` @ `00009174`
- `000094e6: lsls r2,r2,#0x9` in `FUN_00009210` @ `00009210`
- `00020724: movs r2,#0x9` in `FUN_0002064c` @ `0002064c`
- `00020746: movs r2,#0x9` in `FUN_0002064c` @ `0002064c`
- `00021ba6: strb r7,[r5,#0x9]` in `FUN_00021b70` @ `00021b70`
- `000261f2: strb r7,[r0,#0x9]` in `FUN_000261c8` @ `000261c8`
- `00026224: ldrb r3,[r4,#0x9]` in `FUN_0002620c` @ `0002620c`
- `00026dda: lsls r2,r2,#0x9` in `FUN_00026d74` @ `00026d74`
- `00026e8a: movs r3,#0x9` in `FUN_00026d74` @ `00026d74`
- `00026f36: lsls r3,r3,#0x9` in `FUN_00026ecc` @ `00026ecc`
- `00028070: movs r1,#0x9` in `<none>` @ `<none>`
- `00028102: movs r1,#0x9` in `<none>` @ `<none>`
- `0002816a: movs r1,#0x9` in `<none>` @ `<none>`
- `000281d2: movs r1,#0x9` in `<none>` @ `<none>`
- `000328ce: movs r1,#0x9` in `FUN_000328c0` @ `000328c0`
- `00033498: movs r2,#0x9` in `FUN_00033478` @ `00033478`
- `0003355e: cmp r0,#0x9` in `FUN_00033478` @ `00033478`
- `00033ddc: movs r2,#0x9` in `FUN_000338a4` @ `000338a4`
- `00034e4c: lsls r1,r1,#0x9` in `FUN_00034d20` @ `00034d20`
- `00034e5a: lsls r1,r1,#0x9` in `FUN_00034d20` @ `00034d20`
- `00034e6c: lsls r1,r1,#0x9` in `FUN_00034d20` @ `00034d20`
- `00034e7c: lsls r1,r1,#0x9` in `FUN_00034d20` @ `00034d20`
- `00034e8c: lsls r1,r1,#0x9` in `FUN_00034d20` @ `00034d20`
- `00034e9c: lsls r1,r1,#0x9` in `FUN_00034d20` @ `00034d20`
- `00034ea8: lsls r1,r1,#0x9` in `FUN_00034d20` @ `00034d20`
- `00034ee4: lsls r1,r1,#0x9` in `FUN_00034d20` @ `00034d20`
- `00035114: lsls r1,r1,#0x9` in `FUN_00034d20` @ `00034d20`
- `00036032: lsls r3,r3,#0x9` in `FUN_00035f68` @ `00035f68`
- `00036d0c: movs r1,#0x9` in `FUN_00036d04` @ `00036d04`
- `00038e1e: lsrs r3,r3,#0x9` in `FUN_00038de4` @ `00038de4`
- `00038e20: lsls r3,r3,#0x9` in `FUN_00038de4` @ `00038de4`
- `0003b584: lsrs r3,r3,#0x9` in `FUN_0003b550` @ `0003b550`
- `0003b588: lsls r3,r3,#0x9` in `FUN_0003b550` @ `0003b550`
- `0003cb2c: movs r2,#0x9` in `FUN_0003c994` @ `0003c994`
- `0003ce44: movs r2,#0x9` in `FUN_0003c994` @ `0003c994`
- `0003f7a0: ldrb r3,[r4,#0x9]` in `FUN_0003f77c` @ `0003f77c`
- `0004063e: movs r2,#0x9` in `FUN_00040554` @ `00040554`
- `00041446: asrs r1,r1,#0x9` in `FUN_00041388` @ `00041388`
- `000415b0: asrs r5,r5,#0x9` in `FUN_00041388` @ `00041388`
- ... truncated after 80 hits

### `0x8`

- `00000598: ldr r2,[r2,#0x8]` in `FUN_000004e4` @ `000004e4`
- `0000059e: str r2,[r3,#0x8]` in `FUN_000004e4` @ `000004e4`
- `000005be: ldr r2,[r2,#0x8]` in `FUN_000004e4` @ `000004e4`
- `000005c2: str r2,[r3,#0x8]` in `FUN_000004e4` @ `000004e4`
- `00000616: ldrh r3,[r0,#0x8]` in `FUN_000005fc` @ `000005fc`
- `0000064e: strh r1,[r3,#0x8]` in `FUN_000005fc` @ `000005fc`
- `00000822: strb r0,[r4,#0x8]` in `FUN_0000079c` @ `0000079c`
- `000008c8: strh r3,[r0,#0x8]` in `FUN_00000880` @ `00000880`
- `0000090a: ldr r1,[r2,#0x8]` in `FUN_000008d8` @ `000008d8`
- `0000091a: strh r1,[r0,#0x8]` in `FUN_000008d8` @ `000008d8`
- `0000096c: strh r2,[r3,#0x8]` in `FUN_00000950` @ `00000950`
- `00000976: ldrh r2,[r0,#0x8]` in `FUN_00000950` @ `00000950`
- `00000b5e: strh r3,[r2,#0x8]` in `FUN_00000b30` @ `00000b30`
- `00000bfc: sub sp,#0x8` in `FUN_00000bf0` @ `00000bf0`
- `00000c52: add sp,#0x8` in `FUN_00000bf0` @ `00000bf0`
- `00000c5a: movs r3,#0x8` in `FUN_00000bf0` @ `00000bf0`
- `00000cda: movs r3,#0x8` in `FUN_00000c8c` @ `00000c8c`
- `00000d10: movs r2,#0x8` in `FUN_00000cfc` @ `00000cfc`
- `00000d32: ldr r2,[r4,#0x8]` in `FUN_00000d28` @ `00000d28`
- `00000d58: ldr r2,[r0,#0x8]` in `FUN_00000d54` @ `00000d54`
- `00000d6e: sub sp,#0x8` in `FUN_00000d6c` @ `00000d6c`
- `00000d72: ldr r3,[r0,#0x8]` in `FUN_00000d6c` @ `00000d6c`
- `00000d90: add sp,#0x8` in `FUN_00000d6c` @ `00000d6c`
- `00000d96: sub sp,#0x8` in `FUN_00000d94` @ `00000d94`
- `00000da2: ldr r2,[r0,#0x8]` in `FUN_00000d94` @ `00000d94`
- `00000dba: add sp,#0x8` in `FUN_00000d94` @ `00000d94`
- `00000dc8: ldr r5,[r0,#0x8]` in `FUN_00000dc0` @ `00000dc0`
- `00000dec: ldr r5,[r3,#0x8]` in `FUN_00000dc0` @ `00000dc0`
- `00000e5e: sub sp,#0x8` in `FUN_00000e5c` @ `00000e5c`
- `0000123e: adds r2,#0x8` in `<none>` @ `<none>`
- `0000125a: ldrb r2,[r4,#0x8]` in `<none>` @ `<none>`
- `000014da: cmp r3,#0x8` in `FUN_0000140c` @ `0000140c`
- `000015f0: ldrb r0,[r3,#0x8]` in `FUN_0000140c` @ `0000140c`
- `000016c6: asrs r1,r1,#0x8` in `FUN_00001618` @ `00001618`
- `000016ea: asrs r1,r1,#0x8` in `FUN_00001618` @ `00001618`
- `000016fe: movs r3,#0x8` in `FUN_000016f4` @ `000016f4`
- `000017a6: str r3,[r0,#0x8]` in `FUN_000017a0` @ `000017a0`
- `000017ba: ldr r2,[r3,#0x8]` in `FUN_000017ac` @ `000017ac`
- `000017c6: str r0,[r3,#0x8]` in `FUN_000017ac` @ `000017ac`
- `000017c8: str r2,[r0,#0x8]` in `FUN_000017ac` @ `000017ac`
- `000017ce: str r3,[r0,#0x8]` in `FUN_000017ac` @ `000017ac`
- `000017e6: ldr r4,[r4,#0x8]` in `FUN_000017d4` @ `000017d4`
- `0000186e: ldr r1,[r3,#0x8]` in `FUN_00001834` @ `00001834`
- `00001890: str r3,[r4,#0x8]` in `FUN_00001834` @ `00001834`
- `00001894: str r4,[r3,#0x8]` in `FUN_00001834` @ `00001834`
- `00001896: str r1,[r4,#0x8]` in `FUN_00001834` @ `00001834`
- `000019ca: ldr r1,[sp,#0x8]` in `FUN_0000190c` @ `0000190c`
- `000019ce: str r1,[sp,#0x8]` in `FUN_0000190c` @ `0000190c`
- `00001a16: cmp r3,#0x8` in `FUN_0000190c` @ `0000190c`
- `00001a4e: ldr r2,[sp,#0x8]` in `FUN_0000190c` @ `0000190c`
- `00001a52: str r2,[r7,#0x8]` in `FUN_0000190c` @ `0000190c`
- `00001a86: cmp r3,#0x8` in `FUN_0000190c` @ `0000190c`
- `00001bec: ldrh r0,[r1,#0x8]` in `FUN_00001b44` @ `00001b44`
- `00001c4c: cmp r2,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001d50: ldrh r0,[r1,#0x8]` in `FUN_00001b44` @ `00001b44`
- `00001dda: cmp r2,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001e44: asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001e5c: asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001e74: asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001e8c: asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001ea4: asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001ebc: asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001ed2: asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001eea: asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001ef6: cmp r2,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001f02: asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `00001f1a: asrs r1,r1,#0x8` in `FUN_00001b44` @ `00001b44`
- `0000206c: movs r0,#0x8` in `FUN_00001b44` @ `00001b44`
- `000021ee: str r3,[sp,#0x8]` in `FUN_00002120` @ `00002120`
- `000021f4: ldr r2,[r4,#0x8]` in `FUN_00002120` @ `00002120`
- `000021fa: str r2,[r4,#0x8]` in `FUN_00002120` @ `00002120`
- `0000223e: ldr r3,[sp,#0x8]` in `FUN_00002120` @ `00002120`
- `00002260: ldr r3,[r4,#0x8]` in `FUN_00002120` @ `00002120`
- `0000226e: str r3,[r4,#0x8]` in `FUN_00002120` @ `00002120`
- `000024e8: strb r0,[r3,#0x8]` in `FUN_000024e0` @ `000024e0`
- `000027ca: str r3,[sp,#0x8]` in `FUN_00002544` @ `00002544`
- `000027fc: ldr r3,[sp,#0x8]` in `FUN_00002544` @ `00002544`
- `0000294c: ldrb r3,[r3,#0x8]` in `FUN_00002918` @ `00002918`
- `00002b32: ldrb r3,[r0,#0x8]` in `FUN_00002af0` @ `00002af0`
- `00002b6a: strh r7,[r1,#0x8]` in `FUN_00002af0` @ `00002af0`
- ... truncated after 80 hits

## Decompiled Function Scan

Functions whose decompiled C mentions the config key or mode/effect globals.

### `FUN_00000e50` @ `00000e50`

```c

undefined1 FUN_00000e50(void)

{
  return DAT_20004291;
}
```

### `FUN_00000e5c` @ `00000e5c`

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

### `FUN_00002ab8` @ `00002ab8`

```c

undefined4 FUN_00002ab8(void)

{
  return 0x200040a0;
}
```

