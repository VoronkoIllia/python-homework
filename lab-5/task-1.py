
N = int(input("Введіть розмір масиву: "))

while N <= 0:
    print("Розмір масиву має бути більше нуля")
    N = int(input("Введіть розмір масиву: "))


array = []
for index in range(N):
    array.append(index if index < 2 else array[index-2]+array[index-1]) 

print(array)