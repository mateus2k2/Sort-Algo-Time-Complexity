import matplotlib.pyplot as plt
import statistics
from math import sqrt
import csv


def plot_confidence_interval(x, mean, bottom, top, color='#2187bb', horizontal_line_width=0.25):
    # horizontal_line_width = (10000 * (top - bottom)) * 0.0025

    left = x - horizontal_line_width / 2
    right = x + horizontal_line_width / 2
        
    plt.plot([x, x], [top, bottom], color=color)
    plt.plot([left, right], [top, top], color=color)
    plt.plot([left, right], [bottom, bottom], color=color)
    plt.plot(x, mean, 'o', color='#f44336')

file = open("../output/IntervaloMedia.csv", "r")
reader = csv.reader(file)
next(reader)

tamanho = 100

for row in reader:
    if row:
        plt.xlim(-3, 5)
        plt.title('Confidence Interval Tamanho ' + str(tamanho))
        plt.xticks([0, 1, 2], ["Insertion", "Merge", "Radix"])
        
        plot_confidence_interval(0, float(row[1]), float(row[2]), float(row[3])) 
        row = next(reader)
        
        plot_confidence_interval(1, float(row[1]), float(row[2]), float(row[3])) 
        row = next(reader)
        
        plot_confidence_interval(2, float(row[1]), float(row[2]), float(row[3])) 
        row = next(reader)
        
        plt.savefig("../graphs/conf/pythonMesmoGrafico/" + str(tamanho) + ".png")
        plt.clf()
        
        tamanho *= 2
        # plt.show()
        # break


# for row in reader:
#     if row:
#         plt.xlim(-3, 3)
#         plt.title('Confidence Interval Insertion Sort Tamanho ' + str(tamanho))
#         plt.xticks([0], ["insertion"])
#         plot_confidence_interval(0, float(row[1]), float(row[2]), float(row[3])) 
#         plt.savefig("../graphs/conf/python/" + str(tamanho) + "Insertion" + ".png")
#         plt.clf()
#         row = next(reader)
        
#         plt.xlim(-3, 3)
#         plt.title('Confidence Interval Merge Sort Tamanho ' + str(tamanho))
#         plt.xticks([0], ["Merge"])
#         plot_confidence_interval(0, float(row[1]), float(row[2]), float(row[3])) 
#         plt.savefig("../graphs/conf/python/" + str(tamanho) + "Merge" + ".png")
#         plt.clf()
#         row = next(reader)
        
#         plt.xlim(-3, 3)
#         plt.title('Confidence Interval radix Sort Tamanho ' + str(tamanho))
#         plt.xticks([0], ["radix"])
#         plot_confidence_interval(0, float(row[1]), float(row[2]), float(row[3])) 
#         plt.savefig("../graphs/conf/python/" + str(tamanho) + "Radix" + ".png")
#         plt.clf()
#         row = next(reader)
        
#         tamanho *= 2
#         # break

