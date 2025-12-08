def analyze_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            num_lines = len(lines)
            words_count = sum(len(line.split()) for line in lines)
            chars_count = sum(len(line) for line in lines)
            empty_lines = sum(1 for line in lines if line.strip() == '')

            print(f'Количество строк: {num_lines}')
            print(f'Количество слов: {words_count}')
            print(f'Количество символов: {chars_count}')
            print(f'Количество пустых строк: {empty_lines}')

    except FileNotFoundError:
        print('Файл не найден, попробуйте снова.')
    except PermissionError:
        print('Нет прав на чтение файла.')
    except Exception as e:
        print(f'Возникла ошибка: {e}')

filename = input('Введите имя файла: ')
analyze_file(filename)