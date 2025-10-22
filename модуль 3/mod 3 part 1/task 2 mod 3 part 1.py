def main():
    # Ввод начала и конца диапазона
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))

    # Проверка корректности диапазона
    if start > end:
        print("Ошибка: начало диапазона должно быть меньше или равно концу.")
        return

    # 1. Все числа диапазона
    print("Все числа диапазона:")
    for number in range(start, end + 1):
        print(number, end=' ')
    print()  # Переход на новую строку

    # 2. Все числа диапазона в убывающем порядке
    print("Все числа диапазона в убывающем порядке:")
    for number in range(end, start - 1, -1):
        print(number, end=' ')
    print()  # Переход на новую строку

    # 3. Все числа, кратные 7
    print("Числа, кратные 7:")
    multiples_of_7 = []
    for number in range(start, end + 1):
        if number % 7 == 0:
            multiples_of_7.append(number)

    print(multiples_of_7)  # Вывод списка чисел кратных 7

    # 4. Количество чисел, кратных 5
    count_multiples_of_5 = sum(1 for number in range(start, end + 1) if number % 5 == 0)
    print(f"Количество чисел, кратных 5: {count_multiples_of_5}")


if __name__ == "__main__":
    main()