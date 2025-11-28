import re
def count_text_stats(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    sentences = list(filter(None, sentences))
    words = re.findall(r'\b\w+\b', text)
    punctuation_marks = len(re.findall(r'[.,!?:;\'-()]', text))

    return {
        'предложений': len(sentences),
        'слов': len(words),
        'знаков препинания': punctuation_marks
    }
input_text = input("Введите текст: ")
result = count_text_stats(input_text)
print(
    f"В тексте {result['предложений']} предложений, {result['слов']} слов и {result['знаков препинания']} знаков препинания.")