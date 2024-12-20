

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