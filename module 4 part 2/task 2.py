import random

numbers = [random.randint(-100, 100) for _ in range(20)]

min_value = min(numbers)
max_value = max(numbers)

negative_count = sum(1 for x in numbers if x < 0)
positive_count = sum(1 for x in numbers if x > 0)
zero_count = sum(1 for x in numbers if x == 0)

print("Список чисел:", numbers)
print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Количество отрицательных чисел:", negative_count)
print("Количество положительных чисел:", positive_count)
print("Количество нулей:", zero_count)