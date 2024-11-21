
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[2, 0], [1, 3]]

result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
print("\nMa trận sau khi nhân ma trận 1 và ma trận 2:")
for row in result:
    print(row)