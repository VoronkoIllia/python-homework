from math import sqrt
from random import randint


def calculate_expression(m,n):
    z = (sqrt(2) - sqrt(3*n)) / (2*m)
    return z

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


m = float(input("Введіть значення числа m: "))
while(m==0):
    print("Число m має НЕ ДОРІВНЮВАТИ нулю.")
    m = float(input("Введіть значення числа m: "))

n = float(input("Введіть значення числа n: "))
while(n<0):
    print("Число n має бути невід'ємним.")
    n = float(input("Введіть значення числа n: "))

result_of_expression = calculate_expression(m,n)
print(f'Результат виразу: {result_of_expression}')

play_in_guesser()