#include <stdlib.h>
#include <stdio.h>

/* The goal of this programme is two fold:
 * 	- the first is to redirect the control flow to target()
 * 	- the second is gain a shell using a basic shellcode
 */

void target(void)
{
	printf("you win!\n");
	exit(0);
}

void vulnerable(void)
{
	char name[256];
	printf("buffer is at %p\n", name);
	printf("Hello, what is your name?\n");
	scanf("%s", name);
	printf("Welcome %s\n", name);	
}

int main(void)
{
	/* disable buffering */
	setvbuf( stdin, NULL, _IONBF, 0 );
	setvbuf( stdout, NULL, _IONBF, 0 );

	vulnerable();
	exit(0);
}
