"""
\x58\x92\x9a\xe7\x82\x64
pwn.college{Esg5Zdx9t6j4YXHpIWSxbw-M9rO.0VN3IDL1kjMzQzW}


\x51\xd6\xaf\x63\xa6\xbc
pwn.college{wJRaQTfB2yXkEjMgnjgi6jGmdc1.0lN3IDL1kjMzQzW}

as always with yan 85 archi


but now with new emulated task cmp  and ldm task to 

get rid of memcmp functionand no cheese gdb 


FUNCTION CMP [YAN85 , REGID1, REGID2]


  byte bVar1;
  byte bVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  
  uVar3 = describe_register(param_3);
  uVar4 = describe_register(param_2);
  printf("[s] CMP %s %s\n",uVar4,uVar3);
  bVar1 = read_register(yan,param_2);
  bVar2 = read_register(yan,param_3);
  yan->reg_a = 0;
  if (bVar1 < bVar2) {
    yan->reg_a = yan->reg_a | 16;
  }
  if (bVar2 < bVar1) {
    yan->reg_a = yan->reg_a | 1;
  }
  if (bVar1 == bVar2) {
    yan->reg_a = yan->reg_a | 4;
  }
  else {
    yan->reg_a = yan->reg_a | 2;
  }
  if ((bVar1 == 0) && (bVar2 == 0)) {
    yan->reg_a = yan->reg_a | 8;
  }
  return;
     




     the functio will take two regids and cmp them and put the result in reg6


      The flags represent various conditions: less than (0x10), greater than (1),
       equal (4), and not equal (2)
       If both bVar1 and bVar2 are zero, an additional flag (8) is set in yan->reg_a


       the result of all functions will put in varaibles and be compared in the end if one at least 

        of them is differen than 4 it will print incorrect
     


FUNCTION LDM[YAN85,REGID1, REGID2]---------> WILL READ THE CONTENT OF REG2 AS AN ADDRESS AN READ WHAT THERE AND PUT IT IN REG1
    void interpret_ldm(yan85 *param_1,undefined idreg1,undefined idreg2)

{
  undefined uVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  uVar2 = describe_register(idreg2);
  uVar3 = describe_register(idreg1);
  printf("[s] LDM %s = *%s\n",uVar3,uVar2);
  uVar1 = read_register(param_1,idreg2);
  uVar1 = read_memory(param_1,uVar1);
  write_register(param_1,idreg1,uVar1);
  return;
}

"""