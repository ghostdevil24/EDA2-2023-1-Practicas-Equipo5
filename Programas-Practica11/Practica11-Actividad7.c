#include <stdio.h>
int main() {
#pragma omp parallel
{
int i;
printf("Hola Mundo\n");
#pragma omp for
for(i=0;i<10;i++)
printf("Iteraci�n:%d\n",i);
}
printf("Adi�s \n");
return 0;
}
