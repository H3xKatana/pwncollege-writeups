from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from Crypto.Util.Padding import pad, unpad


key=b64d("Vu5I/z8fD8fDR8QKLNc+hw==")
flag=b64d("II5Bu9TKkqNL2hjl8Wq1pUKHSvqKv2leQdPVv8p84JJRqADTy8KR+XxSuP1nhKiiDMFYh0GLyAHWq3NlDx0E5Q==")
cipher = AES.new(key=key, mode=AES.MODE_ECB)
cipher.block_size=16
text = cipher.decrypt(pad(flag, cipher.block_size))


decrypted_data = unpad(cipher.decrypt(flag), cipher.block_size)

print(decrypted_data)
