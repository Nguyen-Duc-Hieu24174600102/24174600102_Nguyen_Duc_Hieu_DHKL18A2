diem_chuyen_can = float(input("Nhập điểm chuyên cần: "))
diem_giua_ky = float(input("Nhập điểm giữa kỳ: "))
diem_cuoi_ky = float(input("Nhập điểm cuối kỳ: "))
diem_trung_binh = (diem_chuyen_can * 0.2) + (diem_giua_ky * 0.3) + (diem_cuoi_ky * 0.5)
if diem_trung_binh >= 9:
    loai_diem = "A"
elif diem_trung_binh >= 7:
    loai_diem = "B"
elif diem_trung_binh >= 5:
    loai_diem = "C"
else:
    loai_diem = "D"
diem_trung_binh_hienthi=f"{diem_trung_binh: .2f}"
print(f"Điểm trung bình của sinh viên là:, {diem_trung_binh_hienthi}")
print("Xếp loại:", loai_diem)