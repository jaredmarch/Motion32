# Motion 32 Event Stream Consumer Probe

Focus: queue `0x20004084` and opcodes `0x14`, `0x15`, `0x16`, `0x36`.

## Focus Functions

### `00001d28` `FUN_00001b44`

Callers/references:
- none

Instructions near `00001d28`:

```asm
00001d08: ldr r6,[r4,r6]
00001d0a: subs r6,r6,r7
00001d0c: adds r0,r0,r6
00001d0e: str r0,[r4,r5]
00001d10: cmp r2,#0x3
00001d12: bne 0x00001d16
00001d14: b 0x00001e22
00001d16: movw r5,#0x300
00001d1a: adds r5,r3,r5
00001d1c: lsls r5,r5,#0x1
00001d1e: ldrsh r6,[r5,r4]
00001d20: movw r8,#0x140c
00001d24: mov r12,r6
00001d26: mov r6,r8
00001d28: ldrh r0,[r1,#0x6]
00001d2a: mov r7,r12
00001d2c: sxth r0,r0
00001d2e: strh r0,[r5,r4]
00001d30: mov r5,r8
00001d32: ldr r6,[r4,r6]
00001d34: subs r6,r6,r7
00001d36: adds r0,r0,r6
00001d38: str r0,[r4,r5]
00001d3a: cmp r2,#0x4
00001d3c: beq 0x00001e22
00001d3e: movw r5,#0x400
00001d42: adds r5,r3,r5
00001d44: lsls r5,r5,#0x1
00001d46: ldrsh r6,[r5,r4]
```

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
/* ... truncated ... */
```

### `00001d54` `FUN_00001b44`

Callers/references:
- none

Instructions near `00001d54`:

```asm
00001d34: subs r6,r6,r7
00001d36: adds r0,r0,r6
00001d38: str r0,[r4,r5]
00001d3a: cmp r2,#0x4
00001d3c: beq 0x00001e22
00001d3e: movw r5,#0x400
00001d42: adds r5,r3,r5
00001d44: lsls r5,r5,#0x1
00001d46: ldrsh r6,[r5,r4]
00001d48: movw r8,#0x1410
00001d4c: mov r12,r6
00001d4e: mov r6,r8
00001d50: ldrh r0,[r1,#0x8]
00001d52: mov r7,r12
00001d54: sxth r0,r0
00001d56: strh r0,[r5,r4]
00001d58: mov r5,r8
00001d5a: ldr r6,[r4,r6]
00001d5c: subs r6,r6,r7
00001d5e: adds r0,r0,r6
00001d60: str r0,[r4,r5]
00001d62: cmp r2,#0x5
00001d64: beq 0x00001e22
00001d66: movw r5,#0x500
00001d6a: adds r5,r3,r5
00001d6c: lsls r5,r5,#0x1
00001d6e: ldrsh r6,[r5,r4]
00001d70: movw r8,#0x1414
00001d74: mov r12,r6
```

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
/* ... truncated ... */
```

### `00001d6c` `FUN_00001b44`

Callers/references:
- none

Instructions near `00001d6c`:

```asm
00001d4e: mov r6,r8
00001d50: ldrh r0,[r1,#0x8]
00001d52: mov r7,r12
00001d54: sxth r0,r0
00001d56: strh r0,[r5,r4]
00001d58: mov r5,r8
00001d5a: ldr r6,[r4,r6]
00001d5c: subs r6,r6,r7
00001d5e: adds r0,r0,r6
00001d60: str r0,[r4,r5]
00001d62: cmp r2,#0x5
00001d64: beq 0x00001e22
00001d66: movw r5,#0x500
00001d6a: adds r5,r3,r5
00001d6c: lsls r5,r5,#0x1
00001d6e: ldrsh r6,[r5,r4]
00001d70: movw r8,#0x1414
00001d74: mov r12,r6
00001d76: mov r6,r8
00001d78: ldrh r0,[r1,#0xa]
00001d7a: mov r7,r12
00001d7c: sxth r0,r0
00001d7e: strh r0,[r5,r4]
00001d80: mov r5,r8
00001d82: ldr r6,[r4,r6]
00001d84: subs r6,r6,r7
00001d86: adds r0,r0,r6
00001d88: str r0,[r4,r5]
00001d8a: cmp r2,#0x6
```

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
/* ... truncated ... */
```

### `00001d94` `FUN_00001b44`

Callers/references:
- none

Instructions near `00001d94`:

```asm
00001d76: mov r6,r8
00001d78: ldrh r0,[r1,#0xa]
00001d7a: mov r7,r12
00001d7c: sxth r0,r0
00001d7e: strh r0,[r5,r4]
00001d80: mov r5,r8
00001d82: ldr r6,[r4,r6]
00001d84: subs r6,r6,r7
00001d86: adds r0,r0,r6
00001d88: str r0,[r4,r5]
00001d8a: cmp r2,#0x6
00001d8c: beq 0x00001e22
00001d8e: movw r5,#0x600
00001d92: adds r5,r3,r5
00001d94: lsls r5,r5,#0x1
00001d96: ldrsh r6,[r5,r4]
00001d98: movw r8,#0x1418
00001d9c: mov r12,r6
00001d9e: mov r6,r8
00001da0: ldrh r0,[r1,#0xc]
00001da2: mov r7,r12
00001da4: sxth r0,r0
00001da6: strh r0,[r5,r4]
00001da8: mov r5,r8
00001daa: ldr r6,[r4,r6]
00001dac: subs r6,r6,r7
00001dae: adds r0,r0,r6
00001db0: str r0,[r4,r5]
00001db2: cmp r2,#0x7
```

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
/* ... truncated ... */
```

### `00001dc0` `FUN_00001b44`

Callers/references:
- none

Instructions near `00001dc0`:

```asm
00001da2: mov r7,r12
00001da4: sxth r0,r0
00001da6: strh r0,[r5,r4]
00001da8: mov r5,r8
00001daa: ldr r6,[r4,r6]
00001dac: subs r6,r6,r7
00001dae: adds r0,r0,r6
00001db0: str r0,[r4,r5]
00001db2: cmp r2,#0x7
00001db4: beq 0x00001e22
00001db6: movw r5,#0x700
00001dba: adds r5,r3,r5
00001dbc: lsls r5,r5,#0x1
00001dbe: ldrsh r6,[r4,r5]
00001dc0: movw r8,#0x141c
00001dc4: mov r12,r6
00001dc6: mov r6,r8
00001dc8: ldrh r0,[r1,#0xe]
00001dca: mov r7,r12
00001dcc: sxth r0,r0
00001dce: strh r0,[r4,r5]
00001dd0: mov r5,r8
00001dd2: ldr r6,[r4,r6]
00001dd4: subs r6,r6,r7
00001dd6: adds r0,r0,r6
00001dd8: str r0,[r4,r5]
00001dda: cmp r2,#0x8
00001ddc: beq 0x00001e22
00001dde: movw r5,#0x800
```

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
/* ... truncated ... */
```

### `00001eec` `FUN_00001b44`

Callers/references:
- none

Instructions near `00001eec`:

```asm
00001ecc: movw r5,#0x1418
00001ed0: ldr r1,[r4,r5]
00001ed2: asrs r1,r1,#0x8
00001ed4: sxth r1,r1
00001ed6: movs r3,r1
00001ed8: adds r3,#0x1e
00001eda: bge 0x00001ede
00001edc: b 0x00002028
00001ede: cmp r2,#0x7
00001ee0: bhi 0x00001ee4
00001ee2: b 0x00001c92
00001ee4: movw r5,#0x141c
00001ee8: ldr r1,[r4,r5]
00001eea: asrs r1,r1,#0x8
00001eec: sxth r1,r1
00001eee: movs r3,r1
00001ef0: adds r3,#0x1e
00001ef2: bge 0x00001ef6
00001ef4: b 0x0000204a
00001ef6: cmp r2,#0x8
00001ef8: bhi 0x00001efc
00001efa: b 0x00001c92
00001efc: movw r5,#0x1420
00001f00: ldr r1,[r4,r5]
00001f02: asrs r1,r1,#0x8
00001f04: sxth r1,r1
00001f06: movs r3,r1
00001f08: adds r3,#0x1e
00001f0a: bge 0x00001f0e
```

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
/* ... truncated ... */
```

### `00001f6c` `FUN_00001b44`

Callers/references:
- none

Instructions near `00001f6c`:

```asm
00001f46: cmp r3,#0xff
00001f48: bls 0x00001f9c
00001f4a: movw r3,#0x142b
00001f4e: strh r2,[r4,r1]
00001f50: movs r2,#0x1
00001f52: strb r2,[r4,r3]
00001f54: b 0x00001c92
00001f56: movs r0,#0x0
00001f58: bl 0x00001ac8
00001f5c: movw r0,#0x462c
00001f60: movw r2,#0x200
00001f64: movs r1,#0x0
00001f66: movt r0,#0x2000
00001f6a: bl 0x00009568
00001f6e: movs r3,#0x0
00001f70: str r3,[r4,r5]
00001f72: movw r3,#0x142a
00001f76: ldrb r2,[r4,r3]
00001f78: b 0x00001e50
00001f7a: movs r0,#0x1
00001f7c: bl 0x00001ac8
00001f80: movw r3,#0x200
00001f84: movw r2,#0x200
00001f88: adds r0,r4,r3
00001f8a: movs r1,#0x0
00001f8c: bl 0x00009568
00001f90: movs r3,#0x0
00001f92: str r3,[r4,r5]
00001f94: movw r3,#0x142a
```

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
/* ... truncated ... */
```

### `00001fb0` `FUN_00001b44`

Callers/references:
- none

Instructions near `00001fb0`:

```asm
00001f8a: movs r1,#0x0
00001f8c: bl 0x00009568
00001f90: movs r3,#0x0
00001f92: str r3,[r4,r5]
00001f94: movw r3,#0x142a
00001f98: ldrb r2,[r4,r3]
00001f9a: b 0x00001e68
00001f9c: strh r3,[r4,r1]
00001f9e: b 0x00001c92
00001fa0: movs r0,#0x5
00001fa2: bl 0x00001ac8
00001fa6: movw r3,#0xa00
00001faa: movw r2,#0x200
00001fae: adds r0,r4,r3
00001fb0: movs r1,#0x0
00001fb2: bl 0x00009568
00001fb6: movs r3,#0x0
00001fb8: str r3,[r4,r5]
00001fba: movw r3,#0x142a
00001fbe: ldrb r2,[r4,r3]
00001fc0: b 0x00001ec6
00001fc2: movs r0,#0x2
00001fc4: bl 0x00001ac8
00001fc8: movw r3,#0x400
00001fcc: movw r2,#0x200
00001fd0: adds r0,r4,r3
00001fd2: movs r1,#0x0
00001fd4: bl 0x00009568
00001fd8: movs r3,#0x0
```

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
/* ... truncated ... */
```

### `00002030` `FUN_00001b44`

Callers/references:
- none

Instructions near `00002030`:

```asm
00002008: bl 0x00001ac8
0000200c: movw r3,#0x800
00002010: movw r2,#0x200
00002014: adds r0,r4,r3
00002016: movs r1,#0x0
00002018: bl 0x00009568
0000201c: movs r3,#0x0
0000201e: str r3,[r4,r5]
00002020: movw r3,#0x142a
00002024: ldrb r2,[r4,r3]
00002026: b 0x00001eb0
00002028: movs r0,#0x6
0000202a: bl 0x00001ac8
0000202e: movw r3,#0xc00
00002032: movw r2,#0x200
00002036: adds r0,r4,r3
00002038: movs r1,#0x0
0000203a: bl 0x00009568
0000203e: movs r3,#0x0
00002040: str r3,[r4,r5]
00002042: movw r3,#0x142a
00002046: ldrb r2,[r4,r3]
00002048: b 0x00001ede
0000204a: movs r0,#0x7
0000204c: bl 0x00001ac8
00002050: movw r3,#0xe00
00002054: movw r2,#0x200
00002058: adds r0,r4,r3
0000205a: movs r1,#0x0
```

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
/* ... truncated ... */
```

### `000020a4` `FUN_00002090`

Callers/references:
- none

Instructions near `000020a4`:

```asm
0000207c: movs r1,#0x0
0000207e: bl 0x00009568
00002082: movs r3,#0x0
00002084: str r3,[r4,r5]
00002086: movw r3,#0x142a
0000208a: ldrb r2,[r4,r3]
0000208c: b 0x00001f0e
00002090: push {r4,lr}
00002092: movw r4,#0x462c
00002096: movw r3,#0x142c
0000209a: movt r4,#0x2000
0000209e: ldrb r3,[r4,r3]
000020a0: cbz r3,0x000020c8
000020a2: movw r2,#0x1400
000020a6: movs r1,#0x0
000020a8: movs r0,r4
000020aa: bl 0x00009568
000020ae: movw r3,#0x1400
000020b2: movs r2,#0x28
000020b4: adds r0,r4,r3
000020b6: movs r1,#0x0
000020b8: bl 0x00009568
000020bc: movw r3,#0x1428
000020c0: movs r2,#0x0
000020c2: strh r2,[r4,r3]
000020c4: adds r3,#0x3
000020c6: strb r2,[r4,r3]
000020c8: pop {r4,pc}
000020cc: movw r0,#0x5a64
```

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

### `00002288` `FUN_00002120`

Callers/references:
- none

Instructions near `00002288`:

```asm
0000226c: movs r3,#0x0
0000226e: str r3,[r4,#0x8]
00002270: ldr r3,[r4,#0xc]
00002272: asrs r3,r2
00002274: cmp r3,#0x14
00002276: bgt 0x000022ce
00002278: adds r3,#0x14
0000227a: blt 0x0000231a
0000227c: movs r3,#0x0
0000227e: str r3,[r4,#0xc]
00002280: ldr r3,[r4,#0x10]
00002282: asrs r3,r2
00002284: cmp r3,#0x14
00002286: bgt 0x000022c2
00002288: adds r3,#0x14
0000228a: blt 0x0000230c
0000228c: movs r3,#0x0
0000228e: str r3,[r4,#0x10]
00002290: strh r3,[r4,#0x14]
00002292: mov r3,r11
00002294: ldrb r3,[r3,#0x0]
00002296: adds r5,#0x1
00002298: mov r8,r3
0000229a: uxtb r3,r5
0000229c: adds r4,#0x1c
0000229e: adds r6,#0x5
000022a0: cmp r3,r8
000022a2: bcs 0x000022a6
000022a4: b 0x000021b0
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

### `0000234c` `FUN_00002120`

Callers/references:
- none

Instructions near `0000234c`:

```asm
0000232c: mov r3,sp
0000232e: movs r1,#0x5
00002330: ldrb r0,[r3,#0xc]
00002332: rsbs r1,r1
00002334: bl 0x00001ac8
00002338: mov r3,r8
0000233a: ldrb r2,[r3,#0x0]
0000233c: b 0x0000226c
0000233e: movs r1,#0x5
00002340: uxtb r0,r6
00002342: rsbs r1,r1
00002344: bl 0x00001ac8
00002348: mov r3,r8
0000234a: ldrb r2,[r3,#0x0]
0000234c: b 0x0000225c
00002350: movw r3,#0x5a5c
00002354: movt r3,#0x2000
00002358: ldrb r3,[r3,#0x0]
0000235a: push {r4,lr}
0000235c: cbz r3,0x0000236e
0000235e: movw r0,#0x5a64
00002362: movs r2,#0x38
00002364: movs r1,#0x0
00002366: movt r0,#0x2000
0000236a: bl 0x00009568
0000236e: pop {r4,pc}
00002370: push {r4,r5,r6,lr}
00002372: movw r4,#0x5b40
00002376: bl 0x00000e50
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

### `0000240c` `FUN_00002370`

Callers/references:
- none

Instructions near `0000240c`:

```asm
000023ea: pop {r4,r5,r6,pc}
000023ec: movw r1,#0x96a0
000023f0: movs r0,r4
000023f2: movs r5,#0x5
000023f4: movt r1,#0x0
000023f8: ldr r3,[r1,#0x0]
000023fa: movs r2,#0x5
000023fc: str r3,[r4,#0x0]
000023fe: ldrb r3,[r1,#0x4]
00002400: adds r0,#0xc
00002402: strb r3,[r4,#0x4]
00002404: adds r1,#0x5
00002406: strb r5,[r4,#0xa]
00002408: bl 0x00009578
0000240c: movw r2,#0x5aa0
00002410: movw r3,#0x9688
00002414: strb r5,[r4,#0x16]
00002416: movt r2,#0x2000
0000241a: movt r3,#0x0
0000241e: ldmia r3!,{r0,r4}
00002420: stmia r2!,{r0,r4}
00002422: ldrh r3,[r3,#0x0]
00002424: strh r3,[r2,#0x0]
00002426: b 0x000023dc
00002428: movw r3,#0x5a9e
0000242c: movt r3,#0x2000
00002430: ldrb r3,[r3,#0x0]
00002432: push {r4,r5,r6,lr}
00002434: movs r4,r0
```

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

### `00002618` `FUN_00002544`

Callers/references:
- none

Instructions near `00002618`:

```asm
000025f8: mov r3,r9
000025fa: ldrb r3,[r3,#0x0]
000025fc: mov r5,r11
000025fe: cmp r3,#0x0
00002600: beq 0x00002604
00002602: b 0x000027a8
00002604: movw r3,#0x5aac
00002608: mov r0,r8
0000260a: movt r3,#0x2000
0000260e: mov r12,r3
00002610: adds r0,#0x28
00002612: mov r2,r10
00002614: movs r1,r6
00002616: add r0,r12
00002618: bl 0x00009578
0000261c: mov r3,r9
0000261e: ldrb r3,[r3,#0x2]
00002620: cmp r3,#0x0
00002622: bne 0x000026f8
00002624: movw r2,#0x5aac
00002628: movs r3,#0x4a
0000262a: movt r2,#0x2000
0000262e: mov r12,r2
00002630: movs r2,#0x0
00002632: muls r3,r7
00002634: add r3,r12
00002636: adds r3,#0x3c
00002638: strb r2,[r3,#0x0]
0000263a: movs r3,#0x0
```

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

### `00009944` `PROBE_000098c8`

Callers/references:
- none

Instructions near `00009944`:

```asm
00009928: movs r4,r1
0000992a: movs r0,r0
0000992c: movs r0,r0
0000992e: lsrs r1,r0,#0x10
00009930: movs r5,r1
00009932: movs r0,r0
00009934: movs r4,r0
00009936: movs r0,r0
00009938: movs r6,r1
0000993a: movs r0,r0
0000993c: movs r0,r0
0000993e: lsrs r1,r0,#0x10
00009940: movs r7,r1
00009942: movs r0,r0
00009944: movs r0,r0
00009946: lsrs r1,r0,#0x10
00009948: lsls r0,r0,#0x4
0000994a: movs r0,r0
0000994c: movs r0,r0
0000994e: lsrs r1,r0,#0x10
00009950: lsls r1,r0,#0x4
00009952: movs r0,r0
00009954: movs r0,r0
00009956: lsrs r1,r0,#0x10
00009958: lsls r2,r0,#0x4
0000995a: movs r0,r0
0000995c: movs r0,r0
0000995e: lsrs r1,r0,#0x10
00009960: lsls r3,r0,#0x4
```

```c

/* WARNING: Control flow encountered bad instruction data */

void PROBE_000098c8(void)

{
  software_interrupt(0xff);
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}
```

### `00009e1c` `<none>`

Callers/references:
- none

Instructions near `00009e1c`:

```asm
00009a48: lsls r3,r1,#0x10
00009a4a: movs r0,r0
00009a4c: movs r0,r0
00009a4e: movs r0,r0
00009a50: lsrs r5,r1,#0x4
00009a52: movs r0,r0
00009a54: movs r0,r0
00009a56: movs r0,r0
00009a58: lsrs r6,r1,#0x4
00009a5a: movs r0,r0
00009a5c: movs r0,r0
00009a5e: movs r0,r0
00009a60: lsrs r7,r1,#0x4
00009a62: movs r0,r0
000200ea: ldr r1,[0x00020168]
000200ec: str r0,[r1,#0x0]
000200ee: ldmia r0!,{r1,r2}
000200f0: msr msp,r1
000200f4: bx r2
000200fe: ldr r0,[0x00020164]
00020100: b 0x000200ea
00020200: push {r3,r4,r5,r6,r7,lr}
00020202: ldr r3,[0x00020258]
00020204: movs r7,r0
00020206: ldrh r5,[r3,#0x0]
00020208: movs r6,r1
0002020a: cmp r5,#0x0
0002020c: beq 0x00020234
0002020e: ldr r4,[0x0002025c]
```

## Queue RAM References

### `20004080`

- from `00000c76` in `FUN_00000bf0` @ `00000bf0` type=WRITE
- from `00000c86` in `FUN_00000bf0` @ `00000bf0` type=WRITE
- from `00000cf4` in `FUN_00000c8c` @ `00000c8c` type=WRITE
- from `00008848` in `FUN_00008764` @ `00008764` type=PARAM

#### `FUN_00000bf0` @ `00000bf0`

Instructions near `00000c76`:

```asm
00000c5e: movs r0,r4
00000c60: movt r2,#0x4010
00000c64: bl 0x00005cb4
00000c68: cmp r0,#0x0
00000c6a: bne 0x00000c52
00000c6c: movw r3,#0x4080
00000c70: movs r2,#0x42
00000c72: movt r3,#0x2000
00000c76: strb r2,[r3,#0x0]
00000c78: b 0x00000c52
00000c7a: movs r0,#0x21
00000c7c: b 0x00000c52
00000c7e: movw r3,#0x4080
00000c82: movt r3,#0x2000
00000c86: strb r0,[r3,#0x0]
00000c88: movs r0,#0x0
00000c8a: b 0x00000c52
```

Instructions near `00000c86`:

```asm
00000c70: movs r2,#0x42
00000c72: movt r3,#0x2000
00000c76: strb r2,[r3,#0x0]
00000c78: b 0x00000c52
00000c7a: movs r0,#0x21
00000c7c: b 0x00000c52
00000c7e: movw r3,#0x4080
00000c82: movt r3,#0x2000
00000c86: strb r0,[r3,#0x0]
00000c88: movs r0,#0x0
00000c8a: b 0x00000c52
00000c8c: movw r3,#0x4290
00000c90: push {r4,r5,lr}
00000c92: movt r3,#0x2000
00000c96: ldrb r3,[r3,#0x0]
00000c98: movs r4,r0
00000c9a: sub sp,#0xc
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_00000bf0(void)

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
    FUN_00000e50();
    uVar1 = DAT_000098c0;
    local_10 = 0xdeadbeef;
    local_c = 0x420001;
    iVar2 = FUN_00005b00(DAT_000098c0,&DAT_40100400,1);
    if ((iVar2 == 0) && (iVar2 = FUN_00005cb4(uVar1,&local_10,&DAT_40100400,8), iVar2 == 0)) {
      DAT_20004080 = 0x42;
    }
  }
  return iVar2;
}
```

#### `FUN_00000c8c` @ `00000c8c`

Instructions near `00000cf4`:

```asm
00000cdc: mov r1,sp
00000cde: movs r0,r5
00000ce0: movt r2,#0x4010
00000ce4: bl 0x00005cb4
00000ce8: cmp r0,#0x0
00000cea: bne 0x00000cd2
00000cec: movw r3,#0x4080
00000cf0: movt r3,#0x2000
00000cf4: strb r4,[r3,#0x0]
00000cf6: b 0x00000cd2
00000cf8: movs r0,#0x21
00000cfa: b 0x00000cd2
00000cfc: movw r3,#0x4290
00000d00: movt r3,#0x2000
00000d04: ldrb r3,[r3,#0x0]
00000d06: push {r4,lr}
00000d08: cbz r3,0x00000d22
```

```c

int FUN_00000c8c(undefined1 param_1)

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
    iVar2 = FUN_00005b00(DAT_000098c0,&DAT_40100400,1);
    if ((iVar2 == 0) && (iVar2 = FUN_00005cb4(uVar1,&local_18,&DAT_40100400,8), iVar2 == 0)) {
      DAT_20004080 = param_1;
    }
  }
  return iVar2;
}
```

#### `FUN_00008764` @ `00008764`

Instructions near `00008848`:

```asm
0000882e: movt r0,#0x2000
00008832: strh r6,[r3,#0x4]
00008834: movs r1,#0x0
00008836: subs r2,r2,r0
00008838: bl 0x00009568
0000883c: movw r0,#0x4080
00008840: movw r2,#0x4108
00008844: movw r1,#0x9e78
00008848: movt r0,#0x2000
0000884c: movt r2,#0x2000
00008850: subs r2,r2,r0
00008852: movt r1,#0x0
00008856: bl 0x00009578
0000885a: movw r5,#0x4100
0000885e: movw r3,#0x4104
00008862: movt r5,#0x2000
00008866: movt r3,#0x2000
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00008764(void)

{
  bool bVar1;
  uint uVar2;
  code *pcVar3;
  int iVar4;
  undefined4 *puVar5;
  
  _DAT_e000ed08 = 0;
  FUN_00000ebc(0);
  FUN_00008330();
  FUN_00008708(1);
  uVar2 = 0;
  bVar1 = (bool)isCurrentModePrivileged();
  if (bVar1) {
    uVar2 = isIRQinterruptsEnabled();
  }
  bVar1 = (bool)isCurrentModePrivileged();
  if (bVar1) {
    enableIRQinterrupts(1);
  }
  bVar1 = (bool)isCurrentModePrivileged();
  if (bVar1) {
    enableIRQinterrupts((uVar2 & 1) == 1);
  }
  uVar2 = 0;
  bVar1 = (bool)isCurrentModePrivileged();
  if (bVar1) {
    uVar2 = isIRQinterruptsEnabled();
  }
  bVar1 = (bool)isCurrentModePrivileged();
  if (bVar1) {
    enableIRQinterrupts(1);
  }
  _DAT_40047004 = _DAT_40047004 & DAT_0000889c | 0x10000000;
  bVar1 = (bool)isCurrentModePrivileged();
  if (bVar1) {
    enableIRQinterrupts((uVar2 & 1) == 1);
  }
  FUN_000086b4(1,uVar2,_DAT_40047004,_DAT_40047004);
  FUN_00000ebc(1);
  _DAT_40000d00 = (undefined2)DAT_000088a0;
  _DAT_40000d08 = _MasterStackPointer + DAT_000088a4;
  _DAT_40000d0c = _MasterStackPointer;
  _DAT_40006120 = 0x1000;
  _DAT_40000d04 = 1;
  FUN_00009568(&DAT_20004120,0,0x23c0);
  FUN_00009578(&DAT_20004080,&DAT_00009e78,0x88);
  puVar5 = (undefined4 *)&DAT_20004100;
  iVar4 = 0;
  do {
    pcVar3 = (code *)*puVar5;
    puVar5 = puVar5 + 1;
    iVar4 = iVar4 + 1;
    (*pcVar3)();
  } while (iVar4 < 1);
  FUN_00008304();
  FUN_0000842c();
  FUN_00000ebc(2);
  FUN_0000868c();
  FUN_0000843c(0);
  return;
}
```

### `20004081`

- from `00000ef8` in `FUN_00000eec` @ `00000eec` type=READ
- from `00000f08` in `FUN_00000eec` @ `00000eec` type=WRITE
- from `00000f36` in `FUN_00000eec` @ `00000eec` type=READ
- from `00000f40` in `FUN_00000eec` @ `00000eec` type=WRITE
- from `00000f76` in `FUN_00000f6c` @ `00000f6c` type=READ
- from `00000f7e` in `FUN_00000f6c` @ `00000f6c` type=WRITE
- from `00000f72` in `FUN_00000f6c` @ `00000f6c` type=PARAM
- from `00000fba` in `FUN_00000fb0` @ `00000fb0` type=READ
- from `00000fc4` in `FUN_00000fb0` @ `00000fb0` type=WRITE
- from `00000fb6` in `FUN_00000fb0` @ `00000fb0` type=PARAM

#### `FUN_00000eec` @ `00000eec`

Instructions near `00000ef8`:

```asm
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
```

Instructions near `00000f08`:

```asm
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
00000f1e: movs r1,#0x16
00000f20: movt r0,#0x2000
```

Instructions near `00000f36`:

```asm
00000f1a: movw r0,#0x4084
00000f1e: movs r1,#0x16
00000f20: movt r0,#0x2000
00000f24: bl 0x00000d6c
00000f28: movw r0,#0x4084
00000f2c: movs r1,r6
00000f2e: movt r0,#0x2000
00000f32: bl 0x00000d6c
00000f36: ldrb r3,[r5,#0x0]
00000f38: cmp r3,r4
00000f3a: beq 0x00000f4e
00000f3c: movw r0,#0x4084
00000f40: strb r4,[r5,#0x0]
00000f42: subs r4,#0x50
00000f44: uxtb r1,r4
00000f46: movt r0,#0x2000
00000f4a: bl 0x00000d6c
```

Instructions near `00000f40`:

```asm
00000f28: movw r0,#0x4084
00000f2c: movs r1,r6
00000f2e: movt r0,#0x2000
00000f32: bl 0x00000d6c
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

#### `FUN_00000f6c` @ `00000f6c`

Instructions near `00000f76`:

```asm
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
```

Instructions near `00000f7e`:

```asm
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
```

Instructions near `00000f72`:

```asm
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

#### `FUN_00000fb0` @ `00000fb0`

Instructions near `00000fba`:

```asm
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
```

Instructions near `00000fc4`:

```asm
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
```

Instructions near `00000fb6`:

```asm
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

### `20004084`

- no direct references found

### `20004098`

- no direct references found

### `200040a0`

- no direct references found

### `200040b4`

- no direct references found

## Ranked Event-Queue Users

### `FUN_00000eec` @ `00000eec` score `55`

- reasons: exact event queue address, event opcode constant, framing/7-bit MIDI-like value

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

### `FUN_00000f6c` @ `00000f6c` score `47`

- reasons: exact event queue address, event opcode constant

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

### `FUN_00000fb0` @ `00000fb0` score `47`

- reasons: exact event queue address, event opcode constant

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

### `FUN_00001030` @ `00001030` score `43`

- reasons: exact event queue address, framing/7-bit MIDI-like value

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

### `FUN_000228c4` @ `000228c4` score `36`

- reasons: event opcode constant, framing/7-bit MIDI-like value, likely outbound MIDI send

```c

undefined4 FUN_000228c4(int param_1,int param_2)

{
  short sVar1;
  undefined2 *puVar2;
  undefined4 uVar3;
  undefined1 uVar4;
  undefined2 uVar5;
  undefined2 uVar6;
  uint uVar7;
  int iVar8;
  undefined2 *puVar9;
  
  uVar7 = FUN_0002dc30(1);
  iVar8 = DAT_00022a6c;
  puVar2 = DAT_00022a68;
  puVar9 = DAT_00022a64;
  if (uVar7 == 3) {
    DAT_00022a64[1] = *(undefined2 *)(*DAT_00022a60 + param_1 * 0x16 + 0xc);
    *puVar9 = (short)DAT_00022a78;
    if (param_2 == 0) {
      puVar9[2] = 0;
    }
    else if (param_2 == 2) {
      puVar9[2] = 0x7f;
    }
    uVar4 = 2;
  }
  else {
    if (3 < uVar7) {
      if (uVar7 != 6) {
        return 0;
      }
      *DAT_00022a68 = 0x8f0;
      uVar4 = *(undefined1 *)(iVar8 + 1);
      *(char *)((int)puVar2 + 7) = (char)param_2;
      *(undefined1 *)(puVar2 + 1) = uVar4;
      *(undefined1 *)((int)puVar2 + 3) = 0x10;
      puVar2[2] = (short)DAT_00022a70;
      *(char *)(puVar2 + 3) = (char)param_1;
      *(undefined1 *)(puVar2 + 4) = 0xf7;
      FUN_0002654c(0,puVar2,9);
      *puVar2 = 0x8f0;
      uVar3 = DAT_00022a70;
      *(undefined1 *)(puVar2 + 1) = *(undefined1 *)(iVar8 + 1);
      puVar2[2] = (short)uVar3;
      *(undefined1 *)((int)puVar2 + 3) = 0x10;
      puVar2[3] = (ushort)param_1 & 0xff | (ushort)(param_2 << 8);
      *(undefined1 *)(puVar2 + 4) = 0xf7;
      FUN_0002654c(2,puVar2,9);
      return 0;
    }
    if (uVar7 == 0) {
      iVar8 = FUN_0002dc30(9);
      uVar3 = DAT_00022a74;
      puVar9 = DAT_00022a64;
      if ((iVar8 != 0) && (sVar1 = *(short *)(*DAT_00022a60 + param_1 * 0x16 + 0x10), sVar1 != 0xff)
         ) {
        DAT_00022a64[1] = sVar1;
        *puVar9 = (short)uVar3;
        if (param_2 == 0) {
          puVar9[2] = 0;
        }
        else if (param_2 == 2) {
          puVar9[2] = 0x7f;
        }
        FUN_00020264(0,5,puVar9);
        return 0;
      }
      uVar4 = FUN_0002dc94(param_1,1);
      puVar9 = DAT_00022a64;
      *(undefined1 *)((int)DAT_00022a64 + 1) = uVar4;
      uVar5 = FUN_0002dc94(param_1,2);
      puVar9[1] = uVar5;
      uVar5 = FUN_0002dc94(param_1,4);
      uVar6 = FUN_0002dc94(param_1,3);
      uVar4 = FUN_0002dc94(param_1,5);
      if (puVar9[1] == 0xff) {
        return 0;
      }
      iVar8 = FUN_0002dc94(param_1,0);
      if (iVar8 == 2) {
        if (param_2 == 2) {
          *(undefined1 *)puVar9 = 1;
          puVar9[2] = uVar5;
        }
        else {
          *(undefined1 *)puVar9 = 0;
          puVar9[2] = uVar6;
        }
      }
      else {
        if (iVar8 == 3) {
          *(undefined1 *)puVar9 = 4;
        }
        else {
          if (iVar8 != 1) {
            return 0;
          }
          *(undefined1 *)puVar9 = 3;
        }
        if (param_2 == 2) {
          puVar9[2] = uVar5;
        }
        else {
          puVar9[2] = uVar6;
        }
      }
    }
    else {
      if (uVar7 != 1) {
        return 0;
      }
      DAT_00022a64[1] = *(undefined2 *)(*DAT_00022a60 + param_1 * 0x16 + 0xe);
      *puVar9 = 3;
      if (param_2 == 0) {
        uVar4 = 0;
        puVar9[2] = 0;
      }
      else {
        if (param_2 == 2) {
          puVar9[2] = 0x7f;
        }
        uVar4 = 0;
      }
    }
  }
  FUN_000225a8(uVar4,puVar9);
  return 0;
}
```

### `FUN_00000ff4` @ `00000ff4` score `35`

- reasons: exact event queue address

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

## Raw Queue Address DWord Hits

### `20004080`

- no raw dword hits found

### `20004081`

- no raw dword hits found

### `20004084`

- no raw dword hits found

### `20004098`

- no raw dword hits found

### `200040a0`

- no raw dword hits found

### `200040b4`

- no raw dword hits found

