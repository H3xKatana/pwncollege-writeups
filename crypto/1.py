from pwn import *



p=process("/challenge/run")
p.recvuntil(':')
data=p.readline()
solu=b64d(data)
print(solu)

