
(gdb) r
Starting program: /tmp/babyrev_level19.1 /tmp/babyrev_level19.1
[+] Welcome to /tmp/babyrev_level19.1!
[+] This challenge is an custom emulator. It emulates a completely custom
[+] architecture that we call "Yan85"! You'll have to understand the
[+] emulator to understand the architecture, and you'll have to understand
[+] the architecture to understand the code being emulated, and you will
[+] have to understand that code to get the flag. Good luck!
[+]
[+] This level is a full Yan85 emulator. You'll have to reason about yancode,
[+] and the implications of how the emulator interprets it!
[+] Starting interpreter loop! Good luck!
KEY: 123456789abcdef

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0xf2
2: x/xb $rbp-2  0x7fffffffdf7e:	0x63
(gdb) f
#0  0x00005555555556aa in ?? ()
(gdb) set *((char *)0x7fffffffdf7e) = 0xf2
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x00
2: x/xb $rbp-2  0x7fffffffdf7e:	0x0b
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0xd0
2: x/xb $rbp-2  0x7fffffffdf7e:	0x62
(gdb) set *((char *)0x7fffffffdf7e) = 0xd0
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x00
2: x/xb $rbp-2  0x7fffffffdf7e:	0x0a
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x38
2: x/xb $rbp-2  0x7fffffffdf7e:	0x61
(gdb) set *((char *)0x7fffffffdf7e) = 0x38
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x00
2: x/xb $rbp-2  0x7fffffffdf7e:	0x09
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x47
2: x/xb $rbp-2  0x7fffffffdf7e:	0x39
(gdb) set *((char *)0x7fffffffdf7e) = 0x47
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x00
2: x/xb $rbp-2  0x7fffffffdf7e:	0x08
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x38
2: x/xb $rbp-2  0x7fffffffdf7e:	0x38
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x00
2: x/xb $rbp-2  0x7fffffffdf7e:	0x07
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x8e
2: x/xb $rbp-2  0x7fffffffdf7e:	0x37
(gdb) set *((char *)0x7fffffffdf7e) = 0x8e
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x00
2: x/xb $rbp-2  0x7fffffffdf7e:	0x06
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x02
2: x/xb $rbp-2  0x7fffffffdf7e:	0x36
(gdb) set *((char *)0x7fffffffdf7e) = 0x02
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x00
2: x/xb $rbp-2  0x7fffffffdf7e:	0x05
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x5b
2: x/xb $rbp-2  0x7fffffffdf7e:	0x35
(gdb) set *((char *)0x7fffffffdf7e) = 0x5b
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x00
2: x/xb $rbp-2  0x7fffffffdf7e:	0x04
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0xd3
2: x/xb $rbp-2  0x7fffffffdf7e:	0x34
(gdb) set *((char *)0x7fffffffdf7e) = 0xd3
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x00
2: x/xb $rbp-2  0x7fffffffdf7e:	0x03
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x39
2: x/xb $rbp-2  0x7fffffffdf7e:	0x33
(gdb) set *((char *)0x7fffffffdf7e) = 0x39
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x00
2: x/xb $rbp-2  0x7fffffffdf7e:	0x02
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x83
2: x/xb $rbp-2  0x7fffffffdf7e:	0x32
(gdb) set *((char *)0x7fffffffdf7e) = 0x83
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x00
2: x/xb $rbp-2  0x7fffffffdf7e:	0x01
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0xfa
2: x/xb $rbp-2  0x7fffffffdf7e:	0x31
(gdb) set *((char *)0x7fffffffdf7e) = 0xfa
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x00
2: x/xb $rbp-2  0x7fffffffdf7e:	0x00
(gdb) c
Continuing.

Breakpoint 1, 0x00005555555556aa in ?? ()
1: x/xb $rbp-1  0x7fffffffdf7f:	0x00
2: x/xb $rbp-2  0x7fffffffdf7e:	0x00
(gdb) c
Continuing.
CORRECT! Your flag:

1: x/xb $rbp-1  0x7fffffffdf7f: 0xf2

1: x/xb $rbp-1  0x7fffffffdf7f: 0xd0

1: x/xb $rbp-1  0x7fffffffdf7f: 0x38

1: x/xb $rbp-1  0x7fffffffdf7f: 0x47

1: x/xb $rbp-1  0x7fffffffdf7f: 0x38

1: x/xb $rbp-1  0x7fffffffdf7f: 0x8e

1: x/xb $rbp-1  0x7fffffffdf7f: 0x02

1: x/xb $rbp-1  0x7fffffffdf7f: 0x5b

1: x/xb $rbp-1  0x7fffffffdf7f: 0xd3

1: x/xb $rbp-1  0x7fffffffdf7f: 0x39

1: x/xb $rbp-1  0x7fffffffdf7f: 0x83

1: x/xb $rbp-1  0x7fffffffdf7f: 0xfa






x/xb $rbp-2  0x7fffffffdf7e: 0x63
2: x/xb $rbp-2  0x7fffffffdf7e: 0x62
2: x/xb $rbp-2  0x7fffffffdf7e: 0x61
2: x/xb $rbp-2  0x7fffffffdf7e: 0x39
2: x/xb $rbp-2  0x7fffffffdf7e: 0x38
2: x/xb $rbp-2  0x7fffffffdf7e: 0x37
2: x/xb $rbp-2  0x7fffffffdf7e: 0x36
2: x/xb $rbp-2  0x7fffffffdf7e: 0x35
2: x/xb $rbp-2  0x7fffffffdf7e: 0x34
2: x/xb $rbp-2  0x7fffffffdf7e: 0x33
2: x/xb $rbp-2  0x7fffffffdf7e: 0x32
2: x/xb $rbp-2  0x7fffffffdf7e: 0x31
