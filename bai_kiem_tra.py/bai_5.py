n = int(input("Nhập một số nguyên: "))
if n < 1:
    print(f"{n} không phải là số hoàn hảo.")
else:
    tong = 0  
    for i in range(1, n):
        if n % i == 0:  
            tong =tong + i
    if tong== n:
        print(f"{n} là số hoàn hảo.")
    else:
        print(f"{n} không phải là số hoàn hảo.")