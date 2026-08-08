# Motion 32 MIDI Packet Shape Probe

## `FUN_0002164c` @ `0002164c` score `100`

- reasons: `byte deref` `u8 deref` `offset +1` `offset +2` `offset +3` `small indexes` `channel nibble mask` `7-bit mask` `0x8f-ish` `127` `midi send call` `sysex end`

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

## `FUN_00047bb4` @ `00047bb4` score `74`

- reasons: `byte deref` `offset +2` `offset +3` `small indexes` `status nibble mask` `channel nibble mask` `0x80` `0xf0`

```c

uint FUN_00047bb4(int param_1,int *param_2)

{
  byte bVar1;
  int iVar2;
  uint uVar3;
  int iVar4;
  uint uVar5;
  uint uVar6;
  int local_1c [2];
  
  local_1c[0] = 0;
  if (param_2 == (int *)0x0) {
    param_2 = local_1c;
  }
  if (param_1 != 0) {
    iVar2 = *param_2;
    uVar3 = (uint)*(byte *)(param_1 + iVar2);
    if (uVar3 != 0) {
      iVar4 = iVar2 + 1;
      if (-1 < (char)*(byte *)(param_1 + iVar2)) {
        *param_2 = iVar4;
        return uVar3;
      }
      if ((uVar3 & 0xffffffe0) == 0xc0) {
        *param_2 = iVar4;
        bVar1 = *(byte *)(param_1 + iVar4);
        if ((bVar1 & 0xffffffc0) == 0x80) {
          *param_2 = iVar2 + 2;
          return (bVar1 & 0x3f) + (uVar3 & 0x1f) * 0x40;
        }
      }
      else if ((uVar3 & 0xfffffff0) == 0xe0) {
        *param_2 = iVar4;
        bVar1 = *(byte *)(param_1 + iVar4);
        if ((bVar1 & 0xffffffc0) == 0x80) {
          *param_2 = iVar2 + 2;
          uVar5 = (uint)*(byte *)(param_1 + iVar2 + 2);
          if ((uVar5 & 0xffffffc0) == 0x80) {
            *param_2 = iVar2 + 3;
            return (bVar1 & 0x3f) * 0x40 + (uVar3 & 0xf) * 0x1000 + (uVar5 & 0x3f);
          }
        }
      }
      else if ((uVar3 & 0xfffffff8) == 0xf0) {
        *param_2 = iVar4;
        bVar1 = *(byte *)(param_1 + iVar4);
        if ((bVar1 & 0xffffffc0) == 0x80) {
          *param_2 = iVar2 + 2;
          uVar5 = (uint)*(byte *)(param_1 + iVar2 + 2);
          if ((uVar5 & 0xffffffc0) == 0x80) {
            *param_2 = iVar2 + 3;
            uVar6 = (uint)*(byte *)(param_1 + iVar2 + 3);
            if ((uVar6 & 0xffffffc0) == 0x80) {
              *param_2 = iVar2 + 4;
              return (uVar5 & 0x3f) * 0x40 + (uVar6 & 0x3f) +
                     ((bVar1 & 0x3f) << 0xc | (uVar3 & 7) << 0x12);
            }
          }
        }
      }
      else {
        *param_2 = iVar4;
      }
    }
  }
  return 0;
}
```

## `FUN_00005854` @ `00005854` score `73`

- reasons: `byte* param` `u8* param` `byte deref` `offset +1` `offset +2` `offset +3` `small indexes` `status nibble mask` `channel nibble mask`

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

## `FUN_00004ce8` @ `00004ce8` score `56`

- reasons: `byte deref` `u8 deref` `offset +1` `offset +2` `offset +3` `small indexes` `channel nibble mask` `127` `sysex end`

```c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_00004ce8(uint *param_1,uint *param_2,undefined2 *param_3)

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
    iVar7 = FUN_00004e3a();
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
    goto LAB_000052d8;
  }
  if ((~bVar12 & 3) != 0) {
    iVar7 = FUN_00004e3a();
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
        FUN_00005602();
        iVar7 = extraout_r1;
        iVar13 = extraout_r2;
        uVar16 = extraout_r3;
      }
      iVar13 = uVar16 - *(ushort *)((int)auStack_60 + iVar13);
      if (0xfffc < iVar13 + 0x7ffeU) {
        FUN_0000574a();
        iVar7 = extraout_r1_00;
        iVar13 = extraout_r3_00;
      }
      sVar4 = (short)iVar13;
      iVar13 = uVar24 * 2;
      psVar23 = (short *)(param_1[6] + iVar13);
      sVar6 = *(short *)(param_1[6] + iVar13);
      if (sVar6 != 0) break;
      *psVar23 = sVar4;
FUN_00004d5c:
      uVar24 = uVar24 + 1;
      iVar7 = iVar7 + 6;
      if (local_a8 <= (uint *)(uVar24 & 0xff)) goto LAB_00004e34;
    }
    iVar9 = (int)(short)(sVar6 - *(short *)(param_1[4] + iVar13));
    iVar25 = (uint)*(ushort *)(param_1[5] + iVar13) + iVar9;
    if (iVar25 + 0x7fffU < 0xffff) {
      if (sVar4 < iVar9) {
        FUN_00005636();
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
          uVar28 = FUN_00004dde();
          uVar16 = extraout_r2_03;
          uVar17 = extraout_r3_03;
          puVar26 = extraout_r12_01;
          goto LAB_0000575e;
        }
        if ((int)(uVar24 - 0x20) < 0) {
          uVar16 = 1 >> (0x20 - uVar24 & 0xff);
        }
        else {
          uVar16 = 1 << (uVar24 - 0x20 & 0xff);
        }
        param_1[3] = param_1[3] & ~uVar16;
        param_1[2] = param_1[2] & ~(1 << (uVar24 & 0xff));
        uVar28 = FUN_00004dde();
        uVar16 = extraout_r2_01;
        uVar17 = extraout_r3_01;
        puVar26 = extraout_r12;
LAB_00005582:
        puVar22 = (ushort *)((int)&SVCall + 1);
        *(undefined2 *)(puVar26[7] + (int)param_1) = 0;
        puVar19 = (uint *)(puVar26[8] + (int)param_1);
        psVar23 = (short *)(uint)*(ushort *)(puVar26[8] + (int)param_1);
        if (psVar23 < (short *)(uint)*(byte *)((int)puVar26 + 0x2d)) {
LAB_0000575e:
          *(short *)puVar19 = (short)psVar23 + 1;
        }
        else {
          if ((int)(uVar17 - 0x20) < 0) {
            uVar18 = 1 >> (0x20 - uVar17 & 0xff);
          }
          else {
            uVar18 = 1 << (uVar17 - 0x20 & 0xff);
          }
          puVar22 = (ushort *)(puVar26[2] & ~(1 << (uVar17 & 0xff)));
          puVar19 = (uint *)(puVar26[3] & ~uVar18);
          puVar26[2] = (uint)puVar22;
          puVar26[3] = (uint)puVar19;
        }
LAB_0000531e:
        if (*(short *)((int)puVar26 + 0x2e) == 0) goto LAB_000052ca;
/* ... truncated ... */
```

## `FUN_00004d5c` @ `00004d5c` score `56`

- reasons: `byte deref` `u8 deref` `offset +1` `offset +2` `offset +3` `small indexes` `channel nibble mask` `127` `sysex end`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4
FUN_00004d5c(undefined4 param_1,int param_2,undefined4 param_3,undefined4 param_4,uint param_5,
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
code_r0x00004d5c:
  unaff_r7 = unaff_r7 + 1;
  if ((unaff_r7 & 0xff) < param_5) {
    while( true ) {
      param_2 = param_2 + 6;
      iVar12 = (uint)*(byte *)(unaff_r5 + param_2) * 4;
      uVar15 = (uint)*(ushort *)(&stack0x0000004a + iVar12);
      if ((int)unaff_r8 < (int)uVar15) {
        FUN_00005602();
        param_2 = extraout_r1;
        iVar12 = extraout_r2;
        uVar15 = extraout_r3;
      }
      iVar12 = uVar15 - *(ushort *)(&stack0x00000048 + iVar12);
      if (unaff_r11 < iVar12 + 0x7ffeU) {
        FUN_0000574a();
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
          FUN_00005636();
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
            uVar28 = FUN_00004dde();
            iVar12 = extraout_r2_01;
            uVar15 = extraout_r3_01;
            iVar6 = extraout_r12;
            goto LAB_00005582;
          }
          *(ushort *)puVar20 = uVar9 + 1;
          uVar28 = FUN_00004dde();
          iVar12 = extraout_r2_03;
          uVar15 = extraout_r3_03;
          iVar6 = extraout_r12_01;
          goto LAB_0000575e;
        }
      }
      if (*(short *)(param_6 + 0x2e) == 0) goto code_r0x00004d5c;
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
        uVar27 = FUN_00005606();
      }
      param_2 = (int)((ulonglong)uVar27 >> 0x20);
      *(undefined4 *)uVar27 = 0;
      unaff_r7 = unaff_r7 + 1;
      *(undefined2 *)(iVar12 + iVar6) = 0;
      if (param_5 <= (unaff_r7 & 0xff)) goto LAB_00004e34;
    }
    *psVar17 = sVar5;
    goto code_r0x00004d5c;
  }
LAB_00004e34:
  uVar16 = *(undefined4 *)(param_6 + 0xc);
  *param_10 = *(undefined4 *)(param_6 + 8);
  param_10[1] = uVar16;
  if (*(char *)(param_9 + 0x11) != '\0') {
    param_6 = 0;
    param_5 = 0;
    do {
      piVar26 = (int *)(*(int *)(param_9 + 4) + param_6 * 8);
      uVar15 = param_5 * 5 & 0xff;
      if ((char)piVar26[1] != '\0') {
        uVar18 = 0;
        psVar17 = (short *)&stack0x00000034;
        uVar22 = uVar15;
        do {
          iVar12 = *piVar26;
          sVar3 = *(short *)(&stack0x00000048 + (uint)*(byte *)(iVar12 + uVar18) * 2);
          *(short *)(uVar22 * 2 + 0x200064a8) = sVar3;
          sVar5 = FUN_00002aa8(*(undefined1 *)(iVar12 + uVar18));
          sVar3 = sVar3 - sVar5;
          *(short *)(&DAT_20006494 + uVar22 * 2) = sVar3;
          *psVar17 = sVar3;
          uVar18 = uVar18 + 1;
          uVar22 = uVar22 + 1;
          psVar17 = psVar17 + 1;
        } while ((uVar18 & 0xff) < (uint)*(byte *)(piVar26 + 1));
      }
      iVar12 = FUN_00003544(param_5,&stack0x00000034);
      uVar22 = (uint)*(byte *)(piVar26 + 1);
      if (((uVar22 == 0) || (*(ushort *)(uVar15 * 2 + 0x20006480) = uStack00000034, uVar22 == 1)) ||
/* ... truncated ... */
```

## `FUN_00004dde` @ `00004dde` score `56`

- reasons: `byte deref` `u8 deref` `offset +1` `offset +2` `offset +3` `small indexes` `channel nibble mask` `127` `sysex end`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4
FUN_00004dde(undefined4 param_1,int param_2,int param_3,undefined4 param_4,uint param_5,uint param_6
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
          uVar27 = FUN_00005606();
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
          if (*(char *)(param_9 + 0x11) == '\0') goto LAB_000050de;
          param_6 = 0;
          param_5 = 0;
          goto LAB_00004e62;
        }
        param_2 = param_2 + 6;
        iVar19 = (uint)*(byte *)(unaff_r5 + param_2) * 4;
        uVar15 = (uint)*(ushort *)(&stack0x0000004a + iVar19);
        if ((int)unaff_r8 < (int)uVar15) {
          FUN_00005602();
          param_2 = extraout_r1;
          iVar19 = extraout_r2;
          uVar15 = extraout_r3;
        }
        iVar19 = uVar15 - *(ushort *)(&stack0x00000048 + iVar19);
        if (unaff_r11 < iVar19 + 0x7ffeU) {
          FUN_0000574a();
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
      FUN_00005636();
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
      uVar12 = 1 << (uVar12 - 0x1f & 0xff);
    }
    *(uint *)(param_6 + 0xc) = *(uint *)(param_6 + 0xc) & ~uVar12;
    *(uint *)(param_6 + 8) = *(uint *)(param_6 + 8) & ~(1 << (unaff_r7 & 0xff));
    uVar28 = FUN_00004dde();
    iVar19 = extraout_r2_01;
    uVar12 = extraout_r3_01;
    iVar8 = extraout_r12;
    goto LAB_00005582;
  }
  *(ushort *)puVar22 = uVar10 + 1;
  uVar28 = FUN_00004dde();
  iVar19 = extraout_r2_03;
  uVar12 = extraout_r3_03;
  iVar8 = extraout_r12_01;
LAB_0000575e:
  *(short *)puVar22 = (short)psVar18 + 1;
LAB_0000531e:
  uVar15 = uVar12;
  if (*(short *)(iVar8 + 0x2e) == 0) goto LAB_000052ca;
  puVar22 = (uint *)(*(int *)(iVar8 + 0x24) + uVar15 * 4);
  unaff_r8 = (ushort *)(*(int *)(iVar8 + 0x28) + uVar21);
  if ((int)(uVar15 - 0x20) < 0) {
    uVar21 = *(uint *)(iVar8 + 8) >> (uVar15 & 0xff) |
             *(int *)(iVar8 + 0xc) << (0x20 - uVar15 & 0xff);
  }
  else {
    uVar21 = *(uint *)(iVar8 + 0xc) >> (uVar15 - 0x20 & 0xff);
  }
  if ((uVar21 & 1) == 0) {
    uVar12 = (int)(uVar28 >> 0x20) + *puVar22;
    *puVar22 = uVar12;
    uVar10 = *unaff_r8;
    *unaff_r8 = uVar10 + 1;
    if ((uint)(ushort)(uVar10 + 1) < (uint)*(ushort *)(iVar8 + 0x2e)) goto LAB_000052ca;
    *(undefined2 *)uVar28 = (short)(uVar12 / *(ushort *)(iVar8 + 0x2e));
    *puVar22 = uVar21 & 1;
    *unaff_r8 = (ushort)(uVar21 & 1);
    goto LAB_000052ca;
  }
/* ... truncated ... */
```

## `FUN_0004de98` @ `0004de98` score `54`

- reasons: `byte deref` `offset +1` `offset +2` `small indexes` `status nibble mask` `channel nibble mask`

```c

void FUN_0004de98(undefined4 *param_1)

{
  ushort uVar1;
  ushort uVar2;
  int iVar3;
  byte *pbVar4;
  uint uVar5;
  int iVar6;
  int iVar7;
  byte *pbVar8;
  ushort *puVar9;
  int iVar10;
  int iVar11;
  uint uVar12;
  ushort *puVar13;
  ushort *puVar14;
  uint uVar15;
  ushort *puVar16;
  int iVar17;
  undefined4 uVar18;
  bool bVar19;
  int local_40;
  
  iVar6 = param_1[1];
  iVar7 = param_1[2];
  iVar3 = FUN_00045c18(param_1[6]);
  pbVar8 = (byte *)param_1[4];
  uVar15 = (uint)*(byte *)((int)param_1 + 0x1b);
  puVar9 = (ushort *)*param_1;
  iVar10 = param_1[3];
  uVar2 = (ushort)iVar3;
  if (pbVar8 == (byte *)0x0) {
    if (uVar15 < 0xfd) {
      if (0 < iVar7) {
        iVar11 = *puVar9 + 1;
        puVar16 = puVar9 + iVar6;
        uVar18 = 0;
        local_40 = 0;
        do {
          bVar19 = ((uint)puVar9 & 3) != 0;
          if (bVar19) {
            uVar2 = FUN_00045cdc(iVar3,*puVar9,uVar15);
            *puVar9 = uVar2;
          }
          uVar12 = (uint)bVar19;
          if ((int)uVar12 < iVar6 + -2) {
            uVar5 = (iVar6 + -3) - uVar12 & 0xfffffffe;
            puVar14 = puVar9 + uVar12;
            do {
              while( true ) {
                if (puVar14[1] == *puVar14) break;
                uVar2 = FUN_00045cdc(iVar3,*puVar14,uVar15);
                *puVar14 = uVar2;
                uVar2 = FUN_00045cdc(iVar3,puVar14[1],uVar15);
                puVar14[1] = uVar2;
LAB_0004e078:
                puVar14 = puVar14 + 2;
                if (puVar14 == puVar9 + uVar12 + uVar5 + 2) goto LAB_0004e096;
              }
              if (*(int *)puVar14 != iVar11) {
                iVar11 = *(int *)puVar14;
                uVar2 = FUN_00045cdc(iVar3,puVar14[1],uVar15);
                *puVar14 = uVar2;
                puVar14[1] = uVar2;
                uVar18 = *(undefined4 *)puVar14;
                goto LAB_0004e078;
              }
              *(undefined4 *)puVar14 = uVar18;
              puVar14 = puVar14 + 2;
            } while (puVar14 != puVar9 + uVar12 + uVar5 + 2);
LAB_0004e096:
            uVar12 = uVar12 + 2 + uVar5;
          }
          if ((int)uVar12 < iVar6) {
            puVar14 = puVar9 + uVar12;
            do {
              uVar2 = FUN_00045cdc(iVar3,*puVar14,uVar15);
              *puVar14 = uVar2;
              puVar14 = puVar14 + 1;
            } while (puVar14 != puVar16);
          }
          puVar9 = (ushort *)((int)puVar9 + iVar10);
          puVar16 = (ushort *)((int)puVar16 + iVar10);
          local_40 = local_40 + 1;
        } while (iVar7 != local_40);
      }
    }
    else if (0 < iVar7) {
      iVar3 = iVar3 * 0x10001;
      iVar11 = 0;
      do {
        puVar16 = puVar9 + (iVar6 - 1U & 0xfffffff0);
        puVar14 = puVar9 + iVar6;
        if (((uint)puVar9 & 3) != 0) {
          *puVar9 = uVar2;
          puVar9 = puVar9 + 1;
        }
        puVar13 = puVar9;
        if (puVar9 < puVar16) {
          do {
            *(int *)puVar13 = iVar3;
            *(int *)(puVar13 + 2) = iVar3;
            *(int *)(puVar13 + 4) = iVar3;
            *(int *)(puVar13 + 6) = iVar3;
            *(int *)(puVar13 + 8) = iVar3;
            *(int *)(puVar13 + 10) = iVar3;
            *(int *)(puVar13 + 0xc) = iVar3;
            *(int *)(puVar13 + 0xe) = iVar3;
            puVar13 = puVar13 + 0x10;
          } while (puVar13 < puVar16);
          puVar9 = (ushort *)
                   ((int)puVar9 + ((int)puVar16 + (-1 - (int)puVar9) & 0xffffffe0U) + 0x20);
        }
        puVar16 = puVar9;
        if (puVar9 < puVar14) {
          do {
            *puVar16 = uVar2;
            puVar16 = puVar16 + 1;
          } while (puVar16 < puVar14);
          puVar9 = (ushort *)((int)puVar9 + ((int)puVar14 + (-1 - (int)puVar9) & 0xfffffffeU) + 2);
        }
        iVar11 = iVar11 + 1;
        puVar9 = (ushort *)((int)puVar9 + iVar10 + iVar6 * -2);
      } while (iVar7 != iVar11);
    }
  }
  else {
    iVar11 = param_1[5];
    if (uVar15 < 0xfd) {
      if ((0 < iVar7) && (0 < iVar6)) {
        puVar14 = puVar9 + iVar6;
        iVar6 = 0;
        puVar16 = puVar9;
        pbVar4 = pbVar8;
        do {
          do {
            uVar2 = FUN_00045cdc(iVar3,*puVar9,uVar15 * *pbVar8 >> 8);
            *puVar9 = uVar2;
            puVar9 = puVar9 + 1;
            pbVar8 = pbVar8 + 1;
          } while (puVar14 != puVar9);
          pbVar8 = pbVar4 + iVar11;
          puVar9 = (ushort *)((int)puVar16 + iVar10);
          puVar14 = (ushort *)((int)puVar14 + iVar10);
          iVar6 = iVar6 + 1;
          puVar16 = puVar9;
          pbVar4 = pbVar8;
        } while (iVar7 != iVar6);
      }
    }
    else if (0 < iVar7) {
      iVar17 = 0;
      do {
        bVar19 = ((uint)pbVar8 & 1) != 0;
        if (bVar19) {
          uVar1 = FUN_00045cdc(iVar3,*puVar9,*pbVar8);
          *puVar9 = uVar1;
        }
        uVar15 = DAT_0004e18c;
        uVar12 = (uint)bVar19;
        if ((int)uVar12 < iVar6 + -1) {
          puVar14 = (ushort *)(pbVar8 + uVar12);
          uVar5 = (iVar6 + -2) - uVar12 & 0xfffffffe;
          puVar16 = puVar9 + uVar12;
          do {
            while (*puVar14 == uVar15) {
              *puVar16 = uVar2;
              puVar16[1] = uVar2;
              puVar16 = puVar16 + 2;
              puVar14 = puVar14 + 1;
              if (puVar16 == puVar9 + uVar12 + uVar5 + 2) goto LAB_0004df46;
            }
            if (*puVar14 != 0) {
              uVar1 = FUN_00045cdc(iVar3,*puVar16,(byte)*puVar14);
              *puVar16 = uVar1;
              uVar1 = FUN_00045cdc(iVar3,puVar16[1],*(byte *)((int)puVar14 + 1));
              puVar16[1] = uVar1;
            }
/* ... truncated ... */
```

## `FUN_0004e94c` @ `0004e94c` score `54`

- reasons: `byte deref` `offset +1` `offset +2` `small indexes` `status nibble mask` `channel nibble mask`

```c

void FUN_0004e94c(undefined4 *param_1)

{
  ushort uVar1;
  uint uVar2;
  uint uVar3;
  uint uVar4;
  ushort uVar5;
  int iVar6;
  int iVar7;
  uint uVar8;
  uint uVar9;
  ushort *puVar10;
  int iVar11;
  uint uVar12;
  ushort *puVar13;
  byte *pbVar14;
  int iVar15;
  ushort *puVar16;
  ushort *puVar17;
  int iVar18;
  bool bVar19;
  byte *local_58;
  int local_48;
  
  iVar6 = param_1[1];
  iVar7 = param_1[2];
  uVar2 = FUN_00045c18(param_1[6]);
  uVar8 = (uVar2 & 0xff) << 8 | uVar2 >> 8 & 0xff;
  uVar9 = (uint)*(byte *)((int)param_1 + 0x1b);
  local_58 = (byte *)param_1[4];
  puVar10 = (ushort *)*param_1;
  iVar11 = param_1[3];
  uVar5 = (ushort)uVar8;
  if (local_58 == (byte *)0x0) {
    if (uVar9 < 0xfd) {
      if ((0 < iVar7) && (0 < iVar6)) {
        iVar18 = 0;
        puVar17 = puVar10 + iVar6;
        do {
          uVar8 = 0;
          uVar5 = *puVar10 - 1;
          puVar16 = puVar10;
          do {
            uVar1 = *puVar16;
            if (uVar1 != uVar5) {
              uVar8 = FUN_00045cdc(uVar2,uVar1 << 8 | uVar1 >> 8,uVar9);
              uVar5 = *puVar16;
              uVar8 = (uVar8 & 0xff) << 8 | uVar8 >> 8 & 0xff;
            }
            *puVar16 = (ushort)uVar8;
            puVar16 = puVar16 + 1;
          } while (puVar16 != puVar17);
          iVar18 = iVar18 + 1;
          puVar10 = (ushort *)((int)puVar10 + iVar11);
          puVar17 = (ushort *)((int)puVar17 + iVar11);
        } while (iVar18 != iVar7);
      }
    }
    else if (0 < iVar7) {
      iVar18 = uVar8 * 0x10001;
      iVar15 = 0;
      do {
        puVar16 = puVar10 + iVar6;
        puVar17 = puVar10 + (iVar6 - 1U & 0xfffffff0);
        if (((uint)puVar10 & 3) != 0) {
          *puVar10 = uVar5;
          puVar10 = puVar10 + 1;
        }
        puVar13 = puVar10;
        if (puVar10 < puVar17) {
          do {
            *(int *)puVar13 = iVar18;
            *(int *)(puVar13 + 2) = iVar18;
            *(int *)(puVar13 + 4) = iVar18;
            *(int *)(puVar13 + 6) = iVar18;
            *(int *)(puVar13 + 8) = iVar18;
            *(int *)(puVar13 + 10) = iVar18;
            *(int *)(puVar13 + 0xc) = iVar18;
            *(int *)(puVar13 + 0xe) = iVar18;
            puVar13 = puVar13 + 0x10;
          } while (puVar13 < puVar17);
          puVar10 = (ushort *)
                    ((int)puVar10 + ((int)puVar17 + (-1 - (int)puVar10) & 0xffffffe0U) + 0x20);
        }
        puVar17 = puVar10;
        if (puVar10 < puVar16) {
          do {
            *puVar17 = uVar5;
            puVar17 = puVar17 + 1;
          } while (puVar17 < puVar16);
          puVar10 = (ushort *)
                    ((int)puVar10 + ((int)puVar16 + (-1 - (int)puVar10) & 0xfffffffeU) + 2);
        }
        iVar15 = iVar15 + 1;
        puVar10 = (ushort *)((int)puVar10 + iVar11 + iVar6 * -2);
      } while (iVar7 != iVar15);
    }
  }
  else {
    iVar18 = param_1[5];
    if (uVar9 < 0xfd) {
      if ((0 < iVar7) && (0 < iVar6)) {
        iVar15 = 0;
        puVar16 = puVar10 + iVar6;
        pbVar14 = local_58;
        puVar17 = puVar10;
        do {
          do {
            uVar8 = FUN_00045cdc(uVar2,*puVar10 << 8 | *puVar10 >> 8,uVar9 * *local_58 >> 8);
            *puVar10 = (ushort)((uVar8 & 0xff) << 8) | (ushort)(uVar8 >> 8) & 0xff;
            puVar10 = puVar10 + 1;
            local_58 = local_58 + 1;
          } while (puVar10 != puVar16);
          local_58 = pbVar14 + iVar18;
          puVar10 = (ushort *)((int)puVar17 + iVar11);
          puVar16 = (ushort *)((int)puVar16 + iVar11);
          iVar15 = iVar15 + 1;
          pbVar14 = local_58;
          puVar17 = puVar10;
        } while (iVar7 != iVar15);
      }
    }
    else if (0 < iVar7) {
      local_48 = 0;
      do {
        bVar19 = ((uint)local_58 & 1) != 0;
        if (bVar19) {
          uVar8 = FUN_00045cdc(uVar2,*puVar10 << 8 | *puVar10 >> 8,*local_58);
          *puVar10 = (ushort)((uVar8 & 0xff) << 8) | (ushort)(uVar8 >> 8) & 0xff;
        }
        uVar8 = DAT_0004ebe0;
        uVar9 = (uint)bVar19;
        if ((int)uVar9 < iVar6 + -1) {
          puVar16 = (ushort *)(local_58 + uVar9);
          puVar17 = puVar10 + uVar9;
          uVar12 = (iVar6 + -2) - uVar9 & 0xfffffffe;
          do {
            while (*puVar16 != uVar8) {
              if (*puVar16 != 0) {
                uVar1 = puVar17[1];
                uVar3 = FUN_00045cdc(uVar2,*puVar17 << 8 | *puVar17 >> 8,(byte)*puVar16);
                uVar4 = FUN_00045cdc(uVar2,uVar1 << 8 | uVar1 >> 8,*(byte *)((int)puVar16 + 1));
                *puVar17 = (ushort)((uVar3 & 0xff) << 8) | (ushort)(uVar3 >> 8) & 0xff;
                puVar17[1] = (ushort)((uVar4 & 0xff) << 8) | (ushort)(uVar4 >> 8) & 0xff;
              }
              puVar17 = puVar17 + 2;
              puVar16 = puVar16 + 1;
              if (puVar10 + uVar12 + uVar9 + 2 == puVar17) goto LAB_0004ea0a;
            }
            *puVar17 = uVar5;
            puVar17[1] = uVar5;
            puVar17 = puVar17 + 2;
            puVar16 = puVar16 + 1;
          } while (puVar10 + uVar12 + uVar9 + 2 != puVar17);
LAB_0004ea0a:
          uVar9 = uVar9 + 2 + uVar12;
        }
        if ((int)uVar9 < iVar6) {
          pbVar14 = local_58 + uVar9;
          puVar17 = puVar10 + uVar9;
          do {
            uVar8 = FUN_00045cdc(uVar2,*puVar17 << 8 | *puVar17 >> 8,*pbVar14);
            *puVar17 = (ushort)((uVar8 & 0xff) << 8) | (ushort)(uVar8 >> 8) & 0xff;
            puVar17 = puVar17 + 1;
            pbVar14 = pbVar14 + 1;
          } while (puVar17 != puVar10 + iVar6);
        }
        puVar10 = (ushort *)((int)puVar10 + iVar11);
        local_58 = local_58 + iVar18;
        local_48 = local_48 + 1;
      } while (iVar7 != local_48);
    }
  }
  return;
}
```

## `FUN_000041fc` @ `000041fc` score `53`

- reasons: `byte* param` `u8* param` `offset +2` `small indexes` `7-bit mask` `127` `record map shape`

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
    uVar2 = *(ushort *)(param_3 + 4);
    param_5[0x38] = (byte)uVar2 & 0x7f;
    param_5[0x39] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x3a] = (byte)(uVar2 >> 0xe);
    uVar2 = *(ushort *)(param_3 + 6);
    param_5[0x3b] = (byte)uVar2 & 0x7f;
    param_5[0x3c] = (byte)(uVar2 >> 7) & 0x7f;
    param_5[0x3d] = (byte)(uVar2 >> 0xe);
    param_5[0x3e] = param_3[8];
    bVar1 = *param_4;
    param_5[0x3f] = bVar1 & 0x7f;
    param_5[0x40] = bVar1 >> 7;
    bVar1 = param_4[1];
    param_5[0x41] = bVar1 & 0x7f;
    param_5[0x42] = bVar1 >> 7;
    bVar1 = param_4[2];
    param_5[0x43] = bVar1 & 0x7f;
    param_5[0x44] = bVar1 >> 7;
    bVar1 = param_4[3];
    param_5[0x45] = bVar1 & 0x7f;
    param_5[0x46] = bVar1 >> 7;
    bVar1 = param_4[4];
    param_5[0x47] = bVar1 & 0x7f;
    param_5[0x48] = bVar1 >> 7;
    bVar1 = param_4[5];
    param_5[0x49] = bVar1 & 0x7f;
    param_5[0x4a] = bVar1 >> 7;
    bVar1 = param_4[6];
    param_5[0x4b] = bVar1 & 0x7f;
    param_5[0x4c] = bVar1 >> 7;
    bVar1 = param_4[7];
    param_5[0x4d] = bVar1 & 0x7f;
    param_5[0x4e] = bVar1 >> 7;
    bVar1 = param_4[8];
    param_5[0x4f] = bVar1 & 0x7f;
    param_5[0x50] = bVar1 >> 7;
    bVar1 = param_4[9];
    param_5[0x51] = bVar1 & 0x7f;
    param_5[0x52] = bVar1 >> 7;
    bVar1 = param_4[10];
    param_5[0x53] = bVar1 & 0x7f;
    param_5[0x54] = bVar1 >> 7;
    param_5[0x55] = param_4[0xb];
    bVar1 = param_4[0xc];
    param_5[0x56] = bVar1 & 0x7f;
    param_5[0x57] = bVar1 >> 7;
    bVar1 = param_4[0xd];
    param_5[0x58] = bVar1 & 0x7f;
    param_5[0x59] = bVar1 >> 7;
    bVar1 = param_4[0xe];
    param_5[0x5a] = bVar1 & 0x7f;
    param_5[0x5b] = bVar1 >> 7;
    bVar1 = param_4[0xf];
    param_5[0x5c] = bVar1 & 0x7f;
    param_5[0x5d] = bVar1 >> 7;
    bVar1 = param_4[0x10];
    param_5[0x5e] = bVar1 & 0x7f;
    param_5[0x5f] = bVar1 >> 7;
    bVar1 = param_4[0x11];
    param_5[0x60] = bVar1 & 0x7f;
    param_5[0x61] = bVar1 >> 7;
    bVar1 = param_4[0x12];
    param_5[0x62] = bVar1 & 0x7f;
    param_5[99] = bVar1 >> 7;
    bVar1 = param_4[0x13];
    param_5[100] = bVar1 & 0x7f;
    param_5[0x65] = bVar1 >> 7;
    bVar1 = param_4[0x14];
    param_5[0x66] = bVar1 & 0x7f;
    param_5[0x67] = bVar1 >> 7;
    bVar1 = param_4[0x15];
    param_5[0x68] = bVar1 & 0x7f;
    param_5[0x69] = bVar1 >> 7;
    bVar1 = param_4[0x16];
    param_5[0x6a] = bVar1 & 0x7f;
    param_5[0x6b] = bVar1 >> 7;
    uVar3 = 0x6d;
    param_5[0x6c] = param_4[0x17];
  }
  return uVar3;
}
```

## `FUN_0000455c` @ `0000455c` score `53`

- reasons: `u8* param` `byte deref` `offset +2` `small indexes` `channel nibble mask` `7-bit mask` `127`

```c

