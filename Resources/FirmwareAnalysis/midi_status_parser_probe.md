# Motion 32 MIDI Status Parser Probe

Search is intentionally biased toward real three-byte MIDI handling:
status nibble/channel tests plus separate data-byte references.

## `FUN_00005854` @ `00005854` score `46`

- reasons: 0x80, 0xf0, status mask &0xf0, channel nibble mask, nibble compose <<4, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_00004d5c` @ `00004d5c` score `33`

- reasons: 0xf7, 0x7f, 0x78, channel nibble mask, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_00004dde` @ `00004dde` score `33`

- reasons: 0xf7, 0x7f, 0x78, channel nibble mask, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_00031730` @ `00031730` score `31`

- reasons: 0xf0, channel nibble mask, status shift >>4, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_00032b10` @ `00032b10` score `31`

- reasons: 0xf0, status mask &0xf0, channel nibble mask, data byte 1, multi-param handler

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

## `FUN_00004ce8` @ `00004ce8` score `30`

- reasons: 0xf7, 0x7f, channel nibble mask, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_00037110` @ `00037110` score `30`

- reasons: channel nibble mask, status shift >>4, nibble compose <<4, data byte 1, data byte 2, byte 3, multi-param handler

```c

void FUN_00037110(int param_1,undefined4 param_2,undefined4 param_3,uint param_4)

