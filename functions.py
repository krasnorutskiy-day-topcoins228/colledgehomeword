def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        times = "раз" if wrapper.count % 10 in (2, 3, 4) and wrapper.count % 100 not in (12, 13, 14) else "раз"
        print(f"Функция {func.__name__} вызвана {wrapper.count} {times}")
        print(f"Аргументы: {args if args else '()'}{', ' + str(kwargs) if kwargs else ''}")
        result = func(*args, **kwargs)
        return result
    wrapper.count = 0
    return wrapper
@call_counter
def add(a, b):
    return a + b
@call_counter
def repeat(text, n):
    return text * n
@call_counter
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

if __name__ == "__main__":
    print(add(2, 3))
    print()

    print(add(10, 5))
    print()
    print(repeat("Hi", 3))
    print()

    print(repeat("Test", 2))
    print()
    print(greet("Alice"))
    print()

    print(greet("Bob", greeting="Hi"))