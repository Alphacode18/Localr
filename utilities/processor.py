import os
import sys
import pandas as pd
from statistics import median

path, dirs, files = next(os.walk(f"../benchmark-results/{sys.argv[1]}"))
file_count = len(files)
frames = []
for iteration in range(file_count):
    if ".csv" in files[iteration]:
        df = pd.read_csv(f"../benchmark-results/{sys.argv[1]}/" + files[iteration], names=["request", "time"])
        frames.append(df)

median_list = []
for i in range(0, 5000):
    time = []
    for j in range(0, 500):
        time.append(frames[j]['time'][i])
    median_list.append([i, median(time)])

median_df = pd.DataFrame(median_list, columns=["request", "time"])

median_df.to_csv(f"../processed-results/{sys.argv[1]}_processed.csv", encoding='utf-8', index=False)