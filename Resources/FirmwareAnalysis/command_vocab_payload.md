# Motion 32 — command vocabulary and configuration block

Program: `motion32_fw_payload_0x1000.bin`  
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
00009500: 62 46 94 40 4f f6 ff 72 2d 04 32 40 ad 18 ac 42 
00009510: f1 d2 01 3b ef e7 37 00 d0 e7 99 46 84 e7 3a 00 
00009520: b1 e7 32 00 62 e7 02 3b 52 19 22 e7 1c 21 01 23 
00009530: 1b 04 98 42 01 d3 00 0c 10 39 1b 0a 98 42 01 d3 
00009540: 00 0a 08 39 1b 09 98 42 01 d3 00 09 04 39 02 a2 
00009550: 10 5c 40 18 70 47 c0 46 04 03 02 02 01 01 01 01 
00009560: 00 00 00 00 00 00 00 00 03 00 82 18 93 42 00 d1 
00009570: 70 47 19 70 01 33 f9 e7 00 23 10 b5 9a 42 00 d1 
00009580: 10 bd cc 5c c4 54 01 33 f8 e7 ff ff 42 75 69 6c 
00009590: 74 20 77 69 74 68 20 52 65 6e 65 73 61 73 20 41 
000095a0: 64 76 61 6e 63 65 64 20 46 6c 65 78 69 62 6c 65 
000095b0: 20 53 6f 66 74 77 61 72 65 20 50 61 63 6b 61 67 
000095c0: 65 20 76 65 72 73 69 6f 6e 20 35 2e 34 2e 30 00 
000095d0: 35 2e 34 2e 30 00 00 00 00 00 04 05 f8 b5 c0 46 
000095e0: f8 bc 08 bc 9e 46 70 47 f8 b5 c0 46 f8 bc 08 bc 
000095f0: 9e 46 70 47 f0 08 26 05 f0 08 24 05 06 02 05 02 
00009600: 07 04 0f 09 0b 04 0a 04 00 04 01 04 08 02 07 02 
00009610: 0e 09 0d 09 09 04 08 04 02 04 03 04 04 03 03 03 
00009620: 01 01 01 01 01 01 01 01 00 01 01 01 01 01 01 01 
00009630: 01 01 01 01 01 00 ff ff 04 00 08 00 10 00 20 00 
00009640: 01 00 02 00 80 00 00 01 40 00 00 02 00 04 01 00 
00009650: 02 00 80 00 04 00 08 00 10 00 20 00 40 00 00 01 
00009660: 00 02 00 04 00 03 05 07 01 02 04 06 08 02 08 06 
00009670: 05 01 00 07 04 03 ff ff 64 8c 8c 8c 64 00 00 00 
00009680: 31 2e 30 2e 30 00 ff ff 00 19 00 00 52 03 fa 00 
00009690: 01 00 ff ff 00 19 00 00 58 02 fa 00 01 00 ff ff 
000096a0: 3c 80 80 80 5a 5a 80 80 80 3c ff ff 9e 2e 00 00 
000096b0: ac 2e 00 00 ba 2e 00 00 c8 2e 00 00 d6 2e 00 00 
000096c0: e4 2e 00 00 f2 2e 00 00 30 2f 00 00 48 2f 00 00 
000096d0: 56 2f 00 00 74 2f 00 00 8c 2e 00 00 8c 2e 00 00 
000096e0: 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 
000096f0: 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 
00009700: 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 
00009710: 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 
00009720: 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 
00009730: 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 
00009740: 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 
00009750: 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 8c 2e 00 00 
```

## 3. USB-MIDI code-index-number decode

`8F 00 7F` reaches the device as a 4-byte USB-MIDI packet whose header low
nibble is the CIN. For a Note Off that is **8**. If the firmware switches on the
CIN, the native-entry handler is one case of that switch and its siblings are the
rest of the host command surface.

Functions comparing against CIN values, ranked by how many distinct CINs they use
(a real dispatch touches several):

```text
FUN_00003690                 @ 00003690   CINs: 0x04 0x05 0x06 0x07 0x08 0x09 0x0e
FUN_00003914                 @ 00003914   CINs: 0x04 0x05 0x06 0x07 0x08 0x09 0x0b
FUN_00003e3a                 @ 00003e3a   CINs: 0x04 0x05 0x06 0x07 0x08 0x09 0x0e
FUN_00004854                 @ 00004854   CINs: 0x04 0x05 0x06 0x07 0x09 0x0b 0x0e
FUN_00006a94                 @ 00006a94   CINs: 0x04 0x05 0x06 0x07 0x08 0x09 0x0b
FUN_0002064c                 @ 0002064c   CINs: 0x04 0x05 0x06 0x07 0x08 0x09 0x0e
FUN_0002578c                 @ 0002578c   CINs: 0x04 0x05 0x06 0x07 0x08 0x09 0x0e
FUN_0005e274                 @ 0005e274   CINs: 0x04 0x05 0x06 0x07 0x08 0x09 0x0b
FUN_0000190c                 @ 0000190c   CINs: 0x04 0x05 0x06 0x07 0x08 0x09
FUN_00001b44                 @ 00001b44   CINs: 0x04 0x05 0x06 0x07 0x08 0x09
FUN_00020f24                 @ 00020f24   CINs: 0x04 0x05 0x06 0x07 0x08 0x0e
FUN_00022e84                 @ 00022e84   CINs: 0x04 0x05 0x06 0x07 0x08 0x09
FUN_000338a4                 @ 000338a4   CINs: 0x04 0x05 0x06 0x07 0x08 0x09
FUN_0004dbe4                 @ 0004dbe4   CINs: 0x04 0x05 0x06 0x08 0x0b 0x0e
FUN_0000140c                 @ 0000140c   CINs: 0x04 0x05 0x06 0x07 0x08
FUN_000228c4                 @ 000228c4   CINs: 0x04 0x05 0x06 0x08 0x09
FUN_00027440                 @ 00027440   CINs: 0x05 0x07 0x08 0x09 0x0e
FUN_00041388                 @ 00041388   CINs: 0x06 0x07 0x08 0x09 0x0e
FUN_0004d190                 @ 0004d190   CINs: 0x04 0x05 0x06 0x08 0x0b
FUN_000537c4                 @ 000537c4   CINs: 0x04 0x05 0x06 0x07 0x0e
FUN_0005a5b4                 @ 0005a5b4   CINs: 0x04 0x06 0x08 0x09 0x0e
FUN_0005bbe8                 @ 0005bbe8   CINs: 0x04 0x06 0x07 0x08 0x09
FUN_0005edb0                 @ 0005edb0   CINs: 0x04 0x05 0x06 0x08 0x09
FUN_000016f4                 @ 000016f4   CINs: 0x04 0x08 0x09 0x0b
FUN_00006360                 @ 00006360   CINs: 0x04 0x07 0x08 0x09
FUN_00022a7c                 @ 00022a7c   CINs: 0x04 0x06 0x08 0x09
PROBE_00022b70               @ 00022b70   CINs: 0x04 0x05 0x06 0x07
FUN_000254e4                 @ 000254e4   CINs: 0x05 0x06 0x07 0x08
FUN_00025b58                 @ 00025b58   CINs: 0x06 0x07 0x08 0x09
FUN_00026c0c                 @ 00026c0c   CINs: 0x05 0x06 0x08 0x09
PROBE_0002f644               @ 0002f644   CINs: 0x04 0x05 0x07 0x0e
PROBE_0002fb60               @ 0002fb60   CINs: 0x05 0x06 0x08 0x0e
FUN_00035b60                 @ 00035b60   CINs: 0x04 0x05 0x06 0x07
FUN_00037b1c                 @ 00037b1c   CINs: 0x04 0x05 0x06 0x08
FUN_00040554                 @ 00040554   CINs: 0x04 0x06 0x08 0x09
FUN_000433c8                 @ 000433c8   CINs: 0x04 0x05 0x07 0x08
FUN_00045bb0                 @ 00045bb0   CINs: 0x04 0x05 0x09 0x0e
FUN_0004ead4                 @ 0004ead4   CINs: 0x04 0x07 0x08 0x09
FUN_0004fd0c                 @ 0004fd0c   CINs: 0x04 0x05 0x07 0x08
FUN_00000b30                 @ 00000b30   CINs: 0x04 0x05 0x09
```

### Decompilation of the top candidates

#### `FUN_00003690` @ `00003690`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

uint FUN_00003690(int *param_1,int *param_2)

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
LAB_000037e0:
        param_1[0xe] = uVar8 * 2 + 0x20005e78;
        param_1[0xf] = uVar8 * 2 + 0x20005e74;
        DAT_20005e7c = (char)uVar8 + *(char *)((int)param_2 + 0x11);
        goto LAB_00003802;
      }
      cVar21 = *(char *)((int)param_2 + 0x11);
      uVar4 = 0;
      if (cVar21 != '\0') goto LAB_00003808;
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
      if (uVar8 < 3) goto LAB_000037e0;
LAB_00003802:
      cVar21 = *(char *)((int)param_2 + 0x11);
      if (cVar21 != '\0') {
LAB_00003808:
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
    if (uVar4 != 0) goto LAB_00003836;
  }
  puVar18 = (undefined4 *)param_2[7];
  param_1[0x1f] = (int)puVar18;
  uVar4 = (**(code **)puVar18[2])(*puVar18,puVar18[1]);
  local_34 = param_2[1];
  iVar5 = *param_2;
LAB_00003836:
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

#### `FUN_00003914` @ `00003914`

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

#### `FUN_00003e3a` @ `00003e3a`

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
      goto joined_r0x000041d8;
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
joined_r0x000041d8:
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

#### `FUN_00004854` @ `00004854`

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

#### `FUN_00006a94` @ `00006a94`

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

#### `FUN_0002064c` @ `0002064c`

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

#### `FUN_0002578c` @ `0002578c`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0002578c(void)

{
  undefined1 uVar1;
  int iVar2;
  uint uVar3;
  int iVar4;
  undefined8 uVar5;
  
  FUN_00025740();
  FUN_00027080(DAT_00025a68,DAT_00025a64);
  FUN_000589c8(0x12,3);
  FUN_000589c8(0x13,3);
  FUN_000589f8(0x12,1,0);
  FUN_000589f8(0x13,1,0);
  FUN_00058a40(0x18);
  _DAT_d0000024 = 0x1000000;
  _DAT_d0000018 = 0x1000000;
  uVar5 = FUN_000599bc();
  iVar4 = (int)((ulonglong)uVar5 >> 0x20);
  if (iVar4 == 0) {
    iVar4 = FUN_0005a480((int)uVar5,1000);
  }
  else {
    iVar4 = FUN_0005a4fc((int)uVar5,iVar4,1000,0);
  }
  while( true ) {
    uVar5 = FUN_000599bc();
    iVar2 = (int)((ulonglong)uVar5 >> 0x20);
    if (iVar2 == 0) {
      iVar2 = FUN_0005a480((int)uVar5,1000);
      uVar3 = iVar2 - iVar4;
    }
    else {
      iVar2 = FUN_0005a4fc((int)uVar5,iVar2,1000,0);
      uVar3 = iVar2 - iVar4;
    }
    if (9 < uVar3) break;
    FUN_0005cc0c(0xffffffff,0);
  }
  _DAT_d0000014 = 0x1000000;
  uVar5 = FUN_000599bc();
  iVar4 = (int)((ulonglong)uVar5 >> 0x20);
  if (iVar4 == 0) {
    iVar4 = FUN_0005a480((int)uVar5,1000);
  }
  else {
    iVar4 = FUN_0005a4fc((int)uVar5,iVar4,1000,0);
  }
  while( true ) {
    uVar5 = FUN_000599bc();
    iVar2 = (int)((ulonglong)uVar5 >> 0x20);
    if (iVar2 == 0) {
      iVar2 = FUN_0005a480((int)uVar5,1000);
      uVar3 = iVar2 - iVar4;
    }
    else {
      iVar2 = FUN_0005a4fc((int)uVar5,iVar2,1000,0);
      uVar3 = iVar2 - iVar4;
    }
    if (9 < uVar3) break;
    FUN_0005cc0c(0xffffffff,0);
  }
  FUN_00058a40(0x19);
  _DAT_d0000024 = 0x2000000;
  _DAT_d0000014 = 0x2000000;
  uVar5 = FUN_000599bc();
  iVar4 = (int)((ulonglong)uVar5 >> 0x20);
  if (iVar4 == 0) {
    iVar4 = FUN_0005a480((int)uVar5,1000);
  }
  else {
    iVar4 = FUN_0005a4fc((int)uVar5,iVar4,1000,0);
  }
  while( true ) {
    uVar5 = FUN_000599bc();
    iVar2 = (int)((ulonglong)uVar5 >> 0x20);
    if (iVar2 == 0) {
      iVar2 = FUN_0005a480((int)uVar5,1000);
      uVar3 = iVar2 - iVar4;
    }
    else {
      iVar2 = FUN_0005a4fc((int)uVar5,iVar2,1000,0);
      uVar3 = iVar2 - iVar4;
    }
    if (9 < uVar3) break;
    FUN_0005cc0c(0xffffffff,0);
  }
  _DAT_d0000018 = 0x2000000;
  uVar5 = FUN_000599bc();
  iVar4 = (int)((ulonglong)uVar5 >> 0x20);
  if (iVar4 == 0) {
    iVar4 = FUN_0005a480((int)uVar5,1000);
  }
  else {
    iVar4 = FUN_0005a4fc((int)uVar5,iVar4,1000,0);
  }
  while( true ) {
    uVar5 = FUN_000599bc();
    iVar2 = (int)((ulonglong)uVar5 >> 0x20);
    if (iVar2 == 0) {
      iVar2 = FUN_0005a480((int)uVar5,1000);
      uVar3 = iVar2 - iVar4;
    }
    else {
      iVar2 = FUN_0005a4fc((int)uVar5,iVar2,1000,0);
      uVar3 = iVar2 - iVar4;
    }
    if (99 < uVar3) break;
    FUN_0005cc0c(0xffffffff,0);
  }
  uVar1 = FUN_0002eed4(0x5a);
  *DAT_00025a6c = uVar1;
  FUN_000589c8(0x1a,0x1f);
  FUN_000589f8(0x1a,0,0);
  FUN_00058a1c(0x1a,0);
  FUN_000589c8(0x1b,0x1f);
  FUN_000589f8(0x1b,0,0);
  FUN_00058a1c(0x1b,0);
  FUN_000589c8(0x1c,0x1f);
  FUN_000589f8(0x1c,0,0);
  FUN_00058a1c(0x1c,0);
  FUN_000589c8(0x1d,0x1f);
  FUN_000589f8(0x1d,0,0);
  FUN_00058a1c(0x1d,0);
  FUN_00058a40(0x14);
  _DAT_d0000024 = 0x100000;
  FUN_00058a40(0x15);
  _DAT_d0000024 = 0x200000;
  FUN_00058a40(0x16);
  _DAT_d0000024 = 0x400000;
  FUN_00058a40(0xf);
  _DAT_d0000024 = 0x8000;
  _DAT_d0000014 = 0x8000;
  FUN_00058a40(0x17);
  _DAT_d0000024 = 0x800000;
  _DAT_d0000018 = 0x800000;
  FUN_00058a40(0xd);
  _DAT_d0000024 = 0x2000;
  _DAT_d0000014 = 0x2000;
  FUN_00058a40(5);
  _DAT_d0000024 = 0x20;
  _DAT_d0000018 = 0x20;
  FUN_00058a40(6);
  _DAT_d0000024 = 0x40;
  _DAT_d0000018 = 0x40;
  FUN_00058a40(7);
  _DAT_d0000024 = 0x80;
  _DAT_d0000018 = 0x80;
  FUN_00058a40(4);
  _DAT_d0000028 = 0x10;
  FUN_00058a40(1);
  _DAT_d0000024 = 2;
  _DAT_d0000014 = 2;
  FUN_00058a40(2);
  _DAT_d0000024 = 4;
  _DAT_d0000018 = 4;
  FUN_000250d4();
  FUN_00025674();
  _DAT_d0000014 = 2;
  _DAT_d0000018 = 2;
  FUN_00027408();
  return;
}


```

