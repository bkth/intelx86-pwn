#include <stdlib.h>
#include <stdio.h>

void target(void)
{
	printf("you win!\n");
}

void vulnerable(void)
{
	char name[256];
	printf("Hello, what is your name? - ");
	scanf("%s", name);
	printf("Welcome %s\n", name);	
}

int main(void)
{
	vulnerable();
	exit(0);
}
