import sys
import pandas as pd

import matplotlib.pyplot as plt

processed_df = pd.read_csv(f"../results/processed/{sys.argv[1]}_processed.csv")

df = pd.DataFrame({
      'x_axis': range(0, 2500),
      'y_axis': processed_df["time"]
})

plt.xlabel('Request Number')
plt.ylabel('Median Latency (micro-seconds)')
plt.plot('x_axis', 'y_axis', data=df, linestyle='-')
plt.title(f"{sys.argv[1]}")
plt.savefig(f'../results/graphs/{sys.argv[1]}.jpeg')