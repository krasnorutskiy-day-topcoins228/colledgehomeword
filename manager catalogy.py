import os
import datetime

FILE_NAME = "notes.txt"
def load_notes():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            notes = []
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|", 1)
                    if len(parts) == 2:
                        category = parts[0].strip()
                        text = parts[1].strip()
                        notes.append((category, text))
            return notes
    except FileNotFoundError:
        open(FILE_NAME, "w", encoding="utf-8").close()
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


def save_notes(notes):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for category, text in notes:
                f.write(f"{category} | {text}\n")
        return True
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")
        return False

def add_note():
    print("\n--- Добавление новой заметки ---")
    category = input("Введите категорию заметки: ").strip()
    while not category:
        print("Категория не может быть пустой!")
        category = input("Введите категорию заметки: ").strip()

    text = input("Введите текст заметки: ").strip()
    while not text:
        print("Текст заметки не может быть пустым!")
        text = input("Введите текст заметки: ").strip()

    add_date = input("Добавить дату к заметке? (да/нет): ").strip().lower()
    if add_date in ['да', 'д', 'yes', 'y']:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        text = f"[{current_date}] {text}"

    try:
        with open(FILE_NAME, "a", encoding="utf-8") as f:
            f.write(f"{category} | {text}\n")
        print("✓ Заметка успешно добавлена!")
        return True
    except Exception as e:
        print(f"✗ Ошибка при добавлении заметки: {e}")
        return False


def find_by_category(category):
    notes = load_notes()
    if not notes:
        return []

    result = [note for note in notes if note[0].lower() == category.lower()]
    return result


def search_word(word):
    notes = load_notes()
    if not notes:
        return []

    result = [note for note in notes if word.lower() in note[1].lower()]
    return result


def show_all_notes():
    notes = load_notes()

    if not notes:
        print("Заметок пока нет.")
        return

    print("\n--- Все заметки ---")
    for i, (category, text) in enumerate(notes, 1):
        print(f"{i}. Категория: {category}")
        print(f"   Текст: {text}")
        print()

    categories = set(note[0] for note in notes)
    print(f"Всего заметок: {len(notes)}")
    print(f"Уникальные категории: {', '.join(categories)}")

    show_sorted = input("\nПоказать заметки, отсортированные по длине? (да/нет): ").strip().lower()
    if show_sorted in ['да', 'д', 'yes', 'y']:
        sorted_notes = sorted(notes, key=lambda x: len(x[1]), reverse=True)
        print("\n--- Заметки (от самых длинных к коротким) ---")
        for i, (category, text) in enumerate(sorted_notes, 1):
            print(f"{i}. Категория: {category}")
            print(f"   Текст: {text} (длина: {len(text)} символов)")
            print()


def show_by_category():
    notes = load_notes()

    if not notes:
        print("Заметок пока нет.")
        return
    categories = sorted(set(note[0] for note in notes))

    print("\n--- Найти заметки по категории ---")
    print("Доступные категории:")
    for cat in categories:
        print(f"  - {cat}")

    category = input("\nВведите категорию для поиска: ").strip()
    if not category:
        print("Категория не указана.")
        return

    result = find_by_category(category)

    if not result:
        print(f"Заметок в категории '{category}' не найдено.")
    else:
        print(f"\n--- Заметки в категории '{category}' ({len(result)} шт.) ---")
        for i, (cat, text) in enumerate(result, 1):
            print(f"{i}. Текст: {text}")
            print()


def show_by_word():
    notes = load_notes()

    if not notes:
        print("Заметок пока нет.")
        return

    print("\n--- Поиск заметок по слову ---")
    word = input("Введите слово для поиска: ").strip()

    if not word:
        print("Слово не указано.")
        return

    result = search_word(word)

    if not result:
        print(f"Заметок, содержащих слово '{word}', не найдено.")
    else:
        print(f"\n--- Заметки, содержащие '{word}' ({len(result)} шт.) ---")
        for i, (category, text) in enumerate(result, 1):
            print(f"{i}. Категория: {category}")
            print(f"   Текст: {text}")
            print()


def main_menu():
    print("=" * 50)
    print("        ПРОГРАММА ДЛЯ РАБОТЫ С ЗАМЕТКАМИ")
    print("=" * 50)

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Найти по категории")
        print("4. Поиск по слову")
        print("5. Удалить заметку")
        print("6. Выход")

        choice = input("\nВыберите действие (1-6): ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            show_all_notes()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            show_by_word()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            print("\nДо свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")


def delete_note():
    notes = load_notes()

    if not notes:
        print("Заметок пока нет.")
        return

    print("\n--- Удаление заметки ---")
    print("Список заметок:")
    for i, (category, text) in enumerate(notes, 1):
        print(f"{i}. Категория: {category}")
        print(f"   Текст: {text[:50]}..." if len(text) > 50 else f"   Текст: {text}")
        print()

    try:
        note_num = int(input("Введите номер заметки для удаления: ").strip())
        if 1 <= note_num <= len(notes):
            deleted_note = notes.pop(note_num - 1)
            if save_notes(notes):
                print(f"✓ Заметка '{deleted_note[1][:30]}...' успешно удалена!")
        else:
            print("Неверный номер заметки.")
    except ValueError:
        print("Пожалуйста, введите число.")
    except Exception as e:
        print(f"Ошибка при удалении: {e}")


def main():
    if not os.path.exists(FILE_NAME):
        print(f"Файл {FILE_NAME} не найден. Создаю новый...")
        open(FILE_NAME, "w", encoding="utf-8").close()
        print("✓ Файл создан успешно.")

    main_menu()


if __name__ == "__main__":
    main()