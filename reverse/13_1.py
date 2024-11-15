 """read(0,pointervar->memory + 0x33,6);
                    /* writting data in register B id 8 immd value 53 */
  load_imm_to_reg(pointervar,8,0x53);
                    /* so regoster 8 is memory adress register and register 1 is usd as stuffunter inc
                        */
  load_imm_to_reg(pointervar,1,1);
 # load_imm_to_reg(pointervar,0x10,0xa8);
  load_mem_add_reg(pointervar,8,0x10);
  interpret_add(pointervar,8,1);
  #load_imm_to_reg(pointervar,0x10,0x52);
  load_mem_add_reg(pointervar,8,0x10);
  interpret_add(pointervar,8,1);
  #load_imm_to_reg(pointervar,0x10,0x42);
  load_mem_add_reg(pointervar,8,0x10);
  interpret_add(pointervar,8,1);
  #load_imm_to_reg(pointervar,0x10,0xe2);
  load_mem_add_reg(pointervar,8,0x10);
  interpret_add(pointervar,8,1);
  #load_imm_to_reg(pointervar,0x10,0x6e);
  load_mem_add_reg(pointervar,8,0x10);
  interpret_add(pointervar,8,1);
  
  the structer of yan85{
    array memory[256]
    byte rega
    byte reg_B
    ....
  }



  
  """

#main representation of the archi

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
        'memory':[ for i in range(255)],
        'reg_64':0,
        'reg_8':0,
        'reg_16':0,
        'reg_1':0,
        'reg_e':0,
        'reg_f':0

    }




    interpret_imm(stuff,1,1)
    interpret_imm(stuff,16,0x8a)
    interpret_imm(stuff,8,0x53)
    interpret_sm(stuff,8,16)
    add()
    
    
