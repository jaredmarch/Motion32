# Motion 32 USB-MIDI Dispatch Trace Probe

Focus: endpoint setup around `FUN_00003a14`, callback labels near
`0x97e4`/`0x9874`, and any recovered path that resembles USB-MIDI
CIN `0x08` / Note Off packet handling.

## Focus Functions / Labels

### `00003a14` `FUN_00003914`

References to this address:
- none

Instructions near `00003a14`:

```asm
000039ee: cmp r1,#0x0
000039f0: blt 0x00003a00
000039f2: ldrh r4,[r6,#0x6]
000039f4: muls r1,r4
000039f6: ldr r4,[r5,#0x10]
000039f8: ldrh r4,[r4,#0x6]
000039fa: sdiv r4,r1,r4
000039fe: uxth r4,r4
00003a00: strh r4,[r3,#0x6]
00003a02: cmp r0,#0x4
00003a04: bne 0x00003a08
00003a06: b 0x00003b9c
00003a08: mov r4,sp
00003a0a: mov r7,sp
00003a0c: ldrh r4,[r4,#0x12]
00003a0e: ldrh r7,[r7,#0x10]
00003a10: ldrh r1,[r2,#0x8]
00003a12: subs r4,r4,r7
00003a14: subs r1,r1,r4
00003a16: movs r4,#0x0
00003a18: cmp r1,#0x0
00003a1a: blt 0x00003a2a
00003a1c: ldrh r4,[r6,#0x6]
00003a1e: muls r1,r4
00003a20: ldr r4,[r5,#0x10]
00003a22: ldrh r4,[r4,#0x8]
00003a24: sdiv r4,r1,r4
00003a28: uxth r4,r4
00003a2a: strh r4,[r3,#0x8]
00003a2c: cmp r0,#0x5
00003a2e: bne 0x00003a32
00003a30: b 0x00003b9c
00003a32: mov r4,sp
00003a34: mov r7,sp
00003a36: ldrh r4,[r4,#0x16]
00003a38: ldrh r7,[r7,#0x14]
00003a3a: ldrh r1,[r2,#0xa]
```

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

### `00003ab8` `FUN_00003914`

References to this address:
- none

Instructions near `00003ab8`:

```asm
00003a92: subs r1,r1,r4
00003a94: movs r4,#0x0
00003a96: cmp r1,#0x0
00003a98: blt 0x00003aa8
00003a9a: ldrh r4,[r6,#0x6]
00003a9c: muls r1,r4
00003a9e: ldr r4,[r5,#0x10]
00003aa0: ldrh r4,[r4,#0xe]
00003aa2: sdiv r4,r1,r4
00003aa6: uxth r4,r4
00003aa8: strh r4,[r3,#0xe]
00003aaa: cmp r0,#0x8
00003aac: bne 0x00003ab0
00003aae: b 0x00003b9c
00003ab0: mov r4,sp
00003ab2: mov r7,sp
00003ab4: ldrh r4,[r4,#0x22]
00003ab6: ldrh r7,[r7,#0x20]
00003ab8: ldrh r1,[r2,#0x10]
00003aba: subs r4,r4,r7
00003abc: subs r1,r1,r4
00003abe: movs r4,#0x0
00003ac0: cmp r1,#0x0
00003ac2: blt 0x00003ad2
00003ac4: ldrh r4,[r6,#0x6]
00003ac6: muls r1,r4
00003ac8: ldr r4,[r5,#0x10]
00003aca: ldrh r4,[r4,#0x10]
00003acc: sdiv r4,r1,r4
00003ad0: uxth r4,r4
00003ad2: strh r4,[r3,#0x10]
00003ad4: cmp r0,#0x9
00003ad6: beq 0x00003b9c
00003ad8: mov r4,sp
00003ada: mov r7,sp
00003adc: ldrh r4,[r4,#0x26]
00003ade: ldrh r7,[r7,#0x24]
```

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

### `00003ac4` `FUN_00003914`

References to this address:
- none

Instructions near `00003ac4`:

```asm
00003a9e: ldr r4,[r5,#0x10]
00003aa0: ldrh r4,[r4,#0xe]
00003aa2: sdiv r4,r1,r4
00003aa6: uxth r4,r4
00003aa8: strh r4,[r3,#0xe]
00003aaa: cmp r0,#0x8
00003aac: bne 0x00003ab0
00003aae: b 0x00003b9c
00003ab0: mov r4,sp
00003ab2: mov r7,sp
00003ab4: ldrh r4,[r4,#0x22]
00003ab6: ldrh r7,[r7,#0x20]
00003ab8: ldrh r1,[r2,#0x10]
00003aba: subs r4,r4,r7
00003abc: subs r1,r1,r4
00003abe: movs r4,#0x0
00003ac0: cmp r1,#0x0
00003ac2: blt 0x00003ad2
00003ac4: ldrh r4,[r6,#0x6]
00003ac6: muls r1,r4
00003ac8: ldr r4,[r5,#0x10]
00003aca: ldrh r4,[r4,#0x10]
00003acc: sdiv r4,r1,r4
00003ad0: uxth r4,r4
00003ad2: strh r4,[r3,#0x10]
00003ad4: cmp r0,#0x9
00003ad6: beq 0x00003b9c
00003ad8: mov r4,sp
00003ada: mov r7,sp
00003adc: ldrh r4,[r4,#0x26]
00003ade: ldrh r7,[r7,#0x24]
00003ae0: ldrh r1,[r2,#0x12]
00003ae2: subs r4,r4,r7
00003ae4: subs r1,r1,r4
00003ae6: movs r4,#0x0
00003ae8: cmp r1,#0x0
00003aea: blt 0x00003afa
```

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

### `00003af0` `FUN_00003914`

References to this address:
- none

Instructions near `00003af0`:

```asm
00003aca: ldrh r4,[r4,#0x10]
00003acc: sdiv r4,r1,r4
00003ad0: uxth r4,r4
00003ad2: strh r4,[r3,#0x10]
00003ad4: cmp r0,#0x9
00003ad6: beq 0x00003b9c
00003ad8: mov r4,sp
00003ada: mov r7,sp
00003adc: ldrh r4,[r4,#0x26]
00003ade: ldrh r7,[r7,#0x24]
00003ae0: ldrh r1,[r2,#0x12]
00003ae2: subs r4,r4,r7
00003ae4: subs r1,r1,r4
00003ae6: movs r4,#0x0
00003ae8: cmp r1,#0x0
00003aea: blt 0x00003afa
00003aec: ldrh r4,[r6,#0x6]
00003aee: muls r1,r4
00003af0: ldr r4,[r5,#0x10]
00003af2: ldrh r4,[r4,#0x12]
00003af4: sdiv r4,r1,r4
00003af8: uxth r4,r4
00003afa: strh r4,[r3,#0x12]
00003afc: cmp r0,#0xa
00003afe: beq 0x00003b9c
00003b00: mov r4,sp
00003b02: mov r7,sp
00003b04: ldrh r4,[r4,#0x2a]
00003b06: ldrh r7,[r7,#0x28]
00003b08: ldrh r1,[r2,#0x14]
00003b0a: subs r4,r4,r7
00003b0c: subs r1,r1,r4
00003b0e: movs r4,#0x0
00003b10: cmp r1,#0x0
00003b12: blt 0x00003b22
00003b14: ldrh r4,[r6,#0x6]
00003b16: muls r1,r4
```

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

### `00004854` `FUN_00004854`

References to this address:
- from `00002a44` in `FUN_00002a14` @ `00002a14` type=UNCONDITIONAL_CALL
- from `00002a5a` in `FUN_00002a14` @ `00002a14` type=UNCONDITIONAL_CALL

Instructions near `00004854`:

```asm
0000482e: ldrb r6,[r4,#0x2]
00004830: movs r2,#0x80
00004832: ldrb r3,[r0,#0x2]
00004834: orrs r3,r2
00004836: strb r3,[r0,#0x2]
00004838: movs r3,#0x3
0000483a: ands r3,r6
0000483c: cmp r3,#0x2
0000483e: beq 0x00004848
00004840: ldrb r3,[r5,#0x0]
00004842: strb r3,[r0,#0x3]
00004844: movs r0,#0x0
00004846: pop {r3,r4,r5,r6,r7,pc}
00004848: movw r2,#0xfe00
0000484c: ldrh r3,[r5,#0x0]
0000484e: orrs r3,r2
00004850: strh r3,[r0,#0xe]
00004852: b 0x00004844
00004854: movw r2,#0x3800
00004858: movt r2,#0x200
0000485c: mov r12,r2
0000485e: push {r3,r4,r5,r6,r7,lr}
00004860: ldrb r3,[r1,#0x0]
00004862: str r1,[r0,#0x1c]
00004864: add r3,r12
00004866: lsls r3,r3,#0x5
00004868: str r3,[r0,#0x20]
0000486a: movs r3,#0x0
0000486c: strb r3,[r0,#0x0]
0000486e: ldr r2,[r1,#0x14]
00004870: movs r5,r1
00004872: str r2,[r0,#0x24]
00004874: ldr r2,[r1,#0x18]
00004876: str r3,[r0,#0x28]
00004878: str r2,[r0,#0x2c]
0000487a: ldrb r2,[r1,#0x1]
0000487c: movs r1,#0x3
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_00004854(undefined1 *param_1,byte *param_2)

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
  FUN_000085dc(iVar10);
  FUN_000084f4(iVar10);
  FUN_0000854c(iVar10,bVar3,param_1);
  iVar10 = (int)(char)param_2[5];
  bVar3 = param_2[4];
  FUN_000085dc(iVar10);
  FUN_000084f4(iVar10);
  FUN_0000854c(iVar10,bVar3,param_1);
  iVar10 = (int)(char)param_2[7];
  bVar3 = param_2[6];
  FUN_000085dc(iVar10);
  FUN_000084f4(iVar10);
  FUN_0000854c(iVar10,bVar3,param_1);
  iVar10 = (int)(char)param_2[9];
  bVar3 = param_2[8];
  FUN_000085dc(iVar10);
  FUN_000084f4(iVar10);
  FUN_0000854c(iVar10,bVar3,param_1);
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
    *(short *)(pbVar9 + 0x14) = (short)DAT_00004ab8;
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
  FUN_00008598((int)*(char *)(*(int *)(param_1 + 0x1c) + 5));
  FUN_00008598((int)*(char *)(*(int *)(param_1 + 0x1c) + 0xb));
  FUN_00008598((int)*(char *)(*(int *)(param_1 + 0x1c) + 7));
  FUN_00008598((int)*(char *)(*(int *)(param_1 + 0x1c) + 9));
  *(byte *)(*(int *)(param_1 + 0x20) + 2) = bVar3 & 3 | 0x70;
  *(undefined2 *)(param_1 + 8) = *(undefined2 *)(pbVar12 + 10);
  *(undefined4 *)(param_1 + 4) = 0x53434955;
  return 0;
}
```

### `00005854` `FUN_00005808`

References to this address:
- none

Instructions near `00005854`:

```asm
00005828: push {r7,lr}
0000582a: strb r1,[r0,r3]
0000582c: movw r3,#0x3fb0
00005830: movs r7,r2
00005832: ldr r2,[0x00005af8]
00005834: movt r6,#0x407e
00005838: strh r2,[r6,r3]
0000583a: ldr r3,[r0,#0x8]
0000583c: movs r4,r0
0000583e: movs r1,r3
00005840: movs r0,#0x6
00005842: sub sp,#0x14
00005844: mov r9,r3
00005846: bl 0x00005138
0000584a: movw r3,#0x180
0000584e: movs r2,#0xa5
00005850: movs r1,#0xef
00005852: str r2,[r6,r3]
00005854: subs r3,#0x80
00005856: subs r2,#0x95
00005858: strb r2,[r6,r3]
0000585a: strb r1,[r6,r3]
0000585c: strb r2,[r6,r3]
0000585e: ldrb r3,[r6,r3]
00005860: cmp r3,#0x10
00005862: bne 0x0000586a
00005864: mov r8,r8
00005866: ldr r3,[r4,#0x8]
00005868: mov r9,r3
0000586a: mov r1,r9
0000586c: movs r0,#0x3
0000586e: bl 0x00005138
00005872: ldr r3,[r4,#0x4]
00005874: ldrb r1,[r3,#0x0]
00005876: cmp r1,#0x0
00005878: beq 0x0000587c
0000587a: b 0x00005978
```

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

### `000097e4` `PROBE_000097e4`

References to this address:
- from `00002a52` in `FUN_00002a14` @ `00002a14` type=PARAM

Instructions near `000097e4`:

```asm
00009572: strb r1,[r3,#0x0]
00009574: adds r3,#0x1
00009576: b 0x0000956c
00009578: movs r3,#0x0
0000957a: push {r4,lr}
0000957c: cmp r2,r3
0000957e: bne 0x00009582
00009580: pop {r4,pc}
00009582: ldrb r4,[r1,r3]
00009584: strb r4,[r0,r3]
00009586: adds r3,#0x1
00009588: b 0x0000957c
000095e8: push {r3,r4,r5,r6,r7,lr}
000095ea: mov r8,r8
000095ec: pop {r3,r4,r5,r6,r7}
000095ee: pop {r3}
000095f0: mov lr,r3
000095f2: bx lr
000097e4: lsls r1,r0,#0x8
000097e6: movs r0,r0
000097e8: movs r2,r0
000097ea: lsls r2,r0,#0x4
000097ec: lsls r2,r0,#0x8
000097ee: lsls r2,r0,#0xc
000097f0: movs r0,r0
000097f2: movs r0,r0
000097f4: movs r0,r0
000097f6: movs r0,r0
000097f8: movs r0,r0
000097fa: movs r0,r0
000097fc: movs r0,r0
000097fe: movs r0,r0
00009800: ldr r0,[sp,#0x10]
00009802: movs r0,r0
00009804: lsls r0,r0,#0x4
00009806: movs r0,r0
00009808: lsrs r0,r3
```

```c

/* WARNING: Control flow encountered bad instruction data */

void PROBE_000097e4(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}
```

### `00009818` `PROBE_00009818`

References to this address:
- from `00000e98` in `FUN_00000e5c` @ `00000e5c` type=PARAM

Instructions near `00009818`:

```asm
000097ea: lsls r2,r0,#0x4
000097ec: lsls r2,r0,#0x8
000097ee: lsls r2,r0,#0xc
000097f0: movs r0,r0
000097f2: movs r0,r0
000097f4: movs r0,r0
000097f6: movs r0,r0
000097f8: movs r0,r0
000097fa: movs r0,r0
000097fc: movs r0,r0
000097fe: movs r0,r0
00009800: ldr r0,[sp,#0x10]
00009802: movs r0,r0
00009804: lsls r0,r0,#0x4
00009806: movs r0,r0
00009808: lsrs r0,r3
0000980a: movs r0,#0x0
0000980c: movs r7,r1
00009818: movs r0,r0
0000981a: movs r0,r0
0000981c: ldrb r0,[r0,r7]
0000981e: movs r0,r0
00009820: movs r0,r0
00009822: movs r0,r0
00009824: cmp r6,#0xe0
00009826: movs r0,r0
00009828: lsls r0,r0,#0x8
0000982a: movs r0,r1
0000982c: cmp r1,#0xd5
0000982e: movs r0,r0
00009830: movs r0,r0
00009832: movs r0,r0
00009834: ldr r0,[sp,#0xe0]
00009836: movs r0,r0
00009838: movs r0,r0
0000983a: movs r0,r0
0000983c: movs r0,r0
```

```c

/* WARNING: Control flow encountered bad instruction data */

void PROBE_00009818(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}
```

### `00009874` `PROBE_00009874`

References to this address:
- from `00002a3c` in `FUN_00002a14` @ `00002a14` type=PARAM

Instructions near `00009874`:

```asm
00009834: ldr r0,[sp,#0xe0]
00009836: movs r0,r0
00009838: movs r0,r0
0000983a: movs r0,r0
0000983c: movs r0,r0
0000983e: movs r0,r0
00009840: movs r0,r0
00009842: movs r0,r0
00009844: movs r0,r0
00009846: movs r0,r0
00009848: movs r0,r0
0000984a: movs r0,r0
0000984c: movs r0,r0
0000984e: movs r0,r0
00009850: movs r0,r0
00009852: movs r0,r0
00009854: movs r0,r0
00009856: movs r0,r0
00009874: lsls r1,r1,#0x8
00009876: movs r0,r0
00009878: lsls r2,r0,#0x10
0000987a: lsls r2,r0,#0x14
0000987c: lsls r2,r0,#0x18
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
```

```c

/* WARNING: Control flow encountered bad instruction data */

void PROBE_00009874(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}
```

### `000098c4` `<none>`

References to this address:
- from `000009ca` in `FUN_000009c0` @ `000009c0` type=READ

Instructions near `000098c4`:

```asm
0000987a: lsls r2,r0,#0x14
0000987c: lsls r2,r0,#0x18
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
000098c8: ldr r2,[sp,#0x370]
000098ca: movs r0,r0
000098cc: movs r0,r0
000098ce: movs r0,r0
000098d0: movs r0,r0
000098d2: movs r0,r0
000098d4: movs r0,r0
000098d6: movs r0,r0
000098d8: movs r0,r0
000098da: movs r0,r0
000098dc: svc 0xff
000098de: movs r0,r0
000098e0: movs r7,r5
000098e2: movs r0,r0
000098e4: ldr r0,[sp,#0x3b0]
000098e6: movs r0,r0
000098e8: movs r0,r0
000098ea: movs r0,r0
000098ec: movs r0,r0
```

## Raw Function-Pointer / Callback Table Hits

### target `00003ac4` / thumb `00003ac5`

- no raw pointer-sized hits found

### target `00003af0` / thumb `00003af1`

- no raw pointer-sized hits found

### target `000097e4` / thumb `000097e5`

- no raw pointer-sized hits found

### target `00009818` / thumb `00009819`

- no raw pointer-sized hits found

### target `00009874` / thumb `00009875`

- no raw pointer-sized hits found

### target `000098c4` / thumb `000098c5`

- no raw pointer-sized hits found

## Ranked CIN / Channel-Voice Receive Candidates

### `FUN_00003ce8` @ `00003ce8` score `68`

- reasons: event/CIN byte offset 4, payload byte offset 8, possible CIN 0x08, observed event code 0x02, observed event code 0x04, channel-voice/status nibble clue, value 127

