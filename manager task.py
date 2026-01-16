import os


def load_notes():
    notes = []
    if not os.path.exists("notes.txt"):
        # Если файла нет, создаем пустой
        with open("notes.txt", "w", encoding="utf-8") as f:
            pass
        return notes

    try:
        with open("notes.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line:  # Пропускаем пустые строки
                    # Разбиваем строку по первому разделителю "|"
                    parts = line.split("|", 1)
                    if len(parts) == 2:
                        category = parts[0].strip()
                        text = parts[1].strip()
                        notes.append((category, text))
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return notes


def save_notes(notes):
    try:
        with open("notes.txt", "w", encoding="utf-8") as f:
            for category, text in notes:
                f.write(f"{category} | {text}\n")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")


def add_note():
    print("\n--- Добавление новой заметки ---")
    category = input("Введите категорию: ").strip()

    if not category:
        print("Категория не может быть пустой!")
        return

    text = input("Введите текст заметки: ").strip()

    if not text:
        print("Текст заметки не может быть пустым!")
        return

    try:
        with open("notes.txt", "a", encoding="utf-8") as f:
            f.write(f"{category} | {text}\n")
        print("Заметка успешно добавлена!")
    except Exception as e:
        print(f"Ошибка при добавлении заметки: {e}")


def show_all_notes():
    notes = load_notes()

    if not notes:
        print("\nНет заметок.")
        return

    print("\n--- Все заметки ---")
    print(f"Всего заметок: {len(notes)}")
    categories = set([note[0] for note in notes])
    print(f"Категории: {', '.join(categories)}")

    print("\nСписок заметок:")
    for i, (category, text) in enumerate(notes, 1):
        print(f"{i}. [{category}] {text}")
    print("\n--- Сортировка по длине текста ---")
    sorted_notes = sorted(notes, key=lambda x: len(x[1]))
    for i, (category, text) in enumerate(sorted_notes, 1):
        print(f"{i}. [{category}] {text[:50]}..." if len(text) > 50 else f"{i}. [{category}] {text}")


def find_by_category():
    print("\n--- Поиск по категории ---")
    notes = load_notes()
    if not notes:
        print("Нет заметок для поиска.")
        return

    categories = set([note[0] for note in notes])
    print(f"Доступные категории: {', '.join(categories)}")

    category = input("Введите категорию для поиска: ").strip()

    if not category:
        print("Категория не может быть пустой!")
        return
    result = [note for note in notes if note[0].lower() == category.lower()]

    if result:
        print(f"\nНайдено заметок в категории '{category}': {len(result)}")
        for i, (cat, text) in enumerate(result, 1):
            print(f"{i}. {text}")
    else:
        print(f"Заметок в категории '{category}' не найдено.")


def search_by_word():
    print("\n--- Поиск по слову ---")

    notes = load_notes()
    if not notes:
        print("Нет заметок для поиска.")
        return

    word = input("Введите слово для поиска: ").strip().lower()

    if not word:
        print("Слово для поиска не может быть пустым!")
        return
    result = [(cat, text) for cat, text in notes if word in text.lower()]

    if result:
        print(f"\nНайдено заметок со словом '{word}': {len(result)}")
        for i, (cat, text) in enumerate(result, 1):
            # Выделяем найденное слово в тексте
            highlighted = text.lower().replace(word, f"**{word.upper()}**")
            print(f"{i}. [{cat}] {highlighted}")
    else:
        print(f"Заметок со словом '{word}' не найдено.")


def main():
    if not os.path.exists("notes.txt"):
        with open("notes.txt", "w", encoding="utf-8") as f:
            pass

    while True:
        print("\n" + "=" * 40)
        print("МЕНЕДЖЕР ЗАМЕТОК")
        print("=" * 40)
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Найти по категории")
        print("4. Поиск по слову")
        print("5. Выход")
        print("=" * 40)

        choice = input("Выберите действие (1-5): ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            show_all_notes()
        elif choice == "3":
            find_by_category()
        elif choice == "4":
            search_by_word()
        elif choice == "5":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 5.")


if __name__ == "__main__":
    main()