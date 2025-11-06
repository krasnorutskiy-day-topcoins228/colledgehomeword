num_str = input("Введите целое число: ")
new_str = ""
for digit in num_str:
    if digit != '3' and digit != '6':
        new_str += digit

if new_str:
    result = int(new_str)
else:
    result = 0

print("Результат:", result)