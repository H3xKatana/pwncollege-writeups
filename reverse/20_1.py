from pwn import *

add=p64(0xc11d009323e6c041)	
add +=p64(0x5c34ce8ca9cc7901)
add +=p64(0xf793c3475df5e935)
add +=p64(0x000000008d0fab58)


answer=   p64(0x930d71b11f591d57)
answer += p64(0x71ba3ac403280b89)
answer += p64(0x9a8f175885319109)
answer += p64(0x00000000920cf22f)	

add=bytearray(add)
answer=bytearray(answer)

original_values = [(answer[i] - add[i]) & 0xff for i in range(len(add))]

# Format the result
result = ''.join([f'\\x{byte:02x}' for byte in original_values])

print(result)




"""
gdb script  


break *0x555555554000+0x1a72
break *0x555555554000+0x1666

#start < file777
r

# Set variables for memory regions
set $base_mem = $rdi
set $base_reg = $base_mem + 0x400
set $input_base = $base_mem + 0x300 +0x30
#del 1
# Display memory contents
display/8bx $base_reg
display/6gx $input_base

#break *0x555555554000+0x1666

# Set commands for the second breakpoint
commands 2
#silent
printf "*************************>>Reached the second breakpoint\n"
continue
end



echo -en "\x16\x5d\x73\xfc\x1e\x71\xf0\xd2\x88\x92\x5c\x5a\x38\x6c\x86\x15\xd4\xa8\x3c\x28\x11\x54\xfc\xa3\xd7\x47\xfd\x05" | /challenge/babyrev_level20.1 
[+] Welcome to /challenge/babyrev_level20.1!
[+] This challenge is an custom emulator. It emulates a completely custom
[+] architecture that we call "Yan85"! You'll have to understand the
[+] emulator to understand the architecture, and you'll have to understand
[+] the architecture to understand the code being emulated, and you will
[+] have to understand that code to get the flag. Good luck!
[+]
[+] This level is a full Yan85 emulator. You'll have to reason about yancode,
[+] and the implications of how the emulator interprets it!
[+] Starting interpreter loop! Good luck!
KEY: CORRECT! Here is your flag:
pwn.college{w1Y_1CvYiDvf35kakOXnjQOj3ZN.0FN4IDL1kjMzQzW}
"""