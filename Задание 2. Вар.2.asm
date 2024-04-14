org 100h

array db 1, -2, 3, -4, 5 
array_size equ $ - array

mov ax, 0 
mov si, 0  
calculate_sum:
cmp si, array_size 
jge done 
mov al, byte [array + si] 
test al, 80h  
jnz not_negative  
add ax, ax 
not_negative:
inc si 
jmp calculate_sum
done:  
mov ah, 4ch
int 21h 
 ret