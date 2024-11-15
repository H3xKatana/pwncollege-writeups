from pwn import *


p=process('/challenge/run')

p.recvuntil('key (b64):')
key=p.recvline()
print(key)
p.recvuntil('secret ciphertext (b64):')
flag= p.recvline()
print(flag)
flag=b64d(flag)
key=b64d(key)
i=xor(bytes(flag),bytes(key))
print(i)
