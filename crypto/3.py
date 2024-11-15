from  pwn import *

 
p=process("/challenge/run")

p.recvuntil("secret ciphertext (b64):")
cipher=p.recvline()
print(cipher)
p.sendline(cipher)
p.recvuntil("ciphertext (b64):")
flag=p.recvline()
flag=b64d(flag)
print(flag)

