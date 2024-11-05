# tam giác pascal
def pascal_triangle(n):
    for i in range(n):
        # In khoảng trống để căn giữa tam giác
        print(" " * (n - i), end="")

        # Khởi tạo giá trị đầu tiên của mỗi hàng
        val = 1
        for j in range(i + 1):
            print(val, end=" ")

            # Tính giá trị tiếp theo trong hàng dựa vào công thức C(i, j+1) = C(i, j) * (i - j) / (j + 1)
            val = val * (i - j) // (j + 1)
        
        print()  # Xuống dòng sau mỗi hàng

# Nhập số hàng
rows = int(input("Nhập số hàng cho Tam giác Pascal: "))
pascal_triangle(rows)

#tam giác floyd
def floyd_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()  # Xuống dòng sau mỗi hàng

# Nhập số hàng
rows = int(input("Nhập số hàng cho Tam giác Floyd: "))
floyd_triangle(rows)