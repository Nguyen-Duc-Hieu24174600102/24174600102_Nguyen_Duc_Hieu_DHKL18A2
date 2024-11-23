# Nhập chuỗi từ người dùng
chuoi_nhap = input("Nhập vào một chuỗi ký tự: ")

# Lấy các chữ số trong chuỗi
chu_so = ''.join([ky_tu for ky_tu in chuoi_nhap if ky_tu.isdigit()])

# Lấy các ký tự không phải là số
chu_khac = ''.join([ky_tu for ky_tu in chuoi_nhap if not ky_tu.isdigit()])

# Kết quả cuối cùng
ket_qua = chu_so + chu_khac

# In chuỗi kết quả
print("Chuỗi sau khi dồn số sang trái:", ket_qua)