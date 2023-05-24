#include "../headers/insertionSort.h"
#include "../headers/mergeSort.h"
#include "../headers/radixSort.h"

#include <stdio.h>

void printArray(int array[], char string[], int size){
    printf("%s", string);

    for (int i = 0; i < size; i++){
        printf("%i ", array[i]);
    }
}

int* generateRandomArray(int n) {
    int* array = (int*)malloc(n * sizeof(int));

    srand(time(NULL));

    for (int i = 0; i < n; i++) {
        array[i] = rand() % n;
    }

    return array;
}

int main(int argc, char *argv[ ]){  

    for (int i = 100; i < 1000; i*2){
        printf("Tamanho Instancia %i", i);
        for (int j = 0; j < 20; j++){
            printf("Instancia %i/20", j+1);
            int* instancia = generateinstancia(i);
            int size = sizeof(instancia) / sizeof(instancia[0]);

            int* instanciaInsertionSort = (int*)malloc(size * sizeof(int));
            memcpy(instanciaInsertionSort, instancia, size * sizeof(int));

            int* instanciaMergeSort = (int*)malloc(size * sizeof(int));
            memcpy(instanciaMergeSort, instancia, size * sizeof(int));

            int* instanciaRadixSort = (int*)malloc(size * sizeof(int));
            memcpy(instanciaRadixSort, instancia, size * sizeof(int));

            insertionSort(instanciaInsertionSort, size);
            mergeSort(instanciaMergeSort, 0, size-1);
            radixsort(instanciaRadixSort, size);

            printArray(instancia, "Instancia Real", size);
            printArray(instanciaInsertionSort, "Sorted With Insertion Sort", size);
            printArray(instanciaMergeSort, "Sorted With Merge Sort", size);
            printArray(instanciaRadixSort, "Sorted With Radix Sort", size);

            free(instancia);
            free(instanciaInsertionSort);
            free(instanciaMergeSort);
            free(instanciaRadixSort);

        }

        printf("------------------------------------------------------------------------\n");

    }
    
    
    return 0;
}

// gcc src/*.c -Wall
// ./a.exe > out/out.txt