luong = float(input("Nhập lương nhân viên: "))

if luong > 15_000_000:
    thue = luong * 0.3
elif 7_000_000 <= luong <= 15_000_000:
    thue = luong * 0.2
else:
    thue = luong * 0.1

luong_rong = luong - thue
print(f"Thuế thu nhập: {thue} đồng, Lương ròng: {luong_rong} đồng")