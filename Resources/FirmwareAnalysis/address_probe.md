# Motion 32 Address Probe

## `0002607b`

- no containing function

```asm
00025fe4: bne 0x00025ff2
00025fe6: movs r1,#0xfa
00025fe8: lsls r1,r1,#0x2
00025fea: bl 0x0005a480
00025fee: str r0,[r4,#0x0]
00025ff0: b 0x00025fb6
00025ff2: movs r2,#0xfa
00025ff4: movs r3,#0x0
00025ff6: lsls r2,r2,#0x2
00025ff8: bl 0x0005a4fc
00025ffc: str r0,[r4,#0x0]
00025ffe: b 0x00025fb6
0002607a: strh.w r2,[r12,#0x301]
0002607e: mov r2,sp
00026080: add r1,sp,#0x10
00026082: strh r3,[r2,#0x10]
00026084: movs r0,#0x0
00026086: bl 0x0005cb24
0002608a: ldrb r0,[r4,#0x0]
0002608c: bl 0x00025b58
00026090: bl 0x0005956c
00026094: ldr r3,[0x00026164]
00026096: ldr r2,[0x00026168]
00026098: str r3,[sp,#0x8]
0002609a: movs r3,#0x0
```

## `000260c3`

- no containing function

```asm
000260a2: movs r3,#0x1
000260a4: rsbs r3,r3
000260a6: bl 0x000598e8
000260aa: movs r2,#0x80
000260ac: ldr r1,[0x00026170]
000260ae: ldr r0,[0x00026174]
000260b0: lsls r2,r2,#0x3
000260b2: bl 0x00057338
000260b6: ldr r4,[0x00026178]
000260b8: bl 0x0002d690
000260bc: bl 0x0002f9ec
000260c0: ldrh r0,[r4,#0x0]
000260c2: bl 0x0004af94
000260c6: movs r1,#0x0
000260c8: ldrh r0,[r4,#0x0]
000260ca: bl 0x00020200
000260ce: bl 0x00025fac
000260d2: ldrh r3,[r4,#0x0]
000260d4: adds r0,r3,r0
000260d6: uxth r0,r0
000260d8: strh r0,[r4,#0x0]
000260da: cmp r0,#0x14
000260dc: bls 0x000260b8
000260de: bl 0x0002620c
000260e2: movs r1,#0x1
```

## `0005fcff`

- no containing function

```asm
0005efee: pop {r0}
0005eff0: bx r12
0005f008: push {r0}
0005f00a: ldr r0,[0x0005f014]
0005f00c: mov r12,r0
0005f00e: pop {r0}
0005f010: bx r12
0005f048: push {r0}
0005f04a: ldr r0,[0x0005f054]
0005f04c: mov r12,r0
0005f04e: pop {r0}
0005f050: bx r12
0005fcfe: strb r3,[r6,#0x11]
0005fd00: movs r0,r0
0005fd02: movs r0,r0
0005fd04: ldr r3,[r2,#0x74]
0005fd06: strb r6,[r4,#0x11]
0005fd08: movs r0,r0
0005fd0a: movs r0,r0
0005fd0c: str r0,[r1,#0x14]
0005fd0e: str r2,[r6,#0x44]
0005fd10: movs r0,r0
0005fd12: movs r0,r0
00060000: ldr r1,[r4,#0x64]
00060002: movs r0,r0
```

## `000a2179`

- no containing function

```asm
00060060: movs r3,#0x44
00060062: cmp r7,#0x20
00060064: cmp r0,r4
00060066: lsls r2,r4,#0x1
00060068: lsls r6,r0,#0x1
0006006a: movs r0,r0
0006006c: movs r3,#0x46
0006006e: cmp r7,#0x20
00060070: bx r4
00089b22: push {r1,r2,r3,r4,r5,r6,r7,lr}
00089b24: add r7,sp,#0x0
0008fffe: udf #0xfb
000a2178: movs r0,r0
000a217a: movs r0,r0
000a217c: movs r0,r0
000a217e: movs r0,r0
000a2180: movs r0,r0
000a2182: movs r0,r0
000a2184: movs r0,r0
000a2186: movs r0,r0
000a2188: movs r0,r0
000a218a: movs r0,r0
000a218c: movs r0,r0
000a218e: movs r0,r0
000a2190: movs r0,r0
```

## `00047bb4`

- function: `PROBE_00047bb4` @ `00047bb4`

```asm
00047a74: strb r5,[r4,#0x0]
00047a76: add sp,#0xc
00047a78: pop {r4,r5,pc}
00047a7a: ldr r2,[0x00047a98]
00047a7c: movs r0,#0x2
00047a7e: str r2,[sp,#0x0]
00047a80: ldr r3,[0x00047a9c]
00047a82: movs r2,#0xb5
00047a84: ldr r1,[0x00047aa0]
00047a86: bl 0x000458e8
00047a8a: b 0x00047a76
00047b9e: movs r0,r4
00047ba0: bl 0x00033798
00047ba4: pop {r4,pc}
00047bb4: movs r1,r0
00047bb6: b 0x00047b9e
00047f90: push {r4,r5,r6,r7,lr}
00047f92: mov lr,r11
00047f94: mov r7,r10
00047f96: mov r6,r9
00047f98: mov r5,r8
00047f9a: push {r5,r6,r7,lr}
00047f9c: ldr r0,[0x00048278]
00047f9e: sub sp,#0xfc
00047fa0: movs r4,r1
00047fa2: bl 0x00032460
00047fa6: cmp r0,#0x1
00047fa8: beq 0x00047fb8
00047faa: add sp,#0xfc
```

```c

void PROBE_00047bb4(void)

{
  func_0x00033798();
  return;
}
```

## `00021f24`

- function: `PROBE_00021f24` @ `00021f24`

```asm
00021c2a: strb r0,[r4,#0x2]
00021c2c: adds r7,#0x1
00021c2e: adds r4,#0x5
00021c30: cmp r6,r3
00021c32: bne 0x00021bee
00021c34: movs r0,#0x0
00021c36: pop {r4,r5,r6,r7}
00021c38: mov r11,r7
00021c3a: mov r10,r6
00021c3c: mov r9,r5
00021c3e: mov r8,r4
00021c40: pop {r3,r4,r5,r6,r7,pc}
00021f18: movs r0,#0x0
00021f1a: pop {r4,pc}
00021f24: movs r1,r4
00021f26: movs r0,#0x28
00021f28: bl 0x0002e7ec
00021f2c: b 0x00021f18
00024b84: push {r4,r5,r6,r7,lr}
00024b86: mov r7,r10
00024b88: mov lr,r11
00024b8a: mov r6,r9
00024b8c: mov r5,r8
00024b8e: push {r5,r6,r7,lr}
00024b90: ldr r3,[0x00024d14]
00024b92: sub sp,#0xc
00024b94: str r3,[sp,#0x4]
00024b96: ldrb r3,[r3,#0x0]
00024b98: mov r10,r0
```

```c

undefined4 PROBE_00021f24(void)

{
  func_0x0002e7ec(0x28);
  return 0;
}
```

## `00022b70`

- function: `PROBE_00022b70` @ `00022b70`

