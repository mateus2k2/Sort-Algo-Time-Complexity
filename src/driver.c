#include "headers/insertionSort.h"
#include "headers/mergeSort.h"
#include "headers/radixSort.h"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void printArray(int array[], const char string[], int size, double tempoGasto) {
    printf("\n%s\n", string);
    printf("%.20f\n", tempoGasto);

    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
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

    int size = 0;

    for (int i = 100; i < 10000; i = i * 2) {
        printf("\n\n------------------------------------------------------------------------\n\n");
        printf("Tamanho Instancia %i\n", i);
        for (int j = 0; j < 20; j++) {
            printf("\n\n\n***Instancia %i/20***\n", j + 1);
            size = i;
            int* instancia = (int*)malloc(size * sizeof(int));
            generateInstancia(instancia, size);

            int* instanciaInsertionSort = (int*)malloc(size * sizeof(int));
            memcpy(instanciaInsertionSort, instancia, size * sizeof(int));

            int* instanciaMergeSort = (int*)malloc(size * sizeof(int));
            memcpy(instanciaMergeSort, instancia, size * sizeof(int));

            int* instanciaRadixSort = (int*)malloc(size * sizeof(int));
            memcpy(instanciaRadixSort, instancia, size * sizeof(int));

            printArray(instancia, "Instancia Real", size, 0);
            
            start = clock();
            insertionSort(instanciaInsertionSort, size);
            end = clock();
            tempoGastoInsertion = ((double)(end - start)) / CLOCKS_PER_SEC;

            printArray(instanciaInsertionSort, "Sorted With Insertion Sort", size, tempoGastoInsertion);
            
            start = clock();
            mergeSort(instanciaMergeSort, 0, size - 1);
            end = clock();
            tempoGastoMerge = ((double)(end - start)) / CLOCKS_PER_SEC;

            printArray(instanciaMergeSort, "Sorted With Merge Sort", size, tempoGastoMerge);
            
            start = clock();
            radixsort(instanciaRadixSort, size);
            end = clock();
            tempoGastoRadix = ((double)(end - start)) / CLOCKS_PER_SEC;

            printArray(instanciaRadixSort, "Sorted With Radix Sort", size, tempoGastoRadix);

            free(instanciaInsertionSort);
            free(instanciaMergeSort);
            free(instanciaRadixSort);
            free(instancia);
        }
    }

    return 0;
}
