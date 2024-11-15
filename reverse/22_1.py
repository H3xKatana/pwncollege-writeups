# op op1 op2 ===> op op2 op1 ou op1 op2 op
# sys 0x8 --- 0x20 exit
# op op2 op2
#0x8  no reg
# stk 0
#
regs=[0x1,0x2,0x4,0x10,0x20,0x40,0x80]

#fuzzin 
from pwn import *
ops=[0x0,0x1,0x2,0x4,0x8,0x10,0x20,0x40,0x80]
regs=[0x1,0x2,0x4,0x10,0x20,0x40,0x80]

for op in ops :
    for op1 in ops :
        
        p=process("/challenge/babyrev_level22.1")
        p.recvuntil(b'Please input your yancode:')
        print(p8(op)+p8(op1)+b'\x10')
        p.send(p8(op1)+p8(op)+b'\x10')
        print(p.recvall(timeout=.2))
        print(p.poll())    
        p.kill()



operations = {
    "imm":0x1, 
    "add":0x8, 
    "stk":0x20,
    "stm":0x2,
    "ldm":0x80,
    "cmp":0x40,
    "jmp":0x10,
    "sys":0x4}  


registers = {
    "a":0x80,
    "b":0x8,
    "c":0x40,
    "d":0x20,
    "s":0x10,
    "i":0x4,
    "f":0x2
    }
  #good
syscalls = {
    "open":0x4,
    "read_code":0x8,
    "read_mem":0x80,
    "write":0x2,
    "sleep":0x40,
    "exit":0x20
    }