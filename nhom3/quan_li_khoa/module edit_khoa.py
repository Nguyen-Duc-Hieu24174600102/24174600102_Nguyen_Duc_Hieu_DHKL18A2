

def edit_khoa(khoa_list):
    makhoa = input('Nhập mã khoa cần sửa: ').strip()
    for khoa in khoa_list:
        if khoa["makhoa"] == makhoa:
            print("Nhập thông tin mới cho khoa:")
             maph = int(input('Nhập mã phòng: ')).strip()
             tenph = input('Nhập tên phòng: ').strip()
             loaiph = input('Nhập loại phòng: ').strip()
             vitri = input('Nhập vị trí khu nhà: ').strip()
             vitritang= input('Nhập vị trí tầng: ').strip()
             sdtql= int(input('Nhập sdt: ')).strip()
             makhoa= int(input('Nhập mã khoa: ')).strip()

            "maph":maph,
            "tenph":tenph,
            "loaiph":loaiph,
            "vitri":vitri,
            "vitritang":vitritang,
            "sdtql":sdtql,
            "makhoa":makhoa 
            print(f"Khoa {makhoa} đã được sửa thành công.")
            return khoa_list
    print('Không tìm thấy mã khoa.')
    return khoa_list