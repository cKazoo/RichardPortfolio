#include<stdio.h>

int main() {
	char str[20];

	printf("Enter a word: ");
	scanf("%s", &str);

	for(int i = 0; str[i] !=0 ; i++) {
	
		printf("%c = %i ascii code\n", str[i], str[i]);
		if(str[i]>='A' && str[i] <= 'Z'){
			str[i] = str[i] +32;
		}
		else if(str[i]>= 'a' && str[i] <= 'z'){
				str[i] = str[i] -32;
		}
	}
	printf("Your string inverted is %s\n", str);
	return 0;
}
