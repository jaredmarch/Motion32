# Motion 32 Mode Getter Callers Dump

## `FUN_00001bf0` @ `00001bf0`

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

## `FUN_00002030` @ `00002030`

```c

void FUN_00002030(char *param_1,uint param_2,undefined4 param_3,undefined4 param_4)

{
  undefined1 uVar1;
  int iVar2;
  undefined4 extraout_r2;
  undefined4 extraout_r2_00;
  undefined4 uVar3;
  undefined1 *puVar4;
  uint uVar5;
  undefined1 *puVar6;
  
  iVar2 = FUN_00001e50();
  if (iVar2 == 0) {
    puVar4 = (undefined1 *)0x95f4;
  }
  else {
    puVar4 = (undefined1 *)0x95f8;
  }
  puVar6 = puVar4 + 4;
  do {
    uVar1 = *puVar4;
    puVar4 = puVar4 + 1;
    FUN_00001d6c(0x20004084,uVar1);
  } while (puVar4 != puVar6);
  if (param_2 != 0) {
    uVar5 = 0;
    uVar3 = extraout_r2;
    do {
      if (-1 < *param_1) {
        FUN_00001d6c(0x20004084,*param_1,uVar3,(int)*param_1,param_4);
        uVar3 = extraout_r2_00;
      }
      uVar5 = uVar5 + 1 & 0xff;
      param_1 = param_1 + 1;
    } while (param_2 != uVar5);
  }
  FUN_00001d6c(0x20004084,0xf7);
  return;
}
```

## `FUN_000020a4` @ `000020a4`

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

## `FUN_0000234c` @ `0000234c`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0000234c(ushort param_1)

{
  ushort uVar1;
  int iVar2;
  uint uVar3;
  
  uVar1 = _DAT_20004532;
  if ((_DAT_20004532 != param_1) && (uVar1 = param_1, DAT_200045cb != 0)) {
    uVar3 = 0;
    do {
      iVar2 = FUN_00001e50();
      if (*(char *)(iVar2 * 0xb + 0x9620 + uVar3) != '\0') {
        iVar2 = FUN_00001e50();
        uVar1 = *(ushort *)((iVar2 * 0xb + uVar3) * 2 + 0x9638);
        if ((uVar1 & param_1) == 0) {
          if ((_DAT_20004532 & uVar1) != 0) {
            FUN_00001f6c(uVar3 & 0xff,0);
          }
        }
        else if ((_DAT_20004532 & uVar1) == 0) {
          FUN_00001f6c(uVar3 & 0xff,2);
          if (uVar3 == 9) {
            DAT_200045c8 = 1;
          }
          else if (uVar3 == 10) {
            DAT_200045c9 = 1;
          }
        }
      }
      uVar3 = uVar3 + 1;
      uVar1 = param_1;
    } while ((uVar3 & 0xff) < (uint)DAT_200045cb);
  }
  _DAT_20004532 = uVar1;
  return;
}
```

## `FUN_0000240c` @ `0000240c`

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

## `FUN_000026f4` @ `000026f4`

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

## `FUN_000028d0` @ `000028d0`

```c

undefined4 FUN_000028d0(void)

{
  int iVar1;
  
  FUN_0000a568(&DAT_20004600,0,0x2c);
  iVar1 = FUN_00001e50();
  DAT_2000462a = (char)iVar1;
  DAT_20004628 = (-('\x01' - (iVar1 == 0)) & 0xfbU) + 10;
  DAT_2000462b = 1;
  DAT_20004629 = 0;
  return 0;
}
```

## `FUN_00002b08` @ `00002b08`

```c

undefined4 FUN_00002b08(void)

{
  int iVar1;
  
  FUN_0000a568(0x2000462c,0,&DAT_00001430);
  iVar1 = FUN_00001e50();
  DAT_20005a56 = (-('\x01' - (iVar1 == 0)) & 0xfbU) + 10;
  DAT_20005a58 = 1;
  return 0;
}
```

## `FUN_000030cc` @ `000030cc`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_000030cc(void)

{
  int iVar1;
  
  FUN_0000a568(&DAT_20005a64,0,0x38);
  iVar1 = FUN_00001e50();
  if (iVar1 == 0) {
    _DAT_20005a5e = 0x10;
    DAT_20005a61 = 2;
    DAT_20005a60 = 4;
  }
  else {
    _DAT_20005a5e = 0x20;
    DAT_20005a60 = 5;
    DAT_20005a61 = 1;
  }
  DAT_20005a5c = 1;
  return 0;
}
```

## `FUN_00003370` @ `00003370`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_00003370(void)

{
  int iVar1;
  
  iVar1 = FUN_00001e50();
  FUN_0000a568(&DAT_20005b40,0,0x18);
  FUN_0000a568(0x20005aac,0,0x94);
  _DAT_20005a9c = 0;
  if (iVar1 == 1) {
    _DAT_20005b40 = 0x44600080;
    DAT_20005b44 = 0x83;
    DAT_20005b4a = 5;
    DAT_20005b50 = 0x83;
    _DAT_20005b4c = 0x44600080;
    _DAT_20005aa0 = DAT_00009694;
    _DAT_20005aa4 = DAT_00009698;
    _DAT_20005aa8 = DAT_0000969c;
  }
  else {
    _DAT_20005b40 = DAT_000096a0;
    DAT_20005b44 = DAT_000096a4;
    DAT_20005b4a = 5;
    FUN_0000a578(&DAT_20005b4c,&DAT_000096a5,5);
    _DAT_20005aa0 = DAT_00009688;
    _DAT_20005aa4 = SUB_0000968c;
    _DAT_20005aa8 = DAT_00009690;
  }
  DAT_20005b56 = 5;
  DAT_20005a9e = 1;
  return 0;
}
```

## `FUN_000098c4` @ `000098c4`

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

## `FUN_000098e4` @ `000098e4`

```c

