
matrix = [
    [1, 7, 9],  # Hàng 1
    [2, 5, 8],  # Hàng 2
    [6, 9, 18]  # Hàng 3
]

print("Ma trận ban đầu:")
for row in matrix:
    print(row)

# Nhân ma trận với một số
k = 4
result = [[element * k for element in row] for row in matrix]
print("\nMa trận sau khi nhân với số", k, ":")
for row in result:
    print(row)

