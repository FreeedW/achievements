
org 100h

mov ax, 10 
mov bx, 5 
mov cx, 2  

sub ax, bx
add ax, bx

mov dx, 15
mul dx
div cx

mov bx, ax
int 21h 

ret