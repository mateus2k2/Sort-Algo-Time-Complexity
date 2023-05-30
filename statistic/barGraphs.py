import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../output/averege.csv')

plt.figure(figsize=(10, 6))

sizes = df['Size'].unique()

positions = range(len(sizes))

bar_width = 0.2

plt.bar(positions, df[' Insertion Time'], width=bar_width, label='Insertion')
plt.bar([p + bar_width for p in positions], df[' Merge Time'], width=bar_width, label='Merge')
plt.bar([p + 2 * bar_width for p in positions], df[' Radix Time'], width=bar_width, label='Radix')

plt.xticks([p + bar_width for p in positions], sizes)

plt.ylabel('Time')

plt.title('Algorithm Execution Time by Size')

plt.legend()

plt.show()
