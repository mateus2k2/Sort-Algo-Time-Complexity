import csv
import matplotlib.pyplot as plt

csv_file = '../output/averege.csv'
output_dir = '../graphs/'

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Skip the header row

    for row in reader:
        size = int(row[0])
        insertion_time = float(row[2])
        merge_time = float(row[3])
        radix_time = float(row[4])

        # Plot the bar graph
        plt.figure()
        plt.bar(['Insertion', 'Merge', 'Radix'], [insertion_time, merge_time, radix_time])
        plt.xlabel('Algorithm')
        plt.ylabel('Time')
        plt.title(f'Size: {size}')
        # plt.show()
        # plt.savefig(f'{output_dir}size_{size}.png')
        # plt.clf()
        # plt.close()
