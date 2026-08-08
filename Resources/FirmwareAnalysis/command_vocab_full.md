# Motion 32 — command vocabulary and configuration block

Program: `motionupgrade.bin`  
Image base: `00000000`

Recovers users of the queue addresses via **literal-pool scanning**, because
`getReferencesTo` returns nothing for them — Thumb loads addresses from PC-
relative pools and the inbound queue is probably `outbound + 0x1c`.

## 1. Who actually uses each address (literal-pool scan)

### `0x20004084`

Literal-pool words holding this value: **0**

Functions loading it: **0**

### `0x200040a0`

Literal-pool words holding this value: **0**

Functions loading it: **0**

### `0x20004324`

Literal-pool words holding this value: **0**

Functions loading it: **0**

### `0x200045ca`

Literal-pool words holding this value: **0**

Functions loading it: **0**

### `0x200045cc`

Literal-pool words holding this value: **0**

Functions loading it: **0**

### `0x20004538`

Literal-pool words holding this value: **0**

Functions loading it: **0**

### `0x20005d24`

Literal-pool words holding this value: **0**

Functions loading it: **0**

### `0x20005cd4`

Literal-pool words holding this value: **0**

Functions loading it: **0**

## 2. The configuration block, whole

`0x95f4` = `F0 08 26 05` (Motion 32), `0x95f8` = `F0 08 24 05` (Motion 16),
then the per-variant tables. Dumped in full so the variant count is a fact.

```text
00009500: c2 58 02 49 0a 40 c2 50 c3 58 70 47 ff ff fe ff 
00009510: 03 00 46 f2 00 02 10 b5 c0 33 c4 f2 00 02 9b 00 
00009520: 99 58 09 4c 21 40 99 50 9b 58 bf f3 5f 8f 1f 21 
00009530: 01 22 01 40 8a 40 4e f2 00 11 43 09 60 33 ce f2 
00009540: 00 01 9b 00 5a 50 10 bd ff ff fe ff f0 b5 c6 46 
00009550: 90 46 4e f2 00 12 ff 24 03 25 ce f2 00 02 94 46 
00009560: 22 00 40 f2 00 37 05 40 ed 00 89 01 aa 40 0c 40 
00009570: ac 40 83 08 9b 00 63 44 de 59 00 b5 96 43 26 43 
00009580: de 51 46 f2 bc 13 42 46 c2 f2 00 03 80 00 1a 50 
00009590: 80 bc b8 46 f0 bd c0 46 03 00 46 f2 00 02 10 b5 
000095a0: c0 33 c4 f2 00 02 9b 00 99 58 0b 4c 21 40 99 50 
000095b0: 9b 58 bf f3 5f 8f 1f 22 01 23 02 40 93 40 4e f2 
000095c0: 00 12 ce f2 00 02 94 46 40 f2 80 12 40 09 80 00 
000095d0: 60 44 83 50 03 60 10 bd ff ff fe ff 1f 21 01 22 
000095e0: 01 40 8a 40 4e f2 00 11 43 09 20 33 ce f2 00 01 
000095f0: 9b 00 5a 50 bf f3 4f 8f bf f3 6f 8f 70 47 c0 46 
00009600: f0 b5 c6 46 90 46 4e f2 00 12 ff 24 03 25 ce f2 
00009610: 00 02 94 46 22 00 40 f2 00 37 05 40 ed 00 89 01 
00009620: aa 40 0c 40 ac 40 83 08 9b 00 63 44 de 59 00 b5 
00009630: 96 43 26 43 de 51 46 f2 bc 13 42 46 81 00 c2 f2 
00009640: 00 03 5a 50 03 00 46 f2 00 02 c0 33 c4 f2 00 02 
00009650: 9b 00 99 58 0c 4c 21 40 99 50 9b 58 bf f3 5f 8f 
00009660: 1f 22 01 23 02 40 93 40 4e f2 00 12 ce f2 00 02 
00009670: 94 46 40 f2 80 12 40 09 80 00 60 44 83 50 03 60 
00009680: 80 bc b8 46 f0 bd c0 46 ff ff fe ff 46 f2 00 00 
00009690: 00 23 c4 f2 00 00 49 f6 64 22 c0 f2 00 02 9a 18 
000096a0: 12 78 1a b1 19 00 c0 31 89 00 0a 50 01 33 20 2b 
000096b0: f1 d1 70 47 30 b5 ef f3 10 81 01 23 83 f3 10 88 
000096c0: 46 f2 3c 23 40 00 c2 f2 00 03 1a 5a 1a b1 1a 5a 
000096d0: 01 3a 92 b2 1a 52 1b 5a 83 b9 4e f2 00 02 49 f6 
000096e0: 78 33 40 f2 fe 34 c4 f2 01 02 c0 f2 00 03 15 5b 
000096f0: 18 5a 04 4b 2b 43 83 43 9b b2 13 53 81 f3 10 88 
00009700: 30 bd c0 46 00 a5 ff ff 70 b5 ef f3 10 81 01 23 
00009710: 83 f3 10 88 46 f2 3c 22 40 00 c2 f2 00 02 13 5a 
00009720: 83 b9 4e f2 00 04 49 f6 78 35 40 f2 fe 36 c4 f2 
00009730: 01 04 c0 f2 00 05 a3 5b 2d 5a 2b 43 4a f2 00 55 
00009740: 2b 43 a3 53 13 5a 01 33 9b b2 13 52 81 f3 10 88 
00009750: 70 bd c0 46 00 be 70 47 10 b5 00 f0 03 f8 fa f7 
```

