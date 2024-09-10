
N = int(input("Введіть розмір масиву: "))

while N <= 0:
    print("Розмір масиву має бути більше нуля")
    N = int(input("Введіть розмір масиву: "))

list = []
for index in range(N):
    list.append(index if index < 2 else list[index-2]+list[index-1]) 

print(list)