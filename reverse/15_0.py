"""
ehco -en "\x02\xce\x83\xe1\xc9\x67\xda\x96" |/challenge/ba...
pwn.college{8nV9VX4M2KVC-1NfGf11-3MZtoQ.01M3IDL1kjMzQzW}


almost the same as the others but with more obfuscated 

now all print statments and exit are used with emulated archi


by sendin eachi char in reg before printing
"""

"""




1---> open flag  and write
4---->read 
8--->write
16--->sleep
32----->exit

  
  uVar3 = describe_register(reg_id);
  printf("[s] SYS %#hhx %s\n",(ulong)sys_call_id,uVar3);
  if ((sys_call_id & 1) != 0) {
    puts("[s] ... open");
    uVar1 = sys_open(pointer_yan,pointer_yan->field0_0x0 + (byte)pointer_yan->reg_1,
                     pointer_yan->reg_2,pointer_yan->reg_3);
    write_register(pointer_yan,reg_id,uVar1);
  }
  if ((sys_call_id & 4) != 0) {
    puts("[s] ... read_memory");
    uVar4 = 0x100 - (byte)pointer_yan->reg_2;
    bVar2 = pointer_yan->reg_3;
    if (uVar4 <= bVar2) {
      bVar2 = (byte)uVar4;
    }
    uVar1 = sys_read(pointer_yan,pointer_yan->reg_1,
                     pointer_yan->field0_0x0 + (byte)pointer_yan->reg_2,bVar2);
    write_register(pointer_yan,reg_id,uVar1);
  }
  if ((sys_call_id & 8) != 0) {
    puts("[s] ... write");
    uVar4 = 0x100 - (byte)pointer_yan->reg_2;
    bVar2 = pointer_yan->reg_3;
    if (uVar4 <= bVar2) {
      bVar2 = (byte)uVar4;
    }
    uVar1 = sys_write(pointer_yan,pointer_yan->reg_1,
                      pointer_yan->field0_0x0 + (byte)pointer_yan->reg_2,bVar2);
    write_register(pointer_yan,reg_id,uVar1);
  }
  if ((sys_call_id & 0x10) != 0) {
    puts("[s] ... sleep");
    uVar1 = sys_sleep(pointer_yan,pointer_yan->reg_1);
    write_register(pointer_yan,reg_id,uVar1);
  }
  if ((sys_call_id & 0x20) != 0) {
    puts("[s] ... exit");
    sys_exit(pointer_yan,pointer_yan->reg_1);
  }
  if (reg_id != '\0') {
    bVar2 = read_register(pointer_yan,reg_id);
    uVar3 = describe_register(reg_id);
    printf("[s] ... return value (in register %s): %#hhx\n",uVar3,(ulong)bVar2);
  }
  return;
}





  interpret_imm(yan85,16,0x69);
  interpret_imm(yan85,64,6);
  interpret_imm(yan85,2,0);
                    /* r16=0x69
                       r64=6
                       r2=0 */
  interpret_sys(yan85,4,2);// it will open 
  interpret_imm(yan85,0x10,0x89);
  interpret_imm(yan85,0x40,1);
  interpret_imm(yan85,2,0xa3);
  interpret_stm(yan85,0x10,2);
  interpret_add(yan85,0x10,0x40);
  interpret_imm(yan85,2,0xe0);
  interpret_stm(yan85,0x10,2);
  interpret_add(yan85,0x10,0x40);
  interpret_imm(yan85,2,0x7f);
  interpret_stm(yan85,0x10,2);
  interpret_add(yan85,0x10,0x40);
  interpret_imm(yan85,2,199);
  interpret_stm(yan85,0x10,2);
  interpret_add(yan85,0x10,0x40);
  interpret_imm(yan85,2,0x94);
  interpret_stm(yan85,0x10,2);
  interpret_add(yan85,0x10,0x40);
  interpret_imm(yan85,2,0xd1);
  interpret_stm(yan85,0x10,2);
  interpret_add(yan85,0x10,0x40)
"""


def getReg_key(reg):
    return f"reg_{reg}"

def get_reg_value(stuff,reg):
    reg=getReg_key(reg)
    return stuff[reg]


def interpret_imm(stuff,reg,imm):
    reg=get_reg_value(reg)
    stuff[reg]=imm


def interpret_sm(stuff,src,dst):
    src=get_reg_value(stuff,src)
    dst=get_reg_value(stuff,dst)
    stuff['memory'][dst]=src

def interpret_add(stuff,reg1,reg2)
    reg1=get_reg_value(reg1)
    reg2=get_reg_value(reg2)
    reg_dst=getReg_key(reg1)
    stuff[reg_dst]=reg1+reg2




def main():
    stuff={
        'memory':[ 0 for i in range(255)],
        'reg_64':0,
        'reg_8':0,
        'reg_16':0,
        'reg_8':0,
        'reg_4':0,
        'reg_1':0,
        'reg_2':0,
        'reg_32':0

    }

"""challenge 14.1
   
  load_imdd(param_1,4,100);
  load_imdd(param_1,0x40,8);
  load_imdd(param_1,8,0);
  sys_call(param_1,2,8); read stdin


  load_imdd(param_1,4,0x84);
  load_imdd(param_1,0x40,1);
  load_imdd(param_1,8,0x54);*****
  load_in_mem(param_1,4,8);
  add_2regs(param_1,4,0x40);
  load_imdd(param_1,8,0xd);*****
  load_in_mem(param_1,4,8);
  add_2regs(param_1,4,0x40);
  load_imdd(param_1,8,0x8b);******
  load_in_mem(param_1,4,8);
  add_2regs(param_1,4,0x40);
  load_imdd(param_1,8,0xab);******
  load_in_mem(param_1,4,8);
  add_2regs(param_1,4,0x40);
  load_imdd(param_1,8,0x2e);******
  load_in_mem(param_1,4,8);
  add_2regs(param_1,4,0x40);
  load_imdd(param_1,8,0xd3);******
  load_in_mem(param_1,4,8);
  add_2regs(param_1,4,0x40);
  load_imdd(param_1,8,0xcb);******
  load_in_mem(param_1,4,8);
  add_2regs(param_1,4,0x40);
  load_imdd(param_1,8,0x8e);******
  load_in_mem(param_1,4,8);
  add_2regs(param_1,4,0x40);
"""