## 3. USB-MIDI code-index-number decode

`8F 00 7F` reaches the device as a 4-byte USB-MIDI packet whose header low
nibble is the CIN. For a Note Off that is **8**. If the firmware switches on the
CIN, the native-entry handler is one case of that switch and its siblings are the
rest of the host command surface.

Functions comparing against CIN values, ranked by how many distinct CINs they use
(a real dispatch touches several):

```text
FUN_00004690                 @ 00004690   CINs: 0x04 0x05 0x06 0x07 0x08 0x09 0x0e
FUN_00004914                 @ 00004914   CINs: 0x04 0x05 0x06 0x07 0x08 0x09 0x0b
FUN_00004e3a                 @ 00004e3a   CINs: 0x04 0x05 0x06 0x07 0x08 0x09 0x0e
FUN_00005854                 @ 00005854   CINs: 0x04 0x05 0x06 0x07 0x09 0x0b 0x0e
FUN_0002164c                 @ 0002164c   CINs: 0x04 0x05 0x06 0x07 0x08 0x09 0x0e
FUN_0005f274                 @ 0005f274   CINs: 0x04 0x05 0x06 0x07 0x08 0x09 0x0b
FUN_0000290c                 @ 0000290c   CINs: 0x04 0x05 0x06 0x07 0x08 0x09
FUN_00002b44                 @ 00002b44   CINs: 0x04 0x05 0x06 0x07 0x08 0x09
FUN_00021f24                 @ 00021f24   CINs: 0x04 0x05 0x06 0x07 0x08 0x0e
FUN_000348a4                 @ 000348a4   CINs: 0x04 0x05 0x06 0x07 0x08 0x09
FUN_0004ebe4                 @ 0004ebe4   CINs: 0x04 0x05 0x06 0x08 0x0b 0x0e
FUN_0000240c                 @ 0000240c   CINs: 0x04 0x05 0x06 0x07 0x08
FUN_00030468                 @ 00030468   CINs: 0x04 0x05 0x06 0x07 0x0e
FUN_00042388                 @ 00042388   CINs: 0x06 0x07 0x08 0x09 0x0e
FUN_0004e190                 @ 0004e190   CINs: 0x04 0x05 0x06 0x08 0x0b
FUN_000547c4                 @ 000547c4   CINs: 0x04 0x05 0x06 0x07 0x0e
FUN_0005b5b4                 @ 0005b5b4   CINs: 0x04 0x06 0x08 0x09 0x0e
FUN_0005cbe8                 @ 0005cbe8   CINs: 0x04 0x06 0x07 0x08 0x09
FUN_0005fdb0                 @ 0005fdb0   CINs: 0x04 0x05 0x06 0x08 0x09
FUN_000026f4                 @ 000026f4   CINs: 0x04 0x08 0x09 0x0b
FUN_00036b60                 @ 00036b60   CINs: 0x04 0x05 0x06 0x07
FUN_00038b1c                 @ 00038b1c   CINs: 0x04 0x05 0x06 0x08
FUN_00041554                 @ 00041554   CINs: 0x04 0x06 0x08 0x09
FUN_000443c8                 @ 000443c8   CINs: 0x04 0x05 0x07 0x08
FUN_00046bb0                 @ 00046bb0   CINs: 0x04 0x05 0x09 0x0e
FUN_0004fad4                 @ 0004fad4   CINs: 0x04 0x07 0x08 0x09
FUN_00050d0c                 @ 00050d0c   CINs: 0x04 0x05 0x07 0x08
FUN_00001b30                 @ 00001b30   CINs: 0x04 0x05 0x09
FUN_0000408c                 @ 0000408c   CINs: 0x04 0x07 0x0e
FUN_0000455c                 @ 0000455c   CINs: 0x07 0x0b 0x0e
FUN_00005e18                 @ 00005e18   CINs: 0x04 0x08 0x09
FUN_0000657c                 @ 0000657c   CINs: 0x05 0x06 0x08
FUN_00022b70                 @ 00022b70   CINs: 0x05 0x06 0x08
FUN_00027fb4                 @ 00027fb4   CINs: 0x04 0x05 0x06
FUN_0002ed0c                 @ 0002ed0c   CINs: 0x04 0x06 0x08
FUN_00039de4                 @ 00039de4   CINs: 0x05 0x08 0x09
FUN_0003a48c                 @ 0003a48c   CINs: 0x04 0x08 0x0e
FUN_0003d994                 @ 0003d994   CINs: 0x05 0x06 0x09
FUN_00043030                 @ 00043030   CINs: 0x04 0x05 0x08
FUN_00045c18                 @ 00045c18   CINs: 0x05 0x08 0x0b
```

### Decompilation of the top candidates

#### `FUN_00004690` @ `00004690`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

uint FUN_00004690(int *param_1,int *param_2)

