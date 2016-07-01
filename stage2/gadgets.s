global gadgets

section .text

gadgets:
	pop ecx		; pops the value pointed by ESP and puts it in ECX
	ret
	pop ebx		; pops the value pointed by ESP and puts it in EBX
	ret
	pop edx		; pops the value pointed by ESP and puts it in EDX
	ret
	mov al, 11	; moves 0xb in the lower 8 bits of EAX
	ret
	xor eax, eax	; sets EAX to zero
	ret
	pop edi		; pops the value pointed by ESP and puts it in EDI
	ret
	int 80h		; system interrupt