undefined4 FUN_000098e4(void)

{
  int iVar1;
  undefined4 uVar2;
  
  iVar1 = FUN_00001e50();
  if (iVar1 == 1) {
    uVar2 = 0x9d80;
  }
  else {
    uVar2 = 0x9d40;
  }
  return uVar2;
}
```

## `FUN_00009904` @ `00009904`

```c

undefined4 FUN_00009904(void)

{
  int iVar1;
  undefined4 uVar2;
  
  iVar1 = FUN_00001e50();
  if (iVar1 == 1) {
    uVar2 = 0x9cd4;
  }
  else {
    uVar2 = 0x9cc4;
  }
  return uVar2;
}
```

## `FUN_00009924` @ `00009924`

```c

undefined4 FUN_00009924(void)

{
  int iVar1;
  undefined4 uVar2;
  
  iVar1 = FUN_00001e50();
  if (iVar1 == 1) {
    uVar2 = 0x9cc0;
  }
  else {
    uVar2 = 0x9cbc;
  }
  return uVar2;
}
```

## `FUN_00009944` @ `00009944`

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
  iVar2 = FUN_000048e8(0xf240bb40);
  if (iVar2 == 0) {
    do {
    } while (DAT_20006465 == '\0');
    DAT_20006465 = 0;
    FUN_00004ce8(0xf240bb40,&DAT_200064d8,0);
    if (DAT_200064bc != '\0') {
      _DAT_200064d8 = _DAT_200064d8 | 0x200;
    }
    if (DAT_200064bd != '\0') {
      _DAT_200064d8 = _DAT_200064d8 | 0x400;
    }
    FUN_0000234c();
    FUN_0000240c();
    FUN_00002618(&DAT_200064c0);
    FUN_00002288(&DAT_200064c0);
    iVar2 = FUN_00003fec();
    if (((iVar2 != 0) && (iVar2 = FUN_00001880(auStack_d4), iVar2 == 0)) &&
       (iVar2 = FUN_000018d8(auStack_c4), iVar2 == 0)) {
      iVar2 = FUN_000034ec();
      if (iVar2 != 0) {
        FUN_0000a578(&local_e0,iVar2,10);
      }
      bVar1 = false;
      iVar2 = FUN_00003508(0,auStack_b0);
      puVar3 = auStack_b0;
      while( true ) {
        if (iVar2 != 0) {
          *(undefined1 *)((int)puVar3 + 10) = 5;
          *(undefined1 *)((int)puVar3 + 0xb) = 0;
          *puVar3 = 0x80808080;
          puVar3[1] = 0x80808080;
          *(short *)(puVar3 + 2) = (short)DAT_00009e18;
        }
        puVar3 = puVar3 + 3;
        if (bVar1) break;
        bVar1 = true;
        iVar2 = FUN_00003508(1,puVar3);
      }
      iVar2 = FUN_000041fc(auStack_d4,auStack_c4,&local_e0,auStack_b0,auStack_98,0x80);
      if (iVar2 != 0) {
        FUN_00002030(auStack_98,iVar2);
      }
    }
    iVar2 = FUN_00003fd8();
    if (iVar2 != 0) {
      FUN_00001b30();
    }
    iVar2 = FUN_000045b0();
    if (iVar2 != 0) {
      iVar2 = FUN_000045c0(auStack_d4,auStack_c4,&local_e0,auStack_b0);
      if (((iVar2 == 0) && (iVar2 = FUN_000015fc(auStack_d4), iVar2 == 0)) &&
         (iVar2 = FUN_00001950(auStack_c4), iVar2 == 0)) {
        FUN_000034a8(local_e0);
        FUN_000034b4(local_df);
        FUN_000034d4(local_de);
        FUN_000034c4(local_dc,local_da);
        FUN_000034e0(local_d8);
        if (local_a5 != '\0') {
          FUN_00003428(0,auStack_b0,local_a6);
        }
        if (local_99 != '\0') {
          FUN_00003428(1,local_a4,local_9a);
        }
        iVar2 = FUN_00001b30();
        if (((iVar2 == 0) && (iVar2 = FUN_000016b8(), iVar2 == 0)) &&
           (iVar2 = FUN_00002ae8(), iVar2 == 0)) {
          FUN_00003090();
          FUN_00003350();
        }
      }
    }
    iVar2 = FUN_00004000();
    if (((iVar2 != 0) && (iVar2 = FUN_00001cfc(auStack_b0), iVar2 == 0)) &&
       (iVar2 = FUN_0000455c(auStack_b0,auStack_98,0x80), iVar2 != 0)) {
      FUN_00002030(auStack_98,iVar2);
    }
    iVar2 = FUN_00004014();
    if (iVar2 != 0) {
      FUN_00004028();
      FUN_00001c8c();
    }
    return;
  }
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

## `FUN_00009e1c` @ `00009e1c`

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

