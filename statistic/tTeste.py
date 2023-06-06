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

def mediaComIC(data):
    confidence_level = 0.95 
    sample_mean = np.mean(data)
    sample_std = np.std(data, ddof=1) 

    critical_value = stats.norm.ppf(1 - (1 - confidence_level) / 2)

    standard_error = sample_std / np.sqrt(len(data))

    margin_of_error = critical_value * standard_error

    confidence_interval = [sample_mean - margin_of_error, sample_mean + margin_of_error]
    
    mediaComIC = [sample_mean, confidence_interval[0], confidence_interval[1]]
    return mediaComIC

csv_file = "../output/output.csv"


insertion_sort_times = []
merge_sort_times = []
radix_sort_times = []

current_sample_size = 100

def analise(a, b, algoritmo1, algoritmo2):
    if((np.mean(a) - np.mean(b)) < 0):
        print("O algoritmo ", algoritmo1, " é melhor que o algoritmo ", algoritmo2, " para a amostra de tamanho: ", current_sample_size)
    else:
        print("O algoritmo ", algoritmo2, " é melhor que o algoritmo ", algoritmo1, " para a amostra de tamanho: ", current_sample_size)


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
            insertionSortMedia = mediaComIC(insertion_sort_times)
            mergeSortMedia = mediaComIC(merge_sort_times)
            radixSortMedia = mediaComIC(radix_sort_times)
            
            print("insertion" + str(current_sample_size) + ',' + str(insertionSortMedia[0]) + ',' + str(insertionSortMedia[1]) + ',' + str(insertionSortMedia[2]) )
            print("merge" + str(current_sample_size) + ',' + str(mergeSortMedia[0]) + ',' + str(mergeSortMedia[1]) + ',' + str(mergeSortMedia[2]) )
            print("radix" + str(current_sample_size) + ',' + str(radixSortMedia[0]) + ',' + str(radixSortMedia[1]) + ',' + str(radixSortMedia[2]) )
            
            # insertion_sort_interval = intervaloDeConfianca(insertion_sort_times, merge_sort_times)
            # merge_sort_interval = intervaloDeConfianca(merge_sort_times, radix_sort_times)
            # radix_sort_interval = intervaloDeConfianca(radix_sort_times, insertion_sort_times)
    
            # #verifica se o intervalo de confiança de cada algoritmo contém o valor 0
            # if insertion_sort_interval[0] <= 0 and insertion_sort_interval[1] >= 0:
            #     print("Algoritmos com tempos iguais para a amostra de tamanho: ", current_sample_size)
            # else:
            #     analise(insertion_sort_times, merge_sort_times, "insertion sort", "merge sort")

            # if merge_sort_interval[0] <= 0 and merge_sort_interval[1] >= 0:
            #     print("Algoritmos com tempos iguais para a amostra de tamanho: ", current_sample_size)
            # else:
            #     analise(merge_sort_times, radix_sort_times, "merge sort", "radix sort")
                
            # if radix_sort_interval[0] <= 0 and radix_sort_interval[1] >= 0:
            #     print("Algoritmos com tempos iguais para a amostra de tamanho: ", current_sample_size)
            # else:
            #     analise(radix_sort_times, insertion_sort_times, "radix sort", "insertion sort")
                
            print()
            
            #limpa as listas para a proxima iteração
            insertion_sort_times.clear()
            merge_sort_times.clear()
            radix_sort_times.clear()
                
            #incrementa o tamanho da amostra
            current_sample_size *= 2


