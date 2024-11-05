import math

x = float(input("Nhập giá trị x: "))
if x**2 + 4 >= 0 and x**4 + 1 > 0:
    numerator = -x + math.sqrt(x**2 + 4)
    denominator = (x**4 + 1)**(1/7)
    f_x = numerator / denominator
    print(f"Giá trị của f(x) là: {f_x:.2f}")
else:
    print("Biểu thức không xác định được với giá trị x đã nhập.")
                