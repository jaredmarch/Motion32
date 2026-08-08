# Motion 32 Native Mode Firmware Probe

- Program: `motionupgrade.bin`
- Language: `ARM:LE:32:Cortex`

## Raw `8f 00 00` Pattern Hits

- `000890dc` — no containing function
- `000a26f1` — no containing function
- `000a88f8` — no containing function

## Functions Using Interesting Constants

- `0x08`: 489 functions
  - `FUN_000014e4` @ `000014e4`
  - `FUN_000015fc` @ `000015fc`
  - `FUN_0000179c` @ `0000179c`
  - `FUN_00001880` @ `00001880`
  - `FUN_000018d8` @ `000018d8`
  - `FUN_00001950` @ `00001950`
  - `FUN_00001b30` @ `00001b30`
  - `FUN_00001bf0` @ `00001bf0`
  - `FUN_00001c8c` @ `00001c8c`
  - `FUN_00001cfc` @ `00001cfc`
  - `FUN_00001d28` @ `00001d28`
  - `FUN_00001d54` @ `00001d54`
  - `FUN_00001d6c` @ `00001d6c`
  - `FUN_00001d94` @ `00001d94`
  - `FUN_00001dc0` @ `00001dc0`
  - `FUN_00001e5c` @ `00001e5c`
  - `FUN_0000240c` @ `0000240c`
  - `FUN_00002618` @ `00002618`
  - `FUN_000026f4` @ `000026f4`
  - `FUN_000027a0` @ `000027a0`
  - ...
- `0x20`: 166 functions
  - `FUN_000015fc` @ `000015fc`
  - `FUN_000018d8` @ `000018d8`
  - `FUN_00001950` @ `00001950`
  - `FUN_0000240c` @ `0000240c`
  - `FUN_0000290c` @ `0000290c`
  - `FUN_000030cc` @ `000030cc`
  - `FUN_0000408c` @ `0000408c`
  - `FUN_000041fc` @ `000041fc`
  - `FUN_00004690` @ `00004690`
  - `FUN_00004914` @ `00004914`
  - `FUN_00004dde` @ `00004dde`
  - `FUN_00004e3a` @ `00004e3a`
  - `FUN_00005636` @ `00005636`
  - `FUN_00005854` @ `00005854`
  - `FUN_00005abc` @ `00005abc`
  - `FUN_00005b7c` @ `00005b7c`
  - `FUN_00005cc0` @ `00005cc0`
  - `FUN_00005d34` @ `00005d34`
  - `FUN_00005f2c` @ `00005f2c`
  - `FUN_0000657c` @ `0000657c`
  - ...
- `0x21`: 39 functions
  - `FUN_000015fc` @ `000015fc`
  - `FUN_000016b8` @ `000016b8`
  - `FUN_0000179c` @ `0000179c`
  - `FUN_00001880` @ `00001880`
  - `FUN_000018d8` @ `000018d8`
  - `FUN_00001950` @ `00001950`
  - `FUN_000019e8` @ `000019e8`
  - `FUN_00001b30` @ `00001b30`
  - `FUN_00001bf0` @ `00001bf0`
  - `FUN_00001c8c` @ `00001c8c`
  - `FUN_00001cfc` @ `00001cfc`
  - `FUN_0000290c` @ `0000290c`
  - `FUN_00002ae8` @ `00002ae8`
  - `FUN_00003428` @ `00003428`
  - `FUN_00003508` @ `00003508`
  - `FUN_00003544` @ `00003544`
  - `FUN_00003918` @ `00003918`
  - `FUN_0000408c` @ `0000408c`
  - `FUN_000041fc` @ `000041fc`
  - `FUN_00005f2c` @ `00005f2c`
  - ...
- `0x22`: 20 functions
  - `FUN_000015fc` @ `000015fc`
  - `FUN_0000290c` @ `0000290c`
  - `FUN_000045c0` @ `000045c0`
  - `FUN_00004914` @ `00004914`
  - `FUN_00005f2c` @ `00005f2c`
  - `FUN_0000657c` @ `0000657c`
  - `FUN_00032b10` @ `00032b10`
  - `FUN_0003b114` @ `0003b114`
  - `FUN_0003d818` @ `0003d818`
  - `FUN_0003eab0` @ `0003eab0`
  - `FUN_00040156` @ `00040156`
  - `FUN_0004777c` @ `0004777c`
  - `FUN_0004a930` @ `0004a930`
  - `FUN_0004db7c` @ `0004db7c`
  - `FUN_0004e190` @ `0004e190`
  - `FUN_0004ebe4` @ `0004ebe4`
  - `FUN_0005d780` @ `0005d780`
  - `FUN_0005f244` @ `0005f244`
  - `FUN_0005f7f8` @ `0005f7f8`
  - `FUN_0005f964` @ `0005f964`
