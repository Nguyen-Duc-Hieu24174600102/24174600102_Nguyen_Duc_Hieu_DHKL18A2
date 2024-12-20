def nhap(khoa_list):
   
    maph = int(input('Nhập mã phòng: ')).strip()
    tenph = input('Nhập tên phòng: ').strip()
    loaiph = input('Nhập loại phòng: ').strip()
    vitri = input('Nhập vị trí khu nhà: ').strip()
    vitritang= input('Nhập vị trí tầng: ').strip()
    sdtql= int(input('Nhập sdt: ')).strip()
    makhoa= int(input('Nhập mã khoa: ')).strip()
    new_khoa={
        "maph":maph,
        "tenph":tenph,
        "loaiph":loaiph,
        "vitri":vitri,
        "vitritang":vitritang,
        "sdtql":sdtql,
        "makhoa":makhoa 
    }
    khoa_list.append(new_khoa)
    print(f"khoa{makhoa} đã được thêm thành công")
    return khoa_list 

    