undefined4 FUN_0000455c(uint *param_1,undefined1 *param_2,uint param_3)

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

## `FUN_00032b10` @ `00032b10` score `53`

- reasons: `byte deref` `u8 deref` `small indexes` `status nibble mask` `channel nibble mask` `record map shape`

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
  if (*(char *)(param_3 + 0x16) != '\0') {
    iVar6 = FUN_00036ab8(param_1,param_2,0x38);
    param_3[0x14] = iVar6;
    if (iVar6 != 0) {
      bVar2 = FUN_00036ab8(param_1,param_2,0x3a);
      *(byte *)(param_3 + 0x16) = bVar2;
      if (2 < bVar2) {
        uVar4 = FUN_00036ab8(param_1,param_2,0x3b);
        param_3[0x15] = uVar4;
        uVar4 = FUN_00036ab8(param_1,param_2,0x39);
        uVar4 = FUN_00036b58(param_1,param_2,uVar4);
        uVar4 = FUN_00032a74(param_1,param_2,param_3[4],uVar4);
        *(char *)((int)param_3 + 0x4a) = (char)uVar4;
        *(char *)((int)param_3 + 0x4b) = (char)((uint)uVar4 >> 8);
        *(char *)(param_3 + 0x13) = (char)((uint)uVar4 >> 0x10);
      }
    }
  }
  if (*(char *)((int)param_3 + 0x3b) != '\0') {
    iVar6 = FUN_00036ab8(param_1,param_2,0x28);
    param_3[0xc] = iVar6;
    if (iVar6 != 0) {
      bVar2 = FUN_00036ab8(param_1,param_2,0x29);
      *(byte *)((int)param_3 + 0x3b) = bVar2;
      if (2 < bVar2) {
        iVar6 = FUN_0003c6b0(param_3[0xc]);
        if (iVar6 == 2) {
          uVar4 = FUN_00036ab8(param_1,param_2,0x5a);
          param_3[0xd] = uVar4;
          uVar4 = FUN_00036ab8(param_1,param_2,0x58);
          uVar4 = FUN_00036b58(param_1,param_2,uVar4);
          uVar4 = FUN_00032a74(param_1,param_2,param_3[4],uVar4);
          *(char *)(param_3 + 0xe) = (char)uVar4;
          *(char *)((int)param_3 + 0x39) = (char)((uint)uVar4 >> 8);
          *(char *)((int)param_3 + 0x3a) = (char)((uint)uVar4 >> 0x10);
        }
        else {
          uVar4 = FUN_00036ab8(param_1,param_2,0x2a);
          uVar3 = FUN_00036b58(param_1,param_2,uVar4);
          uVar1 = FUN_00036ab8(param_1,param_2,0x2b);
          uVar5 = FUN_000329d8(param_1,param_2,param_3[4],uVar3,uVar1);
          *(char *)(param_3 + 0xf) = (char)(uVar5 >> 0x18);
          uVar4 = FUN_00045c94(uVar5 >> 0x10 & 0xff,uVar5 >> 8 & 0xff,uVar5 & 0xff);
          *(char *)(param_3 + 0xe) = (char)uVar4;
          *(char *)((int)param_3 + 0x39) = (char)((uint)uVar4 >> 8);
          *(char *)((int)param_3 + 0x3a) = (char)((uint)uVar4 >> 0x10);
          iVar6 = FUN_00036ab8(param_1,param_2,0x2c);
          *(char *)((int)param_3 + 0x3d) = '\x01' - (iVar6 == 0);
        }
      }
    }
  }
  if (*(char *)(param_3 + 0x1b) != '\0') {
    iVar6 = FUN_00036ab8(param_1,param_2,0x3c);
    param_3[0x17] = iVar6;
    if ((iVar6 != 0) && (2 < *(byte *)(param_3 + 0x1b))) {
      bVar2 = FUN_00036ab8(param_1,param_2,0x3e);
      *(byte *)(param_3 + 0x1b) = bVar2;
      if (2 < bVar2) {
        uVar4 = FUN_00036ab8(param_1,param_2,0x40);
        param_3[0x18] = uVar4;
        uVar4 = FUN_00036ab8(param_1,param_2,0x41);
        param_3[0x19] = uVar4;
        uVar4 = FUN_00036ab8(param_1,param_2,0x42);
        param_3[0x1a] = uVar4;
        uVar4 = FUN_00036ab8(param_1,param_2,0x3d);
        uVar4 = FUN_00036b58(param_1,param_2,uVar4);
        uVar4 = FUN_00032a74(param_1,param_2,param_3[4],uVar4);
        *(char *)((int)param_3 + 0x59) = (char)uVar4;
        *(char *)((int)param_3 + 0x5a) = (char)((uint)uVar4 >> 8);
        *(char *)((int)param_3 + 0x5b) = (char)((uint)uVar4 >> 0x10);
      }
    }
  }
  if (uVar7 < 0xfd) {
    *(char *)(param_3 + 8) = (char)(uVar7 * *(byte *)(param_3 + 8) >> 8);
    *(char *)((int)param_3 + 0x3b) = (char)(uVar7 * *(byte *)((int)param_3 + 0x3b) >> 8);
    *(char *)(param_3 + 0x12) = (char)(uVar7 * *(byte *)(param_3 + 0x12) >> 8);
    *(char *)(param_3 + 0x1b) = (char)(uVar7 * *(byte *)(param_3 + 0x1b) >> 8);
    *(char *)(param_3 + 0x16) = (char)(*(byte *)(param_3 + 0x16) * uVar7 >> 8);
  }
  return;
}
```

## `FUN_00005abc` @ `00005abc` score `51`

- reasons: `byte deref` `u8 deref` `offset +1` `offset +2` `offset +3` `small indexes` `7-bit mask` `127`

```c

void FUN_00005abc(void)

{
  bool bVar1;
  undefined4 uVar2;
  uint *puVar3;
  int iVar4;
  uint uVar5;
  byte *pbVar6;
  int iVar7;
  code *pcVar8;
  uint *puVar9;
  byte bVar10;
  int iVar11;
  ushort *puVar12;
  uint local_28;
  uint local_24;
  uint local_20;
  uint local_1c;
  
  puVar9 = &local_28;
  bVar10 = 0;
  bVar1 = (bool)isCurrentModePrivileged();
  if (bVar1) {
    uVar2 = getCurrentExceptionNumber();
    bVar10 = (byte)uVar2 & 0x1f;
  }
  FUN_000094f4((int)(char)(bVar10 - 0x10));
  iVar11 = *(int *)((char)(bVar10 - 0x10) * 4 + 0x200061bc);
  pbVar6 = *(byte **)(iVar11 + 0x1c);
  if (*(int *)(pbVar6 + 0x10) == 0) {
    iVar7 = *(int *)(iVar11 + 0x10);
    iVar4 = *(int *)(iVar11 + 0x20);
    if (iVar7 == 0) goto LAB_00005af4;
    bVar10 = *(byte *)(iVar11 + 2);
    puVar12 = *(ushort **)(iVar11 + 0xc);
    if ((bVar10 & 3) == 2) {
      *(ushort *)(iVar4 + 0xe) = *puVar12 | 0xfe00;
    }
    else {
      *(char *)(iVar4 + 3) = (char)*puVar12;
    }
    uVar5 = bVar10 & 3;
    iVar7 = iVar7 - uVar5;
    *(int *)(iVar11 + 0x10) = iVar7;
    *(undefined1 **)(iVar11 + 0xc) = (undefined1 *)((int)puVar12 + uVar5);
  }
  else {
    iVar7 = *(int *)(iVar11 + 0x10);
  }
  if (iVar7 != 0) {
    return;
  }
  iVar4 = *(int *)(iVar11 + 0x20);
LAB_00005af4:
  *(byte *)(iVar4 + 2) = *(byte *)(iVar4 + 2) & 0x7f | 4;
  *(undefined4 *)(iVar11 + 0xc) = 0;
  pcVar8 = *(code **)(iVar11 + 0x24);
  if (pcVar8 != (code *)0x0) {
    puVar3 = *(uint **)(iVar11 + 0x28);
    if (puVar3 != (uint *)0x0) {
      local_28 = *puVar3;
      local_24 = puVar3[1];
      local_20 = puVar3[2];
      local_1c = puVar3[3];
      puVar9 = puVar3;
    }
    *puVar9 = (uint)*pbVar6;
    puVar9[2] = 0;
    *(undefined1 *)(puVar9 + 1) = 0x80;
    puVar9[3] = *(uint *)(iVar11 + 0x2c);
    (*pcVar8)();
    puVar9 = *(uint **)(iVar11 + 0x28);
    if (puVar9 != (uint *)0x0) {
      *puVar9 = local_28;
      puVar9[1] = local_24;
      puVar9[2] = local_20;
      puVar9[3] = local_1c;
    }
  }
  return;
}
```

## `FUN_00004e3a` @ `00004e3a` score `50`

- reasons: `byte deref` `u8 deref` `offset +1` `offset +2` `offset +3` `small indexes` `channel nibble mask` `sysex end`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined4 FUN_00004e3a(int param_1)

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
          sVar4 = FUN_00002aa8(*(undefined1 *)(iVar19 + uVar7));
          sVar3 = sVar3 - sVar4;
          *(short *)(&DAT_20006494 + uVar14 * 2) = sVar3;
          *psVar12 = sVar3;
          uVar7 = uVar7 + 1;
          uVar14 = uVar14 + 1;
          psVar12 = psVar12 + 1;
        } while ((uVar7 & 0xff) < (uint)*(byte *)(piVar22 + 1));
      }
      iVar19 = FUN_00003544(uStack00000000,&stack0x00000034);
      uVar14 = uStack00000004;
      uVar7 = (uint)*(byte *)(piVar22 + 1);
      if (((uVar7 == 0) || (*(ushort *)(uVar10 * 2 + 0x20006480) = uStack00000034, uVar7 == 1)) ||
         (*(ushort *)((uVar10 + 1) * 2 + 0x20006480) = uStack00000036, uVar7 == 2)) {
        if (iVar19 == 0) goto LAB_000053a4;
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
          if (iVar19 != 0) goto LAB_00004fa6;
LAB_000053a4:
          iVar18 = uStack00000004 * 2;
          iVar6 = FUN_00003480(uStack00000000);
          if ((iVar6 != 0) && (*(char *)(iVar6 + 0x3c) != '\0')) {
            *(undefined2 *)(*(int *)(unaff_r4 + 0x38) + iVar18) = 0xffff;
          }
          uVar7 = (uint)*(byte *)(piVar22 + 1);
          if (2 < uVar7) goto LAB_00004fa6;
          in_stack_00000030._2_2_ = *(undefined2 *)(*(int *)(unaff_r4 + 0x38) + iVar18);
        }
        else {
          *(undefined2 *)((uVar10 + 9) * 2 + 0x20006480) = uStack00000046;
          if (iVar19 == 0) goto LAB_000053a4;
LAB_00004fa6:
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
          uVar10 = FUN_0000199c(uStack00000000);
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
              iVar6 = (uVar7 + DAT_000057ec) * 2;
              uVar13 = (uint)*(ushort *)((int)&stack0x00000034 + iVar6) -
                       (uint)*(ushort *)((int)&stack0x00000030 + iVar6 + 2) & 0xffff;
              uVar10 = (uint)*(ushort *)((int)&stack0x00000034 + iVar6) -
                       (uint)*(ushort *)((int)&stack0x00000030 + iVar6) & 0xffff;
            }
            else {
              iVar6 = (uVar13 + DAT_000052c4) * 2;
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
                  if ((0x1fe < uVar10) && (uVar10 = uVar10 + DAT_000057e8 & 0xffff, uVar10 != 0)) {
                    in_stack_00000030._2_2_ = (undefined2)((uVar10 << 1) / uVar7);
                  }
                }
                else {
/* ... truncated ... */
```

## `FUN_0005ef68` @ `0005ef68` score `50`

- reasons: `offset +1` `offset +2` `small indexes` `channel nibble mask` `7-bit mask` `127`

```c

uint FUN_0005ef68(int *param_1,int param_2,uint param_3)

{
  ushort uVar1;
  uint uVar2;
  uint uVar3;
  uint uVar4;
  int iVar5;
  uint uVar6;
  uint uVar7;
  int local_2c;
  
  if (param_3 == 0) {
    return 0;
  }
  if (param_1[3] != 0) {
    FUN_0005ffe8(param_1[3],0xffffffff);
  }
  uVar3 = (uint)*(ushort *)(param_1 + 2);
  uVar7 = (uint)*(ushort *)(param_1 + 1);
  uVar4 = (uint)*(ushort *)((int)param_1 + 10);
  if (*(char *)((int)param_1 + 7) < '\0') {
    if (param_3 < uVar7) {
      if (uVar3 < uVar4) {
        iVar5 = uVar7 * 2 - uVar4;
      }
      else {
        iVar5 = -uVar4;
      }
      uVar2 = uVar7 * 2;
      local_2c = param_3 - uVar7;
      if ((int)((uVar3 + iVar5 & 0xffff) + param_3) < (int)uVar2) goto LAB_0005efc2;
      uVar6 = uVar4 + uVar7 & 0xffff;
      uVar3 = uVar6 - param_3 & 0xffff;
      if ((uVar3 < uVar4) || (uVar2 - uVar3 == 0 || uVar2 < uVar3)) {
        uVar3 = uVar3 + uVar7 * -2 & 0xffff;
        uVar6 = param_3 + uVar3 & 0xffff;
      }
      uVar2 = (uint)*(ushort *)((int)param_1 + 6);
      uVar4 = uVar3;
    }
    else {
      if (uVar7 == 0) goto LAB_0005f010;
      uVar2 = (uint)*(ushort *)((int)param_1 + 6);
      param_2 = param_2 + (param_3 - uVar7) * (uVar2 & 0x7fff);
      uVar6 = uVar4 + uVar7 & 0xffff;
      local_2c = 0;
      uVar3 = uVar4;
      param_3 = uVar7;
    }
  }
  else {
    if (uVar3 < uVar4) {
      iVar5 = uVar7 * 2 - uVar4;
    }
    else {
      iVar5 = -uVar4;
    }
    uVar4 = uVar3 + iVar5 & 0xffff;
    if (uVar7 <= uVar4) {
      uVar7 = 0;
      goto LAB_0005f010;
    }
    uVar4 = uVar7 - uVar4;
    uVar1 = (ushort)uVar4;
    if (param_3 < (uVar4 & 0xffff)) {
      uVar1 = (ushort)param_3;
    }
    param_3 = (uint)uVar1;
    local_2c = param_3 - uVar7;
LAB_0005efc2:
    uVar6 = param_3 + uVar3 & 0xffff;
    uVar2 = (uint)*(ushort *)((int)param_1 + 6);
    uVar4 = uVar3;
  }
  for (; uVar7 <= uVar4; uVar4 = uVar4 - uVar7 & 0xffff) {
  }
  uVar2 = uVar2 & 0x7fff;
  uVar7 = uVar7 - uVar4 & 0xffff;
  iVar5 = *param_1 + uVar4 * uVar2;
  if (uVar7 < param_3) {
    uVar7 = uVar2 * uVar7 & 0xffff;
    FUN_0005bef8(iVar5,param_2,uVar7);
    FUN_0005bef8(*param_1,param_2 + uVar7,uVar2 * (uVar4 + local_2c) & 0xffff);
  }
  else {
    FUN_0005bef8(iVar5,param_2,param_3 * uVar2);
  }
  if ((uVar6 < uVar3) || ((uint)*(ushort *)(param_1 + 1) * 2 <= uVar6)) {
    uVar6 = uVar6 + (uint)*(ushort *)(param_1 + 1) * -2;
  }
  *(short *)(param_1 + 2) = (short)uVar6;
  uVar7 = param_3;
LAB_0005f010:
  if (param_1[3] != 0) {
    FUN_0005ff98();
  }
  return uVar7;
}
```

