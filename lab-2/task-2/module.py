from random import randint


def play_in_guesser():
    random_value = randint(1, 100)
    print("\n\t\t\tГра \"Вгадай число\"")
    while(True):
        user_number = int(input("Введіть число від 1 до 100: "))
        if user_number > random_value:
            print("Моє число менше")
        elif user_number < random_value:
            print("Моє число більше")
        else:
            print("Ви вгадали")
            return