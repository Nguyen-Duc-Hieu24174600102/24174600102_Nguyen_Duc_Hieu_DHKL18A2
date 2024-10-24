import math
x = float(input("Nhập vào giá trị x: "))
if x <= 0:
    print("Giá trị x phải lớn hơn 0.")
else:
    log4_x = math.log(x, 4) 
    logx_2 = math.log(2, x) 
    tong = log4_x + logx_2

    print(f"Kết quả: {tong:.2f}")