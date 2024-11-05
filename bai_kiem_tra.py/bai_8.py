n = int(input("Nhập vào một số nguyên dương n: "))
print(f"Các số hoàn hảo nhỏ hơn {n} là:", end=" ")
for n in range(2, n):
    s = 0  
    for i in range(1, n):
        if n % i == 0:  
            s = s + i  
    if s == n:
        print(n, end=" ")