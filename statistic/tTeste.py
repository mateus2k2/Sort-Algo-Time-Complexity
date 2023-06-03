import math
import scipy.stats as stats
import csv
import numpy as np

def desvioSobreN(a):
    return (np.std(a)**2) / len(a)

def desvioPadraoDasDiferencas(a, b):
    desvioA = np.std(a)
    desvioB = np.std(b)
    desvioDasDiferencas = np.sqrt(desvioSobreN(a) + desvioSobreN(b))
    return desvioDasDiferencas

def grauDeLiberdade(a, b):
    desvioA = np.std(a)
    desvioB = np.std(b)
    aux1 = (desvioSobreN(a) + desvioSobreN(b))**2
    aux2 = (desvioSobreN(a)**2) * (1 / (len(a) + 1))
    aux3 = (desvioSobreN(b)**2) * (1 / (len(b) + 1))
    grauDeLiberdade = (aux1 / (aux2 + aux3)) - 2
    
    return grauDeLiberdade

def valorT(confianca, grausDeLiberdade):
    significancia = 1 - confianca
    t = stats.t.ppf(1 - (significancia / 2), grausDeLiberdade)
    return t

def intervaloDeConfianca(a, b):
    desvioDasDiferencas = desvioPadraoDasDiferencas(a, b)
    grausDeLiberdade = grauDeLiberdade(a, b)
    t = valorT(0.95, round(grausDeLiberdade))
    mediaDasDiferencas = np.mean(a) - np.mean(b)
    intervalo = [mediaDasDiferencas - (t * desvioDasDiferencas), mediaDasDiferencas + (t * desvioDasDiferencas)]
    return intervalo

def retornaMedia(a, b):
    mediaA = np.mean(a)
    mediaB = np.mean(b)
    mediaDasDiferencas = mediaA - mediaB
    return [mediaA, mediaB, mediaDasDiferencas]
    

csv_file = "../output/output.csv"


insertion_sort_times = []
merge_sort_times = []
radix_sort_times = []


current_sample_size = 100


with open(csv_file, "r") as file:
    reader = csv.reader(file)
    next(reader)
    #itera sobre as linhas do arquivo
    for row in reader:
        if row:
            insertion_sort_times.append(float(row[2]))
            merge_sort_times.append(float(row[3]))
            radix_sort_times.append(float(row[4]))
        
        else:      
            print("current_sample_size: ", current_sample_size)
            # print(insertion_sort_times)
            # print(merge_sort_times)
            # print(radix_sort_times)
            
            #calcula o intervalo de confiança para cada algoritmo
            insertionRadix_sort_interval = intervaloDeConfianca(insertion_sort_times, merge_sort_times)
            mergeRadix_sort_interval = intervaloDeConfianca(merge_sort_times, radix_sort_times)
            radixInsertion_sort_interval = intervaloDeConfianca(radix_sort_times, insertion_sort_times)
            
            #verifica se o intervalo de confiança de cada algoritmo contém o valor 0
            # if insertionRadix_sort_interval[0] <= 0 and insertionRadix_sort_interval[1] >= 0:
            #     print("insertion sort: ", insertionRadix_sort_interval)
            # if mergeRadix_sort_interval[0] <= 0 and mergeRadix_sort_interval[1] >= 0:
            #     print("merge sort: ", mergeRadix_sort_interval)
            # if radixInsertion_sort_interval[0] <= 0 and radixInsertion_sort_interval[1] >= 0:
            #     print("radix sort: ", radixInsertion_sort_interval)
            print("insertionRadixSortConf =  ", insertionRadix_sort_interval)
            print("mergeRadixSortConf =      ", mergeRadix_sort_interval)
            print("radixInsertionSortConf =  ", radixInsertion_sort_interval)
            
            print("insertionRadixSortMean =  ", retornaMedia(insertion_sort_times, merge_sort_times))
            print("mergeRadixSortMean =      ", retornaMedia(merge_sort_times, radix_sort_times))
            print("radixInsertionSortMean =  ", retornaMedia(radix_sort_times, insertion_sort_times))
            
            print()
            
            #limpa as listas para a proxima iteração
            insertion_sort_times.clear()
            merge_sort_times.clear()
            radix_sort_times.clear()
            
            #incrementa o tamanho da amostra
            current_sample_size *= 2