#### `FUN_0005e274` @ `0005e274`

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
          else if (DAT_0005e7d4 < uVar7) {
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
                FUN_0005e7e8(param_1);
                return piVar11 + 2;
              }
              if (-1 < (int)uVar7) {
                *(uint *)((int)piVar11 + uVar13 + 4) = *(uint *)((int)piVar11 + uVar13 + 4) | 1;
                iVar9 = piVar11[2];
                *(int **)(iVar9 + 0xc) = piVar10;
                piVar10[2] = iVar9;
                FUN_0005e7e8(param_1);
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
              goto LAB_0005e410;
            }
            piVar12 = (int *)*piVar3;
            piVar3 = piVar3 + -2;
            uVar16 = uVar16 - 1;
          } while (piVar12 == piVar3);
          uVar13 = *(uint *)(uVar5 + 4);
LAB_0005e410:
          uVar2 = uVar2 * 2;
          if ((uVar13 <= uVar2 && uVar2 - uVar13 != 0) || (uVar16 = uVar15, uVar2 == 0)) break;
          for (; (uVar13 & uVar2) == 0; uVar2 = uVar2 << 1) {
            uVar16 = uVar16 + 4;
          }
        } while( true );
      }
      uVar15 = *(uint *)(uVar5 + 8);
      uVar16 = *(uint *)(uVar15 + 4) & 0xfffffffc;
      if ((uVar17 <= uVar16) && (uVar2 = uVar16 - uVar17, 0xf < (int)uVar2)) goto LAB_0005e56a;
      uVar2 = *DAT_0005e5c8 + 0x10 + uVar17;
      iVar9 = FUN_0005ec74(8);
      puVar1 = DAT_0005e5cc;
      if (*DAT_0005e5cc != 0xffffffff) {
        uVar2 = (uVar2 - 1) + iVar9 & -iVar9;
      }
      uVar13 = FUN_0005ec3c(param_1,uVar2);
      if (uVar13 == 0xffffffff) {
LAB_0005e69c:
        uVar15 = *(uint *)(uVar5 + 8);
        uVar7 = *(uint *)(uVar15 + 4);
      }
      else {
        uVar7 = uVar15 + uVar16;
        if (uVar13 < uVar7) {
          if (uVar15 == uVar5) {
            local_30 = DAT_0005e7d0;
            uVar6 = *DAT_0005e7d0 + uVar2;
            *DAT_0005e7d0 = uVar6;
            goto LAB_0005e4be;
          }
          goto LAB_0005e69c;
        }
        local_30 = DAT_0005e5d0;
        uVar6 = *DAT_0005e5d0 + uVar2;
        *DAT_0005e5d0 = uVar6;
        if ((uVar7 == uVar13) && ((uVar13 & iVar9 - 1U) == 0)) {
          uVar13 = *(uint *)(uVar5 + 8);
          uVar7 = uVar16 + uVar2 | 1;
          *(uint *)(uVar13 + 4) = uVar7;
        }
        else {
LAB_0005e4be:
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
            uVar4 = FUN_0005ec3c(param_1,uVar8);
            if (uVar4 == 0xffffffff) {
              uVar8 = 0;
              uVar4 = uVar2 + uVar13;
            }
          }
          else {
            iVar14 = 8 - uVar7;
            uVar13 = uVar13 + iVar14;
            uVar8 = uVar8 & (iVar14 + iVar9) - (uVar2 + uVar13 & uVar8);
            uVar4 = FUN_0005ec3c(param_1,uVar8);
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
              goto LAB_0005e6b0;
            }
            uVar16 = uVar16 - 0xc & 0xfffffff8;
            *(uint *)(uVar15 + 4) = *(uint *)(uVar15 + 4) & 1 | uVar16;
            *(undefined4 *)(uVar15 + uVar16 + 4) = 5;
            *(undefined4 *)(uVar15 + uVar16 + 8) = 5;
            if (uVar16 < 0x10) {
              uVar7 = *(uint *)(uVar13 + 4);
            }
            else {
              FUN_0005edb0(param_1,uVar15 + 8);
              uVar6 = *local_30;
              uVar7 = *(uint *)(*(uint *)(uVar5 + 8) + 4);
              uVar13 = *(uint *)(uVar5 + 8);
            }
          }
        }
        uVar15 = uVar13;
        if (*DAT_0005e5d4 < uVar6) {
          *DAT_0005e5d4 = uVar6;
        }
        if (*DAT_0005e5d8 < uVar6) {
          *DAT_0005e5d8 = uVar6;
        }
      }
      uVar2 = (uVar7 & 0xfffffffc) - uVar17;
      if ((uVar17 <= (uVar7 & 0xfffffffc)) && (0xf < (int)uVar2)) {
LAB_0005e56a:
        *(uint *)(uVar15 + 4) = uVar17 | 1;
        *(uint *)(uVar5 + 8) = uVar15 + uVar17;
        *(uint *)(uVar15 + uVar17 + 4) = uVar2 | 1;
        FUN_0005e7e8(param_1);
        return (int *)(uVar15 + 8);
      }
