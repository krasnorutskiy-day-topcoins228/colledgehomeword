class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self):
        print("Персонаж атакует!")

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Сила: {self.power})"


class Warrior(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp + 30, power + 5)

    def attack(self):
        print("Воин наносит мощный удар мечом!")


class Mage(Character):
    def __init__(self, name, hp, power, mana):
        super().__init__(name, hp, power - 3)
        self.mana = mana
    def attack(self):
        print("Маг выпускает огненный шар!")

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Сила: {self.power}, Мана: {self.mana})"


class Archer(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp + 10, power + 3)

    def attack(self):
        print("Лучник стреляет из лука!")

characters = []
characters.append(Warrior("Арагорн", 120, 20))
characters.append(Mage("Гендальф", 80, 10, 200))
characters.append(Archer("Леголас", 90, 15))


def create_character():
    print("\n=== Создание персонажа ===")
    print("1. Воин")
    print("2. Маг")
    print("3. Лучник")

    try:
        choice = int(input("Выберите тип персонажа: "))

        if choice not in [1, 2, 3]:
            print("Некорректный выбор!")
            return

        name = input("Введите имя персонажа: ")

        if choice == 1:
            hp = int(input("Введите здоровье (базовое): "))
            power = int(input("Введите силу (базовую): "))
            characters.append(Warrior(name, hp, power))
            print(f"Воин {name} создан!")

        elif choice == 2:
            hp = int(input("Введите здоровье: "))
            power = int(input("Введите силу: "))
            mana = int(input("Введите количество маны: "))
            characters.append(Mage(name, hp, power, mana))
            print(f"Маг {name} создан!")

        elif choice == 3:
            hp = int(input("Введите здоровье (базовое): "))
            power = int(input("Введите силу (базовую): "))
            characters.append(Archer(name, hp, power))
            print(f"Лучник {name} создан!")

    except ValueError:
        print("Ошибка: введите числовые значения!")


def show_all_characters():
    print("\n=== Список всех персонажей ===")
    if not characters:
        print("Персонажей нет!")
        return

    for i, character in enumerate(characters, 1):
        print(f"{i}. {character}")


def character_attack():
    show_all_characters()

    if not characters:
        return

    try:
        index = int(input("\nВведите номер персонажа для атаки: ")) - 1

        if 0 <= index < len(characters):
            print(f"\n{characters[index].name}: ", end="")
            characters[index].attack()
        else:
            print("Некорректный номер персонажа!")

    except ValueError:
        print("Ошибка: введите число!")


def main():
    print("=== Система персонажей игры ===")

    while True:
        print("\n--- Меню ---")
        print("1. Создать персонажа")
        print("2. Показать всех персонажей")
        print("3. Атака персонажа")
        print("4. Выход")

        try:
            choice = int(input(">>> "))

            if choice == 1:
                create_character()
            elif choice == 2:
                show_all_characters()
            elif choice == 3:
                character_attack()
            elif choice == 4:
                print("Выход из программы...")
                break
            else:
                print("Некорректный выбор! Выберите от 1 до 4.")

        except ValueError:
            print("Ошибка: введите число от 1 до 4!")


if __name__ == "__main__":
    main()