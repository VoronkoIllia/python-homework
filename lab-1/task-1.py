a = int(input("Введіть значення а: "))

while(a <= 0):
    print("Значення a повинно бути додатнім.")
    a = int(input("Введіть значення а: "))

b = int(input("Введіть значення b: "))

while(b <= 0):
    print("Значення b повинно бути додатнім.")
    b = int(input("Введіть значення b: "))


if a > b:
    result = a*b+1
elif a < b:
    result = (a-5)/b
else:
    result = 25

print(f'Результат: {result}')