## `FUN_0004e190` @ `0004e190` score `48`

- reasons: `byte deref` `offset +1` `small indexes` `channel nibble mask` `7-bit mask` `127`

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
            uVar1 = FUN_00045cdc(*puVar8,*puVar6,*pbVar10);
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
LAB_0004e2e8:
        do {
          bVar4 = *(byte *)((int)param_1 + 0x22);
          iVar21 = 0;
          puVar19 = puVar6;
          puVar20 = puVar8;
          if (bVar4 == 3) goto LAB_0004e382;
LAB_0004e2f6:
          if (bVar4 < 4) {
            if (bVar4 == 1) {
              if (*puVar20 == 0) goto LAB_0004e550;
              uVar12 = (uint)(*(byte *)((int)puVar19 + 1) >> 3) +
                       (uint)(*(byte *)((int)puVar20 + 1) >> 3);
              if (0x1f < uVar12) {
                uVar12 = 0x1f;
              }
              uVar13 = ((*puVar19 & 0x7ff) >> 5) + ((*puVar20 & 0x7ff) >> 5);
              if (0x3f < uVar13) {
                uVar13 = 0x3f;
              }
              iVar2 = uVar12 * 0x800 + uVar13 * 0x20;
              uVar12 = ((byte)*puVar19 & 0x1f) + ((byte)*puVar20 & 0x1f);
              if (uVar12 < 0x20) goto LAB_0004e3bc;
              uVar12 = 0x1f;
              goto LAB_0004e3bc;
            }
            if (bVar4 != 2) {
              bVar4 = 0;
              goto LAB_0004e690;
            }
            if (*puVar20 == 0) goto LAB_0004e550;
            uVar12 = (uint)(*(byte *)((int)puVar19 + 1) >> 3) -
                     (uint)(*(byte *)((int)puVar20 + 1) >> 3);
            uVar13 = ((*puVar19 & 0x7ff) >> 5) - ((*puVar20 & 0x7ff) >> 5);
            uVar14 = ((byte)*puVar19 & 0x1f) - ((byte)*puVar20 & 0x1f);
            uVar12 = (uVar12 & (int)~uVar12 >> 0x1f) * 0x800 +
                     (uVar13 & (int)~uVar13 >> 0x1f) * 0x20 + (uVar14 & (int)~uVar14 >> 0x1f) &
                     0xffff;
          }
          else {
            if (bVar4 != 4) {
LAB_0004e690:
              FUN_000468e8(2,DAT_0004e940,0x380,DAT_0004e948,DAT_0004e938,bVar4);
              return;
            }
            iVar17 = (uint)(*(byte *)((int)puVar19 + 1) >> 3) -
                     (uint)(*(byte *)((int)puVar20 + 1) >> 3);
            uVar12 = iVar17 >> 0x1f;
            iVar2 = ((*puVar19 & 0x7ff) >> 5) - ((*puVar20 & 0x7ff) >> 5);
            uVar13 = iVar2 >> 0x1f;
/* ... truncated ... */
```

## `FUN_0004ebe4` @ `0004ebe4` score `48`

- reasons: `byte deref` `offset +1` `small indexes` `channel nibble mask` `7-bit mask` `127`

```c

/* WARNING: Control flow encountered bad instruction data */

void FUN_0004ebe4(undefined4 *param_1)

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
              FUN_0004ec14();
              return;
            }
            iVar15 = 0;
            do {
              FUN_00050328(puVar14,puVar12,iVar11 << 1);
              iVar15 = iVar15 + 1;
              puVar14 = (ushort *)((int)puVar14 + iVar17);
              puVar12 = (ushort *)((int)puVar12 + iVar13);
            } while (iVar6 != iVar15);
            FUN_0004ec14();
            return;
          }
          if (iVar6 < 1) {
            FUN_0004ec14();
            return;
          }
          if (iVar11 < 1) {
            FUN_0004ec14();
            return;
          }
          iVar15 = 0;
          puVar22 = puVar14 + iVar11;
          puVar5 = puVar12;
          puVar21 = puVar14;
          do {
            do {
              uVar3 = FUN_00045cdc(*puVar12 << 8 | *puVar12 >> 8,*puVar14 << 8 | *puVar14 >> 8,
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
          FUN_0004ec14();
          return;
        }
        if (uVar23 < 0xfd) {
          if (iVar6 < 1) {
            FUN_0004ec14();
            return;
          }
          if (iVar11 < 1) {
            FUN_0004ec14();
            return;
          }
          puVar22 = puVar14 + iVar11;
          local_40 = 0;
          puVar5 = puVar12;
          pbVar20 = pbVar16;
          puVar21 = puVar14;
          do {
            do {
              uVar3 = FUN_00045cdc(*puVar12 << 8 | *puVar12 >> 8,*puVar14 << 8 | *puVar14 >> 8,
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
          FUN_0004ec14();
          return;
        }
        if (iVar6 < 1) {
          FUN_0004ec14();
          return;
        }
        if (iVar11 < 1) {
          FUN_0004ec14();
          return;
        }
        puVar22 = puVar14 + iVar11;
        iVar11 = 0;
        puVar5 = puVar12;
        pbVar20 = pbVar16;
        puVar21 = puVar14;
        do {
          do {
            uVar23 = FUN_00045cdc(*puVar12 << 8 | *puVar12 >> 8,*puVar14 << 8 | *puVar14 >> 8,
                                  *pbVar16);
            *puVar14 = (ushort)((uVar23 & 0xff) << 8) | (ushort)(uVar23 >> 8) & 0xff;
            puVar14 = puVar14 + 1;
            puVar12 = puVar12 + 1;
            pbVar16 = pbVar16 + 1;
          } while (puVar22 != puVar14);
          puVar14 = (ushort *)((int)puVar21 + iVar17);
          puVar12 = (ushort *)((int)puVar5 + iVar13);
          puVar22 = (ushort *)((int)puVar22 + iVar17);
          pbVar16 = pbVar20 + iVar15;
          iVar11 = iVar11 + 1;
          puVar5 = puVar12;
          pbVar20 = pbVar16;
          puVar21 = puVar14;
        } while (iVar6 != iVar11);
        FUN_0004ec14();
        return;
      }
      if (0 < iVar6) {
        puVar5 = puVar12 + iVar11;
        local_38 = 0;
        do {
          pbVar20 = pbVar16;
          puVar21 = puVar12;
          puVar22 = puVar14;
          if (0 < iVar11) {
            do {
              local_2a[0] = *puVar21 << 8 | *puVar21 >> 8;
              FUN_00050328(&local_2c,local_2a,2);
              bVar4 = *(byte *)((int)param_1 + 0x22);
              if (bVar4 == 3) {
                if (*puVar21 != DAT_0004f3e0) {
                  uVar3 = *puVar22 & 0xff;
/* ... truncated ... */
```

## `FUN_00037498` @ `00037498` score `44`

- reasons: `byte deref` `u8 deref` `offset +1` `offset +2` `small indexes` `channel nibble mask` `sysex end`

```c

void FUN_00037498(int param_1,int param_2,undefined2 param_3,undefined2 param_4,undefined2 *param_5)

{
  char cVar1;
  undefined1 uVar2;
  int iVar3;
  int iVar4;
  undefined4 *puVar5;
  int *piVar6;
  int iVar7;
  int iVar8;
  int local_88;
  int local_84;
  undefined1 auStack_80 [96];
  
  *(byte *)(param_1 + 0x2a) = *(byte *)(param_1 + 0x2a) | 8;
  *(undefined2 *)(param_1 + 0x28) = param_3;
  iVar3 = FUN_00036ab8(param_1,param_2,*(undefined1 *)(param_5 + 4));
  *(undefined2 *)(param_1 + 0x28) = param_4;
  iVar4 = FUN_00036ab8(param_1,param_2,*(undefined1 *)(param_5 + 4));
  *(byte *)(param_1 + 0x2a) = *(byte *)(param_1 + 0x2a) & 0xf7;
  if ((iVar3 != iVar4) || (iVar3 = FUN_00045c54(iVar4,iVar4), iVar3 == 0)) {
    *(undefined2 *)(param_1 + 0x28) = param_3;
    iVar3 = FUN_00036ab8(param_1,param_2,*(undefined1 *)(param_5 + 4));
    *(undefined2 *)(param_1 + 0x28) = param_4;
    puVar5 = (undefined4 *)FUN_000365f0(param_1,param_2);
    FUN_0004763c(*puVar5,*(undefined1 *)(param_5 + 4),iVar3);
    cVar1 = *(char *)(param_5 + 4);
    if (*(char *)(DAT_00037648 + 0x24) != '\0') {
      FUN_00036f68(param_1,*(undefined4 *)(param_5 + 2));
      cVar1 = *(char *)(param_5 + 4);
    }
    local_88 = iVar3;
    local_84 = iVar4;
    if (cVar1 == '\f') {
      if (iVar3 == DAT_0003765c) {
        iVar7 = FUN_00033ba0(param_1);
        iVar8 = FUN_00033be4(param_1);
        if (iVar7 / 2 < iVar8 / 2) {
          local_88 = iVar7 / 2 + 1;
          local_84 = local_88;
          if (iVar4 != iVar3) {
            local_84 = iVar4;
          }
        }
        else {
          local_88 = iVar8 / 2 + 1;
          local_84 = local_88;
          if (iVar4 != iVar3) {
            local_84 = iVar4;
          }
        }
      }
      else if (iVar4 == DAT_0003765c) {
        iVar4 = FUN_00033ba0(param_1);
        iVar7 = FUN_00033be4(param_1);
        iVar3 = iVar4 / 2;
        if (iVar7 / 2 <= iVar4 / 2) {
          iVar3 = iVar7 / 2;
        }
        local_84 = iVar3 + 1;
      }
    }
    piVar6 = (int *)FUN_00046704(DAT_0003764c);
    if (piVar6 == (int *)0x0) {
      FUN_000468e8(3,DAT_00037670,0x1c9,DAT_00037668,DAT_0003766c,DAT_00037664,DAT_00037660);
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    *piVar6 = param_1;
    piVar6[3] = local_88;
    piVar6[4] = local_84;
    uVar2 = *(undefined1 *)(param_5 + 4);
    piVar6[2] = param_2;
    *(undefined1 *)(piVar6 + 1) = uVar2;
    FUN_00044cac(auStack_80);
    FUN_00044fb8(auStack_80,piVar6);
    FUN_00044fbc(auStack_80,DAT_00037650);
    FUN_00044fdc(auStack_80,DAT_00037654);
    FUN_00044fe0(auStack_80,DAT_00037658);
    FUN_00044fcc(auStack_80,0,0xff);
    FUN_00044fc0(auStack_80,*param_5);
    FUN_00044fc4(auStack_80,param_5[1]);
    FUN_00044fd8(auStack_80,*(undefined4 *)(param_5 + 6));
    FUN_00044ff8(auStack_80,0);
    FUN_00045010(auStack_80,*(undefined4 *)(param_5 + 8));
    FUN_00044ce0(auStack_80);
  }
  return;
}
```

## `FUN_0005d6d0` @ `0005d6d0` score `43`

- reasons: `byte deref` `u8 deref` `offset +1` `offset +2` `offset +3` `7-bit mask` `127`

```c

void FUN_0005d6d0(uint param_1,undefined2 param_2,undefined1 param_3)

{
  uint uVar1;
  int iVar2;
  uint uVar3;
  int iVar4;
  undefined4 *puVar5;
  
  iVar2 = DAT_0005d74c;
  uVar3 = param_1 & 0x7f;
  uVar1 = param_1 >> 7;
  iVar4 = (uVar3 * 2 + uVar1) * 0x20 + DAT_0005d74c;
  *(char *)(iVar4 + 2) = (char)param_1;
  *(byte *)(iVar4 + 1) = (byte)uVar1 ^ 1;
  *(undefined2 *)(iVar4 + 0x18) = param_2;
  *(undefined1 *)(iVar4 + 3) = 0;
  *(undefined1 *)(iVar4 + 0x1b) = param_3;
  if (uVar1 == 1) {
    puVar5 = (undefined4 *)(uVar3 * 8 + DAT_0005d75c);
    iVar4 = uVar3 * 0x40 + iVar2;
    *(undefined4 **)(iVar4 + 0x28) = puVar5;
    *puVar5 = 0;
    if (uVar3 != 0) {
      *(uint *)(iVar4 + 0x24) = uVar3 * 8 + DAT_0005d760;
      return;
    }
  }
  else {
    puVar5 = (undefined4 *)(uVar3 * 8 + DAT_0005d750);
    iVar4 = uVar3 * 0x40 + iVar2;
    *(undefined4 **)(iVar4 + 8) = puVar5;
    *puVar5 = 0;
    if (uVar3 != 0) {
      *(uint *)(iVar4 + 4) = uVar3 * 8 + DAT_0005d758;
      return;
    }
  }
  iVar2 = uVar1 * 0x20 + iVar2;
  *(undefined4 *)(iVar2 + 4) = 0;
  *(undefined4 *)(iVar2 + 0xc) = DAT_0005d754;
  return;
}
```

## `FUN_000437a8` @ `000437a8` score `42`

- reasons: `byte* param` `byte deref` `channel nibble mask` `0x80` `127`

```c

void FUN_000437a8(int param_1,int param_2,int param_3,int param_4,int param_5,int param_6,
                 int param_7,int param_8,int param_9,short *param_10,byte *param_11,char param_12,
                 char param_13)

{
  byte bVar1;
  short sVar2;
  short sVar3;
  uint uVar4;
  int iVar5;
  int iVar6;
  undefined4 uVar7;
  undefined4 uVar8;
  uint uVar9;
  int iVar10;
  int iVar11;
  int iVar12;
  int iVar13;
  int iVar14;
  uint uVar15;
  int iVar16;
  short *psVar17;
  int iVar18;
  bool bVar19;
  int local_5c;
  int local_54;
  int local_50;
  uint local_3c;
  uint local_38;
  
  if (0 < param_9) {
    iVar12 = param_1 + param_4 * param_3;
    iVar13 = param_4 / 2;
    psVar17 = param_10 + param_9;
    iVar16 = 0;
    local_5c = 0;
    do {
      uVar9 = (iVar16 >> 8) + param_5;
      iVar14 = (int)uVar9 >> 8;
      if (((int)uVar9 < 0) || (param_2 <= iVar14)) {
LAB_000438cc:
        *param_11 = 0;
      }
      else {
        uVar4 = (local_5c >> 8) + param_6;
        iVar11 = (int)uVar4 >> 8;
        if (((int)uVar4 < 0) || (param_3 <= iVar11)) goto LAB_000438cc;
        if ((uVar9 & 0x80) == 0) {
          iVar10 = 0x7f - (uVar9 & 0xff);
          local_54 = -1;
        }
        else {
          iVar10 = (uVar9 & 0xff) - 0x80;
          local_54 = 1;
        }
        local_3c = iVar10 * 2;
        if ((uVar4 & 0x80) == 0) {
          iVar5 = 0x7f - (uVar4 & 0xff);
          local_50 = -1;
        }
        else {
          iVar5 = (uVar4 & 0xff) - 0x80;
          local_50 = 1;
        }
        local_38 = iVar5 * 2;
        iVar18 = iVar11 * param_4 + iVar14 * 2;
        iVar6 = param_1 + iVar18;
        *param_10 = *(short *)(param_1 + iVar18);
        if (param_13 == '\0') {
LAB_00043888:
          uVar9 = 0xff;
          if (param_12 != '\0') {
LAB_00043892:
            uVar9 = (uint)*(byte *)(iVar12 + iVar14 + iVar11 * iVar13);
          }
          if (iVar14 == 0) {
            iVar6 = param_2;
            if (local_54 != -1) goto joined_r0x00043936;
LAB_0004393a:
            *param_11 = (byte)((iVar10 * -2 + 0xff) * uVar9 >> 8);
          }
          else {
            iVar6 = local_54;
            if (param_2 + -1 == iVar14) {
joined_r0x00043936:
              if (iVar6 == 1) goto LAB_0004393a;
            }
            if (iVar11 == 0) {
LAB_000438ba:
              bVar19 = local_50 != -1;
              local_50 = param_3;
              if (bVar19) {
joined_r0x0004391a:
                if (local_50 != 1) goto LAB_000438c6;
              }
LAB_0004391e:
              *param_11 = (byte)((iVar5 * -2 + 0xff) * uVar9 >> 8);
            }
            else {
              if (param_3 + -1 == iVar11) goto joined_r0x0004391a;
LAB_000438c6:
              *param_11 = (byte)uVar9;
            }
          }
        }
        else {
          if (local_54 + iVar14 == -1) {
            uVar9 = 0xff;
            if (param_12 != '\0') {
              uVar9 = (uint)*(byte *)(iVar12 + iVar13 * iVar11);
            }
            goto LAB_0004393a;
          }
          if (param_2 <= local_54 + iVar14) goto LAB_00043888;
          if (local_50 + iVar11 == -1) {
            if (param_12 != '\0') goto LAB_00043892;
            if (iVar14 == 0) {
              if ((local_54 == -1) || (param_2 == 1)) {
                uVar9 = 0xff;
                goto LAB_0004393a;
              }
              uVar9 = 0xff;
              goto LAB_000438ba;
            }
            if (iVar14 == param_2 + -1) {
              if (local_54 == 1) {
                uVar9 = 0xff;
                goto LAB_0004393a;
              }
              uVar9 = 0xff;
            }
            else {
              uVar9 = 0xff;
            }
            goto LAB_0004391e;
          }
          if (param_3 <= local_50 + iVar11) goto LAB_00043888;
          sVar3 = *(short *)(local_54 * 2 + iVar6);
          sVar2 = *(short *)(iVar6 + local_50 * param_4);
          if (param_12 == '\0') {
            *param_11 = 0xff;
          }
          else {
            iVar14 = iVar13 * iVar11 + iVar14;
            iVar11 = iVar12 + iVar14;
            bVar1 = *(byte *)(iVar12 + iVar14);
            uVar15 = (uint)bVar1;
            *param_11 = bVar1;
            uVar9 = (uint)*(byte *)(iVar11 + local_54);
            uVar4 = (uint)*(byte *)(iVar11 + iVar13 * local_50);
            if (uVar15 != uVar4) {
              uVar4 = uVar15 * (iVar5 * -2 + 0x100) + local_38 * uVar4 >> 8 & 0xff;
            }
            if (uVar15 != uVar9) {
              uVar9 = (iVar10 * -2 + 0x100) * uVar15 + local_3c * uVar9 >> 8 & 0xff;
            }
            iVar14 = (int)(uVar4 + uVar9) >> 1;
            *param_11 = (byte)iVar14;
            if (iVar14 == 0) goto LAB_000438d0;
          }
          if ((*param_10 != sVar2) || (sVar2 != sVar3)) {
            uVar7 = FUN_00045cdc(sVar2,*param_10,local_38 & 0xff);
            uVar8 = FUN_00045cdc(sVar3,*param_10,local_3c & 0xff);
            sVar3 = FUN_00045cdc(uVar8,uVar7,0x7f);
            *param_10 = sVar3;
          }
        }
      }
LAB_000438d0:
      param_10 = param_10 + 1;
      iVar16 = iVar16 + param_7;
      local_5c = local_5c + param_8;
      param_11 = param_11 + 1;
    } while (psVar17 != param_10);
  }
  return;
}
```

## `FUN_00047db4` @ `00047db4` score `42`

- reasons: `byte deref` `status nibble mask` `channel nibble mask` `0xf0`

```c

void FUN_00047db4(int param_1,int param_2)

{
  byte bVar1;
  int iVar2;
  int iVar3;
  uint uVar4;
  
  iVar2 = 0;
  iVar3 = 0;
  if (param_2 != 0) {
    do {
      bVar1 = *(byte *)(param_1 + iVar2);
      if (bVar1 == 0) {
        return;
      }
      uVar4 = 1;
      if ((char)bVar1 < '\0') {
        if ((bVar1 & 0xe0) == 0xc0) {
          uVar4 = 2;
        }
        else if ((bVar1 & 0xf0) == 0xe0) {
          uVar4 = 3;
        }
        else {
          uVar4 = (uint)((bVar1 & 0xf8) != 0xf0);
        }
      }
      iVar3 = iVar3 + 1;
      iVar2 = iVar2 + uVar4;
    } while (param_2 != iVar3);
  }
  return;
}
```

## `FUN_0000657c` @ `0000657c` score `41`

- reasons: `u8 deref` `small indexes` `channel nibble mask` `7-bit mask` `127`

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

## `FUN_00041554` @ `00041554` score `41`

- reasons: `byte deref` `offset +1` `offset +3` `small indexes` `channel nibble mask` `sysex end`

```c

void FUN_00041554(undefined4 param_1,int param_2,undefined4 param_3)

{
  byte bVar1;
  ushort uVar2;
  int iVar3;
  byte *pbVar4;
  int iVar5;
  byte *pbVar6;
  byte *pbVar7;
  int iVar8;
  int iVar9;
  int *piVar10;
  int local_d8;
  int local_d4;
  int local_d0;
  int local_cc;
  int local_c4;
  int local_c0;
  int local_b4;
  int local_b0;
  int iStack_ac;
  int local_a8;
  int local_a4;
  int local_a0;
  int local_9c;
  int local_98;
  undefined1 auStack_94 [28];
  int local_78;
  int local_68;
  byte bStack_43;
  
  piVar10 = *(int **)(param_2 + 0x1c);
  iVar8 = *piVar10;
  if (iVar8 == 0) {
    return;
  }
  if (*(int *)(param_2 + 0x68) != 0) {
    iVar3 = FUN_0003e060(auStack_94,*(int *)(param_2 + 0x68),0);
    if (iVar3 == 1) {
      if (local_68 != 0) {
        if ((*(byte *)(local_68 + 1) & 0xf7) == 6) {
          uVar2 = *(ushort *)(local_68 + 8);
          local_b4 = *(int *)(param_2 + 0x58);
          local_b0 = *(undefined4 *)(param_2 + 0x5c);
          iStack_ac = *(undefined4 *)(param_2 + 0x60);
          local_a8 = *(undefined4 *)(param_2 + 100);
          FUN_00045064(&local_c4,0,0,*(ushort *)(local_68 + 4) - 1,*(ushort *)(local_68 + 6) - 1);
          FUN_00045574(&local_b4,&local_c4,9,0,0);
          local_b4 = piVar10[1];
          local_b0 = piVar10[2];
          iStack_ac = piVar10[3];
          local_a8 = piVar10[4];
          iVar3 = FUN_000450d4(&local_a4,&local_c4,&local_b4);
          if (iVar3 == 0) {
            FUN_0003e180(auStack_94);
            return;
          }
          FUN_0005beec(&local_d8,0,8);
          local_d0 = *(ushort *)(*piVar10 + 4) - 1;
          local_cc = (local_a0 + -1) - local_b0;
          FUN_0003bf98(*piVar10,&local_d8);
          local_d4 = (local_98 + 1) - local_b0;
          local_cc = *(ushort *)(*piVar10 + 6) - 1;
          FUN_0003bf98(*piVar10,&local_d8);
          local_d8 = 0;
          local_d4 = 0;
          local_d0 = (local_a4 + -1) - local_b4;
          FUN_0003bf98(*piVar10,&local_d8);
          local_d8 = (local_9c + 1) - local_b4;
          local_d0 = *(ushort *)(*piVar10 + 4) - 1;
          FUN_0003bf98(*piVar10,&local_d8);
          iVar8 = FUN_0003bf18(iVar8,local_a4 - local_b4,local_a0 - local_b0);
          pbVar4 = (byte *)FUN_0003bf18(local_68,local_a4 - local_c4,local_a0 - local_c0);
          iVar3 = FUN_000458f0(&local_a4);
          iVar5 = FUN_000458e4(&local_a4);
          if ((0 < iVar3) && (0 < iVar5)) {
            iVar9 = 0;
            do {
              pbVar7 = (byte *)(iVar8 + 3);
              pbVar6 = pbVar4;
              do {
                bVar1 = *pbVar6;
                pbVar6 = pbVar6 + 1;
                *pbVar7 = (byte)((uint)bVar1 * (uint)*pbVar7 >> 8);
                pbVar7 = pbVar7 + 4;
              } while ((byte *)(iVar8 + iVar5 * 4 + 3) != pbVar7);
              iVar9 = iVar9 + 1;
              iVar8 = iVar8 + (uint)*(ushort *)(*piVar10 + 8);
              pbVar4 = pbVar4 + uVar2;
            } while (iVar3 != iVar9);
          }
          FUN_0003e180(auStack_94);
          iVar8 = *piVar10;
        }
        else {
          FUN_0003e180(auStack_94);
          FUN_000468e8(2,DAT_00041778,DAT_0004177c,DAT_00041774,DAT_00041770);
          iVar8 = *piVar10;
        }
        goto LAB_000415ae;
      }
      FUN_0003e180(auStack_94);
    }
    FUN_000468e8(2,DAT_00041778,0x2f0,DAT_00041774,DAT_00041784);
    iVar8 = *piVar10;
  }
LAB_000415ae:
  FUN_0005bef8(auStack_94,param_2,0x6c);
  local_78 = iVar8;
  if ((int)((uint)bStack_43 << 0x1a) < 0) {
    FUN_0003c6cc(param_1,auStack_94,param_3,DAT_00041780);
  }
  else {
    FUN_0003cc44(param_1,auStack_94,param_3,DAT_00041780);
  }
  return;
}
```

## `FUN_000501dc` @ `000501dc` score `41`

- reasons: `u8 deref` `offset +1` `offset +2` `offset +3` `small indexes` `channel nibble mask`

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
        *(undefined1 *)((int)puVar5 + 0x13) = *(undefined1 *)((int)puVar4 + 0x13);
        *(undefined1 *)(puVar5 + 5) = *(undefined1 *)(puVar4 + 5);
        *(undefined1 *)((int)puVar5 + 0x15) = *(undefined1 *)((int)puVar4 + 0x15);
        *(undefined1 *)((int)puVar5 + 0x16) = *(undefined1 *)((int)puVar4 + 0x16);
        *(undefined1 *)((int)puVar5 + 0x17) = *(undefined1 *)((int)puVar4 + 0x17);
        *(undefined1 *)(puVar5 + 6) = *(undefined1 *)(puVar4 + 6);
        *(undefined1 *)((int)puVar5 + 0x19) = *(undefined1 *)((int)puVar4 + 0x19);
        *(undefined1 *)((int)puVar5 + 0x1a) = *(undefined1 *)((int)puVar4 + 0x1a);
        *(undefined1 *)((int)puVar5 + 0x1b) = *(undefined1 *)((int)puVar4 + 0x1b);
        *(undefined1 *)(puVar5 + 7) = *(undefined1 *)(puVar4 + 7);
        *(undefined1 *)((int)puVar5 + 0x1d) = *(undefined1 *)((int)puVar4 + 0x1d);
        *(undefined1 *)((int)puVar5 + 0x1e) = *(undefined1 *)((int)puVar4 + 0x1e);
        puVar2 = (undefined1 *)((int)puVar4 + 0x1f);
        puVar4 = puVar4 + 8;
        *(undefined1 *)((int)puVar5 + 0x1f) = *puVar2;
        puVar5 = puVar5 + 8;
      } while (puVar4 != param_2 + (uVar6 + 1) * 8);
      param_3 = (param_3 - 0x20) + uVar6 * -0x20;
      param_1 = param_1 + uVar6 * 8 + 8;
      param_2 = param_2 + uVar6 * 8 + 8;
    }
    puVar5 = (undefined4 *)((int)param_2 + param_3);
    do {
      uVar3 = *(undefined1 *)param_2;
      param_2 = (undefined4 *)((int)param_2 + 1);
      *(undefined1 *)param_1 = uVar3;
      param_1 = (undefined4 *)((int)param_1 + 1);
    } while (param_2 != puVar5);
  }
  return;
}
```

## `FUN_0005a580` @ `0005a580` score `40`

- reasons: `byte* param` `offset +2` `small indexes` `7-bit mask` `127`

```c

undefined4
FUN_0005a580(sbyte *param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4,
            undefined4 param_5,undefined4 param_6)

{
  short sVar1;
  bool bVar2;
  undefined2 *puVar3;
  int iVar4;
  undefined4 uVar5;
  uint uVar6;
  ushort uVar7;
  
  uVar6 = 0;
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    uVar6 = isIRQinterruptsEnabled();
  }
  disableIRQinterrupts();
  do {
  } while (**(int **)(param_1 + 0x10) == 0);
  DataMemoryBarrier(0x1f);
  sVar1 = *(short *)(param_1 + 2);
  if (sVar1 < 0) {
    DataMemoryBarrier(0x1f);
    **(undefined4 **)(param_1 + 0x10) = 0;
    bVar2 = (bool)isCurrentModePrivileged();
    if (bVar2) {
      enableIRQinterrupts((uVar6 & 1) == 1);
    }
    uVar5 = 0xffffffff;
  }
  else {
    iVar4 = sVar1 * 0x18;
    puVar3 = (undefined2 *)(*(int *)(param_1 + 0x14) + iVar4);
    *(undefined2 *)(param_1 + 2) = *(undefined2 *)(*(int *)(param_1 + 0x14) + iVar4);
    DataMemoryBarrier(0x1f);
    **(undefined4 **)(param_1 + 0x10) = 0;
    bVar2 = (bool)isCurrentModePrivileged();
    if (bVar2) {
      enableIRQinterrupts((uVar6 & 1) == 1);
    }
    *(undefined4 *)(puVar3 + 8) = param_5;
    *(undefined4 *)(puVar3 + 10) = param_6;
    *(undefined4 *)(puVar3 + 4) = param_3;
    *(undefined4 *)(puVar3 + 6) = param_4;
    uVar7 = puVar3[1] + 1 & 0x7fff;
    if (uVar7 == 0) {
      uVar7 = 1;
    }
    puVar3[1] = uVar7;
    uVar5 = CONCAT22(sVar1,uVar7);
    uVar6 = 0;
    bVar2 = (bool)isCurrentModePrivileged();
    if (bVar2) {
      uVar6 = isIRQinterruptsEnabled();
    }
    disableIRQinterrupts();
    do {
    } while (**(int **)(param_1 + 0x10) == 0);
    DataMemoryBarrier(0x1f);
    *puVar3 = *(undefined2 *)(param_1 + 4);
    *(short *)(param_1 + 4) = sVar1;
    DataMemoryBarrier(0x1f);
    **(undefined4 **)(param_1 + 0x10) = 0;
    bVar2 = (bool)isCurrentModePrivileged();
    if (bVar2) {
      enableIRQinterrupts((uVar6 & 1) == 1);
    }
    *(int *)(*(int *)(param_1 + 0xc) + DAT_0005a638) = 1 << *param_1;
  }
  return uVar5;
}
```

## `FUN_00043030` @ `00043030` score `39`

- reasons: `byte deref` `u8 deref` `offset +1` `offset +2` `small indexes` `channel nibble mask`

```c

void FUN_00043030(undefined4 *param_1,undefined4 *param_2,uint param_3,byte param_4)

{
  char cVar1;
  char cVar2;
  int iVar3;
  int iVar4;
  undefined4 uVar5;
  undefined1 *puVar6;
  int *piVar7;
  int *piVar8;
  int iVar9;
  char cVar10;
  undefined4 uVar11;
  uint *puVar12;
  int iVar13;
  int iVar14;
  undefined2 *puVar15;
  int iVar16;
  char cVar17;
  undefined4 uVar18;
  int *piVar19;
  uint uVar20;
  uint uVar21;
  int iVar22;
  ushort *puVar23;
  uint uVar24;
  int iVar25;
  int iVar26;
  int *piVar27;
  int iVar28;
  char *pcVar29;
  int *piVar30;
  bool bVar31;
  int local_48 [4];
  uint local_38 [5];
  
  iVar3 = FUN_000458e4(param_2);
  iVar4 = FUN_000458f0(param_2);
  if (iVar4 < iVar3) {
    iVar3 = iVar4;
  }
  uVar21 = iVar3 >> 1;
  if ((int)param_3 < iVar3 >> 1) {
    uVar21 = param_3;
  }
  uVar5 = *param_2;
  uVar11 = param_2[2];
  uVar18 = param_2[3];
  param_1[3] = param_2[1];
  param_1[4] = uVar11;
  param_1[5] = uVar18;
  *(byte *)(param_1 + 7) = *(byte *)(param_1 + 7) & 0xfe | param_4 & 1;
  *param_1 = DAT_000433a8;
  uVar24 = (int)~uVar21 >> 0x1f & uVar21;
  param_1[2] = uVar5;
  param_1[6] = uVar24;
  *(undefined1 *)(param_1 + 1) = 2;
  iVar3 = DAT_000433ac;
  if ((int)uVar21 < 1) {
    param_1[8] = 0;
  }
  else {
    iVar4 = 0;
    puVar12 = (uint *)(DAT_000433ac + 0x160);
    do {
      iVar22 = (int)uVar24 >> 4;
      if (uVar24 == *puVar12) {
        iVar26 = iVar4 * 0x1c + DAT_000433ac;
        piVar30 = (int *)(iVar26 + 0x15c);
        *piVar30 = *piVar30 + 1;
        iVar25 = 1;
        if (0xf < (int)uVar21) {
          iVar25 = iVar22;
        }
        iVar25 = *(int *)(iVar26 + 0x158) + iVar25;
        if (1000 < iVar25) {
          iVar25 = 1000;
        }
        *(int *)(iVar3 + iVar4 * 0x1c + 0x158) = iVar25;
        param_1[8] = iVar3 + iVar4 * 0x1c + 0x148;
        return;
      }
      iVar4 = iVar4 + 1;
      puVar12 = puVar12 + 7;
    } while (iVar4 != 4);
    piVar30 = (int *)0x0;
    piVar19 = (int *)(DAT_000433ac + 0x148);
    piVar8 = (int *)(DAT_000433ac + 0x1b8);
    do {
      piVar27 = piVar19;
      if (piVar19[5] == 0) {
        piVar7 = piVar19;
        if (piVar30 == (int *)0x0) {
          piVar27 = piVar19 + 7;
          if (piVar27 == piVar8) break;
          piVar7 = piVar27;
          piVar30 = piVar19;
          if (piVar19[0xc] != 0) goto LAB_0004310a;
        }
        iVar3 = piVar30[4];
        piVar27 = piVar7 + 7;
        if (piVar7[4] < iVar3) goto LAB_000430e4;
        while( true ) {
          piVar7 = piVar30;
          if (piVar27 == piVar8) goto LAB_00043114;
          if (piVar27[5] != 0) break;
          while (piVar7 = piVar27, piVar27 = piVar7 + 7, piVar7[4] < iVar3) {
LAB_000430e4:
            if (piVar27 == piVar8) goto LAB_0004311c;
            piVar30 = piVar7;
            if (piVar27[5] != 0) goto LAB_0004310a;
            iVar3 = piVar7[4];
          }
        }
      }
LAB_0004310a:
      piVar19 = piVar27 + 7;
      piVar7 = piVar30;
    } while (piVar19 != piVar8);
LAB_00043114:
    if (piVar7 == (int *)0x0) {
      piVar7 = (int *)FUN_0004ceb8(0x1c);
      if (piVar7 == (int *)0x0) {
        FUN_000468e8(3,DAT_0004354c,0x155,DAT_0004355c,DAT_00043550,DAT_00043558,DAT_00043540);
        do {
                    /* WARNING: Do nothing block with infinite loop */
        } while( true );
      }
      piVar7[4] = -1;
    }
    else {
LAB_0004311c:
      piVar7[5] = piVar7[5] + 1;
      iVar3 = 1;
      if ((0xf < (int)uVar21) && (iVar3 = iVar22, 1000 < iVar22)) {
        iVar3 = 1000;
      }
      piVar7[4] = iVar3;
    }
    iVar3 = *piVar7;
    param_1[8] = piVar7;
    piVar7[6] = uVar24;
    if (iVar3 != 0) {
      FUN_0004cedc();
    }
    iVar3 = uVar24 + 1;
    puVar6 = (undefined1 *)FUN_0004cea4(iVar3 * 6);
    *piVar7 = (int)puVar6;
    if (puVar6 == (undefined1 *)0x0) {
      FUN_000468e8(3,DAT_0004354c,0x438,DAT_00043544,DAT_00043550,DAT_00043548,DAT_00043540);
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    piVar7[1] = (int)puVar6;
    piVar7[3] = (int)(puVar6 + uVar24 * 2 + 2);
    uVar20 = uVar24 * 4;
    piVar7[2] = (int)(puVar6 + uVar20 + 4);
    if (uVar21 != 1) {
      iVar4 = FUN_0004ceb8(iVar3 * 0x10);
      if (iVar4 == 0) {
        FUN_000468e8(3,DAT_0004354c,0x448,DAT_00043544,DAT_00043550,DAT_00043554,DAT_00043540);
        do {
                    /* WARNING: Do nothing block with infinite loop */
        } while( true );
      }
      iVar22 = uVar24 * -4 + 1;
      local_48[0] = (int)uVar20 >> 2;
      iVar28 = iVar3 * 8 + iVar4;
      local_38[0] = 0;
      iVar25 = 0;
      iVar26 = 0;
      iVar3 = 0;
LAB_000431b2:
      iVar13 = iVar25 + 4;
      piVar30 = local_48;
      puVar12 = local_38;
LAB_000431bc:
/* ... truncated ... */
```

## `FUN_00059d0c` @ `00059d0c` score `39`

- reasons: `byte deref` `u8 deref` `offset +1` `offset +2` `small indexes` `channel nibble mask`

```c

void FUN_00059d0c(int param_1,undefined4 param_2,uint param_3)

{
  char cVar1;
  char cVar2;
  bool bVar3;
  undefined1 uVar4;
  int iVar5;
  undefined4 uVar6;
  ushort uVar7;
  int extraout_r1;
  uint uVar8;
  int iVar9;
  uint uVar10;
  undefined4 *puVar11;
  undefined4 *puVar12;
  undefined4 *puVar13;
  undefined4 *puVar14;
  int iVar15;
  uint uVar16;
  undefined4 *local_2c;
  
  puVar12 = DAT_00059f34;
  uVar16 = 0;
  bVar3 = (bool)isCurrentModePrivileged();
  if (bVar3) {
    uVar16 = isIRQinterruptsEnabled();
  }
  disableIRQinterrupts();
  do {
  } while (*DAT_00059f2c == 0);
  DataMemoryBarrier(0x1f);
  cVar1 = *DAT_00059f30;
  iVar15 = (int)cVar1;
  if (iVar15 < 0) {
                    /* WARNING: Subroutine does not return */
    FUN_0005d354(DAT_00059f6c,0x17c,DAT_00059f74,DAT_00059f70);
  }
  puVar14 = DAT_00059f34 + iVar15 * 3;
  *DAT_00059f30 = *(char *)((int)puVar14 + 6);
  iVar9 = (param_1 + 0x10) * 4;
  uVar10 = *(uint *)(*(int *)(DAT_00059f38 + 8) + iVar9);
  uVar4 = (undefined1)param_3;
  if (uVar10 - (int)puVar12 < 0x30) {
    puVar13 = (undefined4 *)(uVar10 & 0xfffffffe);
    FUN_0005b480((int)puVar13 - (int)puVar12,0xc);
    if (extraout_r1 != 0) {
LAB_00059f1c:
                    /* WARNING: Subroutine does not return */
      FUN_0005d354(DAT_00059f6c,0x194,DAT_00059f74,DAT_00059f7c);
    }
    if (param_3 < *(byte *)((int)puVar13 + 7)) {
      do {
        puVar11 = puVar13;
        cVar2 = *(char *)((int)puVar11 + 6);
        if (cVar2 < 0) {
          uVar7 = (ushort)DAT_00059f58;
          goto LAB_00059e16;
        }
        puVar13 = puVar12 + cVar2 * 3;
      } while (param_3 < *(byte *)((int)(puVar12 + cVar2 * 3) + 7));
      if (*(ushort *)(puVar11 + 1) >> 0xb != 0x1c) {
        FUN_00059c4c();
        goto LAB_00059f1c;
      }
      iVar5 = (((int)((uint)*(ushort *)(puVar11 + 1) << 0x15) >> 0x14) + 8) -
              (int)(puVar12 + iVar15 * 3 + 1);
      if ((uint)((int)puVar11 + DAT_00059f44 + iVar5) <= DAT_00059f48) {
        uVar7 = (ushort)DAT_00059f50 | (ushort)(((int)puVar11 + iVar5 + -4 & 0xfffU) >> 1);
LAB_00059e16:
        local_2c = puVar11 + 1;
        if ((uint)((int)puVar14 + (DAT_00059f44 - (int)local_2c)) <= DAT_00059f48) {
          *(ushort *)(puVar11 + 1) =
               (ushort)(((int)puVar14 + (-4 - (int)local_2c) & 0xfffU) >> 1) | (ushort)DAT_00059f50;
          *(char *)((int)puVar11 + 6) = cVar1;
          uVar6 = DAT_00059f5c;
          puVar12 = puVar12 + iVar15 * 3;
          *(char *)((int)puVar12 + 6) = cVar2;
          *puVar12 = uVar6;
          *(ushort *)(puVar12 + 1) = uVar7;
          *(undefined1 *)((int)puVar12 + 7) = uVar4;
          puVar12[2] = param_2;
          goto LAB_00059dac;
        }
      }
    }
    else {
      uVar10 = DAT_00059f40 - ((int)puVar12 + iVar15 * 0xc + 2);
      if (((uVar10 + DAT_00059f44 <= DAT_00059f48) && ((uVar10 & 1) == 0)) &&
         ((uint)((int)puVar13 + (DAT_00059f44 - (int)(puVar12 + iVar15 * 3 + 1))) <= DAT_00059f48))
      {
        uVar8 = (((int)puVar13 - (int)puVar12) * 2 + (uint)(puVar12 <= puVar13)) * DAT_00059f60;
        *(short *)(puVar12 + iVar15 * 3) = (short)DAT_00059f4c;
        uVar7 = (ushort)DAT_00059f50;
        *(ushort *)((int)puVar14 + 2) = (ushort)((uVar10 - 4 & 0xfff) >> 1) | uVar7;
        *(ushort *)(puVar14 + 1) =
             uVar7 | (ushort)(((int)puVar13 + (-4 - (int)(puVar12 + iVar15 * 3 + 1)) & 0xfffU) >> 1)
        ;
        *(char *)((int)puVar14 + 6) = (char)(uVar8 >> 0x14);
        puVar14[2] = param_2;
        uVar6 = DAT_00059f5c;
        *(undefined1 *)((int)puVar14 + 7) = uVar4;
        *puVar13 = uVar6;
        uVar10 = (uint)puVar14 | 1;
        goto LAB_00059dac;
      }
    }
  }
  else {
    if (uVar10 != DAT_00059f3c) {
                    /* WARNING: Subroutine does not return */
      FUN_0005d354(DAT_00059f6c,0x183,DAT_00059f74,DAT_00059f78);
    }
    uVar10 = DAT_00059f40 - ((int)puVar12 + iVar15 * 0xc + 2);
    if ((uVar10 + DAT_00059f44 <= DAT_00059f48) && ((uVar10 & 1) == 0)) {
      *(short *)(puVar12 + iVar15 * 3) = (short)DAT_00059f4c;
      *(ushort *)((int)puVar14 + 2) = (ushort)((uVar10 - 4 & 0xfff) >> 1) | (ushort)DAT_00059f50;
      uVar6 = DAT_00059f54;
      *(undefined1 *)((int)puVar14 + 7) = uVar4;
      *(short *)(puVar14 + 1) = (short)uVar6;
      *(undefined1 *)((int)puVar14 + 6) = 0xff;
      puVar14[2] = param_2;
      uVar10 = (uint)puVar14 | 1;
LAB_00059dac:
      *(uint *)(*(int *)(DAT_00059f38 + 8) + iVar9) = uVar10;
      DataMemoryBarrier(0x1f);
      DataMemoryBarrier(0x1f);
      *DAT_00059f2c = 0;
      bVar3 = (bool)isCurrentModePrivileged();
      if (bVar3) {
        enableIRQinterrupts((uVar16 & 1) == 1);
      }
      return;
    }
  }
                    /* WARNING: Subroutine does not return */
  FUN_0005d354(DAT_00059f6c,0x10e,DAT_00059f68,DAT_00059f64);
}
```

## `FUN_00036738` @ `00036738` score `38`

- reasons: `byte deref` `offset +1` `small indexes` `channel nibble mask` `0xf0`

```c

void FUN_00036738(int param_1,uint param_2,uint param_3,int *param_4)

{
  int *piVar1;
  undefined4 uVar2;
  int *piVar3;
  uint uVar4;
  undefined4 *puVar5;
  uint uVar6;
  
  uVar2 = DAT_00036810;
  piVar3 = (int *)FUN_000467fc(DAT_00036810);
  do {
    do {
      piVar1 = piVar3;
      if ((piVar1 == (int *)0x0) || (param_4 == piVar1)) {
        return;
      }
      piVar3 = (int *)FUN_0004680c(uVar2,piVar1);
    } while (((*piVar1 != param_1) || ((piVar1[2] != param_2 && (param_2 != 0xf0000)))) ||
            ((*(byte *)(piVar1 + 1) != param_3 && (param_3 != 0xff))));
    uVar4 = (uint)*(ushort *)(param_1 + 0x2a);
    uVar6 = 0;
    if ((uVar4 & 0x3ff) >> 4 != 0) {
      do {
        while ((puVar5 = (undefined4 *)(*(int *)(param_1 + 0xc) + uVar6 * 8),
               (*(byte *)((int)puVar5 + 7) & 2) != 0 &&
               ((param_2 == 0xf0000 || (param_2 == (puVar5[1] & 0xffffff)))))) {
          FUN_0004758c(*puVar5,(char)piVar1[1]);
          uVar4 = (uint)*(ushort *)(param_1 + 0x2a);
          uVar6 = uVar6 + 1;
          if ((uVar4 & 0x3ff) >> 4 <= uVar6) goto LAB_000367ea;
        }
        uVar6 = uVar6 + 1;
      } while (uVar6 < (uVar4 & 0x3ff) >> 4);
    }
LAB_000367ea:
    FUN_00044de8(piVar1,0);
    FUN_000467a4(uVar2,piVar1);
    FUN_0004cedc(piVar1);
  } while( true );
}
```

## `FUN_0005ed60` @ `0005ed60` score `38`

- reasons: `offset +1` `offset +2` `small indexes` `7-bit mask` `127`

```c

undefined4
FUN_0005ed60(undefined4 *param_1,undefined4 param_2,uint param_3,ushort param_4,byte param_5)

{
  undefined4 uVar1;
  
  if (param_3 < 0x8001) {
    if (param_1[3] != 0) {
      FUN_0005ffe8(param_1[3],0xffffffff);
    }
    if (param_1[4] != 0) {
      FUN_0005ffe8(param_1[4],0xffffffff);
    }
    *(ushort *)((int)param_1 + 6) = (ushort)param_5 << 0xf | param_4 & 0x7fff;
    *(undefined2 *)((int)param_1 + 10) = 0;
    *param_1 = param_2;
    *(short *)(param_1 + 1) = (short)param_3;
    *(undefined2 *)(param_1 + 2) = 0;
    if (param_1[3] != 0) {
      FUN_0005ff98();
    }
    if (param_1[4] != 0) {
      FUN_0005ff98();
    }
    uVar1 = 1;
  }
  else {
    uVar1 = 0;
  }
  return uVar1;
}
```

## `FUN_00009944` @ `00009944` score `37`

- reasons: `u8 deref` `offset +2` `small indexes` `0x80` `record map shape`

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
/* ... truncated ... */
```

## `FUN_00025b84` @ `00025b84` score `36`

- reasons: `offset +2` `channel nibble mask` `7-bit mask` `127`

```c

undefined4 FUN_00025b84(short param_1)

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
  
  puVar16 = DAT_00025d34;
  pcVar2 = DAT_00025d14;
  if ((*DAT_00025d14 == '\x01') &&
     (uVar6 = *DAT_00025d34, *DAT_00025d34 = uVar6 + param_1, 1999 < (ushort)(uVar6 + param_1))) {
    *puVar16 = 0;
    *pcVar2 = '\0';
  }
  uVar6 = FUN_00026eb8();
  piVar5 = DAT_00025d2c;
  puVar16 = DAT_00025d28;
  iVar4 = DAT_00025d1c;
  puVar3 = DAT_00025d18;
  if ((short)uVar6 < 0) {
    if (*DAT_00025d28 != 0) {
      uVar13 = 0;
      pbVar15 = DAT_00025d20;
      puVar17 = DAT_00025d24;
      do {
        *puVar3 = 0;
        puVar10 = DAT_00025d30;
        uVar12 = *(ushort *)(uVar13 * 2 + *piVar5);
        uVar9 = uVar6 & 0x7fff ^ uVar12;
        uVar7 = uVar9 & 0x3800;
        if ((uVar9 & 0x3800) == 0) {
          if ((uVar12 & ~(uVar6 & 0x7fff | 0x3800)) == 0) {
            if ((*pbVar15 == 0) && (uVar12 = *DAT_00025d30, uVar12 < 2)) {
              *pbVar15 = 2;
              *puVar3 = 1;
              *puVar17 = uVar7;
              uVar12 = uVar12 + 1;
              uVar7 = 2;
              goto LAB_00025cce;
            }
          }
          else if (*pbVar15 != 0) {
            *puVar3 = 1;
            puVar10 = DAT_00025d30;
            *pbVar15 = 0;
            uVar12 = *puVar10 - 1;
LAB_00025cce:
            *puVar10 = uVar12;
            iVar4 = DAT_00025d1c;
            *(ushort *)(DAT_00025d1c + 4) = uVar7;
            *(short *)(iVar4 + 2) = (short)uVar13;
            FUN_00021264(2,0);
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
    pbVar15 = DAT_00025d20;
    puVar16 = DAT_00025d24;
    do {
      while( true ) {
        *puVar3 = 0;
        uVar13 = (uint)*pbVar15;
        if (uVar13 != 2) break;
        uVar6 = *puVar16 + param_1;
        cVar1 = *pcVar2;
        *puVar16 = uVar6;
        if (cVar1 == '\x01') {
          if (uVar6 < 0x7d1) goto LAB_00025bc6;
          uVar11 = 1;
          bVar8 = 1;
        }
        else {
          if (uVar6 < 0x3e9) goto LAB_00025bc6;
          bVar8 = 3;
          uVar11 = 3;
        }
LAB_00025bf4:
        *pbVar15 = bVar8;
        *puVar3 = 1;
        *(short *)(iVar4 + 2) = sVar14;
        sVar14 = sVar14 + 1;
        *puVar16 = 0;
        *(undefined2 *)(iVar4 + 4) = uVar11;
        pbVar15 = pbVar15 + 1;
        FUN_00021264(2,0);
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
        goto LAB_00025bf4;
      }
LAB_00025bc6:
      sVar14 = sVar14 + 1;
      pbVar15 = pbVar15 + 1;
      puVar16 = puVar16 + 1;
    } while (sVar14 != 200);
  }
  return 0;
}
```

## `FUN_00037674` @ `00037674` score `36`

- reasons: `byte deref` `offset +1` `offset +3` `small indexes` `channel nibble mask`

```c

void FUN_00037674(int *param_1,uint param_2)

{
  int iVar1;
  byte bVar2;
  uint uVar3;
  uint uVar4;
  undefined4 *puVar5;
  int iVar6;
  int iVar7;
  uint local_28;
  uint local_24 [2];
  
  iVar6 = *param_1;
  uVar4 = (*(ushort *)(iVar6 + 0x2a) & 0x3ff) >> 4;
  if (uVar4 != 0) {
    uVar3 = 0;
    puVar5 = *(undefined4 **)(iVar6 + 0xc);
    do {
      if (((*(byte *)((int)puVar5 + 7) & 2) != 0) && (param_1[2] == (puVar5[1] & 0xffffff))) {
        iVar7 = uVar3 * 8;
        bVar2 = *(byte *)(param_1 + 1);
        if (bVar2 < 0x79) {
          if (0x57 < bVar2) {
            if ((byte)(bVar2 + 0xa8) < 0x21) {
                    /* WARNING: Could not recover jumptable at 0x000376ca. Too many branches */
                    /* WARNING: Treating indirect jump as call */
              (**(code **)(DAT_0003780c + (uint)(byte)(bVar2 + 0xa8) * 4))();
              return;
            }
            goto LAB_00037752;
          }
          if (0x45 < bVar2) goto LAB_00037752;
          if (bVar2 < 0x31) {
            if ((bVar2 != 0x1c) && (bVar2 != 0x23)) goto LAB_00037752;
LAB_0003776e:
            if ((int)param_2 < 1) {
              local_28 = (uint)*(uint3 *)(param_1 + 3);
            }
            else if ((int)param_2 < 0xff) {
              local_28 = FUN_00045da4(param_1[4],param_1[3],param_2 & 0xff);
              local_28 = local_28 & 0xffffff;
              bVar2 = *(byte *)(param_1 + 1);
              puVar5 = (undefined4 *)(*(int *)(iVar6 + 0xc) + iVar7);
            }
            else {
              local_28 = (uint)*(uint3 *)(param_1 + 4);
            }
            goto LAB_00037706;
          }
          uVar4 = 1 << (uint)(byte)(bVar2 - 0x31);
          if ((uVar4 & DAT_00037810) != 0) goto LAB_0003776e;
          if ((uVar4 & 0x18) == 0) goto LAB_00037752;
          if ((int)param_2 < 0xff) goto LAB_00037702;
        }
        else {
LAB_00037752:
          if (param_2 == 0) {
LAB_00037702:
            local_28 = param_1[3];
            goto LAB_00037706;
          }
          if (param_2 != 0xff) {
            local_28 = ((int)(param_2 * (param_1[4] - param_1[3])) >> 8) + param_1[3];
            goto LAB_00037706;
          }
        }
        local_28 = param_1[4];
LAB_00037706:
        local_24[0] = 0;
        iVar1 = FUN_00047730(*puVar5,bVar2,local_24);
        if (((iVar1 == 0) || (local_28 != local_24[0])) ||
           (iVar1 = FUN_00045c54(local_28,local_28), uVar4 = local_24[0], iVar1 == 0)) {
          FUN_0004763c(*(undefined4 *)(*(int *)(iVar6 + 0xc) + iVar7),(char)param_1[1],local_28);
        }
        else {
          FUN_0004763c(*(undefined4 *)(*(int *)(iVar6 + 0xc) + iVar7),(char)param_1[1],local_28);
          if (local_28 == uVar4) {
            return;
          }
        }
        if (*param_1 != 0) {
          if (*(char *)(DAT_00037814 + 0x24) == '\0') {
            return;
          }
          FUN_00036f68(*param_1,param_1[2],(char)param_1[1]);
          return;
        }
        FUN_000468e8(3,DAT_00037824,0x115,DAT_0003781c,DAT_00037828,DAT_00037820,DAT_00037818);
        do {
                    /* WARNING: Do nothing block with infinite loop */
        } while( true );
      }
      uVar3 = uVar3 + 1;
      puVar5 = puVar5 + 2;
    } while (uVar3 < uVar4);
  }
  return;
}
```

## `FUN_000445e4` @ `000445e4` score `36`

- reasons: `byte deref` `offset +1` `offset +2` `small indexes` `channel nibble mask`

```c

undefined4 FUN_000445e4(undefined4 *param_1,int *param_2,undefined4 param_3,uint param_4)

{
  short sVar1;
  int iVar2;
  undefined4 uVar3;
  undefined4 *puVar4;
  undefined4 *puVar5;
  undefined4 *puVar6;
  
  if (param_1 == (undefined4 *)0x0) {
    FUN_000468e8(3,DAT_000446f4,0x62,DAT_000446ec,DAT_000446f0,DAT_000446f8,DAT_000446e4);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  if (param_2 == (int *)0x0) {
    FUN_000468e8(3,DAT_000446f4,99,DAT_000446ec,DAT_000446f0,DAT_000446e8,DAT_000446e4);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  FUN_00050350(param_2,0,0x20);
  puVar4 = param_1;
  puVar6 = (undefined4 *)0x0;
  do {
    iVar2 = (*(code *)*puVar4)(puVar4,param_2,param_3,
                               -(uint)((*(byte *)(puVar4 + 5) & 4) == 0) & param_4);
    if (iVar2 == 0) {
LAB_00044618:
      puVar4 = (undefined4 *)puVar4[7];
      puVar5 = puVar6;
    }
    else {
      puVar5 = puVar4;
      if ((*(byte *)((int)param_2 + 0x11) & 1) == 0) goto LAB_00044674;
      if (puVar6 != (undefined4 *)0x0) goto LAB_00044618;
      puVar4 = (undefined4 *)puVar4[7];
    }
    puVar6 = puVar5;
  } while (puVar4 != (undefined4 *)0x0);
  if (puVar5 == (undefined4 *)0x0) {
    iVar2 = param_1[3];
    uVar3 = 0;
    sVar1 = (short)(iVar2 / 2);
    *(short *)((int)param_2 + 6) = sVar1;
    *(short *)(param_2 + 1) = sVar1 + 2;
    *(short *)(param_2 + 2) = (short)iVar2;
    *param_2 = 0;
    *(undefined2 *)((int)param_2 + 10) = 0;
    param_2[3] = 0;
    *(ushort *)(param_2 + 4) = *(ushort *)(param_2 + 4) & 0xfe00 | 0x101;
  }
  else {
    (*(code *)*puVar5)(puVar5,param_2,param_3,param_4 & -(uint)((*(byte *)(puVar5 + 5) & 4) == 0));
LAB_00044674:
    uVar3 = 1;
    *param_2 = (int)puVar5;
  }
  return uVar3;
}
```

## `FUN_0004763c` @ `0004763c` score `36`

- reasons: `byte deref` `offset +1` `offset +2` `small indexes` `channel nibble mask`

```c

void FUN_0004763c(int *param_1,uint param_2,undefined4 param_3)

{
  uint uVar1;
  int iVar2;
  char cVar3;
  int iVar4;
  uint uVar5;
  
  uVar1 = (uint)*(byte *)(param_1 + 2);
  if (uVar1 == 0xff) {
    FUN_000468e8(3,DAT_00047728,0x14c,DAT_00047724,DAT_0004772c);
  }
  else {
    if (param_2 == 0) {
      FUN_000468e8(3,DAT_00047728,0x150,DAT_00047724,DAT_00047720,DAT_0004771c);
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    iVar4 = *param_1;
    if ((iVar4 != 0) && (uVar1 != 0)) {
      uVar5 = uVar1;
      do {
        uVar5 = uVar5 - 1;
        if (*(byte *)(uVar1 * 4 + iVar4 + uVar5) == param_2) {
          *(undefined4 *)(uVar5 * 4 + iVar4) = param_3;
          return;
        }
      } while (uVar5 != 0);
    }
    iVar4 = FUN_0004cef4(iVar4,(uVar1 + 1) * 5);
    if (iVar4 != 0) {
      uVar1 = (uint)*(byte *)(param_1 + 2);
      *param_1 = iVar4;
      cVar3 = '\0';
      if (uVar1 != 0) {
        iVar2 = uVar1 * 4 + iVar4;
        FUN_0005fa24(iVar2 + ((uVar1 - 1) - uVar1) + 5,iVar2 + ((uVar1 - 1) - uVar1) + 1);
        cVar3 = (char)param_1[2];
      }
      *(byte *)(param_1 + 2) = cVar3 + 1U;
      *(char *)(iVar4 + (uint)(byte)(cVar3 + 1U) * 5 + -1) = (char)param_2;
      *(undefined4 *)(iVar4 + ((uint)*(byte *)(param_1 + 2) + DAT_00047718) * 4) = param_3;
      if (param_2 >> 2 < 0x20) {
        param_1[1] = param_1[1] | 1 << (param_2 >> 2 & 0xff);
      }
      else {
        param_1[1] = param_1[1] | 0x80000000;
      }
    }
  }
  return;
}
```

## `FUN_0005567c` @ `0005567c` score `36`

- reasons: `offset +2` `small indexes` `channel nibble mask` `0x90`

```c

undefined4 FUN_0005567c(undefined4 param_1,int param_2,char *param_3)

{
  char cVar1;
  undefined4 uVar2;
  int iVar3;
  undefined4 uVar4;
  int local_14;
  
  uVar4 = *(undefined4 *)(param_2 + 0xc);
  cVar1 = *(char *)(param_2 + 0x10);
  if (cVar1 == '\0') {
    FUN_00050328(param_3,uVar4,0xc);
    cVar1 = param_3[1];
  }
  else {
    if (cVar1 != '\x01') {
      if (cVar1 != '\x02') {
        FUN_000468e8(2,DAT_00055768,0xa2,DAT_00055764,DAT_0005576c);
        return 0;
      }
      *(undefined4 *)(param_3 + 4) = DAT_0005575c;
      param_3[1] = '\x0e';
      goto LAB_0005569e;
    }
    uVar2 = FUN_00046638(uVar4);
    iVar3 = FUN_00050484(uVar2,DAT_00055770);
    if (iVar3 != 0) {
      return 0;
    }
    iVar3 = FUN_000463c0(param_2 + 0x14,param_3,0xc,&local_14);
    if ((iVar3 != 0) || (local_14 != 0xc)) {
      FUN_000468e8(2,DAT_00055768,0x86,DAT_00055764,DAT_00055774,iVar3,local_14,0xc);
      return 0;
    }
    if (*param_3 == '\x19') {
      cVar1 = param_3[1];
    }
    else {
      FUN_000468e8(2,DAT_00055768,0x90,DAT_00055764,DAT_00055778,uVar4);
      cVar1 = *param_3;
      *param_3 = '\x19';
      param_3[1] = cVar1;
    }
    *(ushort *)(param_3 + 2) = *(ushort *)(param_3 + 2) | 0x20;
  }
  if (cVar1 == '\0') {
    FUN_000468e8(2,DAT_00055768,0xa7,DAT_00055764,DAT_00055760);
    return 0;
  }
LAB_0005569e:
  if (*param_3 != '\x19') {
    *(ushort *)(param_3 + 2) = *(ushort *)(param_3 + 2) & 0xfffe;
  }
  return 1;
}
```

## `FUN_0005c310` @ `0005c310` score `36`

- reasons: `offset +1` `channel nibble mask` `7-bit mask` `127`

```c

int FUN_0005c310(code *param_1,undefined4 param_2,int param_3,undefined4 param_4,int param_5,
                uint param_6,int param_7,uint param_8,uint param_9)

{
  int iVar1;
  int iVar2;
  undefined4 uVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  undefined4 uVar6;
  uint uVar7;
  undefined8 uVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  longlong lVar11;
  undefined8 uVar12;
  undefined4 local_58;
  uint local_54;
  uint local_50;
  undefined4 local_4c;
  uint local_44;
  uint local_40;
  uint local_38;
  
  iVar1 = FUN_0005b9f2(param_5,param_6,param_5,param_6);
  local_54 = param_6;
  if (((iVar1 != 0) || (iVar1 = FUN_0005b9e8(param_5,param_6,0xffffffff,DAT_0005c6a0), iVar1 != 0))
     || (iVar1 = FUN_0005b9bc(param_5,param_6,0xffffffff,DAT_0005c6a4), iVar1 != 0))
  goto LAB_0005c3e2;
  iVar1 = FUN_0005b9bc(param_5,param_6,0,0);
  if (iVar1 == 0) {
  }
  else {
    local_54 = param_6 + 0x80000000;
  }
  uVar12 = CONCAT44(local_54,param_5);
  local_44 = param_9 & 0x800;
  if ((param_9 & 0x400) == 0) {
    if (local_54 != 0 || param_5 != 0) {
      param_7 = 6;
LAB_0005c450:
      uVar8 = FUN_0005ba14(((local_54 & 0x7fffffff) >> 0x14) + DAT_0005c6ac);
      uVar8 = FUN_0005b93e((int)uVar8,(int)((ulonglong)uVar8 >> 0x20),DAT_0005c6b0,DAT_0005c6b4);
      uVar8 = FUN_0005b900((int)uVar8,(int)((ulonglong)uVar8 >> 0x20),DAT_0005c6b8,DAT_0005c6bc);
      uVar9 = FUN_0005b8f6(param_5,DAT_0005c6c0 | local_54 & 0xfffff,0,DAT_0005c6c4);
      uVar9 = FUN_0005b93e((int)uVar9,(int)((ulonglong)uVar9 >> 0x20),DAT_0005c6c8,DAT_0005c6cc);
      FUN_0005b900((int)uVar8,(int)((ulonglong)uVar8 >> 0x20),(int)uVar9,
                   (int)((ulonglong)uVar9 >> 0x20));
      local_38 = FUN_0005ba44();
      uVar8 = FUN_0005ba14();
      uVar4 = (undefined4)((ulonglong)uVar8 >> 0x20);
      uVar9 = FUN_0005b93e((int)uVar8,uVar4,DAT_0005c6d0,DAT_0005c6d4);
      FUN_0005b900((int)uVar9,(int)((ulonglong)uVar9 >> 0x20),0,DAT_0005c6d8);
      iVar1 = FUN_0005ba44();
      uVar8 = FUN_0005b93e((int)uVar8,uVar4,DAT_0005c6dc,DAT_0005c6e0);
      uVar9 = FUN_0005ba14(iVar1);
      uVar9 = FUN_0005b93e((int)uVar9,(int)((ulonglong)uVar9 >> 0x20),DAT_0005c6e4,DAT_0005c6e8);
      uVar8 = FUN_0005b8f6((int)uVar8,(int)((ulonglong)uVar8 >> 0x20),(int)uVar9,
                           (int)((ulonglong)uVar9 >> 0x20));
      uVar5 = (undefined4)((ulonglong)uVar8 >> 0x20);
      uVar4 = (undefined4)uVar8;
      uVar8 = FUN_0005b93e(uVar4,uVar5,uVar4,uVar5);
      uVar6 = (undefined4)((ulonglong)uVar8 >> 0x20);
      uVar3 = (undefined4)uVar8;
      uVar8 = FUN_0005b900(uVar4,uVar5,uVar4,uVar5);
      uVar9 = FUN_0005b90a(uVar3,uVar6,0,DAT_0005c6ec);
      uVar9 = FUN_0005b900((int)uVar9,(int)((ulonglong)uVar9 >> 0x20),0,DAT_0005c6f0);
      uVar9 = FUN_0005b90a(uVar3,uVar6,(int)uVar9,(int)((ulonglong)uVar9 >> 0x20));
      uVar9 = FUN_0005b900((int)uVar9,(int)((ulonglong)uVar9 >> 0x20),0,DAT_0005c6f4);
      uVar9 = FUN_0005b90a(uVar3,uVar6,(int)uVar9,(int)((ulonglong)uVar9 >> 0x20));
      uVar10 = FUN_0005b8f6(0,0x40000000,uVar4,uVar5);
      uVar9 = FUN_0005b900((int)uVar9,(int)((ulonglong)uVar9 >> 0x20),(int)uVar10,
                           (int)((ulonglong)uVar10 >> 0x20));
      uVar8 = FUN_0005b90a((int)uVar8,(int)((ulonglong)uVar8 >> 0x20),(int)uVar9,
                           (int)((ulonglong)uVar9 >> 0x20));
      uVar8 = FUN_0005b900((int)uVar8,(int)((ulonglong)uVar8 >> 0x20),0,DAT_0005c6c0);
      lVar11 = FUN_0005b93e((int)uVar8,(int)((ulonglong)uVar8 >> 0x20),0,
                            (iVar1 + DAT_0005c6f8) * 0x100000);
      uVar4 = (undefined4)((ulonglong)lVar11 >> 0x20);
      iVar1 = FUN_0005b9e8((int)lVar11,uVar4,param_5,local_54);
      if (iVar1 != 0) {
        local_38 = local_38 - 1;
        lVar11 = FUN_0005b90a((int)lVar11,uVar4,0,DAT_0005c6f0);
      }
      local_4c = (undefined4)((ulonglong)lVar11 >> 0x20);
      local_50 = (uint)lVar11;
      uVar7 = local_50;
      if (local_38 + 99 < 199) {
        local_50 = param_9 & 2;
        if (local_44 != 0) {
          local_40 = 4;
          goto LAB_0005c772;
        }
        local_40 = 4;
        if (4 < param_8) {
          if (local_50 == 0) {
            local_44 = param_8 - 4;
            local_40 = 4;
          }
          else {
            local_40 = 4;
            local_50 = 2;
          }
        }
LAB_0005c5da:
        if (local_38 == 0) goto LAB_0005c5f0;
      }
      else {
        local_50 = param_9 & 2;
        if (local_44 != 0) {
          local_40 = 5;
LAB_0005c772:
          local_50 = param_9 & 2;
          if ((lVar11 == 0) ||
             ((iVar1 = FUN_0005b9d8(param_5,local_54,DAT_0005c830,DAT_0005c834), iVar1 != 0 &&
              (iVar1 = FUN_0005b9bc(param_5,local_54,0,DAT_0005c838), iVar1 != 0))))
          goto LAB_0005c410;
          if ((param_7 == 0) || ((param_9 & 0x400) == 0)) {
            local_44 = 0;
            if (local_40 < param_8) {
              if (local_50 == 0) goto LAB_0005c804;
              local_44 = 0;
              local_50 = 2;
            }
          }
          else {
            param_7 = param_7 + -1;
            local_44 = 0;
            if (local_40 < param_8) {
              if (local_50 == 0) {
LAB_0005c804:
                local_44 = param_8 - local_40;
              }
              else {
                local_50 = 2;
                local_44 = 0;
              }
            }
          }
          goto LAB_0005c5da;
        }
        local_40 = 5;
        if (5 < param_8) {
          if (local_50 == 0) {
            local_44 = param_8 - 5;
            local_40 = 5;
          }
          else {
            local_50 = 2;
            local_40 = 5;
          }
        }
      }
      uVar12 = FUN_0005b90a(param_5,local_54,uVar7,local_4c);
LAB_0005c5f0:
      local_54 = (uint)((ulonglong)uVar12 >> 0x20);
      local_58 = (undefined4)uVar12;
      iVar1 = FUN_0005b9bc(param_5,param_6,0,0);
      if (iVar1 != 0) {
        local_54 = local_54 + -0x80000000;
      }
      iVar1 = FUN_0005c83c(param_1,param_2,param_3,param_4,local_58,local_54,param_7,local_44,
                           DAT_0005c6a8 & param_9);
      (*param_1)((-((param_9 & 0x20) == 0) & 0x20U) + 0x45,param_2,iVar1,param_4);
      iVar1 = FUN_0005c19c(param_1,param_2,iVar1 + 1,param_4,
                           local_38 + ((int)local_38 >> 0x1f) ^ (int)local_38 >> 0x1f,
                           local_38 >> 0x1f,10,0,local_40 - 1,5);
      if (local_50 == 0) {
        return iVar1;
      }
      for (uVar7 = iVar1 - param_3; uVar7 < param_8; uVar7 = uVar7 + 1) {
        (*param_1)(0x20,param_2,iVar1,param_4);
        iVar1 = iVar1 + 1;
      }
      return iVar1;
    }
    if (local_44 == 0) {
      param_7 = 6;
LAB_0005c3ac:
/* ... truncated ... */
```

## `FUN_0005ec60` @ `0005ec60` score `36`

- reasons: `offset +1` `channel nibble mask` `7-bit mask` `127`

```c

undefined4 FUN_0005ec60(int *param_1,undefined4 param_2,uint param_3,uint param_4)

{
  uint uVar1;
  undefined4 uVar2;
  uint uVar3;
  
  uVar3 = (uint)*(ushort *)(param_1 + 1);
  uVar1 = param_3 - param_4 & 0xffff;
  if (param_3 < param_4) {
    uVar1 = uVar1 + uVar3 * 2 & 0xffff;
  }
  uVar2 = 0;
  if (uVar1 != 0) {
    if (uVar3 < uVar1) {
      if (param_3 < uVar3) {
        param_3 = uVar3 + param_3;
        *(short *)((int)param_1 + 10) = (short)param_3;
      }
      else {
        param_3 = param_3 - uVar3;
        *(short *)((int)param_1 + 10) = (short)param_3;
      }
      param_4 = param_3 & 0xffff;
    }
    for (; uVar3 <= param_4; param_4 = param_4 - uVar3 & 0xffff) {
    }
    FUN_0005bef8(param_2,*param_1 + (*(ushort *)((int)param_1 + 6) & 0x7fff) * param_4);
    uVar2 = 1;
  }
  return uVar2;
}
```

## `FUN_0005ecb4` @ `0005ecb4` score `36`

- reasons: `offset +1` `channel nibble mask` `7-bit mask` `127`

```c

uint FUN_0005ecb4(int *param_1,int param_2,uint param_3,uint param_4,ushort param_5)

{
  int iVar1;
  ushort uVar2;
  uint uVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  uint uVar7;
  
  uVar4 = (uint)param_5;
  uVar7 = (uint)*(ushort *)(param_1 + 1);
  uVar5 = param_4 - uVar4 & 0xffff;
  if (param_4 < uVar4) {
    uVar5 = uVar5 + uVar7 * 2 & 0xffff;
  }
  uVar6 = 0;
  if (uVar5 != 0) {
    if (uVar7 < uVar5) {
      uVar5 = uVar7;
      if (uVar7 <= param_4) {
        uVar5 = -uVar7;
      }
      uVar4 = uVar5 + param_4 & 0xffff;
      *(short *)((int)param_1 + 10) = (short)(uVar5 + param_4);
      uVar5 = uVar7;
    }
    uVar2 = (ushort)uVar5;
    if (param_3 < uVar5) {
      uVar2 = (ushort)param_3;
    }
    uVar6 = (uint)uVar2;
    for (; uVar7 <= uVar4; uVar4 = uVar4 - uVar7 & 0xffff) {
    }
    uVar5 = *(ushort *)((int)param_1 + 6) & 0x7fff;
    uVar3 = uVar7 - uVar4 & 0xffff;
    iVar1 = *param_1 + uVar4 * uVar5;
    if (uVar3 < uVar6) {
      uVar3 = uVar5 * uVar3 & 0xffff;
      FUN_0005bef8(param_2,iVar1,uVar3);
      FUN_0005bef8(param_2 + uVar3,*param_1,uVar5 * (uVar4 + (uVar6 - uVar7)) & 0xffff);
    }
    else {
      FUN_0005bef8(param_2,iVar1,uVar6 * uVar5);
    }
  }
  return uVar6;
}
```

## `FUN_0000408c` @ `0000408c` score `34`

- reasons: `small indexes` `7-bit mask` `127` `record map shape`

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

## `FUN_00021f24` @ `00021f24` score `34`

- reasons: `channel nibble mask` `0x80` `0x90`

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
    }
    iVar8 = *(int *)(iVar6 + 0x100);
    uVar4 = FUN_0002ec74(0x13);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0x70);
    uVar4 = FUN_0002ecb8(cVar1,0);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0x80);
    uVar4 = FUN_0002ecb8(cVar1,1);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0x90);
    uVar4 = FUN_0002ecb8(cVar1,2);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0xa0);
    uVar4 = FUN_0002ecb8(cVar1,3);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0xb8);
    uVar4 = FUN_0002ecb8(cVar1,4);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 200);
    uVar4 = FUN_0002ecb8(cVar1,5);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0xd8);
    uVar4 = FUN_0002ecb8(cVar1,6);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0xe8);
    uVar4 = FUN_0002ecb8(cVar1,7);
    if (iVar8 != 0) {
      FUN_0004a750(iVar8,uVar4);
    }
    iVar8 = *(int *)(iVar6 + 0x6c);
    uVar5 = FUN_0002ece0(cVar1,0,0);
    if (iVar8 != 0) {
      uVar3 = FUN_00045c78(*(undefined4 *)(DAT_000222a8 + (uVar5 & 0xff) * 8 + 4));
      FUN_00037ec8(iVar8,uVar3,0x20000);
    }
    iVar8 = *(int *)(iVar6 + 0x7c);
    uVar5 = FUN_0002ece0(cVar1,1,0);
    if (iVar8 != 0) {
      uVar3 = FUN_00045c78(*(undefined4 *)(DAT_000222a8 + (uVar5 & 0xff) * 8 + 4));
      FUN_00037ec8(iVar8,uVar3,0x20000);
    }
    iVar8 = *(int *)(iVar6 + 0x8c);
    uVar5 = FUN_0002ece0(cVar1,2,0);
    if (iVar8 != 0) {
      uVar3 = FUN_00045c78(*(undefined4 *)(DAT_000222a8 + (uVar5 & 0xff) * 8 + 4));
      FUN_00037ec8(iVar8,uVar3,0x20000);
    }
    iVar8 = *(int *)(iVar6 + 0x9c);
    uVar5 = FUN_0002ece0(cVar1,3,0);
    if (iVar8 != 0) {
      uVar3 = FUN_00045c78(*(undefined4 *)(DAT_000222a8 + (uVar5 & 0xff) * 8 + 4));
      FUN_00037ec8(iVar8,uVar3,0x20000);
    }
    iVar8 = *(int *)(iVar6 + 0xb4);
    uVar5 = FUN_0002ece0(cVar1,4,0);
    if (iVar8 != 0) {
      uVar3 = FUN_00045c78(*(undefined4 *)(DAT_000222a8 + (uVar5 & 0xff) * 8 + 4));
      FUN_00037ec8(iVar8,uVar3,0x20000);
    }
    iVar8 = *(int *)(iVar6 + 0xc4);
    uVar5 = FUN_0002ece0(cVar1,5,0);
    if (iVar8 != 0) {
      uVar3 = FUN_00045c78(*(undefined4 *)(DAT_000222a8 + (uVar5 & 0xff) * 8 + 4));
      FUN_00037ec8(iVar8,uVar3,0x20000);
    }
    iVar8 = *(int *)(iVar6 + 0xd4);
    uVar5 = FUN_0002ece0(cVar1,6,0);
    if (iVar8 != 0) {
      uVar3 = FUN_00045c78(*(undefined4 *)(DAT_000222a8 + (uVar5 & 0xff) * 8 + 4));
      FUN_00037ec8(iVar8,uVar3,0x20000);
    }
    iVar8 = *(int *)(iVar6 + 0xe4);
    uVar5 = FUN_0002ece0(cVar1,7,0);
    if (iVar8 != 0) {
      uVar3 = FUN_00045c78(*(undefined4 *)(DAT_000222a8 + (uVar5 & 0xff) * 8 + 4));
      FUN_00037ec8(iVar8,uVar3,0x20000);
    }
    uVar4 = *(undefined4 *)(iVar6 + 0x6c);
    uVar2 = FUN_0002ece0(cVar1,0,8);
    FUN_0004b63c(uVar4,uVar2);
    uVar4 = *(undefined4 *)(iVar6 + 0x7c);
    uVar2 = FUN_0002ece0(cVar1,1,8);
    FUN_0004b63c(uVar4,uVar2);
/* ... truncated ... */
```

## `FUN_00040874` @ `00040874` score `34`

- reasons: `u8* param` `u8 deref` `offset +1` `small indexes` `channel nibble mask`

```c

int * FUN_00040874(undefined1 *param_1,uint param_2,uint param_3)

{
  undefined1 uVar1;
  undefined1 uVar2;
  int *piVar3;
  int *piVar4;
  byte bVar5;
  int *piVar6;
  undefined1 *puVar7;
  uint uVar8;
  int iVar9;
  
  if ((param_1[0xb] & 0xf) == 0) {
    return (int *)0x0;
  }
  bVar5 = param_1[0xb] & 0xf;
  if ((bVar5 == 1) || (param_3 = param_2, (bVar5 + 0xe & 0xf) < 4)) {
    uVar8 = (param_3 + 1) * 3 & 0xfffffffc;
    piVar3 = (int *)FUN_0004cea4((param_3 + 3 & 0xfffffffc) + 0xc + uVar8);
    if (piVar3 != (int *)0x0) {
      piVar6 = piVar3 + 3;
      piVar4 = (int *)((int)piVar3 + uVar8 + 0xc);
      *piVar3 = (int)piVar6;
      piVar3[1] = (int)piVar4;
      piVar3[2] = param_3;
      if (param_3 == 0) {
        return piVar3;
      }
      goto LAB_000408c0;
    }
  }
  else {
    piVar3 = (int *)FUN_0004cea4(0x10c);
    if (piVar3 != (int *)0x0) {
      piVar6 = piVar3 + 3;
      piVar4 = piVar3 + 0x33;
      param_3 = 0x40;
      *piVar3 = (int)piVar6;
      piVar3[1] = (int)piVar4;
      piVar3[2] = 0x40;
LAB_000408c0:
      iVar9 = 0;
      do {
        puVar7 = (undefined1 *)((int)piVar6 + iVar9 * 3);
        if ((int)(param_3 * (byte)param_1[4]) >> 8 < iVar9) {
          FUN_0004077c(param_1,param_3,iVar9,puVar7,(undefined1 *)((int)piVar4 + iVar9));
          param_3 = piVar3[2];
          if (param_3 <= iVar9 + 1U) {
            return piVar3;
          }
        }
        else {
          uVar1 = param_1[1];
          uVar2 = param_1[2];
          *puVar7 = *param_1;
          puVar7[1] = uVar1;
          puVar7[2] = uVar2;
          *(undefined1 *)((int)piVar4 + iVar9) = param_1[3];
          param_3 = piVar3[2];
          if (param_3 <= iVar9 + 1U) {
            return piVar3;
          }
        }
        iVar9 = iVar9 + 1;
        piVar6 = (int *)*piVar3;
        piVar4 = (int *)piVar3[1];
      } while( true );
    }
  }
  FUN_000468e8(3,DAT_00040960,0x70,DAT_00040958,DAT_0004095c,DAT_00040954,DAT_00040950);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

## `FUN_0003c098` @ `0003c098` score `33`

- reasons: `byte deref` `u8 deref` `offset +1` `small indexes` `channel nibble mask`

```c

void FUN_0003c098(int param_1,undefined4 *param_2,int param_3,undefined4 *param_4)

{
  char cVar1;
  ushort uVar2;
  ushort uVar3;
  uint uVar4;
  uint uVar5;
  int iVar6;
  int iVar7;
  int iVar8;
  undefined4 uVar9;
  int iVar10;
  int iVar11;
  
  cVar1 = *(char *)(param_1 + 1);
  if (cVar1 != *(char *)(param_3 + 1)) {
    FUN_000468e8(3,DAT_0003c1d0,0xde,DAT_0003c1c8,DAT_0003c1dc,DAT_0003c1d8,cVar1,
                 *(char *)(param_3 + 1));
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  if (param_2 == (undefined4 *)0x0) {
    uVar4 = (uint)*(ushort *)(param_1 + 4);
    uVar5 = (uint)(byte)(cVar1 - 7);
    if (uVar5 < 4) {
LAB_0003c0f6:
      if (uVar5 == 3) {
        uVar9 = 0x400;
      }
      else {
        uVar9 = *(undefined4 *)(uVar5 * 4 + DAT_0003c1d4);
      }
      FUN_00050328(*(undefined4 *)(param_1 + 0x10),*(undefined4 *)(param_3 + 0x10),uVar9);
    }
    if (param_4 == (undefined4 *)0x0) {
LAB_0003c10c:
      if (*(ushort *)(param_3 + 4) == uVar4) {
        iVar6 = FUN_0003bf18(param_3,0,0);
        goto LAB_0003c150;
      }
      goto LAB_0003c0d0;
    }
  }
  else {
    uVar4 = FUN_000458e4(param_2);
    if (param_4 == (undefined4 *)0x0) {
      uVar5 = *(byte *)(param_1 + 1) - 7 & 0xff;
      if (uVar5 < 4) goto LAB_0003c0f6;
      goto LAB_0003c10c;
    }
  }
  uVar5 = FUN_000458e4(param_4);
  if (uVar5 == uVar4) {
    iVar6 = FUN_0003bf18(param_3,*param_4,param_4[1]);
LAB_0003c150:
    if (param_2 == (undefined4 *)0x0) {
      iVar7 = FUN_0003bf18(param_1,0,0);
      iVar11 = 0;
      iVar10 = *(ushort *)(param_1 + 6) - 1;
    }
    else {
      iVar7 = FUN_0003bf18(param_1,*param_2,param_2[1]);
      iVar11 = param_2[1];
      iVar10 = param_2[3];
    }
    uVar2 = *(ushort *)(param_1 + 8);
    uVar3 = *(ushort *)(param_3 + 8);
    iVar8 = FUN_00045bcc(*(undefined1 *)(param_1 + 1));
    if (iVar11 <= iVar10) {
      do {
        FUN_00050328(iVar7,iVar6,(int)(iVar8 * uVar4 + 7) >> 3);
        iVar7 = iVar7 + (uint)uVar2;
        iVar6 = iVar6 + (uint)uVar3;
        iVar11 = iVar11 + 1;
      } while (iVar11 <= iVar10);
    }
    return;
  }
LAB_0003c0d0:
  FUN_000468e8(3,DAT_0003c1d0,0xee,DAT_0003c1c8,DAT_0003c1cc,DAT_0003c1c4,DAT_0003c1c0);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

## `FUN_0003eab0` @ `0003eab0` score `33`

- reasons: `byte deref` `u8 deref` `offset +1` `small indexes` `channel nibble mask`

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
  local_d8 = iVar12 + param_3[1];
  iVar12 = iVar2;
  if (-1 < (int)(uVar9 << 0x1f)) {
    iVar12 = -(iVar3 + iVar2);
  }
  local_d0 = param_3[3] - iVar12;
  uVar9 = iVar3 - iVar2 & ~(iVar3 - iVar2) >> 0x1f;
  local_40 = CONCAT13(*(undefined1 *)(param_2 + 0x22),
                      CONCAT12(*(undefined1 *)(param_2 + 0x21),
                               CONCAT11(*(undefined1 *)(param_2 + 0x20),
                                        *(undefined1 *)(param_2 + 0x28))));
  if (uVar9 == 0 && iVar3 == 0) {
    FUN_00050350(local_54,0,0x2c);
    uVar1 = local_d0;
    uVar8 = local_d4;
    uVar9 = local_dc;
    uVar4 = *param_3;
    uVar13 = param_3[2];
    uVar7 = param_3[1];
    uVar10 = param_3[3];
    local_54[0] = &local_78;
    local_6c = local_d8 - 1;
    local_78 = uVar4;
    local_70 = uVar13;
    if ((int)local_d8 < (int)uVar7) {
      local_74 = local_d0 + 1;
      local_6c = uVar10;
      if ((int)uVar10 < (int)local_d0) {
        local_70 = local_dc - 1;
        local_74 = uVar7;
        goto LAB_0003ebc8;
      }
      FUN_0004dc20(param_1,local_54);
      local_78 = *param_3;
      local_74 = param_3[1];
    }
    else {
      local_74 = uVar7;
      FUN_0004dc20(param_1,local_54);
      local_74 = local_d0 + 1;
      local_6c = param_3[3];
      if ((int)uVar10 < (int)uVar1) {
        local_70 = local_dc - 1;
        local_78 = *param_3;
        local_74 = local_d8;
        goto LAB_0003ebc8;
      }
      FUN_0004dc20(param_1,local_54);
      local_78 = *param_3;
      local_74 = local_d8;
    }
    local_70 = local_dc - 1;
    local_6c = local_d0;
    if ((int)uVar10 < (int)uVar1) {
      local_6c = param_3[3];
    }
LAB_0003ebc8:
    if ((int)uVar4 <= (int)uVar9) {
      FUN_0004dc20(param_1,local_54);
    }
    local_78 = local_d4 + 1;
    local_70 = param_3[2];
    if ((int)uVar13 < (int)uVar8) {
      return;
    }
    FUN_0004dc20(param_1,local_54);
    return;
  }
  local_110 = FUN_000450d4(&local_cc,param_3,param_1 + 0x38);
  if (local_110 == 0) {
    return;
  }
  uVar5 = FUN_000458e4(&local_cc);
  FUN_00050350(local_54,0,0x2c);
  uVar6 = FUN_0004cea4(uVar5);
  local_3c = uVar6;
  FUN_0005beec(&local_e8,0,0xc);
  FUN_00043030(auStack_9c,&local_dc,uVar9,1);
  local_e8 = auStack_9c;
  if (0 < iVar3) {
    FUN_00043030(&local_78,param_3,iVar3,0);
    local_e4 = &local_78;
  }
  local_ac = iVar3 + *param_3;
  if ((int)(iVar3 + *param_3) < (int)local_dc) {
    local_ac = local_dc;
  }
  local_a4 = param_3[2] - iVar3;
  if ((int)local_d4 < (int)(param_3[2] - iVar3)) {
    local_a4 = local_d4;
/* ... truncated ... */
```

## `FUN_00040156` @ `00040156` score `33`

- reasons: `byte deref` `u8 deref` `offset +1` `small indexes` `channel nibble mask`

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
  local_dc = (uint)bVar3;
  if ((bVar2 & 0xf) == 0) {
    uVar1 = *(undefined1 *)(extraout_r1 + 0x21);
    uVar4 = *(undefined2 *)(extraout_r1 + 0x22);
    FUN_0005beec(&local_60,0,0x2c);
    local_4b = uVar1;
    local_4a = uVar4;
    if (*(int *)(extraout_r1 + 0x1c) == 0) {
      local_60 = &local_b4;
      local_4c = bVar3;
      FUN_0004dc20(iVar20,&local_60);
      goto LAB_000401bc;
    }
  }
  else {
    uVar1 = *(undefined1 *)(extraout_r1 + 0x24);
    uVar4 = *(undefined2 *)(extraout_r1 + 0x25);
    FUN_0005beec(&local_60,0,0x2c);
    local_4b = uVar1;
    local_4a = uVar4;
  }
  if (0xfc < local_dc) {
    local_dc = 0xff;
  }
  iVar6 = FUN_000458e4(&local_b4);
  iVar7 = FUN_000458f0(&local_b4);
  iVar8 = iVar6;
  if (iVar7 < iVar6) {
    iVar8 = iVar7;
  }
  local_e0 = iVar8 >> 1;
  if (*(int *)(extraout_r1 + 0x1c) < iVar8 >> 1) {
    local_e0 = *(int *)(extraout_r1 + 0x1c);
  }
  iVar8 = FUN_000458e4(&local_a4);
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
    piVar10 = (int *)FUN_00040874(extraout_r1 + 0x24,iVar6,iVar7);
    iVar6 = local_b0;
    iVar7 = local_a8;
    if (piVar10 == (int *)0x0) {
      cVar17 = '\0';
      iVar9 = 0;
      local_c8 = (int *)0x0;
      goto LAB_000404ba;
    }
    iVar9 = 0;
    if (1 < bVar11) goto LAB_0004029c;
    if ((bVar2 & 0xf) == 0) goto LAB_000405f0;
LAB_000404d2:
    local_44 = '\x01';
LAB_000404d8:
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
          FUN_000468e8(3,DAT_00040778,299,DAT_00040770,DAT_00040774,DAT_0004076c,DAT_00040768);
          do {
                    /* WARNING: Do nothing block with infinite loop */
          } while( true );
        }
        iVar6 = iVar5 - local_b0;
        FUN_0005bef8(&local_4b,*piVar10 + iVar6 * 3,3);
        local_4c = *(byte *)(piVar10[1] + iVar6);
        if (local_dc < 0xfd) {
          local_4c = (byte)(local_dc * local_4c >> 8);
        }
      }
      FUN_0004dc20(iVar20,&local_60);
    }
  }
  else {
/* ... truncated ... */
```

## `FUN_00040e2c` @ `00040e2c` score `33`

- reasons: `byte deref` `u8 deref` `offset +1` `small indexes` `channel nibble mask`

```c

/* WARNING: Type propagation algorithm not settling */

void FUN_00040e2c(int param_1,int param_2,int param_3,undefined4 param_4,int ****param_5,
                 int *param_6)

{
  char cVar1;
  ushort uVar2;
  undefined2 uVar3;
  int ***pppiVar4;
  undefined4 uVar5;
  undefined4 uVar6;
  int iVar7;
  int iVar8;
  int iVar9;
  int iVar10;
  uint uVar11;
  int iVar12;
  uint uVar13;
  int iVar14;
  int iVar15;
  char cVar16;
  bool bVar17;
  int local_f4;
  uint local_ec;
  undefined4 local_d8;
  undefined4 ****local_c8;
  int local_c4;
  int local_c0;
  int local_bc;
  int ***local_b8;
  int local_b4;
  int local_b0;
  int local_ac;
  int ***local_a8;
  int local_a4;
  int local_a0;
  int local_9c;
  int ****local_80;
  int local_7c;
  uint local_78;
  char local_74;
  int ****local_70;
  undefined1 local_6c;
  undefined1 auStack_6b [3];
  int local_68;
  undefined1 local_64;
  int ****local_60;
  uint local_5c;
  byte bStack_58;
  int ****local_54;
  int local_50;
  uint local_4c;
  char local_48;
  int ****local_44;
  undefined1 local_40;
  undefined1 auStack_3f [3];
  int local_3c;
  undefined1 local_38;
  int ****local_34;
  uint local_30;
  byte bStack_2c;
  
  iVar15 = *(int *)(param_3 + 0x2c);
  uVar2 = *(ushort *)(iVar15 + 8);
  uVar11 = (uint)uVar2;
  iVar12 = *(int *)(param_2 + 0x30);
  local_78 = uVar11;
  if ((iVar12 == 0) && (*(int *)(param_2 + 0x34) == 0x100)) {
    iVar10 = *(int *)(param_2 + 0x38);
    iVar14 = *(int *)(param_2 + 0x2c);
    iVar9 = *(int *)(iVar15 + 0x10);
    cVar1 = *(char *)(iVar15 + 1);
    FUN_00050350(&local_80,0,0x2c);
    local_6c = *(undefined1 *)(param_2 + 0x50);
    bStack_58 = *(byte *)(param_2 + 0x51) & 0xf;
    if (iVar10 == 0x100) {
      if (iVar14 < 1) {
        if (cVar1 == '\x0e') {
          iVar15 = FUN_000450d4(&local_54,param_5,param_1 + 0x38);
          if (iVar15 == 0) {
            return;
          }
          local_60 = param_5;
          local_7c = iVar12;
          local_68 = iVar9;
          local_5c = uVar11;
          FUN_0005bef8(auStack_6b,param_2 + 0x4c,3);
          local_64 = 2;
          local_80 = param_5;
          FUN_0004dc20(param_1,&local_80);
          return;
        }
        local_7c = iVar9;
        if (cVar1 == '\x14') {
          if (*(byte *)(param_2 + 0x4f) < 3) {
            iVar12 = FUN_000458f0(param_5);
            iVar10 = FUN_000458e4(param_5);
            local_70 = param_5;
            iVar15 = FUN_0005b480(uVar11 * iVar10,*(undefined2 *)(iVar15 + 4));
            local_5c = (uint)(uVar2 >> 1);
            local_80 = param_5;
            local_60 = param_5;
            local_64 = 2;
            local_68 = iVar9 + iVar15 * iVar12;
            local_74 = 0x12;
            FUN_0004dc20(param_1,&local_80);
            return;
          }
        }
        else if (((cVar1 == '\x06') || (cVar1 == '\x15')) || (*(byte *)(param_2 + 0x4f) < 3)) {
          local_70 = param_5;
          local_80 = param_5;
          local_74 = cVar1;
          FUN_0004dc20(param_1,&local_80);
          return;
        }
        iVar14 = *(int *)(param_3 + 0x2c);
        local_a8 = (int ***)*param_6;
        local_a4 = param_6[1];
        local_a0 = param_6[2];
        local_9c = param_6[3];
        uVar2 = *(ushort *)(iVar14 + 8);
        cVar1 = *(char *)(iVar14 + 1);
        iVar15 = FUN_00045c38(cVar1);
        iVar9 = FUN_000458f0(param_5);
        iVar12 = FUN_000458e4(&local_a8);
        iVar10 = FUN_000458f0(&local_a8);
        iVar15 = iVar15 * iVar12;
        iVar12 = iVar15;
        if (iVar15 == 0) {
          iVar12 = 1;
        }
        FUN_00039578();
        iVar7 = FUN_0003a048();
        FUN_00039578();
        FUN_0003a314();
        iVar8 = FUN_00045c38();
        local_ec = FUN_0005b480(iVar7 * iVar8 * 4,iVar12);
        if (iVar10 < (int)local_ec) {
          local_ec = iVar10;
        }
        uVar5 = FUN_0004cea4(iVar12 * local_ec);
        FUN_00050350(&local_54,0,0x2c);
        iVar12 = local_9c;
        local_40 = *(undefined1 *)(param_2 + 0x50);
        bStack_2c = *(byte *)(param_2 + 0x51) & 0xf;
        local_48 = cVar1;
        if (cVar1 == '\x14') {
          local_3c = *(int *)(iVar14 + 0x10) + (uint)uVar2 * iVar9;
          local_38 = 2;
          local_48 = '\x12';
          local_30 = (uint)(uVar2 >> 1);
          local_34 = param_5;
        }
        local_54 = &local_a8;
        local_44 = &local_a8;
        local_4c = iVar15;
        iVar7 = local_ec + local_a4 + -1;
        local_50 = uVar5;
        pppiVar4 = local_b8;
        iVar15 = local_b4;
        iVar9 = local_b0;
        iVar10 = local_ac;
        local_b8 = local_a8;
        local_9c = local_a4;
        local_b0 = local_a0;
        while (local_b4 = local_9c, local_ac = iVar7, local_a8 = local_b8, local_a4 = local_b4,
              local_a0 = local_b0, local_9c = local_ac, local_b4 <= iVar12) {
          FUN_000450b8(&local_b8,-(int)*param_5,-(int)param_5[1]);
          FUN_0004096c(local_b8,local_b4,local_b0,local_ac,*(undefined4 *)(iVar14 + 0x10),uVar5,
                       (uint)uVar2,local_48,param_2);
          FUN_0004dc20(param_1,&local_54);
          local_9c = local_9c + 1;
          iVar7 = local_ec + local_9c + -1;
          pppiVar4 = local_b8;
          iVar15 = local_b4;
          iVar9 = local_b0;
          iVar10 = local_ac;
/* ... truncated ... */
```

## `FUN_0003782c` @ `0003782c` score `32`

- reasons: `byte deref` `small indexes` `channel nibble mask` `0xf0`

```c

void FUN_0003782c(int param_1,int param_2,uint param_3)

{
  byte bVar1;
  bool bVar2;
  uint uVar3;
  undefined4 uVar4;
  int *piVar5;
  uint uVar6;
  uint uVar7;
  uint uVar8;
  uint uVar9;
  char cVar10;
  int iVar11;
  int iVar12;
  
  uVar7 = param_3 & 0xff0000;
  if (param_2 == 0) {
    cVar10 = -1;
  }
  else {
    cVar10 = -('\x01' - (*(char *)(param_2 + 8) == '\0'));
    if ((uVar7 == 0) && (iVar11 = FUN_000366e0(param_2), iVar11 != 0)) {
      FUN_00034298(param_1);
    }
  }
  uVar3 = DAT_0003797c;
  uVar6 = (uint)*(ushort *)(param_1 + 0x2a);
  if ((uVar6 & 0x3ff) >> 4 != 0) {
    bVar2 = false;
    uVar9 = 0;
    do {
      iVar12 = *(int *)(param_1 + 0xc);
      iVar11 = uVar9 * 8;
      piVar5 = (int *)(iVar12 + iVar11);
      if (((((param_3 & 0xffff) == uVar3) || ((piVar5[1] & 0xffffU) == (param_3 & 0xffff))) &&
          ((uVar7 == 0xf0000 || (uVar7 == (piVar5[1] & 0xff0000U))))) &&
         ((param_2 == 0 || (*piVar5 == param_2)))) {
        bVar1 = *(byte *)((int)piVar5 + 7);
        if ((bVar1 & 2) != 0) {
          FUN_00036738(param_1,uVar7,0xff,0);
          iVar12 = *(int *)(param_1 + 0xc);
          piVar5 = (int *)(iVar12 + iVar11);
          bVar1 = *(byte *)((int)piVar5 + 7);
        }
        if ((bVar1 & 3) != 0) {
          if (*piVar5 != 0) {
                    /* WARNING: Subroutine does not return */
            FUN_00047570();
          }
          FUN_0004cedc();
          iVar12 = *(int *)(param_1 + 0xc);
          *(undefined4 *)(iVar12 + iVar11) = 0;
        }
        uVar8 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
        uVar6 = uVar8 - 1;
        if (uVar9 < uVar6) {
          FUN_0005fa24(iVar12 + iVar11,iVar12 + iVar11 + 8,(uVar6 - uVar9) * 8);
        }
        uVar6 = uVar8 + 0x3f & 0x3f;
        *(ushort *)(param_1 + 0x2a) =
             (ushort)(uVar6 << 4) | *(ushort *)(param_1 + 0x2a) & (ushort)DAT_00037980;
        uVar4 = FUN_0004cef4(iVar12,uVar6 << 3);
        bVar2 = true;
        uVar6 = (uint)*(ushort *)(param_1 + 0x2a);
        *(undefined4 *)(param_1 + 0xc) = uVar4;
      }
      else {
        uVar9 = uVar9 + 1;
      }
    } while (uVar9 < (uVar6 & 0x3ff) >> 4);
    if (((bVar2) && (cVar10 != '\0')) && (*(char *)(DAT_00037984 + 0x24) != '\0')) {
      FUN_00036f68(param_1,uVar7,0xff);
    }
  }
  return;
}
```

## `FUN_0003bbe0` @ `0003bbe0` score `32`

- reasons: `offset +1` `offset +2` `small indexes` `channel nibble mask`

```c

undefined4
FUN_0003bbe0(uint *param_1,undefined4 param_2,int param_3,undefined4 param_4,int param_5,
            uint param_6,uint param_7)

{
  uint uVar1;
  code *pcVar2;
  
  if (param_1 == (uint *)0x0) {
    FUN_000468e8(3,DAT_0003bcbc,0x112,DAT_0003bcb8,DAT_0003bcc8,DAT_0003bcc4,DAT_0003bcc0);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  FUN_00050350(param_1,0,0x1c);
  if (param_5 == 0) {
    param_5 = 0;
    if (*(code **)(DAT_0003bcac + 0xdc) == (code *)0x0) goto LAB_0003bc1c;
    param_5 = (**(code **)(DAT_0003bcac + 0xdc))(param_2,param_4);
  }
  uVar1 = param_3 * param_5;
  if (param_7 <= uVar1 && uVar1 - param_7 != 0) {
    FUN_000468e8(2,DAT_0003bcbc,0x118,DAT_0003bcb8,DAT_0003bccc,uVar1,param_7);
    return 0;
  }
LAB_0003bc1c:
  *(char *)((int)param_1 + 1) = (char)param_4;
  *(short *)(param_1 + 2) = (short)param_5;
  *param_1 = *param_1 & 0xff00 | 0x19;
  param_1[4] = param_6;
  param_1[5] = param_6;
  uVar1 = DAT_0003bcb0;
  *(short *)(param_1 + 1) = (short)param_2;
  param_1[6] = uVar1;
  pcVar2 = *(code **)(uVar1 + 8);
  *(short *)((int)param_1 + 6) = (short)param_3;
  param_1[3] = param_7;
  if (pcVar2 == (code *)0x0) {
    uVar1 = 0;
  }
  else {
    uVar1 = (*pcVar2)(param_6,param_4);
    param_6 = param_1[5];
  }
  if (uVar1 != param_6) {
    FUN_000468e8(2,DAT_0003bcbc,0x12a,DAT_0003bcb8,DAT_0003bcb4);
  }
  return 1;
}
```

## `FUN_0003bcd0` @ `0003bcd0` score `32`

- reasons: `offset +1` `offset +2` `small indexes` `channel nibble mask`

```c

uint * FUN_0003bcd0(undefined4 *param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4,
                   int param_5)

{
  uint *puVar1;
  uint uVar2;
  uint uVar3;
  uint uVar4;
  
  puVar1 = (uint *)FUN_0004ceb8(0x1c);
  if (puVar1 != (uint *)0x0) {
    if ((param_5 == 0) && (*(code **)(DAT_0003bdb8 + 0xdc) != (code *)0x0)) {
      param_5 = (**(code **)(DAT_0003bdb8 + 0xdc))(param_2,param_4);
    }
    uVar2 = FUN_0003ba04(param_2,param_3,param_4,param_5);
    if (((code *)*param_1 == (code *)0x0) ||
       (uVar3 = (*(code *)*param_1)(uVar2,param_4), uVar3 == 0)) {
      FUN_000468e8(2,DAT_0003bdc4,0x145,DAT_0003bdc0,DAT_0003bdbc,param_2,param_3,param_4,param_5,
                   uVar2);
      FUN_0004cedc(puVar1);
      puVar1 = (uint *)0x0;
    }
    else {
      *(short *)((int)puVar1 + 6) = (short)param_3;
      *(char *)((int)puVar1 + 1) = (char)param_4;
      *(short *)(puVar1 + 2) = (short)param_5;
      uVar4 = DAT_0003bdb4;
      *(short *)(puVar1 + 1) = (short)param_2;
      *puVar1 = uVar4 | *puVar1 & 0xff00;
      if (*(code **)(DAT_0003bdb8 + 0xd0) == (code *)0x0) {
        uVar4 = 0;
      }
      else {
        uVar4 = (**(code **)(DAT_0003bdb8 + 0xd0))(uVar3,param_4);
      }
      puVar1[5] = uVar3;
      puVar1[4] = uVar4;
      puVar1[3] = uVar2;
      puVar1[6] = (uint)param_1;
    }
    return puVar1;
  }
  FUN_000468e8(3,DAT_0003bdc4,0x139,DAT_0003bdc0,DAT_0003bdd0,DAT_0003bdcc,DAT_0003bdc8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

## `FUN_00050d0c` @ `00050d0c` score `32`

- reasons: `small indexes` `channel nibble mask` `0x80`

```c

uint FUN_00050d0c(undefined4 param_1,int param_2)

{
  undefined4 uVar1;
  undefined4 *puVar2;
  uint uVar3;
  uint uVar4;
  int iVar5;
  uint uVar6;
  int *piVar7;
  
  if (param_2 == 0) {
    uVar6 = 0;
  }
  else {
    piVar7 = (int *)(param_2 + -8);
    uVar6 = *(uint *)(param_2 + -4);
    if ((uVar6 & 1) != 0) {
      FUN_000468e8(3,DAT_00050e64,DAT_00050e68,DAT_00050e60,DAT_00050e5c,DAT_00050e58);
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    if (uVar6 < 4) {
      FUN_000468e8(3,DAT_00050e64,0x1c9,DAT_00050e7c,DAT_00050e5c,DAT_00050e78);
      do {
                    /* WARNING: Do nothing block with infinite loop */
      } while( true );
    }
    puVar2 = (undefined4 *)(param_2 + -4 + (uVar6 & 0xfffffffc));
    puVar2[1] = puVar2[1] | 2;
    uVar3 = *(uint *)(param_2 + -4);
    *puVar2 = piVar7;
    *(uint *)(param_2 + -4) = uVar3 | 1;
    if ((uVar3 & 2) != 0) {
      piVar7 = (int *)*piVar7;
      if (piVar7 == (int *)0x0) {
        FUN_000468e8(3,DAT_00050e64,DAT_00050e90,DAT_00050e84,DAT_00050e5c,DAT_00050e8c);
        do {
                    /* WARNING: Do nothing block with infinite loop */
        } while( true );
      }
      uVar3 = piVar7[1];
      if ((uVar3 & 1) == 0) {
        FUN_000468e8(3,DAT_00050e64,DAT_00050e88,DAT_00050e84,DAT_00050e5c,DAT_00050e80);
        do {
                    /* WARNING: Do nothing block with infinite loop */
        } while( true );
      }
      uVar4 = uVar3 & 0xfffffffc;
      if (uVar4 < 0x80) {
        uVar3 = (int)uVar3 >> 2;
        iVar5 = 0;
      }
      else {
        iVar5 = FUN_0005b418(uVar4);
        uVar3 = uVar4 >> (0x1aU - iVar5 & 0xff) ^ 0x20;
        iVar5 = 0x19 - iVar5;
      }
      FUN_000505ac(param_1,piVar7,iVar5,uVar3);
      if ((uint)piVar7[1] < 4) {
        FUN_000468e8(3,DAT_00050e64,DAT_00050e74,DAT_00050e70,DAT_00050e5c,DAT_00050e6c);
        do {
                    /* WARNING: Do nothing block with infinite loop */
        } while( true );
      }
      uVar4 = (*(uint *)(param_2 + -4) & 0xfffffffc) + piVar7[1];
      uVar3 = uVar4 + 4;
      piVar7[1] = uVar3;
      if (0xfffffffb < uVar4) {
        FUN_000468e8(3,DAT_00050e64,0x1c9,DAT_00050e7c,DAT_00050e5c,DAT_00050e78);
        do {
                    /* WARNING: Do nothing block with infinite loop */
        } while( true );
      }
      *(int **)((int)piVar7 + (uVar3 & 0xfffffffc) + 4) = piVar7;
    }
    uVar1 = FUN_00050978(param_1,piVar7);
    FUN_0005064c(param_1,uVar1);
  }
  return uVar6;
}
```

## `FUN_0003c1e0` @ `0003c1e0` score `31`

- reasons: `byte deref` `u8 deref` `offset +1` `offset +2` `channel nibble mask`

```c

undefined4 FUN_0003c1e0(int param_1,uint param_2)

{
  int iVar1;
  int iVar2;
  uint uVar3;
  int iVar4;
  uint uVar5;
  uint uVar6;
  
  if (param_1 == 0) {
    FUN_000468e8(3,DAT_0003c33c,0x1b5,DAT_0003c338,DAT_0003c348,DAT_0003c344,DAT_0003c340);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  if (*(int *)(param_1 + 0x10) != 0) {
    if ((int)((uint)*(ushort *)(param_1 + 2) << 0x1a) < 0) {
      uVar6 = (uint)*(ushort *)(param_1 + 4);
      uVar5 = (uint)*(ushort *)(param_1 + 6);
      if ((param_2 == 0) && (*(code **)(DAT_0003c32c + 0xdc) != (code *)0x0)) {
        param_2 = (**(code **)(DAT_0003c32c + 0xdc))(uVar6,*(undefined1 *)(param_1 + 1));
      }
      if (*(ushort *)(param_1 + 8) == param_2) {
        return 1;
      }
      iVar1 = FUN_00045bcc(*(undefined1 *)(param_1 + 1));
      uVar3 = uVar6 * iVar1 + 7 >> 3;
      if (param_2 < uVar3) {
        FUN_000468e8(2,DAT_0003c33c,0x1d1,DAT_0003c338,DAT_0003c334,uVar3);
      }
      else {
        uVar6 = FUN_0003ba04(uVar6,uVar5,*(undefined1 *)(param_1 + 1),param_2);
        if (uVar6 <= *(uint *)(param_1 + 0xc)) {
          iVar1 = 0;
          uVar6 = *(byte *)(param_1 + 1) - 7 & 0xff;
          if (uVar6 < 4) {
            iVar1 = *(int *)(uVar6 * 4 + DAT_0003c330);
          }
          iVar4 = *(int *)(param_1 + 0x10);
          if (*(ushort *)(param_1 + 8) < param_2) {
            if (uVar5 != 0) {
              iVar2 = iVar4 + (uVar5 - 1) * (uint)*(ushort *)(param_1 + 8) + iVar1;
              iVar4 = iVar4 + param_2 * (uVar5 - 1) + iVar1;
              uVar6 = 0;
              iVar1 = -param_2;
              do {
                FUN_000503bc(iVar4,iVar2,uVar3,iVar1);
                uVar6 = uVar6 + 1;
                iVar2 = iVar2 - (uint)*(ushort *)(param_1 + 8);
                iVar4 = iVar4 + -param_2;
                iVar1 = iVar4;
              } while (uVar6 < uVar5);
            }
          }
          else if (uVar5 != 0) {
            iVar4 = iVar4 + iVar1;
            uVar6 = 0;
            iVar1 = iVar4;
            do {
              FUN_000503bc(iVar1,iVar4,uVar3);
              uVar6 = uVar6 + 1;
              iVar4 = iVar4 + (uint)*(ushort *)(param_1 + 8);
              iVar1 = iVar1 + param_2;
            } while (uVar6 < uVar5);
            *(short *)(param_1 + 8) = (short)param_2;
            return 1;
          }
          *(short *)(param_1 + 8) = (short)param_2;
          return 1;
        }
      }
    }
    return 0;
  }
  FUN_000468e8(3,DAT_0003c33c,0x1b6,DAT_0003c338,DAT_0003c348,DAT_0003c34c,DAT_0003c340);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

## `FUN_00001eec` @ `00001eec` score `30`

- reasons: `channel nibble mask` `7-bit mask` `127`

```c

void FUN_00001eec(uint param_1,uint param_2,undefined4 param_3,undefined4 param_4)

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
    FUN_00001d6c(0x20004084,param_1 - 0x50 & 0xff,param_3,uVar2,param_4);
    uVar2 = extraout_r3;
    param_3 = extraout_r2;
  }
  FUN_00001d6c(0x20004084,0x16,param_3,uVar2,param_4);
  FUN_00001d6c(0x20004084,(int)param_2 >> 7 & 0x7f);
  uVar2 = (uint)DAT_20004081;
  uVar1 = extraout_r2_00;
  if (uVar2 != param_1) {
    DAT_20004081 = (byte)param_1;
    FUN_00001d6c(0x20004084,param_1 - 0x50 & 0xff,extraout_r2_00,uVar2,param_4);
    uVar2 = extraout_r3_00;
    uVar1 = extraout_r2_01;
  }
  FUN_00001d6c(0x20004084,0x36,uVar1,uVar2,param_4);
  FUN_00001d6c(0x20004084,param_2 & 0x7f);
  return;
}
```

## `FUN_00004914` @ `00004914` score `30`

- reasons: `byte deref` `offset +2` `small indexes` `channel nibble mask`

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
/* ... truncated ... */
```

## `FUN_0002754c` @ `0002754c` score `30`

- reasons: `byte deref` `offset +1` `midi send call`

```c

undefined4 FUN_0002754c(int param_1,undefined4 param_2,uint param_3)

{
  undefined4 uVar1;
  uint uVar2;
  
  if (param_3 < 0x101) {
    uVar2 = (uint)*(byte *)(DAT_000275e0 + param_1 * 0x32 + 1);
    if (uVar2 < 0x24) {
                    /* WARNING: Could not recover jumptable at 0x0002756e. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      uVar1 = (**(code **)(DAT_000275e4 + uVar2 * 4))();
      return uVar1;
    }
    uVar1 = 0;
  }
  else {
    uVar1 = 8;
  }
  return uVar1;
}
```

## `FUN_00031730` @ `00031730` score `30`

- reasons: `byte deref` `offset +2` `small indexes` `channel nibble mask`

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
              *(undefined4 *)(puVar14 + 6) = puVar5[2];
              *(char *)(puVar14 + 4) = *pcVar12;
              *(undefined4 *)(puVar14 + 8) = puVar5[1];
              *(uint *)(puVar14 + 2) = uVar3 & 0xffffff;
              pcVar12 = pcVar12 + 1;
              cVar15 = *pcVar12;
            } while ((cVar15 != '\0') && (iVar7 != 0x20));
LAB_0003185c:
            if (uVar10 <= iVar8 + 1U) goto LAB_00031880;
            if (iVar7 == 0x20) goto LAB_000318fc;
            goto LAB_00031868;
          }
        }
LAB_00031878:
        if (iVar8 + 1U < uVar10) goto LAB_00031868;
        goto LAB_00031880;
      }
LAB_00031886:
      FUN_0004cedc(iVar2);
      if ((uVar1 & 0xfd) == 1) {
        FUN_000370c0(param_1,0xf0000,0xff);
      }
      else if (uVar1 == 2) {
        FUN_00034298(param_1);
        FUN_000333bc(param_1);
      }
    }
  }
  return;
LAB_000317de:
  uVar4 = uVar4 + 1;
  if (uVar16 <= uVar4) goto LAB_000318ee;
  goto LAB_000317e6;
LAB_000318ee:
  if (uVar10 <= iVar8 + 1U) {
LAB_00031880:
    if (iVar7 != 0) {
LAB_000318fc:
      iVar8 = iVar2;
      do {
        iVar13 = iVar8 + 0x14;
        FUN_00037498(param_1,*(uint *)(iVar8 + 4) & 0xff0000,uVar9,param_2,iVar8);
        iVar8 = iVar13;
      } while (iVar2 + iVar7 * 0x14 != iVar13);
    }
    goto LAB_00031886;
  }
LAB_00031868:
  iVar8 = iVar8 + 1;
  puVar11 = puVar11 + 2;
  goto LAB_000317a4;
}
```

## `FUN_00036814` @ `00036814` score `30`

- reasons: `byte deref` `offset +2` `small indexes` `channel nibble mask`

```c

bool FUN_00036814(int param_1,uint param_2,uint param_3,undefined4 *param_4)

{
  uint uVar1;
  undefined4 *puVar2;
  uint uVar3;
  undefined4 *puVar4;
  uint uVar5;
  uint uVar6;
  uint uVar7;
  uint uVar8;
  byte *pbVar9;
  uint local_3c;
  
  uVar7 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
  if (uVar7 == 0) {
    return false;
  }
  uVar5 = param_3 >> 2;
  if (0x1f < uVar5) {
    uVar5 = 0x1f;
  }
  uVar8 = 1 << (uVar5 & 0xff);
  uVar5 = 0;
  puVar4 = *(undefined4 **)(param_1 + 0xc);
LAB_0003686c:
  do {
    if ((*(byte *)((int)puVar4 + 7) & 2) == 0) {
      if (uVar7 <= uVar5) {
        return (bool)(*(byte *)((int)puVar4 + 7) & 2);
      }
      puVar4 = *(undefined4 **)(param_1 + 0xc) + uVar5 * 2;
      local_3c = 0xffffffff;
      do {
        puVar2 = (undefined4 *)*puVar4;
        if (((((puVar2[1] & uVar8) != 0) &&
             (uVar1 = puVar4[1], (param_2 & 0xff0000) == (uVar1 & 0xff0000))) &&
            ((uVar1 & 0xffff & ~(param_2 & 0xffff)) == 0)) &&
           ((int)local_3c < (int)(uVar1 & 0xffff))) {
          pbVar9 = (byte *)*puVar2;
          uVar3 = (uint)*(byte *)(puVar2 + 2);
          if (uVar3 == 0xff) {
            uVar3 = (uint)*pbVar9;
            if (uVar3 != 0) {
LAB_000369ce:
              if (param_3 != uVar3) goto LAB_000369c6;
              *param_4 = *(undefined4 *)(pbVar9 + 4);
LAB_00036982:
              local_3c = uVar1 & 0xffff;
              if ((param_2 & 0xffff) == (uVar1 & 0xffff)) {
                return true;
              }
            }
          }
          else if (uVar3 != 0) {
            uVar6 = 0;
            do {
              if (pbVar9[uVar6 + uVar3 * 4] == param_3) {
                *param_4 = *(undefined4 *)(pbVar9 + uVar6 * 4);
                goto LAB_00036982;
              }
              uVar6 = uVar6 + 1;
            } while (uVar6 < uVar3);
          }
        }
LAB_0003698c:
        uVar5 = uVar5 + 1;
        puVar4 = puVar4 + 2;
        if (uVar7 <= uVar5) {
          return local_3c != 0xffffffff;
        }
      } while( true );
    }
    if ((((*(byte *)(param_1 + 0x2a) & 8) == 0) && ((puVar4[1] & 0xff0000) == (param_2 & 0xff0000)))
       && (puVar2 = (undefined4 *)*puVar4, (puVar2[1] & uVar8) != 0)) {
      uVar1 = (uint)*(byte *)(puVar2 + 2);
      pbVar9 = (byte *)*puVar2;
      if (uVar1 == 0xff) {
        for (; *pbVar9 != 0; pbVar9 = pbVar9 + 8) {
          if (param_3 == *pbVar9) {
            *param_4 = *(undefined4 *)(pbVar9 + 4);
            return true;
          }
        }
      }
      else if (uVar1 != 0) {
        uVar3 = 0;
        do {
          if (pbVar9[uVar3 + uVar1 * 4] == param_3) {
            *param_4 = *(undefined4 *)(pbVar9 + uVar3 * 4);
            return true;
          }
          uVar3 = uVar3 + 1;
        } while (uVar3 < uVar1);
        uVar5 = uVar5 + 1;
        puVar4 = puVar4 + 2;
        if (uVar7 <= uVar5) {
          return false;
        }
        goto LAB_0003686c;
      }
    }
    uVar5 = uVar5 + 1;
    puVar4 = puVar4 + 2;
    if (uVar7 <= uVar5) {
      return false;
    }
  } while( true );
LAB_000369c6:
  uVar3 = (uint)pbVar9[8];
  pbVar9 = pbVar9 + 8;
  if (uVar3 == 0) goto LAB_0003698c;
  goto LAB_000369ce;
}
```

## `FUN_00047e7c` @ `00047e7c` score `30`

- reasons: `byte deref` `small indexes` `channel nibble mask` `127`

```c

uint FUN_00047e7c(char *param_1,uint param_2,int param_3,int param_4,int param_5,int *param_6,
                 byte param_7)

{
  uint uVar1;
  int iVar2;
  uint uVar3;
  uint uVar4;
  uint uVar5;
  int iVar6;
  undefined4 uVar7;
  int iVar8;
  char *pcVar9;
  uint uVar10;
  uint uVar11;
  uint uVar12;
  int iVar13;
  int iVar14;
  int iVar15;
  int iVar16;
  int iVar17;
  uint uVar18;
  char cVar19;
  int local_68;
  uint local_54;
  int local_50;
  uint local_4c;
  int local_44;
  uint local_34;
  int local_30;
  int local_2c [2];
  
  iVar8 = DAT_000481a4;
  uVar12 = (uint)param_7;
  if ((param_7 & 3) == 0) {
    uVar18 = 0;
    local_4c = 0;
    cVar19 = '\0';
    local_44 = 0;
    local_34 = uVar12 & 3;
    do {
      uVar3 = uVar18;
      uVar1 = local_34;
      if (((param_2 <= uVar18) || (pcVar9 = param_1 + uVar18, param_1[uVar18] == '\0')) ||
         (param_5 < 1)) goto joined_r0x0004804a;
      local_54 = uVar12;
      if (uVar18 == 0) {
        local_54 = uVar12 | 4;
      }
      if (param_3 == 0) goto joined_r0x0004804a;
      local_30 = 0;
      uVar4 = FUN_00047bb4(pcVar9,&local_30);
      local_2c[0] = local_30;
      if (*pcVar9 == '\0') {
        iVar6 = local_30;
        local_50 = 0;
      }
      else {
        iVar13 = 0;
        local_50 = 0;
        local_68 = 0;
        iVar14 = 0;
        iVar16 = -1;
        do {
          local_30 = local_2c[0];
          uVar5 = FUN_00047bb4(pcVar9,local_2c);
          iVar15 = iVar14 + 1;
          iVar17 = iVar16;
          if ((local_54 & 8) == 0) {
LAB_00047f98:
            iVar6 = FUN_000446fc(param_3,uVar4,uVar5);
            iVar13 = iVar13 + iVar6;
            if (iVar6 != 0) {
              iVar13 = iVar13 + param_4;
            }
            if (((iVar16 != -1) || (iVar13 - param_4 <= param_5)) ||
               (iVar17 = local_68, -1 < (int)(local_54 << 0x1d))) {
              iVar6 = iVar17;
              uVar1 = local_34;
              if (uVar4 == 10) {
LAB_00047fe6:
                if (local_68 == 0) {
                  if (iVar17 != -1) goto LAB_00048112;
                  iVar6 = local_30;
                  local_50 = iVar13;
                  if (iVar14 == 0) goto LAB_00048004;
                  local_44 = local_44 + iVar13;
                  goto joined_r0x0004804a;
                }
                if (iVar17 != -1) goto LAB_00048112;
                iVar6 = local_30;
                if (iVar14 == 0) goto LAB_00048004;
              }
              else {
                if (uVar4 != 0xd) {
                  uVar11 = 0;
                  uVar10 = 0x20;
                  do {
                    if (uVar10 == uVar4) goto LAB_00047fe6;
                    uVar11 = uVar11 + 1 & 0xff;
                    uVar10 = (uint)*(byte *)(iVar8 + uVar11);
                  } while (uVar10 != 0);
                  if (((uVar5 == 0) ||
                      (((0x51ff < uVar5 + DAT_000481a8 && (0x5d < uVar5 + DAT_000481ac)) &&
                       ((0xff < uVar5 + DAT_000481b0 &&
                        ((((0x7f < uVar5 + DAT_000481b4 && (0x2f < uVar5 + DAT_000481b8)) &&
                          (0xf < uVar5 + DAT_000481bc)) && (0x1f < uVar5 + DAT_000481c0)))))))) &&
                     ((uVar4 == 0 ||
                      (((0x51ff < uVar4 + DAT_000481a8 && (0x5d < uVar4 + DAT_000481ac)) &&
                       ((((0xff < uVar4 + DAT_000481b0 &&
                          ((0x7f < uVar4 + DAT_000481b4 && (0x2f < uVar4 + DAT_000481b8)))) &&
                         (0xf < uVar4 + DAT_000481bc)) && (0x1f < uVar4 + DAT_000481c0)))))))) {
                    if (iVar17 == -1) {
                      local_50 = iVar13;
                    }
                    goto LAB_000480f8;
                  }
                  iVar6 = local_30;
                  local_50 = iVar13;
                  if ((iVar17 == -1) || (iVar6 = iVar17, (int)(local_54 << 0x1d) < 0))
                  goto LAB_00048004;
                  goto joined_r0x0004804a;
                }
                if (local_68 == 0) {
                  if (iVar17 != -1) goto LAB_00048112;
                  iVar6 = local_30;
                  local_50 = iVar13;
                  if ((iVar14 == 0) || (uVar5 == 10)) goto LAB_00048004;
                  local_44 = local_44 + iVar13;
                  uVar3 = local_34;
                  goto joined_r0x0004804a;
                }
                if (iVar17 != -1) goto LAB_00048112;
                iVar6 = local_30;
                if ((iVar14 == 0) || (uVar5 == 10)) goto LAB_00048004;
              }
              local_44 = local_44 + local_50;
              goto LAB_00048014;
            }
            iVar6 = local_68;
            if (((local_68 != -1) || (iVar6 = local_30, iVar15 == 0)) ||
               ((uVar4 == 0xd && (uVar5 == 10)))) goto LAB_00048004;
            local_44 = local_44 + local_50;
            local_68 = iVar16;
            goto LAB_00048014;
          }
          if (uVar4 == 0x23) {
            cVar19 = local_4c != 2;
            local_4c = (uint)(byte)cVar19;
          }
          else {
            if (cVar19 != '\x01') goto LAB_00047f98;
            if (uVar4 == 0x20) {
              local_4c = 2;
              cVar19 = '\x02';
            }
          }
LAB_000480f8:
          iVar2 = local_30;
          local_68 = local_30;
          local_30 = local_2c[0];
          uVar4 = uVar5;
          iVar14 = iVar15;
          iVar16 = iVar17;
        } while (pcVar9[iVar2] != '\0');
        iVar6 = iVar17;
        if (iVar17 == -1) {
          iVar6 = local_2c[0];
          if (iVar15 != 0) {
            iVar6 = iVar2;
          }
        }
        else {
LAB_00048112:
          uVar1 = local_34;
          if (-1 < (int)(local_54 << 0x1d)) goto joined_r0x0004804a;
        }
      }
LAB_00048004:
/* ... truncated ... */
```

## `FUN_000547c4` @ `000547c4` score `30`

- reasons: `byte deref` `offset +3` `small indexes` `channel nibble mask`

```c

int FUN_000547c4(int param_1,int param_2,int param_3,int param_4,int param_5,int *param_6)

{
  byte bVar1;
  bool bVar2;
  byte bVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  undefined4 uVar7;
  uint uVar8;
  uint uVar9;
  int iVar10;
  code *pcVar11;
  int local_3c;
  int local_38;
  code *local_34;
  
  iVar4 = FUN_00036ab8(param_1,0,1);
  iVar5 = FUN_00036ab8(param_1,0,2);
  uVar8 = (uint)*(byte *)(param_2 + 3);
  if ((int)(uVar8 << 0x1e) < 0) {
    if (-1 < (int)(uVar8 << 0x1f)) {
      if (iVar5 == DAT_00054acc) goto LAB_00054814;
      goto LAB_00054820;
    }
    if (iVar4 == DAT_00054acc) {
LAB_00054814:
      uVar8 = *(byte *)(param_2 + 3) & 0xfffffffd;
      *(char *)(param_2 + 3) = (char)uVar8;
      goto LAB_0005481c;
    }
  }
  else {
LAB_0005481c:
    if (-1 < (int)(uVar8 << 0x1f)) {
LAB_00054820:
      local_34 = DAT_00054ad4;
      pcVar11 = DAT_00054ad0;
      goto LAB_00054828;
    }
  }
  local_34 = DAT_00054ad0;
  pcVar11 = DAT_00054ad4;
LAB_00054828:
  param_6[1] = 0;
  param_6[2] = 0;
  param_6[5] = 0;
  *param_6 = 0;
  param_6[3] = 0;
  param_6[4] = 0;
  iVar5 = FUN_0003818c(param_1,param_3);
  iVar4 = param_3;
  if (iVar5 == 0) {
    local_38 = param_4;
    if (param_6[5] == 0) {
      local_38 = param_6[2];
    }
    param_6[1] = local_38;
  }
  else {
    local_3c = 0;
    bVar2 = true;
    do {
      iVar6 = FUN_000325b0(iVar5,DAT_00054ad8);
      if (iVar6 == 0) {
        bVar3 = FUN_00036ab8(iVar5,0,0x7e);
        if (bVar3 == 0) {
          iVar6 = (*local_34)(iVar5);
          if (!bVar2) {
            iVar6 = iVar6 + param_5;
          }
          local_38 = param_6[2];
          if (((*(byte *)(param_2 + 3) & 2) != 0) && (param_4 < local_3c + local_38 + iVar6)) {
            if (param_6[5] != 0) {
              local_38 = param_4;
            }
            goto LAB_0005488a;
          }
          param_6[2] = iVar6 + local_38;
        }
        else {
          if ((int)((uint)*(byte *)(param_2 + 3) << 0x1f) < 0) {
            iVar6 = FUN_00036ab8(iVar5,0,4);
            uVar9 = (uint)*(byte *)(param_2 + 3);
            uVar8 = uVar9 & 2;
            if (param_3 == iVar4) goto LAB_000549ae;
LAB_0005491a:
            iVar6 = iVar6 + param_5;
            if ((uVar8 != 0) && (param_4 < local_3c + param_6[2] + iVar6)) break;
            param_6[2] = param_6[2] + param_5;
            bVar1 = *(byte *)(param_6 + 6);
            iVar10 = param_6[5] + 1;
            param_6[5] = iVar10;
          }
          else {
            iVar6 = FUN_00036ab8(iVar5,0,6);
            uVar9 = (uint)*(byte *)(param_2 + 3);
            uVar8 = uVar9 & 2;
            if (param_3 != iVar4) goto LAB_0005491a;
LAB_000549ae:
            if ((uVar8 != 0) && (local_38 = param_6[2], param_4 < local_3c + local_38 + iVar6)) {
              if (param_6[5] == 0) goto LAB_0005488a;
              param_6[1] = param_4;
              goto LAB_00054894;
            }
            bVar1 = *(byte *)(param_6 + 6);
            iVar10 = param_6[5] + 1;
            param_6[5] = iVar10;
          }
          local_3c = local_3c + iVar6;
          if ((bVar1 & 1) != 0) {
            iVar6 = FUN_0004cef4(param_6[4],iVar10 * 0x18);
            if (iVar6 == 0) {
              FUN_000468e8(3,DAT_00054aec,0x11a,DAT_00054ae4,DAT_00054ae8,DAT_00054ae0,DAT_00054adc)
              ;
              do {
                    /* WARNING: Do nothing block with infinite loop */
              } while( true );
            }
            *(int *)(iVar6 + (param_6[5] + -1) * 0x18) = iVar5;
            if ((*(byte *)(param_2 + 3) & 1) == 0) {
              uVar7 = FUN_00036ab8(iVar5,0,6);
            }
            else {
              uVar7 = FUN_00036ab8(iVar5,0,4);
            }
            *(undefined4 *)(iVar6 + (param_6[5] + -1) * 0x18 + 4) = uVar7;
            if ((int)((uint)*(byte *)(param_2 + 3) << 0x1f) < 0) {
              uVar7 = FUN_00036ab8(iVar5,0,5);
            }
            else {
              uVar7 = FUN_00036ab8(iVar5,0,7);
            }
            iVar10 = (param_6[5] + -1) * 0x18 + iVar6;
            *(uint *)(iVar10 + 0x10) = (uint)bVar3;
            *(undefined4 *)(iVar10 + 8) = uVar7;
            *(byte *)(iVar10 + 0x14) = *(byte *)(iVar10 + 0x14) & 0xfe;
            param_6[4] = iVar6;
          }
        }
        iVar6 = (*pcVar11)(iVar5);
        iVar10 = *param_6;
        if (iVar10 < iVar6) {
          iVar10 = (*pcVar11)(iVar5);
        }
        *param_6 = iVar10;
        param_6[3] = param_6[3] + 1;
        bVar2 = false;
      }
      if ((int)((uint)*(byte *)(param_2 + 3) << 0x1d) < 0) {
        iVar4 = iVar4 + -1;
        if (iVar4 < 0) break;
        iVar5 = FUN_0003818c(param_1,iVar4);
      }
      else {
        iVar4 = iVar4 + 1;
        iVar5 = FUN_0003818c(param_1,iVar4);
      }
      if (iVar5 == 0) {
        if (param_6[5] == 0) {
          param_6[1] = param_6[2];
          return iVar4;
        }
        goto LAB_000548d6;
      }
    } while ((param_3 == iVar4) || (iVar6 = FUN_00032568(iVar5,0x200000), iVar6 == 0));
    if (param_6[5] == 0) {
      local_38 = param_6[2];
LAB_0005488a:
      param_6[1] = local_38;
      if (param_3 == iVar4) {
        uVar9 = (uint)*(byte *)(param_2 + 3);
LAB_00054894:
        iVar5 = *(int *)(iVar4 * 4 + **(int **)(param_1 + 8));
        if ((int)(uVar9 << 0x1d) < 0) {
          iVar4 = iVar4 + -1;
        }
        else {
/* ... truncated ... */
```

## `FUN_0005b950` @ `0005b950` score `30`

- reasons: `channel nibble mask` `7-bit mask` `127`

```c

undefined8 FUN_0005b950(int param_1,uint param_2,int param_3,uint param_4)

{
  int iVar1;
  uint uVar2;
  uint uVar3;
  
  uVar3 = (param_4 & 0x7fffffff) >> 0x14;
  if (uVar3 == 0) {
LAB_0005b972:
    param_3 = 0;
    param_4 = param_4 & 0xfff00000;
  }
  else if (uVar3 == DAT_0005b9b8) {
    if ((param_4 & 0x100000) != 0 && (param_4 & 0xfffff) != 0) goto LAB_0005b99c;
    goto LAB_0005b972;
  }
  uVar3 = (param_2 & 0x7fffffff) >> 0x14;
  if (uVar3 == 0) {
LAB_0005b986:
    iVar1 = 0;
    uVar2 = param_2 & 0xfff00000;
  }
  else {
    iVar1 = param_1;
    uVar2 = param_2;
    if (uVar3 == DAT_0005b9b8) {
      if ((param_2 & 0x100000) != 0 && (param_2 & 0xfffff) != 0) goto LAB_0005b99c;
      goto LAB_0005b986;
    }
  }
  if ((int)(uVar2 ^ param_4) < 0) {
    if ((((uVar2 ^ param_4 | param_4) & 0x7fffffff) != 0 || param_3 != 0) || iVar1 != 0) {
      return CONCAT44(param_2,param_1);
    }
  }
  else if ((-1 < (int)uVar2) && (param_4 == uVar2)) {
    return CONCAT44(param_2,param_1);
  }
LAB_0005b99c:
  return CONCAT44(param_2,param_1);
}
```

## `FUN_0005b960` @ `0005b960` score `30`

- reasons: `channel nibble mask` `7-bit mask` `127`

```c

undefined8 FUN_0005b960(int param_1,uint param_2,int param_3,uint param_4)

{
  int iVar1;
  uint uVar2;
  uint uVar3;
  
  uVar3 = (param_2 & 0x7fffffff) >> 0x14;
  if (uVar3 == 0) {
LAB_0005b972:
    iVar1 = 0;
    uVar2 = param_2 & 0xfff00000;
  }
  else {
    iVar1 = param_1;
    uVar2 = param_2;
    if (uVar3 == DAT_0005b9b8) {
      if ((param_2 & 0x100000) != 0 && (param_2 & 0xfffff) != 0) goto LAB_0005b99c;
      goto LAB_0005b972;
    }
  }
  uVar3 = (param_4 & 0x7fffffff) >> 0x14;
  if (uVar3 == 0) {
LAB_0005b986:
    param_3 = 0;
    param_4 = param_4 & 0xfff00000;
  }
  else if (uVar3 == DAT_0005b9b8) {
    if ((param_4 & 0x100000) != 0 && (param_4 & 0xfffff) != 0) goto LAB_0005b99c;
    goto LAB_0005b986;
  }
  if ((int)(param_4 ^ uVar2) < 0) {
    if ((((param_4 ^ uVar2 | uVar2) & 0x7fffffff) != 0 || iVar1 != 0) || param_3 != 0) {
      return CONCAT44(param_2,param_1);
    }
  }
  else if ((-1 < (int)param_4) && (uVar2 == param_4)) {
    return CONCAT44(param_2,param_1);
  }
LAB_0005b99c:
  return CONCAT44(param_2,param_1);
}
```

## `FUN_0005ba44` @ `0005ba44` score `30`

- reasons: `channel nibble mask` `7-bit mask` `127`

```c

int FUN_0005ba44(uint param_1,uint param_2)

{
  uint uVar1;
  uint uVar2;
  int iVar3;
  
  uVar2 = (param_2 & 0x7fffffff) >> 0x14;
  iVar3 = uVar2 - 0x380;
  if (iVar3 < 0x7f) {
    return 0;
  }
  if (iVar3 < 0x9e) {
    uVar2 = -(uVar2 - 0x41e);
    uVar1 = ((param_2 & 0xfffff) << 0xb | 0x80000000) >> (uVar2 & 0xff);
    iVar3 = ((int)param_2 >> 0x1f) * 2 + 1;
    uVar2 = uVar2 + 0x15;
    if ((int)uVar2 < 0x20) {
      return iVar3 * (param_1 >> (uVar2 & 0xff) | uVar1);
    }
    return iVar3 * uVar1;
  }
  return 0x7fffffff - ((int)param_2 >> 0x1f);
}
```

## `FUN_000020a4` @ `000020a4` score `29`

- reasons: `byte deref` `channel nibble mask` `0xf0` `sysex end`

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

