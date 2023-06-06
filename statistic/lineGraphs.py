import csv
import matplotlib.pyplot as plt

file = open('../output/averege.csv', 'r')
reader = csv.DictReader(file)
data = list(reader)

sizes = [int(row['Size']) for row in data]
# insertion_times = [float(row[' Insertion Time']) for row in data]
merge_times = [float(row[' Merge Time']) for row in data]
radix_times = [float(row[' Radix Time']) for row in data]

# plt.xticks([100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400, 204800, 409600, 819200, 1638400], ["100", "200", "400", "800", "1600", "3200", "6400", "12800", "25600", "51200", "102400", "204800", "409600", "819200", "1638400"])

plt.figure(figsize=(10, 6))
# plt.plot(sizes, insertion_times, marker='o', label='Insertion Time')
plt.plot(sizes, merge_times, marker='o', label='Merge Time')
plt.plot(sizes, radix_times, marker='o', label='Radix Time')

plt.xlabel('Tamanho Instância')
plt.ylabel('Tempo Segundos')
plt.title('Merge x Radix')

plt.legend()

# plt.savefig("../graphs/linha/mergeRadix.png")
plt.show()