- `0x24`: 145 functions
  - `FUN_0000179c` @ `0000179c`
  - `FUN_000018d8` @ `000018d8`
  - `FUN_000019e8` @ `000019e8`
  - `FUN_00001b30` @ `00001b30`
  - `FUN_0000240c` @ `0000240c`
  - `FUN_000028d0` @ `000028d0`
  - `FUN_0000290c` @ `0000290c`
  - `FUN_0000408c` @ `0000408c`
  - `FUN_000041fc` @ `000041fc`
  - `FUN_00004690` @ `00004690`
  - `FUN_00004914` @ `00004914`
  - `FUN_00004dde` @ `00004dde`
  - `FUN_00005636` @ `00005636`
  - `FUN_00005854` @ `00005854`
  - `FUN_00005abc` @ `00005abc`
  - `FUN_00005b7c` @ `00005b7c`
  - `FUN_00005cc0` @ `00005cc0`
  - `FUN_00005d34` @ `00005d34`
  - `FUN_00005f2c` @ `00005f2c`
  - `FUN_0000657c` @ `0000657c`
  - ...
- `0x26`: 12 functions
  - `FUN_000015fc` @ `000015fc`
  - `FUN_00001950` @ `00001950`
  - `FUN_0000290c` @ `0000290c`
  - `FUN_0000408c` @ `0000408c`
  - `FUN_000041fc` @ `000041fc`
  - `FUN_00004914` @ `00004914`
  - `FUN_00009304` @ `00009304`
  - `FUN_00032b10` @ `00032b10`
  - `FUN_0003c6cc` @ `0003c6cc`
  - `FUN_0003d8a0` @ `0003d8a0`
  - `FUN_0004962c` @ `0004962c`
  - `FUN_0004990c` @ `0004990c`
- `0x7e`: 6 functions
  - `FUN_00052d50` @ `00052d50`
  - `FUN_000547c4` @ `000547c4`
  - `FUN_00054d98` @ `00054d98`
  - `FUN_0005ba44` @ `0005ba44`
  - `FUN_0005f274` @ `0005f274`
  - `FUN_0005fdb0` @ `0005fdb0`
- `0x7f`: 20 functions
  - `FUN_00001eec` @ `00001eec`
  - `FUN_0000408c` @ `0000408c`
  - `FUN_00005abc` @ `00005abc`
  - `FUN_00006808` @ `00006808`
  - `FUN_00006b00` @ `00006b00`
  - `FUN_00006cb4` @ `00006cb4`
  - `FUN_0002164c` @ `0002164c`
  - `FUN_00022b70` @ `00022b70`
  - `FUN_000437a8` @ `000437a8`
  - `FUN_00047e7c` @ `00047e7c`
  - `FUN_0005064c` @ `0005064c`
  - `FUN_0005070c` @ `0005070c`
  - `FUN_00050978` @ `00050978`
  - `FUN_00050d0c` @ `00050d0c`
  - `FUN_000518aa` @ `000518aa`
  - `FUN_00051912` @ `00051912`
  - `FUN_00051b20` @ `00051b20`
  - `FUN_000529d2` @ `000529d2`
  - `FUN_0005d6d0` @ `0005d6d0`
  - `FUN_0005f274` @ `0005f274`
- `0x8f`: 3 functions
  - `FUN_0002164c` @ `0002164c`
  - `FUN_0003bb58` @ `0003bb58`
  - `FUN_0003e600` @ `0003e600`
- `0xf0`: 14 functions
  - `FUN_000020a4` @ `000020a4`
  - `FUN_00021f24` @ `00021f24`
  - `FUN_00022484` @ `00022484`
  - `FUN_00031730` @ `00031730`
  - `FUN_000328b0` @ `000328b0`
  - `FUN_00033b50` @ `00033b50`
  - `FUN_00036738` @ `00036738`
  - `FUN_00036f68` @ `00036f68`
  - `FUN_00037334` @ `00037334`
  - `FUN_0003782c` @ `0003782c`
  - `FUN_00043fbc` @ `00043fbc`
  - `FUN_00047bb4` @ `00047bb4`
  - `FUN_00047db4` @ `00047db4`
  - `FUN_00051aae` @ `00051aae`
