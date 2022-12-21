#include<stdio.h>
#include<omp.h>
#include<time.h>
void aleatorio(int A[]){
	int i;
	for(i=0;i<10;i++){
		A[i]= rand()%101;
	}
}
void imprimir(int A[]){
	int i;
	for(i=0;i<10;i++){
		printf("%d,",A[i]);
	}
}
int main(){
	omp_set_num_threads(2); 
	srand(time(NULL));
	int A[10],B[10], C[10];
	aleatorio(A);
	aleatorio(B);
	printf("Arreglo A\n");
	imprimir(A);
	printf("\nArreglo B\n");
	imprimir(B);
	
	#pragma omp parallel
	{ 
		int i;
		for(i=0;i<10;i++){
		#pragma omp atomic write
		C[i]=A[i]+B[i];	
	}
	}
	printf("\nResultado:\n");
	imprimir(C);
	return 0;
}
