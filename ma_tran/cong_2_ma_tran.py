
matrix = [
    [1, 7, 9],  # Hàng 1
    [2, 5, 8],  # Hàng 2
    [6, 9, 18]  # Hàng 3
]

print("Ma trận ban đầu:")
for row in matrix:
    print(row)

matrix2 = [
    [1, 2, 3],  # Hàng 1
    [4, 5, 6],  # Hàng 2
    [7, 8, 9]   # Hàng 3
]

# Cộng hai ma trận
result = [[matrix[i][j] + matrix2[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
print("\nMa trận sau khi cộng với ma trận thứ hai:")
for row in result:
    print(row)

