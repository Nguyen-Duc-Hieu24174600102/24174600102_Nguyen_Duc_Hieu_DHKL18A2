x = float(input("Nhập tọa độ x của điểm M: "))
y = float(input("Nhập tọa độ y của điểm M: "))
a = float(input("Nhập tọa độ a của tâm I: "))
b = float(input("Nhập tọa độ b của tâm I: "))
R = float(input("Nhập bán kính R của hình tròn: "))

khoang_cach = ((x - a) ** 2 + (y - b) ** 2) ** 0.5
if khoang_cach <= R:
    print(True)
else:
    print(False)