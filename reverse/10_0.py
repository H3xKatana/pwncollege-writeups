from pwn import *
 
 p=process('/challenge/babyrev_level10.0')
 
 p.recvuntil('Offset (hex) to change:')
 p.sendline('20ed')
 p.recvuntil('New value (hex):')
 p.sendline('31')
 p.interactive()
 
