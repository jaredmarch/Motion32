# Motion 32 Event Encoder Trace Probe

## Function Callers

### `00001d6c` `FUN_00001d6c`

- `FUN_00001eec` @ `00001eec`
- `FUN_00002030` @ `00002030`
- `FUN_00001f6c` @ `00001f6c`
- `FUN_00001fb0` @ `00001fb0`

#### Caller `FUN_00001eec` @ `00001eec`

Call site `00001f16`:

```asm
00001f02: cmp r3,r0
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
00001f32: bl 0x00001d6c
```

Call site `00001f24`:

```asm
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
00001f32: bl 0x00001d6c
00001f36: ldrb r3,[r5,#0x0]
00001f38: cmp r3,r4
00001f3a: beq 0x00001f4e
00001f3c: movw r0,#0x4084
```

Call site `00001f32`:

```asm
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
00001f3c: movw r0,#0x4084
00001f40: strb r4,[r5,#0x0]
00001f42: subs r4,#0x50
00001f44: uxtb r1,r4
00001f46: movt r0,#0x2000
```

Call site `00001f4a`:

```asm
00001f36: ldrb r3,[r5,#0x0]
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
00001f66: bl 0x00001d6c
```

Call site `00001f58`:

```asm
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
00001f66: bl 0x00001d6c
00001f6a: pop {r3,r4,r5,r6,r7,pc}
00001f6c: movw r3,#0x4081
00001f70: push {r4,lr}
00001f72: movt r3,#0x2000
```

Call site `00001f66`:

```asm
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
00001f72: movt r3,#0x2000
00001f76: ldrb r2,[r3,#0x0]
00001f78: movs r4,r1
00001f7a: cmp r2,r0
00001f7c: beq 0x00001f90
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

Call site `00002052`:

```asm
0000203a: cbnz r0,0x0000208e
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
00002064: cmp r3,#0x0
```

Call site `00002070`:

```asm
0000205c: movs r4,#0x0
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
00002084: movt r0,#0x2000
```

Call site `00002088`:

```asm
00002074: adds r4,#0x1
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
000020a2: bx lr
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

Call site `00001f8c`:

```asm
00001f78: movs r4,r1
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
00001fa8: bl 0x00001d6c
```

Call site `00001f9a`:

```asm
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
00001fa8: bl 0x00001d6c
00001fac: pop {r4,pc}
00001fb0: movw r3,#0x4081
00001fb4: push {r4,lr}
00001fb6: movt r3,#0x2000
```

Call site `00001fa8`:

```asm
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
00001fb6: movt r3,#0x2000
00001fba: ldrb r2,[r3,#0x0]
00001fbc: adds r1,#0x40
00001fbe: uxtb r4,r1
00001fc0: cmp r2,r0
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

Call site `00001fd2`:

```asm
00001fbe: uxtb r4,r1
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
00001fee: bl 0x00001d6c
```

Call site `00001fe0`:

```asm
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
00001fee: bl 0x00001d6c
00001ff2: pop {r4,pc}
00002006: pop {r4,pc}
0000202e: b 0x00002006
00002030: push {r3,r4,r5,r6,r7,lr}
```

Call site `00001fee`:

```asm
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
00002030: push {r3,r4,r5,r6,r7,lr}
00002032: movs r5,r0
00002034: movs r6,r1
00002036: bl 0x00001e50
0000203a: cbnz r0,0x0000208e
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

### `00001eec` `FUN_00001eec`

- `FUN_00002288` @ `00002288`

#### Caller `FUN_00002288` @ `00002288`

Call site `0000231e`:

```asm
0000230e: sxth r2,r2
00002310: cmp r2,r3
00002312: bge 0x000022ca
00002314: ldrh r3,[r4,#0x0]
00002316: movs r0,r5
00002318: strh r3,[r6,#0x0]
0000231a: ldrh r1,[r4,#0x0]
0000231c: sxth r1,r1
0000231e: bl 0x00001eec
00002322: mov r3,r8
00002324: ldrb r1,[r3,#0x0]
00002326: b 0x000022d2
00002328: add sp,#0xc
0000232a: pop {r4,r5,r6,r7}
0000232c: mov r11,r7
0000232e: mov r10,r6
00002330: mov r9,r5
```

Call site `0000233c`:

```asm
0000232c: mov r11,r7
0000232e: mov r10,r6
00002330: mov r9,r5
00002332: mov r8,r4
00002334: pop {r4,r5,r6,r7,pc}
00002336: ldrh r1,[r4,#0x0]
00002338: movs r0,r5
0000233a: sxth r1,r1
0000233c: bl 0x00001eec
00002340: mov r3,r11
00002342: ldr r2,[sp,#0x4]
00002344: strb r3,[r2,#0x0]
00002346: mov r3,r8
00002348: ldrb r1,[r3,#0x0]
0000234a: b 0x000022d2
0000234c: push {r3,r4,r5,r6,r7,lr}
0000234e: mov r7,r8
```

