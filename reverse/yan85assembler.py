#! /bin/python
import sys, os, struct
#the instr must be coded like this in bytes {op op2 op1} or { op op1 op2 } 
# {op1 op op2 }  {op1 op2 op} it depands on the challenge
"""
    mov rax,2
    xor rsi,rsi
    xor rsi,rsi
    mov rbx,0x67616c662f
    push rbx
    mov rdi,rsp
    syscall

    mov rdi,rax
    xor rax,rax
    mov rsi,rsp
    mov rdx,100
    syscall

    mov rax,1
    mov rdi,1
    syscall 

    mov rax,60
    syscall

in yan code is 

imm a = 0x30
imm b = 0x2f
stm *a = b
add a, 0x1
imm b = 0x66
stm *a = b
add a, 0x1
imm b = 0x6c
stm *a = b
add a, 0x1
imm b = 0x61
stm *a = b
add a, 0x1
imm b = 0x67
stm *a = b
//loaded /flag
imm c = 0
imm b = 0
imm a = 0x30
sys 0x1, d /open
stk none d
stk a none
imm b = 0x40
imm c = 0x40
sys 0x8, d
imm a = 0x01
imm b = 0x40
imm c = 0x40
sys 0x20, d
"""

"""
  if ((param_2 & 4) != 0) {
    imm(param_1,param_2);
  }
  if ((param_2 & 8) != 0) {
    add(param_1,param_2);
  }
  if ((param_2 & 2) != 0) {
    stk(param_1,param_2);
  }
  local_18 = (char)param_2;
  if (local_18 < '\0') {
    stm(param_1,param_2);
  }
  if ((param_2 & 0x10) != 0) {
    ldm(param_1,param_2);
  }
  if ((param_2 & 0x40) != 0) {
    cmp(param_1,param_2);
  }
  if ((param_2 & 0x20) != 0) {
    jmp(param_1,param_2);
  }
  if ((param_2 & 1) != 0) {
    sys(param_1,param_2);
  }
  return;
}
"""
operations = {
    "imm":0x4,
    "add":0x8,
    "stk":0x2,
    "stm":0x80,
    "ldm":0x10,
    "cmp":0x40,
    "jmp":0x20,
    "sys":0x1}

"""
"""
registers = {
    "a":0x20,
    "b":0x4,
    "c":0x1,
    "d":0x40,
    "s":0x10,
    "i":0x2,
    "f":0x8
    }
  
syscalls = {
    "open":0x8,
    "read_code":0x4,
    "read_mem":0x1,
    "write":0x2,
    "sleep":0x20,
    "exit":0x10
    }



def usage():
    print(sys.argv[0] + " <file>")

OP_ORDER = [0,1,2]

try:
    insts = open(sys.argv[1], "r").readlines()
except IndexError:
    usage()
    exit()

def chunkstring(string, length):
    return list(string[0+i:length+i] for i in range(0, len(string), length))


jmp_ops = {
    "L":0x10,
    "G":0x01,
    "E":0x08,
    "N":0x04,
    "Z":0x02
}

def regCheck(val):

    for k,v in registers.items():
        if val.lower() == k:
            return(hex(v))
        
def jmp(arg1):
    for k,v in jmp_ops.items():
        if k == arg1:
            return hex(v)

def syscall(arg1):
    for k,v in syscalls.items():
        if v == int(arg1,16):
            return hex(v)
        
        elif k == arg1.lower():
            return hex(v)

def genReg(op):
    for k,v in registers.items():
        if op.lower() == k:
            return(hex(v))
        
def operation(op):
    for k,v in operations.items():
        if op.lower() == k:
            return(hex(v))


def assemb(op, arg1, arg2):
    opcode = []

    opcode.append( operation(op) )
    op = op.lower()

    if op == "jmp":
        opcode.append(jmp(arg1))
        opcode.append(regCheck(arg2))

    elif op == "sys": 
       
        opcode.append(syscall(arg1))
        opcode.append(regCheck(arg2))
    
    
    else: 
        
        if regCheck(arg1) != None:
            opcode.append( regCheck(arg1) )
        else:
            opcode.append( (arg1) )

        if regCheck(arg2) != None:
            opcode.append( regCheck(arg2) )
        else:
            opcode.append( (arg2) )

       
    return opcode

def main():
    noOfLiens = len(insts)
    outBytes = b''
    for i in range(noOfLiens):
        op, arg1, arg2 = insts[i].split()

        arg1 = arg1.replace("*", "")
        arg2 = arg2.replace("*", "")

        opcode = assemb(op, arg1, arg2)

        for b in opcode:
            outBytes += struct.pack('B', int(b, 16))
    
    # print(outBytes)
    fileName = sys.argv[1]+'-assem'
    with open(fileName, 'wb') as outFile:
        outFile.write(outBytes)
        outFile.close()

    print(f"[+] File ({fileName}) is created")

main()
