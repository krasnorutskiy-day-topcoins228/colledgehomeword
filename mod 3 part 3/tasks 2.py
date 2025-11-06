count = 0


for number in range(100, 999):

    str_number = str(number)


    if (str_number[0] == str_number[1]) or (str_number[0] == str_number[2]) or (str_number[1] == str_number[2]):
        count += 1

print("Количество целых чисел от 100 до 999 с двумя одинаковыми цифрами:", count)