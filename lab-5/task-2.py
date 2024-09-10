n = 7

matrix = [[index if index<=7 else 0 for index in range(i,n+i)] for i in range(1,n+1)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print("")