{
  byte bVar1;
  undefined2 uVar2;
  int iVar3;
  uint uVar4;
  int iVar5;
  ushort *puVar6;
  byte *pbVar7;
  uint uVar8;
  ushort uVar9;
  short sVar10;
  int iVar11;
  int iVar12;
  int iVar13;
  int iVar14;
  int iVar15;
  int iVar16;
  int iVar17;
  undefined4 *puVar18;
  char cVar19;
  undefined2 *puVar20;
  char cVar21;
  int local_34;
  
  if (*param_1 == 0x544f5543) {
    return 0xe;
  }
  local_34 = param_2[1];
  param_1[0x1e] = (int)param_2;
  iVar5 = *param_2;
  if (iVar5 == 0) {
    if (local_34 != 0) {
      uVar8 = (uint)DAT_20005e7c;
      if (uVar8 < 3) {
        uVar4 = 0;
LAB_000047e0:
        param_1[0xe] = uVar8 * 2 + 0x20005e78;
        param_1[0xf] = uVar8 * 2 + 0x20005e74;
        DAT_20005e7c = (char)uVar8 + *(char *)((int)param_2 + 0x11);
        goto LAB_00004802;
      }
      cVar21 = *(char *)((int)param_2 + 0x11);
      uVar4 = 0;
      if (cVar21 != '\0') goto LAB_00004808;
    }
  }
  else {
    cVar21 = (char)param_2[4];
    uVar4 = (uint)DAT_20005f1a;
    if (uVar4 < 10) {
      iVar3 = uVar4 * 2;
      param_1[6] = iVar3 + 0x20005ee0;
      param_1[7] = iVar3 + 0x20005ecc;
      param_1[8] = iVar3 + 0x20005eb8;
      param_1[9] = uVar4 * 4 + 0x20005e94;
      param_1[10] = iVar3 + 0x20005e80;
      param_1[4] = iVar3 + 0x20005f08;
      DAT_20005f1a = DAT_20005f1a + cVar21;
      param_1[5] = iVar3 + 0x20005ef4;
    }
    bVar1 = *(byte *)((int)param_2 + 0x13);
    iVar3 = param_2[5];
    uVar4 = -(uint)(bVar1 == 0) & 3;
    if ((char)iVar3 == '\0') {
      uVar4 = 3;
    }
    uVar9 = *(ushort *)(param_2 + 6);
    if ((uVar9 != 0) && (uVar9 < bVar1)) {
      uVar4 = 3;
    }
    *(byte *)(param_1 + 0xb) = bVar1;
    *(char *)((int)param_1 + 0x2d) = (char)iVar3;
    uVar2 = *(undefined2 *)((int)param_2 + 0x16);
    *(ushort *)(param_1 + 0xc) = uVar9;
    *(undefined2 *)((int)param_1 + 0x2e) = uVar2;
    if (cVar21 != '\0') {
      iVar3 = param_1[6];
      puVar6 = (ushort *)(iVar5 + 2);
      iVar11 = param_1[7];
      iVar12 = param_1[8];
      iVar13 = param_1[9];
      iVar14 = param_1[10];
      iVar15 = param_1[4];
      cVar19 = '\0';
      iVar16 = param_1[5];
      iVar17 = 0;
      do {
        if (*puVar6 < puVar6[1]) {
          uVar4 = 3;
        }
        *(undefined2 *)(iVar3 + iVar17) = 0;
        *(undefined2 *)(iVar11 + iVar17) = 0;
        *(undefined2 *)(iVar12 + iVar17) = 0;
        *(undefined4 *)(iVar13 + iVar17 * 2) = 0;
        *(undefined2 *)(iVar14 + iVar17) = 0;
        cVar19 = cVar19 + '\x01';
        *(ushort *)(iVar15 + iVar17) = *puVar6;
        *(ushort *)(iVar16 + iVar17) = puVar6[1];
        puVar6 = puVar6 + 3;
        iVar17 = iVar17 + 2;
      } while (cVar19 != cVar21);
    }
    if (local_34 != 0) {
      uVar8 = (uint)DAT_20005e7c;
      if (uVar8 < 3) goto LAB_000047e0;
LAB_00004802:
      cVar21 = *(char *)((int)param_2 + 0x11);
      if (cVar21 != '\0') {
LAB_00004808:
        pbVar7 = (byte *)(local_34 + 4);
        cVar19 = '\0';
        puVar20 = (undefined2 *)param_1[0xf];
        do {
          if (7 < *pbVar7 - 3) {
            uVar4 = 3;
          }
          cVar19 = cVar19 + '\x01';
          *puVar20 = *(undefined2 *)(pbVar7 + 2);
          pbVar7 = pbVar7 + 8;
          puVar20 = puVar20 + 1;
        } while (cVar19 != cVar21);
      }
    }
    if (uVar4 != 0) goto LAB_00004836;
  }
  puVar18 = (undefined4 *)param_2[7];
  param_1[0x1f] = (int)puVar18;
  uVar4 = (**(code **)puVar18[2])(*puVar18,puVar18[1]);
  local_34 = param_2[1];
  iVar5 = *param_2;
LAB_00004836:
  uVar9 = (ushort)*(byte *)(*(int *)(param_2[7] + 4) + 0x18);
  if ((~*(byte *)(*(int *)(param_1[0x1f] + 4) + 5) & 3) == 0) {
    sVar10 = uVar9 * *(byte *)(*(int *)(param_2[7] + 4) + 0x19) * 4;
  }
  else {
    sVar10 = uVar9 << 1;
  }
  if (iVar5 != 0) {
    sVar10 = sVar10 + (ushort)*(byte *)(param_2 + 4) * 7 + 2;
  }
  if (local_34 != 0) {
    sVar10 = sVar10 + (ushort)*(byte *)((int)param_2 + 0x11) * 4 + 2;
  }
  *(short *)(&DAT_20005d98 + (uint)*(byte *)((int)param_2 + 0x1a) * 2) = sVar10 + 5;
  _DAT_20005d94 = param_1;
  *param_1 = 0x544f5543;
  return uVar4;
}


