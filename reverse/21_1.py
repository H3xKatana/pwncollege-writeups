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

"""
openat(AT_FDCWD, "/flag", O_RDONLY)     = -1 EACCES (Permission denied)
read(255, 0x7ffc115e26a0, 64)           = -1 EBADF (Bad file descriptor)
write(1, "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 64) = 64
exit_group(1)                           = ?
+++ exited with 1 +++
hacker@reverse-engineering~level21-1:~$ /challenge/babyrev_level21.1 < yyy-assem 
[+] Welcome to /challenge/babyrev_level21.1!
[+] This challenge is an custom emulator. It emulates a completely custom
[+] architecture that we call "Yan85"! You'll have to understand the
[+] emulator to understand the architecture, and you'll have to understand
[+] the architecture to understand the code being emulated, and you will
[+] have to understand that code to get the flag. Good luck!
[+]
[+] This level is a full Yan85 emulator. You'll have to reason about yancode,
[+] and the implications of how the emulator interprets it!
[!] This time, YOU'RE in control! Please input your yancode: [+] Starting interpreter loop! Good luck!
pwn.college{Qktm0j9dwWe8YW6VqBTrXhTIJN8.0lN4IDL1kjMzQzW}
hacker@reverse-engineering~level21-1:~$ """