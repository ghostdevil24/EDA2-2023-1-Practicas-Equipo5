#include <stdio.h>
#include<omp.h>
int main() {
	int i;
	#pragma omp parallel private(i)
	{
		printf("Hola Mundo\n");
		for(i=0;i<10;i++)
		printf("Iteración:%d\n",i);
	}
	printf("Adios \n");
	return 0;
}
