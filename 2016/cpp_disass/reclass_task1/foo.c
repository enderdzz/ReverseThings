#include <stdio.h>
#include <string.h>

int main(){
	char * s = "hello + \xad";
	int len = strlen(s);
	char *ptr = strchr(s, '+');

	printf("%c\n", *ptr);
	ptr = NULL;
	memset(s, 0, len * sizeof(char));
	return 0;
}
