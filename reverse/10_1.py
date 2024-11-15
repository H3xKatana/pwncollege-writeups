
from pwn import *

p=process('/challenge/babyrev_level10.1')

p.recvuntil('Offset (hex) to change:')
p.sendline('213f')
p.recvuntil('New value (hex):')
p.sendline('31')
p.interactive()