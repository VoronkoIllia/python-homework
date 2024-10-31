from matplotlib import pyplot as plt
from os import path  
import numpy as np
import csv



CURRENT_DIR = path.dirname(__file__)

# функція, що отримує дані з файла data.csv та перетворює їх у словник 
def get_data_from_csv(file_name):
    try:
        csv_file = open(path.join(CURRENT_DIR, file_name), "r")
    except:
        print(f"Файл {file_name} не знайдено")
        return None
    else:
        csv_file_reader = csv.DictReader(csv_file, delimiter=";")
        csv_file_data = {}

        for row in csv_file_reader:
            csv_file_data[row["Country Name"]] = float(row["2019 [YR2019]"].replace(",","."))
        return csv_file_data

data = get_data_from_csv("input.csv")

# якщо файла не існує, завершуємо роботу програми
if data == None:
    exit(0)

labels = [country for country in data]
values = [data[country] for country in data]
plt.title("GDP per capita (current US$)")
plt.pie(values, labels = labels, autopct = "%.1f%%")
plt.legend()
plt.axis("equal")
plt.show()