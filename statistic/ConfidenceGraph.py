# import numpy as np
# import matplotlib.pyplot as plt

# # Generate sample data
# np.random.seed(0)
# sample_data = np.random.normal(loc=5, scale=2, size=100)

# # Calculate mean and standard deviation
# mean = np.mean(sample_data)
# std = np.std(sample_data)

# # Set confidence level and calculate confidence interval
# confidence_level = 0.95
# z_score = 1.96  # For 95% confidence level (two-tailed)
# margin_of_error = z_score * std / np.sqrt(len(sample_data))
# lower_bound = mean - margin_of_error
# upper_bound = mean + margin_of_error

# # Plotting
# plt.errorbar(x=0, y=mean, yerr=margin_of_error, fmt='o', capsize=5, label='Confidence Interval')
# plt.axhline(mean, color='red', linestyle='--', label='Sample Mean')
# plt.axhline(lower_bound, color='green', linestyle='--', label='Lower Bound')
# plt.axhline(upper_bound, color='green', linestyle='--', label='Upper Bound')
# plt.xlabel('Sample')
# plt.ylabel('Value')
# plt.legend()
# plt.title('Confidence Interval Graph')
# plt.show()





# import numpy as np
# from pylab import *

# data1 = [53,38,29]
# data2 = [16,29,32,34,40,44,49,51,52,53]
# data3 = np.random.normal(loc=39,scale=10,size=30)
# data = [data1,np.abs(data2),data3]

# def do_error_bar(x,e,lw=2,w=2):
#     o = plot([x,x],[m+e,m-e],color='k',lw=lw)
#     o = plot([x-w,x+w],[m+e,m+e],color='k',lw=lw)
#     o = plot([x-w,x+w],[m-e,m-e],color='k',lw=lw)

# #layout from 1 to 100
# N = len(data)
# total = 100
# margin = 5
# space = 15
# fig_width = total - margin*2
# all_spaces = (N-1)*space
# total_group_width = fig_width - all_spaces
# group_width = total_group_width * 1.0 / N

# dx = group_width/3.0    # 4 elements per group
# x = margin              # start
# tD = {3:3.182, 10:2.228, 30:2.042}
# S = 50                  # large circle size
# s = 10                  # small circle size
# y = 17                  # y pos for text

# for group in data:
#     for g in group:
#         scatter(x,g,s=s,color='k')
        
#     x += dx
#     n = len(group)
#     m = np.mean(group)
#     sd = np.std(group)
#     scatter(x,m,s=S,color='k')
#     do_error_bar(x,sd)
#     text(x-1.5,y,'std')
#     text(x,y-5,'n = ' + str(n))
    
#     x += dx
#     se = sd/np.sqrt(n)
#     t = tD[n]
#     ci = t * se
#     scatter(x,m,s=S,color='k')
#     do_error_bar(x,ci)
#     text(x-1.5,y,'CI')
    
#     x += dx
#     scatter(x,m,s=S,color='k')
#     do_error_bar(x,se)
#     text(x-1.5,y,'se')
#     x += space

# ax = axes()
# ax.xaxis.set_visible(False)
# show()





import matplotlib.pyplot as plt
import statistics
from math import sqrt


def plot_confidence_interval(x, top, bottom, mean, color='#2187bb', horizontal_line_width=0.25):
    # mean = statistics.mean(values)
    # stdev = statistics.stdev(values)
    # confidence_interval = z * stdev / sqrt(len(values))

    left = x - horizontal_line_width / 2
    # top = mean - confidence_interval
    right = x + horizontal_line_width / 2
    # bottom = mean + confidence_interval
    plt.plot([x, x], [top, bottom], color=color)
    plt.plot([left, right], [top, top], color=color)
    plt.plot([left, right], [bottom, bottom], color=color)
    plt.plot(x, mean, 'o', color='#f44336')



insertionRadixSortConf100  =   [-7.096895771203344e-06, -4.003104228796652e-06]
insertionRadixSortConf200  =   [6.268517743502347e-06, 2.3131482256497647e-05]
insertionRadixSortConf400  =   [-4.4655892880564026e-05, 0.000548455892880564]
insertionRadixSortConf800  =   [0.0001544712671690807, 0.0011715287328309197]
insertionRadixSortConf1600 =   [0.0038162298214923355, 0.005754370178507665]
insertionRadixSortConf3200 =   [0.011658887273331994, 0.02056371272666801]
insertionRadixSortConf6400 =   [0.04458208969819466, 0.05030581030180532]

insertionRadixSortMean100  =   [1.4750000000000001e-05, 2.03e-05, -5.549999999999998e-06]
insertionRadixSortMean200  =   [7.055e-05, 5.5849999999999996e-05, 1.4699999999999998e-05]
insertionRadixSortMean400  =   [0.00038065, 0.00012875, 0.0002519]
insertionRadixSortMean800  =   [0.0010565000000000001, 0.0003934999999999999, 0.0006630000000000002]
insertionRadixSortMean1600 =   [0.00544645, 0.00066115, 0.0047853]
insertionRadixSortMean3200 =   [0.01747695, 0.00136565, 0.016111300000000002]
insertionRadixSortMean6400 =   [0.049212799999999994, 0.0017688499999999995, 0.04744394999999999]



plt.xticks([1, 2, 3, 4, 5, 6, 7], ["100", "200", "400", "800", "1600", "3200", "6400"])
plt.title('Confidence Interval = Insertion X Radix')
plot_confidence_interval(1, max(insertionRadixSortConf100), min(insertionRadixSortConf100), insertionRadixSortMean100[2])
plot_confidence_interval(2, max(insertionRadixSortConf200), min(insertionRadixSortConf200), insertionRadixSortMean200[2])
plot_confidence_interval(3, max(insertionRadixSortConf400), min(insertionRadixSortConf400), insertionRadixSortMean400[2])
plot_confidence_interval(4, max(insertionRadixSortConf800), min(insertionRadixSortConf800), insertionRadixSortMean800[2])
plot_confidence_interval(5, max(insertionRadixSortConf1600), min(insertionRadixSortConf1600), insertionRadixSortMean1600[2])
plot_confidence_interval(6, max(insertionRadixSortConf3200), min(insertionRadixSortConf3200), insertionRadixSortMean3200[2])
plot_confidence_interval(7, max(insertionRadixSortConf6400), min(insertionRadixSortConf6400), insertionRadixSortMean6400[2])
plt.show()


# plt.xticks([100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400, 204800, 409600, 819200, 1638400], ["100", "200", "400", "800", "1600", "3200", "6400", "12800", "25600", "51200", "102400", "204800", "409600", "819200", "1638400"])
