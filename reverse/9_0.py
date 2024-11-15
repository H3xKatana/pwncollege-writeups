from pwn import *

#22cd is the offset 
#31 is the byte code for xor


p=process('/challenge/babyrev_level9.0')
for i in range(5):
	p.recvuntil('Offset (hex) to change:')
	p.sendline('22cd')
	p.recvuntil('New value (hex):')
	p.sendline('31')


p.interactive()