- `0xf7`: 8 functions
  - `FUN_00002030` @ `00002030`
  - `FUN_000020a4` @ `000020a4`
  - `FUN_00006244` @ `00006244`
  - `FUN_0000657c` @ `0000657c`
  - `FUN_00006808` @ `00006808`
  - `FUN_00006b00` @ `00006b00`
  - `FUN_00006cb4` @ `00006cb4`
  - `FUN_0002164c` @ `0002164c`

## Targeted `0x8f` Constant Functions

### `FUN_0002164c` @ `0002164c`

```asm
00021628: strh r0,[r2,r1]
0002162a: ldr r2,[0x00021648]
0002162c: ldr r0,[r2,#0x0]
0002162e: cmp r0,#0x0
00021630: bne 0x00021608
00021632: b 0x00021610
0002164c: push {r4,r5,r6,r7,lr}
0002164e: mov lr,r8
00021650: push {lr}
00021652: movs r0,#0x17
00021654: sub sp,#0x18
00021656: bl 0x0002ec30
0002165a: uxtb r3,r0
```


```c

undefined4 FUN_0002164c(void)

{
  undefined1 *puVar1;
  undefined2 *puVar2;
  byte bVar3;
  int iVar4;
  int iVar5;
  ushort uVar6;
  ushort local_1a;
  
  bVar3 = FUN_0002ec30(0x17);
  iVar4 = FUN_0002ec30(1);
  if (iVar4 == 4) {
    iVar4 = FUN_0002ea70(bVar3,&local_1a);
    puVar1 = DAT_00021750;
    if (iVar4 != 0) {
      *DAT_00021750 = 2;
      puVar1[1] = (char)((local_1a & 0xfff) >> 0xb);
      *(undefined2 *)(puVar1 + 2) = *(undefined2 *)(*DAT_00021754 + (uint)bVar3 * 6 + 4);
      *(short *)(puVar1 + 4) = (short)((local_1a & 0x7ff) >> 4);
      FUN_00021264(0,5);
      FUN_000212ec(0,3,0x2b,3,bVar3 + 0x2b,local_1a >> 4);
    }
  }
  else {
    iVar4 = FUN_0002ec30(1);
    if ((iVar4 == 6) &&
       (iVar5 = FUN_0002ea70(bVar3,&local_1a), iVar4 = DAT_0002175c, puVar2 = DAT_00021758,
       iVar5 != 0)) {
      uVar6 = local_1a >> 7 & 0x7f;
      *DAT_00021758 = 0x8f0;
      *(undefined1 *)(puVar2 + 1) = *(undefined1 *)(iVar4 + 1);
      *(char *)((int)puVar2 + 7) = (char)(local_1a & 0x7f);
      *(undefined1 *)(puVar2 + 2) = 0x2d;
      *(undefined1 *)((int)puVar2 + 3) = 0x10;
      *(byte *)((int)puVar2 + 5) = bVar3;
      *(char *)(puVar2 + 3) = (char)uVar6;
      *(undefined1 *)(puVar2 + 4) = 0xf7;
      FUN_0002754c(0,puVar2,9);
      *puVar2 = 0x8f0;
      *(undefined1 *)(puVar2 + 1) = *(undefined1 *)(iVar4 + 1);
      *(undefined1 *)((int)puVar2 + 3) = 0x10;
      *(undefined1 *)(puVar2 + 2) = 0x2d;
      *(byte *)((int)puVar2 + 5) = bVar3;
      puVar2[3] = (local_1a & 0x7f) << 8 | uVar6;
      *(undefined1 *)(puVar2 + 4) = 0xf7;
      FUN_0002754c(2,puVar2,9);
    }
  }
  return 0;
}
```

### `FUN_0003bb58` @ `0003bb58`

```asm
0003bb48: cmp r3,#0x0
0003bb4a: beq 0x0003bb50
0003bb4c: blx r3
0003bb4e: pop {r4,pc}
0003bb50: movs r0,#0x0
0003bb52: b 0x0003bb4e
0003bb58: push {r4,r5,lr}
0003bb5a: movs r4,r0
0003bb5c: sub sp,#0x24
0003bb5e: cmp r0,#0x0
0003bb60: beq 0x0003bb92
0003bb62: ldr r5,[r0,#0x18]
0003bb64: cmp r5,#0x0
```


