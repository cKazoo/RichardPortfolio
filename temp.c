#include <stdio.h>

float main() {
	float f, c;
	
	printf("Enter a Farenheit Value:  ");
	scanf("%f", &f);
	c = (5.0/9.0)*(f - 32.0);
	printf("The value in Celsius is %f\n.", c);

	return 0;
}
