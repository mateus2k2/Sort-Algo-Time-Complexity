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

file = open("../output/grafico.csv", "r")
reader = csv.reader(file)
next(reader)

tamanho = 6400

plt.xticks([1, 2, 3], ["insertionRadix", "mergeRadix", "radixInsertion"])
plt.title('Confidence Interval = Tamanho = ' + str(tamanho))

for row in reader:
    if row and str(tamanho) in row[0]:
        plot_confidence_interval(1, float(row[1]), float(row[2]), float(row[3])) 
        row = next(reader)
        plot_confidence_interval(2, float(row[1]), float(row[2]), float(row[3]))
        row = next(reader)
        plot_confidence_interval(3, float(row[1]), float(row[2]), float(row[3]))
        break

plt.show()