pi = 3.14
r = float(input("Nhập bán kính của khối trụ: "))
h = float(input("Nhập chiều cao của khối trụ: "))
dien_tich_xung_quanh = 2 * pi * r * h
dien_tich_day = pi * r ** 2
dien_tich_toan_phan = dien_tich_xung_quanh + 2 * dien_tich_day
the_tich = pi * r ** 2 * h
print(f"Diện tích xung quanh: {round(dien_tich_xung_quanh, 2)}")
print(f"Diện tích toàn phần: {round(dien_tich_toan_phan, 2)}")
print(f"Thể tích khối trụ: {round(the_tich, 2)}")
