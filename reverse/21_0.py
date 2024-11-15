import sys, os, struct
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

imm c = 0/flags
imm b = 0/fd
imm a = 0x30/pointer---> yan+0x300+0x30
sys 0x1, d /open


stk none d
stk a none
imm b = 0x40
imm c = 0x40
sys 0x8, d  /read_mem


imm a = 0x01
imm b = 0x40
imm c = 0x40
sys 0x20, d  /write

sys 0x8 d  /exit


"""
operations = {
    "imm":0x4,
    "add":0x40,
    "stk":0x20,
    "stm":0x8,
    "ldm":0x10,
    "cmp":0x2,
    "jmp":0x40,
    "sys":0x1}

registers = {
    "a":0x10,
    "b":0x1,
    "c":0x2,
    "d":0x8,
    "s":0x20,
    "i":0x4,
    "f":0x40
    }
syscalls = {
    "open":0x1,
    "read_code":0x4,
    "read_mem":0x2,
    "write":0x20,
    "sleep":0x10,
    "exit":0x8
    }

