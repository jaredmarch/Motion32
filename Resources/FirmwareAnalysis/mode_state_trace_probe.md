# Motion 32 Mode/State Trace Probe

## `20004291`

- from `00001e82` in `FUN_00001e5c` @ `00001e5c` type=WRITE
- from `00001e7c` in `FUN_00001e5c` @ `00001e5c` type=PARAM
- from `00001e58` in `FUN_00001e50` @ `00001e50` type=READ

### Function `FUN_00001e5c` @ `00001e5c`

Reference site `00001e82`:

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

Reference site `00001e7c`:

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

### Function `FUN_00001e50` @ `00001e50`

Reference site `00001e58`:

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

```c

undefined1 FUN_00001e50(void)

{
  return DAT_20004291;
}
```

## `20004294`

- from `0000211a` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `0000213a` in `FUN_000020a4` @ `000020a4` type=READ

### Function `FUN_000020a4` @ `000020a4`

Reference site `0000211a`:

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

Reference site `0000213a`:

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

## `200045cc`

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

### Function `FUN_0000240c` @ `0000240c`

Reference site `00002416`:

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

Reference site `00002570`:

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

Reference site `00002590`:

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

Reference site `00002614`:

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

Reference site `000025b6`:

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

Reference site `000025d6`:

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

Reference site `00002550`:

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

Reference site `00002530`:

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

Reference site `00002510`:

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

### Function `FUN_000026f4` @ `000026f4`

Reference site `0000270a`:

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

Reference site `00002744`:

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

## `20004538`

- from `00002424` in `FUN_0000240c` @ `0000240c` type=READ

### Function `FUN_0000240c` @ `0000240c`

Reference site `00002424`:

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

## `2000453c`

- from `00002426` in `FUN_0000240c` @ `0000240c` type=READ
- from `00002430` in `FUN_0000240c` @ `0000240c` type=WRITE

### Function `FUN_0000240c` @ `0000240c`

Reference site `00002426`:

```asm
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
00002436: cmp r3,#0x1
```

Reference site `00002430`:

```asm
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
00002436: cmp r3,#0x1
00002438: bls 0x000024f6
0000243a: ldr r1,[r4,#0x10]
0000243c: ldr r2,[r4,#0x14]
0000243e: cmp r1,r2
00002440: beq 0x0000244c
```

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

## `200064c0`