```c

void FUN_00002288(short *param_1)

{
  byte bVar1;
  byte bVar2;
  short *psVar3;
  int iVar4;
  char *local_2c;
  
  if (DAT_200045ca != 0) {
    bVar2 = 0;
    iVar4 = 0xc;
    psVar3 = (short *)&DAT_20004534;
    local_2c = &DAT_200045c8;
    bVar1 = DAT_200045ca;
    do {
      if ((*param_1 < 0xc) || (0x3f4 < *param_1)) {
        iVar4 = 2;
      }
      if ((*psVar3 + iVar4 < (int)*param_1) || ((int)*param_1 < *psVar3 - iVar4)) {
        *psVar3 = *param_1;
        FUN_00001eec(bVar2,(int)*param_1);
        bVar1 = DAT_200045ca;
      }
      else if (*local_2c != '\0') {
        FUN_00001eec(bVar2,(int)*param_1);
        *local_2c = '\0';
        bVar1 = DAT_200045ca;
      }
      bVar2 = bVar2 + 1;
      local_2c = local_2c + 1;
      param_1 = param_1 + 1;
      psVar3 = psVar3 + 1;
    } while (bVar2 < bVar1);
  }
  return;
}
```

### `00001fb0` `FUN_00001fb0`

- `FUN_0000240c` @ `0000240c`

#### Caller `FUN_0000240c` @ `0000240c`

Call site `0000250c`:

```asm
000024f6: pop {r4,r5,r6,pc}
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
```

Call site `0000252c`:

```asm
00002518: movw r2,#0x9664
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
```

Call site `0000254c`:

```asm
00002538: movw r2,#0x9664
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
```

Call site `0000256c`:

```asm
00002558: movw r2,#0x9664
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
```

Call site `0000258c`:

```asm
00002578: movw r2,#0x9664
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
```

Call site `000025b2`:

```asm
0000259e: movw r2,#0x9664
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
```

Call site `000025d2`:

```asm
000025be: movw r2,#0x9664
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
```

Call site `000025f2`:

```asm
000025de: movw r2,#0x9664
000025e2: movt r2,#0x0
000025e6: mov r12,r2
000025e8: lsls r3,r0,#0x3
000025ea: adds r3,r3,r0
000025ec: add r3,r12
000025ee: movs r1,r5
000025f0: ldrb r0,[r3,#0x8]
000025f2: bl 0x00001fb0
000025f6: b 0x000024f6
000025f8: bl 0x00001e50
000025fc: movw r2,#0x9664
00002600: movt r2,#0x0
00002604: mov r12,r2
00002606: lsls r3,r0,#0x3
00002608: adds r3,r3,r0
0000260a: add r3,r12
```

Call site `00002610`:

```asm
000025fc: movw r2,#0x9664
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

### `000020a4` `FUN_000020a4`

- no direct function callers found

### `0000240c` `FUN_0000240c`

- `FUN_00009944` @ `00009944`
- `FUN_00009e1c` @ `00009e1c`

#### Caller `FUN_00009944` @ `00009944`

Call site `00009aa2`:

```asm
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
00009abe: bl 0x00003fec
00009ac2: cmp r0,#0x0
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

#### Caller `FUN_00009e1c` @ `00009e1c`

Call site `00009f56`:

```asm
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
00009f66: movw r0,#0x64c0
00009f6a: movt r0,#0x2000
00009f6e: bl 0x00002288
00009f72: b 0x00009e2a
00009f74: movw r1,#0x3ff
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

## RAM Address References

### `20004081`

- from `00001ef8` in `FUN_00001eec` @ `00001eec` type=READ
- from `00001f08` in `FUN_00001eec` @ `00001eec` type=WRITE
- from `00001f36` in `FUN_00001eec` @ `00001eec` type=READ
- from `00001f40` in `FUN_00001eec` @ `00001eec` type=WRITE
- from `00001f76` in `FUN_00001f6c` @ `00001f6c` type=READ
- from `00001f7e` in `FUN_00001f6c` @ `00001f6c` type=WRITE
- from `00001f72` in `FUN_00001f6c` @ `00001f6c` type=PARAM
- from `00001fba` in `FUN_00001fb0` @ `00001fb0` type=READ
- from `00001fc4` in `FUN_00001fb0` @ `00001fb0` type=WRITE
- from `00001fb6` in `FUN_00001fb0` @ `00001fb0` type=PARAM

### `20004084`

- no direct references found

