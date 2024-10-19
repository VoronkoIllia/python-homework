import csv
import os


CURRENT_DIR = os.path.dirname(__file__)

def Open(file_name, mode):
    
    
    file_path = os.path.join(CURRENT_DIR,file_name)
    
    try:
        file = open(file_path, mode)
    except:
        print(f"Файл {file_name} не знайдено!")
        return None
    else:
        return file


#Виведення в консоль вмісту вхідного файла
input_csv = Open("input.csv", "r")

if input_csv != None:
    input_csv_reader = csv.DictReader(input_csv, delimiter=";")
    print("Country Name : 2019 [YR2019]")
    for row in input_csv_reader:
        print(f'{row["Country Name"]} : {row["2019 [YR2019]"]}')
    input_csv.close()


#Пошук по назвам країн, які введе користувач
input_csv = Open("input.csv", "r")
if input_csv != None:
    does_search_countries_exist = False
    
    input_csv_reader = csv.DictReader(input_csv, delimiter=";")
    user_input = input("Введіть через кому назви країн, дані яких вас цікавлять (Зразок: Ukraine, Poland): ")
    
    country_names = user_input.split(", ")
    
    os.system('cls') # використовую "cls" тому, що в мене Windows
    
    for row in input_csv_reader:
        if row["Country Name"] in country_names:

            does_search_countries_exist = True

            print(f'{row["Country Name"]} : {row["2019 [YR2019]"]}')

            with open(os.path.join(CURRENT_DIR,"output.csv"), "a") as output_csv:
                output_csv_writer = csv.writer(output_csv, delimiter=";", lineterminator="\n")
                output_csv_writer.writerow((row["Country Name"], row["2019 [YR2019]"]))
    
    input_csv.close()

    if not does_search_countries_exist:
        os.system('cls')
        print("Введені країни відсутні в файлі")