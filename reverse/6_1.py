input_list = [0xbc, 0x8a, 0xc6, 0xbe, 0x8c, 0xcd, 0xb4, 0x83, 0xcb, 0xad, 0x98, 0xd7, 0xaf, 0x9b, 0xd6, 0xa9, 0x9f]

# First transformation
for counter in range(0x11):
    choice = counter % 3
    if choice == 2:
        input_list[counter] = input_list[counter] ^ 0x8f
    elif choice < 3:
        if choice == 0:
            input_list[counter] = input_list[counter] ^ 0xa7
        elif choice == 1:
            input_list[counter] = input_list[counter] ^ 4

# Second transformation
for k in range(0x11):
    choice = k % 3
    if choice == 2:
        input_list[k] = input_list[k] ^ 0x2a
    elif choice < 3:
        if choice == 0:
            input_list[k] = input_list[k] ^ 0x7a
        elif choice == 1:
            input_list[k] = input_list[k] ^ 0xec


# The sorted and modified list is now in the `input_list` variable
print("".join(chr(i) for i in input_list))
