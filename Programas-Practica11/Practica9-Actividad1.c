#include <stdio.h>
int main() {
	int i;
	printf("Hola Mundo\n");
	for(i=0;i<10;i++){
		printf("Iteracion:%d\n",i);
		printf("Adios \n");
	}
	#pragma omp parallel
	{
	int i;
	printf("Hola Mundo\n");
	for(i=0;i<10;i++){
		printf("Iteracion:%d\n",i);
		printf("Adios \n");
	}
}
return 0;
}
