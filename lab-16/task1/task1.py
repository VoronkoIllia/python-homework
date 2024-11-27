from nltk import sent_tokenize,  word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from collections import Counter 
from os import path

try:

    File = open(path.join(path.dirname(__file__),'austen-emma.txt'), 'r', encoding='utf-8')

except FileNotFoundError:

    print("Файл не знайдено!")

    exit(0)

text = File.read()

def count_words(text):

    sentences = sent_tokenize(text,"english")

    words_count = 0

    for sentence in sentences:

        words = word_tokenize(sentence)

        words_count += len(words)

    return words_count

def most_used_words(text):

    text_words = text.split() #cписок зі словами

    cnt = Counter(text_words) #підрахунок слів

    cort1 = cnt.most_common(10)

    x1 = [cort1[el][0] for el in range(len(cort1))] #слова

    y1 = [cort1[el][1] for el in range(len(cort1))] #к-ть повторень у тексті

    stop_words = set(stopwords.words('english')) #отримуємо стоп-слова
    text_without_stopwords = [word for word in text_words if word not in stop_words] #cписок слів без стоп-слів

    cnt1 = Counter(text_without_stopwords) #підрахунок слів (стоп-слова не включаються)

    cort2 = cnt1.most_common(10)

    x2 = [cort2[el][0] for el in range(len(cort2))] #слова

    y2 = [cort2[el][1] for el in range(len(cort2))] #к-ть повторень у тексті

    fig, axs = plt.subplots(1, 2)

    fig.suptitle('Найбільш вживані слова у тексті')
    axs[0].set_title("Із стоп-словами")
    axs[0].bar(x1, y1)
    axs[1].set_title("Без стоп-слів")
    axs[1].bar(x2, y2)
    
    plt.show()

print("Кількість слів: ", count_words(text))
most_used_words(text)