```c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_00003ce8(uint *param_1,uint *param_2,undefined2 *param_3)

{
  bool bVar1;
  char cVar2;
  ushort uVar3;
  short sVar4;
  uint *puVar5;
  short sVar6;
  int iVar7;
  int *piVar8;
  int iVar9;
  ushort *puVar10;
  ushort uVar11;
  int extraout_r1;
  int extraout_r1_00;
  int extraout_r1_01;
  byte bVar12;
  int iVar13;
  int extraout_r2;
  int extraout_r2_00;
  uint uVar14;
  uint extraout_r2_01;
  uint extraout_r2_02;
  uint extraout_r2_03;
  int iVar15;
  uint extraout_r3;
  int extraout_r3_00;
  uint uVar16;
  uint uVar17;
  uint extraout_r3_01;
  uint extraout_r3_02;
  uint extraout_r3_03;
  uint uVar18;
  uint *puVar19;
  uint uVar20;
  uint uVar21;
  ushort *puVar22;
  short *psVar23;
  uint uVar24;
  int iVar25;
  uint *extraout_r12;
  uint *extraout_r12_00;
  uint *extraout_r12_01;
  uint *puVar26;
  undefined8 uVar27;
  ulonglong uVar28;
  uint *local_a8;
  uint *local_a4;
  undefined2 *local_9c;
  ushort auStack_78 [3];
  ushort auStack_72 [4];
  undefined2 uStack_6a;
  undefined2 uStack_68;
  undefined2 uStack_66;
  undefined2 uStack_64;
  undefined2 uStack_62;
  ushort auStack_60 [30];
  
  iVar7 = (**(code **)(((undefined4 *)param_1[0x1f])[2] + 8))
                    (*(undefined4 *)param_1[0x1f],auStack_60);
  if (iVar7 == 6000) {
    return 6000;
  }
  if (iVar7 == 0x1772) {
    return 0x1772;
  }
  piVar8 = (int *)param_1[0x1e];
  local_a8 = (uint *)(uint)*(byte *)(piVar8 + 4);
  if (local_a8 == (uint *)0x0) {
    iVar7 = FUN_00003e3a();
    return iVar7;
  }
  bVar12 = *(byte *)(*(int *)(param_1[0x1f] + 4) + 5);
  if (bVar12 == 1) {
    uVar24 = 0;
    uVar16 = param_1[6];
    uVar17 = 0;
    puVar19 = local_a8;
    puVar26 = param_1;
    puVar5 = (uint *)*piVar8;
    local_a4 = local_a8;
    goto LAB_000042d8;
  }
  if ((~bVar12 & 3) != 0) {
    iVar7 = FUN_00003e3a();
    return iVar7;
  }
  iVar15 = *piVar8;
  iVar7 = 0;
  uVar24 = 0;
  puVar22 = (ushort *)0xafc7;
  do {
    while( true ) {
      iVar13 = (uint)*(byte *)(iVar15 + iVar7) * 4;
      uVar16 = (uint)auStack_60[(uint)*(byte *)(iVar15 + iVar7) * 2 + 1];
      if (44999 < uVar16) {
        FUN_00004602();
        iVar7 = extraout_r1;
        iVar13 = extraout_r2;
        uVar16 = extraout_r3;
      }
      iVar13 = uVar16 - *(ushort *)((int)auStack_60 + iVar13);
      if (0xfffc < iVar13 + 0x7ffeU) {
        FUN_0000474a();
        iVar7 = extraout_r1_00;
        iVar13 = extraout_r3_00;
      }
      sVar4 = (short)iVar13;
      iVar13 = uVar24 * 2;
      psVar23 = (short *)(param_1[6] + iVar13);
      sVar6 = *(short *)(param_1[6] + iVar13);
      if (sVar6 != 0) break;
      *psVar23 = sVar4;
FUN_00003d5c:
      uVar24 = uVar24 + 1;
      iVar7 = iVar7 + 6;
      if (local_a8 <= (uint *)(uVar24 & 0xff)) goto LAB_00003e34;
    }
    iVar9 = (int)(short)(sVar6 - *(short *)(param_1[4] + iVar13));
    iVar25 = (uint)*(ushort *)(param_1[5] + iVar13) + iVar9;
    if (iVar25 + 0x7fffU < 0xffff) {
      if (sVar4 < iVar9) {
        FUN_00004636();
        iVar7 = extraout_r1_01;
        iVar13 = extraout_r2_00;
      }
      if ((int)(short)iVar25 < (int)sVar4) {
        *(undefined2 *)(param_1[7] + iVar13) = 0;
        puVar19 = (uint *)(param_1[8] + iVar13);
        uVar11 = *(ushort *)(param_1[8] + iVar13);
        piVar8 = (int *)0xfffc;
        local_a4 = param_1;
        if (uVar11 < *(byte *)((int)param_1 + 0x2d)) {
          *(ushort *)puVar19 = uVar11 + 1;
          uVar28 = FUN_00003dde();
/* ... truncated ... */
```

### `FUN_00003d5c` @ `00003d5c` score `68`

- reasons: event/CIN byte offset 4, payload byte offset 8, possible CIN 0x08, observed event code 0x02, observed event code 0x04, channel-voice/status nibble clue, value 127

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4
FUN_00003d5c(undefined4 param_1,int param_2,undefined4 param_3,undefined4 param_4,uint param_5,
            uint param_6,undefined4 param_7,undefined2 *param_8,int param_9,undefined4 *param_10)

