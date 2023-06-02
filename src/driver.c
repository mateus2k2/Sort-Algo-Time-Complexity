#include "headers/insertionSort.h"
#include "headers/mergeSort.h"
#include "headers/radixSort.h"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

//Rodar e gerar o arquivo com todos os dados
//Analise de complexidade de todos os metodos
//Gerar testes estatisticos para cada metodos
//Gerar gráficos para os metodos
//Escrever resto relatorio

void printArray(int array[], int size){
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
}

void printValues(int size, int instanceIndex, double insertionTime, double mergeTime, double radixTime, int arrayReal[], int arrayInsertion[], int arrayMerge[] ,int arrayRadix[]) {
    printf("%d, %d, %.20f, %.20f, %.20f\n", size, instanceIndex, insertionTime, mergeTime, radixTime);
    // printf("%d, %d, %.20f, %.20f, %.20f", size, instanceIndex, insertionTime, mergeTime, radixTime);
    // printf(", "); 
    // printArray(arrayReal, size);
    // printf(", "); 
    // printArray(arrayInsertion, size);
    // printf(", "); 
    // printArray(arrayMerge, size);
    // printf(", "); 
    // printArray(arrayRadix, size);
    // printf("\n");
}

void generateInstancia(int *array, int size) {
    for (int i = 0; i < size; i++) {
        array[i] = rand() % size;
    }
}

int main(int argc, char* argv[]) {
    srand(time(NULL));

    clock_t start, end;
    double tempoGastoInsertion;
    double tempoGastoMerge;
    double tempoGastoRadix;

    int size = atoi(argv[1]);

    // printf("Size, Instance Index, Insertion Time, Merge Time, Radix Time\n");
    // printf("Size, Instance Index, Insertion Time, Merge Time, Radix Time, Real Array, Insertion Array, Merge Array, Radix Array\n");

    for (int j = 0; j < 20; j++) {
        int* instancia = (int*)malloc(size * sizeof(int));
        generateInstancia(instancia, size);

        int* instanciaInsertionSort = (int*)malloc(size * sizeof(int));
        memcpy(instanciaInsertionSort, instancia, size * sizeof(int));

        int* instanciaMergeSort = (int*)malloc(size * sizeof(int));
        memcpy(instanciaMergeSort, instancia, size * sizeof(int));

        int* instanciaRadixSort = (int*)malloc(size * sizeof(int));
        memcpy(instanciaRadixSort, instancia, size * sizeof(int));

        start = clock();
        insertionSort(instanciaInsertionSort, size);
        end = clock();
        tempoGastoInsertion = ((double)(end - start)) / CLOCKS_PER_SEC;

        start = clock();
        mergeSort(instanciaMergeSort, 0, size - 1);
        end = clock();
        tempoGastoMerge = ((double)(end - start)) / CLOCKS_PER_SEC;

        start = clock();
        radixsort(instanciaRadixSort, size);
        end = clock();
        tempoGastoRadix = ((double)(end - start)) / CLOCKS_PER_SEC;

        printValues(size, j + 1, tempoGastoInsertion, tempoGastoMerge, tempoGastoRadix, instancia, instanciaInsertionSort, instanciaMergeSort, instanciaRadixSort);

        free(instanciaInsertionSort);
        free(instanciaMergeSort);
        free(instanciaRadixSort);
        free(instancia);
    }

    printf("\n");

    return 0;
}
