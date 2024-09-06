sentence = str(input("Введіть речення: "))

sentence_words = sentence.strip().split(" ")

tmp = sentence_words[0]
sentence_words[0] = sentence_words[-1]
sentence_words[-1] = tmp

print("Після зміни місцями першого і останнього слова:"," ".join(sentence_words))