```

#### `FUN_00004914` @ `00004914`

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

#### `FUN_00004e3a` @ `00004e3a`

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
LAB_00005392:
                  in_stack_00000030._2_2_ = (undefined2)(uVar10 / uVar7);
                }
              }
              else {
                uVar10 = uVar10 * 2 - uVar23 & 0xffff;
                in_stack_00000030._2_2_ = 0x3ff;
                if (uVar10 <= uVar7 * 0x3ff) goto LAB_00005392;
              }
            }
          }
          else {
            in_stack_00000030._2_2_ = 0xffff;
          }
          *(undefined2 *)(*(int *)(unaff_r4 + 0x38) + iVar20) = in_stack_00000030._2_2_;
          uVar15 = in_stack_00000030._2_2_;
          if (iVar19 != 0) goto LAB_000050bc;
        }
        FUN_00003918(uStack00000000,(int)&stack0x00000030 + 2);
        *(undefined2 *)(*(int *)(unaff_r4 + 0x38) + uVar14 * 2) = in_stack_00000030._2_2_;
        uVar15 = in_stack_00000030._2_2_;
      }
LAB_000050bc:
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
    if (((((cVar2 != '\x01') && (uVar10 = uVar10 + _DAT_20005d9a & 0xffff, cVar2 != '\x02')) &&
         (uVar10 = uVar10 + _DAT_20005d9c & 0xffff, cVar2 != '\x03')) &&
        ((uVar10 = uVar10 + _DAT_20005d9e & 0xffff, cVar2 != '\x04' &&
         (uVar10 = uVar10 + _DAT_20005da0 & 0xffff, cVar2 != '\x05')))) &&
       ((uVar10 = uVar10 + _DAT_20005da2 & 0xffff, cVar2 != '\x06' &&
        (uVar10 = uVar10 + _DAT_20005da4 & 0xffff, cVar2 != '\a')))) {
      uVar10 = uVar10 + _DAT_20005da6 & 0xffff;
    }
    uVar23 = uVar10 + 2 & 0xffff;
    uVar7 = uVar10 + 1 & 0xffff;
    uVar21 = uVar10 + 3 & 0xffff;
    uVar14 = uVar10 + 4 & 0xffff;
  }
  *(char *)(uVar10 + 0x20005dac) = DAT_20005da8;
  *(undefined1 *)(uVar7 + 0x20005dac) = *(undefined1 *)(*(int *)(unaff_r4 + 0x78) + 0x1a);
  if ((*(byte *)(*(int *)(*(int *)(unaff_r4 + 0x7c) + 4) + 5) & 0xf7) == 1) {
    *(undefined1 *)(uVar23 + 0x20005dac) = 0;
    bVar11 = *(byte *)(*(int *)(*(int *)(*(int *)(unaff_r4 + 0x78) + 0x1c) + 4) + 0x18);
    uVar10 = (uint)bVar11;
    *(byte *)(uVar21 + 0x20005dac) = bVar11;
    if (uVar10 != 0) {
      puVar9 = (undefined2 *)&stack0x00000048;
      uVar23 = 0;
      uVar7 = uVar14;
      do {
        uVar15 = *puVar9;
        uVar21 = uVar7 + 1;
        *(undefined1 *)(uVar7 + 0x20005dac) = *(undefined1 *)puVar9;
        uVar23 = uVar23 + 1 & 0xffff;
        uVar7 = uVar7 + 2 & 0xffff;
        *(char *)((uVar21 & 0xffff) + 0x20005dac) = (char)((ushort)uVar15 >> 8);
        puVar9 = puVar9 + 1;
      } while (uVar23 < uVar10);
      iVar19 = *(int *)(unaff_r4 + 0x78);
      cVar2 = *(char *)(iVar19 + 0x10);
      uVar14 = uVar14 + uVar10 * 2 & 0xffff;
      goto joined_r0x000051d8;
    }
  }
  else {
    *(undefined1 *)(uVar23 + 0x20005dac) = 1;
    iVar19 = *(int *)(*(int *)(*(int *)(unaff_r4 + 0x78) + 0x1c) + 4);
    bVar11 = *(char *)(iVar19 + 0x19) * *(char *)(iVar19 + 0x18);
    uVar10 = (uint)bVar11;
    *(byte *)(uVar21 + 0x20005dac) = bVar11;
    if (uVar10 != 0) {
      iVar19 = 0;
      puVar9 = (undefined2 *)&stack0x00000048;
      uVar7 = uVar14;
      do {
        uVar15 = *puVar9;
        uVar23 = uVar7 + 1;
        *(undefined1 *)(uVar7 + 0x20005dac) = *(undefined1 *)puVar9;
        iVar19 = iVar19 + 1;
        uVar7 = uVar7 + 2 & 0xffff;
        *(char *)((uVar23 & 0xffff) + 0x20005dac) = (char)((ushort)uVar15 >> 8);
        puVar9 = puVar9 + 1;
      } while (iVar19 < (int)(uVar10 * 2));
      uVar14 = uVar14 + uVar10 * 4 & 0xffff;
    }
  }
  iVar19 = *(int *)(unaff_r4 + 0x78);
  cVar2 = *(char *)(iVar19 + 0x10);
joined_r0x000051d8:
  if (cVar2 != '\0') {
    *(undefined1 *)(uVar14 + 0x20005dac) = 0;
    *(undefined1 *)((uVar14 + 1 & 0xffff) + 0x20005dac) =
         *(undefined1 *)(*(int *)(unaff_r4 + 0x78) + 0x10);
    iVar19 = *(int *)(unaff_r4 + 0x78);
    uVar14 = uVar14 + 2 & 0xffff;
    if (*(char *)(iVar19 + 0x10) != '\0') {
      uVar10 = 0;
      do {
        if ((int)(uVar10 - 0x20) < 0) {
          bVar11 = (byte)(*(uint *)(unaff_r4 + 8) >> (uVar10 & 0xff)) |
                   (byte)(*(int *)(unaff_r4 + 0xc) << (0x20 - uVar10 & 0xff));
        }
        else {
          bVar11 = (byte)(*(uint *)(unaff_r4 + 0xc) >> (uVar10 - 0x20 & 0xff));
        }
        *(byte *)(uVar14 + 0x20005dac) = bVar11 & 1;
        iVar19 = uVar10 * 2;
        *(undefined1 *)((uVar14 + 1 & 0xffff) + 0x20005dac) =
             *(undefined1 *)(*(int *)(unaff_r4 + 0x18) + iVar19);
        *(char *)((uVar14 + 2 & 0xffff) + 0x20005dac) =
             (char)((ushort)*(undefined2 *)(*(int *)(unaff_r4 + 0x18) + iVar19) >> 8);
        *(undefined1 *)((uVar14 + 3 & 0xffff) + 0x20005dac) =
             *(undefined1 *)(*(int *)(unaff_r4 + 0x10) + iVar19);
        *(char *)((uVar14 + 4 & 0xffff) + 0x20005dac) =
             (char)((ushort)*(undefined2 *)(*(int *)(unaff_r4 + 0x10) + iVar19) >> 8);
        *(undefined1 *)((uVar14 + 5 & 0xffff) + 0x20005dac) =
             *(undefined1 *)(*(int *)(unaff_r4 + 0x14) + iVar19);
        *(char *)((uVar14 + 6 & 0xffff) + 0x20005dac) =
             (char)((ushort)*(undefined2 *)(*(int *)(unaff_r4 + 0x14) + iVar19) >> 8);
        iVar19 = *(int *)(unaff_r4 + 0x78);
        uVar10 = uVar10 + 1;
        uVar14 = uVar14 + 7 & 0xffff;
      } while ((uVar10 & 0xffff) < (uint)*(byte *)(iVar19 + 0x10));
    }
  }
  if (*(char *)(iVar19 + 0x11) != '\0') {
    *(undefined1 *)(uVar14 + 0x20005dac) = 1;
    *(undefined1 *)((uVar14 + 1 & 0xffff) + 0x20005dac) =
         *(undefined1 *)(*(int *)(unaff_r4 + 0x78) + 0x11);
    uVar14 = uVar14 + 2 & 0xffff;
    if (*(char *)(*(int *)(unaff_r4 + 0x78) + 0x11) != '\0') {
      uVar10 = 0;
      do {
        iVar19 = uVar10 * 2;
        uVar10 = uVar10 + 1;
        *(undefined1 *)(uVar14 + 0x20005dac) = *(undefined1 *)(*(int *)(unaff_r4 + 0x38) + iVar19);
        *(char *)((uVar14 + 1 & 0xffff) + 0x20005dac) =
             (char)((ushort)*(undefined2 *)(*(int *)(unaff_r4 + 0x38) + iVar19) >> 8);
        *(undefined1 *)((uVar14 + 2 & 0xffff) + 0x20005dac) =
             *(undefined1 *)(*(int *)(unaff_r4 + 0x3c) + iVar19);
        *(char *)((uVar14 + 3 & 0xffff) + 0x20005dac) =
             (char)((ushort)*(undefined2 *)(*(int *)(unaff_r4 + 0x3c) + iVar19) >> 8);
        uVar14 = uVar14 + 4 & 0xffff;
      } while ((uVar10 & 0xffff) < (uint)*(byte *)(*(int *)(unaff_r4 + 0x78) + 0x11));
    }
  }
  cVar2 = DAT_20005da8 + '\x01';
  *(char *)(uVar14 + 0x20005dac) = DAT_20005da8;
  DAT_20005da8 = cVar2;
  return 0;
}


```

