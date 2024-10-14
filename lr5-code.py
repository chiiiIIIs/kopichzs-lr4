def calculate_column_sums_and_counts(array, lower_bound, upper_bound):
 rows = len(array)
 cols = len(array[0]) if rows > 0 else 0

 for col in range(cols):
  column_sum = 0
  count = 0
 
  for row in range(rows):
   if lower_bound <= array[row][col] <= upper_bound:
    column_sum += array[row][col]
    count += 1

  if count > 0:
     print(f"Столбец {col}: Сумма = {column_sum}, Количество = {count}")
 else:
     print(f"Столбец {col}: Нет элементов в заданном диапазоне.")
array1 = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
array2 = [
 [10, 11, 12],
 [13, 14, 15],
 [16, 17, 18]
]
4
lower_bound = 5
upper_bound = 15
print("Результаты для первого массива:")
calculate_column_sums_and_counts(array1, lower_bound, upper_bound)
print("\nРезультаты для второго массива:")
calculate_column_sums_and_counts(array2, lower_bound, upper_bound)
