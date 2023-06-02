import math
import scipy.stats as stats
import csv
import numpy as np

file = open("../output/averege.csv", "r")
reader = csv.reader(file)
next(reader)

def calculaIntervaloConfianca(a, b, confianca=0.95):
    diferencaMedias = a - b
    
    var = stats.t.interval( confidence=confianca,
                            df=len(diferencaMedias)-1,
                            loc=np.mean(diferencaMedias), 
                            scale=stats.sem(diferencaMedias))

    return var

def calculaTudo():
    for row in reader:
        insertion = float(row[2])
        merge = float(row[3])
        radix = float(row[4])
        
        insertionMerge_lower, insertionMerge_upper =  calculaIntervaloConfianca(insertion, merge)
        insertionRadix_lower, insertionRadix_upper =  calculaIntervaloConfianca(insertion, radix)
        MergeRadix_lower, MergeRadix_upper =  calculaIntervaloConfianca(merge, radix)

        print("Tamanho" + row[0])
        print("insertion X Merge = " + str(insertionMerge_lower) + "|" + str(insertionMerge_upper))
        print("insertion X Radix = " + str(insertionRadix_lower) + "|" + str(insertionRadix_upper))
        print("Merge X Radix     = " + str(MergeRadix_lower) +     "|" + str(MergeRadix_upper))
        print()

# Era pra dar = (-6.92, 6.26)
print(calculaIntervaloConfianca(-0.33, 0))