```asm
000225e2: movs r0,#0x0
000225e4: strb r3,[r4,#0x1]
000225e6: bl 0x00020264
000225ea: b 0x000225cc
000225ec: lsrs r3,r3,#0x8
000225ee: b 0x000225dc
00022b2e: movs r0,#0x0
00022b30: add sp,#0xc
00022b32: pop {r4,r5,r6,r7}
00022b34: mov r11,r7
00022b36: mov r10,r6
00022b38: mov r9,r5
00022b3a: mov r8,r4
00022b3c: pop {r4,r5,r6,r7,pc}
00022b70: bl 0x0002dce0
00022b74: movs r2,#0x5
00022b76: movs r1,r4
00022b78: mov r10,r0
00022b7a: movs r0,r7
00022b7c: bl 0x0002dce0
00022b80: movs r2,#0x6
00022b82: movs r1,r4
00022b84: mov r11,r0
00022b86: movs r0,r7
00022b88: bl 0x0002dce0
00022b8c: uxtb r2,r0
00022b8e: mov r9,r2
00022b90: movs r1,r4
00022b92: movs r2,#0x1
```

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
  func_0x000225a8(uVar2);
  return 0;
}
```

## `0002164c`

- function: `FUN_00021484` @ `00021484`

```asm
0002162c: movs r0,r5
0002162e: ldr r1,[sp,#0x8]
00021630: bl 0x00036ee4
00021634: movs r3,#0xf2
00021636: lsls r3,r3,#0x1
00021638: ldr r5,[r4,r3]
0002163a: cmp r5,#0x0
0002163c: beq 0x00021660
0002163e: ldr r3,[0x000216c0]
00021640: ldr r0,[r3,#0x44]
00021642: bl 0x00044c78
00021646: add r3,sp,#0x4
00021648: strb r0,[r3,#0x0]
0002164a: lsls r2,r0,#0x10
0002164c: lsls r0,r0,#0x8
0002164e: lsrs r2,r2,#0x18
00021650: lsrs r0,r0,#0x18
00021652: strb r2,[r3,#0x1]
00021654: strb r0,[r3,#0x2]
00021656: movs r2,#0x0
00021658: movs r0,r5
0002165a: ldr r1,[sp,#0x4]
0002165c: bl 0x00036ee4
00021660: movs r3,#0xf8
00021662: lsls r3,r3,#0x1
00021664: ldr r4,[r4,r3]
00021666: cmp r4,#0x0
00021668: beq 0x0002168c
0002166a: ldr r3,[0x000216c0]
```

```c

undefined4 FUN_00021484(void)

{
  char *pcVar1;
  undefined3 uVar2;
  int iVar3;
  undefined4 uVar4;
  int iVar5;
  int iVar6;
  
  iVar5 = DAT_0002169c;
  pcVar1 = DAT_00021698;
  if (*DAT_00021694 == '\0') {
    uVar4 = 2;
  }
  else {
    if (*DAT_00021698 != '\0') {
      if (*(int *)(DAT_0002169c + 400) != 0) {
        FUN_00049750(*(int *)(DAT_0002169c + 400),DAT_000216a0);
      }
      if (*(int *)(iVar5 + 0x19c) != 0) {
        FUN_00049750(*(int *)(iVar5 + 0x19c),DAT_000216a4);
      }
      if (*(int *)(iVar5 + 0x1a8) != 0) {
        FUN_00049750(*(int *)(iVar5 + 0x1a8),DAT_000216a8);
      }
      if (*(int *)(iVar5 + 0x1b4) != 0) {
        FUN_00049750(*(int *)(iVar5 + 0x1b4),DAT_000216ac);
      }
      if (*(int *)(iVar5 + 0x1c8) != 0) {
        FUN_00049750(*(int *)(iVar5 + 0x1c8),DAT_000216b0);
      }
      if (*(int *)(iVar5 + 0x1d4) != 0) {
        FUN_00049750(*(int *)(iVar5 + 0x1d4),DAT_000216b4);
      }
      if (*(int *)(iVar5 + 0x1e0) != 0) {
        FUN_00049750(*(int *)(iVar5 + 0x1e0),DAT_000216b8);
      }
      if (*(int *)(iVar5 + 0x1ec) != 0) {
        FUN_00049750(*(int *)(iVar5 + 0x1ec),DAT_000216bc);
      }
      *pcVar1 = '\0';
    }
    iVar3 = FUN_0002dc30(0x43);
    iVar6 = *(int *)(iVar5 + 0x194);
    if (iVar3 == 0) {
      if (iVar6 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_00021828 + 0x5c));
        FUN_00036ee4(iVar6,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1a0);
      if (iVar3 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_00021828 + 0x5c));
        FUN_00036ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1ac);
      if (iVar3 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_00021828 + 0x5c));
        FUN_00036ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1b8);
      if (iVar3 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_00021828 + 0x5c));
        FUN_00036ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1cc);
      if (iVar3 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_00021828 + 0x5c));
        FUN_00036ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1d8);
      if (iVar3 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_00021828 + 0x5c));
        FUN_00036ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1e4);
      if (iVar3 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_00021828 + 0x5c));
        FUN_00036ee4(iVar3,uVar2,0);
      }
      iVar5 = *(int *)(iVar5 + 0x1f0);
      if (iVar5 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_00021828 + 0x5c));
        FUN_00036ee4(iVar5,uVar2,0);
      }
    }
    else {
      if (iVar6 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_000216c0 + 0x44));
        FUN_00036ee4(iVar6,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1a0);
      if (iVar3 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_000216c0 + 0x44));
        FUN_00036ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1ac);
      if (iVar3 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_000216c0 + 0x44));
        FUN_00036ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1b8);
      if (iVar3 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_000216c0 + 0x44));
        FUN_00036ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1cc);
      if (iVar3 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_000216c0 + 0x44));
        FUN_00036ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1d8);
      if (iVar3 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_000216c0 + 0x44));
        FUN_00036ee4(iVar3,uVar2,0);
      }
      iVar3 = *(int *)(iVar5 + 0x1e4);
      if (iVar3 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_000216c0 + 0x44));
        FUN_00036ee4(iVar3,uVar2,0);
      }
      iVar5 = *(int *)(iVar5 + 0x1f0);
      if (iVar5 != 0) {
        uVar2 = FUN_00044c78(*(undefined4 *)(DAT_000216c0 + 0x44));
        FUN_00036ee4(iVar5,uVar2,0);
      }
    }
    uVar4 = 0;
  }
  return uVar4;
}
```

## `0002064c`

- function: `FUN_0002064c` @ `0002064c`

```asm
00020618: add sp,#0xc
0002061a: pop {pc}
0002061c: movs r0,#0x90
0002061e: ldr r2,[0x00020644]
00020620: str r3,[sp,#0x4]
00020622: str r1,[r2,r0]
00020624: movs r1,#0x8e
00020626: subs r0,#0x8a
00020628: strh r0,[r2,r1]
0002062a: ldr r2,[0x00020648]
0002062c: ldr r0,[r2,#0x0]
0002062e: cmp r0,#0x0
00020630: bne 0x00020608
00020632: b 0x00020610
0002064c: push {r4,r5,r6,r7,lr}
0002064e: mov lr,r8
00020650: push {lr}
00020652: movs r0,#0x17
00020654: sub sp,#0x18
00020656: bl 0x0002dc30
0002065a: uxtb r3,r0
0002065c: movs r4,r0
0002065e: movs r0,#0x1
00020660: str r3,[sp,#0xc]
00020662: bl 0x0002dc30
00020666: cmp r0,#0x4
00020668: beq 0x0002067e
0002066a: movs r0,#0x1
0002066c: bl 0x0002dc30
```

```c

undefined4 FUN_0002064c(void)

{
  undefined1 *puVar1;
  undefined2 *puVar2;
  byte bVar3;
  int iVar4;
  int iVar5;
  ushort uVar6;
  ushort local_1a;
  
  bVar3 = FUN_0002dc30(0x17);
  iVar4 = FUN_0002dc30(1);
  if (iVar4 == 4) {
    iVar4 = FUN_0002da70(bVar3,&local_1a);
    puVar1 = DAT_00020750;
    if (iVar4 != 0) {
      *DAT_00020750 = 2;
      puVar1[1] = (char)((local_1a & 0xfff) >> 0xb);
      *(undefined2 *)(puVar1 + 2) = *(undefined2 *)(*DAT_00020754 + (uint)bVar3 * 6 + 4);
      *(short *)(puVar1 + 4) = (short)((local_1a & 0x7ff) >> 4);
      FUN_00020264(0,5);
      FUN_000202ec(0,3,0x2b,3,bVar3 + 0x2b,local_1a >> 4);
    }
  }
  else {
    iVar4 = FUN_0002dc30(1);
    if ((iVar4 == 6) &&
       (iVar5 = FUN_0002da70(bVar3,&local_1a), iVar4 = DAT_0002075c, puVar2 = DAT_00020758,
       iVar5 != 0)) {
      uVar6 = local_1a >> 7 & 0x7f;
      *DAT_00020758 = 0x8f0;
      *(undefined1 *)(puVar2 + 1) = *(undefined1 *)(iVar4 + 1);
      *(char *)((int)puVar2 + 7) = (char)(local_1a & 0x7f);
      *(undefined1 *)(puVar2 + 2) = 0x2d;
      *(undefined1 *)((int)puVar2 + 3) = 0x10;
      *(byte *)((int)puVar2 + 5) = bVar3;
      *(char *)(puVar2 + 3) = (char)uVar6;
      *(undefined1 *)(puVar2 + 4) = 0xf7;
      FUN_0002654c(0,puVar2,9);
      *puVar2 = 0x8f0;
      *(undefined1 *)(puVar2 + 1) = *(undefined1 *)(iVar4 + 1);
      *(undefined1 *)((int)puVar2 + 3) = 0x10;
      *(undefined1 *)(puVar2 + 2) = 0x2d;
      *(byte *)((int)puVar2 + 5) = bVar3;
      puVar2[3] = (local_1a & 0x7f) << 8 | uVar6;
      *(undefined1 *)(puVar2 + 4) = 0xf7;
      FUN_0002654c(2,puVar2,9);
    }
  }
  return 0;
}
```

## `0003ab58`

- function: `FUN_0003ab58` @ `0003ab58`

```asm
0003ab34: blx r3
0003ab36: pop {r4,pc}
0003ab38: movs r0,#0x0
0003ab3a: b 0x0003ab36
0003ab40: movs r2,#0xd0
0003ab42: ldr r3,[0x0003ab54]
0003ab44: push {r4,lr}
0003ab46: ldr r3,[r3,r2]
0003ab48: cmp r3,#0x0
0003ab4a: beq 0x0003ab50
0003ab4c: blx r3
0003ab4e: pop {r4,pc}
0003ab50: movs r0,#0x0
0003ab52: b 0x0003ab4e
0003ab58: push {r4,r5,lr}
0003ab5a: movs r4,r0
0003ab5c: sub sp,#0x24
0003ab5e: cmp r0,#0x0
0003ab60: beq 0x0003ab92
0003ab62: ldr r5,[r0,#0x18]
0003ab64: cmp r5,#0x0
0003ab66: beq 0x0003abac
0003ab68: ldr r3,[r5,#0x10]
0003ab6a: cmp r3,#0x0
0003ab6c: beq 0x0003ab76
0003ab6e: cmp r1,#0x0
0003ab70: beq 0x0003ab7a
0003ab72: movs r0,r4
0003ab74: blx r3
```

```c

void FUN_0003ab58(int param_1,undefined1 *param_2)

{
  code *pcVar1;
  int iVar2;
  undefined1 auStack_20 [20];
  
  if (param_1 == 0) {
    FUN_000458e8(3,DAT_0003abd8,0x8f,DAT_0003abd0,DAT_0003abd4,DAT_0003abcc,DAT_0003abc8);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar2 = *(int *)(param_1 + 0x18);
  if (iVar2 != 0) {
    pcVar1 = *(code **)(iVar2 + 0x10);
    if (pcVar1 != (code *)0x0) {
      if (param_2 == (undefined1 *)0x0) {
        FUN_00044064(auStack_20,0,0,*(ushort *)(param_1 + 4) - 1,*(ushort *)(param_1 + 6) - 1);
        pcVar1 = *(code **)(iVar2 + 0x10);
        param_2 = auStack_20;
      }
      (*pcVar1)(param_1,param_2);
    }
    return;
  }
  FUN_000458e8(3,DAT_0003abd8,0x90,DAT_0003abd0,DAT_0003abd4,DAT_0003abdc,DAT_0003abc8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

## `0003d600`

- function: `FUN_0003d600` @ `0003d600`

```asm
0003d5e4: asrs r4,r4,#0x8
0003d5e6: subs r2,r4,r5
0003d5e8: adds r4,r5,r4
0003d5ea: subs r4,r4,r3
0003d5ec: str r4,[r6,#0x8]
0003d5ee: str r2,[r6,#0x0]
0003d5f0: cmp r0,#0x0
0003d5f2: bgt 0x0003d5cc
0003d5f4: adds r0,#0x80
0003d5f6: asrs r0,r0,#0x8
0003d5f8: subs r2,r0,r5
0003d5fa: adds r5,r5,r0
0003d5fc: subs r5,r5,r3
0003d5fe: b 0x0003d5d6
0003d600: push {r4,r5,r6,r7,lr}
0003d602: mov r6,r9
0003d604: mov r5,r8
0003d606: mov lr,r11
0003d608: mov r7,r10
0003d60a: movs r3,#0x3c
0003d60c: push {r5,r6,r7,lr}
0003d60e: ldr r4,[0x0003d904]
0003d610: ldrb r3,[r1,r3]
0003d612: mov r12,r0
0003d614: mov r9,r0
0003d616: movs r5,r1
0003d618: add sp,r4
0003d61a: cmp r3,#0x2
0003d61c: bhi 0x0003d620
```

```c

void FUN_0003d600(int param_1,int param_2,undefined4 *param_3)

{
  undefined4 *puVar1;
  int *piVar2;
  undefined1 uVar3;
  byte bVar4;
  ushort uVar5;
  int iVar6;
  int iVar7;
  int iVar8;
  undefined4 uVar9;
  int iVar10;
  int iVar11;
  char cVar12;
  uint uVar13;
  int iVar14;
  int iVar15;
  int iVar16;
  int iVar17;
  int iVar18;
  int iVar19;
  undefined4 uVar20;
  undefined4 *puVar21;
  undefined4 *puVar22;
  int *piVar23;
  undefined4 *puVar24;
  undefined4 *puVar25;
  int *piVar26;
  undefined4 *puVar27;
  
  iVar6 = DAT_0003d904;
  puVar21 = (undefined4 *)(&stack0xffffffdc + DAT_0003d904);
  puVar22 = (undefined4 *)(&stack0xffffffdc + DAT_0003d904);
  piVar23 = (int *)(&stack0xffffffdc + DAT_0003d904);
  puVar24 = (undefined4 *)(&stack0xffffffdc + DAT_0003d904);
  puVar25 = (undefined4 *)(&stack0xffffffdc + DAT_0003d904);
  piVar26 = (int *)(&stack0xffffffdc + DAT_0003d904);
  puVar27 = (undefined4 *)(&stack0xffffffdc + DAT_0003d904);
  if (*(byte *)(param_2 + 0x3c) < 3) {
    return;
  }
  iVar19 = *(int *)(param_2 + 0x20);
  if (iVar19 == 0) {
    return;
  }
  if (*(int *)(param_2 + 0x24) == *(int *)(param_2 + 0x28)) {
    return;
  }
  uVar5 = *(ushort *)(param_2 + 0x34);
  puVar1 = (undefined4 *)(&stack0x00000034 + DAT_0003d904);
  uVar9 = param_3[1];
  uVar20 = param_3[2];
  *puVar1 = *param_3;
  *(undefined4 *)(&stack0x00000038 + DAT_0003d904) = uVar9;
  *(undefined4 *)(&stack0x0000003c + DAT_0003d904) = uVar20;
  *(undefined4 *)(&stack0x00000040 + DAT_0003d904) = param_3[3];
  iVar7 = FUN_000440d4(&stack0x00000044 + DAT_0003d904,puVar1,param_1 + 0x38);
  *(int *)(&stack0xfffffffc + iVar6) = iVar7;
  if (iVar7 == 0) {
    return;
  }
  *(uint *)(&stack0xfffffff0 + iVar6) = (uint)uVar5;
  if (iVar19 < (int)(uint)uVar5) {
    *(int *)(&stack0xfffffff0 + iVar6) = iVar19;
  }
  *(undefined4 *)(&stack0xfffffff4 + iVar6) = *(undefined4 *)(param_2 + 0x24);
  *(undefined4 *)(&stack0xffffffec + iVar6) = *(undefined4 *)(param_2 + 0x28);
  if (*(int *)(param_2 + 0x38) == 0) {
    if ((*(int *)(&stack0xfffffff4 + iVar6) + 0x168 == *(int *)(&stack0xffffffec + iVar6)) ||
       (*(int *)(&stack0xffffffec + iVar6) + 0x168 == *(int *)(&stack0xfffffff4 + iVar6))) {
      FUN_0003c970(&stack0x00000188 + iVar6);
      (&stack0x000001b0)[iVar6] = *(undefined1 *)(param_2 + 0x3c);
      *(undefined2 *)(&stack0x000001a8 + iVar6) = *(undefined2 *)(param_2 + 0x1c);
      (&stack0x000001aa)[iVar6] = *(undefined1 *)(param_2 + 0x1e);
      *(undefined4 *)(&stack0x000001ac + iVar6) = *(undefined4 *)(&stack0xfffffff0 + iVar6);
      *(undefined4 *)(&stack0x000001a4 + iVar6) = DAT_0003da98;
      (&stack0x000001b1)[iVar6] = (&stack0x000001b1)[iVar6] & 0xe0 | 0xf;
      FUN_0003dab0(param_1,&stack0x00000188 + iVar6,puVar1);
      return;
    }
  }
  iVar7 = *(int *)(param_2 + 0x20);
  *(int *)(&stack0x00000060 + iVar6) = *(int *)(&stack0x00000040 + iVar6) - iVar7;
  iVar19 = *(int *)(&stack0xfffffff4 + iVar6);
  *(int *)(&stack0x00000054 + iVar6) = *(int *)(&stack0x00000034 + iVar6) + iVar7;
  *(int *)(&stack0x00000058 + iVar6) = iVar7 + *(int *)(&stack0x00000038 + iVar6);
  *(int *)(&stack0x0000005c + iVar6) = *(int *)(&stack0x0000003c + iVar6) - iVar7;
  if (0x167 < iVar19) {
    do {
      iVar19 = iVar19 + -0x168;
    } while (0x167 < iVar19);
    *(int *)(&stack0xfffffff4 + iVar6) = iVar19;
  }
  iVar19 = *(int *)(&stack0xffffffec + iVar6);
  if (0x167 < iVar19) {
    do {
      iVar19 = iVar19 + -0x168;
    } while (0x167 < iVar19);
    *(int *)(&stack0xffffffec + iVar6) = iVar19;
  }
  FUN_0005aeec(&stack0x00000064 + iVar6,0,0x10);
  uVar20 = *(undefined4 *)(param_2 + 0x30);
  uVar9 = *(undefined4 *)(param_2 + 0x2c);
  *puVar21 = *(undefined4 *)(&stack0xffffffec + iVar6);
  FUN_00041f7c(&stack0x00000188 + iVar6,uVar9,uVar20,*(undefined4 *)(&stack0xfffffff4 + iVar6));
  *(undefined1 **)(&stack0x00000064 + iVar6) = &stack0x00000188 + iVar6;
  FUN_00042030(&stack0x000000a4 + iVar6,puVar1,DAT_0003d908,0);
  *(undefined1 **)(&stack0x00000068 + iVar6) = &stack0x000000a4 + iVar6;
  iVar19 = FUN_000448e4(&stack0x00000054 + iVar6);
  if ((iVar19 < 1) || (iVar19 = FUN_000448f0(&stack0x00000054 + iVar6), iVar19 < 1)) {
    *(undefined4 *)(&stack0xfffffffc + iVar6) = 0;
  }
  else {
    FUN_00042030(&stack0x000000c8 + iVar6,&stack0x00000054 + iVar6,DAT_0003d908,1);
    *(undefined1 **)(&stack0x0000006c + iVar6) = &stack0x000000c8 + iVar6;
  }
  iVar19 = FUN_000448f0(&stack0x00000044 + iVar6);
  uVar9 = FUN_000448e4(&stack0x00000044 + iVar6);
  *(undefined4 *)(&stack0x00000000 + iVar6) = uVar9;
  iVar7 = FUN_0004bea4();
  piVar2 = (int *)(&stack0x00000074 + iVar6);
  FUN_0005aef8(piVar2,&stack0x00000044 + iVar6,0x10);
  FUN_0005aeec(&stack0x00000114 + iVar6,0,0x28);
  *(int *)(&stack0x00000128 + iVar6) = iVar7;
  iVar10 = *(int *)(param_2 + 0x38);
  (&stack0x00000124)[iVar6] = *(undefined1 *)(param_2 + 0x3c);
  *(int **)(&stack0x00000110 + iVar6) = piVar2;
  *(int **)(&stack0x00000130 + iVar6) = piVar2;
  if (iVar10 == 0) {
LAB_0003d7da:
    FUN_0005aef8(&stack0x00000125 + iVar6,param_2 + 0x1c,3);
  }
  else {
    iVar10 = FUN_0003d060(&stack0x0000013c + iVar6,iVar10,0);
    if ((iVar10 == 0) || (iVar10 = *(int *)(&stack0x00000168 + iVar6), iVar10 == 0)) {
      *puVar22 = DAT_0003d90c;
      FUN_000458e8(2,DAT_0003d914,0x86,DAT_0003d910);
      goto LAB_0003d7da;
    }
    *(undefined4 *)(&stack0x00000014 + iVar6) = 0;
    *(undefined4 *)(&stack0x00000018 + iVar6) = 0;
    uVar5 = *(ushort *)(iVar10 + 4);
    *(uint *)(&stack0x0000001c + iVar6) = uVar5 - 1;
    iVar11 = *(int *)(param_2 + 0x2c);
    *(uint *)(&stack0x00000020 + iVar6) = *(ushort *)(iVar10 + 6) - 1;
    uVar13 = (uint)(uVar5 >> 1);
    FUN_000440b8(&stack0x00000014 + iVar6,iVar11 - uVar13,*(int *)(param_2 + 0x30) - uVar13);
    *(undefined1 **)(&stack0x00000120 + iVar6) = &stack0x00000014 + iVar6;
    iVar11 = *(int *)(&stack0x00000168 + iVar6);
    iVar10 = *(int *)(iVar11 + 0x10);
    *(int *)(&stack0x00000114 + iVar6) = iVar10;
    uVar5 = *(ushort *)(iVar11 + 8);
    *(uint *)(&stack0x00000118 + iVar6) = (uint)uVar5;
    if (*(char *)(iVar11 + 1) == '\x14') {
      (&stack0x0000011c)[iVar6] = 0x12;
      iVar11 = FUN_000448f0(&stack0x00000014 + iVar6);
      iVar10 = iVar10 + (uint)uVar5 * iVar11;
      goto LAB_0003d7f0;
    }
    (&stack0x0000011c)[iVar6] = *(char *)(iVar11 + 1);
  }
  iVar10 = 0;
LAB_0003d7f0:
  bVar4 = *(byte *)(param_2 + 0x3d);
  *(undefined4 *)(&stack0xfffffff8 + iVar6) = 0;
  if ((int)((uint)bVar4 << 0x1f) < 0) {
    iVar18 = *(int *)(&stack0xfffffff0 + iVar6) * *(int *)(&stack0xfffffff0 + iVar6);
    iVar11 = FUN_0004bea4(iVar18);
    *(int *)(&stack0xfffffff8 + iVar6) = iVar11;
    if (iVar11 == 0) {
      *(undefined4 *)(&stack0xffffffe4 + iVar6) = DAT_0003da9c;
      *(undefined4 *)(&stack0xffffffe0 + iVar6) = DAT_0003daa0;
      *puVar27 = DAT_0003daa8;
      FUN_000458e8(3,DAT_0003daac,0xa0,DAT_0003daa4);
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    iVar11 = *(int *)(&stack0xfffffff8 + iVar6);
    FUN_0004f350(iVar11,0xff,iVar18);
    *(undefined4 *)(&stack0x00000024 + iVar6) = 0;
    *(undefined4 *)(&stack0x00000028 + iVar6) = 0;
    iVar18 = *(int *)(&stack0xfffffff0 + iVar6) + -1;
    *(int *)(&stack0x0000002c + iVar6) = iVar18;
    *(int *)(&stack0x00000030 + iVar6) = iVar18;
    FUN_00042030(&stack0x000000ec + iVar6,&stack0x00000024 + iVar6,
                 *(int *)(&stack0xfffffff0 + iVar6) / 2,0);
    *(undefined4 *)(&stack0x00000010 + iVar6) = 0;
    *(undefined1 **)(&stack0x0000000c + iVar6) = &stack0x000000ec + iVar6;
    if (0 < *(int *)(&stack0xfffffff0 + iVar6)) {
      *(int *)(&stack0x00000004 + iVar6) = param_2;
      *(int *)(&stack0x00000008 + iVar6) = iVar7;
      iVar7 = 0;
      iVar18 = *(int *)(&stack0xfffffff0 + iVar6);
      do {
        *piVar26 = iVar18;
        iVar8 = FUN_00041cd8(&stack0x0000000c + iVar6,iVar11,0,iVar7);
        if (iVar8 == 0) {
          FUN_0004f350(iVar11,0,iVar18);
        }
        iVar7 = iVar7 + 1;
        iVar11 = iVar11 + iVar18;
      } while (iVar18 != iVar7);
      param_2 = *(int *)(&stack0x00000004 + iVar6);
      iVar7 = *(int *)(&stack0x00000008 + iVar6);
    }
    FUN_00041d34(&stack0x000000ec + iVar6);
    uVar3 = (&stack0xfffffff0)[iVar6];
    FUN_0003d58c((int)*(short *)(&stack0xfffffff4 + iVar6),*(undefined2 *)(param_2 + 0x34),uVar3,
                 &stack0x00000084 + iVar6);
    FUN_000440b8(&stack0x00000084 + iVar6,*(undefined4 *)(param_2 + 0x2c),
                 *(undefined4 *)(param_2 + 0x30));
    FUN_0003d58c((int)*(short *)(&stack0xffffffec + iVar6),*(undefined2 *)(param_2 + 0x34),uVar3,
                 &stack0x00000094 + iVar6);
    FUN_000440b8(&stack0x00000094 + iVar6,*(undefined4 *)(param_2 + 0x2c),
                 *(undefined4 *)(param_2 + 0x30));
  }
  *(undefined4 *)(&stack0x00000080 + iVar6) = *(undefined4 *)(&stack0x00000078 + iVar6);
/* ... truncated ... */
```

## `0003f83a`

- function: `PROBE_0003f83a` @ `0003f83a`

```asm
0003f7d6: ldrb r3,[r3,#0x3]
0003f7d8: ldr r2,[sp,#0x20]
0003f7da: strb r3,[r2,#0x0]
0003f7dc: add sp,#0xc
0003f7de: pop {r4,r5,r6,r7,pc}
0003f7e0: ldrb r0,[r4,#0x4]
0003f7e2: movs r6,#0xff
0003f7e4: muls r1,r0
0003f7e6: asrs r1,r1,#0x8
0003f7e8: subs r2,r2,r1
0003f7ea: lsls r0,r2,#0x8
0003f7ec: subs r1,r3,r1
0003f7ee: subs r0,r0,r2
0003f7f0: bl 0x0005a430
0003f83a: uxtb r0,r0
0003f83c: bl 0x00044c94
0003f840: strb r0,[r5,#0x0]
0003f842: lsls r3,r0,#0x10
0003f844: lsls r0,r0,#0x8
0003f846: lsrs r3,r3,#0x18
0003f848: lsrs r0,r0,#0x18
0003f84a: strb r3,[r5,#0x1]
0003f84c: strb r0,[r5,#0x2]
0003f84e: ldrb r2,[r4,#0x8]
0003f850: ldrb r3,[r4,#0x3]
0003f852: muls r2,r6
0003f854: muls r3,r7
0003f856: adds r2,r2,r3
0003f858: lsls r3,r2,#0x8
```

```c

void PROBE_0003f83a(undefined1 param_1)

{
  undefined4 uVar1;
  int unaff_r4;
  undefined1 *unaff_r5;
  int unaff_r6;
  int unaff_r7;
  undefined1 *in_stack_00000020;
  
  uVar1 = FUN_00044c94(param_1);
  *unaff_r5 = (char)uVar1;
  unaff_r5[1] = (char)((uint)uVar1 >> 8);
  unaff_r5[2] = (char)((uint)uVar1 >> 0x10);
  *in_stack_00000020 =
       (char)((unaff_r6 * (uint)*(byte *)(unaff_r4 + 8) + unaff_r7 * (uint)*(byte *)(unaff_r4 + 3))
              * 0x8081 >> 0x17);
  return;
}
```

## `0003f354`

- function: `FUN_0003f156` @ `0003f156`

```asm
0003f336: bne 0x0003f33a
0003f338: b 0x0003f480
0003f33a: cmp r3,#0x2
0003f33c: bne 0x0003f340
0003f33e: b 0x0003f448
0003f340: ldr r3,[sp,#0x24]
0003f342: cmp r3,#0x0
0003f344: beq 0x0003f348
0003f346: b 0x0003f578
0003f348: mov r1,r10
0003f34a: ldr r0,[sp,#0x20]
0003f34c: bl 0x0004cc20
0003f350: ldr r1,[sp,#0x44]
0003f352: ldr r2,[sp,#0x4c]
0003f354: ldr r3,[sp,#0x14]
0003f356: adds r4,#0x1
0003f358: cmp r3,r4
0003f35a: bgt 0x0003f35e
0003f35c: b 0x0003f4b4
0003f35e: ldr r3,[sp,#0x54]
0003f360: adds r5,r4,r1
0003f362: subs r6,r2,r4
0003f364: cmp r3,r5
0003f366: ble 0x0003f36e
0003f368: ldr r3,[sp,#0x5c]
0003f36a: cmp r3,r6
0003f36c: blt 0x0003f354
0003f36e: movs r2,r7
0003f370: mov r0,r9
```

```c

void FUN_0003f156(void)

{
  undefined1 uVar1;
  byte bVar2;
  byte bVar3;
  undefined2 uVar4;
  int iVar5;
  int iVar6;
  int iVar7;
  int iVar8;
  int iVar9;
  int *piVar10;
  int extraout_r1;
  byte bVar11;
  undefined1 *puVar12;
  int *extraout_r2;
  int in_r3;
  undefined1 *puVar13;
  int unaff_r4;
  undefined1 *puVar14;
  int iVar15;
  int unaff_r5;
  int iVar16;
  char cVar17;
  int iVar18;
  int iVar19;
  int iVar20;
  int unaff_r11;
  undefined1 *in_stack_00000024;
  int local_e0;
  uint local_dc;
  int local_d0;
  int local_cc;
  int *local_c8;
  undefined1 *local_bc;
  undefined4 local_b8;
  int local_b4;
  int local_b0;
  int local_ac;
  int local_a8;
  int local_a4;
  int local_a0;
  undefined4 local_9c;
  int local_98;
  int local_94;
  int local_90;
  undefined4 local_8c;
  int local_88;
  undefined1 auStack_84 [36];
  int *local_60;
  int local_5c;
  undefined1 local_54;
  int *local_50;
  byte local_4c;
  undefined1 local_4b;
  undefined2 local_4a;
  int local_48;
  char local_44;
  int *local_40;
  
  iVar20 = 0;
  puVar14 = in_stack_00000024 + unaff_r4;
  do {
    puVar12 = in_stack_00000024 + in_r3 + -1;
    puVar13 = in_stack_00000024;
    do {
      uVar1 = *puVar13;
      *puVar13 = *puVar12;
      puVar13 = puVar13 + 1;
      *puVar12 = uVar1;
      puVar12 = puVar12 + -1;
    } while (puVar13 != puVar14);
    iVar20 = iVar20 + 1;
    in_stack_00000024 = in_stack_00000024 + unaff_r11;
    puVar14 = puVar14 + unaff_r11;
  } while (unaff_r11 != iVar20);
  FUN_0003e79c();
  iVar20 = unaff_r5 >> 7;
  if (*(byte *)(extraout_r1 + 0x20) < 3) goto LAB_0003f1bc;
  local_b0 = extraout_r2[1];
  local_ac = extraout_r2[2];
  local_a8 = extraout_r2[3];
  local_b4 = *extraout_r2;
  iVar5 = FUN_000440d4(&local_a4,&local_b4,iVar20 + 0x38);
  if (iVar5 == 0) goto LAB_0003f1bc;
  bVar2 = *(byte *)(extraout_r1 + 0x2f);
  bVar11 = bVar2 & 0xf;
  bVar3 = *(byte *)(extraout_r1 + 0x20);
  local_dc = (uint)bVar3;
  if ((bVar2 & 0xf) == 0) {
    uVar1 = *(undefined1 *)(extraout_r1 + 0x21);
    uVar4 = *(undefined2 *)(extraout_r1 + 0x22);
    FUN_0005aeec(&local_60,0,0x2c);
    local_4b = uVar1;
    local_4a = uVar4;
    if (*(int *)(extraout_r1 + 0x1c) == 0) {
      local_60 = &local_b4;
      local_4c = bVar3;
      FUN_0004cc20(iVar20,&local_60);
      goto LAB_0003f1bc;
    }
  }
  else {
    uVar1 = *(undefined1 *)(extraout_r1 + 0x24);
    uVar4 = *(undefined2 *)(extraout_r1 + 0x25);
    FUN_0005aeec(&local_60,0,0x2c);
    local_4b = uVar1;
    local_4a = uVar4;
  }
  if (0xfc < local_dc) {
    local_dc = 0xff;
  }
  iVar6 = FUN_000448e4(&local_b4);
  iVar7 = FUN_000448f0(&local_b4);
  iVar8 = iVar6;
  if (iVar7 < iVar6) {
    iVar8 = iVar7;
  }
  local_e0 = iVar8 >> 1;
  if (*(int *)(extraout_r1 + 0x1c) < iVar8 >> 1) {
    local_e0 = *(int *)(extraout_r1 + 0x1c);
  }
  iVar8 = FUN_000448e4(&local_a4);
  local_bc = (undefined1 *)0x0;
  local_b8 = 0;
  bVar3 = (byte)local_dc;
  if (local_e0 < 1) {
    local_60 = &local_94;
    local_94 = local_a4;
    local_8c = local_9c;
    local_48 = 0;
    local_4c = 0xff;
    local_40 = local_60;
    piVar10 = (int *)FUN_0003f874(extraout_r1 + 0x24,iVar6,iVar7);
    iVar6 = local_b0;
    iVar7 = local_a8;
    if (piVar10 == (int *)0x0) {
      cVar17 = '\0';
      iVar9 = 0;
      local_c8 = (int *)0x0;
      goto LAB_0003f4ba;
    }
    iVar9 = 0;
    if (1 < bVar11) goto LAB_0003f29c;
    if ((bVar2 & 0xf) == 0) goto LAB_0003f5f0;
LAB_0003f4d2:
    local_44 = '\x01';
LAB_0003f4d8:
    iVar5 = local_a0;
    if (local_a0 < iVar6 + local_e0) {
      iVar5 = iVar6 + local_e0;
    }
    local_4c = bVar3;
    iVar8 = local_98;
    if (iVar7 - local_e0 < local_98) {
      iVar8 = iVar7 - local_e0;
    }
    for (; iVar5 <= iVar8; iVar5 = iVar5 + 1) {
      local_90 = iVar5;
      local_88 = iVar5;
      if (bVar11 == 1) {
        if (piVar10 == (int *)0x0) {
          FUN_000458e8(3,DAT_0003f778,299,DAT_0003f770,DAT_0003f774,DAT_0003f76c,DAT_0003f768);
          do {
                    /* WARNING: Do nothing block with infinite loop */
          } while( true );
        }
        iVar6 = iVar5 - local_b0;
        FUN_0005aef8(&local_4b,*piVar10 + iVar6 * 3,3);
        local_4c = *(byte *)(piVar10[1] + iVar6);
        if (local_dc < 0xfd) {
          local_4c = (byte)(local_dc * local_4c >> 8);
        }
      }
      FUN_0004cc20(iVar20,&local_60);
    }
  }
  else {
    iVar9 = FUN_0004bea4();
    FUN_00042030(auStack_84,&local_b4,local_e0,0);
    local_94 = local_a4;
    local_8c = local_9c;
    local_60 = &local_94;
    local_4c = 0xff;
    local_bc = auStack_84;
    local_48 = iVar9;
    local_40 = local_60;
    piVar10 = (int *)FUN_0003f874(extraout_r1 + 0x24,iVar6,iVar7);
    if (piVar10 != (int *)0x0) {
      local_c8 = piVar10;
      if (bVar11 < 2) {
LAB_0003f6a8:
        piVar10 = local_c8;
        local_c8 = (int *)0x0;
        iVar19 = 0;
        goto LAB_0003f2f4;
      }
LAB_0003f29c:
      local_50 = &local_94;
      local_5c = *piVar10 + (local_a4 - local_b4) * 3;
      iVar6 = local_b0;
      iVar7 = local_a8;
      if (*(char *)(extraout_r1 + 0x2e) != '\0') {
        if (*(char *)(extraout_r1 + 0x27) == -1) {
          if (*(char *)(extraout_r1 + 0x2e) == '\x01') {
            if (bVar11 == 2) {
LAB_0003f676:
              local_54 = 0xf;
              local_c8 = piVar10;
              if (0 < local_e0) goto LAB_0003f6a8;
              local_c8 = (int *)0x0;
              goto LAB_0003f68a;
            }
            iVar19 = 0;
          }
          else {
            if (*(char *)(extraout_r1 + 0x2c) != -1) goto joined_r0x0003f61c;
            iVar19 = 0;
/* ... truncated ... */
```

## `0004b084`

- function: `PROBE_0004b084` @ `0004b084`

```asm
0004b064: strb r6,[r4,r3]
0004b066: ldrb r2,[r4,r3]
0004b068: cmp r2,#0x0
0004b06a: beq 0x0004b064
0004b06c: b 0x0004b030
0004b06e: movs r2,#0xb8
0004b070: movs r0,#0x1
0004b072: ldr r7,[r4,r2]
0004b074: movs r2,#0xbc
0004b076: strb r0,[r4,r2]
0004b078: ldrb r1,[r4,r2]
0004b07a: cmp r1,#0x0
0004b07c: beq 0x0004b076
0004b07e: b 0x0004b028
0004b084: movs r2,#0xc4
0004b086: ldr r3,[0x0004b08c]
0004b088: str r0,[r3,r2]
0004b08a: bx lr
0004bea4: push {r4,lr}
0004bea6: cmp r0,#0x0
0004bea8: bne 0x0004beae
0004beaa: ldr r0,[0x0004beb4]
0004beac: pop {r4,pc}
0004beae: bl 0x0004e494
0004beb2: b 0x0004beac
0004beb8: push {r4,r5,r6,lr}
0004beba: subs r5,r0,#0x0
0004bebc: bne 0x0004bec4
0004bebe: ldr r4,[0x0004bed8]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_0004b084(undefined4 param_1)

{
  *(undefined4 *)(_DAT_0004b08c + 0xc4) = param_1;
  return;
}
```

## `0005ed60`

- function: `FUN_0005ed00` @ `0005ed00`

```asm
0005ed3e: bl 0x0005ec3c
0005ed42: ldr r3,[r7,#0x8]
0005ed44: adds r3,r3,r5
0005ed46: cmp r0,r3
0005ed48: beq 0x0005ed58
0005ed4a: mov r0,r8
0005ed4c: bl 0x0005e7e8
0005ed50: movs r0,#0x0
0005ed52: pop {r7}
0005ed54: mov r8,r7
0005ed56: pop {r4,r5,r6,r7,pc}
0005ed58: mov r0,r8
0005ed5a: rsbs r1,r4
0005ed5c: bl 0x0005ec3c
0005ed60: adds r0,#0x1
0005ed62: beq 0x0005ed80
0005ed64: movs r2,#0x1
0005ed66: subs r5,r5,r4
0005ed68: ldr r3,[r7,#0x8]
0005ed6a: orrs r5,r2
0005ed6c: ldr r2,[0x0005eda8]
0005ed6e: str r5,[r3,#0x4]
0005ed70: ldr r3,[r2,#0x0]
0005ed72: mov r0,r8
0005ed74: subs r3,r3,r4
0005ed76: str r3,[r2,#0x0]
0005ed78: bl 0x0005e7e8
0005ed7c: movs r0,#0x1
0005ed7e: b 0x0005ed52
```

```c

undefined4 FUN_0005ed00(undefined4 param_1,int param_2)

{
  int *piVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  uint uVar5;
  
  iVar2 = FUN_0005ec74(8);
  FUN_0005e7d8(param_1);
  iVar4 = DAT_0005eda4;
  uVar5 = *(uint *)(*(int *)(DAT_0005eda4 + 8) + 4) & 0xfffffffc;
  iVar3 = FUN_0005a480(((uVar5 - 0x11) - param_2) + iVar2,iVar2);
  iVar3 = iVar2 * (iVar3 + -1);
  if ((iVar2 <= iVar3) && (iVar2 = FUN_0005ec3c(param_1,0), iVar2 == *(int *)(iVar4 + 8) + uVar5)) {
    iVar2 = FUN_0005ec3c(param_1,-iVar3);
    piVar1 = DAT_0005eda8;
    if (iVar2 != -1) {
      *(uint *)(*(int *)(iVar4 + 8) + 4) = uVar5 - iVar3 | 1;
      *piVar1 = *piVar1 - iVar3;
      FUN_0005e7e8(param_1);
      return 1;
    }
    iVar2 = FUN_0005ec3c(param_1,0);
    iVar4 = *(int *)(iVar4 + 8);
    uVar5 = iVar2 - iVar4;
    if (0xf < (int)uVar5) {
      *DAT_0005eda8 = iVar2 - *DAT_0005edac;
      *(uint *)(iVar4 + 4) = uVar5 | 1;
    }
  }
  FUN_0005e7e8(param_1);
  return 0;
}
```

## `0000657c`

- function: `FUN_000064dc` @ `000064dc`

```asm
0000655e: ands r1,r6
00006560: mov r6,r9
00006562: subs r1,r6,r1
00006564: mov r9,r1
00006566: mov r1,r11
00006568: mov r6,r11
0000656a: lsls r1,r1,#0x4
0000656c: subs r1,r1,r6
0000656e: movs r6,#0x68
00006570: lsls r1,r1,#0x3
00006572: ldrb r6,[r0,r6]
00006574: lsrs r1,r1,#0x3
00006576: asrs r1,r6
00006578: movw r6,#0x3ff
0000657c: sdiv r9,r9,r1
00006580: mov r1,r8
00006582: ands r1,r6
00006584: mov r6,r9
00006586: adds r1,r6,r1
00006588: bmi 0x000065fc
0000658a: movw r6,#0x3ff
0000658e: cmp r1,r6
00006590: ble 0x000065da
00006592: mov r1,r12
00006594: adds r1,#0x1
00006596: strb r1,[r7,#0x0]
00006598: ldr r6,[r0,#0x24]
0000659a: ldr r1,[sp,#0x4]
0000659c: ldr r7,[r0,#0x14]
```

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

## `00006808`

- function: `PROBE_00006808` @ `00006808`

```asm
000067ec: bics r6,r7
000067ee: ands r2,r7
000067f0: orrs r2,r6
000067f2: strb r2,[r3,#0x2]
000067f4: cmp r1,#0x9
000067f6: beq 0x000068a0
000067f8: movs r2,#0x1f
000067fa: strb r2,[r3,#0x5]
000067fc: ldr r2,[r3,#0x0]
000067fe: ldr r1,[0x000068dc]
00006800: ands r2,r1
00006802: str r2,[r3,#0x0]
00006804: ldr r2,[r3,#0x0]
00006806: lsls r2,r2,#0x1
00006808: lsrs r2,r2,#0x1
0000680a: str r2,[r3,#0x0]
0000680c: movs r2,#0x80
0000680e: ldr r1,[r3,#0x8]
00006810: lsls r2,r2,#0x9
00006812: orrs r2,r1
00006814: str r2,[r3,#0x8]
00006816: movs r3,#0x4e
00006818: ldrb r2,[r4,r3]
0000681a: movw r3,#0x2000
0000681e: movt r3,#0x4008
00006822: strb r2,[r3,#0xc]
00006824: movs r2,#0x4f
00006826: ldrb r2,[r4,r2]
00006828: strb r2,[r3,#0xd]
```

```c

void PROBE_00006808(undefined4 param_1,undefined4 param_2,uint param_3,uint *param_4)

{
  int unaff_r4;
  
  *param_4 = param_3 >> 1;
  param_4[2] = param_4[2] | 0x10000;
  DAT_4008200c = *(undefined1 *)(unaff_r4 + 0x4e);
  DAT_4008200d = *(undefined1 *)(unaff_r4 + 0x4f);
  DAT_4008200e = *(undefined1 *)(unaff_r4 + 0x50);
  DAT_4008200f = *(undefined1 *)(unaff_r4 + 0x51);
  DAT_40082010 = *(undefined1 *)(unaff_r4 + 0x52);
  DAT_40082014 = *(undefined1 *)(unaff_r4 + 0x53);
  DAT_40082015 = *(undefined1 *)(unaff_r4 + 0x54);
  DAT_40082016 = *(undefined1 *)(unaff_r4 + 0x55);
  DAT_40082017 = *(undefined1 *)(unaff_r4 + 0x56);
  DAT_40082018 = *(undefined1 *)(unaff_r4 + 0x57);
  *(undefined1 *)(unaff_r4 + 4) = 2;
  *(undefined1 *)(unaff_r4 + 4) = 2;
  DAT_40082000 = DAT_40082000 | 1;
  return;
}
```

## `00006b00`

- function: `FUN_00006a94` @ `00006a94`

```asm
00006ae4: bge 0x00006ae8
00006ae6: b 0x00006c90
00006ae8: ldrh r0,[r6,#0x28]
00006aea: cmp r4,r0
00006aec: bge 0x00006af0
00006aee: b 0x00006c96
00006af0: ldrh r0,[r6,#0x2a]
00006af2: cmp r4,r0
00006af4: bge 0x00006af8
00006af6: b 0x00006c9c
00006af8: ldrh r0,[r6,#0x2c]
00006afa: cmp r4,r0
00006afc: bge 0x00006b00
00006afe: b 0x00006ca2
00006b00: ldrh r0,[r6,#0x2e]
00006b02: cmp r4,r0
00006b04: bge 0x00006b08
00006b06: b 0x00006ca8
00006b08: ldrh r0,[r6,#0x30]
00006b0a: cmp r4,r0
00006b0c: bge 0x00006b10
00006b0e: b 0x00006cae
00006b10: ldrh r0,[r6,#0x32]
00006b12: cmp r4,r0
00006b14: bge 0x00006b18
00006b16: b 0x00006cb4
00006b18: ldrh r0,[r6,#0x34]
00006b1a: cmp r4,r0
00006b1c: bge 0x00006b20
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00006a94(undefined2 *param_1,uint param_2,int param_3,int param_4,char param_5)

{
  ushort uVar1;
  uint uVar2;
  int iVar3;
  uint uVar4;
  int iVar5;
  longlong lVar6;
  longlong lVar7;
  longlong lVar8;
  undefined8 uVar9;
  uint local_50;
  uint local_40;
  uint local_38;
  
  if (param_4 == 7) {
    uVar4 = param_2;
    if (param_5 == '\a') {
LAB_00006c1e:
      lVar6 = 0;
      uVar9 = 0;
      local_50 = 0;
      goto LAB_00006bee;
    }
  }
  else {
    if (param_5 == '\a') goto LAB_00006c1e;
    uVar4 = (int)(param_2 << 3) / (param_4 + 1);
  }
  uVar2 = (uint)_DAT_20005f5c;
  if ((int)uVar4 < (int)uVar2) {
    uVar1 = *(ushort *)(param_3 * 0x18 + 0x20005f74);
    local_40 = 0;
    local_38 = 0;
  }
  else {
    uVar2 = (uint)_DAT_20005f5e;
    if ((int)uVar4 < (int)uVar2) {
      iVar3 = 1;
LAB_00006c62:
      iVar5 = iVar3 + -1;
    }
    else {
      uVar2 = (uint)_DAT_20005f60;
      if ((int)uVar4 < (int)uVar2) {
        iVar3 = 2;
        iVar5 = 1;
      }
      else {
        uVar2 = (uint)_DAT_20005f62;
        if ((int)uVar4 < (int)uVar2) {
          iVar3 = 3;
          iVar5 = 2;
        }
        else {
          uVar2 = (uint)_DAT_20005f64;
          if ((int)uVar4 < (int)uVar2) {
            iVar3 = 4;
            iVar5 = 3;
          }
          else {
            uVar2 = (uint)_DAT_20005f66;
            if ((int)uVar4 < (int)uVar2) {
              iVar3 = 5;
              iVar5 = 4;
            }
            else {
              uVar2 = (uint)_DAT_20005f68;
              if ((int)uVar4 < (int)uVar2) {
                iVar3 = 6;
                iVar5 = 5;
              }
              else {
                uVar2 = (uint)_DAT_20005f6a;
                if ((int)uVar4 < (int)uVar2) {
                  iVar3 = 7;
                  iVar5 = 6;
                }
                else {
                  uVar2 = (uint)_DAT_20005f6c;
                  if ((int)uVar4 < (int)uVar2) {
                    iVar3 = 8;
                    iVar5 = 7;
                  }
                  else {
                    uVar2 = (uint)_DAT_20005f6e;
                    if ((int)uVar4 < (int)uVar2) {
                      iVar3 = 9;
                      iVar5 = 8;
                    }
                    else {
                      uVar2 = (uint)_DAT_20005f70;
                      if ((int)uVar4 < (int)uVar2) {
                        iVar3 = 10;
                        iVar5 = 9;
                      }
                      else {
                        uVar2 = (uint)_DAT_20005f72;
                        iVar5 = 10;
                        iVar3 = 0xb;
                        if ((int)uVar4 < (int)uVar2) goto LAB_00006c62;
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
    uVar1 = *(ushort *)(&DAT_20005f3c + (iVar3 + param_3 * 0xc + 0x1c) * 2);
    local_40 = (uint)*(ushort *)(&DAT_20005f3c + (iVar5 + 0x10) * 2);
    local_38 = (uint)*(ushort *)(&DAT_20005f3c + (iVar5 + param_3 * 0xc + 0x1c) * 2);
  }
  local_50 = (uint)uVar1;
  if (param_4 == 7) {
    uVar9 = FUN_00009174(local_50 - local_38,-(uint)(local_50 < local_38),uVar2 - param_2,
                         -(uint)(uVar2 < param_2));
    lVar6 = CONCAT44(-(uint)(uVar2 < local_40),uVar2 - local_40);
  }
  else {
    param_4 = param_4 + 1;
    lVar6 = FUN_00009174(uVar2,0,param_4,0);
    lVar6 = lVar6 >> 3;
    lVar7 = FUN_00009174(local_50,0,param_4,0);
    local_50 = (uint)(lVar7 >> 3);
    lVar8 = FUN_00009174(local_38,0,param_4,0);
    lVar7 = (lVar7 >> 3) - (lVar8 >> 3);
    uVar9 = FUN_00009174((int)lVar7,(int)((ulonglong)lVar7 >> 0x20),(uint)lVar6 - param_2,
                         (int)((ulonglong)lVar6 >> 0x20) - (uint)((uint)lVar6 < param_2));
    lVar7 = FUN_00009174(local_40,0,param_4,0);
    lVar6 = lVar6 - (lVar7 >> 3);
  }
LAB_00006bee:
  iVar3 = FUN_0000912c((int)uVar9,(int)((ulonglong)uVar9 >> 0x20),(int)lVar6,
                       (int)((ulonglong)lVar6 >> 0x20));
  local_50 = local_50 - iVar3;
  if (0xffff < local_50) {
    local_50 = 0xffff;
  }
  *param_1 = (short)local_50;
  return;
}
```

## `00006cb4`

- function: `FUN_00006a94` @ `00006a94`

```asm
00006c98: subs r7,r5,#0x1
00006c9a: b 0x00006b2c
00006c9c: movs r5,#0x5
00006c9e: subs r7,r5,#0x1
00006ca0: b 0x00006b2c
00006ca2: movs r5,#0x6
00006ca4: subs r7,r5,#0x1
00006ca6: b 0x00006b2c
00006ca8: movs r5,#0x7
00006caa: subs r7,r5,#0x1
00006cac: b 0x00006b2c
00006cae: movs r5,#0x8
00006cb0: subs r7,r5,#0x1
00006cb2: b 0x00006b2c
00006cb4: movs r5,#0x9
00006cb6: subs r7,r5,#0x1
00006cb8: b 0x00006b2c
00006cba: movs r5,#0xa
00006cbc: subs r7,r5,#0x1
00006cbe: b 0x00006b2c
00006cc0: push {r4,r5,r6,r7,lr}
00006cc2: mov r5,r8
00006cc4: mov lr,r11
00006cc6: mov r7,r10
00006cc8: mov r6,r9
00006cca: movs r3,#0x68
00006ccc: push {r5,r6,r7,lr}
00006cce: ldrb r3,[r0,r3]
00006cd0: sub sp,#0x24
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00006a94(undefined2 *param_1,uint param_2,int param_3,int param_4,char param_5)

{
  ushort uVar1;
  uint uVar2;
  int iVar3;
  uint uVar4;
  int iVar5;
  longlong lVar6;
  longlong lVar7;
  longlong lVar8;
  undefined8 uVar9;
  uint local_50;
  uint local_40;
  uint local_38;
  
  if (param_4 == 7) {
    uVar4 = param_2;
    if (param_5 == '\a') {
LAB_00006c1e:
      lVar6 = 0;
      uVar9 = 0;
      local_50 = 0;
      goto LAB_00006bee;
    }
  }
  else {
    if (param_5 == '\a') goto LAB_00006c1e;
    uVar4 = (int)(param_2 << 3) / (param_4 + 1);
  }
  uVar2 = (uint)_DAT_20005f5c;
  if ((int)uVar4 < (int)uVar2) {
    uVar1 = *(ushort *)(param_3 * 0x18 + 0x20005f74);
    local_40 = 0;
    local_38 = 0;
  }
  else {
    uVar2 = (uint)_DAT_20005f5e;
    if ((int)uVar4 < (int)uVar2) {
      iVar3 = 1;
LAB_00006c62:
      iVar5 = iVar3 + -1;
    }
    else {
      uVar2 = (uint)_DAT_20005f60;
      if ((int)uVar4 < (int)uVar2) {
        iVar3 = 2;
        iVar5 = 1;
      }
      else {
        uVar2 = (uint)_DAT_20005f62;
        if ((int)uVar4 < (int)uVar2) {
          iVar3 = 3;
          iVar5 = 2;
        }
        else {
          uVar2 = (uint)_DAT_20005f64;
          if ((int)uVar4 < (int)uVar2) {
            iVar3 = 4;
            iVar5 = 3;
          }
          else {
            uVar2 = (uint)_DAT_20005f66;
            if ((int)uVar4 < (int)uVar2) {
              iVar3 = 5;
              iVar5 = 4;
            }
            else {
              uVar2 = (uint)_DAT_20005f68;
              if ((int)uVar4 < (int)uVar2) {
                iVar3 = 6;
                iVar5 = 5;
              }
              else {
                uVar2 = (uint)_DAT_20005f6a;
                if ((int)uVar4 < (int)uVar2) {
                  iVar3 = 7;
                  iVar5 = 6;
                }
                else {
                  uVar2 = (uint)_DAT_20005f6c;
                  if ((int)uVar4 < (int)uVar2) {
                    iVar3 = 8;
                    iVar5 = 7;
                  }
                  else {
                    uVar2 = (uint)_DAT_20005f6e;
                    if ((int)uVar4 < (int)uVar2) {
                      iVar3 = 9;
                      iVar5 = 8;
                    }
                    else {
                      uVar2 = (uint)_DAT_20005f70;
                      if ((int)uVar4 < (int)uVar2) {
                        iVar3 = 10;
                        iVar5 = 9;
                      }
                      else {
                        uVar2 = (uint)_DAT_20005f72;
                        iVar5 = 10;
                        iVar3 = 0xb;
                        if ((int)uVar4 < (int)uVar2) goto LAB_00006c62;
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
    uVar1 = *(ushort *)(&DAT_20005f3c + (iVar3 + param_3 * 0xc + 0x1c) * 2);
    local_40 = (uint)*(ushort *)(&DAT_20005f3c + (iVar5 + 0x10) * 2);
    local_38 = (uint)*(ushort *)(&DAT_20005f3c + (iVar5 + param_3 * 0xc + 0x1c) * 2);
  }
  local_50 = (uint)uVar1;
  if (param_4 == 7) {
    uVar9 = FUN_00009174(local_50 - local_38,-(uint)(local_50 < local_38),uVar2 - param_2,
                         -(uint)(uVar2 < param_2));
    lVar6 = CONCAT44(-(uint)(uVar2 < local_40),uVar2 - local_40);
  }
  else {
    param_4 = param_4 + 1;
    lVar6 = FUN_00009174(uVar2,0,param_4,0);
    lVar6 = lVar6 >> 3;
    lVar7 = FUN_00009174(local_50,0,param_4,0);
    local_50 = (uint)(lVar7 >> 3);
    lVar8 = FUN_00009174(local_38,0,param_4,0);
    lVar7 = (lVar7 >> 3) - (lVar8 >> 3);
    uVar9 = FUN_00009174((int)lVar7,(int)((ulonglong)lVar7 >> 0x20),(uint)lVar6 - param_2,
                         (int)((ulonglong)lVar6 >> 0x20) - (uint)((uint)lVar6 < param_2));
    lVar7 = FUN_00009174(local_40,0,param_4,0);
    lVar6 = lVar6 - (lVar7 >> 3);
  }
LAB_00006bee:
  iVar3 = FUN_0000912c((int)uVar9,(int)((ulonglong)uVar9 >> 0x20),(int)lVar6,
                       (int)((ulonglong)lVar6 >> 0x20));
  local_50 = local_50 - iVar3;
  if (0xffff < local_50) {
    local_50 = 0xffff;
  }
  *param_1 = (short)local_50;
  return;
}
```

## `00001e50`

- function: `FUN_00001b44` @ `00001b44`

```asm
00001e30: movw r3,#0x1428
00001e34: movs r1,#0x0
00001e36: strh r1,[r4,r3]
00001e38: adds r3,#0x3
00001e3a: adds r1,#0x1
00001e3c: strb r1,[r4,r3]
00001e3e: movw r5,#0x1400
00001e42: ldr r1,[r4,r5]
00001e44: asrs r1,r1,#0x8
00001e46: sxth r1,r1
00001e48: movs r3,r1
00001e4a: adds r3,#0x1e
00001e4c: bge 0x00001e50
00001e4e: b 0x00001f56
00001e50: cmp r2,#0x1
00001e52: bhi 0x00001e56
00001e54: b 0x00001c92
00001e56: movw r5,#0x1404
00001e5a: ldr r1,[r4,r5]
00001e5c: asrs r1,r1,#0x8
00001e5e: sxth r1,r1
00001e60: movs r3,r1
00001e62: adds r3,#0x1e
00001e64: bge 0x00001e68
00001e66: b 0x00001f7a
00001e68: cmp r2,#0x2
00001e6a: bhi 0x00001e6e
00001e6c: b 0x00001c92
00001e6e: movw r5,#0x1408
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

## `00001fb0`

- function: `FUN_00001b44` @ `00001b44`

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

## `0000240c`

- function: `FUN_00002370` @ `00002370`

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

## `0002ea70`

- function: `PROBE_0002ea70` @ `0002ea70`

```asm
0002e8ee: bl 0x0002e7ec
0002e8f2: movs r1,#0x4
0002e8f4: movs r0,#0x11
0002e8f6: bl 0x0002e7ec
0002e8fa: movs r1,#0xa
0002e8fc: b 0x0002e8a0
0002ea60: ldrh r2,[r3,#0xa]
0002ea62: cmp r2,#0x1
0002ea64: beq 0x0002ea6a
0002ea66: ldrh r2,[r3,#0x0]
0002ea68: strh r2,[r4,#0x0]
0002ea6a: adds r3,#0x10
0002ea6c: adds r4,#0x2
0002ea6e: cmp r0,r3
0002ea70: bne 0x0002ea60
0002ea72: bl 0x0002e864
0002ea76: movs r2,#0x80
0002ea78: ldr r4,[0x0002eb70]
0002ea7a: lsls r2,r2,#0x4
0002ea7c: movs r0,#0x0
0002ea7e: ldr r1,[r4,#0x0]
0002ea80: bl 0x0002edb8
0002ea84: ldr r3,[r4,#0x0]
0002ea86: movs r0,#0xff
0002ea88: mov r12,r3
0002ea8a: movs r2,r3
0002ea8c: movs r3,#0xff
0002ea8e: ldr r7,[0x0002eb74]
0002ea90: add r7,r12
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4
PROBE_0002ea70(undefined2 *param_1,undefined4 param_2,undefined4 param_3,undefined2 *param_4)

{
  byte bVar1;
  int *piVar2;
  uint uVar3;
  uint uVar4;
  byte *pbVar5;
  byte *pbVar6;
  uint uVar7;
  undefined2 *unaff_r4;
  int unaff_r5;
  int unaff_r6;
  char in_ZR;
  
  while (in_ZR == '\0') {
    if (param_4[5] != 1) {
      *unaff_r4 = *param_4;
    }
    param_4 = param_4 + 8;
    unaff_r4 = unaff_r4 + 1;
    in_ZR = param_1 == param_4;
  }
  func_0x0002e864();
  piVar2 = _DAT_0002eb70;
  func_0x0002edb8(0,*_DAT_0002eb70,0x800);
  pbVar6 = (byte *)*piVar2;
  uVar3 = 0xff;
  uVar7 = 0xff;
  pbVar5 = pbVar6;
  do {
    bVar1 = *pbVar5;
    pbVar5 = pbVar5 + 1;
    uVar4 = bVar1 ^ uVar7;
    uVar7 = *(byte *)(unaff_r5 + uVar4) ^ uVar3;
    uVar3 = (uint)*(byte *)(unaff_r6 + uVar4);
  } while (pbVar5 != pbVar6 + _DAT_0002eb74);
  if ((uint)*(ushort *)(pbVar6 + _DAT_0002eb74) == (uVar7 << 8 | uVar3)) {
    func_0x0002e7ec(0xc,*(undefined2 *)(pbVar6 + 0x34c));
    func_0x0002e7ec(0xd,*(undefined2 *)(*piVar2 + _DAT_0002eb78));
    func_0x0002e7ec(0xe,*(undefined2 *)(*piVar2 + 0x350));
    func_0x0002e7ec(0xf,*(undefined2 *)(*piVar2 + _DAT_0002eb7c));
    func_0x0002e7ec(0x10,*(undefined2 *)(*piVar2 + 0x354));
    func_0x0002e7ec(0x11,*(undefined2 *)(*piVar2 + _DAT_0002eb80));
    func_0x0002e7ec(0x12,*(undefined2 *)(*piVar2 + 0x358));
    func_0x0002e7ec(0x13,*(undefined2 *)(*piVar2 + _DAT_0002eb84));
    func_0x0002e7ec(0x14,*(undefined2 *)(*piVar2 + 0x35c));
    func_0x0002e7ec(0x15,*(undefined2 *)(*piVar2 + _DAT_0002eb88));
    func_0x0002e7ec(0x16,*(undefined2 *)(*piVar2 + 0x360));
  }
  return 0;
}
```

## `0002ec30`

- function: `PROBE_0002ec30` @ `0002ec30`

```asm
0002eb3e: movs r0,#0x14
0002eb40: bl 0x0002e7ec
0002eb44: ldr r2,[r4,#0x0]
0002eb46: ldr r3,[0x0002eb88]
0002eb48: movs r0,#0x15
0002eb4a: ldrh r1,[r2,r3]
0002eb4c: bl 0x0002e7ec
0002eb50: movs r3,#0xd8
0002eb52: ldr r2,[r4,#0x0]
0002eb54: lsls r3,r3,#0x2
0002eb56: ldrh r1,[r2,r3]
0002eb58: movs r0,#0x16
0002eb5a: bl 0x0002e7ec
0002eb5e: b 0x0002eab2
0002ec30: movs r1,r0
0002ec32: movs r0,r4
0002ec34: bl 0x0002e7ec
0002ec38: movs r0,#0x0
0002ec3a: add sp,#0xc
0002ec3c: pop {r4,r5,pc}
0002edb8: push {r4,r5,lr}
0002edba: movs r5,r1
0002edbc: movs r4,r2
0002edbe: sub sp,#0xc
0002edc0: cmp r1,#0x0
0002edc2: beq 0x0002ede6
0002edc4: cmp r2,#0x0
0002edc6: beq 0x0002edec
0002edc8: movs r3,#0x80
```

```c

undefined4 PROBE_0002ec30(void)

{
  func_0x0002e7ec();
  return 0;
}
```

## `0002ec74`

- function: `PROBE_0002ec74` @ `0002ec74`

```asm
0002eb4c: bl 0x0002e7ec
0002eb50: movs r3,#0xd8
0002eb52: ldr r2,[r4,#0x0]
0002eb54: lsls r3,r3,#0x2
0002eb56: ldrh r1,[r2,r3]
0002eb58: movs r0,#0x16
0002eb5a: bl 0x0002e7ec
0002eb5e: b 0x0002eab2
0002ec30: movs r1,r0
0002ec32: movs r0,r4
0002ec34: bl 0x0002e7ec
0002ec38: movs r0,#0x0
0002ec3a: add sp,#0xc
0002ec3c: pop {r4,r5,pc}
0002ec74: adds r1,r1,r2
0002ec76: uxth r0,r1
0002ec78: movs r2,r3
0002ec7a: movs r1,r4
0002ec7c: bl 0x0002edb8
0002ec80: movs r3,#0x8b
0002ec82: lsls r3,r3,#0x5
0002ec84: adds r7,r4,r3
0002ec86: movs r2,r4
0002ec88: movs r0,#0xff
0002ec8a: movs r3,#0xff
0002ec8c: ldr r6,[0x0002ecc4]
0002ec8e: ldr r5,[0x0002ecc8]
0002ec90: ldrb r1,[r2,#0x0]
0002ec92: adds r2,#0x1
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

byte PROBE_0002ec74(undefined4 param_1,short param_2,short param_3)

{
  byte bVar1;
  uint uVar2;
  uint uVar3;
  byte *pbVar4;
  uint uVar5;
  byte *unaff_r4;
  
  func_0x0002edb8(param_2 + param_3);
  uVar2 = 0xff;
  uVar5 = 0xff;
  pbVar4 = unaff_r4;
  do {
    bVar1 = *pbVar4;
    pbVar4 = pbVar4 + 1;
    uVar3 = bVar1 ^ uVar5;
    uVar5 = *(byte *)(_DAT_0002ecc4 + uVar3) ^ uVar2;
    uVar2 = (uint)*(byte *)(_DAT_0002ecc8 + uVar3);
  } while (pbVar4 != unaff_r4 + 0x1160);
  return -((uint)*(ushort *)(unaff_r4 + 0x1160) != (uVar5 << 8 | uVar2)) & 0x1d;
}
```

## `0002ecb8`

- function: `PROBE_0002ec74` @ `0002ec74`

```asm
0002ec9c: ldrb r0,[r5,r1]
0002ec9e: cmp r2,r7
0002eca0: bne 0x0002ec90
0002eca2: movs r2,#0x8b
0002eca4: lsls r2,r2,#0x5
0002eca6: ldrh r2,[r4,r2]
0002eca8: lsls r3,r3,#0x8
0002ecaa: orrs r3,r0
0002ecac: subs r3,r2,r3
0002ecae: subs r2,r3,#0x1
0002ecb0: sbcs r3,r2
0002ecb2: movs r0,#0x1d
0002ecb4: rsbs r3,r3
0002ecb6: ands r0,r3
0002ecb8: pop {r3,r4,r5,r6,r7,pc}
0002edb8: push {r4,r5,lr}
0002edba: movs r5,r1
0002edbc: movs r4,r2
0002edbe: sub sp,#0xc
0002edc0: cmp r1,#0x0
0002edc2: beq 0x0002ede6
0002edc4: cmp r2,#0x0
0002edc6: beq 0x0002edec
0002edc8: movs r3,#0x80
0002edca: lsls r3,r3,#0x9
0002edcc: subs r3,r3,r0
0002edce: cmp r2,r3
0002edd0: bhi 0x0002ede6
0002edd2: mov r3,sp
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

byte PROBE_0002ec74(undefined4 param_1,short param_2,short param_3)

{
  byte bVar1;
  uint uVar2;
  uint uVar3;
  byte *pbVar4;
  uint uVar5;
  byte *unaff_r4;
  
  func_0x0002edb8(param_2 + param_3);
  uVar2 = 0xff;
  uVar5 = 0xff;
  pbVar4 = unaff_r4;
  do {
    bVar1 = *pbVar4;
    pbVar4 = pbVar4 + 1;
    uVar3 = bVar1 ^ uVar5;
    uVar5 = *(byte *)(_DAT_0002ecc4 + uVar3) ^ uVar2;
    uVar2 = (uint)*(byte *)(_DAT_0002ecc8 + uVar3);
  } while (pbVar4 != unaff_r4 + 0x1160);
  return -((uint)*(ushort *)(unaff_r4 + 0x1160) != (uVar5 << 8 | uVar2)) & 0x1d;
}
```

## `0002ece0`

- function: `PROBE_0002ece0` @ `0002ece0`

```asm
0002ec9e: cmp r2,r7
0002eca0: bne 0x0002ec90
0002eca2: movs r2,#0x8b
0002eca4: lsls r2,r2,#0x5
0002eca6: ldrh r2,[r4,r2]
0002eca8: lsls r3,r3,#0x8
0002ecaa: orrs r3,r0
0002ecac: subs r3,r2,r3
0002ecae: subs r2,r3,#0x1
0002ecb0: sbcs r3,r2
0002ecb2: movs r0,#0x1d
0002ecb4: rsbs r3,r3
0002ecb6: ands r0,r3
0002ecb8: pop {r3,r4,r5,r6,r7,pc}
0002ece0: adds r7,r0,r3
0002ece2: movs r2,r0
0002ece4: movs r3,#0xff
0002ece6: movs r0,#0xff
0002ece8: ldr r6,[0x0002ed24]
0002ecea: ldr r5,[0x0002ed28]
0002ecec: ldrb r1,[r2,#0x0]
0002ecee: adds r2,#0x1
0002ecf0: eors r1,r3
0002ecf2: uxtb r1,r1
0002ecf4: ldrb r3,[r6,r1]
0002ecf6: eors r3,r0
0002ecf8: ldrb r0,[r5,r1]
0002ecfa: cmp r2,r7
0002ecfc: bne 0x0002ecec
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 PROBE_0002ece0(byte *param_1,undefined4 param_2,undefined4 param_3,int param_4)

{
  byte bVar1;
  uint uVar2;
  uint uVar3;
  uint uVar4;
  int unaff_r4;
  byte *pbVar5;
  int unaff_r8;
  int in_r12;
  
  pbVar5 = param_1 + param_4;
  uVar4 = 0xff;
  uVar2 = 0xff;
  do {
    bVar1 = *param_1;
    param_1 = param_1 + 1;
    uVar3 = bVar1 ^ uVar4;
    uVar4 = *(byte *)(_DAT_0002ed24 + uVar3) ^ uVar2;
    bVar1 = *(byte *)(_DAT_0002ed28 + uVar3);
    uVar2 = (uint)bVar1;
  } while (param_1 != pbVar5);
  *(ushort *)(unaff_r4 + 0x1160) = (ushort)(uVar4 << 8) | (ushort)bVar1;
  func_0x0002ed30(_DAT_0002ed2c * in_r12 + unaff_r8 & 0xffff);
  return 0;
}
```

## `0002edc4`

- function: `PROBE_0002edc4` @ `0002edc4`

```asm
0002eda0: adds r7,r7,r4
0002eda2: subs r6,r6,r4
0002eda4: bne 0x0002ed50
0002eda6: movs r0,#0x1
0002eda8: b 0x0002edac
0002edaa: movs r0,#0x0
0002edac: add sp,#0x14
0002edae: pop {r4,r5,r6,r7,pc}
0002edb8: push {r4,r5,lr}
0002edba: movs r5,r1
0002edbc: movs r4,r2
0002edbe: sub sp,#0xc
0002edc0: cmp r1,#0x0
0002edc2: beq 0x0002ede6
0002edc4: cmp r2,#0x0
0002edc6: beq 0x0002edec
0002edc8: movs r3,#0x80
0002edca: lsls r3,r3,#0x9
0002edcc: subs r3,r3,r0
0002edce: cmp r2,r3
0002edd0: bhi 0x0002ede6
0002edd2: mov r3,sp
0002edd4: rev16 r0,r0
0002edd6: strh r0,[r3,#0x4]
0002edd8: movs r2,#0x2
0002edda: movs r0,#0x51
0002eddc: add r1,sp,#0x4
0002edde: bl 0x0002562c
0002ede2: cmp r0,#0x0
```

```c

undefined4 PROBE_0002edc4(uint param_1,undefined4 param_2,uint param_3)

{
  int iVar1;
  undefined4 uVar2;
  ushort uStack00000004;
  
  if (param_3 == 0) {
    uVar2 = 1;
  }
  else {
    if (param_3 <= 0x10000 - param_1) {
      uStack00000004 = (ushort)((param_1 & 0xff) << 8) | (ushort)(param_1 >> 8) & 0xff;
      iVar1 = func_0x0002562c(0x51,&stack0x00000004,2);
      if (iVar1 != 0) {
        uVar2 = func_0x00025650(0x51);
        return uVar2;
      }
    }
    uVar2 = 0;
  }
  return uVar2;
}
```

## `0002eadc`

- function: `PROBE_0002ea70` @ `0002ea70`

```asm
0002eaa4: mov r1,r12
0002eaa6: ldr r2,[0x0002eb74]
0002eaa8: lsls r3,r3,#0x8
0002eaaa: ldrh r2,[r1,r2]
0002eaac: orrs r3,r0
0002eaae: cmp r2,r3
0002eab0: beq 0x0002ead0
0002eab2: movs r0,#0x0
0002eab4: pop {r3,r4,r5,r6,r7,pc}
0002ead0: movs r3,#0xd3
0002ead2: lsls r3,r3,#0x2
0002ead4: ldrh r1,[r1,r3]
0002ead6: movs r0,#0xc
0002ead8: bl 0x0002e7ec
0002eadc: ldr r2,[r4,#0x0]
0002eade: ldr r3,[0x0002eb78]
0002eae0: movs r0,#0xd
0002eae2: ldrh r1,[r2,r3]
0002eae4: bl 0x0002e7ec
0002eae8: movs r3,#0xd4
0002eaea: ldr r2,[r4,#0x0]
0002eaec: lsls r3,r3,#0x2
0002eaee: ldrh r1,[r2,r3]
0002eaf0: movs r0,#0xe
0002eaf2: bl 0x0002e7ec
0002eaf6: ldr r2,[r4,#0x0]
0002eaf8: ldr r3,[0x0002eb7c]
0002eafa: movs r0,#0xf
0002eafc: ldrh r1,[r2,r3]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4
PROBE_0002ea70(undefined2 *param_1,undefined4 param_2,undefined4 param_3,undefined2 *param_4)

{
  byte bVar1;
  int *piVar2;
  uint uVar3;
  uint uVar4;
  byte *pbVar5;
  byte *pbVar6;
  uint uVar7;
  undefined2 *unaff_r4;
  int unaff_r5;
  int unaff_r6;
  char in_ZR;
  
  while (in_ZR == '\0') {
    if (param_4[5] != 1) {
      *unaff_r4 = *param_4;
    }
    param_4 = param_4 + 8;
    unaff_r4 = unaff_r4 + 1;
    in_ZR = param_1 == param_4;
  }
  func_0x0002e864();
  piVar2 = _DAT_0002eb70;
  func_0x0002edb8(0,*_DAT_0002eb70,0x800);
  pbVar6 = (byte *)*piVar2;
  uVar3 = 0xff;
  uVar7 = 0xff;
  pbVar5 = pbVar6;
  do {
    bVar1 = *pbVar5;
    pbVar5 = pbVar5 + 1;
    uVar4 = bVar1 ^ uVar7;
    uVar7 = *(byte *)(unaff_r5 + uVar4) ^ uVar3;
    uVar3 = (uint)*(byte *)(unaff_r6 + uVar4);
  } while (pbVar5 != pbVar6 + _DAT_0002eb74);
  if ((uint)*(ushort *)(pbVar6 + _DAT_0002eb74) == (uVar7 << 8 | uVar3)) {
    func_0x0002e7ec(0xc,*(undefined2 *)(pbVar6 + 0x34c));
    func_0x0002e7ec(0xd,*(undefined2 *)(*piVar2 + _DAT_0002eb78));
    func_0x0002e7ec(0xe,*(undefined2 *)(*piVar2 + 0x350));
    func_0x0002e7ec(0xf,*(undefined2 *)(*piVar2 + _DAT_0002eb7c));
    func_0x0002e7ec(0x10,*(undefined2 *)(*piVar2 + 0x354));
    func_0x0002e7ec(0x11,*(undefined2 *)(*piVar2 + _DAT_0002eb80));
    func_0x0002e7ec(0x12,*(undefined2 *)(*piVar2 + 0x358));
    func_0x0002e7ec(0x13,*(undefined2 *)(*piVar2 + _DAT_0002eb84));
    func_0x0002e7ec(0x14,*(undefined2 *)(*piVar2 + 0x35c));
    func_0x0002e7ec(0x15,*(undefined2 *)(*piVar2 + _DAT_0002eb88));
    func_0x0002e7ec(0x16,*(undefined2 *)(*piVar2 + 0x360));
  }
  return 0;
}
```

## `0002eb4c`

- function: `PROBE_0002ea70` @ `0002ea70`

```asm
0002eb2c: ldr r3,[0x0002eb84]
0002eb2e: movs r0,#0x13
0002eb30: ldrh r1,[r2,r3]
0002eb32: bl 0x0002e7ec
0002eb36: movs r3,#0xd7
0002eb38: ldr r2,[r4,#0x0]
0002eb3a: lsls r3,r3,#0x2
0002eb3c: ldrh r1,[r2,r3]
0002eb3e: movs r0,#0x14
0002eb40: bl 0x0002e7ec
0002eb44: ldr r2,[r4,#0x0]
0002eb46: ldr r3,[0x0002eb88]
0002eb48: movs r0,#0x15
0002eb4a: ldrh r1,[r2,r3]
0002eb4c: bl 0x0002e7ec
0002eb50: movs r3,#0xd8
0002eb52: ldr r2,[r4,#0x0]
0002eb54: lsls r3,r3,#0x2
0002eb56: ldrh r1,[r2,r3]
0002eb58: movs r0,#0x16
0002eb5a: bl 0x0002e7ec
0002eb5e: b 0x0002eab2
0002ec30: movs r1,r0
0002ec32: movs r0,r4
0002ec34: bl 0x0002e7ec
0002ec38: movs r0,#0x0
0002ec3a: add sp,#0xc
0002ec3c: pop {r4,r5,pc}
0002ec74: adds r1,r1,r2
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4
PROBE_0002ea70(undefined2 *param_1,undefined4 param_2,undefined4 param_3,undefined2 *param_4)

{
  byte bVar1;
  int *piVar2;
  uint uVar3;
  uint uVar4;
  byte *pbVar5;
  byte *pbVar6;
  uint uVar7;
  undefined2 *unaff_r4;
  int unaff_r5;
  int unaff_r6;
  char in_ZR;
  
  while (in_ZR == '\0') {
    if (param_4[5] != 1) {
      *unaff_r4 = *param_4;
    }
    param_4 = param_4 + 8;
    unaff_r4 = unaff_r4 + 1;
    in_ZR = param_1 == param_4;
  }
  func_0x0002e864();
  piVar2 = _DAT_0002eb70;
  func_0x0002edb8(0,*_DAT_0002eb70,0x800);
  pbVar6 = (byte *)*piVar2;
  uVar3 = 0xff;
  uVar7 = 0xff;
  pbVar5 = pbVar6;
  do {
    bVar1 = *pbVar5;
    pbVar5 = pbVar5 + 1;
    uVar4 = bVar1 ^ uVar7;
    uVar7 = *(byte *)(unaff_r5 + uVar4) ^ uVar3;
    uVar3 = (uint)*(byte *)(unaff_r6 + uVar4);
  } while (pbVar5 != pbVar6 + _DAT_0002eb74);
  if ((uint)*(ushort *)(pbVar6 + _DAT_0002eb74) == (uVar7 << 8 | uVar3)) {
    func_0x0002e7ec(0xc,*(undefined2 *)(pbVar6 + 0x34c));
    func_0x0002e7ec(0xd,*(undefined2 *)(*piVar2 + _DAT_0002eb78));
    func_0x0002e7ec(0xe,*(undefined2 *)(*piVar2 + 0x350));
    func_0x0002e7ec(0xf,*(undefined2 *)(*piVar2 + _DAT_0002eb7c));
    func_0x0002e7ec(0x10,*(undefined2 *)(*piVar2 + 0x354));
    func_0x0002e7ec(0x11,*(undefined2 *)(*piVar2 + _DAT_0002eb80));
    func_0x0002e7ec(0x12,*(undefined2 *)(*piVar2 + 0x358));
    func_0x0002e7ec(0x13,*(undefined2 *)(*piVar2 + _DAT_0002eb84));
    func_0x0002e7ec(0x14,*(undefined2 *)(*piVar2 + 0x35c));
    func_0x0002e7ec(0x15,*(undefined2 *)(*piVar2 + _DAT_0002eb88));
    func_0x0002e7ec(0x16,*(undefined2 *)(*piVar2 + 0x360));
  }
  return 0;
}
```

## `0002eba8`

- function: `PROBE_0002eba8` @ `0002eba8`

```asm
0002eb56: ldrh r1,[r2,r3]
0002eb58: movs r0,#0x16
0002eb5a: bl 0x0002e7ec
0002eb5e: b 0x0002eab2
0002eb94: adds r4,#0x1
0002eb96: uxth r4,r4
0002eb98: adds r5,#0x10
0002eb9a: cmp r4,#0x57
0002eb9c: beq 0x0002ebb6
0002eb9e: ldrh r3,[r5,#0xe]
0002eba0: cmp r3,#0x0
0002eba2: beq 0x0002eb94
0002eba4: uxtb r0,r4
0002eba6: adds r4,#0x1
0002eba8: ldrh r1,[r5,#0x0]
0002ebaa: uxth r4,r4
0002ebac: bl 0x0002e7ec
0002ebb0: adds r5,#0x10
0002ebb2: cmp r4,#0x57
0002ebb4: bne 0x0002eb9e
0002ebb6: movs r0,#0x0
0002ebb8: pop {r4,r5,r6,pc}
0002ec30: movs r1,r0
0002ec32: movs r0,r4
0002ec34: bl 0x0002e7ec
0002ec38: movs r0,#0x0
0002ec3a: add sp,#0xc
0002ec3c: pop {r4,r5,pc}
0002ec74: adds r1,r1,r2
```

```c

undefined4 PROBE_0002eba8(uint param_1)

{
  uint uVar1;
  undefined2 *puVar2;
  uint unaff_r4;
  undefined2 *unaff_r5;
  
  do {
    func_0x0002e7ec(param_1,*unaff_r5);
    puVar2 = unaff_r5;
    while( true ) {
      uVar1 = unaff_r4 & 0xffff;
      if (uVar1 == 0x57) {
        return 0;
      }
      unaff_r5 = puVar2 + 8;
      if (puVar2[0xf] != 0) break;
      unaff_r4 = uVar1 + 1;
      puVar2 = unaff_r5;
    }
    param_1 = unaff_r4 & 0xff;
    unaff_r4 = uVar1 + 1;
  } while( true );
}
```

## `0002f1f8`

- function: `PROBE_0002f1f8` @ `0002f1f8`

```asm
0002f072: movs r2,r7
0002f074: adds r3,#0x10
0002f076: mov r1,r11
0002f078: mov r0,r10
0002f07a: bl 0x000270e8
0002f07e: movs r3,#0x10
0002f080: add r8,r3
0002f082: mov r3,r8
0002f084: adds r5,#0x10
0002f086: adds r6,#0x10
0002f088: adds r4,#0x10
0002f08a: cmp r3,#0xc0
0002f08c: bne 0x0002f010
0002f08e: b 0x0002f030
0002f1f8: strb r5,[r0,#0x0]
0002f1fa: strb r5,[r3,#0x0]
0002f1fc: movs r3,r1
0002f1fe: add r2,r8
0002f200: strb r5,[r2,#0x0]
0002f202: ldr r2,[0x0002f23c]
0002f204: add r3,r12
0002f206: strb r5,[r3,r2]
0002f208: add sp,#0x8
0002f20a: pop {r5,r6,r7}
0002f20c: mov r10,r7
0002f20e: mov r9,r6
0002f210: mov r8,r5
0002f212: pop {r4,r5,r6,r7,pc}
0002f6e8: ldr r3,[0x0002f7a8]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_0002f1f8(undefined1 *param_1,int param_2,int param_3,undefined1 *param_4)

{
  undefined1 unaff_r5;
  int unaff_r8;
  int in_r12;
  
  *param_1 = unaff_r5;
  *param_4 = unaff_r5;
  *(undefined1 *)(param_3 + unaff_r8) = unaff_r5;
  *(undefined1 *)(param_2 + in_r12 + _DAT_0002f23c) = unaff_r5;
  return;
}
```

## `0002f220`

- function: `PROBE_0002f220` @ `0002f220`

```asm
0002f1f8: strb r5,[r0,#0x0]
0002f1fa: strb r5,[r3,#0x0]
0002f1fc: movs r3,r1
0002f1fe: add r2,r8
0002f200: strb r5,[r2,#0x0]
0002f202: ldr r2,[0x0002f23c]
0002f204: add r3,r12
0002f206: strb r5,[r3,r2]
0002f208: add sp,#0x8
0002f20a: pop {r5,r6,r7}
0002f20c: mov r10,r7
0002f20e: mov r9,r6
0002f210: mov r8,r5
0002f212: pop {r4,r5,r6,r7,pc}
0002f220: ldrb r5,[r6,#0x0]
0002f222: adds r0,r0,r2
0002f224: orrs r5,r7
0002f226: strb r5,[r6,#0x0]
0002f228: add r0,r8
0002f22a: ldrb r0,[r0,#0x0]
0002f22c: orrs r0,r7
0002f22e: b 0x0002f1dc
0002f6e8: ldr r3,[0x0002f7a8]
0002f6ea: ldr r2,[0x0002f7ac]
0002f6ec: push {r4,r5,r6,r7,lr}
0002f6ee: adds r4,r3,r2
0002f6f0: ldr r2,[0x0002f7b0]
0002f6f2: mov r6,r8
0002f6f4: adds r5,r3,r2
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_0002f220(int param_1,int param_2,int param_3,int param_4)

{
  int iVar1;
  int iVar2;
  undefined1 *puVar3;
  int unaff_r4;
  byte *unaff_r6;
  byte unaff_r7;
  int unaff_r8;
  int unaff_r10;
  int in_r12;
  
  *unaff_r6 = *unaff_r6 | unaff_r7;
  iVar2 = param_2 + (param_4 + in_r12) * 0x10;
  *(byte *)(iVar2 + param_3 + _DAT_0002f234) = *(byte *)(param_1 + param_3 + unaff_r8) | unaff_r7;
  iVar1 = _DAT_0002f238;
  puVar3 = (undefined1 *)(iVar2 + unaff_r4 + _DAT_0002f238);
  *(undefined1 *)(iVar2 + unaff_r10 + _DAT_0002f238) = 1;
  *puVar3 = 1;
  *(undefined1 *)(iVar2 + param_3 + iVar1) = 1;
  *(undefined1 *)(param_2 + in_r12 + _DAT_0002f23c) = 1;
  return;
}
```

## `0002f234`

- function: `PROBE_0002f234` @ `0002f234`

```asm
0002f208: add sp,#0x8
0002f20a: pop {r5,r6,r7}
0002f20c: mov r10,r7
0002f20e: mov r9,r6
0002f210: mov r8,r5
0002f212: pop {r4,r5,r6,r7,pc}
0002f220: ldrb r5,[r6,#0x0]
0002f222: adds r0,r0,r2
0002f224: orrs r5,r7
0002f226: strb r5,[r6,#0x0]
0002f228: add r0,r8
0002f22a: ldrb r0,[r0,#0x0]
0002f22c: orrs r0,r7
0002f22e: b 0x0002f1dc
0002f234: lsls r2,r3,#0x14
0002f236: movs r0,r0
0002f238: lsls r2,r6,#0x14
0002f23a: movs r0,r0
0002f23c: lsrs r2,r5,#0x1a
0002f23e: movs r0,r0
0002f240: push {r4,r5,r6,r7,lr}
0002f242: mov lr,r11
0002f244: mov r7,r10
0002f246: mov r6,r9
0002f248: mov r5,r8
0002f24a: ldr r4,[0x0002f2c4]
0002f24c: lsls r3,r0,#0x3
0002f24e: adds r3,r3,r0
0002f250: adds r3,r4,r3
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_0002f234(int param_1,uint param_2)

{
  byte bVar1;
  ushort uVar2;
  int *piVar3;
  uint uVar4;
  int iVar5;
  uint uVar6;
  int iVar7;
  uint uVar8;
  
  piVar3 = _DAT_0002f2c4;
  iVar7 = (int)_DAT_0002f2c4 + param_1 * 9;
  if (*(byte *)(iVar7 + 0x11) != param_2) {
    iVar5 = *_DAT_0002f2c4 + param_1 * 0x14;
    uVar2 = *(ushort *)(iVar5 + 0x12);
    *(char *)(iVar7 + 0x11) = (char)param_2;
    bVar1 = *(byte *)((int)piVar3 + 6);
    uVar6 = (uint)*(byte *)(iVar5 + 0xc);
    uVar8 = uVar6 + 0x30;
    uVar4 = uVar2 & 0xff;
    do {
      iVar5 = uVar6 + uVar4 * 0x180;
      uVar6 = uVar6 + 0x10 & 0xff;
      *(char *)((int)piVar3 + _DAT_0002f2c8 + iVar5) =
           (char)(bVar1 * param_2 * (uint)*(byte *)(iVar7 + 0xe) * (uint)*(byte *)(iVar7 + 0xb) >>
                 0x18);
      iVar7 = iVar7 + 1;
      *(undefined1 *)((int)piVar3 + _DAT_0002f2cc + iVar5) = 1;
    } while (uVar6 != (uVar8 & 0xff));
    *(undefined1 *)((int)piVar3 + _DAT_0002f2d0 + uVar4) = 1;
  }
  return;
}
```

## `0002f2f0`

- function: `PROBE_0002f2f0` @ `0002f2f0`

```asm
0002f2a6: ldr r0,[0x0002f2cc]
0002f2a8: adds r3,#0x1
0002f2aa: strb r7,[r1,r0]
0002f2ac: cmp r2,r10
0002f2ae: bne 0x0002f28c
0002f2b0: ldr r3,[0x0002f2d0]
0002f2b2: add r4,r11
0002f2b4: strb r7,[r4,r3]
0002f2b6: pop {r4,r5,r6,r7}
0002f2b8: mov r11,r7
0002f2ba: mov r10,r6
0002f2bc: mov r9,r5
0002f2be: mov r8,r4
0002f2c0: pop {r4,r5,r6,r7,pc}
0002f2f0: lsls r4,r4,#0x2
0002f2f2: adds r4,r6,r4
0002f2f4: ldrh r6,[r4,#0x12]
0002f2f6: ldrh r4,[r4,#0xc]
0002f2f8: mov r12,r6
0002f2fa: strb r2,[r5,#0xb]
0002f2fc: lsls r1,r1,#0x4
0002f2fe: ldrb r6,[r0,#0x6]
0002f300: adds r1,r4,r1
0002f302: ldrb r4,[r3,#0x11]
0002f304: ldrb r3,[r5,#0xe]
0002f306: muls r4,r6
0002f308: muls r3,r4
0002f30a: muls r2,r3
0002f30c: mov r3,r12
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_0002f2f0(int param_1,char param_2,int param_3,int param_4)

{
  ushort uVar1;
  undefined2 uVar2;
  uint uVar3;
  int unaff_r4;
  int iVar4;
  int unaff_r5;
  int unaff_r6;
  
  iVar4 = unaff_r6 + unaff_r4 * 4;
  uVar1 = *(ushort *)(iVar4 + 0x12);
  uVar2 = *(undefined2 *)(iVar4 + 0xc);
  *(char *)(unaff_r5 + 0xb) = (char)param_3;
  uVar3 = uVar1 & 0xff;
  iVar4 = param_1 + uVar3 * 0x180 + (uint)(byte)((char)uVar2 + param_2 * '\x10');
  *(char *)(iVar4 + _DAT_0002f340) =
       (char)((uint)*(byte *)(param_1 + 6) * (uint)*(byte *)(param_4 + 0x11) *
              (uint)*(byte *)(unaff_r5 + 0xe) * param_3 >> 0x18);
  *(undefined1 *)(iVar4 + _DAT_0002f344) = 1;
  *(undefined1 *)(param_1 + uVar3 + _DAT_0002f348) = 1;
  return;
}
```

## `0002f644`

- function: `PROBE_0002f644` @ `0002f644`

```asm
0002f626: movs r2,r4
0002f628: mov r1,r8
0002f62a: str r3,[sp,#0x0]
0002f62c: mov r0,r11
0002f62e: movs r3,#0x2
0002f630: bl 0x000270e8
0002f634: movs r2,#0x2
0002f636: ldrb r3,[r5,#0x0]
0002f638: orrs r3,r2
0002f63a: movs r2,#0x0
0002f63c: strb r3,[r5,#0x0]
0002f63e: ldrb r3,[r5,#0x0]
0002f640: strb r2,[r4,#0x0]
0002f642: strb r3,[r4,#0x1]
0002f644: bl 0x000599bc
0002f648: adds r0,r0,r6
0002f64a: adcs r1,r7
0002f64c: cmp r1,r10
0002f64e: bcc 0x0002f656
0002f650: movs r0,#0x1
0002f652: ldr r1,[0x0002f6dc]
0002f654: rsbs r0,r0
0002f656: mov r3,r9
0002f658: str r0,[sp,#0x8]
0002f65a: str r1,[sp,#0xc]
0002f65c: movs r2,r4
0002f65e: mov r1,r8
0002f660: str r3,[sp,#0x0]
0002f662: mov r0,r11
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_0002f644(void)

{
  char cVar1;
  undefined1 uVar2;
  byte bVar3;
  undefined2 *unaff_r4;
  byte *unaff_r5;
  char *in_stack_00000010;
  int in_stack_00000014;
  
  while( true ) {
    FUN_000599bc();
    FUN_000270e8();
    *unaff_r4 = 0xe;
    FUN_000599bc();
    FUN_000270e8();
    in_stack_00000010 = in_stack_00000010 + 1;
    if (_DAT_0002f6e4 == in_stack_00000010) break;
    cVar1 = *in_stack_00000010;
    *unaff_r4 = (short)_DAT_0002f6d8;
    FUN_000599bc();
    FUN_000270e8();
    *unaff_r4 = (short)_DAT_0002f6e0;
    FUN_000599bc();
    FUN_000270e8();
    uVar2 = *(undefined1 *)(in_stack_00000014 + 3);
    *(undefined1 *)unaff_r4 = 2;
    *(undefined1 *)((int)unaff_r4 + 1) = uVar2;
    FUN_000599bc();
    FUN_000270e8();
    uVar2 = *(undefined1 *)(in_stack_00000014 + 4);
    *(undefined1 *)unaff_r4 = 3;
    *(undefined1 *)((int)unaff_r4 + 1) = uVar2;
    FUN_000599bc();
    FUN_000270e8();
    *unaff_r4 = 5;
    FUN_000599bc();
    FUN_000270e8();
    *unaff_r5 = 0;
    *unaff_r5 = *unaff_r5 & 199 | (*(byte *)(in_stack_00000014 + 2) & 7) << 3;
    *unaff_r5 = *unaff_r5 & 0xfb;
    *unaff_r5 = *unaff_r5 & 0xfd;
    *unaff_r5 = *unaff_r5 | 1;
    if (cVar1 == 'P') {
      *unaff_r5 = *unaff_r5 & 0x3f | 0x40;
    }
    else {
      *unaff_r5 = *unaff_r5 & 0x3f | 0x80;
    }
    bVar3 = *unaff_r5;
    *(undefined1 *)unaff_r4 = 0;
    *(byte *)((int)unaff_r4 + 1) = bVar3;
    FUN_000599bc();
    FUN_000270e8();
    *unaff_r5 = *unaff_r5 | 2;
    bVar3 = *unaff_r5;
    *(undefined1 *)unaff_r4 = 0;
    *(byte *)((int)unaff_r4 + 1) = bVar3;
  }
  return;
}
```

## `0002fb60`

- function: `PROBE_0002fb60` @ `0002fb60`

```asm
0002fb32: adds r6,#0x8
0002fb34: lsls r3,r3,#0x1
0002fb36: strh r6,[r4,r3]
0002fb38: pop {r7}
0002fb3a: mov r8,r7
0002fb3c: pop {r4,r5,r6,r7,pc}
0002fb3e: ldrb r2,[r4,#0x3]
0002fb40: cmp r2,#0x0
0002fb42: beq 0x0002fba6
0002fb44: mov r2,r12
0002fb46: ands r1,r2
0002fb48: b 0x0002fb02
0002fb4a: movs r1,#0x0
0002fb4c: b 0x0002fb04
0002fb60: ldrb r1,[r4,#0x2]
0002fb62: adds r3,#0x1
0002fb64: strb r1,[r4,r3]
0002fb66: adds r3,#0x1
0002fb68: strb r2,[r4,r3]
0002fb6a: cmp r6,#0x0
0002fb6c: beq 0x0002fbaa
0002fb6e: subs r3,#0x5
0002fb70: mov r12,r3
0002fb72: add r12,r4
0002fb74: mov r8,r12
0002fb76: b 0x0002faec
0002fb7e: movs r3,#0x28
0002fb80: adds r3,#0xff
0002fb82: strb r2,[r4,r3]
```

```c

undefined4 PROBE_0002fb60(uint param_1,undefined4 param_2,undefined1 param_3,int param_4)

{
  byte bVar1;
  uint uVar2;
  int unaff_r4;
  uint unaff_r5;
  uint unaff_r6;
  byte bVar3;
  
  *(undefined1 *)(unaff_r4 + param_4 + 1) = *(undefined1 *)(unaff_r4 + 2);
  *(undefined1 *)(unaff_r4 + param_4 + 2) = param_3;
  if (unaff_r6 == 0) {
    bVar3 = 0;
  }
  else {
    bVar3 = 0;
    uVar2 = 0;
    do {
      if (param_1 < unaff_r5) {
        bVar1 = *(byte *)(*(int *)(unaff_r4 + 0x18) + param_1);
        if (*(char *)(*(int *)(unaff_r4 + 0x18) + param_1) < '\0') {
          if (*(char *)(unaff_r4 + 3) == '\0') {
            return 0xd;
          }
          bVar1 = bVar1 & 0x7f;
        }
        bVar3 = bVar3 ^ bVar1;
      }
      else {
        bVar1 = 0;
      }
      *(byte *)(unaff_r4 + uVar2 + 0x28) = bVar1;
      param_1 = param_1 + 1;
      *(uint *)(unaff_r4 + 0xc) = param_1;
      if ((*(char *)(unaff_r4 + 0x15) == '\0') && (unaff_r5 == param_1)) {
        *(undefined1 *)(unaff_r4 + 0x127) = 0;
        *(undefined1 *)(unaff_r4 + 0x25) = 0x7d;
        *(undefined1 *)(unaff_r4 + 0x2a) = 0xf7;
        *(undefined2 *)(unaff_r4 + 0x122) = 6;
        (**(code **)(unaff_r4 + 0x128))(param_4 + -3 + unaff_r4,6);
        return 0xe;
      }
      uVar2 = uVar2 + 1 & 0xff;
    } while (uVar2 < unaff_r6);
  }
  *(byte *)(unaff_r4 + unaff_r6 + 0x28) = bVar3;
  *(undefined1 *)(unaff_r4 + unaff_r6 + 0x29) = 0xf7;
  *(short *)(unaff_r4 + 0x122) = (short)unaff_r6 + 8;
  return 0;
}
```

## `0002ee68`

- function: `PROBE_0002ee68` @ `0002ee68`

```asm
0002eddc: add r1,sp,#0x4
0002edde: bl 0x0002562c
0002ede2: cmp r0,#0x0
0002ede4: bne 0x0002edf0
0002ede6: movs r0,#0x0
0002ede8: add sp,#0xc
0002edea: pop {r4,r5,pc}
0002edec: movs r0,#0x1
0002edee: b 0x0002ede8
0002edf0: movs r2,r4
0002edf2: movs r1,r5
0002edf4: movs r0,#0x51
0002edf6: bl 0x00025650
0002edfa: b 0x0002ede8
0002ee68: lsls r2,r2,#0x2
0002ee6a: bl 0x0005a4fc
0002ee6e: movs r2,#0xfa
0002ee70: movs r5,r0
0002ee72: ldr r0,[sp,#0x0]
0002ee74: ldr r1,[sp,#0x4]
0002ee76: movs r3,#0x0
0002ee78: lsls r2,r2,#0x2
0002ee7a: bl 0x0005a4fc
0002ee7e: subs r5,r5,r0
0002ee80: str r5,[r6,#0x0]
0002ee82: movs r5,r4
0002ee84: cmp r4,r8
0002ee86: bls 0x0002ee8a
0002ee88: mov r5,r8
```

```c

undefined4
PROBE_0002ee68(undefined4 param_1,undefined4 param_2,int param_3,undefined4 param_4,
              undefined4 param_5,undefined4 param_6)

{
  int iVar1;
  int iVar2;
  uint unaff_r4;
  uint uVar3;
  int *unaff_r6;
  uint unaff_r8;
  uint unaff_r9;
  
  iVar1 = FUN_0005a4fc(param_1,param_2,param_3 << 2);
  iVar2 = FUN_0005a4fc(param_5,param_6,1000,0);
  *unaff_r6 = iVar1 - iVar2;
  while( true ) {
    uVar3 = unaff_r4;
    if (unaff_r8 < unaff_r4) {
      uVar3 = unaff_r8;
    }
    iVar1 = func_0x0002edb8(unaff_r9,&stack0x00000088,uVar3);
    if ((iVar1 == 0) ||
       (iVar1 = func_0x0005e9e0(&stack0x00000008,&stack0x00000088,uVar3), iVar1 != 0)) break;
    unaff_r9 = unaff_r9 + uVar3 & 0xffff;
    unaff_r8 = unaff_r8 - uVar3;
    if (unaff_r8 == 0) {
      return 1;
    }
  }
  return 0;
}
```

## `0002f304`

- function: `PROBE_0002f2f0` @ `0002f2f0`

```asm
0002f2ba: mov r10,r6
0002f2bc: mov r9,r5
0002f2be: mov r8,r4
0002f2c0: pop {r4,r5,r6,r7,pc}
0002f2f0: lsls r4,r4,#0x2
0002f2f2: adds r4,r6,r4
0002f2f4: ldrh r6,[r4,#0x12]
0002f2f6: ldrh r4,[r4,#0xc]
0002f2f8: mov r12,r6
0002f2fa: strb r2,[r5,#0xb]
0002f2fc: lsls r1,r1,#0x4
0002f2fe: ldrb r6,[r0,#0x6]
0002f300: adds r1,r4,r1
0002f302: ldrb r4,[r3,#0x11]
0002f304: ldrb r3,[r5,#0xe]
0002f306: muls r4,r6
0002f308: muls r3,r4
0002f30a: muls r2,r3
0002f30c: mov r3,r12
0002f30e: str r2,[sp,#0x4]
0002f310: movs r2,#0xff
0002f312: ands r2,r3
0002f314: lsls r3,r2,#0x1
0002f316: adds r3,r3,r2
0002f318: lsls r3,r3,#0x7
0002f31a: uxtb r1,r1
0002f31c: adds r3,r0,r3
0002f31e: ldr r4,[sp,#0x4]
0002f320: adds r3,r3,r1
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_0002f2f0(int param_1,char param_2,int param_3,int param_4)

{
  ushort uVar1;
  undefined2 uVar2;
  uint uVar3;
  int unaff_r4;
  int iVar4;
  int unaff_r5;
  int unaff_r6;
  
  iVar4 = unaff_r6 + unaff_r4 * 4;
  uVar1 = *(ushort *)(iVar4 + 0x12);
  uVar2 = *(undefined2 *)(iVar4 + 0xc);
  *(char *)(unaff_r5 + 0xb) = (char)param_3;
  uVar3 = uVar1 & 0xff;
  iVar4 = param_1 + uVar3 * 0x180 + (uint)(byte)((char)uVar2 + param_2 * '\x10');
  *(char *)(iVar4 + _DAT_0002f340) =
       (char)((uint)*(byte *)(param_1 + 6) * (uint)*(byte *)(param_4 + 0x11) *
              (uint)*(byte *)(unaff_r5 + 0xe) * param_3 >> 0x18);
  *(undefined1 *)(iVar4 + _DAT_0002f344) = 1;
  *(undefined1 *)(param_1 + uVar3 + _DAT_0002f348) = 1;
  return;
}
```

## `0002f788`

- function: `PROBE_0002f788` @ `0002f788`

```asm
0002f76c: movs r3,#0x0
0002f76e: lsls r2,r2,#0x2
0002f770: adds r0,r0,r2
0002f772: adcs r1,r3
0002f774: cmp r1,#0x0
0002f776: bge 0x0002f77e
0002f778: movs r0,#0x1
0002f77a: ldr r1,[0x0002f7c4]
0002f77c: rsbs r0,r0
0002f77e: movs r2,r7
0002f780: movs r3,#0x1
0002f782: mov r7,r9
0002f784: str r0,[sp,#0x8]
0002f786: str r1,[sp,#0xc]
0002f788: str r3,[sp,#0x0]
0002f78a: movs r1,r7
0002f78c: adds r3,#0x1
0002f78e: mov r0,r10
0002f790: bl 0x000270e8
0002f794: movs r2,r5
0002f796: movs r1,r5
0002f798: movs r0,r7
0002f79a: adds r2,#0xc0
0002f79c: bl 0x0002efec
0002f7a0: movs r3,#0x0
0002f7a2: strb r3,[r4,#0x0]
0002f7a4: b 0x0002f70e
0002f7c8: movs r2,#0xeb
0002f7ca: ldr r3,[0x0002f884]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_0002f788(undefined4 param_1,undefined4 param_2,undefined2 *param_3,int param_4)

{
  char *unaff_r4;
  int unaff_r5;
  byte *unaff_r6;
  uint unaff_r7;
  char *unaff_r8;
  undefined4 unaff_r10;
  int iStack00000000;
  
  do {
    iStack00000000 = param_4;
    FUN_000270e8(unaff_r10,unaff_r7,param_3,param_4 + 1);
    func_0x0002efec(unaff_r7,unaff_r5,unaff_r5 + 0xc0);
    *unaff_r4 = '\0';
    param_3 = _DAT_0002f7b8;
    do {
      unaff_r4 = unaff_r4 + 1;
      unaff_r6 = unaff_r6 + 1;
      unaff_r5 = unaff_r5 + 0x180;
      if (unaff_r4 == unaff_r8) {
        return;
      }
    } while (*unaff_r4 == '\0');
    unaff_r7 = (uint)*unaff_r6;
    *_DAT_0002f7b8 = (short)_DAT_0002f7bc;
    FUN_000599bc();
    unaff_r10 = _DAT_0002f7c0;
    iStack00000000 = 1;
    FUN_000270e8(_DAT_0002f7c0,unaff_r7,param_3,2);
    *param_3 = 0x1fd;
    FUN_000599bc();
    param_4 = 1;
  } while( true );
}
```

## `0002f7b8`

- function: `PROBE_0002f7b8` @ `0002f7b8`

```asm
0002f786: str r1,[sp,#0xc]
0002f788: str r3,[sp,#0x0]
0002f78a: movs r1,r7
0002f78c: adds r3,#0x1
0002f78e: mov r0,r10
0002f790: bl 0x000270e8
0002f794: movs r2,r5
0002f796: movs r1,r5
0002f798: movs r0,r7
0002f79a: adds r2,#0xc0
0002f79c: bl 0x0002efec
0002f7a0: movs r3,#0x0
0002f7a2: strb r3,[r4,#0x0]
0002f7a4: b 0x0002f70e
0002f7b8: str r7,[sp,#0x260]
0002f7ba: movs r0,#0x0
0002f7bc: stmia r5,{r1,r2,r3,r4,r5,r6,r7}
0002f7c8: movs r2,#0xeb
0002f7ca: ldr r3,[0x0002f884]
0002f7cc: push {r4,r5,r6,r7,lr}
0002f7ce: lsls r2,r2,#0x4
0002f7d0: mov r6,r8
0002f7d2: mov lr,r10
0002f7d4: mov r7,r9
0002f7d6: adds r4,r3,r2
0002f7d8: ldr r2,[0x0002f888]
0002f7da: push {r6,r7,lr}
0002f7dc: adds r5,r3,r2
0002f7de: ldr r2,[0x0002f88c]
```

```c

/* WARNING: Control flow encountered bad instruction data */

void PROBE_0002f7b8(undefined4 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)

{
  undefined4 unaff_r4;
  undefined4 *unaff_r5;
  undefined4 unaff_r6;
  undefined4 unaff_r7;
  
  *unaff_r5 = param_2;
  unaff_r5[1] = param_3;
  unaff_r5[2] = param_4;
  unaff_r5[3] = unaff_r4;
  unaff_r5[4] = unaff_r5;
  unaff_r5[5] = unaff_r6;
  unaff_r5[6] = unaff_r7;
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}
```

## `0002f7ec`

- function: `PROBE_0002f7ec` @ `0002f7ec`

```asm
0002f7d0: mov r6,r8
0002f7d2: mov lr,r10
0002f7d4: mov r7,r9
0002f7d6: adds r4,r3,r2
0002f7d8: ldr r2,[0x0002f888]
0002f7da: push {r6,r7,lr}
0002f7dc: adds r5,r3,r2
0002f7de: ldr r2,[0x0002f88c]
0002f7e0: ldr r6,[0x0002f890]
0002f7e2: adds r3,r3,r2
0002f7e4: mov r8,r3
0002f7e6: sub sp,#0x10
0002f7e8: ldrb r3,[r4,#0x0]
0002f7ea: cmp r3,#0x0
0002f7ec: bne 0x0002f806
0002f7ee: adds r5,#0x81
0002f7f0: adds r4,#0x1
0002f7f2: adds r6,#0x1
0002f7f4: adds r5,#0xff
0002f7f6: cmp r4,r8
0002f7f8: bne 0x0002f7e8
0002f7fa: add sp,#0x10
0002f7fc: pop {r5,r6,r7}
0002f7fe: mov r10,r7
0002f800: mov r9,r6
0002f802: mov r8,r5
0002f804: pop {r4,r5,r6,r7,pc}
0002f806: ldrb r3,[r6,#0x0]
0002f808: ldr r7,[0x0002f894]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_0002f7ec(void)

{
  undefined1 uVar1;
  undefined2 *puVar2;
  undefined4 uVar3;
  char *unaff_r4;
  int unaff_r5;
  undefined1 *unaff_r6;
  char *unaff_r8;
  char in_ZR;
  
  while( true ) {
    puVar2 = _DAT_0002f894;
    if (in_ZR == '\0') {
      uVar1 = *unaff_r6;
      *_DAT_0002f894 = (short)_DAT_0002f898;
      FUN_000599bc();
      uVar3 = _DAT_0002f89c;
      FUN_000270e8(_DAT_0002f89c,uVar1,puVar2,2);
      *puVar2 = (short)_DAT_0002f8a4;
      FUN_000599bc();
      FUN_000270e8(uVar3,uVar1,puVar2,2);
      func_0x0002efec(uVar1,unaff_r5,unaff_r5 + 0xc0);
      *unaff_r4 = '\0';
    }
    unaff_r4 = unaff_r4 + 1;
    unaff_r6 = unaff_r6 + 1;
    unaff_r5 = unaff_r5 + 0x180;
    if (unaff_r4 == unaff_r8) break;
    in_ZR = *unaff_r4 == '\0';
  }
  return;
}
```

## `0002f864`

- function: `PROBE_0002f7ec` @ `0002f7ec`

```asm
0002f848: movs r2,#0xfa
0002f84a: movs r3,#0x0
0002f84c: lsls r2,r2,#0x2
0002f84e: adds r0,r0,r2
0002f850: adcs r1,r3
0002f852: cmp r1,#0x0
0002f854: bge 0x0002f85c
0002f856: movs r0,#0x1
0002f858: ldr r1,[0x0002f8a0]
0002f85a: rsbs r0,r0
0002f85c: movs r2,r7
0002f85e: movs r3,#0x1
0002f860: mov r7,r9
0002f862: str r0,[sp,#0x8]
0002f864: str r1,[sp,#0xc]
0002f866: str r3,[sp,#0x0]
0002f868: movs r1,r7
0002f86a: adds r3,#0x1
0002f86c: mov r0,r10
0002f86e: bl 0x000270e8
0002f872: movs r2,r5
0002f874: movs r1,r5
0002f876: movs r0,r7
0002f878: adds r2,#0xc0
0002f87a: bl 0x0002efec
0002f87e: movs r3,#0x0
0002f880: strb r3,[r4,#0x0]
0002f882: b 0x0002f7ee
0002f8a8: push {r4,r5,r6,r7,lr}
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_0002f7ec(void)

{
  undefined1 uVar1;
  undefined2 *puVar2;
  undefined4 uVar3;
  char *unaff_r4;
  int unaff_r5;
  undefined1 *unaff_r6;
  char *unaff_r8;
  char in_ZR;
  
  while( true ) {
    puVar2 = _DAT_0002f894;
    if (in_ZR == '\0') {
      uVar1 = *unaff_r6;
      *_DAT_0002f894 = (short)_DAT_0002f898;
      FUN_000599bc();
      uVar3 = _DAT_0002f89c;
      FUN_000270e8(_DAT_0002f89c,uVar1,puVar2,2);
      *puVar2 = (short)_DAT_0002f8a4;
      FUN_000599bc();
      FUN_000270e8(uVar3,uVar1,puVar2,2);
      func_0x0002efec(uVar1,unaff_r5,unaff_r5 + 0xc0);
      *unaff_r4 = '\0';
    }
    unaff_r4 = unaff_r4 + 1;
    unaff_r6 = unaff_r6 + 1;
    unaff_r5 = unaff_r5 + 0x180;
    if (unaff_r4 == unaff_r8) break;
    in_ZR = *unaff_r4 == '\0';
  }
  return;
}
```

## `0002f908`

- function: `PROBE_0002f908` @ `0002f908`

```asm
0002f8ea: mov r10,r6
0002f8ec: mov r9,r5
0002f8ee: mov r8,r4
0002f8f0: pop {r4,r5,r6,r7,pc}
0002f8f2: mov r3,r11
0002f8f4: ldrb r3,[r3,#0x0]
0002f8f6: mov r9,r3
0002f8f8: ldr r3,[0x0002f9dc]
0002f8fa: mov r10,r3
0002f8fc: mov r2,r10
0002f8fe: ldr r3,[0x0002f9e0]
0002f900: strh r3,[r2,#0x0]
0002f902: bl 0x000599bc
0002f906: ldr r3,[0x0002f9e4]
0002f908: movs r2,#0xfa
0002f90a: mov r8,r3
0002f90c: movs r3,#0x0
0002f90e: lsls r2,r2,#0x2
0002f910: adds r0,r0,r2
0002f912: adcs r1,r3
0002f914: cmp r1,#0x0
0002f916: bge 0x0002f91e
0002f918: movs r0,#0x1
0002f91a: ldr r1,[0x0002f9e8]
0002f91c: rsbs r0,r0
0002f91e: movs r3,#0x1
0002f920: str r0,[sp,#0x8]
0002f922: str r1,[sp,#0xc]
0002f924: mov r2,r10
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_0002f908(undefined4 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)

{
  char cVar1;
  char *unaff_r4;
  char *pcVar2;
  char cVar3;
  char *unaff_r7;
  uint unaff_r9;
  char *unaff_r10;
  byte *unaff_r11;
  longlong lVar4;
  undefined4 uStack00000000;
  undefined4 uStack00000008;
  undefined4 uStack0000000c;
  char *in_stack_00000014;
  
  lVar4 = CONCAT44(param_2,param_1);
  do {
    _uStack00000008 = lVar4 + 1000;
    if ((longlong)_uStack00000008 < 0) {
      _uStack00000008 = CONCAT44(_DAT_0002f9e8,0xffffffff);
    }
    uStack00000000 = 1;
    FUN_000270e8(param_4,unaff_r9,unaff_r10,2);
    unaff_r10[0] = -3;
    unaff_r10[1] = '\0';
    lVar4 = FUN_000599bc();
    _uStack00000008 = lVar4 + 1000;
    if ((longlong)_uStack00000008 < 0) {
      _uStack00000008 = CONCAT44(_DAT_0002f9e8,0xffffffff);
    }
    uStack00000000 = 1;
    FUN_000270e8(param_4,unaff_r9,unaff_r10,2);
    cVar3 = '\0';
    pcVar2 = unaff_r7;
    do {
      while (pcVar2[0x18] == '\x01') {
        cVar1 = *pcVar2;
        *unaff_r10 = cVar3;
        unaff_r10[1] = cVar1;
        lVar4 = FUN_000599bc();
        _uStack00000008 = lVar4 + 1000;
        if (0x7fffffffffffffff < _uStack00000008) {
          _uStack00000008 = CONCAT44(_DAT_0002f9e8,0xffffffff);
        }
        cVar3 = cVar3 + '\x01';
        uStack00000000 = 1;
        FUN_000270e8(param_4,unaff_r9,unaff_r10,2);
        pcVar2 = pcVar2 + 1;
        if (cVar3 == '\x18') goto LAB_0002f9c0;
      }
      cVar3 = cVar3 + '\x01';
      pcVar2 = pcVar2 + 1;
    } while (cVar3 != '\x18');
LAB_0002f9c0:
    *unaff_r4 = '\0';
    unaff_r10 = _DAT_0002f9dc;
    do {
      unaff_r11 = unaff_r11 + 1;
      unaff_r4 = unaff_r4 + 1;
      unaff_r7 = unaff_r7 + 0x30;
      if (unaff_r4 == in_stack_00000014) {
        return;
      }
    } while (*unaff_r4 == '\0');
    unaff_r9 = (uint)*unaff_r11;
    *(short *)_DAT_0002f9dc = (short)_DAT_0002f9e0;
    lVar4 = FUN_000599bc();
    param_4 = _DAT_0002f9e4;
  } while( true );
}
```

## `0002f968`

- function: `PROBE_0002f908` @ `0002f908`

```asm
0002f94a: movs r0,#0x1
0002f94c: ldr r1,[0x0002f9e8]
0002f94e: rsbs r0,r0
0002f950: movs r3,#0x1
0002f952: str r0,[sp,#0x8]
0002f954: str r1,[sp,#0xc]
0002f956: mov r2,r10
0002f958: str r3,[sp,#0x0]
0002f95a: mov r1,r9
0002f95c: adds r3,#0x1
0002f95e: mov r0,r8
0002f960: bl 0x000270e8
0002f964: mov r3,r10
0002f966: movs r5,r7
0002f968: mov r10,r4
0002f96a: movs r6,#0x0
0002f96c: movs r4,r3
0002f96e: b 0x0002f97a
0002f970: adds r6,#0x1
0002f972: uxtb r6,r6
0002f974: adds r5,#0x1
0002f976: cmp r6,#0x18
0002f978: beq 0x0002f9c0
0002f97a: ldrb r3,[r5,#0x18]
0002f97c: cmp r3,#0x1
0002f97e: bne 0x0002f970
0002f980: ldrb r3,[r5,#0x0]
0002f982: strb r6,[r4,#0x0]
0002f984: strb r3,[r4,#0x1]
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void PROBE_0002f908(undefined4 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)

{
  char cVar1;
  char *unaff_r4;
  char *pcVar2;
  char cVar3;
  char *unaff_r7;
  uint unaff_r9;
  char *unaff_r10;
  byte *unaff_r11;
  longlong lVar4;
  undefined4 uStack00000000;
  undefined4 uStack00000008;
  undefined4 uStack0000000c;
  char *in_stack_00000014;
  
  lVar4 = CONCAT44(param_2,param_1);
  do {
    _uStack00000008 = lVar4 + 1000;
    if ((longlong)_uStack00000008 < 0) {
      _uStack00000008 = CONCAT44(_DAT_0002f9e8,0xffffffff);
    }
    uStack00000000 = 1;
    FUN_000270e8(param_4,unaff_r9,unaff_r10,2);
    unaff_r10[0] = -3;
    unaff_r10[1] = '\0';
    lVar4 = FUN_000599bc();
    _uStack00000008 = lVar4 + 1000;
    if ((longlong)_uStack00000008 < 0) {
      _uStack00000008 = CONCAT44(_DAT_0002f9e8,0xffffffff);
    }
    uStack00000000 = 1;
    FUN_000270e8(param_4,unaff_r9,unaff_r10,2);
    cVar3 = '\0';
    pcVar2 = unaff_r7;
    do {
      while (pcVar2[0x18] == '\x01') {
        cVar1 = *pcVar2;
        *unaff_r10 = cVar3;
        unaff_r10[1] = cVar1;
        lVar4 = FUN_000599bc();
        _uStack00000008 = lVar4 + 1000;
        if (0x7fffffffffffffff < _uStack00000008) {
          _uStack00000008 = CONCAT44(_DAT_0002f9e8,0xffffffff);
        }
        cVar3 = cVar3 + '\x01';
        uStack00000000 = 1;
        FUN_000270e8(param_4,unaff_r9,unaff_r10,2);
        pcVar2 = pcVar2 + 1;
        if (cVar3 == '\x18') goto LAB_0002f9c0;
      }
      cVar3 = cVar3 + '\x01';
      pcVar2 = pcVar2 + 1;
    } while (cVar3 != '\x18');
LAB_0002f9c0:
    *unaff_r4 = '\0';
    unaff_r10 = _DAT_0002f9dc;
    do {
      unaff_r11 = unaff_r11 + 1;
      unaff_r4 = unaff_r4 + 1;
      unaff_r7 = unaff_r7 + 0x30;
      if (unaff_r4 == in_stack_00000014) {
        return;
      }
    } while (*unaff_r4 == '\0');
    unaff_r9 = (uint)*unaff_r11;
    *(short *)_DAT_0002f9dc = (short)_DAT_0002f9e0;
    lVar4 = FUN_000599bc();
    param_4 = _DAT_0002f9e4;
  } while( true );
}
```

