#include<stdio.h>
#include<omp.h>
#include<time.h>
void aleatorio(int A[]){
	int i;
	for(i=0;i<10;i++){
		A[i]= rand()%101;
	}
}
int generarNumero(){
	return rand()%11;
}
int mediaGranularidad(int num, int pot){
	int resultado=1,i;
	int tid,inicio,fin;
	omp_set_num_threads(2);
	#pragma omp parallel private(inicio,tid,fin,i)
	{
	tid=omp_get_thread_num();
	inicio = tid*(int)pot/omp_get_num_threads();
	fin = (tid+1)*pot/omp_get_num_threads();
	for(i=inicio; i<fin;i++){
		resultado=resultado*num;
	}
}
	return resultado;
}
int main(){
	int resultado=0;
	int tid,inicio,fin;
	srand(time(NULL));
	int x[5];
	int temp[5],i;
	aleatorio(x);
	printf("Paralelismo a nivel de instrucciones:\n");
	for(i=0;i<5;i++){
		#pragma omp atomic read
		temp[i]=x[i];
		#pragma omp atomic write
		x[i]=temp[i]*2;
		#pragma omp atomic update
		x[i]*=2;
	}
	printf("Imprimiendo datos generados\n");
	for(i=0;i<5;i++){
		printf("%d\n",x[i]);
	}
	int pot=5;
	int num=2;
	printf("Paralelismo a nivel de tareas\n");
	#pragma omp parallel private(inicio,tid,fin,i)
	{
	tid=omp_get_thread_num();
	inicio = tid*(int)pot/omp_get_num_threads();
	fin = (tid+1)*pot/omp_get_num_threads();
	for(i=inicio; i<fin;i++){
		resultado=mediaGranularidad(num,pot)+resultado;
	}
	}
	printf("El  resultado de sumar las potencias de los números es: %d",resultado);
}
