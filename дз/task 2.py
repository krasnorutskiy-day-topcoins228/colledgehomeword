text = input("Введите текст: ")
lowercase_text = text.lower()
words = lowercase_text.split()
total_chars = len(lowercase_text)
vowels = set('аеуёияоюэюы')
consonants = set('бвгджзйклмнпрстфхцчшщ')
num_vowels = 0
num_consonants = 0
for word in words:
    for char in word:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            elif char in consonants:
                num_consonants += 1
longest_word = max(words, key=len)
word_count = len(words)
print(f'Количество слов: {word_count}')
print(f'Общее количество символов: {total_chars}')
print(f'Гласных букв: {num_vowels}')
print(f'Согласных букв: {num_consonants}')
print(f'Самое длинное слово: "{longest_word}"')