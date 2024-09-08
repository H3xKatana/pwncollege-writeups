start:
    push rbp
    mov rbp, rsp
    sub rsp, 0xff
    xor ecx, ecx

count_loop:
    cmp rcx, rax
    jge end_count_loop

    mov edx, byte [rsi + rcx]
    inc byte [rbp - 0xff + rdx]
    inc rcx
    jmp count_loop

end_count_loop:
    xor rdx, rdx
    mov rcx, 0xff

find_max_loop:
    cmp byte [rbp - 0x255 + rcx], dl
    jbe find_max_next_byte
    mov dl, byte [rbp - 0x255 + rcx]
    mov al, dl
find_max_next_byte:
    loop find_max_loop

    mov rsp, rbp
    pop rbp
    ret
