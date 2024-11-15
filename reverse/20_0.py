from pwn import *



add=p64(0x15801575a46df8c1)	
add +=p64(0x4aa5ed65199bd95c)
add +=p64(0x15c853fb5a)


	
answer=   p64(0x1900ef32fb8365cb)
answer += p64(0x0a39be88be334f48)
answer += p64(0x7c6951ec9d)	

add=bytearray(add)
answer=bytearray(answer)

original_values = [(answer[i] - add[i]) & 0xff for i in range(len(add))]

# Format the result
result = ''.join([f'\\x{byte:02x}' for byte in original_values])

print(result)



"""

# Set a breakpoint at the interpret_instruction function

break *interpret_instruction
start < file777
c
# Set variables for memory regions
set $base = $rdi
set $base_reg = $base + 0x400
set $input_base = $base + 0x300 + 0x30

# Display memory contents
display/8bx $base_reg
display/6gx $input_base

#comaperd values are loaded in rev startin form 0xb8 and the length is 0x15
display/6gx $base+0x300+0xa4
# Continue execution
c


echo -en "\x0a\x6d\x16\x57\xbd\xda\x80\x04\xec\x76\x98\xa5\x23\xd1
\x94\xc0\x43\xf1\xfe\xa1\x67" |
/challenge/babyrev_level20.0 
pwn.college{guwRriXIHDll_oa-4Ri3V5UR3xu.01M4IDL1kjMzQzW}
"""