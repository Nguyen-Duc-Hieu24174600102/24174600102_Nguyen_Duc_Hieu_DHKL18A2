n = int(input("Nhập vào một số nguyên dương n: "))

print(f"Các số chính phương nhỏ hơn {n} là:", end=" ")
for i in range(1, n):
    if i * i < n:
        print(i * i, end=" ")
    else:
        break