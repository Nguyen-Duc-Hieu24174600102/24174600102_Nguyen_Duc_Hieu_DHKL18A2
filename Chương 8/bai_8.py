diem = input("Nhập điểm (A, B, C, D, E, F): ")

if diem == "A" or diem == "a":
    print("Sinh viên xuất sắc")
elif diem == "B" or diem == "b":
    print("Sinh viên giỏi")
elif diem == "C" or diem == "c":
    print("Sinh viên khá")
elif diem == "D" or diem == "d":
    print("Sinh viên trung bình")
elif diem == "E" or diem == "e":
    print("Sinh viên yếu")
elif diem == "F" or diem == "f":
    print("Sinh viên kém")
else:
    print("Điểm không hợp lệ")