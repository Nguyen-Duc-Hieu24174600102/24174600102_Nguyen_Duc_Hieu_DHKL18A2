import csv
import sys
from datetime import datetime

# Danh sách lưu trữ phòng
lph = []
filename = 'ds_phong_khoa.csv'
headers = ["maph", "tenph", "loaiph", "vitri", "vitritang", "sdtql", "makhoa"]

# Đọc dữ liệu từ file CSV khi khởi động chương trình
def read_csv_file():
    data = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({
                    "maph": row["maph"],
                    "tenph": row["tenph"],
                    "loaiph": int(row["loaiph"]),
                    "vitri": row["vitri"],
                    "vitritang": int(row["vitritang"]),
                    "sdtql": int(row["sdtql"]),
                    "makhoa": row["makhoa"]
                })
    except (FileNotFoundError, KeyError):
        print(f"File '{filename}' không tồn tại hoặc lỗi định dạng. Tạo file mới.")
        write_csv_file([])
    return data

# Ghi dữ liệu vào file CSV
def write_csv_file(data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

# Hàm nhập phòng
def nhap():
    n = int(input('Nhập số phòng: '))
    for i in range(n):
        print(f'Nhập thông tin phòng thứ {i + 1}:')
        maph = input('Nhập mã phòng (string): ').strip()
        tenph = input('Nhập tên phòng: ').strip()
        loaiph = int(input('Nhập loại phòng (số nguyên): '))
        vitri = input('Nhập vị trí khu nhà: ').strip()
        vitritang = int(input('Nhập vị trí tầng (số nguyên): '))
        sdtql = int(input('Nhập số điện thoại quản lý (số nguyên): '))
        makhoa = input('Nhập mã khoa: ').strip()

        d = {"maph": maph, "tenph": tenph, "loaiph": loaiph, "vitri": vitri,
             "vitritang": vitritang, "sdtql": sdtql, "makhoa": makhoa}
        lph.append(d)
    write_csv_file(lph)
    print("Dữ liệu đã được cập nhật vào file CSV.")

# Hàm xóa phòng
def delete():
    tk = input('Nhập mã phòng cần xóa: ').strip()
    for i, phong in enumerate(lph):
        if phong["maph"] == tk:
            lph.pop(i)
            write_csv_file(lph)
            print(f"Phòng {tk} đã được xóa và cập nhật vào file CSV.")
            return
    print('Không tìm thấy mã phòng.')

# Hàm sửa phòng
def sua():
    tk = input('Nhập mã phòng cần sửa: ').strip()
    for i, phong in enumerate(lph):
        if phong["maph"] == tk:
            print("Nhập thông tin mới cho phòng:")
            maph = input('Nhập mã phòng: ').strip()
            tenph = input('Nhập tên phòng: ').strip()
            loaiph = int(input('Nhập loại phòng (số nguyên): '))
            vitri = input('Nhập vị trí khu nhà: ').strip()
            vitritang = int(input('Nhập vị trí tầng (số nguyên): '))
            sdtql = int(input('Nhập số điện thoại quản lý (số nguyên): '))
            makhoa = input('Nhập mã khoa: ').strip()

            lph[i] = {"maph": maph, "tenph": tenph, "loaiph": loaiph, "vitri": vitri,
                      "vitritang": vitritang, "sdtql": sdtql, "makhoa": makhoa}
            write_csv_file(lph)
            print(f"Phòng {tk} đã được sửa và cập nhật vào file CSV.")
            return
    print('Không tìm thấy mã phòng.')

# Hàm thêm phòng
def add():
    print('Nhập thông tin phòng cần thêm:')
    maph = input('Nhập mã phòng: ').strip()
    tenph = input('Nhập tên phòng: ').strip()
    loaiph = int(input('Nhập loại phòng (số nguyên): '))
    vitri = input('Nhập vị trí khu nhà: ').strip()
    vitritang = int(input('Nhập vị trí tầng (số nguyên): '))
    sdtql = int(input('Nhập số điện thoại quản lý (số nguyên): '))
    makhoa = input('Nhập mã khoa: ').strip()

    d = {"maph": maph, "tenph": tenph, "loaiph": loaiph, "vitri": vitri,
         "vitritang": vitritang, "sdtql": sdtql, "makhoa": makhoa}
    lph.append(d)
    write_csv_file(lph)
    print(f"Phòng {maph} đã được thêm và cập nhật vào file CSV.")

# Hàm hiển thị danh sách phòng
def show():
    if not lph:
        print("Danh sách phòng trống.")
        return
    print(f"\n{'Mã phòng':<10} {'Tên phòng':<15} {'Loại':<5} {'Vị trí':<10} {'Tầng':<5} {'SDT':<10} {'Mã khoa':<10}")
    for phong in lph:
        print(f"{phong['maph']:<10} {phong['tenph']:<15} {phong['loaiph']:<5} {phong['vitri']:<10} {phong['vitritang']:<5} {phong['sdtql']:<10} {phong['makhoa']:<10}")

# Chương trình chính
def main():
    global lph
    lph = read_csv_file()  # Đọc dữ liệu từ file khi khởi động
    while True:
        print('''\n***************************
1. Nhập phòng
2. Thêm phòng
3. Xóa phòng
4. Sửa phòng
5. Xem danh sách
6. Thoát
*************************''')

        chon = input('Bạn hãy nhập lựa chọn: ').strip()
        if chon == '1':
            nhap()
        elif chon == '2':
            add()
        elif chon == '3':
            delete()
        elif chon == '4':
            sua()
        elif chon == '5':
            show()
        elif chon == '6':
            print("Thoát chương trình. Dữ liệu đã được lưu.")
            sys.exit()
        else:
            print('Lựa chọn không hợp lệ.')

if __name__ == "__main__":
    main()