#### `FUN_00005854` @ `00005854`

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

#### `FUN_0002164c` @ `0002164c`

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

#### `FUN_0005f274` @ `0005f274`

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
          piVar3[3] = iVar18;
        }
      }
      uVar2 = 1 << ((int)uVar16 >> 2 & 0xffU);
      if (uVar2 <= uVar15) {
        if ((uVar15 & uVar2) == 0) {
          uVar16 = uVar16 & 0xfffffffc;
          do {
            uVar2 = uVar2 << 1;
            uVar16 = uVar16 + 4;
          } while ((uVar15 & uVar2) == 0);
        }
        do {
          piVar3 = (int *)(uVar16 * 8 + uVar5);
          piVar12 = piVar3;
          uVar15 = uVar16;
          do {
            piVar10 = (int *)piVar12[3];
            while (piVar11 = piVar10, piVar12 != piVar11) {
              uVar13 = piVar11[1] & 0xfffffffc;
              uVar7 = uVar13 - uVar17;
              piVar10 = (int *)piVar11[3];
              if (0xf < (int)uVar7) {
                iVar9 = (int)piVar11 + uVar17;
                piVar11[1] = uVar17 | 1;
                iVar14 = piVar11[2];
                *(int **)(iVar14 + 0xc) = piVar10;
                piVar10[2] = iVar14;
                *(int *)(uVar5 + 0x10) = iVar9;
                *(int *)(uVar5 + 0x14) = iVar9;
                *(uint *)(iVar9 + 4) = uVar7 | 1;
                *(uint *)(iVar9 + 0xc) = uVar5 + 8;
                *(uint *)(iVar9 + 8) = uVar5 + 8;
                *(uint *)((int)piVar11 + uVar13) = uVar7;
                FUN_0005f7e8(param_1);
                return piVar11 + 2;
              }
              if (-1 < (int)uVar7) {
                *(uint *)((int)piVar11 + uVar13 + 4) = *(uint *)((int)piVar11 + uVar13 + 4) | 1;
                iVar9 = piVar11[2];
                *(int **)(iVar9 + 0xc) = piVar10;
                piVar10[2] = iVar9;
                FUN_0005f7e8(param_1);
                return piVar11 + 2;
              }
            }
            uVar15 = uVar15 + 1;
            piVar12 = piVar12 + 2;
          } while ((uVar15 & 3) != 0);
          do {
            if ((uVar16 & 3) == 0) {
              uVar13 = *(uint *)(uVar5 + 4) & ~uVar2;
              *(uint *)(uVar5 + 4) = uVar13;
              goto LAB_0005f410;
            }
            piVar12 = (int *)*piVar3;
            piVar3 = piVar3 + -2;
            uVar16 = uVar16 - 1;
          } while (piVar12 == piVar3);
          uVar13 = *(uint *)(uVar5 + 4);
LAB_0005f410:
          uVar2 = uVar2 * 2;
          if ((uVar13 <= uVar2 && uVar2 - uVar13 != 0) || (uVar16 = uVar15, uVar2 == 0)) break;
          for (; (uVar13 & uVar2) == 0; uVar2 = uVar2 << 1) {
            uVar16 = uVar16 + 4;
          }
        } while( true );
      }
      uVar15 = *(uint *)(uVar5 + 8);
      uVar16 = *(uint *)(uVar15 + 4) & 0xfffffffc;
      if ((uVar17 <= uVar16) && (uVar2 = uVar16 - uVar17, 0xf < (int)uVar2)) goto LAB_0005f56a;
      uVar2 = *DAT_0005f5c8 + 0x10 + uVar17;
      iVar9 = FUN_0005fc74(8);
      puVar1 = DAT_0005f5cc;
      if (*DAT_0005f5cc != 0xffffffff) {
        uVar2 = (uVar2 - 1) + iVar9 & -iVar9;
      }
      uVar13 = FUN_0005fc3c(param_1,uVar2);
      if (uVar13 == 0xffffffff) {
LAB_0005f69c:
        uVar15 = *(uint *)(uVar5 + 8);
        uVar7 = *(uint *)(uVar15 + 4);
      }
      else {
        uVar7 = uVar15 + uVar16;
        if (uVar13 < uVar7) {
          if (uVar15 == uVar5) {
            local_30 = DAT_0005f7d0;
            uVar6 = *DAT_0005f7d0 + uVar2;
            *DAT_0005f7d0 = uVar6;
            goto LAB_0005f4be;
          }
          goto LAB_0005f69c;
        }
        local_30 = DAT_0005f5d0;
        uVar6 = *DAT_0005f5d0 + uVar2;
        *DAT_0005f5d0 = uVar6;
        if ((uVar7 == uVar13) && ((uVar13 & iVar9 - 1U) == 0)) {
          uVar13 = *(uint *)(uVar5 + 8);
          uVar7 = uVar16 + uVar2 | 1;
          *(uint *)(uVar13 + 4) = uVar7;
        }
        else {
LAB_0005f4be:
          uVar8 = iVar9 - 1;
          if (*puVar1 == 0xffffffff) {
            *puVar1 = uVar13;
          }
          else {
            *local_30 = (uVar13 - uVar7) + uVar6;
          }
          uVar7 = uVar13 & 7;
          if ((uVar13 & 7) == 0) {
            uVar8 = uVar8 & iVar9 - (uVar2 + uVar13 & uVar8);
            uVar4 = FUN_0005fc3c(param_1,uVar8);
            if (uVar4 == 0xffffffff) {
              uVar8 = 0;
              uVar4 = uVar2 + uVar13;
            }
          }
          else {
            iVar14 = 8 - uVar7;
            uVar13 = uVar13 + iVar14;
            uVar8 = uVar8 & (iVar14 + iVar9) - (uVar2 + uVar13 & uVar8);
            uVar4 = FUN_0005fc3c(param_1,uVar8);
            if (uVar4 == 0xffffffff) {
              uVar8 = 0;
              uVar4 = uVar2 + uVar13 + (uVar7 - 8);
            }
          }
          uVar6 = *local_30 + uVar8;
          *local_30 = uVar6;
          uVar7 = (uVar4 - uVar13) + uVar8 | 1;
          *(uint *)(uVar5 + 8) = uVar13;
          *(uint *)(uVar13 + 4) = uVar7;
          if (uVar15 != uVar5) {
            if (uVar16 < 0x10) {
              *(undefined4 *)(uVar13 + 4) = 1;
              goto LAB_0005f6b0;
            }
            uVar16 = uVar16 - 0xc & 0xfffffff8;
            *(uint *)(uVar15 + 4) = *(uint *)(uVar15 + 4) & 1 | uVar16;
            *(undefined4 *)(uVar15 + uVar16 + 4) = 5;
            *(undefined4 *)(uVar15 + uVar16 + 8) = 5;
            if (uVar16 < 0x10) {
              uVar7 = *(uint *)(uVar13 + 4);
            }
            else {
              FUN_0005fdb0(param_1,uVar15 + 8);
              uVar6 = *local_30;
              uVar7 = *(uint *)(*(uint *)(uVar5 + 8) + 4);
              uVar13 = *(uint *)(uVar5 + 8);
            }
          }
        }
        uVar15 = uVar13;
        if (*DAT_0005f5d4 < uVar6) {
          *DAT_0005f5d4 = uVar6;
        }
        if (*DAT_0005f5d8 < uVar6) {
          *DAT_0005f5d8 = uVar6;
        }
      }
      uVar2 = (uVar7 & 0xfffffffc) - uVar17;
      if ((uVar17 <= (uVar7 & 0xfffffffc)) && (0xf < (int)uVar2)) {
LAB_0005f56a:
        *(uint *)(uVar15 + 4) = uVar17 | 1;
        *(uint *)(uVar5 + 8) = uVar15 + uVar17;
        *(uint *)(uVar15 + uVar17 + 4) = uVar2 | 1;
        FUN_0005f7e8(param_1);
        return (int *)(uVar15 + 8);
      }
