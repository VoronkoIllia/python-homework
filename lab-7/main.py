def add_command(commands, command_name, command_score):
    commands[command_name] = command_score
    print(f"Додано {command_name}.")

def delete_command(commands, command_name):
    del commands[command_name]
    print(f"Видалено {command_name}.")

def print_commands(commands):
    for command in commands:
        print(f"Команда {command} - {commands[command]} очок")

def print_sort_commands(commands):
    sorted_commands = {key: commands[key] for key in sorted(commands)}

    print("Відсортований список команд:")
    for command in sorted_commands:
        print(f"Команда {command} - {sorted_commands[command]} очок")

def solve(commands):
    new_command_name = str(input("Введіть ім'я нової команди: "))
    new_command_score = int(input("Введіть кількість очок у нової команди: "))
  
    commands_with_less_scores = [command for command in commands if commands[command] < new_command_score]
    new_command_place = len(commands.keys()) - len(commands_with_less_scores) + 1

    print(f"Список команд з мeншою кількість очок, ніж у {new_command_name}: ",commands_with_less_scores)
    print(f"Місце, яке посіла команда {new_command_name}: ", new_command_place)

def get_user_answer():
    
    print("1. Вивести словник в консоль.")
    print("2. Додати нове значення в словник.")
    print("3. Видалити значення зі словника.")
    print("4. Переглянути вміст словника за відсортованими ключами.")
    print("5. Вивести місце нової команди та назви команд, які набрали менше очок, ніж ця команда.")
    print("0. Вийти з програми.")
    
    answer = int(input("Введіть варіант меню: "))
    return answer

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


while True:
    
    user_answer = get_user_answer()
    
    match user_answer:
        case 1:
            print_commands(commands)
        case 2:
            command_name = str(input("Введіть ім'я нової команди: "))
            command_score = int(input("Введіть кількість очок у нової команди: "))
            add_command(commands, command_name, command_score)
        case 3:
            command_name = str(input("Введіть ім'я команди, яку потрібно видалити: "))
            delete_command(commands, command_name)
        case 4:
            print_sort_commands(commands)
        case 5:
            solve(commands)            
        case 0:
            break
        case _:
            print("Такого варіанта немає. Спробуйте ще раз")
            
    input("Press Enter to continue...")
    print()