- from `00009d74` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009d76` in `FUN_00009944` @ `00009944` type=READ
- from `00009d7e` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009aaa` in `FUN_00009944` @ `00009944` type=PARAM
- from `00009ab6` in `FUN_00009944` @ `00009944` type=PARAM
- from `00009d34` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009d36` in `FUN_00009944` @ `00009944` type=READ
- from `00009d3e` in `FUN_00009944` @ `00009944` type=WRITE
- from `00009f5e` in `FUN_00009e1c` @ `00009e1c` type=PARAM
- from `00009f6a` in `FUN_00009e1c` @ `00009e1c` type=PARAM
- from `00009fa0` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `00009ffa` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `00009ffc` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `0000a004` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `00009fba` in `FUN_00009e1c` @ `00009e1c` type=WRITE
- from `00009fbc` in `FUN_00009e1c` @ `00009e1c` type=READ
- from `00009fc4` in `FUN_00009e1c` @ `00009e1c` type=WRITE

### Function `FUN_00009944` @ `00009944`

Reference site `00009d74`:

```asm
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
00009d7a: cmp r1,r6
00009d7c: ble 0x00009d80
00009d7e: strh r0,[r2,#0x0]
00009d80: movs r2,#0x1
00009d82: strb r2,[r5,#0x0]
00009d84: adds r2,#0x3
```

Reference site `00009d76`:

```asm
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
00009d7a: cmp r1,r6
00009d7c: ble 0x00009d80
00009d7e: strh r0,[r2,#0x0]
00009d80: movs r2,#0x1
00009d82: strb r2,[r5,#0x0]
00009d84: adds r2,#0x3
00009d86: str r2,[r3,#0x0]
```

Reference site `00009d7e`:

```asm
00009d6a: movw r6,#0x3e8
00009d6e: sxth r1,r1
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
```

Reference site `00009aaa`:

```asm
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
00009abe: bl 0x00003fec
00009ac2: cmp r0,#0x0
00009ac4: beq 0x00009ac8
00009ac6: b 0x00009caa
```

Reference site `00009ab6`:

```asm
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
00009abe: bl 0x00003fec
00009ac2: cmp r0,#0x0
00009ac4: beq 0x00009ac8
00009ac6: b 0x00009caa
00009ac8: bl 0x00003fd8
00009acc: cmp r0,#0x0
00009ace: beq 0x00009ad2
```

Reference site `00009d34`:

```asm
00009d1a: b 0x00009b3c
00009d1c: bl 0x00004028
00009d20: bl 0x00001c8c
00009d24: b 0x00009af0
00009d26: movw r3,#0x64c0
00009d2a: movw r0,#0x3e8
00009d2e: sxth r2,r2
00009d30: movt r3,#0x2000
00009d34: strh r2,[r3,#0x0]
00009d36: ldrh r2,[r3,#0x0]
00009d38: sxth r2,r2
00009d3a: cmp r2,r0
00009d3c: ble 0x00009d40
00009d3e: strh r1,[r3,#0x0]
00009d40: movw r5,#0x64bc
00009d44: movs r3,#0x1
00009d46: movt r5,#0x2000
```

Reference site `00009d36`:

```asm
00009d1c: bl 0x00004028
00009d20: bl 0x00001c8c
00009d24: b 0x00009af0
00009d26: movw r3,#0x64c0
00009d2a: movw r0,#0x3e8
00009d2e: sxth r2,r2
00009d30: movt r3,#0x2000
00009d34: strh r2,[r3,#0x0]
00009d36: ldrh r2,[r3,#0x0]
00009d38: sxth r2,r2
00009d3a: cmp r2,r0
00009d3c: ble 0x00009d40
00009d3e: strh r1,[r3,#0x0]
00009d40: movw r5,#0x64bc
00009d44: movs r3,#0x1
00009d46: movt r5,#0x2000
00009d4a: strb r3,[r5,#0x0]
```

Reference site `00009d3e`:

```asm
00009d2a: movw r0,#0x3e8
00009d2e: sxth r2,r2
00009d30: movt r3,#0x2000
00009d34: strh r2,[r3,#0x0]
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
/* ... truncated ... */
```

### Function `FUN_00009e1c` @ `00009e1c`

Reference site `00009f5e`:

```asm
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
00009f72: b 0x00009e2a
00009f74: movw r1,#0x3ff
00009f78: ldrh r2,[r6,#0x0]
00009f7a: cmp r2,r1
```

Reference site `00009f6a`:

```asm
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
00009f72: b 0x00009e2a
00009f74: movw r1,#0x3ff
00009f78: ldrh r2,[r6,#0x0]
00009f7a: cmp r2,r1
00009f7c: bls 0x00009fac
00009f7e: movw r3,#0x40f8
00009f82: movt r3,#0x2000
```

Reference site `00009fa0`:

```asm
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
00009fb4: sxth r2,r2
```

Reference site `00009ffa`:

```asm
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
0000a000: cmp r1,r6
0000a002: ble 0x0000a006
0000a004: strh r0,[r2,#0x0]
0000a006: movs r2,#0x1
0000a008: strb r2,[r5,#0x0]
0000a00a: adds r2,#0x3
```

Reference site `00009ffc`:

```asm
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
0000a000: cmp r1,r6
0000a002: ble 0x0000a006
0000a004: strh r0,[r2,#0x0]
0000a006: movs r2,#0x1
0000a008: strb r2,[r5,#0x0]
0000a00a: adds r2,#0x3
0000a00c: str r2,[r3,#0x0]
```

Reference site `0000a004`:

```asm
00009ff0: movw r6,#0x3e8
00009ff4: sxth r1,r1
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
```

Reference site `00009fba`:

```asm
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
00009fc0: cmp r2,r0
00009fc2: ble 0x00009fc6
00009fc4: strh r1,[r3,#0x0]
00009fc6: movw r5,#0x64bc
00009fca: movs r3,#0x1
00009fcc: movt r5,#0x2000
```

Reference site `00009fbc`:

```asm
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
00009fc0: cmp r2,r0
00009fc2: ble 0x00009fc6
00009fc4: strh r1,[r3,#0x0]
00009fc6: movw r5,#0x64bc
00009fca: movs r3,#0x1
00009fcc: movt r5,#0x2000
00009fd0: strb r3,[r5,#0x0]
```

Reference site `00009fc4`:

```asm
00009fb0: movw r0,#0x3e8
00009fb4: sxth r2,r2
00009fb6: movt r3,#0x2000
00009fba: strh r2,[r3,#0x0]
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

## `200064d4`

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

### Function `FUN_00009944` @ `00009944`

Reference site `00009b86`:

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

Reference site `00009bd8`:

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

Reference site `00009a3a`:

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

Reference site `0000997a`:

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

Reference site `0000998e`:

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

Reference site `00009b76`:

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
/* ... truncated ... */
```

### Function `FUN_00009e1c` @ `00009e1c`

Reference site `00009e62`:

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

Reference site `00009ef8`:

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

Reference site `00009f08`:

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

Reference site `00009f78`:

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

## `200064d8`

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

### Function `FUN_00009944` @ `00009944`

Reference site `00009a88`:

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

Reference site `00009bd0`:

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

Reference site `00009a9c`:

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

Reference site `00009b04`:

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

Reference site `00009a7e`:

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
/* ... truncated ... */
```

### Function `FUN_00009e1c` @ `00009e1c`

Reference site `00009ea0`:

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

Reference site `00009eb0`:

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

Reference site `00009eb4`:

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

Reference site `00009ebe`:

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

Reference site `00009ec2`:

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

Reference site `00009f4a`:

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

Reference site `00009fa6`:

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

