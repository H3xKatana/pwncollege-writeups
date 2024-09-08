.intel_syntax noprefix


_start:

        int3
        xor eax,eax
#first if
        cmp rdi,0
        je  end
        #start loop
loop:
#bl contain the  first bytee for fast cmp
        mov ebx,0
        mov bl, [rdi]
        cmp bl,0
        je end
#inside loop check


        cmp bl,90
        jg greater

        int 3

        push rdi
        push rax
        mov rdi,0
        mov dil,bl


        mov r10,0x403000
        call r10
        mov bl,al



        pop rax
        pop rdi
        add rax,1
        mov  [rdi],bl
greater:
        add rdi,1
        jmp loop

end:
        ret

