from pwn import *
   ...: 
   ...: #23ba is the offset 
   ...: #31 is the byte code for xor
   ...: 
   ...: 
   ...: p=process('/challenge/babyrev_level9.1')
   ...: for i in range(5):
   ...:         p.recvuntil('Offset (hex) to change:')
   ...:         p.sendline('23ba')
   ...:         p.recvuntil('New value (hex):')
   ...:         p.sendline('31')
   ...: 
   ...: 
   ...: p.interactive()

