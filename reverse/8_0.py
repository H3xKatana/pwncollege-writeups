from pwn import *

def main():
    input_data = [0xe8, 0xb9, 0x7b, 0xe4, 0x85, 0xb5, 0xa5, 0xab, 0xea, 0xdc, 0x77, 0xf2, 0xbc, 0x33, 0xd9, 0x2c, 0x35, 0xed, 0x23, 0x05, 0x2d, 0x6d, 0x2a, 0x6f, 0x0a, 0xef, 0x75, 0x68, 0xa1, 0x53, 0x3d, 0xa7, 0x65, 0x34, 0x91, 0xa1]
    
    reverse_mangle(input_data)

    for i in range(len(input_data)):
        if i % 5 == 0:
            input_data[i] ^= 0xed
        elif i % 5 == 1:
            input_data[i] ^= 0x1b
        elif i % 5 == 2:
            input_data[i] ^= 0x2f
        elif i % 5 == 3:
            input_data[i] ^= 0xb3
        elif i % 5 == 4:
            input_data[i] ^= 0xae

    input_data[2], input_data[5] = input_data[5], input_data[2]

    for i in range(len(input_data)):
        if i % 3 == 0:
            input_data[i] ^= 0x8d
        elif i % 3 == 1:
            input_data[i] ^= 0x95
        elif i % 3 == 2:
            input_data[i] ^= 0xe5

    for i in range(len(input_data)):
        if i % 3 == 0:
            input_data[i] ^= 0xd5
        elif i % 3 == 1:
            input_data[i] ^= 0x8d
        elif i % 3 == 2:
            input_data[i] ^= 0xdf

    for i in range(len(input_data)):
        if i % 6 == 0:
            input_data[i] ^= 0x77
        elif i % 6 == 1:
            input_data[i] ^= 0xf1
        elif i % 6 == 2:
            input_data[i] ^= 0x89
        elif i % 6 == 3:
            input_data[i] ^= 0xe8
        elif i % 6 == 4:
            input_data[i] ^= 0x76
        else:
            input_data[i] ^= 0x46

    print("Final result of mangling input: {}".format(''.join('\\x{:02x}'.format(x) for x in input_data)))
"""
    p = process('/challenge/babyrev_level8.0')
    p.recvuntil('Ready to receive your license key!')
    p.send(bytes(input_data))
"""
def reverse_mangle(data):
    for i in range(18):
        data[i], data[35 - i] = data[35 - i], data[i]

if __name__ == "__main__":
    main()
