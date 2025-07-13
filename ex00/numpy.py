import numpy as np

np.set_printoptions(precision=2, suppress=True)

dates_row = 7
patients_column = 7
min_temp = 35.0
max_temp = 40.0

#matrix = np.array([[1, 2, 3], [4, 5, 6]]) -> no random values
#matrix = np.random.randint(min, max, quantity) -> for int and 1D
matrix = np.random.uniform(min_temp, max_temp, size=(dates_row, patients_column))

average_patiente = np.mean(matrix, axis=0)
#axis=0 (computes the mean column by column - by patient in this ex)
#average_patiente is an array with the results
min_patiente = np.min(matrix, axis=0)
max_patiente = np.max(matrix, axis=0)

average_day = np.mean(matrix, axis=1)
#axis=1 (computes the mean row by row - by day in this ex)
min_day = np.min(matrix, axis=1)
max_day = np.max(matrix, axis=1)

print("\n🔹 Patiente - average temperature:")
print(average_patiente)

print("\n🔹 Patiente - min temp:")
print(min_patiente)

print("\n🔹 Patiente - max temp:")
print(max_patiente)

print("\n🔹 Day - average temperature:")
print(average_day)

print("\n🔹 Day - min temp:")
print(min_day)

print("\n🔹 Day - max temp:")
print(max_day)

matrix_swapped = matrix[::-1]

print("\n🔹 Inverted rows:")
print(matrix_swapped)

sorted_index = np.argsort(average_day)
#print(average_day) = [37.96 37.97 37.72 37.93 37.44 38.17 37.61]
#print(sorted_index) = [6 4 1 0 2 5 3]
matrix_sorted_by_day_avg = matrix[sorted_index]

print("\n🔹 Matriz sorted by average temperature in a day:")
print(matrix_sorted_by_day_avg)
