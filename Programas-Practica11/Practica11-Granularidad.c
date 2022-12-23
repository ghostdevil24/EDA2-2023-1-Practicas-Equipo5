#include<stdio.h>
#include<omp.h>
void altaGranularidad(int num, int pot){
	int resultado=1,i;
	int tid,inicio,fin;
	omp_set_num_threads(4);
	#pragma omp parallel private(inicio,tid,fin,i)
	{
	tid=omp_get_thread_num();
	inicio = tid*(int)pot/omp_get_num_threads();
	fin = (tid+1)*pot/omp_get_num_threads();
	for(i=inicio; i<fin;i++){
		resultado=resultado*num;
		printf("hilo %d calculo %d elevado a %d\n",tid,num,i+1);
	}
}
printf("Resultado final: %d\n",resultado);
}
void mediaGranularidad(int num, int pot){
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
		printf("hilo %d calculo %d elevado a %d\n",tid,num,i+1);
	}
}
printf("Resultado final: %d\n",resultado);
}
void bajaGranularidad(int num, int pot){
	int resultado=1,i;
	int tid,inicio,fin;
	omp_set_num_threads(0);
	#pragma omp parallel private(inicio,tid,fin,i)
	{
	tid=omp_get_thread_num();
	inicio = tid*(int)pot/omp_get_num_threads();
	fin = (tid+1)*pot/omp_get_num_threads();
	for(i=inicio; i<fin;i++){
		resultado=resultado*num;
		printf("hilo %d calculo %d elevado a %d\n",tid,num,i+1);
	}
}
printf("Resultado final: %d\n",resultado);
}
int main(){
	int num, pot;
	printf("Ingrese un numero a potenciar: ");
	scanf("%d",&num);
	printf("Ingrese la potencia del numero anterior: ");
	scanf("%d",&pot);
	printf("######## Granularidad alta ##########\n");
	altaGranularidad(num,pot);
	printf("######## Granularidad media ########\n");
	mediaGranularidad(num,pot);
	printf("######## Granularidad baja ####### \n");
	bajaGranularidad(num,pot);
}