{
  bool bVar1;
  char cVar2;
  short sVar3;
  ushort uVar4;
  short sVar5;
  int iVar6;
  int iVar7;
  ushort *puVar8;
  ushort uVar9;
  int extraout_r1;
  int extraout_r1_00;
  int extraout_r1_01;
  undefined2 *puVar10;
  byte bVar11;
  int iVar12;
  int extraout_r2;
  int extraout_r2_00;
  uint uVar13;
  int extraout_r2_01;
  int extraout_r2_02;
  int extraout_r2_03;
  undefined2 uVar14;
  uint uVar15;
  uint extraout_r3;
  int extraout_r3_00;
  undefined4 uVar16;
  uint extraout_r3_01;
  uint extraout_r3_02;
  uint extraout_r3_03;
  short *psVar17;
  uint uVar18;
  uint uVar19;
  uint *puVar20;
  uint uVar21;
  uint uVar22;
  int unaff_r5;
  uint unaff_r7;
  int iVar23;
  uint uVar24;
  ushort *unaff_r8;
  int iVar25;
  int *piVar26;
  uint unaff_r11;
  int extraout_r12;
  int extraout_r12_00;
  int extraout_r12_01;
  undefined8 uVar27;
  ulonglong uVar28;
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
  
  uVar19 = param_6;
code_r0x00003d5c:
  unaff_r7 = unaff_r7 + 1;
  if ((unaff_r7 & 0xff) < param_5) {
    while( true ) {
      param_2 = param_2 + 6;
      iVar12 = (uint)*(byte *)(unaff_r5 + param_2) * 4;
      uVar15 = (uint)*(ushort *)(&stack0x0000004a + iVar12);
      if ((int)unaff_r8 < (int)uVar15) {
        FUN_00004602();
        param_2 = extraout_r1;
        iVar12 = extraout_r2;
        uVar15 = extraout_r3;
      }
      iVar12 = uVar15 - *(ushort *)(&stack0x00000048 + iVar12);
      if (unaff_r11 < iVar12 + 0x7ffeU) {
        FUN_0000474a();
        param_2 = extraout_r1_00;
        iVar12 = extraout_r3_00;
      }
      sVar5 = (short)iVar12;
      iVar12 = unaff_r7 * 2;
      psVar17 = (short *)(*(int *)(param_6 + 0x18) + iVar12);
      sVar3 = *(short *)(*(int *)(param_6 + 0x18) + iVar12);
      if (sVar3 == 0) break;
      iVar6 = (int)(short)(sVar3 - *(short *)(*(int *)(param_6 + 0x10) + iVar12));
      iVar25 = (uint)*(ushort *)(*(int *)(param_6 + 0x14) + iVar12) + iVar6;
      if (iVar25 + 0x7fffU < 0xffff) {
        if (sVar5 < iVar6) {
          FUN_00004636();
          param_2 = extraout_r1_01;
          iVar12 = extraout_r2_00;
        }
        if ((int)(short)iVar25 < (int)sVar5) {
          *(undefined2 *)(*(int *)(param_6 + 0x1c) + iVar12) = 0;
          puVar20 = (uint *)(*(int *)(param_6 + 0x20) + iVar12);
          uVar9 = *(ushort *)(*(int *)(param_6 + 0x20) + iVar12);
          if (*(byte *)(param_6 + 0x2d) <= uVar9) {
            if ((int)(unaff_r7 - 0x20) < 0) {
              uVar15 = 1 >> (0x20 - unaff_r7 & 0xff);
            }
            else {
              uVar15 = 1 << (unaff_r7 - 0x20 & 0xff);
            }
            *(uint *)(param_6 + 0xc) = *(uint *)(param_6 + 0xc) & ~uVar15;
            *(uint *)(param_6 + 8) = *(uint *)(param_6 + 8) & ~(1 << (unaff_r7 & 0xff));
            uVar28 = FUN_00003dde();
            iVar12 = extraout_r2_01;
            uVar15 = extraout_r3_01;
            iVar6 = extraout_r12;
            goto LAB_00004582;
          }
          *(ushort *)puVar20 = uVar9 + 1;
          uVar28 = FUN_00003dde();
          iVar12 = extraout_r2_03;
          uVar15 = extraout_r3_03;
          iVar6 = extraout_r12_01;
          goto LAB_0000475e;
        }
      }
      if (*(short *)(param_6 + 0x2e) == 0) goto code_r0x00003d5c;
      iVar6 = *(int *)(param_6 + 0x28);
      uVar27 = CONCAT44(param_2,unaff_r7 * 4 + *(int *)(param_6 + 0x24));
      if ((int)(unaff_r7 - 0x20) < 0) {
        uVar15 = *(uint *)(param_6 + 8) >> (unaff_r7 & 0xff) |
                 *(int *)(param_6 + 0xc) << (0x20 - unaff_r7 & 0xff);
      }
      else {
        uVar15 = *(uint *)(param_6 + 0xc) >> (unaff_r7 - 0x20 & 0xff);
      }
      if ((uVar15 & 1) == 0) {
        uVar27 = FUN_00004606();
/* ... truncated ... */
```

### `FUN_00003dde` @ `00003dde` score `68`

- reasons: event/CIN byte offset 4, payload byte offset 8, possible CIN 0x08, observed event code 0x02, observed event code 0x04, channel-voice/status nibble clue, value 127

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4
FUN_00003dde(undefined4 param_1,int param_2,int param_3,undefined4 param_4,uint param_5,uint param_6
            ,undefined4 param_7,undefined2 *param_8,int param_9,undefined4 *param_10)

{
  bool bVar1;
  char cVar2;
  short sVar3;
  ushort uVar4;
  short sVar5;
  int iVar6;
  ushort *puVar7;
  int iVar8;
  uint uVar9;
  ushort uVar10;
  int extraout_r1;
  int extraout_r1_00;
  int extraout_r1_01;
  undefined2 *puVar11;
  uint uVar12;
  byte bVar13;
  int extraout_r2;
  int extraout_r2_00;
  uint uVar14;
  uint uVar15;
  int extraout_r2_01;
  int extraout_r2_02;
  int extraout_r2_03;
  undefined2 uVar16;
  uint extraout_r3;
  int extraout_r3_00;
  undefined4 uVar17;
  uint extraout_r3_01;
  uint extraout_r3_02;
  uint extraout_r3_03;
  short *psVar18;
  int iVar19;
  int iVar20;
  uint uVar21;
  uint *puVar22;
  int unaff_r5;
  uint unaff_r7;
  int iVar23;
  uint uVar24;
  ushort *unaff_r8;
  int *piVar25;
  uint unaff_r11;
  int extraout_r12;
  int extraout_r12_00;
  int extraout_r12_01;
  uint uVar26;
  undefined8 uVar27;
  ulonglong uVar28;
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
  
  uVar21 = param_6;
  do {
    do {
      uVar12 = unaff_r7;
      if (*(short *)(param_6 + 0x2e) != 0) {
        iVar19 = *(int *)(param_6 + 0x28);
        uVar27 = CONCAT44(param_2,unaff_r7 * 4 + *(int *)(param_6 + 0x24));
        if ((int)(unaff_r7 - 0x20) < 0) {
          uVar15 = *(uint *)(param_6 + 8) >> (unaff_r7 & 0xff) |
                   *(int *)(param_6 + 0xc) << (0x20 - unaff_r7 & 0xff);
        }
        else {
          uVar15 = *(uint *)(param_6 + 0xc) >> (unaff_r7 - 0x20 & 0xff);
        }
        if ((uVar15 & 1) == 0) {
          uVar27 = FUN_00004606();
        }
        param_2 = (int)((ulonglong)uVar27 >> 0x20);
        *(undefined4 *)uVar27 = 0;
        *(undefined2 *)(param_3 + iVar19) = 0;
      }
      while( true ) {
        unaff_r7 = uVar12 + 1;
        if (param_5 <= (unaff_r7 & 0xff)) {
          uVar17 = *(undefined4 *)(param_6 + 0xc);
          *param_10 = *(undefined4 *)(param_6 + 8);
          param_10[1] = uVar17;
          if (*(char *)(param_9 + 0x11) == '\0') goto LAB_000040de;
          param_6 = 0;
          param_5 = 0;
          goto LAB_00003e62;
        }
        param_2 = param_2 + 6;
        iVar19 = (uint)*(byte *)(unaff_r5 + param_2) * 4;
        uVar15 = (uint)*(ushort *)(&stack0x0000004a + iVar19);
        if ((int)unaff_r8 < (int)uVar15) {
          FUN_00004602();
          param_2 = extraout_r1;
          iVar19 = extraout_r2;
          uVar15 = extraout_r3;
        }
        iVar19 = uVar15 - *(ushort *)(&stack0x00000048 + iVar19);
        if (unaff_r11 < iVar19 + 0x7ffeU) {
          FUN_0000474a();
          param_2 = extraout_r1_00;
          iVar19 = extraout_r3_00;
        }
        sVar5 = (short)iVar19;
        param_3 = unaff_r7 * 2;
        psVar18 = (short *)(*(int *)(param_6 + 0x18) + param_3);
        sVar3 = *(short *)(*(int *)(param_6 + 0x18) + param_3);
        if (sVar3 != 0) break;
        *psVar18 = sVar5;
        uVar12 = unaff_r7;
      }
      iVar19 = (int)(short)(sVar3 - *(short *)(*(int *)(param_6 + 0x10) + param_3));
      iVar8 = (uint)*(ushort *)(*(int *)(param_6 + 0x14) + param_3) + iVar19;
    } while (0xfffe < iVar8 + 0x7fffU);
    if (sVar5 < iVar19) {
      FUN_00004636();
      param_2 = extraout_r1_01;
      param_3 = extraout_r2_00;
    }
  } while ((int)sVar5 <= (int)(short)iVar8);
  *(undefined2 *)(*(int *)(param_6 + 0x1c) + param_3) = 0;
  puVar22 = (uint *)(*(int *)(param_6 + 0x20) + param_3);
  uVar10 = *(ushort *)(*(int *)(param_6 + 0x20) + param_3);
  if (*(byte *)(param_6 + 0x2d) <= uVar10) {
    if ((int)(uVar12 - 0x1f) < 0) {
      uVar12 = 1 >> (0x20 - unaff_r7 & 0xff);
    }
    else {
/* ... truncated ... */
```

### `FUN_00003e3a` @ `00003e3a` score `62`

- reasons: event/CIN byte offset 4, payload byte offset 8, possible CIN 0x08, observed event code 0x02, observed event code 0x04, channel-voice/status nibble clue

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
/* ... truncated ... */
```

### `FUN_0005d624` @ `0005d624` score `52`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, observed event code 0x04, channel-voice/status nibble clue

```c

int FUN_0005d624(int param_1,int param_2,int param_3,int param_4)

{
  byte bVar1;
  undefined1 uVar2;
  byte bVar3;
  int iVar4;
  uint uVar5;
  uint uVar6;
  char cVar7;
  byte bVar8;
  int iVar9;
  int iVar10;
  int iVar11;
  int iVar12;
  int iVar13;
  int iVar14;
  
  iVar4 = DAT_0005d7fc;
  iVar9 = param_1 * 0x248;
  if (*(char *)(DAT_0005d7fc + iVar9 + 1) == '\0') {
    param_4 = 0;
  }
  else {
    if (param_4 != 0) {
      iVar13 = iVar9 + 0x24 + DAT_0005d7fc;
      iVar14 = iVar9 + 3 + DAT_0005d7fc;
      iVar12 = 0;
      do {
        uVar5 = FUN_0005ddf8(iVar13);
        if (uVar5 < 4) {
          FUN_0005d550(param_1);
          return iVar12;
        }
        bVar1 = *(byte *)(param_3 + iVar12);
        iVar10 = iVar4 + param_1 * 0x248;
        bVar8 = *(byte *)(iVar10 + 7);
        uVar5 = (uint)bVar8;
        iVar12 = iVar12 + 1;
        if (uVar5 == 0) {
          *(undefined1 *)(iVar10 + 7) = 2;
          *(byte *)(iVar10 + 4) = bVar1;
          if ((*(byte *)(iVar10 + 3) & 0xf) == 4) {
            if (bVar1 == 0xf7) {
              *(byte *)(iVar10 + 3) = (byte)(param_2 << 4) | 5;
LAB_0005d77e:
              uVar6 = 2;
              *(undefined1 *)(iVar4 + param_1 * 0x248 + 8) = 2;
              goto LAB_0005d746;
            }
            *(undefined1 *)(iVar10 + 8) = 4;
          }
          else {
            bVar3 = bVar1 >> 4;
            uVar5 = (uint)bVar3;
            bVar8 = (byte)(0x4f00U >> uVar5) & 1;
            if ((0x4f00U >> uVar5 & 1) == 0) {
              if (uVar5 - 0xc < 2) {
                *(byte *)(iVar10 + 3) = (byte)(param_2 << 4) | bVar3;
                *(undefined1 *)(iVar10 + 8) = 3;
              }
              else {
                if (uVar5 != 0xf) {
                  *(byte *)(iVar10 + 5) = bVar8;
                  *(byte *)(iVar10 + 3) = (byte)(param_2 << 4) | 0xf;
                  *(byte *)(iVar10 + 6) = bVar8;
                  goto LAB_0005d77e;
                }
                if (bVar1 == 0xf0) {
                  bVar8 = 4;
                  cVar7 = '\x04';
                }
                else if ((bVar1 & 0xfd) == 0xf1) {
                  bVar8 = 2;
                  cVar7 = '\x03';
                }
                else if (bVar1 == 0xf2) {
                  bVar8 = 3;
                  cVar7 = '\x04';
                }
                else {
                  bVar8 = 5;
                  cVar7 = '\x02';
                }
                iVar10 = iVar4 + param_1 * 0x248;
                *(char *)(iVar10 + 8) = cVar7;
                *(byte *)(iVar10 + 3) = bVar8 | (byte)(param_2 << 4);
                if (cVar7 == '\x02') {
                  uVar6 = 2;
                  goto LAB_0005d746;
                }
              }
            }
            else {
              *(byte *)(iVar10 + 3) = (byte)(param_2 << 4) | bVar3;
              *(undefined1 *)(iVar10 + 8) = 4;
            }
          }
        }
        else {
          if (3 < uVar5) {
            return iVar12;
          }
          *(byte *)(iVar10 + uVar5 + 3) = bVar1;
          uVar6 = uVar5 + 1 & 0xff;
          uVar2 = (undefined1)(uVar5 + 1);
          *(undefined1 *)(iVar10 + 7) = uVar2;
          if (((*(byte *)(iVar10 + 3) & 0xf) == 4) && (bVar1 == 0xf7)) {
            *(byte *)(iVar10 + 3) = bVar8 + 4 | (byte)(param_2 << 4);
            *(undefined1 *)(iVar10 + 8) = uVar2;
          }
          else if (*(byte *)(iVar4 + param_1 * 0x248 + 8) != uVar6) goto LAB_0005d6fe;
          if (uVar6 != 4) {
LAB_0005d746:
            FUN_0005aeec(iVar4 + uVar6 + iVar9 + 3,0,4 - uVar6 & 0xff);
          }
          iVar10 = FUN_0005df68(iVar13,iVar14,4);
          iVar11 = iVar4 + param_1 * 0x248;
          *(undefined1 *)(iVar11 + 8) = 0;
          *(undefined1 *)(iVar11 + 7) = 0;
          if (iVar10 != 4) {
            return iVar12;
          }
        }
LAB_0005d6fe:
      } while (param_4 != iVar12);
    }
    FUN_0005d550(param_1);
  }
  return param_4;
}
```

### `FUN_00006074` @ `00006074` score `50`

- reasons: event/CIN byte offset 4, payload byte offset 8, possible CIN 0x08, channel-voice/status nibble clue

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_00006074(int param_1,int param_2,int param_3,undefined2 param_4)

{
  uint uVar1;
  int iVar2;
  int iVar3;
  
  uVar1 = (uint)*(char *)(param_1 + 4);
  iVar2 = *(int *)(uVar1 * 4 + 0x20004000);
  iVar3 = (uVar1 + 0xc0) * 4;
  *(uint *)(iVar3 + 0x40006000) = *(uint *)(iVar3 + 0x40006000) & DAT_00006108;
  do {
  } while ((uVar1 | 0x8000) == (uint)_DAT_4000540e);
  if (param_2 != 0) {
    *(int *)(iVar2 + 4) = param_2;
  }
  if (param_3 != 0) {
    *(int *)(iVar2 + 8) = param_3;
  }
  if ((*(byte *)(iVar2 + 3) & 0xc0) == 0x80) {
    *(undefined2 *)(iVar2 + 0xc) = param_4;
  }
  else if (*(byte *)(iVar2 + 3) < 0x40) {
    *(undefined2 *)(iVar2 + 0xe) = param_4;
  }
  DAT_40005400 = 0x18;
  iVar2 = (uVar1 + 0xc0) * 4;
  *(uint *)(iVar2 + 0x40006000) = *(uint *)(iVar2 + 0x40006000) | 0x1000000;
  return 0;
}
```

### `FUN_0000355c` @ `0000355c` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, channel-voice/status nibble clue, value 127

```c

undefined4 FUN_0000355c(uint *param_1,undefined1 *param_2,uint param_3)

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

### `FUN_00004854` @ `00004854` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, channel-voice/status nibble clue

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_00004854(undefined1 *param_1,byte *param_2)

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
  FUN_000085dc(iVar10);
  FUN_000084f4(iVar10);
  FUN_0000854c(iVar10,bVar3,param_1);
  iVar10 = (int)(char)param_2[5];
  bVar3 = param_2[4];
  FUN_000085dc(iVar10);
  FUN_000084f4(iVar10);
  FUN_0000854c(iVar10,bVar3,param_1);
  iVar10 = (int)(char)param_2[7];
  bVar3 = param_2[6];
  FUN_000085dc(iVar10);
  FUN_000084f4(iVar10);
  FUN_0000854c(iVar10,bVar3,param_1);
  iVar10 = (int)(char)param_2[9];
  bVar3 = param_2[8];
  FUN_000085dc(iVar10);
  FUN_000084f4(iVar10);
  FUN_0000854c(iVar10,bVar3,param_1);
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
    *(short *)(pbVar9 + 0x14) = (short)DAT_00004ab8;
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
/* ... truncated ... */
```

### `FUN_0000557c` @ `0000557c` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, channel-voice/status nibble clue, value 127

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_0000557c(undefined4 *param_1,char *param_2)

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
    FUN_00008600((int)param_2[0x11],param_2[0x10],param_1);
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
    FUN_00005138(6,uVar3);
  }
  _DAT_407effb0 = (short)DAT_00005800;
  FUN_00005138(6,uVar3);
  _DAT_407ec180 = 0xa5;
  DAT_407ec100 = 0x10;
  FUN_00005138(3,param_1[2]);
  if (*(char *)param_1[1] != '\0') {
    FUN_00008598((int)((char *)param_1[1])[0x11]);
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
  FUN_00005138(0x10,param_1[2]);
  _DAT_407effb0 = (short)DAT_00005804;
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

### `FUN_000225f4` @ `000225f4` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, channel-voice/status nibble clue

```c

undefined4 FUN_000225f4(undefined4 param_1,int param_2,int param_3,undefined1 param_4,byte param_5)

{
  byte bVar1;
  ushort uVar2;
  undefined2 uVar3;
  undefined1 *puVar4;
  int iVar5;
  int iVar6;
  int iVar7;
  char cVar8;
  int iVar9;
  uint uVar10;
  uint uVar11;
  uint uVar12;
  uint uVar13;
  uint uVar14;
  
  uVar14 = 0;
  uVar13 = 0;
  iVar5 = FUN_0002dc30(0x37);
  iVar9 = (int)(short)iVar5;
  FUN_0002dc40(0x28);
  uVar11 = 0;
  uVar12 = 0;
  iVar6 = FUN_0002dc30(0x26);
  if (iVar6 == 0) {
    iVar6 = FUN_0002dc30(0x38);
    if (iVar6 == 0) {
      iVar7 = FUN_0002dc30(0x35);
      bVar1 = *(byte *)(DAT_000228b8 + param_2);
      iVar6 = DAT_000228bc;
    }
    else {
      if (iVar6 != 1) goto LAB_00022648;
      iVar7 = FUN_0002dc30(0x36);
      bVar1 = *(byte *)(DAT_000228b8 + param_2);
      iVar6 = DAT_000228c0;
    }
    iVar7 = (iVar7 * 0x10 + (uint)bVar1) * 4;
    uVar13 = (uint)*(byte *)(iVar7 + iVar6);
    iVar6 = iVar6 + iVar7;
    uVar12 = (uint)*(byte *)(iVar6 + 1);
    uVar11 = (uint)*(byte *)(iVar6 + 2);
    uVar14 = (uint)*(byte *)(iVar6 + 3);
  }
  else {
    iVar6 = FUN_0002dc40(0x1e);
    iVar5 = iVar5 + iVar6 * 0xc;
    iVar9 = (int)(short)iVar5;
    iVar6 = FUN_0002dc30(0x39);
    if (iVar6 == 1) {
      iVar6 = FUN_0002dc30(0x3a);
      uVar2 = *(ushort *)(DAT_000228b0 + 0x284);
      iVar7 = FUN_0002dc30(0x28);
      iVar6 = DAT_000228b4 + iVar6 * 0x114 + (((uint)uVar2 + param_2) - iVar7) * 0xc;
      uVar13 = (uint)*(byte *)(iVar6 + 4);
      uVar12 = (uint)*(byte *)(iVar6 + 5);
      uVar14 = (uint)*(byte *)(iVar6 + 7);
      uVar11 = (uint)*(byte *)(iVar6 + 6);
    }
    else if (iVar6 == 2) {
      iVar6 = FUN_0002dc30(0x3a);
      uVar2 = *(ushort *)(DAT_000228b0 + 0x284);
      iVar7 = FUN_0002dc30(0x28);
      iVar6 = DAT_000228b4 + iVar6 * 0x114 + (((uint)uVar2 + param_2) - iVar7) * 0xc;
      uVar13 = (uint)*(byte *)(iVar6 + 8);
      uVar12 = (uint)*(byte *)(iVar6 + 9);
      uVar14 = (uint)*(byte *)(iVar6 + 0xb);
      uVar11 = (uint)*(byte *)(iVar6 + 10);
    }
    else if (iVar6 == 0) {
      iVar6 = FUN_0002dc30(0x3a);
      uVar2 = *(ushort *)(DAT_000228b0 + 0x284);
      iVar7 = FUN_0002dc30(0x28);
      iVar6 = (iVar6 * 0x45 + (((uint)uVar2 + param_2) - iVar7) * 3) * 4;
      uVar13 = (uint)*(byte *)(iVar6 + DAT_000228b4);
      iVar6 = DAT_000228b4 + iVar6;
      uVar14 = (uint)*(byte *)(iVar6 + 3);
      uVar12 = (uint)*(byte *)(iVar6 + 1);
      uVar11 = (uint)*(byte *)(iVar6 + 2);
    }
  }
LAB_00022648:
  puVar4 = DAT_000228a8;
  DAT_000228a8[1] = param_4;
  *puVar4 = (char)param_3;
  uVar10 = uVar13 + iVar5 & 0xffff;
  uVar3 = (undefined2)(uVar13 + iVar5);
  if (param_3 == 1) {
    *(undefined2 *)(puVar4 + 2) = uVar3;
    *(ushort *)(puVar4 + 4) = (ushort)param_5;
    if ((uVar10 < 0x80) &&
       (cVar8 = *(char *)(DAT_000228ac + uVar13 + iVar9) + '\x01',
       *(char *)(DAT_000228ac + uVar13 + iVar9) = cVar8, cVar8 == '\x01')) {
      FUN_000225a8(param_1,puVar4);
    }
    *(short *)(puVar4 + 2) = (short)(uVar12 + iVar5);
    if (((uVar12 + iVar5 & 0xffff) < 0x80) &&
       (cVar8 = *(char *)(DAT_000228ac + uVar12 + iVar9) + '\x01',
       *(char *)(DAT_000228ac + uVar12 + iVar9) = cVar8, cVar8 == '\x01')) {
      FUN_000225a8(param_1,puVar4);
    }
    *(short *)(puVar4 + 2) = (short)(uVar11 + iVar5);
    if (((uVar11 + iVar5 & 0xffff) < 0x80) &&
       (cVar8 = *(char *)(DAT_000228ac + uVar11 + iVar9) + '\x01',
       *(char *)(DAT_000228ac + uVar11 + iVar9) = cVar8, cVar8 == '\x01')) {
      FUN_000225a8(param_1,puVar4);
    }
    *(short *)(puVar4 + 2) = (short)(iVar5 + uVar14);
    if (((iVar5 + uVar14 & 0xffff) < 0x80) &&
       (cVar8 = *(char *)(DAT_000228ac + uVar14 + iVar9) + '\x01',
       *(char *)(DAT_000228ac + uVar14 + iVar9) = cVar8, cVar8 == '\x01')) {
      FUN_000225a8(param_1,puVar4);
    }
  }
  else {
    *(undefined2 *)(puVar4 + 2) = uVar3;
    *(undefined2 *)(puVar4 + 4) = 0;
    if (uVar10 < 0x80) {
      cVar8 = *(char *)(DAT_000228ac + uVar13 + iVar9);
      if (cVar8 != '\0') {
        *(char *)(DAT_000228ac + uVar13 + iVar9) = cVar8 + -1;
        FUN_000225a8(param_1,puVar4);
      }
    }
    *(short *)(puVar4 + 2) = (short)(uVar12 + iVar5);
    if ((uVar12 + iVar5 & 0xffff) < 0x80) {
      cVar8 = *(char *)(DAT_000228ac + uVar12 + iVar9);
      if (cVar8 != '\0') {
        *(char *)(DAT_000228ac + uVar12 + iVar9) = cVar8 + -1;
        FUN_000225a8(param_1,puVar4);
      }
    }
    *(short *)(puVar4 + 2) = (short)(uVar11 + iVar5);
    if ((uVar11 + iVar5 & 0xffff) < 0x80) {
      cVar8 = *(char *)(DAT_000228ac + uVar11 + iVar9);
      if (cVar8 != '\0') {
        *(char *)(DAT_000228ac + uVar11 + iVar9) = cVar8 + -1;
/* ... truncated ... */
```

### `FUN_00022a7c` @ `00022a7c` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, observed event code 0x04, channel-voice/status nibble clue, value 127, outgoing SysEx false positive

```c

undefined4 FUN_00022a7c(int param_1,uint param_2)

{
  short sVar1;
  undefined2 *puVar2;
  undefined4 uVar3;
  undefined1 uVar4;
  undefined1 uVar5;
  undefined2 uVar6;
  undefined2 uVar7;
  uint uVar8;
  int iVar9;
  uint uVar10;
  uint uVar11;
  undefined2 *puVar12;
  
  uVar4 = FUN_0002dc30(0x2d);
  uVar8 = FUN_0002dc30(1);
  iVar9 = DAT_00022cd4;
  puVar2 = DAT_00022cd0;
  puVar12 = DAT_00022cc8;
  if (uVar8 == 3) {
    uVar7 = FUN_0002dc30(0x47);
    puVar12 = DAT_00022cc8;
    *DAT_00022cc8 = (short)DAT_00022cdc;
    uVar6 = *(undefined2 *)(*DAT_00022ccc + param_1 * 0xc + 6);
    puVar12[2] = uVar7;
    puVar12[1] = uVar6;
    uVar5 = 2;
    goto LAB_00022bd0;
  }
  if (3 < uVar8) {
    if (uVar8 != 6) {
      return 0;
    }
    *DAT_00022cd0 = 0x8f0;
    uVar4 = *(undefined1 *)(iVar9 + 1);
    *(undefined1 *)((int)puVar2 + 3) = 0x10;
    uVar3 = DAT_00022cd8;
    *(undefined1 *)(puVar2 + 1) = uVar4;
    puVar2[2] = (short)uVar3;
    *(char *)((int)puVar2 + 7) = (char)param_2;
    *(char *)(puVar2 + 3) = (char)param_1;
    *(undefined1 *)(puVar2 + 4) = 0xf7;
    FUN_0002654c(0,puVar2,9);
    *puVar2 = 0x8f0;
    uVar3 = DAT_00022cd8;
    *(undefined1 *)(puVar2 + 1) = *(undefined1 *)(iVar9 + 1);
    puVar2[2] = (short)uVar3;
    *(undefined1 *)((int)puVar2 + 3) = 0x10;
    puVar2[3] = (ushort)param_1 & 0xff | (ushort)(param_2 << 8);
    *(undefined1 *)(puVar2 + 4) = 0xf7;
    FUN_0002654c(2,puVar2,9);
    return 0;
  }
  sVar1 = (short)param_2;
  if (uVar8 != 0) {
    if (uVar8 != 1) {
      return 0;
    }
    *DAT_00022cc8 = 3;
    puVar12[1] = *(undefined2 *)(*DAT_00022ccc + param_1 * 0xc + 8);
    if (param_2 < 0x41) {
      puVar12[2] = 0x80 - sVar1;
    }
    else {
      puVar12[2] = sVar1 + -0x40;
    }
    uVar5 = 0;
    goto LAB_00022bd0;
  }
  iVar9 = FUN_0002dce0(uVar4,param_1,8);
  uVar5 = FUN_0002dce0(uVar4,param_1,2);
  puVar12 = DAT_00022cc8;
  *(undefined1 *)((int)DAT_00022cc8 + 1) = uVar5;
  uVar6 = FUN_0002dce0(uVar4,param_1,3);
  puVar12[1] = uVar6;
  uVar8 = FUN_0002dce0(uVar4,param_1,4);
  uVar10 = FUN_0002dce0(uVar4,param_1,5);
  uVar5 = FUN_0002dce0(uVar4,param_1,6);
  uVar11 = FUN_0002dce0(uVar4,param_1,1);
  if (uVar11 == 4) {
    *(undefined1 *)puVar12 = 3;
    puVar12[1] = 0x20;
  }
  else if (uVar11 < 5) {
    if (uVar11 == 1) {
      *(undefined1 *)puVar12 = 3;
    }
    else {
      if (uVar11 != 3) goto LAB_00022c14;
      *(undefined1 *)puVar12 = 4;
    }
  }
  else {
    if (uVar11 != 5) {
LAB_00022c14:
      uVar11 = FUN_0002dce0(uVar4,param_1,7);
      if (uVar11 == 2) {
        puVar12[2] = sVar1;
        return 0;
      }
      if (2 < uVar11) {
        if (uVar11 != 3) {
          return 0;
        }
        if (0x3f < param_2) {
          puVar12[2] = sVar1 + -0x3f;
          return 0;
        }
        puVar12[2] = sVar1 + 0x41;
        return 0;
      }
      if (uVar11 != 0) {
        if (0x40 < param_2) {
          puVar12[2] = sVar1 + -0x40;
          return 0;
        }
        puVar12[2] = 0x80 - sVar1;
        return 0;
      }
      goto LAB_00022c4c;
    }
    puVar12[1] = 0;
    *(undefined1 *)puVar12 = 3;
  }
  uVar11 = FUN_0002dce0(uVar4,param_1,7);
  if (uVar11 == 2) {
    puVar12[2] = sVar1;
  }
  else if (uVar11 < 3) {
    if (uVar11 == 0) {
LAB_00022c4c:
      if (uVar8 < uVar10) {
                    /* WARNING: Subroutine does not return */
        FUN_0005a430(((iVar9 * uVar10 + uVar8 * 0x7f) - uVar8) + 1,0x7f);
      }
                    /* WARNING: Subroutine does not return */
      FUN_0005a430(((uVar8 * 0x7f - uVar8 * iVar9) - uVar10) + 1,0x7f);
/* ... truncated ... */
```

### `PROBE_00022b70` @ `00022b70` score `46`

- reasons: event/CIN byte offset 4, observed event code 0x02, observed event code 0x04, channel-voice/status nibble clue, value 127

```c

undefined4 PROBE_00022b70(void)

{
  short sVar1;
  undefined1 uVar2;
  uint uVar3;
  uint uVar4;
  uint uVar5;
  undefined2 unaff_r5;
  undefined1 *unaff_r6;
  uint unaff_r8;
  int in_stack_00000004;
  
  uVar3 = FUN_0002dce0();
  uVar4 = FUN_0002dce0();
  uVar2 = FUN_0002dce0();
  uVar5 = FUN_0002dce0();
  sVar1 = (short)unaff_r8;
  if (uVar5 == 4) {
    *unaff_r6 = 3;
    *(undefined2 *)(unaff_r6 + 2) = 0x20;
  }
  else if (uVar5 < 5) {
    if (uVar5 == 1) {
      *unaff_r6 = 3;
    }
    else {
      if (uVar5 != 3) goto LAB_00022c14;
      *unaff_r6 = 4;
    }
  }
  else {
    if (uVar5 != 5) {
LAB_00022c14:
      uVar5 = FUN_0002dce0();
      if (uVar5 == 2) {
        *(short *)(unaff_r6 + 4) = sVar1;
        return 0;
      }
      if (2 < uVar5) {
        if (uVar5 != 3) {
          return 0;
        }
        if (0x3f < unaff_r8) {
          *(short *)(unaff_r6 + 4) = sVar1 + -0x3f;
          return 0;
        }
        *(short *)(unaff_r6 + 4) = sVar1 + 0x41;
        return 0;
      }
      if (uVar5 != 0) {
        if (0x40 < unaff_r8) {
          *(short *)(unaff_r6 + 4) = sVar1 + -0x40;
          return 0;
        }
        *(short *)(unaff_r6 + 4) = 0x80 - sVar1;
        return 0;
      }
      goto LAB_00022c4c;
    }
    *(undefined2 *)(unaff_r6 + 2) = unaff_r5;
    *unaff_r6 = 3;
  }
  uVar5 = FUN_0002dce0();
  if (uVar5 == 2) {
    *(short *)(unaff_r6 + 4) = sVar1;
  }
  else if (uVar5 < 3) {
    if (uVar5 == 0) {
LAB_00022c4c:
      if (uVar3 < uVar4) {
                    /* WARNING: Subroutine does not return */
        FUN_0005a430(((in_stack_00000004 * uVar4 + uVar3 * 0x7f) - uVar3) + 1,0x7f);
      }
                    /* WARNING: Subroutine does not return */
      FUN_0005a430(((uVar3 * 0x7f - uVar3 * in_stack_00000004) - uVar4) + 1,0x7f);
    }
    if (unaff_r8 < 0x41) {
      *(short *)(unaff_r6 + 4) = 0x80 - sVar1;
    }
    else {
      *(short *)(unaff_r6 + 4) = sVar1 + -0x40;
    }
  }
  else if (uVar5 == 3) {
    if (unaff_r8 < 0x40) {
      *(short *)(unaff_r6 + 4) = sVar1 + 0x41;
    }
    else {
      *(short *)(unaff_r6 + 4) = sVar1 + -0x3f;
    }
  }
  FUN_000225a8(uVar2);
  return 0;
}
```

### `FUN_00030730` @ `00030730` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, channel-voice/status nibble clue

```c

void FUN_00030730(int param_1,uint param_2)

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
    uVar1 = FUN_00035b60(param_1,uVar9,param_2);
    if (uVar1 == 0) {
      *(short *)(param_1 + 0x28) = (short)param_2;
    }
    else {
      FUN_00033298(param_1);
      *(short *)(param_1 + 0x28) = (short)param_2;
      FUN_00035e90(param_1);
      iVar2 = FUN_0004beb8(0x280);
      uVar10 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
      if (uVar10 != 0) {
        iVar7 = 0;
        iVar8 = 0;
        puVar11 = *(undefined4 **)(param_1 + 0xc);
LAB_000307a4:
        uVar3 = puVar11[1];
        if (((~param_2 & uVar3 & 0xffff) == 0) && ((*(byte *)((int)puVar11 + 7) & 2) == 0)) {
          uVar16 = (uint)*(byte *)((undefined4 *)*puVar11 + 2);
          pcVar12 = *(char **)*puVar11;
          if (uVar16 == 0xff) {
            for (; *pcVar12 != '\0'; pcVar12 = pcVar12 + 8) {
              if (*pcVar12 == 'h') {
                puVar5 = *(undefined4 **)(pcVar12 + 4);
                goto LAB_000307f4;
              }
            }
          }
          else if (uVar16 != 0) {
            uVar4 = 0;
LAB_000307e6:
            if (pcVar12[uVar4 + uVar16 * 4] != 'h') goto LAB_000307de;
            puVar5 = *(undefined4 **)(pcVar12 + uVar4 * 4);
LAB_000307f4:
            pcVar12 = (char *)*puVar5;
            cVar15 = *pcVar12;
            if (cVar15 == '\0') goto LAB_00030878;
            if (iVar7 == 0) goto LAB_000308b6;
            do {
              while( true ) {
                iVar13 = 0;
                puVar6 = (uint *)(iVar2 + 4);
                while ((((char)puVar6[1] != cVar15 || ((*puVar6 & 0xff0000) != (uVar3 & 0xff0000)))
                       || ((*puVar6 & 0xffff) < (uVar3 & 0xffff)))) {
                  iVar13 = iVar13 + 1;
                  puVar6 = puVar6 + 5;
                  if (iVar13 == iVar7) goto LAB_000308b6;
                }
                if (iVar7 == iVar13) break;
                pcVar12 = pcVar12 + 1;
                cVar15 = *pcVar12;
                if (cVar15 == '\0') goto LAB_0003085c;
              }
LAB_000308b6:
              puVar14 = (undefined2 *)(iVar2 + iVar7 * 0x14);
              iVar7 = iVar7 + 1;
              *puVar14 = (short)puVar5[3];
              puVar14[1] = (short)puVar5[4];
              *(undefined4 *)(puVar14 + 6) = puVar5[2];
              *(char *)(puVar14 + 4) = *pcVar12;
              *(undefined4 *)(puVar14 + 8) = puVar5[1];
              *(uint *)(puVar14 + 2) = uVar3 & 0xffffff;
              pcVar12 = pcVar12 + 1;
              cVar15 = *pcVar12;
            } while ((cVar15 != '\0') && (iVar7 != 0x20));
LAB_0003085c:
            if (uVar10 <= iVar8 + 1U) goto LAB_00030880;
            if (iVar7 == 0x20) goto LAB_000308fc;
            goto LAB_00030868;
          }
        }
LAB_00030878:
        if (iVar8 + 1U < uVar10) goto LAB_00030868;
        goto LAB_00030880;
      }
LAB_00030886:
      FUN_0004bedc(iVar2);
      if ((uVar1 & 0xfd) == 1) {
        FUN_000360c0(param_1,0xf0000,0xff);
      }
      else if (uVar1 == 2) {
        FUN_00033298(param_1);
        FUN_000323bc(param_1);
      }
    }
  }
  return;
LAB_000307de:
  uVar4 = uVar4 + 1;
  if (uVar16 <= uVar4) goto LAB_000308ee;
  goto LAB_000307e6;
LAB_000308ee:
  if (uVar10 <= iVar8 + 1U) {
LAB_00030880:
    if (iVar7 != 0) {
LAB_000308fc:
      iVar8 = iVar2;
      do {
        iVar13 = iVar8 + 0x14;
        FUN_00036498(param_1,*(uint *)(iVar8 + 4) & 0xff0000,uVar9,param_2,iVar8);
        iVar8 = iVar13;
      } while (iVar2 + iVar7 * 0x14 != iVar13);
    }
    goto LAB_00030886;
  }
LAB_00030868:
  iVar8 = iVar8 + 1;
  puVar11 = puVar11 + 2;
  goto LAB_000307a4;
}
```

### `FUN_00031b10` @ `00031b10` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, channel-voice/status nibble clue

```c

void FUN_00031b10(undefined4 param_1,int param_2,undefined4 *param_3)

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
    uVar7 = FUN_00035de8();
    if (param_2 == 0) goto LAB_00031b32;
  }
  else {
    uVar7 = (uint)*(byte *)(param_3[4] + 0x38);
    if (param_2 == 0) goto LAB_00031b32;
    uVar5 = FUN_00035ab8(param_1,param_2,0x62);
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
LAB_00031b32:
  uVar4 = FUN_00035ab8(param_1,param_2,0xc);
  param_3[7] = uVar4;
  if (*(char *)(param_3 + 8) != '\0') {
    bVar2 = FUN_00035ab8(param_1,param_2,0x1d);
    *(byte *)(param_3 + 8) = bVar2;
    if (2 < bVar2) {
      uVar4 = FUN_00035ab8(param_1,param_2,0x1c);
      uVar3 = FUN_00035b58(param_1,param_2,uVar4);
      uVar4 = FUN_00031a74(param_1,param_2,param_3[4],uVar3);
      *(char *)((int)param_3 + 0x21) = (char)uVar4;
      *(char *)((int)param_3 + 0x23) = (char)((uint)uVar4 >> 0x10);
      *(char *)((int)param_3 + 0x22) = (char)((uint)uVar4 >> 8);
      iVar6 = FUN_00035ab8(param_1,param_2,0x26);
      if ((iVar6 == 0) || ((*(byte *)(iVar6 + 0xb) & 0xf) == 0)) {
        bVar2 = FUN_00035ab8(param_1,param_2,0x20);
        *(byte *)((int)param_3 + 0x2f) = *(byte *)((int)param_3 + 0x2f) & 0xf0 | bVar2 & 0xf;
        if ((bVar2 & 0xf) != 0) {
          FUN_0005aef8(param_3 + 9,(int)param_3 + 0x21,3);
          uVar4 = FUN_00035ab8(param_1,param_2,0x23);
          uVar3 = FUN_00035b58(param_1,param_2,uVar4);
          uVar4 = FUN_00031a74(param_1,param_2,param_3[4],uVar3);
          *(char *)((int)param_3 + 0x29) = (char)uVar4;
          *(char *)((int)param_3 + 0x2a) = (char)((uint)uVar4 >> 8);
          *(char *)((int)param_3 + 0x2b) = (char)((uint)uVar4 >> 0x10);
          uVar1 = FUN_00035ab8(param_1,param_2,0x21);
          *(undefined1 *)(param_3 + 10) = uVar1;
          uVar1 = FUN_00035ab8(param_1,param_2,0x22);
          *(undefined1 *)((int)param_3 + 0x2d) = uVar1;
          uVar1 = FUN_00035ab8(param_1,param_2,0x24);
          *(undefined1 *)((int)param_3 + 0x27) = uVar1;
          uVar1 = FUN_00035ab8(param_1,param_2,0x25);
          *(undefined1 *)(param_3 + 0xb) = uVar1;
        }
      }
      else {
        FUN_0004f328(param_3 + 9,iVar6,0xc);
      }
    }
  }
  if (*(char *)(param_3 + 0x12) != '\0') {
    iVar6 = FUN_00035ab8(param_1,param_2,0x30);
    param_3[0x11] = iVar6;
    if (iVar6 != 0) {
      bVar2 = FUN_00035ab8(param_1,param_2,0x32);
      *(byte *)(param_3 + 0x12) = bVar2;
      if (2 < bVar2) {
        bVar2 = FUN_00035ab8(param_1,param_2,0x34);
        *(byte *)((int)param_3 + 0x49) = *(byte *)((int)param_3 + 0x49) & 0xe0 | bVar2 & 0x1f;
        uVar4 = FUN_00035ab8(param_1,param_2,0x31);
        uVar4 = FUN_00035b58(param_1,param_2,uVar4);
        uVar4 = FUN_00031a74(param_1,param_2,param_3[4],uVar4);
        *(char *)((int)param_3 + 0x3e) = (char)uVar4;
        *(char *)((int)param_3 + 0x3f) = (char)((uint)uVar4 >> 8);
        *(char *)(param_3 + 0x10) = (char)((uint)uVar4 >> 0x10);
      }
    }
  }
  if (*(char *)(param_3 + 0x16) != '\0') {
    iVar6 = FUN_00035ab8(param_1,param_2,0x38);
    param_3[0x14] = iVar6;
    if (iVar6 != 0) {
      bVar2 = FUN_00035ab8(param_1,param_2,0x3a);
      *(byte *)(param_3 + 0x16) = bVar2;
      if (2 < bVar2) {
        uVar4 = FUN_00035ab8(param_1,param_2,0x3b);
        param_3[0x15] = uVar4;
        uVar4 = FUN_00035ab8(param_1,param_2,0x39);
        uVar4 = FUN_00035b58(param_1,param_2,uVar4);
        uVar4 = FUN_00031a74(param_1,param_2,param_3[4],uVar4);
        *(char *)((int)param_3 + 0x4a) = (char)uVar4;
        *(char *)((int)param_3 + 0x4b) = (char)((uint)uVar4 >> 8);
        *(char *)(param_3 + 0x13) = (char)((uint)uVar4 >> 0x10);
      }
    }
  }
  if (*(char *)((int)param_3 + 0x3b) != '\0') {
    iVar6 = FUN_00035ab8(param_1,param_2,0x28);
    param_3[0xc] = iVar6;
    if (iVar6 != 0) {
      bVar2 = FUN_00035ab8(param_1,param_2,0x29);
      *(byte *)((int)param_3 + 0x3b) = bVar2;
      if (2 < bVar2) {
        iVar6 = FUN_0003b6b0(param_3[0xc]);
        if (iVar6 == 2) {
          uVar4 = FUN_00035ab8(param_1,param_2,0x5a);
          param_3[0xd] = uVar4;
          uVar4 = FUN_00035ab8(param_1,param_2,0x58);
          uVar4 = FUN_00035b58(param_1,param_2,uVar4);
          uVar4 = FUN_00031a74(param_1,param_2,param_3[4],uVar4);
          *(char *)(param_3 + 0xe) = (char)uVar4;
          *(char *)((int)param_3 + 0x39) = (char)((uint)uVar4 >> 8);
          *(char *)((int)param_3 + 0x3a) = (char)((uint)uVar4 >> 0x10);
        }
        else {
          uVar4 = FUN_00035ab8(param_1,param_2,0x2a);
          uVar3 = FUN_00035b58(param_1,param_2,uVar4);
          uVar1 = FUN_00035ab8(param_1,param_2,0x2b);
          uVar5 = FUN_000319d8(param_1,param_2,param_3[4],uVar3,uVar1);
          *(char *)(param_3 + 0xf) = (char)(uVar5 >> 0x18);
          uVar4 = FUN_00044c94(uVar5 >> 0x10 & 0xff,uVar5 >> 8 & 0xff,uVar5 & 0xff);
          *(char *)(param_3 + 0xe) = (char)uVar4;
          *(char *)((int)param_3 + 0x39) = (char)((uint)uVar4 >> 8);
          *(char *)((int)param_3 + 0x3a) = (char)((uint)uVar4 >> 0x10);
          iVar6 = FUN_00035ab8(param_1,param_2,0x2c);
          *(char *)((int)param_3 + 0x3d) = '\x01' - (iVar6 == 0);
        }
      }
/* ... truncated ... */
```

### `FUN_00037b1c` @ `00037b1c` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, channel-voice/status nibble clue

```c

/* WARNING: Restarted to delay deadcode elimination for space: stack */

void FUN_00037b1c(int param_1,int param_2)

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
  
  uVar2 = FUN_00035ab8(param_2,0,99);
  if ((uVar2 & 0xff) < 3) {
    return;
  }
  uVar11 = *(uint *)(param_1 + 0x38);
  uVar1 = *(undefined1 *)(param_1 + 0x3c);
  local_94 = uVar2;
  local_94 = FUN_00035ab8(param_2,0,0x62);
  if ((local_94 & 0xff) < 0xfd) {
    *(char *)(param_1 + 0x38) = (char)((local_94 & 0xff) * (uVar11 & 0xff) >> 8);
  }
  uVar3 = FUN_00036bf4(param_2,0,*(undefined4 *)(param_1 + 0x39));
  *(char *)(param_1 + 0x39) = (char)uVar3;
  *(char *)(param_1 + 0x3a) = (char)((uint)uVar3 >> 8);
  *(char *)(param_1 + 0x3c) = (char)((uint)uVar3 >> 0x18);
  *(char *)(param_1 + 0x3b) = (char)((uint)uVar3 >> 0x10);
  iVar4 = FUN_0003244c(param_2);
  if (iVar4 == 0) {
    FUN_00037814(param_1,param_2);
  }
  else {
    uVar3 = FUN_0003243c(param_2);
    FUN_00032b50(param_2,&local_c4);
    FUN_0004409c(&local_c4,uVar3,uVar3);
    if (iVar4 != 2) {
      if (iVar4 != 1) {
        FUN_000458e8(2,DAT_00037f38,DAT_00037f3c,DAT_00037f34,DAT_00037f30);
        return;
      }
      iVar4 = FUN_000440d4(&local_94,param_1 + 0x18,&local_c4);
      if (iVar4 == 0) {
        return;
      }
      local_d4 = local_94;
      local_d0 = local_90;
      local_cc = uStack_8c;
      local_c8 = local_88;
      FUN_000448f0(&local_d4);
      FUN_000448f0(&local_d4);
      uVar3 = FUN_000448e4(&local_d4);
      FUN_00044c38(*(undefined1 *)(*(int *)(DAT_00037f1c + 0x10) + 0x40));
                    /* WARNING: Subroutine does not return */
      FUN_0005a430(0x2000,uVar3);
    }
    local_a4 = local_c4;
    local_a0 = (uint *)uStack_c0;
    local_9c = uStack_bc;
    local_98 = local_b8;
    FUN_00033030(param_2,&local_a4,0);
    iVar4 = FUN_000440d4(&local_b4,param_1 + 0x18,&local_a4);
    if (iVar4 == 0) {
      return;
    }
    local_94 = local_b4;
    local_90 = puStack_b0;
    uStack_8c = uStack_ac;
    local_88 = local_a8;
    FUN_00033030(param_2,&local_94,2);
    iVar4 = FUN_000440d4(&local_94,&local_94,&local_c4);
    if (iVar4 == 0) {
      return;
    }
    local_d4 = local_94;
    local_d0 = local_90;
    local_cc = uStack_8c;
    local_c8 = local_88;
    FUN_0004409c(&local_d4,5,5);
    iVar9 = FUN_000448f0(&local_d4);
    iVar10 = FUN_000448f0(&local_d4);
    iVar4 = DAT_00037f1c;
    local_a4 = local_d4;
    local_9c = local_cc;
    if ((int)local_d0 < local_c8) {
      local_a0 = local_d0;
      do {
        local_98 = (int)local_a0 + iVar9 + -1;
        if (local_c8 < local_98) {
          local_98 = local_c8;
        }
        uVar5 = FUN_00035ab8(param_2,0,0x75);
        local_94 = uVar5;
        if ((uVar5 == 0) && (iVar8 = FUN_00044434(&local_a4,param_2 + 0x14), iVar8 != 0)) {
          local_94 = local_94 & 0xffffff00;
          local_90 = &local_a4;
          FUN_00032498(param_2,0x1a,&local_94);
/* ... truncated ... */
```

### `FUN_00045124` @ `00045124` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, channel-voice/status nibble clue

```c

void FUN_00045124(int param_1)

{
  int *piVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  
  if (param_1 != 0) {
    iVar4 = *(int *)(param_1 + 4);
    if (iVar4 != 0) {
      iVar3 = 0;
      do {
        piVar1 = (int *)FUN_00044af8(param_1,iVar3);
        iVar2 = *piVar1;
        *(byte *)(param_1 + 0x14) = *(byte *)(param_1 + 0x14) | 2;
        iVar3 = iVar3 + 1;
        *(uint *)(iVar2 + 8) = *(uint *)(iVar2 + 8) | 0x10000;
      } while (iVar4 != iVar3);
    }
    if ((*(byte *)(param_1 + 0x14) & 3) == 2) {
      FUN_00044f30(param_1);
      *(byte *)(param_1 + 0x14) = *(byte *)(param_1 + 0x14) & 0xfd;
    }
    return;
  }
  FUN_000458e8(3,DAT_000451ac,0xc3,DAT_000451a4,DAT_000451a8,DAT_000451a0,DAT_0004519c);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

### `FUN_0004d190` @ `0004d190` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, channel-voice/status nibble clue, value 127

```c

/* WARNING: Type propagation algorithm not settling */

void FUN_0004d190(undefined4 *param_1)

{
  ushort uVar1;
  int iVar2;
  int iVar3;
  byte bVar4;
  uint uVar5;
  ushort *puVar6;
  int iVar7;
  ushort *puVar8;
  int iVar9;
  byte *pbVar10;
  int iVar11;
  uint uVar12;
  uint uVar13;
  uint uVar14;
  uint uVar15;
  int iVar16;
  int iVar17;
  int iVar18;
  ushort *puVar19;
  ushort *puVar20;
  int iVar21;
  ushort *puVar22;
  byte *pbVar23;
  int local_30;
  int local_2c;
  
  if (*(char *)(param_1 + 8) == '\x12') {
    iVar3 = param_1[2];
    iVar16 = param_1[1];
    uVar5 = (uint)*(byte *)((int)param_1 + 0x21);
    puVar6 = (ushort *)*param_1;
    iVar7 = param_1[3];
    puVar8 = (ushort *)param_1[6];
    iVar9 = param_1[7];
    pbVar10 = (byte *)param_1[4];
    iVar11 = param_1[5];
    if (*(char *)((int)param_1 + 0x22) == '\0') {
      if (pbVar10 == (byte *)0x0) {
        if (uVar5 < 0xfd) {
          if ((0 < iVar3) && (0 < iVar16)) {
            iVar11 = 0;
            puVar22 = puVar8 + iVar16;
            puVar19 = puVar6;
            puVar20 = puVar8;
            do {
              do {
                uVar1 = FUN_00044cdc(*puVar8,*puVar6,uVar5);
                puVar8 = puVar8 + 1;
                *puVar6 = uVar1;
                puVar6 = puVar6 + 1;
              } while (puVar22 != puVar8);
              puVar6 = (ushort *)((int)puVar19 + iVar7);
              puVar8 = (ushort *)((int)puVar20 + iVar9);
              iVar11 = iVar11 + 1;
              puVar22 = (ushort *)((int)puVar22 + iVar9);
              puVar19 = puVar6;
              puVar20 = puVar8;
            } while (iVar3 != iVar11);
          }
        }
        else if (0 < iVar3) {
          iVar11 = 0;
          do {
            FUN_0004f328(puVar6,puVar8,iVar16 << 1);
            iVar11 = iVar11 + 1;
            puVar6 = (ushort *)((int)puVar6 + iVar7);
            puVar8 = (ushort *)((int)puVar8 + iVar9);
          } while (iVar3 != iVar11);
        }
      }
      else if (uVar5 < 0xfd) {
        if ((0 < iVar3) && (0 < iVar16)) {
          puVar22 = puVar8 + iVar16;
          local_30 = 0;
          puVar19 = puVar6;
          puVar20 = puVar8;
          pbVar23 = pbVar10;
          do {
            do {
              uVar1 = FUN_00044cdc(*puVar8,*puVar6,uVar5 * *pbVar10 >> 8);
              puVar8 = puVar8 + 1;
              *puVar6 = uVar1;
              pbVar10 = pbVar10 + 1;
              puVar6 = puVar6 + 1;
            } while (puVar22 != puVar8);
            puVar6 = (ushort *)((int)puVar19 + iVar7);
            puVar8 = (ushort *)((int)puVar20 + iVar9);
            pbVar10 = pbVar23 + iVar11;
            puVar22 = (ushort *)((int)puVar22 + iVar9);
            local_30 = local_30 + 1;
            puVar19 = puVar6;
            puVar20 = puVar8;
            pbVar23 = pbVar10;
          } while (iVar3 != local_30);
        }
      }
      else if ((0 < iVar3) && (0 < iVar16)) {
        iVar21 = 0;
        puVar22 = puVar8 + iVar16;
        puVar19 = puVar6;
        puVar20 = puVar8;
        pbVar23 = pbVar10;
        do {
          do {
            uVar1 = FUN_00044cdc(*puVar8,*puVar6,*pbVar10);
            puVar8 = puVar8 + 1;
            *puVar6 = uVar1;
            pbVar10 = pbVar10 + 1;
            puVar6 = puVar6 + 1;
          } while (puVar22 != puVar8);
          puVar6 = (ushort *)((int)puVar19 + iVar7);
          puVar8 = (ushort *)((int)puVar20 + iVar9);
          pbVar10 = pbVar23 + iVar11;
          puVar22 = (ushort *)((int)puVar22 + iVar9);
          iVar21 = iVar21 + 1;
          puVar19 = puVar6;
          puVar20 = puVar8;
          pbVar23 = pbVar10;
        } while (iVar3 != iVar21);
      }
    }
    else if (0 < iVar3) {
      local_2c = 0;
      if (0 < iVar16) {
LAB_0004d2e8:
        do {
          bVar4 = *(byte *)((int)param_1 + 0x22);
          iVar21 = 0;
          puVar19 = puVar6;
          puVar20 = puVar8;
          if (bVar4 == 3) goto LAB_0004d382;
LAB_0004d2f6:
          if (bVar4 < 4) {
            if (bVar4 == 1) {
/* ... truncated ... */
```

### `FUN_0004dbe4` @ `0004dbe4` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, channel-voice/status nibble clue, value 127

```c

/* WARNING: Control flow encountered bad instruction data */

void FUN_0004dbe4(undefined4 *param_1)

{
  ushort uVar1;
  int iVar2;
  uint uVar3;
  byte bVar4;
  ushort *puVar5;
  int iVar6;
  uint uVar7;
  uint uVar8;
  int iVar9;
  uint uVar10;
  byte *extraout_r2;
  int iVar11;
  ushort *puVar12;
  int iVar13;
  ushort *puVar14;
  int iVar15;
  byte *pbVar16;
  int iVar17;
  uint uVar18;
  int iVar19;
  int extraout_r3;
  int extraout_r3_00;
  byte *pbVar20;
  ushort *puVar21;
  ushort *puVar22;
  uint uVar23;
  int iVar24;
  int local_40;
  int local_38;
  undefined2 local_2c;
  ushort local_2a [3];
  
  if (*(char *)(param_1 + 8) != '\x12') {
    if (*(char *)(param_1 + 8) == '\x1b') {
      iVar11 = param_1[1];
      iVar6 = param_1[2];
      iVar13 = param_1[7];
      uVar23 = (uint)*(byte *)((int)param_1 + 0x21);
      pbVar16 = (byte *)param_1[4];
      puVar14 = (ushort *)*param_1;
      iVar15 = param_1[5];
      iVar17 = param_1[3];
      puVar12 = (ushort *)param_1[6];
      if (*(char *)((int)param_1 + 0x22) == '\0') {
        if (pbVar16 == (byte *)0x0) {
          if (0xfc < uVar23) {
            if (iVar6 < 1) {
              FUN_0004dc14();
              return;
            }
            iVar15 = 0;
            do {
              FUN_0004f328(puVar14,puVar12,iVar11 << 1);
              iVar15 = iVar15 + 1;
              puVar14 = (ushort *)((int)puVar14 + iVar17);
              puVar12 = (ushort *)((int)puVar12 + iVar13);
            } while (iVar6 != iVar15);
            FUN_0004dc14();
            return;
          }
          if (iVar6 < 1) {
            FUN_0004dc14();
            return;
          }
          if (iVar11 < 1) {
            FUN_0004dc14();
            return;
          }
          iVar15 = 0;
          puVar22 = puVar14 + iVar11;
          puVar5 = puVar12;
          puVar21 = puVar14;
          do {
            do {
              uVar3 = FUN_00044cdc(*puVar12 << 8 | *puVar12 >> 8,*puVar14 << 8 | *puVar14 >> 8,
                                   uVar23);
              *puVar14 = (ushort)((uVar3 & 0xff) << 8) | (ushort)(uVar3 >> 8) & 0xff;
              puVar14 = puVar14 + 1;
              puVar12 = puVar12 + 1;
            } while (puVar22 != puVar14);
            puVar14 = (ushort *)((int)puVar21 + iVar17);
            puVar12 = (ushort *)((int)puVar5 + iVar13);
            puVar22 = (ushort *)((int)puVar22 + iVar17);
            iVar15 = iVar15 + 1;
            puVar5 = puVar12;
            puVar21 = puVar14;
          } while (iVar6 != iVar15);
          FUN_0004dc14();
          return;
        }
        if (uVar23 < 0xfd) {
          if (iVar6 < 1) {
            FUN_0004dc14();
            return;
          }
          if (iVar11 < 1) {
            FUN_0004dc14();
            return;
          }
          puVar22 = puVar14 + iVar11;
          local_40 = 0;
          puVar5 = puVar12;
          pbVar20 = pbVar16;
          puVar21 = puVar14;
          do {
            do {
              uVar3 = FUN_00044cdc(*puVar12 << 8 | *puVar12 >> 8,*puVar14 << 8 | *puVar14 >> 8,
                                   uVar23 * *pbVar16 >> 8);
              *puVar14 = (ushort)((uVar3 & 0xff) << 8) | (ushort)(uVar3 >> 8) & 0xff;
              puVar14 = puVar14 + 1;
              puVar12 = puVar12 + 1;
              pbVar16 = pbVar16 + 1;
            } while (puVar22 != puVar14);
            puVar14 = (ushort *)((int)puVar21 + iVar17);
            puVar12 = (ushort *)((int)puVar5 + iVar13);
            puVar22 = (ushort *)((int)puVar22 + iVar17);
            pbVar16 = pbVar20 + iVar15;
            local_40 = local_40 + 1;
            puVar5 = puVar12;
            pbVar20 = pbVar16;
            puVar21 = puVar14;
          } while (iVar6 != local_40);
          FUN_0004dc14();
          return;
        }
        if (iVar6 < 1) {
          FUN_0004dc14();
          return;
        }
        if (iVar11 < 1) {
          FUN_0004dc14();
          return;
        }
        puVar22 = puVar14 + iVar11;
/* ... truncated ... */
```

### `FUN_00053b48` @ `00053b48` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, channel-voice/status nibble clue

```c

void FUN_00053b48(uint param_1)

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
  
  local_44 = FUN_00035ab8(param_1,0,0x7a);
  local_69 = (byte)(((int)(local_44 & 0xff) >> 2 & 1U) << 1) | ~(byte)local_44 & 1 |
             (byte)(((int)(local_44 & 0xff) >> 3 & 1U) << 2) | local_69 & 0xf8;
  local_44 = FUN_00035ab8(param_1,0,0x7b);
  uVar20 = local_44 & 0xff;
  local_44 = FUN_00035ab8(param_1,0,0x7c);
  uVar4 = local_44 << 8;
  local_bc = uVar20 | uVar4;
  local_44 = FUN_00035ab8(param_1,0,0x7d);
  uVar14 = local_44 & 0xff;
  local_6a = (undefined1)local_44;
  local_44 = FUN_00035ab8(param_1,0,0x27);
  bVar3 = local_69;
  uVar15 = local_44 & 0xff;
  uVar21 = (uint)local_69;
  bVar1 = local_69 & 1;
  uVar16 = uVar21 & 1;
  if ((local_69 & 1) == 0) {
    local_d4 = FUN_00035ab8(param_1,0,0x15);
    local_44 = local_d4;
    local_b4 = FUN_00035ab8(param_1,0,0x14);
    local_44 = local_b4;
    local_d8 = FUN_00032cd0(param_1);
  }
  else {
    local_d4 = FUN_00035ab8(param_1,0,0x14);
    local_44 = local_d4;
    local_b4 = FUN_00035ab8(param_1,0,0x15);
    local_44 = local_b4;
    local_d8 = FUN_00032c28(param_1);
  }
  iVar19 = *(int *)(param_1 + 0x18);
  uVar5 = FUN_00035ab8(param_1,0,0x10);
  local_44 = uVar5;
  uVar6 = FUN_00035ab8(param_1,0,0x30);
  local_44 = uVar6;
  local_44 = FUN_00035ab8(param_1,0,0x34);
  if ((int)(local_44 << 0x1e) < 0) {
    uVar5 = uVar5 + uVar6;
  }
  local_68 = FUN_00034258(param_1);
  local_68 = (iVar19 + uVar5) - local_68;
  iVar19 = *(int *)(param_1 + 0x14);
  uVar5 = FUN_00035ab8(param_1,0,0x12);
  local_44 = uVar5;
  uVar6 = FUN_00035ab8(param_1,0,0x30);
  local_44 = uVar6;
  local_44 = FUN_00035ab8(param_1,0,0x34);
  if ((int)(local_44 << 0x1d) < 0) {
    uVar5 = uVar5 + uVar6;
  }
  iVar7 = FUN_00034248(param_1);
  iVar7 = (iVar19 + uVar5) - iVar7;
  local_64 = iVar7;
  if (bVar1 == 0) {
    uVar10 = FUN_00035ab8(param_1,0,1);
    local_44 = uVar10;
    uVar22 = FUN_00035ab8(param_1,0,2);
    uVar5 = (uint)uVar22;
    local_74 = uVar10;
    local_44 = uVar5;
    if ((uVar10 == DAT_000542e0) && (-1 < (int)((uint)*(byte *)(param_1 + 0x2b) << 0x1c))) {
      if (uVar15 == 1) {
LAB_00054510:
        local_60 = 0;
        unaff_r10 = uVar21 & 4;
/* ... truncated ... */
```

### `FUN_00053cde` @ `00053cde` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, channel-voice/status nibble clue

```c

void FUN_00053cde(void)

{
  byte bVar1;
  ushort uVar2;
  byte bVar3;
  byte bVar4;
  byte bVar5;
  int *piVar6;
  int iVar7;
  int iVar8;
  uint uVar9;
  int iVar10;
  undefined4 uVar11;
  int iVar12;
  int iVar13;
  int iVar14;
  int iVar15;
  uint uVar16;
  int *piVar17;
  int unaff_r4;
  int iVar18;
  uint uVar19;
  int iVar20;
  uint uVar21;
  int iVar22;
  uint uVar23;
  int unaff_r6;
  int iVar24;
  uint uVar25;
  int in_stack_00000010;
  undefined4 in_stack_00000018;
  int in_stack_0000001c;
  int iStack00000020;
  int in_stack_00000030;
  ushort in_stack_00000034;
  int in_stack_0000003c;
  int *in_stack_00000040;
  code *pcStack00000048;
  code *pcStack0000004c;
  code *pcStack0000005c;
  code *pcStack00000060;
  code *pcStack00000064;
  code *pcStack00000068;
  code *pcStack00000070;
  int in_stack_0000007c;
  ushort uStack00000084;
  byte bStack00000087;
  int in_stack_00000088;
  int in_stack_0000008c;
  int in_stack_00000090;
  int in_stack_00000094;
  int in_stack_00000098;
  uint in_stack_0000009c;
  undefined4 in_stack_000000a0;
  undefined4 in_stack_000000a4;
  undefined4 in_stack_000000a8;
  int in_stack_000000ac;
  int in_stack_000000b0;
  int in_stack_000000b4;
  undefined4 in_stack_000000b8;
  int *in_stack_000000bc;
  int in_stack_000000c0;
  byte in_stack_000000c4;
  
  iVar13 = unaff_r4 + -1;
  iVar20 = 0;
  iVar18 = 0;
  do {
    if (iVar13 < 0) break;
    iVar20 = iVar20 + 1;
    in_stack_000000c4 = in_stack_000000c4 & 0xfe;
    uStack00000084 = in_stack_00000034;
    iVar13 = FUN_000537c4(in_stack_00000010,&stack0x00000084,iVar13,in_stack_00000018);
    iVar18 = iVar18 + in_stack_000000ac + in_stack_0000001c;
    in_stack_00000034 = uStack00000084;
  } while (iVar13 < (int)(uint)*(ushort *)(*(int *)(in_stack_00000010 + 8) + 0x30));
  bVar3 = bStack00000087;
  bVar1 = bStack00000087 & 4;
  if (iVar20 != 0) {
    iVar18 = iVar18 - in_stack_0000001c;
  }
  if ((bStack00000087 & 1) == 0) {
    FUN_00032c28(in_stack_00000010);
  }
  else {
    FUN_00032cd0(in_stack_00000010);
  }
  FUN_000536f0();
  if (bVar1 == 0) {
    if (in_stack_00000030 != 1) {
      iStack00000020 = 0;
      if (*(short *)(*(int *)(in_stack_00000010 + 8) + 0x30) != 0) {
        do {
          if (iStack00000020 < 0) break;
          in_stack_000000c4 = in_stack_000000c4 | 1;
          uStack00000084 = in_stack_00000034;
          in_stack_000000ac = 0;
          in_stack_000000b0 = 0;
          in_stack_000000bc = (int *)0x0;
          in_stack_000000c0 = 0;
          iVar8 = FUN_000537c4(in_stack_00000010,&stack0x00000084,iStack00000020,in_stack_00000018);
          iVar7 = in_stack_000000c0;
          piVar6 = in_stack_000000bc;
          iVar12 = in_stack_000000b0;
          iVar20 = in_stack_000000ac;
          iVar18 = in_stack_0000008c;
          iVar13 = in_stack_00000088;
          uVar2 = uStack00000084;
          in_stack_00000034 = uStack00000084;
          uVar21 = (uint)bStack00000087;
          bVar1 = bStack00000087 & 1;
          bVar3 = bStack00000087 & 1;
          bVar4 = bStack00000087 & 1;
          bVar5 = bStack00000087 & 1;
          if (in_stack_00000030 == 1) {
            if ((bStack00000087 & 1) != 0) goto LAB_000541f8;
            *in_stack_00000040 = *in_stack_00000040 - in_stack_000000ac;
LAB_00053e18:
            pcStack0000005c = DAT_00053e6c;
            pcStack00000048 = DAT_00053e70;
            pcStack00000068 = DAT_00053e74;
            pcStack00000064 = DAT_00053e78;
            pcStack00000070 = DAT_00053e7c;
            pcStack0000004c = DAT_00053e80;
            pcStack00000060 = DAT_00053e84;
          }
          else {
            if ((bStack00000087 & 1) == 0) goto LAB_00053e18;
LAB_000541f8:
            pcStack0000005c = DAT_000542f4;
            pcStack00000048 = DAT_000542f8;
            pcStack00000068 = DAT_000542fc;
            pcStack00000064 = DAT_00054300;
            pcStack00000070 = DAT_00054304;
            pcStack0000004c = DAT_00054308;
            pcStack00000060 = DAT_0005430c;
          }
          if (in_stack_000000c0 != 0) {
/* ... truncated ... */
```

### `FUN_00053ce0` @ `00053ce0` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, channel-voice/status nibble clue

```c

void FUN_00053ce0(undefined4 param_1,undefined4 param_2,int param_3)

{
  byte bVar1;
  ushort uVar2;
  byte bVar3;
  byte bVar4;
  byte bVar5;
  int iVar6;
  int *piVar7;
  int iVar8;
  int iVar9;
  uint uVar10;
  int iVar11;
  undefined4 uVar12;
  int iVar13;
  int iVar14;
  int iVar15;
  uint uVar16;
  int *piVar17;
  int iVar18;
  uint uVar19;
  int iVar20;
  uint uVar21;
  int iVar22;
  uint uVar23;
  int unaff_r6;
  int iVar24;
  uint uVar25;
  int in_stack_00000010;
  undefined4 in_stack_00000018;
  int in_stack_0000001c;
  int iStack00000020;
  int in_stack_00000030;
  ushort in_stack_00000034;
  int in_stack_0000003c;
  int *in_stack_00000040;
  code *pcStack00000048;
  code *pcStack0000004c;
  code *pcStack0000005c;
  code *pcStack00000060;
  code *pcStack00000064;
  code *pcStack00000068;
  code *pcStack00000070;
  int in_stack_0000007c;
  ushort uStack00000084;
  byte bStack00000087;
  int in_stack_00000088;
  int in_stack_0000008c;
  int in_stack_00000090;
  int in_stack_00000094;
  int in_stack_00000098;
  uint in_stack_0000009c;
  undefined4 in_stack_000000a0;
  undefined4 in_stack_000000a4;
  undefined4 in_stack_000000a8;
  int in_stack_000000ac;
  int in_stack_000000b0;
  int in_stack_000000b4;
  undefined4 in_stack_000000b8;
  int *in_stack_000000bc;
  int in_stack_000000c0;
  byte in_stack_000000c4;
  
  iVar20 = 0;
  iVar18 = 0;
  do {
    if (param_3 < 0) break;
    iVar20 = iVar20 + 1;
    in_stack_000000c4 = in_stack_000000c4 & 0xfe;
    uStack00000084 = in_stack_00000034;
    param_3 = FUN_000537c4(in_stack_00000010,&stack0x00000084,param_3,in_stack_00000018);
    iVar18 = iVar18 + in_stack_000000ac + in_stack_0000001c;
    in_stack_00000034 = uStack00000084;
  } while (param_3 < (int)(uint)*(ushort *)(*(int *)(in_stack_00000010 + 8) + 0x30));
  bVar3 = bStack00000087;
  bVar1 = bStack00000087 & 4;
  if (iVar20 != 0) {
    iVar18 = iVar18 - in_stack_0000001c;
  }
  if ((bStack00000087 & 1) == 0) {
    FUN_00032c28(in_stack_00000010);
  }
  else {
    FUN_00032cd0(in_stack_00000010);
  }
  FUN_000536f0();
  if (bVar1 == 0) {
    if (in_stack_00000030 != 1) {
      iStack00000020 = 0;
      if (*(short *)(*(int *)(in_stack_00000010 + 8) + 0x30) != 0) {
        do {
          if (iStack00000020 < 0) break;
          in_stack_000000c4 = in_stack_000000c4 | 1;
          uStack00000084 = in_stack_00000034;
          in_stack_000000ac = 0;
          in_stack_000000b0 = 0;
          in_stack_000000bc = (int *)0x0;
          in_stack_000000c0 = 0;
          iVar9 = FUN_000537c4(in_stack_00000010,&stack0x00000084,iStack00000020,in_stack_00000018);
          iVar8 = in_stack_000000c0;
          piVar7 = in_stack_000000bc;
          iVar13 = in_stack_000000b0;
          iVar6 = in_stack_000000ac;
          iVar20 = in_stack_0000008c;
          iVar18 = in_stack_00000088;
          uVar2 = uStack00000084;
          in_stack_00000034 = uStack00000084;
          uVar21 = (uint)bStack00000087;
          bVar1 = bStack00000087 & 1;
          bVar3 = bStack00000087 & 1;
          bVar4 = bStack00000087 & 1;
          bVar5 = bStack00000087 & 1;
          if (in_stack_00000030 == 1) {
            if ((bStack00000087 & 1) != 0) goto LAB_000541f8;
            *in_stack_00000040 = *in_stack_00000040 - in_stack_000000ac;
LAB_00053e18:
            pcStack0000005c = DAT_00053e6c;
            pcStack00000048 = DAT_00053e70;
            pcStack00000068 = DAT_00053e74;
            pcStack00000064 = DAT_00053e78;
            pcStack00000070 = DAT_00053e7c;
            pcStack0000004c = DAT_00053e80;
            pcStack00000060 = DAT_00053e84;
          }
          else {
            if ((bStack00000087 & 1) == 0) goto LAB_00053e18;
LAB_000541f8:
            pcStack0000005c = DAT_000542f4;
            pcStack00000048 = DAT_000542f8;
            pcStack00000068 = DAT_000542fc;
            pcStack00000064 = DAT_00054300;
            pcStack00000070 = DAT_00054304;
            pcStack0000004c = DAT_00054308;
            pcStack00000060 = DAT_0005430c;
          }
          if (in_stack_000000c0 != 0) {
            iVar15 = in_stack_000000b0 - in_stack_000000b4;
            iVar24 = 0;
/* ... truncated ... */
```

### `FUN_00053d5c` @ `00053d5c` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, channel-voice/status nibble clue

```c

void FUN_00053d5c(void)

{
  byte bVar1;
  ushort uVar2;
  byte bVar3;
  byte bVar4;
  byte bVar5;
  int iVar6;
  int iVar7;
  int *piVar8;
  int iVar9;
  int iVar10;
  uint uVar11;
  int iVar12;
  undefined4 uVar13;
  int iVar14;
  int iVar15;
  int iVar16;
  uint uVar17;
  int iVar18;
  int *piVar19;
  int unaff_r4;
  uint uVar20;
  uint uVar21;
  int iVar22;
  uint uVar23;
  int unaff_r6;
  int iVar24;
  uint uVar25;
  uint unaff_r7;
  int unaff_r10;
  int in_stack_00000010;
  undefined4 in_stack_00000018;
  int in_stack_0000001c;
  int iStack00000020;
  int in_stack_00000030;
  ushort in_stack_00000034;
  int in_stack_0000003c;
  int *in_stack_00000040;
  code *pcStack00000048;
  code *pcStack0000004c;
  code *pcStack0000005c;
  code *pcStack00000060;
  code *pcStack00000064;
  code *pcStack00000068;
  code *pcStack00000070;
  int in_stack_0000007c;
  ushort uStack00000084;
  byte bStack00000087;
  int in_stack_00000088;
  int in_stack_0000008c;
  int in_stack_00000090;
  int in_stack_00000094;
  int in_stack_00000098;
  uint in_stack_0000009c;
  undefined4 in_stack_000000a0;
  undefined4 in_stack_000000a4;
  undefined4 in_stack_000000a8;
  int in_stack_000000ac;
  int in_stack_000000b0;
  int in_stack_000000b4;
  undefined4 in_stack_000000b8;
  int *in_stack_000000bc;
  int in_stack_000000c0;
  byte in_stack_000000c4;
  
  FUN_00032cd0(in_stack_00000010);
  FUN_000536f0();
  if (unaff_r10 == 0) {
    if (in_stack_00000030 != 1) {
      iStack00000020 = 0;
      if (*(short *)(*(int *)(in_stack_00000010 + 8) + 0x30) != 0) {
        do {
          if (iStack00000020 < 0) break;
          in_stack_000000c4 = in_stack_000000c4 | 1;
          uStack00000084 = in_stack_00000034;
          in_stack_000000ac = 0;
          in_stack_000000b0 = 0;
          in_stack_000000bc = (int *)0x0;
          in_stack_000000c0 = 0;
          iVar10 = FUN_000537c4(in_stack_00000010,&stack0x00000084,iStack00000020,in_stack_00000018)
          ;
          iVar9 = in_stack_000000c0;
          piVar8 = in_stack_000000bc;
          iVar14 = in_stack_000000b0;
          iVar7 = in_stack_000000ac;
          iVar6 = in_stack_0000008c;
          iVar18 = in_stack_00000088;
          uVar2 = uStack00000084;
          in_stack_00000034 = uStack00000084;
          uVar21 = (uint)bStack00000087;
          bVar1 = bStack00000087 & 1;
          bVar3 = bStack00000087 & 1;
          bVar4 = bStack00000087 & 1;
          bVar5 = bStack00000087 & 1;
          if (in_stack_00000030 == 1) {
            if ((bStack00000087 & 1) != 0) goto LAB_000541f8;
            *in_stack_00000040 = *in_stack_00000040 - in_stack_000000ac;
LAB_00053e18:
            pcStack0000005c = DAT_00053e6c;
            pcStack00000048 = DAT_00053e70;
            pcStack00000068 = DAT_00053e74;
            pcStack00000064 = DAT_00053e78;
            pcStack00000070 = DAT_00053e7c;
            pcStack0000004c = DAT_00053e80;
            pcStack00000060 = DAT_00053e84;
          }
          else {
            if ((bStack00000087 & 1) == 0) goto LAB_00053e18;
LAB_000541f8:
            pcStack0000005c = DAT_000542f4;
            pcStack00000048 = DAT_000542f8;
            pcStack00000068 = DAT_000542fc;
            pcStack00000064 = DAT_00054300;
            pcStack00000070 = DAT_00054304;
            pcStack0000004c = DAT_00054308;
            pcStack00000060 = DAT_0005430c;
          }
          if (in_stack_000000c0 != 0) {
            iVar16 = in_stack_000000b0 - in_stack_000000b4;
            iVar24 = 0;
            piVar19 = in_stack_000000bc;
            do {
              while ((*(byte *)(piVar19 + 5) & 1) != 0) {
                iVar15 = piVar19[3];
                piVar19 = piVar19 + 6;
                iVar16 = iVar16 - iVar15;
                if (piVar19 == in_stack_000000bc + in_stack_000000c0 * 6) goto LAB_00053ea2;
              }
              iVar15 = piVar19[4];
              piVar19 = piVar19 + 6;
              iVar24 = iVar24 + iVar15;
            } while (piVar19 != in_stack_000000bc + in_stack_000000c0 * 6);
LAB_00053ea2:
            iVar22 = 0;
            piVar19 = in_stack_000000bc;
            do {
              if ((*(byte *)(piVar19 + 5) & 1) == 0) {
/* ... truncated ... */
```

### `FUN_00053d90` @ `00053d90` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, channel-voice/status nibble clue

```c

void FUN_00053d90(void)

{
  byte bVar1;
  ushort uVar2;
  byte bVar3;
  byte bVar4;
  byte bVar5;
  int iVar6;
  int iVar7;
  int *piVar8;
  int iVar9;
  int iVar10;
  uint uVar11;
  int iVar12;
  undefined4 uVar13;
  int iVar14;
  int iVar15;
  int in_r3;
  int iVar16;
  uint uVar17;
  int iVar18;
  int *piVar19;
  uint uVar20;
  uint uVar21;
  int iVar22;
  uint uVar23;
  int unaff_r6;
  int iVar24;
  uint uVar25;
  int in_stack_00000010;
  undefined4 in_stack_00000018;
  int in_stack_0000001c;
  int in_stack_00000020;
  int in_stack_00000030;
  ushort in_stack_00000034;
  int in_stack_0000003c;
  int *in_stack_00000040;
  code *pcStack00000048;
  code *pcStack0000004c;
  code *pcStack0000005c;
  code *pcStack00000060;
  code *pcStack00000064;
  code *pcStack00000068;
  code *pcStack00000070;
  int in_stack_0000007c;
  ushort uStack00000084;
  byte bStack00000087;
  int in_stack_00000088;
  int in_stack_0000008c;
  int in_stack_00000090;
  int in_stack_00000094;
  int in_stack_00000098;
  uint in_stack_0000009c;
  undefined4 in_stack_000000a0;
  undefined4 in_stack_000000a4;
  undefined4 in_stack_000000a8;
  int in_stack_000000ac;
  int in_stack_000000b0;
  int in_stack_000000b4;
  undefined4 in_stack_000000b8;
  int *in_stack_000000bc;
  int in_stack_000000c0;
  byte in_stack_000000c4;
  
  if (in_stack_00000020 < in_r3) {
    do {
      if (in_stack_00000020 < 0) break;
      in_stack_000000c4 = in_stack_000000c4 | 1;
      uStack00000084 = in_stack_00000034;
      in_stack_000000ac = 0;
      in_stack_000000b0 = 0;
      in_stack_000000bc = (int *)0x0;
      in_stack_000000c0 = 0;
      iVar10 = FUN_000537c4(in_stack_00000010,&stack0x00000084,in_stack_00000020,in_stack_00000018);
      iVar9 = in_stack_000000c0;
      piVar8 = in_stack_000000bc;
      iVar14 = in_stack_000000b0;
      iVar7 = in_stack_000000ac;
      iVar6 = in_stack_0000008c;
      iVar18 = in_stack_00000088;
      uVar2 = uStack00000084;
      in_stack_00000034 = uStack00000084;
      uVar21 = (uint)bStack00000087;
      bVar1 = bStack00000087 & 1;
      bVar3 = bStack00000087 & 1;
      bVar4 = bStack00000087 & 1;
      bVar5 = bStack00000087 & 1;
      if (in_stack_00000030 == 1) {
        if ((bStack00000087 & 1) != 0) goto LAB_000541f8;
        *in_stack_00000040 = *in_stack_00000040 - in_stack_000000ac;
LAB_00053e18:
        pcStack0000005c = DAT_00053e6c;
        pcStack00000048 = DAT_00053e70;
        pcStack00000068 = DAT_00053e74;
        pcStack00000064 = DAT_00053e78;
        pcStack00000070 = DAT_00053e7c;
        pcStack0000004c = DAT_00053e80;
        pcStack00000060 = DAT_00053e84;
      }
      else {
        if ((bStack00000087 & 1) == 0) goto LAB_00053e18;
LAB_000541f8:
        pcStack0000005c = DAT_000542f4;
        pcStack00000048 = DAT_000542f8;
        pcStack00000068 = DAT_000542fc;
        pcStack00000064 = DAT_00054300;
        pcStack00000070 = DAT_00054304;
        pcStack0000004c = DAT_00054308;
        pcStack00000060 = DAT_0005430c;
      }
      if (in_stack_000000c0 != 0) {
        iVar16 = in_stack_000000b0 - in_stack_000000b4;
        iVar24 = 0;
        piVar19 = in_stack_000000bc;
        do {
          while ((*(byte *)(piVar19 + 5) & 1) != 0) {
            iVar15 = piVar19[3];
            piVar19 = piVar19 + 6;
            iVar16 = iVar16 - iVar15;
            if (piVar19 == in_stack_000000bc + in_stack_000000c0 * 6) goto LAB_00053ea2;
          }
          iVar15 = piVar19[4];
          piVar19 = piVar19 + 6;
          iVar24 = iVar24 + iVar15;
        } while (piVar19 != in_stack_000000bc + in_stack_000000c0 * 6);
LAB_00053ea2:
        iVar22 = 0;
        piVar19 = in_stack_000000bc;
        do {
          if ((*(byte *)(piVar19 + 5) & 1) == 0) {
            if (iVar24 == 0) {
              FUN_000458e8(3,DAT_000542f0,0x16f,DAT_000542ec);
              do {
                    /* WARNING: Do nothing block with infinite loop */
              } while( true );
            }
                    /* WARNING: Subroutine does not return */
            FUN_0005a430(iVar16,iVar24,iVar15,piVar19[4]);
/* ... truncated ... */
```

### `FUN_00053d98` @ `00053d98` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, channel-voice/status nibble clue

```c

void FUN_00053d98(void)

{
  byte bVar1;
  ushort uVar2;
  byte bVar3;
  byte bVar4;
  byte bVar5;
  int iVar6;
  int iVar7;
  int *piVar8;
  int iVar9;
  int iVar10;
  uint uVar11;
  int iVar12;
  undefined4 uVar13;
  int iVar14;
  int iVar15;
  int iVar16;
  uint uVar17;
  int iVar18;
  int *piVar19;
  uint uVar20;
  uint uVar21;
  int iVar22;
  uint uVar23;
  int unaff_r6;
  int iVar24;
  uint uVar25;
  int in_stack_00000010;
  undefined4 in_stack_00000018;
  int in_stack_0000001c;
  int in_stack_00000020;
  int in_stack_00000030;
  ushort in_stack_00000034;
  int in_stack_0000003c;
  int *in_stack_00000040;
  code *pcStack00000048;
  code *pcStack0000004c;
  code *pcStack0000005c;
  code *pcStack00000060;
  code *pcStack00000064;
  code *pcStack00000068;
  code *pcStack00000070;
  int in_stack_0000007c;
  ushort uStack00000084;
  byte bStack00000087;
  int in_stack_00000088;
  int in_stack_0000008c;
  int in_stack_00000090;
  int in_stack_00000094;
  int in_stack_00000098;
  uint in_stack_0000009c;
  undefined4 in_stack_000000a0;
  undefined4 in_stack_000000a4;
  undefined4 in_stack_000000a8;
  int in_stack_000000ac;
  int in_stack_000000b0;
  int in_stack_000000b4;
  undefined4 in_stack_000000b8;
  int *in_stack_000000bc;
  int in_stack_000000c0;
  byte in_stack_000000c4;
  
  do {
    if (in_stack_00000020 < 0) break;
    in_stack_000000c4 = in_stack_000000c4 | 1;
    uStack00000084 = in_stack_00000034;
    in_stack_000000ac = 0;
    in_stack_000000b0 = 0;
    in_stack_000000bc = (int *)0x0;
    in_stack_000000c0 = 0;
    iVar10 = FUN_000537c4(in_stack_00000010,&stack0x00000084,in_stack_00000020,in_stack_00000018);
    iVar9 = in_stack_000000c0;
    piVar8 = in_stack_000000bc;
    iVar14 = in_stack_000000b0;
    iVar7 = in_stack_000000ac;
    iVar6 = in_stack_0000008c;
    iVar18 = in_stack_00000088;
    uVar2 = uStack00000084;
    in_stack_00000034 = uStack00000084;
    uVar21 = (uint)bStack00000087;
    bVar1 = bStack00000087 & 1;
    bVar3 = bStack00000087 & 1;
    bVar4 = bStack00000087 & 1;
    bVar5 = bStack00000087 & 1;
    if (in_stack_00000030 == 1) {
      if ((bStack00000087 & 1) != 0) goto LAB_000541f8;
      *in_stack_00000040 = *in_stack_00000040 - in_stack_000000ac;
LAB_00053e18:
      pcStack0000005c = DAT_00053e6c;
      pcStack00000048 = DAT_00053e70;
      pcStack00000068 = DAT_00053e74;
      pcStack00000064 = DAT_00053e78;
      pcStack00000070 = DAT_00053e7c;
      pcStack0000004c = DAT_00053e80;
      pcStack00000060 = DAT_00053e84;
    }
    else {
      if ((bStack00000087 & 1) == 0) goto LAB_00053e18;
LAB_000541f8:
      pcStack0000005c = DAT_000542f4;
      pcStack00000048 = DAT_000542f8;
      pcStack00000068 = DAT_000542fc;
      pcStack00000064 = DAT_00054300;
      pcStack00000070 = DAT_00054304;
      pcStack0000004c = DAT_00054308;
      pcStack00000060 = DAT_0005430c;
    }
    if (in_stack_000000c0 != 0) {
      iVar16 = in_stack_000000b0 - in_stack_000000b4;
      iVar24 = 0;
      piVar19 = in_stack_000000bc;
      do {
        while ((*(byte *)(piVar19 + 5) & 1) != 0) {
          iVar15 = piVar19[3];
          piVar19 = piVar19 + 6;
          iVar16 = iVar16 - iVar15;
          if (piVar19 == in_stack_000000bc + in_stack_000000c0 * 6) goto LAB_00053ea2;
        }
        iVar15 = piVar19[4];
        piVar19 = piVar19 + 6;
        iVar24 = iVar24 + iVar15;
      } while (piVar19 != in_stack_000000bc + in_stack_000000c0 * 6);
LAB_00053ea2:
      iVar22 = 0;
      piVar19 = in_stack_000000bc;
      do {
        if ((*(byte *)(piVar19 + 5) & 1) == 0) {
          if (iVar24 == 0) {
            FUN_000458e8(3,DAT_000542f0,0x16f,DAT_000542ec);
            do {
                    /* WARNING: Do nothing block with infinite loop */
            } while( true );
          }
                    /* WARNING: Subroutine does not return */
          FUN_0005a430(iVar16,iVar24,iVar15,piVar19[4]);
        }
        iVar22 = iVar22 + 1;
/* ... truncated ... */
```

### `FUN_000544ec` @ `000544ec` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, observed event code 0x02, channel-voice/status nibble clue

```c

void FUN_000544ec(undefined4 param_1,undefined4 param_2)

{
  byte bVar1;
  ushort uVar2;
  byte bVar3;
  byte bVar4;
  int iVar5;
  int *piVar6;
  int iVar7;
  uint uVar8;
  undefined4 uVar9;
  int iVar10;
  int iVar11;
  int iVar12;
  int iVar13;
  int extraout_r2;
  int iVar14;
  uint uVar15;
  int iVar16;
  int *piVar17;
  int extraout_r3;
  uint uVar18;
  uint unaff_r4;
  uint uVar19;
  int iVar20;
  uint uVar21;
  int iVar22;
  uint uVar23;
  int unaff_r6;
  uint unaff_r7;
  uint unaff_r10;
  int unaff_r11;
  undefined8 uVar24;
  int in_stack_00000010;
  undefined4 in_stack_00000018;
  int in_stack_0000001c;
  int iStack00000020;
  uint in_stack_00000024;
  int in_stack_00000030;
  ushort in_stack_00000034;
  int in_stack_0000003c;
  int *piStack00000040;
  int in_stack_00000044;
  code *pcStack00000048;
  code *pcStack0000004c;
  int in_stack_00000058;
  code *pcStack0000005c;
  code *pcStack00000060;
  code *pcStack00000064;
  code *pcStack00000068;
  code *pcStack00000070;
  int in_stack_00000074;
  int in_stack_0000007c;
  ushort uStack00000084;
  byte bStack00000087;
  int in_stack_00000088;
  int in_stack_0000008c;
  int iStack00000090;
  int in_stack_00000094;
  int in_stack_00000098;
  uint in_stack_0000009c;
  undefined4 in_stack_000000a0;
  undefined4 in_stack_000000a4;
  undefined4 in_stack_000000a8;
  int in_stack_000000ac;
  int in_stack_000000b0;
  int in_stack_000000b4;
  undefined4 in_stack_000000b8;
  int *in_stack_000000bc;
  int in_stack_000000c0;
  byte in_stack_000000c4;
  
  uVar24 = CONCAT44(param_2,param_1);
  iStack00000090 = 0;
  if (unaff_r11 == 0) {
    if (-1 < (int)(unaff_r7 << 0x1d)) goto LAB_000545a4;
    piStack00000040 = &stack0x00000088;
    unaff_r4 = 0;
  }
  else {
    unaff_r4 = (uint)*(ushort *)(*(int *)(in_stack_00000010 + 8) + 0x30);
    if ((unaff_r7 & 4) == 0) {
LAB_0005457c:
      unaff_r10 = unaff_r7 & 4;
      piStack00000040 = &stack0x00000088;
      if (unaff_r4 != 0) {
        FUN_00053ce0((int)uVar24,(int)((ulonglong)uVar24 >> 0x20),0,0);
      }
      FUN_00053d5c();
      piStack00000040 = &stack0x00000088;
      FUN_00053d98();
LAB_000545a4:
      piStack00000040 = &stack0x00000088;
      uVar24 = FUN_00053d90();
      piStack00000040 = &stack0x0000008c;
      if (unaff_r4 != 0) {
        FUN_00053ce0((int)uVar24,(int)((ulonglong)uVar24 >> 0x20),0);
      }
    }
    else {
      piStack00000040 = &stack0x00000088;
      uVar24 = FUN_00053cde();
      iStack00000090 = 0;
      unaff_r10 = unaff_r7 & 4;
      unaff_r4 = (uint)*(ushort *)(*(int *)(in_stack_00000010 + 8) + 0x30);
      if ((unaff_r7 & 4) != 0) {
        piStack00000040 = &stack0x0000008c;
        unaff_r11 = 1;
        uVar24 = FUN_00053cde();
        goto LAB_0005457c;
      }
      if (unaff_r4 != 0) {
        piStack00000040 = &stack0x0000008c;
        FUN_00053ce0((int)uVar24,(int)((ulonglong)uVar24 >> 0x20),0,1);
        iVar13 = extraout_r2;
        iVar16 = extraout_r3;
        goto LAB_0005453a;
      }
      piStack00000040 = &stack0x0000008c;
      unaff_r11 = 1;
    }
    uVar9 = FUN_00032c28(in_stack_00000010);
    FUN_000536f0(unaff_r11,uVar9,unaff_r4,0);
    if (unaff_r10 == 0) {
      if (in_stack_00000030 != 1) {
        iStack00000020 = 0;
        in_stack_00000074 = unaff_r6;
        if (*(short *)(*(int *)(in_stack_00000010 + 8) + 0x30) != 0) {
          while (-1 < iStack00000020) {
            in_stack_000000c4 = in_stack_000000c4 | 1;
            uStack00000084 = in_stack_00000034;
            in_stack_000000ac = 0;
            in_stack_000000b0 = 0;
            in_stack_000000bc = (int *)0x0;
            in_stack_000000c0 = 0;
            in_stack_00000044 =
                 FUN_000537c4(in_stack_00000010,&stack0x00000084,iStack00000020,in_stack_00000018);
            iVar7 = in_stack_000000c0;
/* ... truncated ... */
```

### `FUN_0005e274` @ `0005e274` score `46`

- reasons: event/CIN byte offset 4, payload byte offset 8, channel-voice/status nibble clue, value 127

```c

int * FUN_0005e274(undefined4 *param_1,uint param_2)

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
LAB_0005e434:
      *param_1 = 0xc;
      return (int *)0x0;
    }
    FUN_0005e7d8();
    uVar17 = 0x10;
    iVar9 = 0x18;
    uVar16 = 2;
  }
  else {
    uVar17 = uVar16 & 0xfffffff8;
    if (((int)uVar17 < 0) || (uVar17 < param_2)) goto LAB_0005e434;
    FUN_0005e7d8();
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
      else if (DAT_0005e7d4 < uVar5) {
        uVar5 = 0x7f;
        uVar15 = 0x7e;
        iVar9 = 0x3f8;
      }
      else {
        uVar15 = (uVar16 >> 0x12) + 0x7c;
        uVar5 = (uVar16 >> 0x12) + 0x7d;
        iVar9 = uVar5 * 8;
      }
      iVar14 = *(int *)(DAT_0005e5c4 + iVar9 + 4);
      do {
        iVar18 = iVar14;
        uVar16 = uVar5;
        if (DAT_0005e5c4 + iVar9 + -8 == iVar18) goto LAB_0005e340;
        uVar2 = *(uint *)(iVar18 + 4) & 0xfffffffc;
        uVar16 = uVar15;
        if (0xf < (int)(uVar2 - uVar17)) goto LAB_0005e340;
        iVar14 = *(int *)(iVar18 + 0xc);
      } while ((int)(uVar2 - uVar17) < 0);
      iVar9 = *(int *)(iVar18 + 8);
      *(int *)(iVar9 + 0xc) = iVar14;
      *(int *)(iVar14 + 8) = iVar9;
      goto LAB_0005e2ba;
    }
    uVar16 = uVar16 >> 3;
    iVar9 = uVar17 + 8;
  }
  iVar9 = DAT_0005e5c4 + iVar9;
  iVar18 = *(int *)(iVar9 + 4);
  if (iVar18 == iVar9 + -8) {
    iVar18 = *(int *)(iVar9 + 0xc);
    uVar16 = uVar16 + 2;
    if (iVar9 == iVar18) {
LAB_0005e340:
      uVar5 = DAT_0005e5c4;
      iVar18 = *(int *)(DAT_0005e5c4 + 0x10);
      iVar9 = DAT_0005e5c4 + 8;
      if (iVar18 == iVar9) {
        uVar15 = *(uint *)(DAT_0005e5c4 + 4);
      }
      else {
        uVar13 = *(uint *)(iVar18 + 4);
        uVar2 = uVar13 & 0xfffffffc;
        uVar15 = uVar2 - uVar17;
        if (0xf < (int)uVar15) {
          iVar14 = iVar18 + uVar17;
          *(uint *)(iVar18 + 4) = uVar17 | 1;
          *(int *)(uVar5 + 0x10) = iVar14;
          *(int *)(uVar5 + 0x14) = iVar14;
          *(int *)(iVar14 + 0xc) = iVar9;
          *(int *)(iVar14 + 8) = iVar9;
          *(uint *)(iVar14 + 4) = uVar15 | 1;
          *(uint *)(iVar18 + uVar2) = uVar15;
          FUN_0005e7e8(param_1);
          return (int *)(iVar18 + 8);
        }
        *(int *)(DAT_0005e5c4 + 0x10) = iVar9;
        *(int *)(uVar5 + 0x14) = iVar9;
        if (-1 < (int)uVar15) goto LAB_0005e2ba;
        uVar15 = *(uint *)(uVar5 + 4);
        if (uVar2 < 0x200) {
          uVar15 = uVar15 | 1 << (uVar13 >> 5 & 0xff);
          iVar14 = (uVar13 & 0xfffffff8) + uVar5;
          iVar9 = *(int *)(iVar14 + 8);
          *(uint *)(uVar5 + 4) = uVar15;
          *(int *)(iVar18 + 0xc) = iVar14;
          *(int *)(iVar18 + 8) = iVar9;
          *(int *)(iVar14 + 8) = iVar18;
          *(int *)(iVar9 + 0xc) = iVar18;
        }
        else {
          uVar7 = uVar13 >> 9;
/* ... truncated ... */
```

### `FUN_00003914` @ `00003914` score `40`

- reasons: event/CIN byte offset 4, payload byte offset 8, channel-voice/status nibble clue

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
/* ... truncated ... */
```

### `FUN_00004f2c` @ `00004f2c` score `40`

- reasons: event/CIN byte offset 4, payload byte offset 8, channel-voice/status nibble clue

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_00004f2c(undefined4 *param_1,char *param_2)

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
  *puVar8 = &DAT_0000a500;
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
  FUN_00004f20((int)param_2[0x12],param_2[0x11],param_1);
  FUN_00004f20((int)*(char *)(iVar9 + 0x24),*(undefined1 *)(iVar9 + 0x22),param_1);
  FUN_00004f20((int)*(char *)(iVar9 + 0x25),*(undefined1 *)(iVar9 + 0x23),param_1);
  *param_1 = 0x475054;
  return 0;
}
```

### `FUN_00005808` @ `00005808` score `40`

- reasons: event/CIN byte offset 4, payload byte offset 8, channel-voice/status nibble clue

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

### `FUN_00005b00` @ `00005b00` score `40`

- reasons: event/CIN byte offset 4, payload byte offset 8, channel-voice/status nibble clue

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_00005b00(int param_1,uint param_2,int param_3)

{
  uint uVar1;
  char cVar2;
  int iVar3;
  int local_1c;
  
  *(char *)(param_1 + 0x34) = **(char **)(param_1 + 4) << 1;
  _DAT_407effb0 = (short)DAT_00005cac;
  FUN_00005138(6,*(undefined4 *)(param_1 + 8));
  _DAT_407ec180 = 0xa5;
  DAT_407ec100 = 0x10;
  FUN_00005138(3,*(undefined4 *)(param_1 + 8));
  cVar2 = '\0';
  if (**(char **)(param_1 + 4) != '\0') {
    FUN_00008598((int)(*(char **)(param_1 + 4))[0x11]);
    cVar2 = **(char **)(param_1 + 4);
  }
  iVar3 = (param_2 & 0xfffffc00) + 0xbdf00000;
  *(int *)(param_1 + 0x28) = iVar3;
  *(int *)(param_1 + 0x30) = param_3;
  DAT_407ec104 = 0;
  _DAT_407ec110 = (undefined2)((uint)iVar3 >> 0x10);
  uVar1 = param_3 * 0x400 + -1 + iVar3;
  _DAT_407ec108 = (undefined2)iVar3;
  _DAT_407ec120 = uVar1 >> 0x10;
  _DAT_407ec118 = (undefined2)uVar1;
  DAT_407ec114 = 0x84;
  if (cVar2 == '\0') {
    param_3 = param_3 * *(int *)(param_1 + 0x20);
    iVar3 = param_3;
    while (-1 < _DAT_407ec12c << 0x19) {
      if (iVar3 == 0) goto LAB_00005bda;
      iVar3 = iVar3 + -1;
    }
    DAT_407ec114 = 0;
    while (_DAT_407ec12c << 0x19 < 0) {
      if (param_3 == 0) {
LAB_00005bda:
        FUN_00005244(param_1);
        return 0x14;
      }
      param_3 = param_3 + -1;
    }
    if ((_DAT_407ec1f0 & 0x11) != 0) {
      FUN_00005244(param_1);
      return 0x19;
    }
    local_1c = 0x4b00;
    _DAT_407ec180 = 0xa5;
    DAT_407ec100 = 8;
    FUN_00005138(0x10,*(undefined4 *)(param_1 + 8));
    _DAT_407effb0 = (short)DAT_00005cb0;
    for (; (_DAT_407effb0 != 0 && (local_1c != 0)); local_1c = local_1c + -1) {
    }
  }
  return 0;
}
```

### `FUN_00006360` @ `00006360` score `40`

- reasons: event/CIN byte offset 4, payload byte offset 8, channel-voice/status nibble clue

```c

void FUN_00006360(int param_1)

{
  byte bVar1;
  undefined4 uVar2;
  int iVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  short sVar7;
  code *pcVar8;
  undefined4 *puVar9;
  
  puVar9 = *(undefined4 **)(*(int *)(param_1 + 0x6c) + 0x24);
  iVar3 = *(int *)puVar9[1];
  *(undefined2 *)(iVar3 + 0xe) = 1;
  if (DAT_20005f3c == '\x01') {
    *(undefined2 *)(iVar3 + 0xc) = 1;
    *(undefined4 *)(iVar3 + 4) = 0x20005f40;
  }
  else {
    *(byte *)(iVar3 + 3) = *(byte *)(iVar3 + 3) & 0xf3 | 8;
    bVar1 = *(byte *)(param_1 + 6);
    *(undefined2 *)(iVar3 + 0xc) = *(undefined2 *)(param_1 + 8);
    if ((((bVar1 != 9) && ((~bVar1 & 3) == 0)) && (*(char *)(param_1 + 0x84) != '\0')) &&
       (-1 < *(char *)(param_1 + 0x20))) {
      sVar7 = 0;
      uVar6 = 0;
      do {
        uVar4 = uVar6;
        if ((*(byte *)(param_1 + 0x4e) >> (uVar4 & 0xff) & 1) != 0) {
          sVar7 = sVar7 + 1;
        }
        uVar6 = uVar4 + 1;
      } while (uVar4 + 1 != 0x20);
      uVar6 = 0;
      do {
        uVar5 = uVar6;
        if ((*(byte *)(param_1 + uVar4 + 0x30) >> (uVar5 & 0xff) & 1) != 0) {
          sVar7 = sVar7 + 1;
        }
        uVar6 = uVar5 + 1;
      } while (uVar5 + 1 != 0x20);
      uVar6 = 0;
      do {
        uVar4 = uVar6;
        if ((*(byte *)(param_1 + uVar5 + 0x31) >> (uVar4 & 0xff) & 1) != 0) {
          sVar7 = sVar7 + 1;
        }
        uVar6 = uVar4 + 1;
      } while (uVar4 + 1 != 0x20);
      uVar6 = 0;
      do {
        uVar5 = uVar6;
        if ((*(byte *)(param_1 + uVar4 + 0x32) >> (uVar5 & 0xff) & 1) != 0) {
          sVar7 = sVar7 + 1;
        }
        uVar6 = uVar5 + 1;
      } while (uVar5 + 1 != 0x20);
      uVar6 = 0;
      do {
        if ((*(byte *)(param_1 + uVar5 + 0x33) >> (uVar6 & 0xff) & 1) != 0) {
          sVar7 = sVar7 + 1;
        }
        uVar6 = uVar6 + 1;
      } while (uVar6 != 0x20);
      *(short *)(iVar3 + 0xc) = sVar7;
    }
    *(undefined4 *)(iVar3 + 4) = *(undefined4 *)(param_1 + 0x24);
  }
  iVar3 = (**(code **)(puVar9[2] + 4))(*puVar9);
  if (iVar3 == 0) {
    puVar9 = *(undefined4 **)(*(int *)(param_1 + 0x6c) + 0x28);
    iVar3 = *(int *)puVar9[1];
    *(undefined2 *)(iVar3 + 0xe) = 1;
    if (DAT_20005f3c == '\x01') {
      *(undefined2 *)(iVar3 + 0xc) = 1;
      *(undefined4 *)(iVar3 + 8) = 0x20005f44;
      *(byte *)(iVar3 + 3) = *(byte *)(iVar3 + 3) & 0xcf | 0x10;
      *(undefined4 *)(iVar3 + 4) = 0x40082024;
    }
    else {
      *(byte *)(iVar3 + 3) = *(byte *)(iVar3 + 3) & 0xcf | 0x10;
      bVar1 = *(byte *)(param_1 + 6);
      uVar2 = *(undefined4 *)(param_1 + 0x28);
      *(undefined2 *)(iVar3 + 0xc) = *(undefined2 *)(param_1 + 8);
      *(undefined4 *)(iVar3 + 8) = uVar2;
      if (bVar1 == 9) {
        *(undefined4 *)(iVar3 + 4) = 0x40082024;
      }
      else {
        *(undefined4 *)(iVar3 + 4) = 0x40082024;
        if ((~bVar1 & 3) == 0) {
          uVar2 = *puVar9;
          *(undefined4 *)(iVar3 + 8) = *(undefined4 *)(param_1 + 0x34);
          pcVar8 = *(code **)(puVar9[2] + 4);
          *(short *)(iVar3 + 0xc) = *(short *)(iVar3 + 0xc) << 1;
          (*pcVar8)(uVar2);
          return;
        }
      }
    }
    (**(code **)(puVar9[2] + 4))(*puVar9);
  }
  return;
}
```

### `FUN_00020314` @ `00020314` score `40`

- reasons: event/CIN byte offset 4, payload byte offset 8, channel-voice/status nibble clue

```c

undefined4 FUN_00020314(ushort *param_1,uint param_2,undefined4 param_3)

{
  ushort uVar1;
  ushort uVar2;
  ushort *puVar3;
  ushort *puVar4;
  ushort *puVar5;
  int iVar6;
  uint uVar7;
  uint uVar8;
  uint uVar9;
  uint uVar10;
  int iVar11;
  uint uVar12;
  
  puVar3 = DAT_0002047c;
  uVar8 = DAT_00020478;
  if ((((param_1 == (ushort *)0x0) || (iVar11 = *(int *)(param_1 + 4), iVar11 == 0)) ||
      (*(int *)(param_1 + 8) == 0)) ||
     ((iVar6 = *(int *)(param_1 + 10), iVar6 == 0 || (*(int *)(param_1 + 0xc) == 0)))) {
    return 7;
  }
  if (param_2 != DAT_00020478) {
    uVar10 = (uint)*param_1;
    uVar9 = (uint)*DAT_0002047c;
    if (uVar10 != 0) {
      uVar12 = 0;
      while( true ) {
        uVar7 = (uint)*(ushort *)((uVar9 * uVar10 + uVar12) * 2 + iVar6);
        if (uVar7 != uVar8) {
          (**(code **)(param_1 + 0xe))(uVar7,param_3);
          uVar9 = (uint)*puVar3;
          uVar10 = (uint)*param_1;
        }
        uVar12 = uVar12 + 1;
        if (uVar10 <= (uVar12 & 0xffff)) break;
        iVar6 = *(int *)(param_1 + 10);
      }
      iVar11 = *(int *)(param_1 + 4);
    }
    puVar4 = DAT_00020480;
    uVar2 = *(ushort *)((uVar9 * param_1[2] + param_2 & 0xffff) * 2 + iVar11);
    uVar8 = (uint)uVar2;
    *DAT_00020480 = uVar2;
    puVar5 = DAT_00020488;
    if (uVar8 != DAT_00020478) {
      uVar12 = 0;
      if (uVar10 == 0) {
        if (uVar8 != DAT_00020484) {
          uVar1 = *puVar3;
          if (uVar8 == uVar1) {
            return 0;
          }
          *puVar3 = uVar2;
          *puVar5 = uVar1;
          return 0;
        }
      }
      else {
        while( true ) {
          uVar8 = (uint)*(ushort *)((uVar10 * uVar9 + uVar12) * 2 + *(int *)(param_1 + 0xc));
          if (uVar8 != DAT_00020478) {
            (**(code **)(param_1 + 0xe))(uVar8,param_3);
            uVar10 = (uint)*param_1;
          }
          puVar5 = DAT_00020488;
          uVar12 = uVar12 + 1;
          if (uVar10 <= (uVar12 & 0xffff)) break;
          uVar9 = (uint)*puVar3;
        }
        uVar8 = 0;
        if (uVar10 != 0) {
          do {
            uVar9 = (uint)*(ushort *)
                           (((uint)param_1[2] * (uint)*puVar3 + param_2 +
                            uVar8 * param_1[1] * (uint)param_1[2]) * 2 + *(int *)(param_1 + 6));
            if (uVar9 != DAT_00020478) {
              (**(code **)(param_1 + 0xe))(uVar9,param_3);
              uVar10 = (uint)*param_1;
            }
            puVar5 = DAT_00020488;
            uVar8 = uVar8 + 1;
          } while ((uVar8 & 0xffff) < uVar10);
          uVar2 = *puVar4;
          if (uVar2 == DAT_00020484) {
            *puVar3 = *DAT_00020488;
          }
          else {
            uVar1 = *puVar3;
            if ((uint)uVar1 != (uint)uVar2) {
              *puVar3 = uVar2;
              *puVar5 = uVar1;
            }
          }
          uVar8 = DAT_00020478;
          if (uVar10 == 0) {
            return 0;
          }
          uVar9 = 0;
          do {
            uVar12 = (uint)*(ushort *)((uVar10 * *puVar3 + uVar9) * 2 + *(int *)(param_1 + 8));
            if (uVar12 != uVar8) {
              (**(code **)(param_1 + 0xe))(uVar12,param_3);
              uVar10 = (uint)*param_1;
            }
            uVar9 = uVar9 + 1;
          } while ((uVar9 & 0xffff) < uVar10);
          return 0;
        }
        uVar2 = *puVar4;
        if (uVar2 != DAT_00020484) {
          uVar1 = *puVar3;
          if ((uint)uVar1 == (uint)uVar2) {
            return 0;
          }
          *puVar3 = uVar2;
          *puVar5 = uVar1;
          return 0;
        }
      }
      *puVar3 = *DAT_00020488;
    }
  }
  return 0;
}
```

### `FUN_00024b84` @ `00024b84` score `40`

- reasons: event/CIN byte offset 4, observed event code 0x02, channel-voice/status nibble clue, value 127

```c

undefined4 FUN_00024b84(short param_1)

{
  char cVar1;
  char *pcVar2;
  undefined1 *puVar3;
  int iVar4;
  int *piVar5;
  ushort uVar6;
  ushort uVar7;
  byte bVar8;
  ushort uVar9;
  ushort *puVar10;
  undefined2 uVar11;
  ushort uVar12;
  uint uVar13;
  short sVar14;
  byte *pbVar15;
  ushort *puVar16;
  ushort *puVar17;
  
  puVar16 = DAT_00024d34;
  pcVar2 = DAT_00024d14;
  if ((*DAT_00024d14 == '\x01') &&
     (uVar6 = *DAT_00024d34, *DAT_00024d34 = uVar6 + param_1, 1999 < (ushort)(uVar6 + param_1))) {
    *puVar16 = 0;
    *pcVar2 = '\0';
  }
  uVar6 = FUN_00025eb8();
  piVar5 = DAT_00024d2c;
  puVar16 = DAT_00024d28;
  iVar4 = DAT_00024d1c;
  puVar3 = DAT_00024d18;
  if ((short)uVar6 < 0) {
    if (*DAT_00024d28 != 0) {
      uVar13 = 0;
      pbVar15 = DAT_00024d20;
      puVar17 = DAT_00024d24;
      do {
        *puVar3 = 0;
        puVar10 = DAT_00024d30;
        uVar12 = *(ushort *)(uVar13 * 2 + *piVar5);
        uVar9 = uVar6 & 0x7fff ^ uVar12;
        uVar7 = uVar9 & 0x3800;
        if ((uVar9 & 0x3800) == 0) {
          if ((uVar12 & ~(uVar6 & 0x7fff | 0x3800)) == 0) {
            if ((*pbVar15 == 0) && (uVar12 = *DAT_00024d30, uVar12 < 2)) {
              *pbVar15 = 2;
              *puVar3 = 1;
              *puVar17 = uVar7;
              uVar12 = uVar12 + 1;
              uVar7 = 2;
              goto LAB_00024cce;
            }
          }
          else if (*pbVar15 != 0) {
            *puVar3 = 1;
            puVar10 = DAT_00024d30;
            *pbVar15 = 0;
            uVar12 = *puVar10 - 1;
LAB_00024cce:
            *puVar10 = uVar12;
            iVar4 = DAT_00024d1c;
            *(ushort *)(DAT_00024d1c + 4) = uVar7;
            *(short *)(iVar4 + 2) = (short)uVar13;
            FUN_00020264(2,0);
          }
        }
        uVar13 = uVar13 + 1;
        pbVar15 = pbVar15 + 1;
        puVar17 = puVar17 + 1;
      } while ((uVar13 & 0xffff) < (uint)*puVar16);
    }
  }
  else {
    sVar14 = 0;
    pbVar15 = DAT_00024d20;
    puVar16 = DAT_00024d24;
    do {
      while( true ) {
        *puVar3 = 0;
        uVar13 = (uint)*pbVar15;
        if (uVar13 != 2) break;
        uVar6 = *puVar16 + param_1;
        cVar1 = *pcVar2;
        *puVar16 = uVar6;
        if (cVar1 == '\x01') {
          if (uVar6 < 0x7d1) goto LAB_00024bc6;
          uVar11 = 1;
          bVar8 = 1;
        }
        else {
          if (uVar6 < 0x3e9) goto LAB_00024bc6;
          bVar8 = 3;
          uVar11 = 3;
        }
LAB_00024bf4:
        *pbVar15 = bVar8;
        *puVar3 = 1;
        *(short *)(iVar4 + 2) = sVar14;
        sVar14 = sVar14 + 1;
        *puVar16 = 0;
        *(undefined2 *)(iVar4 + 4) = uVar11;
        pbVar15 = pbVar15 + 1;
        FUN_00020264(2,0);
        puVar16 = puVar16 + 1;
        if (sVar14 == 200) {
          return 0;
        }
      }
      if (uVar13 < 3) {
        if (uVar13 == 1) {
          *pbVar15 = 0;
        }
      }
      else if ((uVar13 - 3 < 2) &&
              (uVar6 = *puVar16, *puVar16 = uVar6 + param_1, 0x28 < (ushort)(uVar6 + param_1))) {
        bVar8 = 4;
        uVar11 = 4;
        goto LAB_00024bf4;
      }
LAB_00024bc6:
      sVar14 = sVar14 + 1;
      pbVar15 = pbVar15 + 1;
      puVar16 = puVar16 + 1;
    } while (sVar14 != 200);
  }
  return 0;
}
```

### `FUN_000254e4` @ `000254e4` score `40`

- reasons: event/CIN byte offset 4, payload byte offset 8, channel-voice/status nibble clue

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_000254e4(undefined4 *param_1)

{
  undefined1 uVar1;
  undefined4 uVar2;
  int iVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  
  uVar2 = FUN_00059f84(5);
  *param_1 = uVar2;
  uVar1 = FUN_0005a0b4();
  *(undefined1 *)(param_1 + 1) = uVar1;
  param_1[3] = 0;
  uVar2 = FUN_00026d38(DAT_00025618);
  param_1[4] = uVar2;
  uVar2 = FUN_000254b0(DAT_0002561c);
  param_1[5] = uVar2;
  iVar3 = FUN_00059f84(5);
  uVar2 = FUN_0005a480(iVar3 << 1,(_DAT_14000000 & 0xff) + 1);
  param_1[2] = uVar2;
  uVar2 = FUN_00059f84(7);
  param_1[8] = uVar2;
  uVar2 = FUN_00059f84(6);
  uVar5 = *(undefined4 *)(DAT_00025620 + 0x24);
  uVar4 = FUN_0005ac90(*(undefined4 *)(DAT_00025620 + 0x28));
  uVar4 = FUN_0005ac1e(uVar4,0x3c800000);
  uVar5 = FUN_0005ac90(uVar5);
  uVar4 = FUN_0005abe8(uVar4,uVar5);
  iVar3 = FUN_0005ac80(uVar4,0);
  if (iVar3 == 0) {
    uVar2 = FUN_0005ac90(uVar2);
    uVar4 = FUN_0005ac1e(uVar4,0x41800000);
    FUN_0005abf2(uVar2,uVar4);
    uVar2 = FUN_0005ace0();
  }
  else {
    uVar2 = 0;
  }
  param_1[6] = uVar2;
  uVar2 = FUN_00059f84(6);
  uVar5 = *(undefined4 *)(DAT_00025624 + 0x24);
  uVar4 = FUN_0005ac90(*(undefined4 *)(DAT_00025624 + 0x28));
  uVar4 = FUN_0005ac1e(uVar4,0x3c800000);
  uVar5 = FUN_0005ac90(uVar5);
  uVar4 = FUN_0005abe8(uVar4,uVar5);
  iVar3 = FUN_0005ac80(uVar4,0);
  if (iVar3 == 0) {
    uVar2 = FUN_0005ac90(uVar2);
    uVar4 = FUN_0005ac1e(uVar4,0x41800000);
    FUN_0005abf2(uVar2,uVar4);
    uVar2 = FUN_0005ace0();
  }
  else {
    uVar2 = 0;
  }
  param_1[7] = uVar2;
  FUN_0004bf4c(param_1 + 9);
  uVar2 = DAT_00025628;
  FUN_0005c2cc(param_1 + 0x10,8,DAT_00025628,2,2,0);
  FUN_0005c2cc(param_1 + 0x12,8,uVar2,9,3,0);
  return;
}
```

### `FUN_0002dd0c` @ `0002dd0c` score `40`

- reasons: event/CIN byte offset 4, payload byte offset 8, channel-voice/status nibble clue

```c

undefined4 FUN_0002dd0c(int param_1,uint param_2,int param_3,uint param_4)

{
  int *piVar1;
  undefined1 uVar2;
  undefined4 uVar3;
  int iVar4;
  int iVar5;
  
  piVar1 = DAT_0002ddbc;
  if (param_2 < 9) {
    if ((int)param_4 < 1) {
      if (param_4 != 0) {
        iVar5 = param_2 * 0x1a + param_1 * 0xea;
        iVar4 = DAT_0002ddb8 + param_3 * 0x10;
        uVar2 = FUN_000202c8(*(undefined1 *)(*DAT_0002ddbc + iVar5 + param_3 + DAT_0002ddc0),
                             -param_4 & 0xffff,*(undefined2 *)(iVar4 + 2),*(undefined2 *)(iVar4 + 4)
                             ,*(undefined1 *)(iVar4 + 8));
        *(undefined1 *)(*piVar1 + iVar5 + param_3 + DAT_0002ddc0) = uVar2;
      }
    }
    else {
      iVar5 = param_2 * 0x1a + param_1 * 0xea;
      iVar4 = DAT_0002ddb8 + param_3 * 0x10;
      uVar2 = FUN_000202a8(*(undefined1 *)(*DAT_0002ddbc + iVar5 + param_3 + DAT_0002ddc0),
                           param_4 & 0xffff,*(undefined2 *)(iVar4 + 2),*(undefined2 *)(iVar4 + 4),
                           *(undefined1 *)(iVar4 + 8));
      *(undefined1 *)(*piVar1 + iVar5 + param_3 + DAT_0002ddc0) = uVar2;
    }
    uVar3 = 0;
  }
  else {
    uVar3 = 6;
  }
  return uVar3;
}
```

