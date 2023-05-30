import math
import scipy.stats as stats
import csv

file = open("../output/averege.csv", "r")
reader = csv.reader(file)
next(reader)

def calculate_confidence_interval(a, b, confidence_level=0.95):
    mean = (a + b) / 2
    std_dev = math.sqrt(((a - mean) ** 2 + (b - mean) ** 2) / 2)

    dof = 1  # Degrees of freedom (assuming a normal distribution with two numbers)
    alpha = 1 - confidence_level
    t_critical = stats.t.ppf(1 - alpha / 2, dof)

    margin_of_error = t_critical * std_dev / math.sqrt(2)

    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error

    return lower_bound, upper_bound

for row in reader:
    insertion = float(row[2])
    merge = float(row[3])
    radix = float(row[4])
    
    insertionMerge_lower, insertionMerge_upper =  calculate_confidence_interval(insertion, merge)
    insertionRadix_lower, insertionRadix_upper =  calculate_confidence_interval(insertion, radix)
    MergeRadix_lower, MergeRadix_upper =  calculate_confidence_interval(merge, radix)

    print("Tamanho" + row[0])
    print("insertion X Merge = " + str(insertionMerge_lower) + "|" +  str(insertionMerge_upper))
    print("insertion X Radix = " + str(insertionRadix_lower) + "|" +str(insertionRadix_upper))
    print("Merge X Radix     = " + str(MergeRadix_lower) +     "|" + str(MergeRadix_upper))
    print()



