count = 0


for i in range(100, 9999):
    i_str = str(i)

    if (i_str[0] == i_str[1]) or (i_str[0] == i_str[2]):
        count += 1

print("Количество целых чисел от 100 до 9999 с разными цифрами:", count)