
countOfNumbers = 0

for number in range(30, 61):
    if number%3 == 0:
        print(f'{number} ')
        countOfNumbers += 1

print(f'Кількість чисел, кратних 3, у діапазоні [30, 60]: {countOfNumbers}')