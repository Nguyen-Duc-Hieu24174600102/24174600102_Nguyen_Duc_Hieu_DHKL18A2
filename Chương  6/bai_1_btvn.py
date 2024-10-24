pi = 3.14
r = float(input("Nhập bán kính của khối trụ: "))
h = float(input("Nhập chiều cao của khối trụ: "))
if r > 0 and h > 0:
    Sxq = 2 * pi * r * h
    Stp = 2 * pi * r * (r + h)
    V = pi * r**2 * h
    print(f"Diện tích xung quanh: {Sxq:.2f}")
    print(f"Diện tích toàn phần: {Stp:.2f}")
    print(f"Thể tích: {V:.2f}")
else:
    print("Chiều cao và bán kính nhập sai")