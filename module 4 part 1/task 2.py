text=input("Введите текст:")
reserved_words=input("Введите список зарезервированных слов через пробел:").split()
words=text.split()
for i in range(0,len(words)):
    if words[i] in reserved_words:
        words[i]=words[i].upper()
        modified_text=' '.join(words)
        print("Измененный текст",modified_text)

