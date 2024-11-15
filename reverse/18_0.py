"""
so  after some static snalysis idecided to go with
so dynamic



\x4e\xe7\x1e\x45\x1f\xe5

after that each one  in mem get add with a value before

being compared after some calcs we find 


or using gdb by checking the value of register 0x10 
after each add or before cmp to get the values 
0x7fffffffe4f0
0x557e847d9ea3

like that 

display/10xb pointer_yan+0x100
0x7fffffffe5f0: 0x31    0xe7    0x76    0x00    0x00    0x00    0x12    0x00

using finish to end the add-function then check
the value of reg0x10 to get the value we need to input


\x79\x5d\x8e\xb0\x55\x35

pwn.college{8PTvxPtMfxwgoVGnfNyarw5XraT.0VO3IDL1kjMzQzW}
"""


"""
0x5650688b998c
0x7fffffffe4f0
so my input will get something add and compared to some value
in data so we need to substruct by hand since we can't the values 
directly before bien procece so 

each time substuct register64 - registerc to get value 

now idint check for the oferflow value i willcheckt it 
\xa2\x8d\xd7\xe8\x6f\x33\x2c\xd7\xb2
\x00\xe2\x4f\x5c\x40\xf1\x69\x91\x56
    
\xa2\xab\x88\x8c\x2f\x42\xc3\x46\x5c


remeber in byte wise op when we reach 255 it resets to 0
display/10xb 0x7fffffffe4f0+0x100
display/107xb 0x7fffffffe4d0
"""