# Motion 32 Parser/Callback Trace Probe

## Function Callers

### `00001d54` `FUN_00001d54`

- `FUN_000020a4` @ `000020a4`

#### Target `FUN_00001d54` @ `00001d54`

```c

int FUN_00001d54(uint *param_1)

{
  int iVar1;
  uint uVar2;
  uint uVar3;
  
  uVar2 = *param_1;
  uVar3 = param_1[1];
  iVar1 = uVar3 - uVar2;
  if (uVar3 < uVar2) {
    iVar1 = (param_1[2] + uVar3 + 1) - uVar2;
  }
  return param_1[2] - iVar1;
}
```

#### Caller `FUN_000020a4` @ `000020a4`

Site `000020ca`:

```asm
000020b2: movw r6,#0x4320
000020b6: movw r7,#0x4294
000020ba: movs r4,r0
000020bc: movt r5,#0x2000
000020c0: movt r6,#0x2000
000020c4: movt r7,#0x2000
000020c8: movs r0,r4
000020ca: bl 0x00001d54
000020ce: cbz r0,0x00002132
000020d0: movs r0,r4
000020d2: bl 0x00001d94
000020d6: ldrb r3,[r5,#0x0]
000020d8: cmp r3,#0x1
000020da: beq 0x00002138
000020dc: cmp r3,#0x2
```

Site `0000212a`:

```asm
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
00002132: pop {r7}
00002134: mov r8,r7
00002136: pop {r4,r5,r6,r7,pc}
00002138: ldrb r2,[r6,#0x0]
0000213a: ldr r1,[r7,#0x0]
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

### `00001d6c` `FUN_00001d6c`

- `FUN_00001eec` @ `00001eec`
- `FUN_00002030` @ `00002030`
- `FUN_00001f6c` @ `00001f6c`
- `FUN_00001fb0` @ `00001fb0`

#### Target `FUN_00001d6c` @ `00001d6c`

```c

void FUN_00001d6c(int *param_1,undefined1 param_2)

