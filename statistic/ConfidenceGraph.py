import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import statistics
from math import sqrt
import csv
import numpy as np

file = open("../output/IntervaloMedia.csv", "r")
reader = csv.reader(file)
next(reader)

def plot_confidence_interval(x, mean, bottom, top, color='#2187bb'):
    plt.errorbar(x, mean, yerr=[[mean-bottom], [top-mean]], fmt='o', color=color, capsize=5, capthick=1)
    plt.vlines(x, bottom, top, colors=color, linestyles='solid')
    plt.plot(x, mean, marker='o', color=color)

def tudoJuntoPorImagem():
    dicionarioIntervalo = { "100": 1, "200": 2, "400": 3, "800": 4, "1600": 5, "3200": 6, "6400": 7, "12800": 8, "25600": 9, "51200": 10, "102400": 11, "204800": 12, "409600": 13, "819200": 14, "1638400": 15 }

    for row in reader:
        if row :
            plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], ["100", "200", "400", "800", "1600", "3200", "6400", "12800", "25600", "51200", "102400", "204800", "409600", "819200", "1638400"])        
            tamanhoAtual = row[0].replace("insertion", "")
            plt.title('Confidence Interval Tamanho ' + tamanhoAtual)
            
            plot_confidence_interval(dicionarioIntervalo[tamanhoAtual], float(row[1]), float(row[2]), float(row[3]), "#2ca02c") 
            row = next(reader)
            
            plot_confidence_interval(dicionarioIntervalo[tamanhoAtual], float(row[1]), float(row[2]), float(row[3]), '#ff7f0e') 
            row = next(reader)
            
            plot_confidence_interval(dicionarioIntervalo[tamanhoAtual], float(row[1]), float(row[2]), float(row[3]), '#1f77b4') 
            row = next(reader)
            
            cor1 = mpatches.Patch(color='#2ca02c', label='Insertion')
            cor2 = mpatches.Patch(color='#ff7f0e', label='Merge')
            cor3 = mpatches.Patch(color='#1f77b4', label='Radix')
            plt.legend(handles=[cor1, cor2, cor3])

            plt.xlabel('Instância')
            plt.ylabel('Intervalo')

            plt.grid(True)
            
            plt.savefig("../graphs/conf/tudoJunto/" + tamanhoAtual +".png")
            plt.clf()
            
            # break
    
    # plt.savefig("../graphs/conf/tudoJunto.png")
    # plt.show()

def tudoJunto():
    plt.title('Confidence Interval')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], ["100", "200", "400", "800", "1600", "3200", "6400", "12800", "25600", "51200", "102400", "204800", "409600", "819200", "1638400"])        

    dicionarioIntervalo = { "100": 1, "200": 2, "400": 3, "800": 4, "1600": 5, "3200": 6, "6400": 7, "12800": 8, "25600": 9, "51200": 10, "102400": 11, "204800": 12, "409600": 13, "819200": 14, "1638400": 15 }
    permitidos = ["100"]
    # "100", "200", "400", "800", "1600", "3200", "6400", "12800", "25600", "51200", "102400", "204800", "409600", "819200", "1638400"

    for row in reader:
        if row and (row[0].replace("insertion", "") in permitidos):
            tamanhoAtual = row[0].replace("insertion", "")
            
            plot_confidence_interval(dicionarioIntervalo[tamanhoAtual], float(row[1]), float(row[2]), float(row[3]), "#2ca02c") 
            row = next(reader)
            
            plot_confidence_interval(dicionarioIntervalo[tamanhoAtual], float(row[1]), float(row[2]), float(row[3]), '#ff7f0e') 
            row = next(reader)
            
            plot_confidence_interval(dicionarioIntervalo[tamanhoAtual], float(row[1]), float(row[2]), float(row[3]), '#1f77b4') 
            row = next(reader)
            
            # break

    cor1 = mpatches.Patch(color='#2ca02c', label='Insertion')
    cor2 = mpatches.Patch(color='#ff7f0e', label='Merge')
    cor3 = mpatches.Patch(color='#1f77b4', label='Radix')
    plt.legend(handles=[cor1, cor2, cor3])

    plt.xlabel('Instância')
    plt.ylabel('Intervalo')

    plt.grid(True)
    
    # plt.savefig("../graphs/conf/tudoJunto.png")
    plt.show()

def porTamanho():
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

def separado():
    for row in reader:
        if row:
            plt.xlim(-3, 3)
            plt.title('Confidence Interval Insertion Sort Tamanho ' + str(tamanho))
            plt.xticks([0], ["insertion"])
            plot_confidence_interval(0, float(row[1]), float(row[2]), float(row[3])) 
            plt.savefig("../graphs/conf/python/" + str(tamanho) + "Insertion" + ".png")
            plt.clf()
            row = next(reader)
            
            plt.xlim(-3, 3)
            plt.title('Confidence Interval Merge Sort Tamanho ' + str(tamanho))
            plt.xticks([0], ["Merge"])
            plot_confidence_interval(0, float(row[1]), float(row[2]), float(row[3])) 
            plt.savefig("../graphs/conf/python/" + str(tamanho) + "Merge" + ".png")
            plt.clf()
            row = next(reader)
            
            plt.xlim(-3, 3)
            plt.title('Confidence Interval radix Sort Tamanho ' + str(tamanho))
            plt.xticks([0], ["radix"])
            plot_confidence_interval(0, float(row[1]), float(row[2]), float(row[3])) 
            plt.savefig("../graphs/conf/python/" + str(tamanho) + "Radix" + ".png")
            plt.clf()
            row = next(reader)
            
            tamanho *= 2
            # break

tudoJuntoPorImagem()