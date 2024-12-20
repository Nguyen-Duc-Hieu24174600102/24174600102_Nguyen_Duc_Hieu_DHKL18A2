lct=[]

def nhap():
    for i in range(0, n):
        print(f'nhập cầu thủ thứ {i+1} ')
        mct=input('nhập mã cầu thủ')
        tct=input('nhập tên cầu thủ')
        tuoi=int(input('nhập số tuổi'))
        vitri=input('nhập vị trí')
        sohuychuong=int(input('nhập số huy chương'))
        thuong=float(input('nhập số tiền thưởng'))
        d={"mct":mct, "tct":tct, "tuoi":tuoi, "vitri":vitri, "sohuychuong":sohuychuong, "thuong":thuong}
        lct.append(d)
def delete():
    kt=input('nhập mã cầu thủ cần xóa')
    for i in range(0,len(lct)):
        if lct[i].get("mct")==kt:
            lct.remove(lct[i])
            break
    else:
        print('ko có trong danh sách ctct')
def sua():
    kt=input('nhập mã cầu thủ cần sửa')
    for i in range (0,len(lct)):
        if lct[i].get("mct")==kt:
            mct=input('nhập mã cầu thủ')
            tct=input('nhập tên cầu thủ')
            tuoi=int(input('nhập số tuổi'))
            vitri=input('nhập vị trí')
            sohuychuong=int(input('nhập số huy chương'))
            thuong=float(input('nhập số tiền thưởng'))
            d={"mct":mct, "tct":tct, "tuoi":tuoi, "vitri":vitri, "sohuychuong":sohuychuong, "thuong":thuong}
            lct.append(d)
            break
    else:
        print('ko có trong danh sách phòng')    
def add():
    print('nhập thông tin cầu thủ cần thêm')
    mct=input('nhập mã cầu thủ')
    tct=input('nhập tên cầu thủ')
    tuoi=int(input('nhập số tuổi'))
    vitri=input('nhập vị trí')
    sohuychuong=int(input('nhập số huy chương'))
    thuong=float(input('nhập số tiền thưởng'))
    d={"mct":mct, "tct":tct, "tuoi":tuoi, "vitri":vitri, "sohuychuong":sohuychuong, "thuong":thuong}
    lct.append(d)
def show():
    print('lct')
def tinh_thuong():
    try:
        for cau_thu in lct:
            so_huy_chuong = cau_thu["so_huy_chuong"]
            if so_huy_chuong > 10:
                cau_thu["thuong"] = so_huy_chuong * 500000
            elif 5 <= so_huy_chuong <= 10:
                cau_thu["thuong"] = so_huy_chuong * 300000
            else:
                cau_thu["thuong"] = so_huy_chuong * 200000
        print("Đã tính thưởng cho tất cả cầu thủ.")
    except Exception as e:
        print(f"Có lỗi xảy ra khi tính thưởng: {e}")
danh_sach_sap_xep = sorted(lct, key=lambda x: x['so_huy_chuong'])
        
print("\nDanh sách cầu thủ (Sắp xếp theo huy chương từ nhỏ đến lớn):")
for cau_thu in danh_sach_sap_xep:
        print(f"Mã: {cau_thu['ma']}, Tên: {cau_thu['ten']}, Tuổi: {cau_thu['tuoi']}, "
                  f"Vị trí: {cau_thu['vi_tri']}, Số huy chương: {cau_thu['so_huy_chuong']}, "
                  f"Thưởng: {cau_thu['thuong']}")

while True:
    print('''***************************
1. Nhập cầu thủ
2. Thêm cầu thủ
3. Xóa cầu thủ
4. Sửa cầu thủ
5. Xem danh sách
6. tính thưởng
7.thoát
***************************''')

    chon = int(input('Bạn hãy nhập lựa chọn: '))
    if chon == 1:
        n = int(input('Nhập số cầu thủ: '))
        nhap()
    elif chon == 2:
        add()
    elif chon == 3:
        delete()
    elif chon == 4:
        sua()
    elif chon == 5:
        show()
    elif chon == 6:
        tinh_thuong()
    elif chon==7:
        break
        
    else:
        print('Lựa chọn không hợp lệ.')







            