{
  int local_4;
  
  local_4 = *param_1;
  if (param_1[2] + 1 == local_4) {
    local_4 = 0;
  }
  *(undefined1 *)(param_1[5] + local_4) = param_2;
  *param_1 = local_4 + 1;
  return;
}
```

#### Caller `FUN_00001eec` @ `00001eec`

Site `00001f16`:

```asm
00001f04: beq 0x00001f1a
00001f06: movs r1,r0
00001f08: strb r0,[r5,#0x0]
00001f0a: movw r0,#0x4084
00001f0e: subs r1,#0x50
00001f10: uxtb r1,r1
00001f12: movt r0,#0x2000
00001f16: bl 0x00001d6c
00001f1a: movw r0,#0x4084
00001f1e: movs r1,#0x16
00001f20: movt r0,#0x2000
00001f24: bl 0x00001d6c
00001f28: movw r0,#0x4084
00001f2c: movs r1,r6
00001f2e: movt r0,#0x2000
```

Site `00001f24`:

```asm
00001f0e: subs r1,#0x50
00001f10: uxtb r1,r1
00001f12: movt r0,#0x2000
00001f16: bl 0x00001d6c
00001f1a: movw r0,#0x4084
00001f1e: movs r1,#0x16
00001f20: movt r0,#0x2000
00001f24: bl 0x00001d6c
00001f28: movw r0,#0x4084
00001f2c: movs r1,r6
00001f2e: movt r0,#0x2000
00001f32: bl 0x00001d6c
00001f36: ldrb r3,[r5,#0x0]
00001f38: cmp r3,r4
00001f3a: beq 0x00001f4e
```

Site `00001f32`:

```asm
00001f1a: movw r0,#0x4084
00001f1e: movs r1,#0x16
00001f20: movt r0,#0x2000
00001f24: bl 0x00001d6c
00001f28: movw r0,#0x4084
00001f2c: movs r1,r6
00001f2e: movt r0,#0x2000
00001f32: bl 0x00001d6c
00001f36: ldrb r3,[r5,#0x0]
00001f38: cmp r3,r4
00001f3a: beq 0x00001f4e
00001f3c: movw r0,#0x4084
00001f40: strb r4,[r5,#0x0]
00001f42: subs r4,#0x50
00001f44: uxtb r1,r4
```

Site `00001f4a`:

```asm
00001f38: cmp r3,r4
00001f3a: beq 0x00001f4e
00001f3c: movw r0,#0x4084
00001f40: strb r4,[r5,#0x0]
00001f42: subs r4,#0x50
00001f44: uxtb r1,r4
00001f46: movt r0,#0x2000
00001f4a: bl 0x00001d6c
00001f4e: movw r0,#0x4084
00001f52: movs r1,#0x36
00001f54: movt r0,#0x2000
00001f58: bl 0x00001d6c
00001f5c: movw r0,#0x4084
00001f60: movs r1,r7
00001f62: movt r0,#0x2000
```

Site `00001f58`:

```asm
00001f42: subs r4,#0x50
00001f44: uxtb r1,r4
00001f46: movt r0,#0x2000
00001f4a: bl 0x00001d6c
00001f4e: movw r0,#0x4084
00001f52: movs r1,#0x36
00001f54: movt r0,#0x2000
00001f58: bl 0x00001d6c
00001f5c: movw r0,#0x4084
00001f60: movs r1,r7
00001f62: movt r0,#0x2000
00001f66: bl 0x00001d6c
00001f6a: pop {r3,r4,r5,r6,r7,pc}
00001f6c: movw r3,#0x4081
00001f70: push {r4,lr}
```

Site `00001f66`:

```asm
00001f4e: movw r0,#0x4084
00001f52: movs r1,#0x36
00001f54: movt r0,#0x2000
00001f58: bl 0x00001d6c
00001f5c: movw r0,#0x4084
00001f60: movs r1,r7
00001f62: movt r0,#0x2000
00001f66: bl 0x00001d6c
00001f6a: pop {r3,r4,r5,r6,r7,pc}
00001f6c: movw r3,#0x4081
00001f70: push {r4,lr}
00001f72: movt r3,#0x2000
00001f76: ldrb r2,[r3,#0x0]
00001f78: movs r4,r1
00001f7a: cmp r2,r0
```

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

#### Caller `FUN_00002030` @ `00002030`

Site `00002052`:

```asm
0000203c: movw r4,#0x95f4
00002040: movt r4,#0x0
00002044: adds r7,r4,#0x4
00002046: movw r0,#0x4084
0000204a: ldrb r1,[r4,#0x0]
0000204c: movt r0,#0x2000
00002050: adds r4,#0x1
00002052: bl 0x00001d6c
00002056: cmp r4,r7
00002058: bne 0x00002046
0000205a: cbz r6,0x0000207e
0000205c: movs r4,#0x0
0000205e: movs r3,#0x0
00002060: ldrsb r3,[r5,r3]
00002062: ldrb r1,[r5,#0x0]
```

Site `00002070`:

```asm
0000205e: movs r3,#0x0
00002060: ldrsb r3,[r5,r3]
00002062: ldrb r1,[r5,#0x0]
00002064: cmp r3,#0x0
00002066: blt 0x00002074
00002068: movw r0,#0x4084
0000206c: movt r0,#0x2000
00002070: bl 0x00001d6c
00002074: adds r4,#0x1
00002076: uxtb r4,r4
00002078: adds r5,#0x1
0000207a: cmp r6,r4
0000207c: bne 0x0000205e
0000207e: movw r0,#0x4084
00002082: movs r1,#0xf7
```

Site `00002088`:

```asm
00002076: uxtb r4,r4
00002078: adds r5,#0x1
0000207a: cmp r6,r4
0000207c: bne 0x0000205e
0000207e: movw r0,#0x4084
00002082: movs r1,#0xf7
00002084: movt r0,#0x2000
00002088: bl 0x00001d6c
0000208c: pop {r3,r4,r5,r6,r7,pc}
0000208e: movw r4,#0x95f8
00002092: movt r4,#0x0
00002096: b 0x00002044
00002098: movw r3,#0x4298
0000209c: movt r3,#0x2000
000020a0: str r0,[r3,#0x0]
```

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

#### Caller `FUN_00001f6c` @ `00001f6c`

Site `00001f8c`:

```asm
00001f7a: cmp r2,r0
00001f7c: beq 0x00001f90
00001f7e: strb r0,[r3,#0x0]
00001f80: subs r0,#0x50
00001f82: uxtb r1,r0
00001f84: movw r0,#0x4084
00001f88: movt r0,#0x2000
00001f8c: bl 0x00001d6c
00001f90: movw r0,#0x4084
00001f94: movs r1,#0x14
00001f96: movt r0,#0x2000
00001f9a: bl 0x00001d6c
00001f9e: movw r0,#0x4084
00001fa2: movs r1,r4
00001fa4: movt r0,#0x2000
```

Site `00001f9a`:

```asm
00001f82: uxtb r1,r0
00001f84: movw r0,#0x4084
00001f88: movt r0,#0x2000
00001f8c: bl 0x00001d6c
00001f90: movw r0,#0x4084
00001f94: movs r1,#0x14
00001f96: movt r0,#0x2000
00001f9a: bl 0x00001d6c
00001f9e: movw r0,#0x4084
00001fa2: movs r1,r4
00001fa4: movt r0,#0x2000
00001fa8: bl 0x00001d6c
00001fac: pop {r4,pc}
00001fb0: movw r3,#0x4081
00001fb4: push {r4,lr}
```

Site `00001fa8`:

```asm
00001f90: movw r0,#0x4084
00001f94: movs r1,#0x14
00001f96: movt r0,#0x2000
00001f9a: bl 0x00001d6c
00001f9e: movw r0,#0x4084
00001fa2: movs r1,r4
00001fa4: movt r0,#0x2000
00001fa8: bl 0x00001d6c
00001fac: pop {r4,pc}
00001fb0: movw r3,#0x4081
00001fb4: push {r4,lr}
00001fb6: movt r3,#0x2000
00001fba: ldrb r2,[r3,#0x0]
00001fbc: adds r1,#0x40
00001fbe: uxtb r4,r1
```

```c

void FUN_00001f6c(uint param_1,undefined4 param_2)

{
  if (DAT_20004081 != param_1) {
    DAT_20004081 = (byte)param_1;
    FUN_00001d6c(0x20004084,param_1 - 0x50 & 0xff);
  }
  FUN_00001d6c(0x20004084,0x14);
  FUN_00001d6c(0x20004084,param_2);
  return;
}
```

#### Caller `FUN_00001fb0` @ `00001fb0`

Site `00001fd2`:

```asm
00001fc0: cmp r2,r0
00001fc2: beq 0x00001fd6
00001fc4: strb r0,[r3,#0x0]
00001fc6: subs r0,#0x50
00001fc8: uxtb r1,r0
00001fca: movw r0,#0x4084
00001fce: movt r0,#0x2000
00001fd2: bl 0x00001d6c
00001fd6: movw r0,#0x4084
00001fda: movs r1,#0x15
00001fdc: movt r0,#0x2000
00001fe0: bl 0x00001d6c
00001fe4: movw r0,#0x4084
00001fe8: movs r1,r4
00001fea: movt r0,#0x2000
```

Site `00001fe0`:

```asm
00001fc8: uxtb r1,r0
00001fca: movw r0,#0x4084
00001fce: movt r0,#0x2000
00001fd2: bl 0x00001d6c
00001fd6: movw r0,#0x4084
00001fda: movs r1,#0x15
00001fdc: movt r0,#0x2000
00001fe0: bl 0x00001d6c
00001fe4: movw r0,#0x4084
00001fe8: movs r1,r4
00001fea: movt r0,#0x2000
00001fee: bl 0x00001d6c
00001ff2: pop {r4,pc}
00002006: pop {r4,pc}
0000202e: b 0x00002006
```

Site `00001fee`:

```asm
00001fd6: movw r0,#0x4084
00001fda: movs r1,#0x15
00001fdc: movt r0,#0x2000
00001fe0: bl 0x00001d6c
00001fe4: movw r0,#0x4084
00001fe8: movs r1,r4
00001fea: movt r0,#0x2000
00001fee: bl 0x00001d6c
00001ff2: pop {r4,pc}
00002006: pop {r4,pc}
0000202e: b 0x00002006
00002030: push {r3,r4,r5,r6,r7,lr}
00002032: movs r5,r0
00002034: movs r6,r1
00002036: bl 0x00001e50
```

```c

void FUN_00001fb0(uint param_1,char param_2)

{
  if (DAT_20004081 != param_1) {
    DAT_20004081 = (byte)param_1;
    FUN_00001d6c(0x20004084,param_1 - 0x50 & 0xff);
  }
  FUN_00001d6c(0x20004084,0x15);
  FUN_00001d6c(0x20004084,param_2 + '@');
  return;
}
```

### `00001d94` `FUN_00001d94`

- `FUN_000020a4` @ `000020a4`

#### Target `FUN_00001d94` @ `00001d94`

```c

undefined1 FUN_00001d94(int param_1)

{
  undefined1 uVar1;
  undefined4 local_4;
  
  local_4 = *(int *)(param_1 + 4) + 1;
  if (*(int *)(param_1 + 8) + 1 == local_4) {
    local_4 = 0;
  }
  uVar1 = *(undefined1 *)(*(int *)(param_1 + 0x14) + local_4);
  *(int *)(param_1 + 4) = local_4;
  return uVar1;
}
```

#### Caller `FUN_000020a4` @ `000020a4`

Site `000020d2`:

```asm
000020bc: movt r5,#0x2000
000020c0: movt r6,#0x2000
000020c4: movt r7,#0x2000
000020c8: movs r0,r4
000020ca: bl 0x00001d54
000020ce: cbz r0,0x00002132
000020d0: movs r0,r4
000020d2: bl 0x00001d94
000020d6: ldrb r3,[r5,#0x0]
000020d8: cmp r3,#0x1
000020da: beq 0x00002138
000020dc: cmp r3,#0x2
000020de: beq 0x0000214c
000020e0: cmp r3,#0x0
000020e2: bne 0x00002146
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

### `00001dc0` `FUN_00001dc0`

- no direct function callers found

#### Target `FUN_00001dc0` @ `00001dc0`

```c

int FUN_00001dc0(uint *param_1,int param_2,int param_3)

{
  undefined1 uVar1;
  int iVar2;
  uint uVar3;
  int iVar4;
  uint uVar5;
  uint uVar6;
  uint local_20;
  uint local_1c;
  
  uVar6 = *param_1;
  uVar3 = param_1[1];
  uVar5 = param_1[2];
  iVar2 = uVar3 - uVar6;
  if (uVar3 < uVar6) {
    iVar2 = (uVar5 + uVar3 + 1) - uVar6;
  }
  iVar2 = uVar5 - iVar2;
  if (param_2 == 0) {
    if (iVar2 == 0) {
      return 0;
    }
    iVar4 = 0;
    if (param_3 != 0) {
      while( true ) {
        local_1c = param_1[1] + 1;
        if (uVar5 + 1 == local_1c) {
          local_1c = 0;
        }
        iVar4 = iVar4 + 1;
        param_1[1] = local_1c;
        if (iVar4 == iVar2) break;
        if (param_3 == iVar4) {
          return param_3;
        }
      }
      return iVar2;
    }
  }
  else {
    if (iVar2 == 0) {
      return 0;
    }
    if (param_3 != 0) {
      iVar4 = 0;
      while( true ) {
        local_20 = param_1[1] + 1;
        if (uVar5 + 1 == local_20) {
          local_20 = 0;
        }
        uVar1 = *(undefined1 *)(param_1[5] + local_20);
        param_1[1] = local_20;
        *(undefined1 *)(param_2 + iVar4) = uVar1;
        iVar4 = iVar4 + 1;
        if (iVar4 == iVar2) break;
        if (param_3 == iVar4) {
          return param_3;
        }
        uVar5 = param_1[2];
      }
      return iVar2;
    }
  }
  return 0;
}
```

### `000020a4` `FUN_000020a4`

- no direct function callers found

#### Target `FUN_000020a4` @ `000020a4`

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

### `00002098` `FUN_00002098`

- `FUN_00003f88` @ `00003f88`

#### Target `FUN_00002098` @ `00002098`

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00002098(undefined4 param_1)

{
  _DAT_20004298 = param_1;
  return;
}
```

#### Caller `FUN_00003f88` @ `00003f88`

Site `00003f92`:

```asm
00003e7c: ldr r3,[r2,r3]
00003e7e: mov pc,r3
00003e8c: add sp,#0xc
00003e8e: pop {pc}
00003f88: movw r0,#0x2e6d
00003f8c: push {r4,lr}
00003f8e: movt r0,#0x0
00003f92: bl 0x00002098
00003f96: pop {r4,pc}
00003f98: movw r3,#0x5cb8
00003f9c: movt r3,#0x2000
00003fa0: ldrb r0,[r3,#0x0]
00003fa2: uxtb r0,r0
00003fa4: bx lr
00003fa8: movw r3,#0x5cb6
```

```c

void FUN_00003f88(void)

{
  FUN_00002098(0x2e6d);
  return;
}
```

### `00002e6c` `FUN_00002b44`

- no direct function callers found

#### Target `FUN_00002b44` @ `00002b44`

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
/* ... truncated ... */
```

### `00003ab8` `FUN_00003ab8`

- `FUN_000020a4` @ `000020a4`

#### Target `FUN_00003ab8` @ `00003ab8`

```c

undefined4 FUN_00003ab8(void)

{
  return 0x200040a0;
}
```

#### Caller `FUN_000020a4` @ `000020a4`

Site `000020aa`:

```asm
00002098: movw r3,#0x4298
0000209c: movt r3,#0x2000
000020a0: str r0,[r3,#0x0]
000020a2: bx lr
000020a4: push {r4,r5,r6,r7,lr}
000020a6: mov lr,r8
000020a8: push {lr}
000020aa: bl 0x00003ab8
000020ae: movw r5,#0x4321
000020b2: movw r6,#0x4320
000020b6: movw r7,#0x4294
000020ba: movs r4,r0
000020bc: movt r5,#0x2000
000020c0: movt r6,#0x2000
000020c4: movt r7,#0x2000
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

### `00003f88` `FUN_00003f88`

- `FUN_00001e5c` @ `00001e5c`

#### Target `FUN_00003f88` @ `00003f88`

```c

void FUN_00003f88(void)

{
  FUN_00002098(0x2e6d);
  return;
}
```

#### Caller `FUN_00001e5c` @ `00001e5c`

Site `00001e88`:

```asm
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
00001ea4: movw r0,#0x5d04
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

## RAM References

### `20004290`

- from `000019e4` in `FUN_000019c0` @ `000019c0` type=WRITE
- from `000019f2` in `FUN_000019e8` @ `000019e8` type=READ
- from `000019ee` in `FUN_000019e8` @ `000019e8` type=PARAM
- from `00001b3a` in `FUN_00001b30` @ `00001b30` type=READ
- from `00001bfa` in `FUN_00001bf0` @ `00001bf0` type=READ
- from `00001c96` in `FUN_00001c8c` @ `00001c8c` type=READ
- from `00001d04` in `FUN_00001cfc` @ `00001cfc` type=READ

#### Function `FUN_000019c0` @ `000019c0`

Site `000019e4`:

```asm
000019d2: cmp r0,#0xe
000019d4: beq 0x000019d8
000019d6: pop {r4,pc}
000019d8: movw r3,#0x4290
000019dc: movs r2,#0x1
000019de: movt r3,#0x2000
000019e2: movs r0,#0x0
000019e4: strb r2,[r3,#0x0]
000019e6: b 0x000019d6
000019e8: movw r3,#0x4290
000019ec: push {r4,r5,r6,lr}
000019ee: movt r3,#0x2000
000019f2: ldrb r6,[r3,#0x0]
000019f4: sub sp,#0x48
000019f6: cmp r6,#0x0
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

int FUN_000019c0(undefined4 param_1,undefined4 param_2,undefined4 param_3)

{
  int iVar1;
  
  iVar1 = FUN_0000657c(DAT_000098c0,_FUN_000098c4,param_3,0x98c8);
  if ((iVar1 == 0) || (iVar1 == 0xe)) {
    iVar1 = 0;
    DAT_20004290 = 1;
  }
  return iVar1;
}
```

#### Function `FUN_000019e8` @ `000019e8`

Site `000019f2`:

```asm
000019de: movt r3,#0x2000
000019e2: movs r0,#0x0
000019e4: strb r2,[r3,#0x0]
000019e6: b 0x000019d6
000019e8: movw r3,#0x4290
000019ec: push {r4,r5,r6,lr}
000019ee: movt r3,#0x2000
000019f2: ldrb r6,[r3,#0x0]
000019f4: sub sp,#0x48
000019f6: cmp r6,#0x0
000019f8: beq 0x00001aae
000019fa: movs r1,#0x0
000019fc: add r5,sp,#0x4
000019fe: movs r2,#0x44
00001a00: movs r0,r5
```

Site `000019ee`:

```asm
000019dc: movs r2,#0x1
000019de: movt r3,#0x2000
000019e2: movs r0,#0x0
000019e4: strb r2,[r3,#0x0]
000019e6: b 0x000019d6
000019e8: movw r3,#0x4290
000019ec: push {r4,r5,r6,lr}
000019ee: movt r3,#0x2000
000019f2: ldrb r6,[r3,#0x0]
000019f4: sub sp,#0x48
000019f6: cmp r6,#0x0
000019f8: beq 0x00001aae
000019fa: movs r1,#0x0
000019fc: add r5,sp,#0x4
000019fe: movs r2,#0x44
```

```c

int FUN_000019e8(void)

{
  undefined4 uVar1;
  int iVar2;
  char cVar3;
  int local_54;
  short local_50;
  undefined1 auStack_4e [2];
  undefined1 auStack_4c [14];
  undefined1 local_3e;
  undefined1 local_3d;
  undefined1 local_3c;
  undefined2 local_3a;
  undefined2 local_38;
  undefined1 local_36;
  undefined1 auStack_34 [10];
  undefined1 uStack_2a;
  char cStack_29;
  undefined1 auStack_28 [10];
  undefined1 uStack_1e;
  char cStack_1d;
  
  cVar3 = DAT_20004290;
  if (DAT_20004290 == '\0') {
    iVar2 = 0x21;
  }
  else {
    FUN_0000a578(&local_54,0x40100000,0x44);
    if ((local_54 == -0x35014542) && (local_50 == 9)) {
      iVar2 = FUN_000015fc(auStack_4c);
      if (iVar2 == 0) {
        FUN_000034a8(local_3e);
        FUN_000034b4(local_3d);
        FUN_000034d4(local_3c);
        FUN_000034c4(local_3a,local_38);
        FUN_000034e0(local_36);
        if (cStack_29 != '\0') {
          FUN_00003428(0,auStack_34,uStack_2a);
        }
        if (cStack_1d != '\0') {
          FUN_00003428(1,auStack_28,uStack_1e);
        }
      }
    }
    else {
      FUN_0000a568(auStack_4e,0,0x3e);
      local_54 = -0x35014542;
      local_50 = 9;
      iVar2 = FUN_00001880(auStack_4c);
      if (iVar2 == 0) {
        iVar2 = FUN_000034ec();
        if (iVar2 != 0) {
          FUN_0000a578(&local_3e,iVar2,10);
        }
        iVar2 = FUN_00003508(0,auStack_34);
        cStack_29 = cVar3;
        if (iVar2 != 0) {
          FUN_0000a568(auStack_34,0,10);
          uStack_2a = 5;
          cStack_29 = '\0';
        }
        iVar2 = FUN_00003508(1,auStack_28);
        if (iVar2 != 0) {
          FUN_0000a568(auStack_28,0,10);
          cVar3 = '\0';
          uStack_1e = 5;
        }
        uVar1 = DAT_000098c0;
        cStack_1d = cVar3;
        iVar2 = FUN_00006b00(DAT_000098c0,0x40100000,1);
        if (iVar2 == 0) {
          iVar2 = FUN_00006cb4(uVar1,&local_54,0x40100000,0x44);
        }
      }
    }
  }
  return iVar2;
}
```

#### Function `FUN_00001b30` @ `00001b30`

Site `00001b3a`:

```asm
00001b26: ldrb r2,[r5,r3]
00001b28: movs r0,#0x0
00001b2a: bl 0x00003428
00001b2e: b 0x00001ae4
00001b30: movw r3,#0x4290
00001b34: push {r4,lr}
00001b36: movt r3,#0x2000
00001b3a: ldrb r3,[r3,#0x0]
00001b3c: sub sp,#0x48
00001b3e: cmp r3,#0x0
00001b40: beq 0x00001bbe
00001b42: movs r0,#0xa
00001b44: movs r2,#0x3e
00001b46: movs r1,#0x0
00001b48: add r0,sp
```

```c

int FUN_00001b30(void)

{
  undefined4 uVar1;
  int iVar2;
  undefined4 local_4c;
  undefined2 local_48;
  undefined1 auStack_46 [2];
  undefined1 auStack_44 [14];
  undefined1 auStack_36 [10];
  undefined1 auStack_2c [10];
  undefined1 uStack_22;
  undefined1 auStack_20 [10];
  undefined1 uStack_16;
  
  if (DAT_20004290 == '\0') {
    iVar2 = 0x21;
  }
  else {
    FUN_0000a568(auStack_46,0,0x3e);
    local_4c = 0xcafebabe;
    local_48 = 9;
    iVar2 = FUN_00001880(auStack_44);
    if (iVar2 == 0) {
      iVar2 = FUN_000034ec();
      if (iVar2 != 0) {
        FUN_0000a578(auStack_36,iVar2,10);
      }
      iVar2 = FUN_00003508(0,auStack_2c);
      if (iVar2 != 0) {
        FUN_0000a568(auStack_2c,0,0xc);
        uStack_22 = 5;
      }
      iVar2 = FUN_00003508(1,auStack_20);
      if (iVar2 != 0) {
        FUN_0000a568(auStack_20,0,0xc);
        uStack_16 = 5;
      }
      uVar1 = DAT_000098c0;
      iVar2 = FUN_00006b00(DAT_000098c0,0x40100000,1);
      if (iVar2 == 0) {
        iVar2 = FUN_00006cb4(uVar1,&local_4c,0x40100000,0x44);
      }
    }
  }
  return iVar2;
}
```

#### Function `FUN_00001bf0` @ `00001bf0`

Site `00001bfa`:

```asm
00001be6: movs r2,#0x5
00001be8: adds r1,#0x4
00001bea: strb r2,[r1,r3]
00001bec: b 0x00001b86
00001bf0: movw r3,#0x4290
00001bf4: push {r4,lr}
00001bf6: movt r3,#0x2000
00001bfa: ldrb r3,[r3,#0x0]
00001bfc: sub sp,#0x8
00001bfe: cmp r3,#0x0
00001c00: beq 0x00001c7a
00001c02: movw r3,#0x400
00001c06: movw r2,#0xbeef
00001c0a: movt r3,#0x4010
00001c0e: ldrh r1,[r3,#0x4]
```

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

#### Function `FUN_00001c8c` @ `00001c8c`

Site `00001c96`:

```asm
00001c82: movt r3,#0x2000
00001c86: strb r0,[r3,#0x0]
00001c88: movs r0,#0x0
00001c8a: b 0x00001c52
00001c8c: movw r3,#0x4290
00001c90: push {r4,r5,lr}
00001c92: movt r3,#0x2000
00001c96: ldrb r3,[r3,#0x0]
00001c98: movs r4,r0
00001c9a: sub sp,#0xc
00001c9c: cmp r3,#0x0
00001c9e: beq 0x00001cf8
00001ca0: movw r3,#0xbeef
00001ca4: movt r3,#0xdead
00001ca8: mov r2,sp
```

```c

int FUN_00001c8c(undefined1 param_1)

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
    iVar2 = FUN_00006b00(DAT_000098c0,&DAT_40100400,1);
    if ((iVar2 == 0) && (iVar2 = FUN_00006cb4(uVar1,&local_18,&DAT_40100400,8), iVar2 == 0)) {
      DAT_20004080 = param_1;
    }
  }
  return iVar2;
}
```

#### Function `FUN_00001cfc` @ `00001cfc`

Site `00001d04`:

```asm
00001cf0: movt r3,#0x2000
00001cf4: strb r4,[r3,#0x0]
00001cf6: b 0x00001cd2
00001cf8: movs r0,#0x21
00001cfa: b 0x00001cd2
00001cfc: movw r3,#0x4290
00001d00: movt r3,#0x2000
00001d04: ldrb r3,[r3,#0x0]
00001d06: push {r4,lr}
00001d08: cbz r3,0x00001d22
00001d0a: cbz r0,0x00001d1e
00001d0c: movw r1,#0x400
00001d10: movs r2,#0x8
00001d12: movt r1,#0x4010
00001d16: bl 0x0000a578
```

```c

undefined4 FUN_00001cfc(int param_1)

{
  undefined4 uVar1;
  
  if (DAT_20004290 == '\0') {
    uVar1 = 0x21;
  }
  else if (param_1 == 0) {
    uVar1 = 1;
  }
  else {
    FUN_0000a578(param_1,&DAT_40100400,8);
    uVar1 = 0;
  }
  return uVar1;
}
```

### `20004291`

- from `00001e82` in `FUN_00001e5c` @ `00001e5c` type=WRITE
- from `00001e7c` in `FUN_00001e5c` @ `00001e5c` type=PARAM
- from `00001e58` in `FUN_00001e50` @ `00001e50` type=READ

#### Function `FUN_00001e5c` @ `00001e5c`

Site `00001e82`:

```asm
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
```

Site `00001e7c`:

```asm
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

#### Function `FUN_00001e50` @ `00001e50`

Site `00001e58`:

```asm
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
```

```c

undefined1 FUN_00001e50(void)

{
  return DAT_20004291;
}
```

### `20004292`

- from `00002128` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `00002122` in `FUN_000020a4` @ `000020a4` type=PARAM
- from `000021b4` in `FUN_000020a4` @ `000020a4` type=READ

#### Function `FUN_000020a4` @ `000020a4`

Site `00002128`:

```asm
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
00002132: pop {r7}
00002134: mov r8,r7
00002136: pop {r4,r5,r6,r7,pc}
00002138: ldrb r2,[r6,#0x0]
```

Site `00002122`:

```asm
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
00002132: pop {r7}
00002134: mov r8,r7
```

Site `000021b4`:

```asm
000021a2: mov r2,r8
000021a4: strb r3,[r5,#0x0]
000021a6: strb r3,[r2,#0x0]
000021a8: b 0x000020c8
000021aa: movw r3,#0x4292
000021ae: movt r3,#0x2000
000021b2: adds r2,#0x1
000021b4: ldrb r3,[r3,#0x0]
000021b6: uxtb r2,r2
000021b8: strb r2,[r6,#0x0]
000021ba: cmp r3,r2
000021bc: bls 0x000021c0
000021be: b 0x000020c8
000021c0: movs r3,#0x2
000021c2: strb r3,[r5,#0x0]
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

### `20004294`

- from `0000211a` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `0000213a` in `FUN_000020a4` @ `000020a4` type=READ

#### Function `FUN_000020a4` @ `000020a4`

Site `0000211a`:

```asm
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
```

Site `0000213a`:

```asm
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

### `20004298`

- from `000020a0` in `FUN_00002098` @ `00002098` type=WRITE
- from `0000218a` in `FUN_000020a4` @ `000020a4` type=READ

#### Function `FUN_00002098` @ `00002098`

Site `000020a0`:

```asm
00002088: bl 0x00001d6c
0000208c: pop {r3,r4,r5,r6,r7,pc}
0000208e: movw r4,#0x95f8
00002092: movt r4,#0x0
00002096: b 0x00002044
00002098: movw r3,#0x4298
0000209c: movt r3,#0x2000
000020a0: str r0,[r3,#0x0]
000020a2: bx lr
000020a4: push {r4,r5,r6,r7,lr}
000020a6: mov lr,r8
000020a8: push {lr}
000020aa: bl 0x00003ab8
000020ae: movw r5,#0x4321
000020b2: movw r6,#0x4320
```

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00002098(undefined4 param_1)

{
  _DAT_20004298 = param_1;
  return;
}
```

#### Function `FUN_000020a4` @ `000020a4`

Site `0000218a`:

```asm
00002172: movw r3,#0x42a0
00002176: movt r3,#0x2000
0000217a: strb r0,[r3,r2]
0000217c: b 0x000020c8
0000217e: movw r3,#0x4298
00002182: movw r8,#0x429c
00002186: movt r3,#0x2000
0000218a: ldr r3,[r3,#0x0]
0000218c: movt r8,#0x2000
00002190: cbz r3,0x000021a0
00002192: mov r2,r8
00002194: movw r0,#0x42a0
00002198: ldrb r1,[r2,#0x0]
0000219a: movt r0,#0x2000
0000219e: blx r3
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

### `2000429c`

- from `00002100` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `000020fc` in `FUN_000020a4` @ `000020a4` type=PARAM
- from `00002162` in `FUN_000020a4` @ `000020a4` type=READ
- from `00002164` in `FUN_000020a4` @ `000020a4` type=READ
- from `00002170` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `0000216c` in `FUN_000020a4` @ `000020a4` type=PARAM
- from `000021a6` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `000021a2` in `FUN_000020a4` @ `000020a4` type=PARAM
- from `000021d4` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `000021d2` in `FUN_000020a4` @ `000020a4` type=PARAM
- from `00002198` in `FUN_000020a4` @ `000020a4` type=READ
- from `00002192` in `FUN_000020a4` @ `000020a4` type=PARAM

#### Function `FUN_000020a4` @ `000020a4`

Site `00002100`:

```asm
000020ec: movw r8,#0x429c
000020f0: movs r1,#0x1
000020f2: movt r2,#0x2000
000020f6: movt r8,#0x2000
000020fa: strb r1,[r2,#0x0]
000020fc: mov r2,r8
000020fe: strb r1,[r5,#0x0]
00002100: strb r3,[r2,#0x0]
00002102: bl 0x00001e50
00002106: movw r3,#0x4294
0000210a: movt r3,#0x2000
0000210e: cmp r0,#0x0
00002110: bne 0x000021e8
00002112: movw r2,#0x95f4
00002116: movt r2,#0x0
```

Site `000020fc`:

```asm
000020e6: bne 0x000020c8
000020e8: movw r2,#0x4320
000020ec: movw r8,#0x429c
000020f0: movs r1,#0x1
000020f2: movt r2,#0x2000
000020f6: movt r8,#0x2000
000020fa: strb r1,[r2,#0x0]
000020fc: mov r2,r8
000020fe: strb r1,[r5,#0x0]
00002100: strb r3,[r2,#0x0]
00002102: bl 0x00001e50
00002106: movw r3,#0x4294
0000210a: movt r3,#0x2000
0000210e: cmp r0,#0x0
00002110: bne 0x000021e8
```

Site `00002162`:

```asm
00002150: cmp r0,#0xf0
00002152: beq 0x000021d8
00002154: movw r8,#0x429c
00002158: movt r8,#0x2000
0000215c: lsls r3,r0,#0x18
0000215e: bmi 0x000021a0
00002160: mov r3,r8
00002162: ldrb r2,[r3,#0x0]
00002164: ldrb r3,[r3,#0x0]
00002166: sxtb r3,r3
00002168: cmp r3,#0x0
0000216a: blt 0x000021a0
0000216c: mov r1,r8
0000216e: adds r3,r2,#0x1
00002170: strb r3,[r1,#0x0]
```

Site `00002164`:

```asm
00002152: beq 0x000021d8
00002154: movw r8,#0x429c
00002158: movt r8,#0x2000
0000215c: lsls r3,r0,#0x18
0000215e: bmi 0x000021a0
00002160: mov r3,r8
00002162: ldrb r2,[r3,#0x0]
00002164: ldrb r3,[r3,#0x0]
00002166: sxtb r3,r3
00002168: cmp r3,#0x0
0000216a: blt 0x000021a0
0000216c: mov r1,r8
0000216e: adds r3,r2,#0x1
00002170: strb r3,[r1,#0x0]
00002172: movw r3,#0x42a0
```

Site `00002170`:

```asm
00002162: ldrb r2,[r3,#0x0]
00002164: ldrb r3,[r3,#0x0]
00002166: sxtb r3,r3
00002168: cmp r3,#0x0
0000216a: blt 0x000021a0
0000216c: mov r1,r8
0000216e: adds r3,r2,#0x1
00002170: strb r3,[r1,#0x0]
00002172: movw r3,#0x42a0
00002176: movt r3,#0x2000
0000217a: strb r0,[r3,r2]
0000217c: b 0x000020c8
0000217e: movw r3,#0x4298
00002182: movw r8,#0x429c
00002186: movt r3,#0x2000
```

Site `0000216c`:

```asm
0000215e: bmi 0x000021a0
00002160: mov r3,r8
00002162: ldrb r2,[r3,#0x0]
00002164: ldrb r3,[r3,#0x0]
00002166: sxtb r3,r3
00002168: cmp r3,#0x0
0000216a: blt 0x000021a0
0000216c: mov r1,r8
0000216e: adds r3,r2,#0x1
00002170: strb r3,[r1,#0x0]
00002172: movw r3,#0x42a0
00002176: movt r3,#0x2000
0000217a: strb r0,[r3,r2]
0000217c: b 0x000020c8
0000217e: movw r3,#0x4298
```

Site `000021a6`:

```asm
00002194: movw r0,#0x42a0
00002198: ldrb r1,[r2,#0x0]
0000219a: movt r0,#0x2000
0000219e: blx r3
000021a0: movs r3,#0x0
000021a2: mov r2,r8
000021a4: strb r3,[r5,#0x0]
000021a6: strb r3,[r2,#0x0]
000021a8: b 0x000020c8
000021aa: movw r3,#0x4292
000021ae: movt r3,#0x2000
000021b2: adds r2,#0x1
000021b4: ldrb r3,[r3,#0x0]
000021b6: uxtb r2,r2
000021b8: strb r2,[r6,#0x0]
```

Site `000021a2`:

```asm
00002190: cbz r3,0x000021a0
00002192: mov r2,r8
00002194: movw r0,#0x42a0
00002198: ldrb r1,[r2,#0x0]
0000219a: movt r0,#0x2000
0000219e: blx r3
000021a0: movs r3,#0x0
000021a2: mov r2,r8
000021a4: strb r3,[r5,#0x0]
000021a6: strb r3,[r2,#0x0]
000021a8: b 0x000020c8
000021aa: movw r3,#0x4292
000021ae: movt r3,#0x2000
000021b2: adds r2,#0x1
000021b4: ldrb r3,[r3,#0x0]
```

Site `000021d4`:

```asm
000021c2: strb r3,[r5,#0x0]
000021c4: b 0x000020c8
000021c6: strb r3,[r6,#0x0]
000021c8: movw r8,#0x429c
000021cc: movt r8,#0x2000
000021d0: movs r3,#0x0
000021d2: mov r2,r8
000021d4: strb r3,[r2,#0x0]
000021d6: b 0x000020c8
000021d8: movw r3,#0x4320
000021dc: movs r2,#0x1
000021de: movt r3,#0x2000
000021e2: strb r2,[r5,#0x0]
000021e4: strb r2,[r3,#0x0]
000021e6: b 0x000021c8
```

Site `000021d2`:

```asm
000021c0: movs r3,#0x2
000021c2: strb r3,[r5,#0x0]
000021c4: b 0x000020c8
000021c6: strb r3,[r6,#0x0]
000021c8: movw r8,#0x429c
000021cc: movt r8,#0x2000
000021d0: movs r3,#0x0
000021d2: mov r2,r8
000021d4: strb r3,[r2,#0x0]
000021d6: b 0x000020c8
000021d8: movw r3,#0x4320
000021dc: movs r2,#0x1
000021de: movt r3,#0x2000
000021e2: strb r2,[r5,#0x0]
000021e4: strb r2,[r3,#0x0]
```

Site `00002198`:

```asm
00002182: movw r8,#0x429c
00002186: movt r3,#0x2000
0000218a: ldr r3,[r3,#0x0]
0000218c: movt r8,#0x2000
00002190: cbz r3,0x000021a0
00002192: mov r2,r8
00002194: movw r0,#0x42a0
00002198: ldrb r1,[r2,#0x0]
0000219a: movt r0,#0x2000
0000219e: blx r3
000021a0: movs r3,#0x0
000021a2: mov r2,r8
000021a4: strb r3,[r5,#0x0]
000021a6: strb r3,[r2,#0x0]
000021a8: b 0x000020c8
```

Site `00002192`:

```asm
0000217c: b 0x000020c8
0000217e: movw r3,#0x4298
00002182: movw r8,#0x429c
00002186: movt r3,#0x2000
0000218a: ldr r3,[r3,#0x0]
0000218c: movt r8,#0x2000
00002190: cbz r3,0x000021a0
00002192: mov r2,r8
00002194: movw r0,#0x42a0
00002198: ldrb r1,[r2,#0x0]
0000219a: movt r0,#0x2000
0000219e: blx r3
000021a0: movs r3,#0x0
000021a2: mov r2,r8
000021a4: strb r3,[r5,#0x0]
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

### `200042a0`

- no direct references found

### `20004320`

- from `000020fa` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `000021e4` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `00002138` in `FUN_000020a4` @ `000020a4` type=READ
- from `000021c6` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `000021b8` in `FUN_000020a4` @ `000020a4` type=WRITE

#### Function `FUN_000020a4` @ `000020a4`

Site `000020fa`:

```asm
000020e4: cmp r0,#0xf0
000020e6: bne 0x000020c8
000020e8: movw r2,#0x4320
000020ec: movw r8,#0x429c
000020f0: movs r1,#0x1
000020f2: movt r2,#0x2000
000020f6: movt r8,#0x2000
000020fa: strb r1,[r2,#0x0]
000020fc: mov r2,r8
000020fe: strb r1,[r5,#0x0]
00002100: strb r3,[r2,#0x0]
00002102: bl 0x00001e50
00002106: movw r3,#0x4294
0000210a: movt r3,#0x2000
0000210e: cmp r0,#0x0
```

Site `000021e4`:

```asm
000021d2: mov r2,r8
000021d4: strb r3,[r2,#0x0]
000021d6: b 0x000020c8
000021d8: movw r3,#0x4320
000021dc: movs r2,#0x1
000021de: movt r3,#0x2000
000021e2: strb r2,[r5,#0x0]
000021e4: strb r2,[r3,#0x0]
000021e6: b 0x000021c8
000021e8: movw r2,#0x95f8
000021ec: movt r2,#0x0
000021f0: b 0x0000211a
00002288: push {r4,r5,r6,r7,lr}
0000228a: mov r5,r8
0000228c: movw r8,#0x45ca
```

Site `00002138`:

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
```

Site `000021c6`:

```asm
000021b8: strb r2,[r6,#0x0]
000021ba: cmp r3,r2
000021bc: bls 0x000021c0
000021be: b 0x000020c8
000021c0: movs r3,#0x2
000021c2: strb r3,[r5,#0x0]
000021c4: b 0x000020c8
000021c6: strb r3,[r6,#0x0]
000021c8: movw r8,#0x429c
000021cc: movt r8,#0x2000
000021d0: movs r3,#0x0
000021d2: mov r2,r8
000021d4: strb r3,[r2,#0x0]
000021d6: b 0x000020c8
000021d8: movw r3,#0x4320
```

Site `000021b8`:

```asm
000021a6: strb r3,[r2,#0x0]
000021a8: b 0x000020c8
000021aa: movw r3,#0x4292
000021ae: movt r3,#0x2000
000021b2: adds r2,#0x1
000021b4: ldrb r3,[r3,#0x0]
000021b6: uxtb r2,r2
000021b8: strb r2,[r6,#0x0]
000021ba: cmp r3,r2
000021bc: bls 0x000021c0
000021be: b 0x000020c8
000021c0: movs r3,#0x2
000021c2: strb r3,[r5,#0x0]
000021c4: b 0x000020c8
000021c6: strb r3,[r6,#0x0]
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

### `20004321`

- from `000020d6` in `FUN_000020a4` @ `000020a4` type=READ
- from `000020fe` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `00002148` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `000021a4` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `000021e2` in `FUN_000020a4` @ `000020a4` type=WRITE
- from `000021c2` in `FUN_000020a4` @ `000020a4` type=WRITE

#### Function `FUN_000020a4` @ `000020a4`

Site `000020d6`:

```asm
000020c0: movt r6,#0x2000
000020c4: movt r7,#0x2000
000020c8: movs r0,r4
000020ca: bl 0x00001d54
000020ce: cbz r0,0x00002132
000020d0: movs r0,r4
000020d2: bl 0x00001d94
000020d6: ldrb r3,[r5,#0x0]
000020d8: cmp r3,#0x1
000020da: beq 0x00002138
000020dc: cmp r3,#0x2
000020de: beq 0x0000214c
000020e0: cmp r3,#0x0
000020e2: bne 0x00002146
000020e4: cmp r0,#0xf0
```

Site `000020fe`:

```asm
000020e8: movw r2,#0x4320
000020ec: movw r8,#0x429c
000020f0: movs r1,#0x1
000020f2: movt r2,#0x2000
000020f6: movt r8,#0x2000
000020fa: strb r1,[r2,#0x0]
000020fc: mov r2,r8
000020fe: strb r1,[r5,#0x0]
00002100: strb r3,[r2,#0x0]
00002102: bl 0x00001e50
00002106: movw r3,#0x4294
0000210a: movt r3,#0x2000
0000210e: cmp r0,#0x0
00002110: bne 0x000021e8
00002112: movw r2,#0x95f4
```

Site `00002148`:

```asm
0000213a: ldr r1,[r7,#0x0]
0000213c: ldrb r1,[r1,r2]
0000213e: cmp r1,r0
00002140: beq 0x000021aa
00002142: cmp r0,#0xf0
00002144: beq 0x000021c6
00002146: movs r3,#0x0
00002148: strb r3,[r5,#0x0]
0000214a: b 0x000020c8
0000214c: cmp r0,#0xf7
0000214e: beq 0x0000217e
00002150: cmp r0,#0xf0
00002152: beq 0x000021d8
00002154: movw r8,#0x429c
00002158: movt r8,#0x2000
```

Site `000021a4`:

```asm
00002192: mov r2,r8
00002194: movw r0,#0x42a0
00002198: ldrb r1,[r2,#0x0]
0000219a: movt r0,#0x2000
0000219e: blx r3
000021a0: movs r3,#0x0
000021a2: mov r2,r8
000021a4: strb r3,[r5,#0x0]
000021a6: strb r3,[r2,#0x0]
000021a8: b 0x000020c8
000021aa: movw r3,#0x4292
000021ae: movt r3,#0x2000
000021b2: adds r2,#0x1
000021b4: ldrb r3,[r3,#0x0]
000021b6: uxtb r2,r2
```

Site `000021e2`:

```asm
000021d0: movs r3,#0x0
000021d2: mov r2,r8
000021d4: strb r3,[r2,#0x0]
000021d6: b 0x000020c8
000021d8: movw r3,#0x4320
000021dc: movs r2,#0x1
000021de: movt r3,#0x2000
000021e2: strb r2,[r5,#0x0]
000021e4: strb r2,[r3,#0x0]
000021e6: b 0x000021c8
000021e8: movw r2,#0x95f8
000021ec: movt r2,#0x0
000021f0: b 0x0000211a
00002288: push {r4,r5,r6,r7,lr}
0000228a: mov r5,r8
```

Site `000021c2`:

```asm
000021b4: ldrb r3,[r3,#0x0]
000021b6: uxtb r2,r2
000021b8: strb r2,[r6,#0x0]
000021ba: cmp r3,r2
000021bc: bls 0x000021c0
000021be: b 0x000020c8
000021c0: movs r3,#0x2
000021c2: strb r3,[r5,#0x0]
000021c4: b 0x000020c8
000021c6: strb r3,[r6,#0x0]
000021c8: movw r8,#0x429c
000021cc: movt r8,#0x2000
000021d0: movs r3,#0x0
000021d2: mov r2,r8
000021d4: strb r3,[r2,#0x0]
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