{
  uint uVar1;
  undefined4 *puVar2;
  undefined4 uVar3;
  int iVar4;
  uint uVar5;
  undefined4 *puVar6;
  int iVar7;
  int iVar8;
  
  FUN_00036738(param_1,param_4 & 0xff0000,param_2,0);
  uVar1 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
  if (uVar1 == 0) {
    uVar1 = 1;
  }
  else {
    uVar5 = 0;
    puVar2 = *(undefined4 **)(param_1 + 0xc);
    do {
      if (((*(byte *)((int)puVar2 + 7) & 1) != 0) && (param_4 == (puVar2[1] & 0xffffff)))
      goto LAB_000371f0;
      uVar5 = uVar5 + 1;
      puVar2 = puVar2 + 2;
    } while (uVar5 < uVar1);
    uVar1 = uVar1 + 1 & 0x3f;
  }
  uVar5 = *(ushort *)(param_1 + 0x2a) & DAT_00037278;
  *(ushort *)(param_1 + 0x2a) = (ushort)uVar5 | (ushort)(uVar1 << 4);
  if ((uVar5 & 0x3f0) == 0 && uVar1 == 0) {
    FUN_000468e8(3,DAT_0003728c,DAT_00037290,DAT_00037288,DAT_00037284,DAT_00037280);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  puVar2 = (undefined4 *)FUN_0004cef4(*(undefined4 *)(param_1 + 0xc),uVar1 << 3);
  *(undefined4 **)(param_1 + 0xc) = puVar2;
  if (puVar2 == (undefined4 *)0x0) {
    FUN_000468e8(3,DAT_0003728c,0x2c4,DAT_00037288,DAT_0003729c,DAT_00037298,DAT_00037294);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  uVar1 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
  iVar4 = uVar1 - 1;
  if (uVar1 != 1) {
    puVar6 = puVar2 + (uVar1 - 2) * 2;
    do {
      if ((*(byte *)((int)puVar6 + 7) & 3) != 0) {
        puVar2 = puVar6 + 2;
        iVar4 = iVar4 << 3;
        goto LAB_000371bc;
      }
      iVar4 = iVar4 + -1;
      puVar6[2] = *puVar6;
      puVar6[3] = puVar6[1];
      puVar6 = puVar6 + -2;
    } while (iVar4 != 0);
  }
  iVar4 = 0;
LAB_000371bc:
  FUN_00050350(puVar2,0,8);
  iVar8 = *(int *)(param_1 + 0xc);
  uVar3 = FUN_0004ceb8(0xc);
  iVar7 = *(int *)(param_1 + 0xc);
  *(undefined4 *)(iVar8 + iVar4) = uVar3;
  FUN_00047564(*(undefined4 *)(iVar7 + iVar4));
  puVar2 = (undefined4 *)(*(int *)(param_1 + 0xc) + iVar4);
  puVar2[1] = (uint)(*(byte *)((int)puVar2 + 7) | 1) << 0x18 | param_4 & 0xffffff;
LAB_000371f0:
  uVar3 = *puVar2;
  if ((param_4 == 0) && (iVar4 = FUN_00047840(param_2), iVar4 << 0x1a < 0)) {
    FUN_00034298(param_1);
    FUN_0004763c(uVar3,param_2,param_3);
  }
  else {
    FUN_0004763c(uVar3,param_2,param_3);
  }
  if (*(char *)(DAT_0003727c + 0x24) != '\0') {
    FUN_00036f68(param_1,param_4,param_2);
  }
  return;
}
```

## `FUN_00043030` @ `00043030` score `30`

- reasons: channel nibble mask, status shift >>4, nibble compose <<4, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_00036738` @ `00036738` score `29`

- reasons: 0xf0, channel nibble mask, status shift >>4, data byte 1, data byte 2, multi-param handler

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

## `FUN_00039de4` @ `00039de4` score `29`

- reasons: 0xb0, channel nibble mask, data byte 1, data byte 2, byte 3, multi-param handler

```c

int * FUN_00039de4(int param_1,int param_2)

{
  int *piVar1;
  int iVar2;
  int iVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  int *piVar6;
  undefined4 local_20;
  undefined1 uStack_1d;
  undefined4 local_1c;
  
  piVar1 = (int *)FUN_00046704(DAT_00039ff4);
  if (piVar1 == (int *)0x0) {
    FUN_000468e8(3,DAT_0003a010,0x41,DAT_0003a008,DAT_0003a014,DAT_0003a018,DAT_0003a004);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  FUN_00050350(piVar1,0,0x324);
  piVar1[2] = -1;
  piVar1[3] = -1;
  piVar1[4] = 0;
  piVar1[5] = 0;
  piVar1[6] = 0x82;
  *piVar1 = param_1;
  *(ushort *)((int)piVar1 + 0x3e) = *(ushort *)((int)piVar1 + 0x3e) & 0xfe00 | 3;
  piVar1[1] = param_2;
  *(undefined1 *)(piVar1 + 0x10) = 0x12;
  iVar2 = FUN_0004cea4(0x58);
  piVar1[0xac] = iVar2;
  if (iVar2 == 0) {
    FUN_000468e8(3,DAT_0003a010,0x58,DAT_0003a008,DAT_0003a014,DAT_0003a00c,DAT_0003a004);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  FUN_0003b2e0();
  if ((code *)piVar1[0xad] != (code *)0x0) {
    (*(code *)piVar1[0xad])(piVar1,piVar1[0xac]);
  }
  iVar2 = piVar1[0xac];
  *(undefined4 *)(iVar2 + 4) = 0;
  *(undefined4 *)(iVar2 + 8) = 0;
  *(int *)(iVar2 + 0x10) = param_2 + -1;
  *(int *)(iVar2 + 0xc) = param_1 + -1;
  *(char *)(iVar2 + 0x14) = (char)piVar1[0x10];
  piVar1[0x9a] = 1;
  iVar2 = FUN_0004bfac();
  piVar1[0xc3] = iVar2;
  FUN_000466f4(piVar1 + 0x9b,0x10);
  uVar4 = DAT_00039ffc;
  iVar2 = DAT_00039ff8;
  piVar6 = *(int **)(DAT_00039ff8 + 0x14);
  *(int **)(DAT_00039ff8 + 0x14) = piVar1;
  iVar3 = FUN_000487e8(uVar4,0x21,piVar1);
  piVar1[0xc2] = iVar3;
  if (iVar3 == 0) {
    FUN_000468e8(3,DAT_0003a010,0x6d,DAT_0003a008,DAT_0003a014,DAT_0003a01c,DAT_0003a004);
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  iVar3 = FUN_00052af4();
  if (iVar3 == 0) {
    uVar4 = FUN_00046cdc(5);
    uVar5 = FUN_00046cdc(0);
    local_1c = CONCAT22(CONCAT11(local_1c._3_1_,(char)((uint)uVar5 >> 0x10)),(short)uVar5);
    iVar3 = FUN_000513b8(piVar1,CONCAT22(CONCAT11(uStack_1d,(char)((uint)uVar4 >> 0x10)),
                                         (short)uVar4),local_1c,1,0);
  }
  else {
    iVar3 = FUN_00052ad4();
  }
  piVar1[0xc1] = iVar3;
  iVar3 = FUN_000322b4(0);
  piVar1[0xb3] = iVar3;
  iVar3 = FUN_000322b4(0);
  piVar1[0xb2] = iVar3;
  iVar3 = FUN_000322b4(0);
  piVar1[0xb1] = iVar3;
  iVar3 = FUN_000322b4(0);
  piVar1[0xb0] = iVar3;
  FUN_00037988(piVar1[0xb3]);
  FUN_00037988(piVar1[0xb1]);
  FUN_00037988(piVar1[0xb0]);
  FUN_000323cc(piVar1[0xb1],2);
  FUN_000323cc(piVar1[0xb0],2);
  FUN_000351c0(piVar1[0xb3],0);
  FUN_000351c0(piVar1[0xb1],0);
  FUN_000351c0(piVar1[0xb0],0);
  FUN_00034298(piVar1[0xb2]);
  if (piVar6 == (int *)0x0) {
    piVar6 = piVar1;
  }
  *(int **)(iVar2 + 0x14) = piVar6;
  FUN_000460b8(piVar1 + 0xba,DAT_0003a000,0x38,0);
  FUN_0004893c(piVar1[0xc2]);
  return piVar1;
}
```

## `FUN_0004e190` @ `0004e190` score `29`

- reasons: 0x80, 0x7f, channel nibble mask, data byte 1, data byte 2, byte 3

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

## `FUN_0004ebe4` @ `0004ebe4` score `29`

- reasons: 0x80, 0x7f, channel nibble mask, data byte 1, data byte 2, byte 3

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

## `FUN_0005f274` @ `0005f274` score `29`

- reasons: 0x7f, 0x78, channel nibble mask, data byte 1, data byte 2, byte 3, multi-param handler

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
        uVar16 = uVar5;
        if (DAT_0005f5c4 + iVar9 + -8 == iVar18) goto LAB_0005f340;
        uVar2 = *(uint *)(iVar18 + 4) & 0xfffffffc;
        uVar16 = uVar15;
        if (0xf < (int)(uVar2 - uVar17)) goto LAB_0005f340;
        iVar14 = *(int *)(iVar18 + 0xc);
      } while ((int)(uVar2 - uVar17) < 0);
      iVar9 = *(int *)(iVar18 + 8);
      *(int *)(iVar9 + 0xc) = iVar14;
      *(int *)(iVar14 + 8) = iVar9;
      goto LAB_0005f2ba;
    }
    uVar16 = uVar16 >> 3;
    iVar9 = uVar17 + 8;
  }
  iVar9 = DAT_0005f5c4 + iVar9;
  iVar18 = *(int *)(iVar9 + 4);
  if (iVar18 == iVar9 + -8) {
    iVar18 = *(int *)(iVar9 + 0xc);
    uVar16 = uVar16 + 2;
    if (iVar9 == iVar18) {
LAB_0005f340:
      uVar5 = DAT_0005f5c4;
      iVar18 = *(int *)(DAT_0005f5c4 + 0x10);
      iVar9 = DAT_0005f5c4 + 8;
      if (iVar18 == iVar9) {
        uVar15 = *(uint *)(DAT_0005f5c4 + 4);
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
          FUN_0005f7e8(param_1);
          return (int *)(iVar18 + 8);
        }
        *(int *)(DAT_0005f5c4 + 0x10) = iVar9;
        *(int *)(uVar5 + 0x14) = iVar9;
        if (-1 < (int)uVar15) goto LAB_0005f2ba;
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
          if (uVar7 < 5) {
            iVar9 = (uVar13 >> 6) + 0x38;
            iVar14 = ((uVar13 >> 6) + 0x39) * 8;
          }
          else if (uVar7 < 0x15) {
            iVar9 = uVar7 + 0x5b;
            iVar14 = (uVar7 + 0x5c) * 8;
          }
          else if (uVar7 < 0x55) {
            iVar9 = (uVar13 >> 0xc) + 0x6e;
            iVar14 = ((uVar13 >> 0xc) + 0x6f) * 8;
          }
          else if (uVar7 < 0x155) {
            iVar9 = (uVar13 >> 0xf) + 0x77;
            iVar14 = ((uVar13 >> 0xf) + 0x78) * 8;
          }
          else if (DAT_0005f7d4 < uVar7) {
            iVar9 = 0x7e;
            iVar14 = 0x3f8;
          }
          else {
            iVar9 = (uVar13 >> 0x12) + 0x7c;
            iVar14 = ((uVar13 >> 0x12) + 0x7d) * 8;
          }
          piVar12 = (int *)(uVar5 + iVar14) + -2;
          piVar3 = *(int **)(uVar5 + iVar14);
          if (piVar12 == piVar3) {
            uVar15 = uVar15 | 1 << (iVar9 >> 2 & 0xffU);
            *(uint *)(uVar5 + 4) = uVar15;
          }
          else {
            do {
              if ((piVar3[1] & 0xfffffffcU) <= uVar2) break;
              piVar3 = (int *)piVar3[2];
            } while (piVar12 != piVar3);
            piVar12 = (int *)piVar3[3];
          }
          *(int **)(iVar18 + 0xc) = piVar12;
          *(int **)(iVar18 + 8) = piVar3;
          piVar12[2] = iVar18;
/* ... truncated ... */
```

## `FUN_0003782c` @ `0003782c` score `28`

- reasons: 0xf0, channel nibble mask, status shift >>4, nibble compose <<4, data byte 1, multi-param handler

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

## `FUN_00005f2c` @ `00005f2c` score `27`

- reasons: 0x80, channel nibble mask, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_00037674` @ `00037674` score `27`

- reasons: channel nibble mask, status shift >>4, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_0003bb58` @ `0003bb58` score `27`

- reasons: exact 0x8f, 0x90, multi-param handler

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

## `FUN_0005fa24` @ `0005fa24` score `27`

- reasons: channel nibble mask, status shift >>4, data byte 1, data byte 2, byte 3, multi-param handler

```c

void FUN_0005fa24(undefined4 *param_1,undefined4 *param_2,uint param_3)

{
  undefined4 *puVar1;
  undefined4 *puVar2;
  uint uVar3;
  uint uVar4;
  int iVar5;
  uint uVar6;
  undefined4 *puVar7;
  bool bVar8;
  
  if ((param_2 < param_1) && (puVar2 = (undefined4 *)((int)param_2 + param_3), param_1 < puVar2)) {
    uVar6 = (int)param_1 + param_3;
    if (3 < param_3) {
      uVar3 = param_3;
      if (((uVar6 | (uint)puVar2) & 3) != 0) goto LAB_0005fa44;
      do {
        *(undefined4 *)((int)param_1 + (uVar3 - 4)) = *(undefined4 *)((int)param_2 + (uVar3 - 4));
        uVar3 = uVar3 - 4;
      } while (3 < uVar3);
      iVar5 = (param_3 >> 2) - 1;
      param_3 = param_3 & 3;
      puVar2 = puVar2 + (-1 - iVar5);
      uVar6 = (uVar6 + iVar5 * -4) - 4;
    }
    if (param_3 == 0) {
      return;
    }
LAB_0005fa44:
    param_3 = param_3 - 1;
    uVar3 = ~param_3;
    do {
      *(undefined1 *)(uVar6 + uVar3 + param_3) = *(undefined1 *)((int)puVar2 + param_3 + uVar3);
      bVar8 = param_3 != 0;
      param_3 = param_3 - 1;
    } while (bVar8);
    return;
  }
  if (3 < param_3) {
    uVar6 = ((uint)param_2 | (uint)param_1) & 3;
    if ((((uint)param_2 | (uint)param_1) & 3) != 0) goto LAB_0005fa64;
    if (0xf < param_3) {
      iVar5 = (param_3 >> 4) - 1;
      puVar7 = param_1 + iVar5 * 4 + 4;
      puVar2 = param_2;
      do {
        *param_1 = *puVar2;
        param_1[1] = puVar2[1];
        param_1[2] = puVar2[2];
        puVar1 = puVar2 + 3;
        puVar2 = puVar2 + 4;
        param_1[3] = *puVar1;
        param_1 = param_1 + 4;
      } while (param_1 != puVar7);
      uVar3 = param_3 & 0xf;
      uVar4 = param_3 & 0xc;
      param_2 = param_2 + iVar5 * 4 + 4;
      param_3 = uVar3;
      if (uVar4 == 0) goto LAB_0005fa5e;
    }
    do {
      *(undefined4 *)((int)param_1 + uVar6) = *(undefined4 *)((int)param_2 + uVar6);
      uVar6 = uVar6 + 4;
    } while (3 < param_3 - uVar6);
    param_2 = param_2 + (param_3 >> 2);
    param_1 = param_1 + (param_3 >> 2);
    param_3 = param_3 & 3;
  }
LAB_0005fa5e:
  if (param_3 == 0) {
    return;
  }
LAB_0005fa64:
  uVar6 = 0;
  do {
    *(undefined1 *)((int)param_1 + uVar6) = *(undefined1 *)((int)param_2 + uVar6);
    uVar6 = uVar6 + 1;
  } while (param_3 != uVar6);
  return;
}
```

## `FUN_0000455c` @ `0000455c` score `26`

- reasons: 0x7f, channel nibble mask, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_0000657c` @ `0000657c` score `26`

- reasons: 0x7f, channel nibble mask, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_0005c310` @ `0005c310` score `26`

- reasons: 0x80, 0x7f, channel nibble mask, data byte 1, multi-param handler

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

## `FUN_0005ef68` @ `0005ef68` score `26`

- reasons: 0x7f, channel nibble mask, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_00004e3a` @ `00004e3a` score `25`

- reasons: 0xf7, 0x78, channel nibble mask, data byte 1, data byte 2, byte 3

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

## `FUN_00036814` @ `00036814` score `25`

- reasons: channel nibble mask, status shift >>4, data byte 1, data byte 2, multi-param handler

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

## `FUN_00037498` @ `00037498` score `25`

- reasons: 0xf7, channel nibble mask, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_00041554` @ `00041554` score `25`

- reasons: 0xf7, channel nibble mask, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_0004763c` @ `0004763c` score `25`

- reasons: 0x80, channel nibble mask, data byte 1, data byte 2, multi-param handler

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

## `FUN_0005567c` @ `0005567c` score `25`

- reasons: 0x90, channel nibble mask, data byte 1, data byte 2, multi-param handler

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

## `FUN_0005b52c` @ `0005b52c` score `25`

- reasons: 0x80, 0x7f, channel nibble mask, nibble compose <<4, multi-param handler

```c

ulonglong FUN_0005b52c(uint param_1,uint param_2,uint param_3,uint param_4)

{
  int iVar1;
  int iVar2;
  undefined4 uVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  uint uVar7;
  int iVar8;
  int iVar9;
  uint uVar10;
  uint uVar11;
  uint uVar12;
  uint uVar13;
  uint uVar14;
  bool bVar15;
  bool bVar16;
  undefined8 uVar17;
  ulonglong uVar18;
  
  iVar2 = DAT_0005b8e8;
  iVar1 = DAT_0005b71c;
  iVar8 = DAT_0005b658;
  iVar9 = DAT_0005b5f8;
  if ((int)param_4 < 0) {
    if ((int)param_2 < 0) {
      param_2 = ~param_2;
      if (-param_1 == 0) {
        param_2 = param_2 + 1;
      }
      param_4 = ~param_4;
      if (-param_3 == 0) {
        param_4 = param_4 + 1;
      }
      uVar18 = FUN_0005b5b4(-param_1,param_2,-param_3,param_4);
      return uVar18;
    }
    uVar17 = FUN_0005b5b4();
    uVar7 = ~(uint)((ulonglong)uVar17 >> 0x20);
    if (-(int)uVar17 == 0) {
      uVar7 = uVar7 + 1;
    }
    return CONCAT44(uVar7,-(int)uVar17);
  }
  if ((param_4 == 0) && (param_3 == 0)) {
    if (param_1 == 0) {
      uVar3 = 0;
      uVar7 = 0;
      if (param_2 == 0) goto LAB_0005b56e;
    }
    uVar3 = 0;
    uVar7 = param_2 & 0x80000000;
    if (uVar7 == 0) {
      uVar3 = 0xffffffff;
      uVar7 = 0x7fffffff;
    }
LAB_0005b56e:
    uVar18 = FUN_0005ffc8(uVar3,uVar7);
    return uVar18;
  }
  if ((int)param_2 < 0) {
    param_2 = ~param_2;
    if (-param_1 == 0) {
      param_2 = param_2 + 1;
    }
    uVar17 = FUN_0005b5b4(-param_1,param_2);
    uVar7 = ~(uint)((ulonglong)uVar17 >> 0x20);
    if (-(int)uVar17 == 0) {
      uVar7 = uVar7 + 1;
    }
    return CONCAT44(uVar7,-(int)uVar17);
  }
  if (param_2 == 0) {
    if (param_4 != 0) {
      return 0;
    }
    if (param_3 != 0) {
      *(uint *)(DAT_0005b5f8 + 0x60) = param_1;
      *(uint *)(iVar9 + 100) = param_3;
      return (ulonglong)*(uint *)(iVar9 + 0x70);
    }
    uVar3 = 0;
    if (param_1 == 0) goto LAB_0005b5e2;
  }
  else {
    if (param_4 != 0) {
      if (param_4 >> 0x10 != 0) {
        uVar7 = 0;
        if (param_4 + 1 != 0) {
          *(uint *)(DAT_0005b8e8 + 100) = param_4 + 1;
          *(uint *)(iVar2 + 0x60) = param_2;
          uVar7 = *(uint *)(iVar2 + 0x70);
        }
        uVar10 = uVar7 * (param_3 & 0xffff);
        uVar6 = param_1 - uVar10;
        uVar11 = uVar7 * (param_3 >> 0x10);
        uVar10 = (((param_2 - uVar7 * (param_4 & 0xffff)) - (uint)(param_1 < uVar10)) -
                 (uVar7 * (param_4 >> 0x10) * 0x10000 | uVar11 >> 0x10)) -
                 (uint)(uVar6 < uVar11 * 0x10000);
        for (uVar6 = uVar6 + uVar11 * -0x10000;
            (param_4 <= uVar10 && ((uVar10 != param_4 || (param_3 <= uVar6))));
            uVar6 = uVar6 - param_3) {
          uVar10 = (uVar10 - param_4) - (uint)(uVar6 < param_3);
          uVar7 = uVar7 + 1;
        }
        return (ulonglong)uVar7;
      }
      uVar10 = 0;
      uVar7 = param_3;
      uVar6 = param_4;
      if (param_4 >> 8 == 0) {
        uVar6 = param_4 << 8 | param_3 >> 0x18;
        uVar7 = param_3 << 8;
        uVar10 = 8;
      }
      if (uVar6 >> 0xc == 0) {
        uVar6 = uVar6 << 4 | uVar7 >> 0x1c;
        uVar7 = uVar7 << 4;
        uVar10 = uVar10 + 4;
      }
      if (uVar6 >> 0xe == 0) {
        uVar6 = uVar6 << 2 | uVar7 >> 0x1e;
        uVar7 = uVar7 << 2;
        uVar10 = uVar10 + 2;
      }
      if (uVar6 >> 0xf == 0) {
        bVar15 = CARRY4(uVar7,uVar7);
        uVar7 = uVar7 * 2;
        uVar6 = uVar6 * 2 + (uint)bVar15;
        uVar10 = uVar10 + 1;
      }
      *(uint *)(DAT_0005b8e8 + 100) = uVar6 * 2 + (uint)CARRY4(uVar7,uVar7) + 1;
      *(undefined4 *)(iVar2 + 0x60) = DAT_0005b8ec;
      iVar9 = *(int *)(iVar2 + 0x70);
      uVar11 = iVar9 * (param_2 >> 0x10) >> 0x10;
      uVar12 = uVar11 * (uVar7 & 0xffff);
      if (param_1 < uVar12) {
        param_2 = param_2 - 1;
      }
      uVar4 = (param_1 - uVar12) - uVar12;
      if (param_1 - uVar12 < uVar12) {
        param_2 = param_2 - 1;
      }
      uVar13 = uVar11 * (uVar7 >> 0x10);
      uVar12 = uVar4 + uVar13 * -0x20000;
      uVar4 = ((param_2 + uVar11 * (uVar6 & 0xffff) * -2) - (uVar13 >> 0xf)) -
              (uint)(uVar4 < uVar13 * 0x20000);
      uVar13 = iVar9 * (uVar4 >> 3) >> 0x10;
      if (uVar10 < 0xc) {
        uVar7 = uVar13 >> (0xc - uVar10 & 0xff);
        iVar9 = (uVar11 << uVar10) * 2;
      }
      else {
        uVar14 = uVar13 * (uVar7 >> 0xc & 0xffff);
        uVar5 = uVar12 - uVar14;
        if (uVar12 < uVar14) {
          uVar4 = uVar4 - 1;
        }
        uVar7 = uVar13 * ((uVar7 >> 0xc | uVar6 << 0x14) >> 0x10);
        uVar12 = uVar5 + uVar7 * -0x10000;
        uVar4 = ((uVar4 - uVar13 * (uVar6 >> 0xc & 0xffff)) - (uVar7 >> 0x10)) -
                (uint)(uVar5 < uVar7 * 0x10000);
        uVar7 = iVar9 * (uVar12 >> 0x16 | uVar4 * 0x400) >> (0x29 - uVar10 & 0xff);
        iVar9 = uVar11 * 0x2000 + uVar13 << (uVar10 - 0xc & 0xff);
      }
      uVar11 = uVar7 * (param_3 & 0xffff);
      uVar6 = uVar12 - uVar11;
      uVar13 = uVar7 * (param_3 >> 0x10);
      uVar10 = uVar6 + uVar13 * -0x10000;
      uVar6 = (((uVar4 - uVar7 * (param_4 & 0xffff)) - (uint)(uVar12 < uVar11)) - (uVar13 >> 0x10))
              - (uint)(uVar6 < uVar13 * 0x10000);
      uVar7 = iVar9 + uVar7;
      do {
        uVar12 = uVar7;
        bVar16 = param_3 <= uVar10;
        uVar10 = uVar10 - param_3;
        uVar11 = uVar6 - param_4;
/* ... truncated ... */
```

## `FUN_00002b44` @ `00002b44` score `24`

- reasons: 0x80, 0x90, channel nibble mask, data byte 1

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00002b44(void)

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
    if ((uVar4 + 1 & 0xffff) < 0x100) goto LAB_00002e3e;
  }
  _DAT_20005a54 = 0;
  DAT_20005a57 = '\x01';
LAB_00002e3e:
  if ((short)((uint)_DAT_20005a2c >> 8) < -0x1e) {
    FUN_00002ac8(0);
    FUN_0000a568(0x2000462c,0,0x200);
    _DAT_20005a2c = 0;
    bVar3 = DAT_20005a56;
  }
  if (1 < bVar3) {
    if ((short)((uint)_DAT_20005a30 >> 8) < -0x1e) {
      FUN_00002ac8(1);
      FUN_0000a568(0x2000482c,0,0x200);
      _DAT_20005a30 = 0;
      bVar3 = DAT_20005a56;
    }
    if (2 < bVar3) {
      if ((short)((uint)_DAT_20005a34 >> 8) < -0x1e) {
        FUN_00002ac8(2);
        FUN_0000a568(0x20004a2c,0,0x200);
        _DAT_20005a34 = 0;
        bVar3 = DAT_20005a56;
      }
      if (3 < bVar3) {
        if ((short)((uint)_DAT_20005a38 >> 8) < -0x1e) {
          FUN_00002ac8(3);
          FUN_0000a568(0x20004c2c,0,0x200);
          _DAT_20005a38 = 0;
          bVar3 = DAT_20005a56;
/* ... truncated ... */
```

## `FUN_00004914` @ `00004914` score `24`

- reasons: 0x78, channel nibble mask, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_000365f0` @ `000365f0` score `24`

- reasons: channel nibble mask, status shift >>4, nibble compose <<4, data byte 2, multi-param handler

```c

int FUN_000365f0(int param_1,uint param_2)

{
  uint uVar1;
  undefined4 uVar2;
  uint uVar3;
  int iVar4;
  int iVar5;
  undefined4 *puVar6;
  undefined4 *puVar7;
  
  uVar1 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
  if (uVar1 == 0) {
    uVar1 = 1;
  }
  else {
    uVar3 = 0;
    iVar4 = *(int *)(param_1 + 0xc);
    do {
      if (((*(byte *)(iVar4 + 7) & 2) != 0) && ((*(uint *)(iVar4 + 4) & 0xffffff) == param_2))
      break;
      uVar3 = uVar3 + 1;
      iVar4 = iVar4 + 8;
    } while (uVar3 < uVar1);
    if (uVar1 != uVar3) {
      return uVar3 * 8 + *(int *)(param_1 + 0xc);
    }
    uVar1 = uVar1 + 1 & 0x3f;
  }
  uVar3 = *(ushort *)(param_1 + 0x2a) & DAT_000366c8;
  *(ushort *)(param_1 + 0x2a) = (ushort)uVar3 | (ushort)(uVar1 << 4);
  if ((uVar3 & 0x3f0) != 0 || uVar1 != 0) {
    iVar4 = FUN_0004cef4(*(undefined4 *)(param_1 + 0xc),uVar1 << 3);
    *(int *)(param_1 + 0xc) = iVar4;
    uVar1 = (*(ushort *)(param_1 + 0x2a) & 0x3ff) >> 4;
    iVar5 = uVar1 - 1;
    if (uVar1 != 1) {
      FUN_0005fa24(iVar4 + ((iVar5 - uVar1) + 2) * 8,iVar4 + ((iVar5 - uVar1) + DAT_000366dc) * 8,
                   iVar5 * 8);
    }
    FUN_00050350(iVar4,0,8);
    puVar7 = *(undefined4 **)(param_1 + 0xc);
    uVar2 = FUN_0004cea4(0xc);
    puVar6 = *(undefined4 **)(param_1 + 0xc);
    *puVar7 = uVar2;
    FUN_00047564(*puVar6);
    iVar4 = *(int *)(param_1 + 0xc);
    *(uint *)(iVar4 + 4) = (uint)(*(byte *)(iVar4 + 7) | 2) << 0x18 | param_2 & 0xffffff;
    return iVar4;
  }
  FUN_000468e8(3,DAT_000366d8,0x2e8,DAT_000366d4,DAT_000366d0,DAT_000366cc);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

## `FUN_0005ed60` @ `0005ed60` score `24`

- reasons: 0x80, 0x7f, data byte 1, data byte 2, byte 3, multi-param handler

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

## `FUN_0005fdb0` @ `0005fdb0` score `24`

- reasons: 0x78, channel nibble mask, data byte 1, data byte 2, byte 3, multi-param handler

```c

void FUN_0005fdb0(undefined4 param_1,int param_2)

{
  int *piVar1;
  uint *puVar2;
  uint uVar3;
  int *piVar4;
  uint uVar5;
  int iVar6;
  int iVar7;
  uint uVar8;
  int iVar9;
  uint uVar10;
  int *piVar11;
  
  if (param_2 == 0) {
    return;
  }
  FUN_0005f7d8();
  iVar6 = DAT_0005ff70;
  piVar1 = (int *)(param_2 + -8);
  uVar10 = *(uint *)(param_2 + -4);
  uVar5 = uVar10 & 0xfffffffe;
  puVar2 = (uint *)((int)piVar1 + uVar5);
  uVar3 = puVar2[1] & 0xfffffffc;
  if (*(uint **)(DAT_0005ff70 + 8) == puVar2) {
    uVar5 = uVar5 + uVar3;
    if ((uVar10 & 1) == 0) {
      iVar7 = *piVar1;
      piVar1 = (int *)((int)piVar1 - iVar7);
      iVar9 = piVar1[2];
      uVar5 = uVar5 + iVar7;
      iVar7 = piVar1[3];
      *(int *)(iVar9 + 0xc) = iVar7;
      *(int *)(iVar7 + 8) = iVar9;
    }
    piVar1[1] = uVar5 | 1;
    puVar2 = DAT_0005ff78;
    *(int **)(iVar6 + 8) = piVar1;
    if (*puVar2 <= uVar5) {
      FUN_0005fd00(param_1,*DAT_0005ff7c);
    }
    goto LAB_0005fe3a;
  }
  puVar2[1] = uVar3;
  uVar8 = *(uint *)((int)puVar2 + uVar3 + 4) & 1;
  if ((uVar10 & 1) == 0) {
    iVar7 = *piVar1;
    piVar1 = (int *)((int)piVar1 - iVar7);
    uVar5 = uVar5 + iVar7;
    uVar10 = piVar1[2];
    if (uVar10 == DAT_0005ff74) {
      if (uVar8 == 0) {
        uVar3 = uVar3 + uVar5;
        uVar5 = puVar2[2];
        uVar10 = puVar2[3];
        *(uint *)(uVar5 + 0xc) = uVar10;
        *(uint *)(uVar10 + 8) = uVar5;
        piVar1[1] = uVar3 | 1;
        *(uint *)((int)piVar1 + uVar3) = uVar3;
      }
      else {
        piVar1[1] = uVar5 | 1;
        *puVar2 = uVar5;
      }
      goto LAB_0005fe3a;
    }
    iVar7 = piVar1[3];
    *(int *)(uVar10 + 0xc) = iVar7;
    *(uint *)(iVar7 + 8) = uVar10;
    if (uVar8 == 0) goto LAB_0005fe4a;
    piVar1[1] = uVar5 | 1;
    *puVar2 = uVar5;
  }
  else if (uVar8 == 0) {
LAB_0005fe4a:
    uVar5 = uVar5 + uVar3;
    uVar3 = puVar2[2];
    if (uVar3 == DAT_0005ff74) {
      *(int **)(uVar3 + 0xc) = piVar1;
      *(int **)(uVar3 + 8) = piVar1;
      piVar1[3] = uVar3;
      piVar1[2] = uVar3;
      piVar1[1] = uVar5 | 1;
      *(uint *)((int)piVar1 + uVar5) = uVar5;
      goto LAB_0005fe3a;
    }
    uVar10 = puVar2[3];
    *(uint *)(uVar3 + 0xc) = uVar10;
    *(uint *)(uVar10 + 8) = uVar3;
    piVar1[1] = uVar5 | 1;
    *(uint *)((int)piVar1 + uVar5) = uVar5;
  }
  else {
    *(uint *)(param_2 + -4) = uVar10 | 1;
    *puVar2 = uVar5;
  }
  if (uVar5 < 0x200) {
    *(uint *)(iVar6 + 4) = 1 << (uVar5 >> 5 & 0xff) | *(uint *)(iVar6 + 4);
    iVar6 = (uVar5 & 0xfffffff8) + iVar6;
    iVar7 = *(int *)(iVar6 + 8);
    piVar1[3] = iVar6;
    piVar1[2] = iVar7;
    *(int **)(iVar6 + 8) = piVar1;
    *(int **)(iVar7 + 0xc) = piVar1;
  }
  else {
    uVar3 = uVar5 >> 9;
    if (uVar3 < 5) {
      iVar7 = (uVar5 >> 6) + 0x38;
      iVar9 = ((uVar5 >> 6) + 0x39) * 8;
    }
    else if (uVar3 < 0x15) {
      iVar7 = uVar3 + 0x5b;
      iVar9 = (uVar3 + 0x5c) * 8;
    }
    else if (uVar3 < 0x55) {
      iVar7 = (uVar5 >> 0xc) + 0x6e;
      iVar9 = ((uVar5 >> 0xc) + 0x6f) * 8;
    }
    else if (uVar3 < 0x155) {
      iVar7 = (uVar5 >> 0xf) + 0x77;
      iVar9 = ((uVar5 >> 0xf) + 0x78) * 8;
    }
    else if (DAT_0005ff80 < uVar3) {
      iVar7 = 0x7e;
      iVar9 = 0x3f8;
    }
    else {
      iVar7 = (uVar5 >> 0x12) + 0x7c;
      iVar9 = ((uVar5 >> 0x12) + 0x7d) * 8;
    }
    piVar4 = *(int **)(iVar6 + iVar9);
    piVar11 = (int *)(iVar6 + iVar9) + -2;
    if (piVar11 == piVar4) {
      *(uint *)(iVar6 + 4) = 1 << (iVar7 >> 2 & 0xffU) | *(uint *)(iVar6 + 4);
    }
    else {
      do {
        if ((piVar4[1] & 0xfffffffcU) <= uVar5) break;
        piVar4 = (int *)piVar4[2];
      } while (piVar11 != piVar4);
      piVar11 = (int *)piVar4[3];
    }
    piVar1[3] = (int)piVar11;
    piVar1[2] = (int)piVar4;
    piVar11[2] = (int)piVar1;
    piVar4[3] = (int)piVar1;
  }
LAB_0005fe3a:
  FUN_0005f7e8(param_1);
  return;
}
```

## `FUN_00004be8` @ `00004be8` score `22`

- reasons: 0x78, channel nibble mask, data byte 1, data byte 2, multi-param handler

```c

undefined4 FUN_00004be8(int param_1,int *param_2)

{
  byte bVar1;
  ushort uVar2;
  int iVar3;
  ushort *puVar4;
  int iVar5;
  uint uVar6;
  uint uVar7;
  int iVar8;
  int iVar9;
  
  uVar6 = (uint)*(byte *)(*(int **)(param_1 + 0x78) + 4);
  if (uVar6 != 0) {
    iVar8 = *(int *)(param_1 + 0x10);
    iVar9 = *(int *)(param_1 + 0x14);
    iVar3 = *param_2;
    iVar5 = 0;
    bVar1 = *(byte *)(param_2 + 2);
    puVar4 = (ushort *)(**(int **)(param_1 + 0x78) + 2);
    do {
      uVar2 = *puVar4;
      puVar4 = puVar4 + 3;
      uVar7 = ((uint)uVar2 * (uint)*(ushort *)((int)param_2 + 6)) / (uint)*(ushort *)(param_2 + 1);
      *(short *)(iVar8 + iVar5) = (short)uVar7;
      *(short *)(iVar9 + iVar5) = (short)(((uint)bVar1 * (uVar7 & 0xffff)) / 100);
      uVar7 = ((uint)*(ushort *)(iVar8 + iVar5) * (uint)*(ushort *)(iVar3 + iVar5)) / 100;
      *(short *)(iVar8 + iVar5) = (short)uVar7;
      *(short *)(iVar9 + iVar5) = (short)(((uint)bVar1 * (uVar7 & 0xffff)) / 100);
      iVar5 = iVar5 + 2;
    } while (uVar6 * 2 != iVar5);
  }
  return 0;
}
```

## `FUN_00005e18` @ `00005e18` score `22`

- reasons: 0x80, channel nibble mask, data byte 1, data byte 2

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00005e18(short *param_1)

{
  short sVar1;
  bool bVar2;
  uint *puVar3;
  short sVar4;
  uint uVar5;
  uint uVar6;
  int iVar7;
  
  uVar6 = DAT_00005eec;
  uVar5 = 0;
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    uVar5 = isIRQinterruptsEnabled();
  }
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    enableIRQinterrupts(1);
  }
  if (_DAT_200061b8 == 0) {
    DAT_40040d03 = 0x40;
  }
  _DAT_200061b8 = _DAT_200061b8 + 1;
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    enableIRQinterrupts((uVar5 & 1) == 1);
  }
  sVar1 = *param_1;
  if (sVar1 != 0) {
    sVar4 = 0;
    puVar3 = *(uint **)(param_1 + 2);
    do {
      uVar5 = *puVar3;
      iVar7 = ((uint)(ushort)((ushort)puVar3[1] >> 8) * 0x10 + ((ushort)puVar3[1] & 0xff)) * 4;
      if ((uVar5 & 0x10000) != 0) {
        *(uint *)(&DAT_40040800 + iVar7) = *(uint *)(&DAT_40040800 + iVar7) & uVar6;
        *(uint *)(&DAT_40040800 + iVar7) = uVar5 & uVar6;
      }
      sVar4 = sVar4 + 1;
      *(uint *)(&DAT_40040800 + iVar7) = uVar5;
      puVar3 = puVar3 + 2;
    } while (sVar4 != sVar1);
  }
  uVar6 = 0;
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    uVar6 = isIRQinterruptsEnabled();
  }
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    enableIRQinterrupts(1);
  }
  if (_DAT_200061b8 != 0) {
    _DAT_200061b8 = _DAT_200061b8 + -1;
  }
  if (_DAT_200061b8 == 0) {
    DAT_40040d03 = 0x80;
  }
  bVar2 = (bool)isCurrentModePrivileged();
  if (bVar2) {
    enableIRQinterrupts((uVar6 & 1) == 1);
  }
  return;
}
```

## `FUN_000437a8` @ `000437a8` score `22`

- reasons: 0x80, 0x7f, channel nibble mask, multi-param handler

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

## `FUN_0005ba44` @ `0005ba44` score `22`

- reasons: 0x80, 0x7f, channel nibble mask, multi-param handler

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

## `FUN_0005cbe8` @ `0005cbe8` score `22`

- reasons: 0x78, channel nibble mask, data byte 1, data byte 2, multi-param handler

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
            local_54 = local_54 + 1;
            pbVar3 = pbVar9;
            if ((int)uVar14 < 0) {
              uVar17 = 2;
              uVar14 = -uVar14;
              uVar8 = (uint)param_4[2];
              pbVar6 = param_4 + 3;
            }
            else {
              uVar8 = (uint)param_4[2];
              pbVar6 = param_4 + 3;
            }
          }
        }
        pbVar15 = pbVar6;
        local_50 = 0;
        if (uVar8 == 0x2e) {
          local_50 = 0;
          uVar17 = uVar17 | 0x400;
          uVar8 = (uint)pbVar3[1];
          if (uVar8 - 0x30 < 10) {
            local_50 = 0;
            do {
              pbVar9 = pbVar15;
              pbVar15 = pbVar9 + 1;
              iVar10 = local_50 * 10 + uVar8;
              uVar8 = (uint)*pbVar15;
              local_50 = iVar10 - 0x30;
            } while (uVar8 - 0x30 < 10);
            pbVar15 = pbVar9 + 2;
          }
          else if (uVar8 == 0x2a) {
            uVar8 = (uint)pbVar3[2];
            local_50 = *local_54;
            local_54 = local_54 + 1;
            local_50 = local_50 & (int)~local_50 >> 0x1f;
            pbVar15 = pbVar3 + 3;
          }
          else {
            pbVar15 = pbVar15 + 1;
          }
        }
        uVar11 = uVar8 - 0x68 & 0xff;
        if (uVar11 < 0x13) {
                    /* WARNING: Could not recover jumptable at 0x0005cc82. Too many branches */
                    /* WARNING: Treating indirect jump as call */
          uVar8 = (**(code **)(iVar5 + uVar11 * 4))();
          return uVar8;
        }
        if (uVar8 < 0x68) {
          if ((0x24 < uVar8) && (uVar17 = uVar8 - 0x25 & 0xff, uVar17 < 0x43)) {
                    /* WARNING: Could not recover jumptable at 0x0005ccd0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
            uVar8 = (**(code **)(DAT_0005cf18 + uVar17 * 4))();
            return uVar8;
          }
          goto LAB_0005cc22;
        }
        uVar11 = uVar8 - 0x69 & 0xff;
        if (0xf < uVar11) goto LAB_0005cc22;
        local_48 = DAT_0005cf1c & 1 << uVar11;
        if ((1 << uVar11 & DAT_0005cf1c) == 0) {
          if (uVar11 == 10) {
            pcVar12 = (char *)*local_54;
            puVar18 = local_54 + 1;
            uVar8 = local_50;
            if (local_50 == 0) {
              uVar8 = 0xffffffff;
            }
            cVar7 = *pcVar12;
            pcVar13 = pcVar12;
            if (cVar7 == '\0') {
              local_44 = uVar17 & 0x400;
              if ((uVar17 & 0x400) == 0) {
                local_54 = (uint *)(uVar17 & 2);
                if ((uVar17 & 2) == 0) goto LAB_0005d2a6;
              }
              else {
                if (-1 < (int)(uVar17 << 0x1e)) {
                  local_54 = (uint *)0x400;
LAB_0005d2a6:
                  local_44 = 0;
                  uVar17 = uVar16;
                  if (uVar14 != 0) goto LAB_0005d110;
                  goto LAB_0005cc2c;
                }
                local_44 = 0;
              }
            }
            else {
              do {
                if (pcVar12 + uVar8 == pcVar13) {
                  local_44 = (int)(pcVar12 + uVar8) - (int)pcVar12;
                  goto LAB_0005cdec;
                }
                pcVar1 = pcVar13 + 1;
                pcVar13 = pcVar13 + 1;
              } while (*pcVar1 != '\0');
              local_44 = (int)pcVar13 - (int)pcVar12;
LAB_0005cdec:
/* ... truncated ... */
```

## `FUN_0005d780` @ `0005d780` score `22`

- reasons: 0x80, 0x90, 0x78, data byte 1, multi-param handler

```c

undefined4 FUN_0005d780(int param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)

{
  int iVar1;
  int iVar2;
  undefined4 *puVar3;
  undefined4 uVar4;
  
  if (param_1 == 0) {
    FUN_0005da08();
    iVar1 = DAT_0005d800;
    *(undefined4 *)(DAT_0005d800 + 0x78) = 0xc;
    FUN_00059d0c(5,DAT_0005d804,0xff);
    iVar2 = DAT_0005d808;
    FUN_0005beec(DAT_0005d808,0,0x40);
    *(undefined2 *)(iVar2 + 0x18) = 0x40;
    puVar3 = DAT_0005d80c;
    *(undefined1 *)(iVar2 + 1) = 1;
    *(undefined4 **)(iVar2 + 8) = puVar3;
    *puVar3 = 0;
    *(undefined1 *)(iVar2 + 0x21) = 0;
    *(undefined2 *)(iVar2 + 0x22) = 0x80;
    *(undefined2 *)(iVar2 + 0x38) = 0x40;
    uVar4 = DAT_0005d810;
    *(undefined1 *)(iVar2 + 0x3b) = 0;
    puVar3 = DAT_0005d814;
    *(undefined4 *)(iVar2 + 4) = 0;
    *(undefined4 *)(iVar2 + 0xc) = uVar4;
    *(undefined4 **)(iVar2 + 0x28) = puVar3;
    *puVar3 = 0;
    *(undefined4 *)(iVar2 + 0x24) = 0;
    *(undefined4 *)(iVar2 + 0x2c) = uVar4;
    FUN_0005ffa8();
    *(undefined4 *)(iVar1 + 0x40) = 1;
    *(undefined4 *)(iVar1 + 0x4c) = 0x20000000;
    *(undefined4 *)(iVar1 + 0x90) = DAT_0005d818;
    *(undefined4 *)(DAT_0005d81c + 0x4c) = 0x10000;
    return 1;
  }
                    /* WARNING: Subroutine does not return */
  FUN_0005d354(DAT_0005d828,0x163,DAT_0005d824,DAT_0005d820,param_4);
}
```

