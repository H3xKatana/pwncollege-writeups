from pwn import *



# integrity check the check the pre hashed program if its changed the prgram has been cracked
#so we need a double crack
p=process('/challenge/babyrev_level11.1')

p.recvuntil('Offset (hex) to change:')
p.sendline('27d9')
p.recvuntil('New value (hex):')
p.sendline('31')
p.recvuntil('Offset (hex) to change:')
p.sendline('28b7')
p.recvuntil('New value (hex):')
p.sendline('31')

p.interactive()