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


def plot_confidence_interval(x, values, z=1.96, color='#2187bb', horizontal_line_width=0.25):
    mean = statistics.mean(values)
    stdev = statistics.stdev(values)
    confidence_interval = z * stdev / sqrt(len(values))

    left = x - horizontal_line_width / 2
    top = mean - confidence_interval
    right = x + horizontal_line_width / 2
    bottom = mean + confidence_interval
    plt.plot([x, x], [top, bottom], color=color)
    plt.plot([left, right], [top, top], color=color)
    plt.plot([left, right], [bottom, bottom], color=color)
    plt.plot(x, mean, 'o', color='#f44336')

    return mean, confidence_interval


plt.xticks([1, 2, 3, 4], ['FF', 'BF', 'FFD', 'BFD'])
plt.title('Confidence Interval')
plot_confidence_interval(1, [10, 11, 42, 45, 44])
plot_confidence_interval(2, [10, 21, 42, 45, 44])
plot_confidence_interval(3, [20, 2, 4, 45, 44])
plot_confidence_interval(4, [30, 31, 42, 45, 44])
plt.show()