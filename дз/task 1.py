def clean_text(text, banned_words):
    words = text.split()
    cleaned_words = []
    for word in words:
        if word.lower() in banned_words:
            cleaned_word = '***'
        else:
            cleaned_word = word
        cleaned_words.append(cleaned_word)
    return ' '.join(cleaned_words)
input_text = input("Введите текст: ")
banned_list = input("Введите список запрещенных слов через запятую: ").lower().split(',')

cleaned_result = clean_text(input_text, banned_list)
print(f'Очищенный текст:\n{cleaned_result}')