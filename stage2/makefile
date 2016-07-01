CC=gcc
CFLAGS=-m32 -fno-stack-protector -o stage2

all:
	nasm -f elf gadgets.s
	$(CC) $(CFLAGS) stage2.c gadgets.o

clean:
	rm stage2 gadgets.o
