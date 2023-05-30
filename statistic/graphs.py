import csv
import matplotlib.pyplot as plt

file = open('../output/averege.csv', 'r')
reader = csv.DictReader(file)
data = list(reader)

sizes = [int(row['Size']) for row in data]
insertion_times = [float(row[' Insertion Time']) for row in data]
merge_times = [float(row[' Merge Time']) for row in data]
radix_times = [float(row[' Radix Time']) for row in data]

plt.figure(figsize=(10, 6))
plt.plot(sizes, insertion_times, marker='o', label='Insertion Time')
plt.plot(sizes, merge_times, marker='o', label='Merge Time')
plt.plot(sizes, radix_times, marker='o', label='Radix Time')

plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Sorting Algorithms Performance')

plt.legend()

plt.show()


