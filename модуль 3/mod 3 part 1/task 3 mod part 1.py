def main():
    # Ввод начала и конца диапазона
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))

    # Проверка корректности диапазона
    if start > end:
        print("Ошибка: начало диапазона должно быть меньше или равно концу.")
        return

    # Анализ чисел в диапазоне
    for number in range(start, end + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("Fizz Buzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

if __name__ == "__main__":
    main()