CC=gcc
CFLAGS=-m32 -fno-stack-protector -z execstack -o stage1

all:
	$(CC) $(CFLAGS) stage1.c

clean:
	rm stage1
