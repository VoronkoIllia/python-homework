N = int(input("Введіть число n: "))

while N < 0:
    print("Число n має бути невід'ємним")
    N = int(input("Введіть розмір масиву: "))


array = []
for index in range(N):
    array.append(array[index-2] + array[index-1] if index > 1 else 1) 

print(array)