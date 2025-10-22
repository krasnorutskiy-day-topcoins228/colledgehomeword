def main():
    # Ввод начала и конца диапазона
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))

    # Проверка корректности диапазона
    if start > end:
        print("Ошибка: начало диапазона должно быть меньше или равно концу.")
        return

    print(f"Числа, кратные 7, в диапазоне от {start} до {end}:")

    # Поиск и вывод чисел, кратных 7
    for number in range(start, end + 1):
        if number % 7 == 0:
            print(number)


if __name__ == "__main__":
    main()