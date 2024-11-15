"""
\xd\x66\xed\xaa\x23\xd9\x63\x43\x5a
\xd9\xb2\xc3\xda\xf\xc6\x70\x6\x91
=
\xe6\x18\xb0\x84\x32\x9f\xd3\x49\xeb



this challnge is the same as the last one but now 
we have some changes in data in memory bu adding to
diffrent value in mem before compare 
this time i used a new approach so we know the 
program is not stripped so i used gdb to 
get the address of yan pointer than inspected the 
value by x/9bx $pointer to get the values 

the address of the yan pointer 0x7ffe7de05ad0
0x7ffcc6b336c0


the script is almost like this 
starti
break execute_program
continue
    commands
        set $pointer = $rdi
    end

break *execute_program+1866
    commands
        x/9bx $pointer+0x90
        continue
    end





"""


"""

for the stripped version i decided to go with 
gdb also 

so by using base address from info proc mapping 

and add the offset of the exe program i could get
the pointer of yan archi from rdi

we set a break point befor in exe+1866 after all process has 
ended


we inspece all pointer sotrage 232 bytes or 
directly access 12 bytes from were the values
were stored 


-----> x/12bx pointer+0x77

\x42\x27\x29\x4e\x49\x84\xd9\xf4\xe4\x73\x31\xfa
pwn.college{UUQ6ZtI_5jpoARGUWLzwSouAujA.0FO3IDL1kjMzQzW}

"""