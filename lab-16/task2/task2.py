from os import path
from nltk import word_tokenize
from nltk import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

CURRENT_DIR = path.dirname(__file__)

try:
    input_file = open(path.join(CURRENT_DIR, "input.txt"), "r")
except FileNotFoundError:
    print("Файл input.txt не знайдено")
    exit(0)


stop_words = set(stopwords.words("english"))
tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

text = input_file.read()
text_words = word_tokenize(text) #токенізація по словам
text_without_stopwords = [word for word in text_words if word not in stop_words] #видалення стоп-слів
lemmed_words = [lemmatizer.lemmatize(word) for word in text_without_stopwords] #лемматизація
stemmed_words = [stemmer.stem(word) for word in lemmed_words] #стемінг
stemmed_text = " ".join(stemmed_words)
tokens_without_punctuation = tokenizer.tokenize(stemmed_text) # видалення пунктуації
result_text_without_punctuation = " ".join(tokens_without_punctuation)

with open(path.join(CURRENT_DIR,"output.txt"),"w") as output_file:
    output_file.write(result_text_without_punctuation)