from matplotlib import pyplot as plt
from os import path
import csv
import numpy as np


CURRENT_DIR = path.dirname(__file__)
years = [str(2000 + i) for i in range(17)]

# функція, що отримує дані з файла data.csv та перетворює їх у словник 
def get_data_from_csv(file_name):
    try:
        csv_file = open(path.join(CURRENT_DIR, file_name), "r")
    except:
        print(f"Файл {file_name} не знайдено")
    else:
        csv_file_reader = csv.DictReader(csv_file, delimiter=";")
        csv_file_data = {}

        for row in csv_file_reader:
            csv_file_data[row["Country Name"]] = [ int(row[year]) for year in years]
        return csv_file_data

# функція, яка будує графіки на основі даних двох країн
def draw_graphic_of_two_countries():

    data = get_data_from_csv("data.csv")

    if data != None:
        np.array(years)

        for country in data:
            np.array(data[country])
            plt.plot(years, data[country], label = country)

        plt.title("Population, total")
        plt.xlabel("Year", fontsize="12", color="red")
        plt.ylabel("Indicator", fontsize="12", color="red")
        plt.grid(True)
        plt.show()

# функція, яка будує стовпчасту діаграму на основі даних про країну
def draw_diagram_about_country(country_name):

    data = get_data_from_csv("data.csv")

    if data != None:
        np.array(data[country_name])

        plt.bar(years, data[country_name])
        plt.title("Population, total")
        plt.xlabel("Year", color="red", fontsize="12")
        plt.ylabel("Indicator", color="red", fontsize="12")
        plt.show()


while True: 
    
    print("1. Show dynamics of the population index in Kuwait and Kazakhstan")
    print("2. Show dynamics of the population index in entered country")
    print("0. Exit")

    variant = int(input("Input variant: "))

    if variant == 1:
        draw_graphic_of_two_countries()
    elif variant == 2:
        country_name = str(input("Input name of country: "))
        draw_diagram_about_country(country_name)
    elif variant == 0:
        exit(0)
    else:
        print("This variant doesn't exist. Try again")

    print()
