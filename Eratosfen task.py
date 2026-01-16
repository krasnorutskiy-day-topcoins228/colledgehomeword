import random
import math


def main():
    print("=" * 60)
    print("ОБЪЕДИНЕННЫЙ КОД: РЕШЕНИЕ ТРЕХ ЗАДАЧ")
    print("=" * 60)
    print("\n" + "=" * 60)
    print("1. РЕШЕТО ЭРАТОСФЕНА ДЛЯ ПОИСКА ПРОСТЫХ ЧИСЕЛ")
    print("=" * 60)

    def sieve_of_eratosthenes(start, end):
        if end < 2:
            return []
        is_prime = [True] * (end + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(end ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, end + 1, i):
                    is_prime[j] = False
        primes = [num for num in range(max(2, start), end + 1) if is_prime[num]]
        return primes
    start_num = 10
    end_num = 50
    primes = sieve_of_eratosthenes(start_num, end_num)
    print(f"Промежуток: от {start_num} до {end_num}")
    print(f"Простые числа: {primes}")
    print(f"Количество простых чисел: {len(primes)}")
    print("\n" + "=" * 60)
    print("2. ПЕРЕМЕШИВАНИЕ СЛОВ В ТЕКСТЕ")
    print("=" * 60)

    def shuffle_words(text, seed=None):
        if seed is not None:
            random.seed(seed)
        words = text.split()
        random.shuffle(words)
        shuffled_text = ' '.join(words)
        return shuffled_text
    text = "Дан текст со словами Перемешайте все слова этого текста в случайном порядке"
    print(f"Исходный текст: '{text}'")

    shuffled = shuffle_words(text)
    print(f"Перемешанный текст: '{shuffled}'")
    shuffled1 = shuffle_words(text, seed=42)
    shuffled2 = shuffle_words(text, seed=42)
    print(f"С seed=42 (1-й раз): '{shuffled1}'")
    print(f"С seed=42 (2-й раз): '{shuffled2}'")
    print(f"Результаты совпадают: {shuffled1 == shuffled2}")
    print("\n" + "=" * 60)
    print("3. ОБНУЛЕНИЕ СТОЛБЦА В ДВУМЕРНОМ СПИСКЕ")
    print("=" * 60)

    def print_matrix(matrix, title="Матрица"):
        print(f"\n{title}:")
        for row in matrix:
            print("  " + " ".join(f"{num:3d}" for num in row))

    def zero_column(matrix, column_index, inplace=False):
        if not inplace:
            result = [row.copy() for row in matrix]
        else:
            result = matrix
        if column_index < 0 or column_index >= len(result[0]):
            print(f"Ошибка: индекс столбца {column_index} вне диапазона!")
            return None if not inplace else None
        for row in result:
            row[column_index] = 0

        return result
    matrix = [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
        [51, 52, 53, 54, 55],
    ]

    print("Исходная матрица:")
    print_matrix(matrix)
    column_to_zero = 2
    result1 = zero_column(matrix, column_to_zero, inplace=False)
    print_matrix(result1, f"Матрица после обнуления столбца {column_to_zero} (без изменения оригинала)")
    matrix_copy = [row.copy() for row in matrix]
    result2 = zero_column(matrix_copy, column_to_zero, inplace=True)
    print_matrix(result2, f"Матрица после обнуления столбца {column_to_zero} (inplace)")
    print("\n" + "-" * 40)
    print("Проверка сохранности исходной матрицы:")
    print("Исходная матрица осталась неизменной:", matrix[0][2] == 13)
    print("\n" + "=" * 60)
    print("ДОПОЛНИТЕЛЬНЫЙ ПРИМЕР: ИСПОЛЬЗОВАНИЕ ВСЕХ ФУНКЦИЙ")
    print("=" * 60)
    print("\nСоздаем матрицу 3x3 из первых 9 простых чисел:")
    primes_9 = sieve_of_eratosthenes(2, 30)[:9]
    small_matrix = [[primes_9[i * 3 + j] for j in range(3)] for i in range(3)]
    print_matrix(small_matrix, "Матрица из простых чисел")
    zero_column(small_matrix, 1, inplace=True)
    print_matrix(small_matrix, "После обнуления среднего столбца")
    matrix_text = " ".join(str(num) for row in small_matrix for num in row)
    print(f"\nТекст из элементов матрицы: '{matrix_text}'")
    shuffled_matrix_text = shuffle_words(matrix_text)
    print(f"Перемешанный текст: '{shuffled_matrix_text}'")

    print("\n" + "=" * 60)
    print("ВСЕ ЗАДАЧИ ВЫПОЛНЕНЫ УСПЕШНО!")
    print("=" * 60)


if __name__ == "__main__":
    main()