```c

void FUN_0003bb58(int param_1,undefined1 *param_2)

{
  code *pcVar1;
  int iVar2;
  undefined1 auStack_20 [20];
  
  if (param_1 == 0) {
    FUN_000468e8(3,DAT_0003bbd8,0x8f,DAT_0003bbd0,DAT_0003bbd4,DAT_0003bbcc,DAT_0003bbc8);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar2 = *(int *)(param_1 + 0x18);
  if (iVar2 != 0) {
    pcVar1 = *(code **)(iVar2 + 0x10);
    if (pcVar1 != (code *)0x0) {
      if (param_2 == (undefined1 *)0x0) {
        FUN_00045064(auStack_20,0,0,*(ushort *)(param_1 + 4) - 1,*(ushort *)(param_1 + 6) - 1);
        pcVar1 = *(code **)(iVar2 + 0x10);
        param_2 = auStack_20;
      }
      (*pcVar1)(param_1,param_2);
    }
    return;
  }
  FUN_000468e8(3,DAT_0003bbd8,0x90,DAT_0003bbd0,DAT_0003bbd4,DAT_0003bbdc,DAT_0003bbc8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

### `FUN_0003e600` @ `0003e600`

```asm
0003e5f4: adds r0,#0x80
0003e5f6: asrs r0,r0,#0x8
0003e5f8: subs r2,r0,r5
0003e5fa: adds r5,r5,r0
0003e5fc: subs r5,r5,r3
0003e5fe: b 0x0003e5d6
0003e600: push {r4,r5,r6,r7,lr}
0003e602: mov r6,r9
0003e604: mov r5,r8
0003e606: mov lr,r11
0003e608: mov r7,r10
0003e60a: movs r3,#0x3c
0003e60c: push {r5,r6,r7,lr}
```


```c

