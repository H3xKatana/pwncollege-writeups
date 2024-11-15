rom pwn import *

def main():
    input_data = [0x05, 0x04, 0x90, 0x71, 0x00, 0x09, 0x9f, 0x7d, 0x0c, 0x0d, 0x98, 0x60, 0x11, 0x16, 0x82, 0x1c, 0>

    reverse_mangle(input_data)

    input_data[19], input_data[21] = input_data[21], input_data[19]

    for i5 in range(len(input_data)):
        iVar5 = i5 % 4
        if iVar5 == 3:
            input_data[i5] ^= 0xdf
        elif iVar5 == 2:
            input_data[i5] ^= 0x4a
        elif iVar5 == 0:
            input_data[i5] ^= 0xd8
        elif iVar5 == 1:
            input_data[i5] ^= 0xa9

    input_data.sort()

    input_data[10], input_data[14] = input_data[14], input_data[10]

    for i1 in range(len(input_data)):
        if i1 % 2 == 0:
            input_data[i1] ^= 0xe9
        else:
            input_data[i1] ^= 0x9a

    # Second loop
    for i2 in range(len(input_data)):
        if i2 % 2 == 0:
            input_data[i2] ^= 0x58
        else:
            input_data[i2] ^= 0x95

    print("Final result of mangling input: {}".format(''.join('\\x{:02x}'.format(x) for x in input_data)))

    p = process('/challenge/babyrev_level8.1')
    p.recvuntil('Ready to receive your license key!')
    p.send(bytes(input_data))
    p.interactive()

def reverse_mangle(data):
    for i in range(18):
        data[i], data[0x24 - i] = data[0x24 - i], data[i]

if __name__ == "__main__":
    main()


