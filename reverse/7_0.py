def hex_strings_to_ints(hex_strings):
    return [int(hex_string, 16) for hex_string in hex_strings]





input_list=[ 0x16, 0x17, 0x14, 0x0d, 0x07, 0x38, 0x33, 0x2d, 0x28, 0x23, 0x5b, 0x57, 0x51, 0x51, 0x4d, 0x48, 0x48, 0x49, 0x47, 0x43, 0x43, 0x40, 0x7e, 0x78, 0x79, 0x79, 0x70, 0x6c ]
#input_list =[0x96, 0x84, 0x96, 0x84, 0x96, 0x84, 0x96, 0x84, 0x96, 0x84, 0x96, 0x84, 0x96, 0x84, 0x96, 0x84, 0x96, 0x84, 0x96, 0x84, 0x96, 0x84, 0x96, 0x84, 0x96, 0x84, 0x96, 0x84, 0x96, 0x84]




print(input_list)
#ascii_characters = ''.join(chr(hex_value) for hex_value in input_list)

# Print the result
#print(ascii_characters)
        

for i in range(0x1c):
	input_list[i]=hex(input_list[i] ^ 0x1e)

print(input_list)
input_list=hex_strings_to_ints(input_list)

"""		
print(input_list)
input_list.sort()
input_list.reverse()
print(input_list)"""

  # Your input list goes here
input_list.sort()
#print(input_list)
input_list.reverse()
#print(input_list)

#0xd3f1fd9cb4
for j in range(0x1c):
    case = j % 5
    if case == 0:
        input_list[j] =hex(input_list[j] ^ 0xd3)
    elif case == 1:
        input_list[j] =hex(input_list[j] ^ 0xf1) 
    elif case == 2:
        input_list[j] =hex(input_list[j] ^ 0xfd) 
    elif case == 3:
        input_list[j] =hex(input_list[j] ^ 0x9c) 
    elif case == 4:
        input_list[j] = hex(input_list[j] ^ 0xb4)


#print(input_list)
input_list=hex_strings_to_ints(input_list)


# The modified list is now in the `input_list` variable
for i in range(0x1c):
    case = i % 2
    if case == 0:
        input_list[i] =hex(input_list[i] ^ 0xd4) 
    else:
        input_list[i] =hex(input_list[i]^ 0xc6 )

print(len(input_list))
#echo -e"\x75\x.............."|/chalenge/babyrev
#pwn.college{Qb2PX_j6_rar6KlZR9YFro7T0Oq.01M2IDL1kjMzQzW}
