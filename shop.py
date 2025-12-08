shop= {
    "Телефон": frozenset({"техника", "электроника"}),
    "Самурайский меч": frozenset({"редкое", "оружие"}),
    "Миксер": frozenset({"бытовое", "техника"}),
    "Смартфон": frozenset({"техника", "электроника"})
}
def find_by_category(category):
    return {item for item, categories in shop.items() if category in categories}
while True:
    print("\nМеню:")
    print("1. Добавить новый товар")
    print("2. Вывести все товары")
    print("3. Найти товары по категории")
    print("4. Выход")

    choice = input("Выберите действие (1-4): ")

    if choice == '1':
        name = input("Название товара: ").strip()
        categories_input = input("Категории через запятую: ").split(',')
        categories = frozenset(map(str.strip, categories_input))

        if name not in shop:
            shop[name] = categories
            print(f"Товар '{name}' успешно добавлен.")
        else:
            print(f"Товар '{name}' уже существует!")

    elif choice == '2':
        sorted_shop = dict(sorted(shop.items(), key=lambda x: len(x[0])))
        for good, cats in sorted_shop.items():
            print(f"{good}: {', '.join(cats)}")

    elif choice == '3':
        cat = input("Категория для поиска: ").strip()
        found_items = find_by_category(cat)
        if found_items:
            print(f"Товары в категории '{cat}': {', '.join(found_items)}")
        else:
            print(f"В указанной категории ничего не найдено.")

    elif choice == '4':
        break
    else:
        print("Неверный выбор. Повторите попытку.")