LAB_0005f6b0:
      FUN_0005f7e8(param_1);
      return (int *)0x0;
    }
  }
  iVar9 = *(int *)(iVar18 + 8);
  uVar2 = *(uint *)(iVar18 + 4) & 0xfffffffc;
  iVar14 = *(int *)(iVar18 + 0xc);
  *(int *)(iVar9 + 0xc) = iVar14;
  *(int *)(iVar14 + 8) = iVar9;
LAB_0005f2ba:
  *(uint *)(iVar18 + uVar2 + 4) = *(uint *)(iVar18 + uVar2 + 4) | 1;
  FUN_0005f7e8(param_1);
  return (int *)(iVar18 + 8);
}


```

#### `FUN_0000290c` @ `0000290c`

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

#### `FUN_00002b44` @ `00002b44`

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
        }
        if (4 < bVar3) {
          if ((short)((uint)_DAT_20005a3c >> 8) < -0x1e) {
            FUN_00002ac8(4);
            FUN_0000a568(0x20004e2c,0,0x200);
            _DAT_20005a3c = 0;
            bVar3 = DAT_20005a56;
          }
          if (5 < bVar3) {
            if ((short)((uint)_DAT_20005a40 >> 8) < -0x1e) {
              FUN_00002ac8(5);
              FUN_0000a568(0x2000502c,0,0x200);
              _DAT_20005a40 = 0;
              bVar3 = DAT_20005a56;
            }
            if (6 < bVar3) {
              if ((short)((uint)_DAT_20005a44 >> 8) < -0x1e) {
                FUN_00002ac8(6);
                FUN_0000a568(0x2000522c,0,0x200);
                _DAT_20005a44 = 0;
                bVar3 = DAT_20005a56;
              }
              if (7 < bVar3) {
                if ((short)((uint)_DAT_20005a48 >> 8) < -0x1e) {
                  FUN_00002ac8(7);
                  FUN_0000a568(0x2000542c,0,0x200);
                  _DAT_20005a48 = 0;
                  bVar3 = DAT_20005a56;
                }
                if (8 < bVar3) {
                  if ((short)((uint)_DAT_20005a4c >> 8) < -0x1e) {
                    FUN_00002ac8(8);
                    FUN_0000a568(0x2000562c,0,0x200);
                    _DAT_20005a4c = 0;
                    bVar3 = DAT_20005a56;
                  }
                  if ((9 < bVar3) && ((short)((uint)_DAT_20005a50 >> 8) < -0x1e)) {
                    FUN_00002ac8(9);
                    FUN_0000a568(0x2000582c,0,0x200);
                    _DAT_20005a50 = 0;
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

## 4. Fender header templates (`08 26` / `08 24` without the F0)

The inbound parser has to match the manufacturer and device id. A two-byte
template, or a compare against `0x26`, is where that happens.

### `08 26`

```text
0000a22d  9b 01 9c 40 f2 00 08 26 1e 0a da 25 00 1c 00 00 23 62  in FUN_0000a210
0000a5f5  bc 9e 46 70 47 f0 08 26 05 f0 08 24 05 06 02 05 02 07  (data)
00022b94  30 20 ac 70 98 46 08 26 0c f0 4b f8 28 70 80 2e 0c d0  in FUN_00022b70
00024fb0  00 2b 21 d0 5d 24 08 26 00 25 05 e0 01 35 02 34 eb b2  (data)
00026c65  f0 eb ff 45 43 a8 08 26 f0 1d f9 01 1e 23 d0 00 23 20  (data)
00046a0e  57 46 83 46 98 46 08 26 a2 46 4b 46 52 46 63 43 98 12  in FUN_000469c8
00052e0c  16 10 bc 13 14 10 08 26 14 10 04 04 14 10 00 b5 85 b0  (data)
00052e48  16 10 bc 13 14 10 08 26 14 10 04 04 14 10 00 b5 85 b0  (data)
00052e88  16 10 bc 13 14 10 08 26 14 10 04 04 14 10 00 b5 85 b0  (data)
00052ecc  16 10 bc 13 14 10 08 26 14 10 04 04 14 10 10 b5 04 00  (data)
00052f40  14 10 dc c5 16 10 08 26 14 10 40 26 14 10 60 c6 16 10  (data)
00052f8c  16 10 c8 16 14 10 08 26 14 10 04 04 14 10 10 30 70 47  (data)
00052ff4  16 10 bc 13 14 10 08 26 14 10 04 04 14 10 e8 17 14 10  (data)
0005303c  16 10 bc 13 14 10 08 26 14 10 04 04 14 10 10 b5 03 7a  (data)
00088fe0  88 b2 00 b5 88 00 08 26 40 00 00 0a 00 00 00 b0 00 0a  (data)
000a580d  46 25 50 25 5a 26 08 26 0e 26 22 26 24 26 27 26 30 26  (data)
000a7425  46 25 50 25 5a 26 08 26 0e 26 22 26 24 26 27 26 30 26  (data)
000a93a5  46 25 50 25 5a 26 08 26 0e 26 22 26 24 26 27 26 30 26  (data)
000b17c9  46 25 50 25 5a 26 08 26 0e 26 22 26 24 26 27 26 30 26  (data)
000b3a55  46 25 50 25 5a 26 08 26 0e 26 22 26 24 26 27 26 30 26  (data)
```

### `08 24`

```text
0000a5f9  47 f0 08 26 05 f0 08 24 05 06 02 05 02 07 04 0f 09 0b  (data)
000248e8  12 20 ff f7 8e fd 08 24 19 25 b0 e7 c0 46 04 6b 14 10  (data)
0004bc6a  ff e6 d5 06 26 d4 08 24 22 42 00 d1 4a e7 02 9d 5b 1b  (data)
0005a312  84 42 00 d9 7a e7 08 24 a0 46 3b 81 b8 44 54 46 ba 46  in FUN_0005a1bc
0005a39c  7d 69 73 00 9b 19 08 24 11 5f db 00 40 46 eb 18 00 29  in FUN_0005a1bc
0005a52c  0e 4b 03 20 dc 60 08 24 08 4b 0c 49 1c 62 ff f7 b6 fb  in FUN_0005a4d0
000a57c3  3a 23 3b 23 5a 24 08 24 0d 24 0e 24 0f 24 1b 24 1c 24  (data)
000a73db  3a 23 3b 23 5a 24 08 24 0d 24 0e 24 0f 24 1b 24 1c 24  (data)
000a935b  3a 23 3b 23 5a 24 08 24 0d 24 0e 24 0f 24 1b 24 1c 24  (data)
000b177f  3a 23 3b 23 5a 24 08 24 0d 24 0e 24 0f 24 1b 24 1c 24  (data)
000b3a0b  3a 23 3b 23 5a 24 08 24 0d 24 0e 24 0f 24 1b 24 1c 24  (data)
```

### Functions comparing against the device id `0x26`

```text
FUN_00003af0 @ 00003af0  [00003c1a movs r7,#0x26]
FUN_0000408c @ 0000408c  [000041b4 movs r6,#0x26]
FUN_000041fc @ 000041fc  [00004326 movs r7,#0x26]
FUN_00009304 @ 00009304  [00009308 movs r2,#0x26]
FUN_00032b10 @ 00032b10  [00032ce6 adds r2,#0x26]
FUN_00032b10 @ 00032b10  [00032e12 adds r2,#0x26]
FUN_00032b10 @ 00032b10  [00032e96 movs r2,#0x26]
FUN_00032b10 @ 00032b10  [00032fa2 adds r2,#0x26]
FUN_0003d8a0 @ 0003d8a0  [0003d8d4 movs r3,#0x26]
FUN_0004962c @ 0004962c  [000496ae subs r3,#0x26]
FUN_0004990c @ 0004990c  [00049916 movs r1,#0x26]
```


---

## Reading order

1. **Section 1**, the functions loading the inbound queue. One of them is the
   framed-message consumer; its small constants are the accepted command ids.
   Anything past `0x20`/`0x21`/`0x22` is undocumented host->device vocabulary.
2. **Section 3**, CIN `0x08`. `8F 00 7F` arrives as a USB-MIDI packet whose
   header nibble is 8; if the firmware switches on that, the native-entry
   handler is in that switch and every sibling case is another host command.
3. **Section 2**, the config block, to settle the variant count as data.
