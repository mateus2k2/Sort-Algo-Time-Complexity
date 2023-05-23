import random
from insertionSort import *
from mergeSort import *
from radixSort import *


def randomInstance(n):
    instance = []
    for _ in range(n):
        instance.append(random.randint(0, n*2))
    return instance

index = 100
while index < 200:
    for i in  range(0, 20):
        instance = randomInstance(index)
        resultInsertionSort = insertionSort(instance)
        resultMergeSort = mergeSort(instance)
        resultRadixSort = radixSort(instance)
        print(instance)
        print(resultInsertionSort)
        print(resultMergeSort)
        print(resultRadixSort)
    index *= 2