# Nhập số nguyên dương n
n = int(input("Nhập một số nguyên dương n: "))


tong = 0

# Duyệt qua các số từ 1 đến n
for k in range(1, n + 1):
    # Tính căn bậc 7 của k
    tong += k ** (1/7)

# In kết quả
print(f"Tổng S từ k=1 đến {n} là: {tong:}")


