lph = []

def nhap():
    for i in range(0, n):
        print(f'Nhập khoa thứ {i + 1}')
        maph = int(input('Nhập mã phòng: '))
        tenph = input('Nhập tên phòng: ')
        loaiph = input('Nhập loại phòng: ')
        vitri = input('Nhập vị trí khu nhà: ')
        vitritang= input('Nhập vị trí tầng: ')
        sdtql= int(input('Nhập sdt: '))
        makhoa= int(input('Nhập mã khoa: '))
        d = {"maph": maph, "tenph": tenph, "loaiph": loaiph, "vitri": vitri, "vitritang":vitritang,"sdtql":sdtql,"makhoa":makhoa }
        lph.append(d)

def delete():
    tk = int(input('Nhập mã phong cần xóa: '))
    for i in range(0, len(lph)):
        if lph[i].get("maph") == tk:
            lph.remove(lph[i])
            break
    else:
        print('Không có trong danh sách phòng.')

def sua():
    tk = int(input('Nhập mã phòng cần sửa: '))
    for i in range(0, len(lph)):
        if lph[i].get("maph") == tk:
            maph = int(input('Nhập mã phòng: '))
            tenph = input('Nhập tên phòng: ')
            loaiph = input('Nhập loại phòng: ')
            vitri = input('Nhập vị trí khu nhà: ')
            vitritang= input('Nhập vị trí tầng: ')
            sdtql= int(input('Nhập sdt: '))
            makhoa= int(input('Nhập mã khoa: '))
            d = {"maph": maph, "tenph": tenph, "loaiph": loaiph, "vitri": vitri, "vitritang":vitritang,"sdtql":sdtql,"makhoa":makhoa }
            lph.append(d)
            break
    else:
        print('Không có trong danh sách phòng.')

def add():
    print('Nhập thông tin phòngphòng cần thêm')
    maph = int(input('Nhập mã phòng: '))
    tenph = input('Nhập tên phòng: ')
    loaiph = input('Nhập loại phòng: ')
    vitri = input('Nhập vị trí khu nhà:')
    vitritang= input('Nhập vị trí tầng: ')
    sdtql= int(input('Nhập sdt: '))
    makhoa= int(input('Nhập mã khoa: '))
    d = {"maph": maph, "tenph": tenph, "loaiph": loaiph, "vitri": vitri, "vitritang":vitritang,"sdtql":sdtql,"makhoa":makhoa }
    lph.append(d)

def show():
    print(lph)

while True:
    print('''***************************
1. Nhập phòng
2. Thêm phòng
3. Xóa phòng
4. Sửa phòng
5. Xem danh sách
6. Thoát
***************************''')

    chon = int(input('Bạn hãy nhập lựa chọn: '))
    if chon == 1:
        n = int(input('Nhập số phòng: '))
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
        break
    else:
        print('Lựa chọn không hợp lệ.')

import csv

# Hàm đọc dữ liệu từ file CSV
def read_csv_file(filename, headers):
    data = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"File '{filename}' không tồn tại. Khởi tạo dữ liệu rỗng.")
        # Tạo file với header nếu file không tồn tại
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
    return data

# Hàm ghi dữ liệu vào file CSV
def write_csv_file(filename, headers, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

# Hàm kiểm tra và chuẩn hóa dữ liệu ds_khoa
def validate_ds_khoa(data):
    validated_data = []
    seen_keys = set()  # Kiểm tra khóa trùng lặp (Mã khoa)
    for row in data:
        ma_khoa = str(row.get("Ma khoa", "")).strip()[:10]
        ten_khoa = str(row.get("Ten khoa", "")).strip()[:2020]
        tong_so_phong=str(row.get("Tổng số phòng là : ", 0))
        if ma_khoa in seen_keys:
            print(f"Lỗi: Mã khoa '{ma_khoa}' bị trùng!")
            continue
        seen_keys.add(ma_khoa)

        validated_data.append([ma_khoa, ten_khoa, tong_so_phong])
    return validated_data

# ==== MAIN PROGRAM ====
# Khởi tạo các headers
ds_khoa_headers = ["Ma khoa", "Ten khoa","Tong so phong"]

# Đọc file CSV khi khởi động
ds_khoa_data = read_csv_file('ds_khoa.csv', ds_khoa_headers)

# Dữ liệu mẫu để thêm mới (nếu cần)
new_ds_khoa = [
    {"Ma khoa ": "P001", "Ten khoakhoa": "Phong hop", "Tong so phong":"1"},
    {"Ma phong": "P002", "Ten phong": "Phong may tinh", "Tong so phong":"2"}
]

# Chuẩn hóa và ghi lại dữ liệu vào file CSV
ds_khoa_validated = validate_ds_khoa(new_ds_khoa + ds_khoa_data)
write_csv_file('ds_khoa.csv', ds_khoa_headers, ds_khoa_validated)

print("Đã ghi lại dữ liệu phòng khoa vào file CSV!")