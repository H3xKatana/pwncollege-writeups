input=[ 0x40, 0xf3, 0x82, 0xd6, 0x9b, 0x57, 0xe2, 0x98, 0xdf, 0x6f, 0x5b, 0xf3, 0x9c, 0xd6, 0x7e, 0x68, 0xff, 0x94, 0xd0, 0x68, 0x52, 0xfd, 0x63, 0xc5, 0x52, 0x4a, 0xe6, 0x9b, 0xc3 ]
print(len(input))


c=input[15]
input[15]=input[24]
input[24]=c

b=input[4]
input[4]=input[22]
input[22]=b

for j in range(14):
    input[j], input[0x1c - j] = input[0x1c - j], input[j]

# XOR each element based on the switch case
for k in range(0x1d):
    case = k % 5
    if case == 0:
        input[k] ^= 0xb4
    elif case == 1:
        input[k] ^= 0xec
    elif case == 2:
        input[k] ^= 0x96
    elif case == 3:
        input[k] ^= 0x33
    elif case == 4:
        input[k] ^= 10

# Reverse the first 14 and last 14 elements again


for i in range(14):
    input[i], input[28 - i] = input[28 - i], input[i]


hex_string = ''.join([f'\\x{num:02x}' for num in input])
#print("".join(chr(i)[for i in input])
print(hex_string)

#use echo -e .....
# or directly print cause all chars are printtable 
#pwn.college{4AUrQR_kKDpjkkKAnF6a1NLDK83.0FN2IDL1kjMzQzW}

