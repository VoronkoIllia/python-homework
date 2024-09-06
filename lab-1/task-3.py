n = int(input("Введіть число N: "))

while(n<=1 or n>=9):
    print("Значення N має бути більше 1 та менше 9.")
    n = int(input("Введіть число N: "))

for i in range(n,0,-1):
    for j in range(i, n+i):
        if j <= n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print("")