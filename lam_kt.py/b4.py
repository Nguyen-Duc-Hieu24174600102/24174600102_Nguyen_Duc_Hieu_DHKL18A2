n = int(input("Nhập một số nguyên dương n: "))

# Tính tổng thứ nhất từ k=1 đến n+4 với biểu thức (k+1) / (2k-1)
sum1 = 0
for k in range(1, n + 5):  # k chạy từ 1 đến n+4
    sum1 += (k + 1) / (2 * k - 1)

# Tính tổng thứ hai từ k=2 đến n với biểu thức k
sum2 = 0
for k in range(2, n + 1):  # k chạy từ 2 đến n
    sum2 += k

# Tính tổng S và đổi dấu
S = -sum1 * sum2

# In kết quả
print(f"Tổng S = {S:}")