LAB_0005e6b0:
      FUN_0005e7e8(param_1);
      return (int *)0x0;
    }
  }
  iVar9 = *(int *)(iVar18 + 8);
  uVar2 = *(uint *)(iVar18 + 4) & 0xfffffffc;
  iVar14 = *(int *)(iVar18 + 0xc);
  *(int *)(iVar9 + 0xc) = iVar14;
  *(int *)(iVar14 + 8) = iVar9;
LAB_0005e2ba:
  *(uint *)(iVar18 + uVar2 + 4) = *(uint *)(iVar18 + uVar2 + 4) | 1;
  FUN_0005e7e8(param_1);
  return (int *)(iVar18 + 8);
}


```

## 4. Fender header templates (`08 26` / `08 24` without the F0)

The inbound parser has to match the manufacturer and device id. A two-byte
template, or a compare against `0x26`, is where that happens.

### `08 26`

```text
0000922d  9b 01 9c 40 f2 00 08 26 1e 0a da 25 00 1c 00 00 23 62  in FUN_00009210
000095f5  bc 9e 46 70 47 f0 08 26 05 f0 08 24 05 06 02 05 02 07  (data)
00021b94  30 20 ac 70 98 46 08 26 0c f0 4b f8 28 70 80 2e 0c d0  in FUN_00021b70
00023fb0  00 2b 21 d0 5d 24 08 26 00 25 05 e0 01 35 02 34 eb b2  (data)
00025c65  f0 eb ff 45 43 a8 08 26 f0 1d f9 01 1e 23 d0 00 23 20  in FUN_00025b58
00045a0e  57 46 83 46 98 46 08 26 a2 46 4b 46 52 46 63 43 98 12  in FUN_000459c8
00051e0c  16 10 bc 13 14 10 08 26 14 10 04 04 14 10 00 b5 85 b0  (data)
00051e48  16 10 bc 13 14 10 08 26 14 10 04 04 14 10 00 b5 85 b0  (data)
00051e88  16 10 bc 13 14 10 08 26 14 10 04 04 14 10 00 b5 85 b0  (data)
00051ecc  16 10 bc 13 14 10 08 26 14 10 04 04 14 10 10 b5 04 00  (data)
00051f40  14 10 dc c5 16 10 08 26 14 10 40 26 14 10 60 c6 16 10  (data)
00051f8c  16 10 c8 16 14 10 08 26 14 10 04 04 14 10 10 30 70 47  (data)
00051ff4  16 10 bc 13 14 10 08 26 14 10 04 04 14 10 e8 17 14 10  (data)
0005203c  16 10 bc 13 14 10 08 26 14 10 04 04 14 10 10 b5 03 7a  (data)
00087fe0  88 b2 00 b5 88 00 08 26 40 00 00 0a 00 00 00 b0 00 0a  (data)
000a480d  46 25 50 25 5a 26 08 26 0e 26 22 26 24 26 27 26 30 26  (data)
000a6425  46 25 50 25 5a 26 08 26 0e 26 22 26 24 26 27 26 30 26  (data)
000a83a5  46 25 50 25 5a 26 08 26 0e 26 22 26 24 26 27 26 30 26  (data)
000b07c9  46 25 50 25 5a 26 08 26 0e 26 22 26 24 26 27 26 30 26  (data)
000b2a55  46 25 50 25 5a 26 08 26 0e 26 22 26 24 26 27 26 30 26  (data)
```

### `08 24`

```text
000095f9  47 f0 08 26 05 f0 08 24 05 06 02 05 02 07 04 0f 09 0b  (data)
000238e8  12 20 ff f7 8e fd 08 24 19 25 b0 e7 c0 46 04 6b 14 10  (data)
0004ac6a  ff e6 d5 06 26 d4 08 24 22 42 00 d1 4a e7 02 9d 5b 1b  (data)
00059312  84 42 00 d9 7a e7 08 24 a0 46 3b 81 b8 44 54 46 ba 46  in FUN_000591bc
0005939c  7d 69 73 00 9b 19 08 24 11 5f db 00 40 46 eb 18 00 29  in FUN_000591bc
0005952c  0e 4b 03 20 dc 60 08 24 08 4b 0c 49 1c 62 ff f7 b6 fb  in FUN_000594d0
000a47c3  3a 23 3b 23 5a 24 08 24 0d 24 0e 24 0f 24 1b 24 1c 24  (data)
000a63db  3a 23 3b 23 5a 24 08 24 0d 24 0e 24 0f 24 1b 24 1c 24  (data)
000a835b  3a 23 3b 23 5a 24 08 24 0d 24 0e 24 0f 24 1b 24 1c 24  (data)
000b077f  3a 23 3b 23 5a 24 08 24 0d 24 0e 24 0f 24 1b 24 1c 24  (data)
000b2a0b  3a 23 3b 23 5a 24 08 24 0d 24 0e 24 0f 24 1b 24 1c 24  (data)
```

### Functions comparing against the device id `0x26`

```text
FUN_00002af0 @ 00002af0  [00002c1a movs r7,#0x26]
FUN_0000308c @ 0000308c  [000031b4 movs r6,#0x26]
FUN_000031fc @ 000031fc  [00003326 movs r7,#0x26]
FUN_00008304 @ 00008304  [00008308 movs r2,#0x26]
FUN_00008330 @ 00008330  [00008378 adds r2,#0x26]
FUN_000225f4 @ 000225f4  [00022628 movs r0,#0x26]
FUN_00031b10 @ 00031b10  [00031ce6 adds r2,#0x26]
FUN_00031b10 @ 00031b10  [00031e12 adds r2,#0x26]
FUN_00031b10 @ 00031b10  [00031e96 movs r2,#0x26]
FUN_00031b10 @ 00031b10  [00031fa2 adds r2,#0x26]
FUN_0003c8a0 @ 0003c8a0  [0003c8d4 movs r3,#0x26]
FUN_0004862c @ 0004862c  [000486ae subs r3,#0x26]
FUN_0004890c @ 0004890c  [00048916 movs r1,#0x26]
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