void FUN_0003e600(int param_1,int param_2,undefined4 *param_3)

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
  
  iVar6 = DAT_0003e904;
  puVar21 = (undefined4 *)(&stack0xffffffdc + DAT_0003e904);
  puVar22 = (undefined4 *)(&stack0xffffffdc + DAT_0003e904);
  piVar23 = (int *)(&stack0xffffffdc + DAT_0003e904);
  puVar24 = (undefined4 *)(&stack0xffffffdc + DAT_0003e904);
  puVar25 = (undefined4 *)(&stack0xffffffdc + DAT_0003e904);
  piVar26 = (int *)(&stack0xffffffdc + DAT_0003e904);
  puVar27 = (undefined4 *)(&stack0xffffffdc + DAT_0003e904);
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
  puVar1 = (undefined4 *)(&stack0x00000034 + DAT_0003e904);
  uVar9 = param_3[1];
  uVar20 = param_3[2];
  *puVar1 = *param_3;
  *(undefined4 *)(&stack0x00000038 + DAT_0003e904) = uVar9;
  *(undefined4 *)(&stack0x0000003c + DAT_0003e904) = uVar20;
  *(undefined4 *)(&stack0x00000040 + DAT_0003e904) = param_3[3];
  iVar7 = FUN_000450d4(&stack0x00000044 + DAT_0003e904,puVar1,param_1 + 0x38);
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
      FUN_0003d970(&stack0x00000188 + iVar6);
      (&stack0x000001b0)[iVar6] = *(undefined1 *)(param_2 + 0x3c);
      *(undefined2 *)(&stack0x000001a8 + iVar6) = *(undefined2 *)(param_2 + 0x1c);
      (&stack0x000001aa)[iVar6] = *(undefined1 *)(param_2 + 0x1e);
      *(undefined4 *)(&stack0x000001ac + iVar6) = *(undefined4 *)(&stack0xfffffff0 + iVar6);
      *(undefined4 *)(&stack0x000001a4 + iVar6) = DAT_0003ea98;
      (&stack0x000001b1)[iVar6] = (&stack0x000001b1)[iVar6] & 0xe0 | 0xf;
      FUN_0003eab0(param_1,&stack0x00000188 + iVar6,puVar1);
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
  FUN_0005beec(&stack0x00000064 + iVar6,0,0x10);
  uVar20 = *(undefined4 *)(param_2 + 0x30);
  uVar9 = *(undefined4 *)(param_2 + 0x2c);
  *puVar21 = *(undefined4 *)(&stack0xffffffec + iVar6);
  FUN_00042f7c(&stack0x00000188 + iVar6,uVar9,uVar20,*(undefined4 *)(&stack0xfffffff4 + iVar6));
  *(undefined1 **)(&stack0x00000064 + iVar6) = &stack0x00000188 + iVar6;
  FUN_00043030(&stack0x000000a4 + iVar6,puVar1,DAT_0003e908,0);
  *(undefined1 **)(&stack0x00000068 + iVar6) = &stack0x000000a4 + iVar6;
  iVar19 = FUN_000458e4(&stack0x00000054 + iVar6);
  if ((iVar19 < 1) || (iVar19 = FUN_000458f0(&stack0x00000054 + iVar6), iVar19 < 1)) {
    *(undefined4 *)(&stack0xfffffffc + iVar6) = 0;
  }
  else {
    FUN_00043030(&stack0x000000c8 + iVar6,&stack0x00000054 + iVar6,DAT_0003e908,1);
    *(undefined1 **)(&stack0x0000006c + iVar6) = &stack0x000000c8 + iVar6;
  }
  iVar19 = FUN_000458f0(&stack0x00000044 + iVar6);
  uVar9 = FUN_000458e4(&stack0x00000044 + iVar6);
  *(undefined4 *)(&stack0x00000000 + iVar6) = uVar9;
  iVar7 = FUN_0004cea4();
  piVar2 = (int *)(&stack0x00000074 + iVar6);
  FUN_0005bef8(piVar2,&stack0x00000044 + iVar6,0x10);
  FUN_0005beec(&stack0x00000114 + iVar6,0,0x28);
  *(int *)(&stack0x00000128 + iVar6) = iVar7;
  iVar10 = *(int *)(param_2 + 0x38);
  (&stack0x00000124)[iVar6] = *(undefined1 *)(param_2 + 0x3c);
  *(int **)(&stack0x00000110 + iVar6) = piVar2;
  *(int **)(&stack0x00000130 + iVar6) = piVar2;
  if (iVar10 == 0) {
LAB_0003e7da:
    FUN_0005bef8(&stack0x00000125 + iVar6,param_2 + 0x1c,3);
  }
  else {
    iVar10 = FUN_0003e060(&stack0x0000013c + iVar6,iVar10,0);
    if ((iVar10 == 0) || (iVar10 = *(int *)(&stack0x00000168 + iVar6), iVar10 == 0)) {
      *puVar22 = DAT_0003e90c;
      FUN_000468e8(2,DAT_0003e914,0x86,DAT_0003e910);
      goto LAB_0003e7da;
    }
    *(undefined4 *)(&stack0x00000014 + iVar6) = 0;
    *(undefined4 *)(&stack0x00000018 + iVar6) = 0;
    uVar5 = *(ushort *)(iVar10 + 4);
    *(uint *)(&stack0x0000001c + iVar6) = uVar5 - 1;
    iVar11 = *(int *)(param_2 + 0x2c);
    *(uint *)(&stack0x00000020 + iVar6) = *(ushort *)(iVar10 + 6) - 1;
    uVar13 = (uint)(uVar5 >> 1);
    FUN_000450b8(&stack0x00000014 + iVar6,iVar11 - uVar13,*(int *)(param_2 + 0x30) - uVar13);
    *(undefined1 **)(&stack0x00000120 + iVar6) = &stack0x00000014 + iVar6;
    iVar11 = *(int *)(&stack0x00000168 + iVar6);
    iVar10 = *(int *)(iVar11 + 0x10);
    *(int *)(&stack0x00000114 + iVar6) = iVar10;
    uVar5 = *(ushort *)(iVar11 + 8);
    *(uint *)(&stack0x00000118 + iVar6) = (uint)uVar5;
    if (*(char *)(iVar11 + 1) == '\x14') {
      (&stack0x0000011c)[iVar6] = 0x12;
      iVar11 = FUN_000458f0(&stack0x00000014 + iVar6);
      iVar10 = iVar10 + (uint)uVar5 * iVar11;
      goto LAB_0003e7f0;
/* ... truncated ... */
```


## Highest-Signal Multi-Constant Functions

### `FUN_0000290c` @ `0000290c`

- constants: `0x08` `0x22` `0x20` `0x26` `0x24` `0x21`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_0000290c(void)

{
  int iVar1;
  char cVar2;
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
  
  if (DAT_2000462b == '\0') {
    iVar1 = 0x21;
  }
  else {
    iVar1 = 7;
    if (_DAT_d0f52800 == 0x43545355) {
      FUN_0000a568(&local_48,0,0x28);
      cVar2 = -0x80;
      do {
        iVar1 = FUN_000048e8(0x2b007de3);
        if (iVar1 != 0) {
          return iVar1;
        }
        do {
        } while (DAT_20006465 == '\0');
        DAT_20006465 = '\0';
        iVar1 = FUN_00004ce8(0x2b007de3,0,0,0);
        if (iVar1 != 0) {
          return iVar1;
        }
        if (((((((DAT_20004628 != '\0') &&
                (local_48 = local_48 + *(ushort *)(_DAT_d0f52830 + 2), DAT_20004628 != '\x01')) &&
               (local_44 = local_44 + *(ushort *)(_DAT_d0f52830 + 6), DAT_20004628 != '\x02')) &&
              ((local_40 = local_40 + *(ushort *)(_DAT_d0f52830 + 10), DAT_20004628 != '\x03' &&
               (local_3c = local_3c + *(ushort *)(_DAT_d0f52830 + 0xe), DAT_20004628 != '\x04'))))
             && ((local_38 = local_38 + *(ushort *)(_DAT_d0f52830 + 0x12), DAT_20004628 != '\x05' &&
                 ((local_34 = local_34 + *(ushort *)(_DAT_d0f52830 + 0x16), DAT_20004628 != '\x06'
                  && (local_30 = local_30 + *(ushort *)(_DAT_d0f52830 + 0x1a), DAT_20004628 != '\a')
                  ))))) &&
            (local_2c = local_2c + *(ushort *)(_DAT_d0f52830 + 0x1e), DAT_20004628 != '\b')) &&
           (local_28 = local_28 + *(ushort *)(_DAT_d0f52830 + 0x22), DAT_20004628 != '\t')) {
          local_24 = local_24 + *(ushort *)(_DAT_d0f52830 + 0x26);
        }
        cVar2 = cVar2 + -1;
      } while (cVar2 != '\0');
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
      iVar1 = 0;
    }
  }
  return iVar1;
}
```

### `FUN_0000408c` @ `0000408c`

- constants: `0x7f` `0x20` `0x08` `0x21` `0x24` `0x26`

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
}
```

### `FUN_00032b10` @ `00032b10`

- constants: `0x20` `0x24` `0x08` `0x26` `0x21` `0x22`

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
        *(byte *)((int)param_3 + 0x49) = *(byte *)((int)param_3 + 0x49) & 0xe0 | bVar2 & 0x1f;
        uVar4 = FUN_00036ab8(param_1,param_2,0x31);
        uVar4 = FUN_00036b58(param_1,param_2,uVar4);
        uVar4 = FUN_00032a74(param_1,param_2,param_3[4],uVar4);
        *(char *)((int)param_3 + 0x3e) = (char)uVar4;
        *(char *)((int)param_3 + 0x3f) = (char)((uint)uVar4 >> 8);
        *(char *)(param_3 + 0x10) = (char)((uint)uVar4 >> 0x10);
      }
    }
  }
/* ... truncated ... */
```

### `FUN_000015fc` @ `000015fc`

- constants: `0x08` `0x22` `0x20` `0x26` `0x21`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_000015fc(undefined2 *param_1)

{
  short sVar1;
  undefined4 uVar2;
  
  if (param_1 == (undefined2 *)0x0) {
    uVar2 = 1;
  }
  else if (DAT_200041ac == '\0') {
    uVar2 = 0x21;
  }
  else {
    DAT_20004218 = *(undefined1 *)(param_1 + 2);
    _DAT_20004258 = *param_1;
    sVar1 = param_1[1];
    _DAT_2000413c = CONCAT22(param_1[4],param_1[4]);
    _DAT_2000422e = param_1[5];
    _DAT_20004250 = param_1[6];
    _DAT_2000420a = param_1[3];
    if (sVar1 != -1) {
      _DAT_20004256 = sVar1;
      _DAT_2000425c = sVar1;
      _DAT_20004262 = sVar1;
      _DAT_20004268 = sVar1;
      _DAT_2000426e = sVar1;
      _DAT_20004274 = sVar1;
      _DAT_2000427a = sVar1;
      _DAT_20004280 = sVar1;
      _DAT_20004286 = sVar1;
      _DAT_2000428c = sVar1;
    }
    uVar2 = 0;
    _DAT_20004212 = _DAT_2000420a;
    _DAT_2000425e = _DAT_20004258;
    _DAT_20004264 = _DAT_20004258;
    _DAT_2000426a = _DAT_20004258;
    _DAT_20004270 = _DAT_20004258;
    _DAT_20004276 = _DAT_20004258;
    _DAT_2000427c = _DAT_20004258;
    _DAT_20004282 = _DAT_20004258;
    _DAT_20004288 = _DAT_20004258;
    _DAT_2000428e = _DAT_20004258;
  }
  return uVar2;
}
```

### `FUN_000041fc` @ `000041fc`

- constants: `0x21` `0x20` `0x08` `0x24` `0x26`

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
    param_5[0x30] = (byte)(uVar2 >> 0xe);
    uVar2 = param_2[9];
    param_5[0x31] = (byte)uVar2 & 0x7f;
    param_5[0x32] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x33] = (byte)(uVar2 >> 0xe);
    param_5[0x34] = *param_3;
    bVar1 = param_3[1];
    param_5[0x35] = bVar1 & 0x7f;
    param_5[0x36] = bVar1 >> 7;
    param_5[0x37] = param_3[2];
/* ... truncated ... */
```

### `FUN_00004914` @ `00004914`

- constants: `0x08` `0x22` `0x20` `0x26` `0x24`

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
/* ... truncated ... */
```

### `FUN_00005f2c` @ `00005f2c`

- constants: `0x08` `0x21` `0x24` `0x20` `0x22`

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

### `FUN_0000657c` @ `0000657c`

- constants: `0x08` `0x20` `0x22` `0x24` `0xf7`

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

### `FUN_0003d8a0` @ `0003d8a0`

- constants: `0x21` `0x08` `0x24` `0x26` `0x20`

```c

void FUN_0003d8a0(int param_1)

{
  undefined4 uVar1;
  
  FUN_00050350(param_1,0,0x70);
  uVar1 = FUN_00045d1c();
  *(char *)(param_1 + 0x21) = (char)uVar1;
  *(char *)(param_1 + 0x22) = (char)((uint)uVar1 >> 8);
  *(char *)(param_1 + 0x23) = (char)((uint)uVar1 >> 0x10);
  uVar1 = FUN_00045d1c();
  *(char *)(param_1 + 0x24) = (char)uVar1;
  *(char *)(param_1 + 0x25) = (char)((uint)uVar1 >> 8);
  *(char *)(param_1 + 0x26) = (char)((uint)uVar1 >> 0x10);
  uVar1 = FUN_00045d30();
  *(char *)(param_1 + 0x29) = (char)uVar1;
  *(char *)(param_1 + 0x2a) = (char)((uint)uVar1 >> 8);
  *(char *)(param_1 + 0x2b) = (char)((uint)uVar1 >> 0x10);
  *(undefined1 *)(param_1 + 0x2d) = 0xff;
  *(undefined1 *)(param_1 + 0x2e) = 2;
  uVar1 = FUN_00045d30();
  *(char *)(param_1 + 0x3e) = (char)uVar1;
  *(char *)(param_1 + 0x3f) = (char)((uint)uVar1 >> 8);
  *(char *)(param_1 + 0x40) = (char)((uint)uVar1 >> 0x10);
  uVar1 = FUN_00045d30();
  *(char *)(param_1 + 0x59) = (char)uVar1;
  *(char *)(param_1 + 0x5a) = (char)((uint)uVar1 >> 8);
  *(char *)(param_1 + 0x5b) = (char)((uint)uVar1 >> 0x10);
  *(undefined4 *)(param_1 + 0x34) = 0;
  *(undefined1 *)(param_1 + 0x20) = 0xff;
  *(undefined1 *)(param_1 + 0x3b) = 0xff;
  *(undefined1 *)(param_1 + 0x58) = 0xff;
  *(undefined1 *)(param_1 + 0x6c) = 0xff;
  *(ushort *)(param_1 + 0x48) = *(ushort *)(param_1 + 0x48) & 0xe000 | (ushort)DAT_0003d954;
  return;
}
```

### `FUN_0003eab0` @ `0003eab0`

- constants: `0x24` `0x08` `0x20` `0x21` `0x22`

```c

void FUN_0003eab0(int param_1,int param_2,uint *param_3)

{
  uint uVar1;
  int iVar2;
  int iVar3;
  uint uVar4;
  undefined4 uVar5;
  undefined4 uVar6;
  uint uVar7;
  uint uVar8;
  uint uVar9;
  uint uVar10;
  uint uVar11;
  int iVar12;
  uint uVar13;
  int local_110;
  undefined1 *local_e8;
  uint *local_e4;
  uint local_dc;
  uint local_d8;
  uint local_d4;
  uint local_d0;
  uint local_cc;
  uint local_c8;
  int local_c4;
  int local_c0;
  uint local_bc;
  uint local_b8;
  uint local_b4;
  uint local_b0;
  uint local_ac;
  uint local_a8;
  uint local_a4;
  uint local_a0;
  undefined1 auStack_9c [36];
  uint local_78;
  uint local_74;
  uint local_70;
  uint local_6c;
  uint *local_54 [5];
  undefined4 local_40;
  undefined4 local_3c;
  undefined1 local_38;
  uint *local_34;
  
  if (*(byte *)(param_2 + 0x28) < 3) {
    return;
  }
  if (*(int *)(param_2 + 0x24) == 0) {
    return;
  }
  if ((*(byte *)(param_2 + 0x29) & 0x1f) == 0) {
    return;
  }
  iVar2 = FUN_000458e4(param_3);
  iVar3 = FUN_000458f0(param_3);
  if (iVar3 < iVar2) {
    iVar12 = *(int *)(param_2 + 0x1c);
    iVar3 = iVar3 >> 1;
    if (iVar12 < iVar3) {
LAB_0003ee18:
      iVar3 = iVar12;
    }
  }
  else {
    iVar12 = *(int *)(param_2 + 0x1c);
    iVar3 = iVar2 >> 1;
    if (iVar12 < iVar3) goto LAB_0003ee18;
  }
  iVar2 = *(int *)(param_2 + 0x24);
  uVar9 = (uint)*(byte *)(param_2 + 0x29);
  if ((int)(uVar9 << 0x1d) < 0) {
    local_dc = iVar2 + *param_3;
    if ((int)(uVar9 << 0x1c) < 0) goto LAB_0003eb2c;
LAB_0003edf0:
    iVar12 = iVar3 + iVar2;
  }
  else {
    local_dc = *param_3 - (iVar3 + iVar2);
    if (-1 < (int)(uVar9 << 0x1c)) goto LAB_0003edf0;
LAB_0003eb2c:
    iVar12 = -iVar2;
  }
  local_d4 = param_3[2] + iVar12;
  iVar12 = iVar2;
  if (-1 < (int)(uVar9 << 0x1e)) {
    iVar12 = -(iVar3 + iVar2);
  }
/* ... truncated ... */
```

### `FUN_00040156` @ `00040156`

- constants: `0x24` `0x08` `0x20` `0x21` `0x22`

```c

void FUN_00040156(void)

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
  FUN_0003f79c();
  iVar20 = unaff_r5 >> 7;
  if (*(byte *)(extraout_r1 + 0x20) < 3) goto LAB_000401bc;
  local_b0 = extraout_r2[1];
  local_ac = extraout_r2[2];
  local_a8 = extraout_r2[3];
  local_b4 = *extraout_r2;
  iVar5 = FUN_000450d4(&local_a4,&local_b4,iVar20 + 0x38);
  if (iVar5 == 0) goto LAB_000401bc;
  bVar2 = *(byte *)(extraout_r1 + 0x2f);
  bVar11 = bVar2 & 0xf;
  bVar3 = *(byte *)(extraout_r1 + 0x20);
/* ... truncated ... */
```

### `FUN_0004e190` @ `0004e190`

- constants: `0x20` `0x24` `0x08` `0x21` `0x22`

```c

/* WARNING: Type propagation algorithm not settling */

void FUN_0004e190(undefined4 *param_1)

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
                uVar1 = FUN_00045cdc(*puVar8,*puVar6,uVar5);
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
            FUN_00050328(puVar6,puVar8,iVar16 << 1);
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
              uVar1 = FUN_00045cdc(*puVar8,*puVar6,uVar5 * *pbVar10 >> 8);
              puVar8 = puVar8 + 1;
              *puVar6 = uVar1;
              pbVar10 = pbVar10 + 1;
              puVar6 = puVar6 + 1;
/* ... truncated ... */
```


