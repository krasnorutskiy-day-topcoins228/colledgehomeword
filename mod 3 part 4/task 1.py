import math

def is_prime(n):
    """Проверяем, является ли число n простым."""
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):  # проверяем до квадратного корня
        if n % i == 0:
            return False
    return True

# Пример диапазона (его должен задать пользователь)
lower = int(input("Введите нижнюю границу диапазона: "))
upper = int(input("Введите верхнюю границу диапазона: "))

print(f"Простые числа в диапазоне {lower}-{upper}:")
for num in range(lower, upper+1):
    if is_prime(num):
        print(num)