t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
if t > 0:
    U = 220  # Vôn
    I = 2.7  # Ampe
    W = U * I * t  
    kWh = W / (3.6 * 10**6)
    tien_dien = kWh * 7000
    print(f"Năng lượng tiêu thụ: {kWh:.2f} kWh")
    print(f"Số tiền điện phải trả: {tien_dien:.2f} đồng")
else:
    print("Thời gian sử dụng phải lớn hơn 0!")