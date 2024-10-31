loai_xe = int(input("Nhập loại xe (4 hoặc 7): "))
km = float(input("Nhập số km đã đi: "))
tg_cho = int(input("Nhập số phút chờ: "))

cuoc = 0
if loai_xe == 4:
    if km <= 0.8:
        cuoc = 11000
    elif km <= 20:
        cuoc = 11000 + (km - 0.8) * 12100
    else:
        cuoc = 11000 + 19.2 * 12100 + (km - 20) * 10000
elif loai_xe == 7:
    if km <= 0.8:
        cuoc = 13000
    elif km <= 30:
        cuoc = 13000 + (km - 0.8) * 14100
    else:
        cuoc = 13000 + 29.2 * 14100 + (km - 30) * 12000

cuoc += max(0, tg_cho - 5) * 800
print(f"Cước taxi: {cuoc} đồng")