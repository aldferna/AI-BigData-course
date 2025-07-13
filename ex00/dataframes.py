import numpy as np
import pandas as pd

pd.set_option('display.precision', 2)

dates_row = 7
patients_column = 7
min_temp = 35.0
max_temp = 40.0

matrix = np.random.uniform(min_temp, max_temp, size=(dates_row, patients_column))

df = pd.DataFrame(matrix, 
                  index=["Day {}".format(i+1) for i in range(dates_row)], 
                  columns=["Patiente {}".format(j+1) for j in range(patients_column)])
#personalized names: ['Day 1', 'Day 2', 'Day 3']


print("🔹 Original matrix (temperatures):")
print(df)

print("\n🔹 Average: patiente:")
print(df.mean(axis=0).round(2))

print("\n🔹 Min: patiente:")
print(df.min(axis=0).round(2))

print("\n🔹 Max: patiente:")
print(df.max(axis=0).round(2))

print("\n🔹 Average: day:")
print(df.mean(axis=1).round(2))

print("\n🔹 Min: day:")
print(df.min(axis=1).round(2))

print("\n🔹 Max: day:")
print(df.max(axis=1).round(2))

df_swapped = df[::-1]
print("\n🔹 Inverted rows:")
print(df_swapped)

df_copy = df.copy()
df_copy['Average temp/day'] = df.mean(axis=1)
#print(df_copy['Average temp/day']) = Day1:37.66  Day2:37.86  Day3:37.19 ...
df_sorted = df_copy.sort_values(by='Average temp/day').drop(columns='Average temp/day')
#print(df_copy) misma tabla que df; its oganized by the new column and then erased

print("\n🔹 Matrix sorted by average temperature in a day:")
print(df_sorted)
