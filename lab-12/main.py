import json
from os import path

#шлях до файлу json
PATH_TO_JSON_FILE = path.join(path.dirname(__file__), "data.json") 

#початкові дані
commands = {
    "Astralis":21,
    "NaVi":18,
    "FaZe": 16,
    "Liquid":14,
    "Monte":12,
    "Vitality": 10,
    "ENCE":8,
    "mousesports": 6,
    "fnatic":4,
}

#запис початкових даних до файлу
with open(PATH_TO_JSON_FILE, "wt") as jsonFile:
    json.dump(commands, jsonFile)
    jsonFile.close()

#допоміжна функція для додавання нових даних у словник
def add_command(commands, command_name, command_score):
    if command_name in commands:
        print(f"Command {command_name} is already in list.")
    else:
        commands[command_name] = command_score
        print(f"Command {command_name} was added.")


while True:
    print("Select an option:\n 1 - Add data\n 2 - View data\n 3 - Find place of new command\n 4 - Exit") 
    user_choice = int(input("Choose an option: "))

    if user_choice == 1:
        #зчитуємо дані з файлу
        with open(PATH_TO_JSON_FILE, "rt") as jsonFile:
            commands = json.load(jsonFile)
            jsonFile.close()
        
        #додаємо нові дані
        new_command_name = str(input("Input new command's name: "))
        new_command_score = int(input("Input new command's score: "))
        add_command(commands, new_command_name, new_command_score)
        
        #записуємо оновлені дані до файлу
        with open(PATH_TO_JSON_FILE, "wt") as jsonFile:
            json.dump(commands, jsonFile)


    elif user_choice == 2:
        with open(PATH_TO_JSON_FILE, "rt") as jsonFile:
            #зчитуємо дані з файлу
            jsonData = json.load(jsonFile)

            #друкуємо дані в консоль
            print(jsonData)

    elif user_choice == 3:

        #зчитуємо дані з файлу
        with open(PATH_TO_JSON_FILE, "rt") as jsonFile:
            commands = json.load(jsonFile)
            jsonFile.close()

        #введення даних користувачем
        new_command_name = str(input("Input new command's name: "))
        new_command_score = int(input("Input new command's score: "))
        
        #визначення місця нової команди та списку команд, які мають нижчу кількість очок 
        commands_with_less_scores = [command for command in commands if commands[command] < new_command_score]
        new_command_place = len(commands.keys()) - len(commands_with_less_scores) + 1

        #виведення результатів
        print(f"List of commands with fewer points than the {new_command_name}: ",commands_with_less_scores)
        print(f"Place of command {new_command_name}: ", new_command_place)
        
    elif user_choice == 4:
        #завершення роботи програми
        quit(0)
    else:
        print("This variant doesn't exist. Try again")    

    print()    