import sys
import pandas as pd

import matplotlib.pyplot as plt

processed_df = pd.read_csv(f"../results/processed-results/{sys.argv[1]}_processed.csv")

df = pd.DataFrame({
      'x_axis': range(0, 1000),
      'y_axis': processed_df["time"]
})

plt.xlabel('Request Number')
plt.ylabel('Median Latency (micro-seconds)')
# plt.yscale("log")
# plt.xscale("log")
plt.plot('x_axis', 'y_axis', data=df, linestyle='-')
plt.title(f"{sys.argv[1]}")
plt.savefig(f'../results/graphs/{sys.argv[1]}.jpeg')