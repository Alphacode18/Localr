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
for i in range(0, 1000):
    median_list.append([i, median([frames[0]['time'][i], frames[1]['time'][i], 
    frames[2]['time'][i], frames[3]['time'][i], frames[4]['time'][i]])])

median_df = pd.DataFrame(median_list, columns=["request", "time"])

median_df.to_csv(f"../processed-results/{sys.argv[1]}_processed.csv", encoding='utf-8', index=False)