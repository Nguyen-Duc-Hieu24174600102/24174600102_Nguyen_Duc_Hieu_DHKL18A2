# # #Hàm đo độ dài kiểu dữ liệu tuần tự: len
# print(len(a))
# range(len(a)) #thu được chỉ mục chạy từ 0 đến len(a)-1 = 10

# for i in range(len(a)):
#     print(a[i])
    
# #tính chất của kiểu dữ liệu chuỗi ký tự:
# # - Có thể truy cập
# # - Không thể chỉnh sửa
# # - Không thể sắp xếp

# b = "Hello" + "world"
# print(b)

# n = int(input("nhap vao so nguyen duong: "))
# if n > 0:
#     print("Da nhap dung so nguyen duong")
    
# c = ""    
# for i in range(len(a)):
#     if a[i] == "a":
#         c = c + i

# for i in a:
#     print(i)


# #Các phương thức trong xử lý chuỗi ký tự
# a = "Hello world"
# #Các phương thức kiểm tra (trả về cho mình True hoặc False)
# #các phương thức này sẽ thường bắt đầu bằng chữ "is"

# # - kiểm tra chuỗi có phải alphanumeric (chỉ có ký tự số và chữ hay không)
# print(a.isalnum())
# # - kiểm tra chuỗi có toàn số hay không (numeric)
# print(a.isnumeric())
# # - kiểm tra chuỗi có toàn chữ hay không (character)
# print(a.isalpha())
# # - Kiểm tra chuỗi có nằm trong bảng mã ascii hay không
# print(a.isascii())
# # - Kiểm tra chuỗi có phải kiểu số hay không
# print(a.isdigit()) #Số thông thường
# print(a.isdecimal()) # số thập phân
# #- kiểm tra xem chuỗi có khoảng trống hay không
# print(a.isspace())
# #- kiểm tra in hoa in thường
# print(a.isupper())
# print(a.islower())

# #- kiểm tra ký tự tồn tại trong chuỗi
# print(a.find("llo"))
# print(a.count("l"))
# print(a.index("s"))


# #Phương thức biến đổi (các phương thức này trả về chuỗi ký tự mới, không thay đổi chuỗi ký tự ban đầu)
# a = "Hello world"
# #- Xóa ký tự đầu và cuối của chuỗi
# a_sua = a.strip()
# a_sua = a.lstrip()
# a_sua = a.rstrip()

# #- Thay thế ký tự bất kỳ
# a_sua = a.replace("l","w")

# # - biến đổi viết hoa viết thường
# a_sua = a.upper()
# a_sua = a.lower()
# a_sua = a.capitalize() 





# def f(qty,item,price):
#     print(f'{qty} {item} cost ${price:.2f}')

# f(6, 'banana', 1.74) 


# n=int(input("nhập số n"))
# for i in range(n+1):
#     if i==6:
#         print(i)
#         break
# else:
#     print("ko tìm thấy 6")
    



# open_file=open(file="file.txt", open="r")

# print(open_file.readline())


                                                                                                                

class Khoa:
    def __init__(self, ma_khoa, ten_khoa, truong_khoa):
        self.ma_khoa = ma_khoa
        self.ten_khoa = ten_khoa
        self.truong_khoa = truong_khoa

    def __str__(self):
        return f"{self.ma_khoa} - {self.ten_khoa} - Trưởng khoa: {self.truong_khoa}"


class PhongHoc:
    def __init__(self, ma_phong, ten_phong, so_cho_ngoi, tinh_trang, khoa_quan_ly):
        self.ma_phong = ma_phong
        self.ten_phong = ten_phong
        self.so_cho_ngoi = so_cho_ngoi
        self.tinh_trang = tinh_trang  # Ví dụ: 'Tốt', 'Xuống cấp'
        self.khoa_quan_ly = khoa_quan_ly

    def __str__(self):
        return f"{self.ma_phong} - {self.ten_phong} - {self.so_cho_ngoi} chỗ - Tình trạng: {self.tinh_trang} - Khoa quản lý: {self.khoa_quan_ly}"


class QuanLy:
    def __init__(self):
        self.ds_khoa = []
        self.ds_phong = []

    # Quản lý khoa
    def them_khoa(self, khoa):
        self.ds_khoa.append(khoa)

    def xoa_khoa(self, ma_khoa):
        self.ds_khoa = [khoa for khoa in self.ds_khoa if khoa.ma_khoa != ma_khoa]

    def hien_thi_khoa(self):
        print("\nDanh sách các khoa:")
        for khoa in self.ds_khoa:
            print(khoa)

    # Quản lý phòng học
    def them_phong(self, phong):
        self.ds_phong.append(phong)

    def xoa_phong(self, ma_phong):
        self.ds_phong = [phong for phong in self.ds_phong if phong.ma_phong != ma_phong]

    def hien_thi_phong(self):
        print("\nDanh sách phòng học:")
        for phong in self.ds_phong:
            print(phong)

    # Sắp xếp phòng học theo số chỗ ngồi
    def sap_xep_phong_theo_so_cho(self):
        self.ds_phong.sort(key=lambda x: x.so_cho_ngoi)
        self.hien_thi_phong()

    # Thống kê phòng học
    def thong_ke_phong_hoc(self):
        tong_phong = len(self.ds_phong)
        phong_tot = sum(1 for phong in self.ds_phong if phong.tinh_trang == "Tốt")
        phong_xuong_cap = tong_phong - phong_tot

        print("\nThống kê phòng học:")
        print(f"Tổng số phòng: {tong_phong}")
        print(f"Phòng tình trạng tốt: {phong_tot}")
        print(f"Phòng xuống cấp: {phong_xuong_cap}")

    # Tìm kiếm phòng theo mã khoa quản lý
    def tim_phong_theo_khoa(self, ma_khoa):
        print(f"\nDanh sách phòng thuộc khoa {ma_khoa}:")
        for phong in self.ds_phong:
            if phong.khoa_quan_ly == ma_khoa:
                print(phong)


# Chương trình chính
def main():
    ql = QuanLy()

    # Thêm khoa
    ql.them_khoa(Khoa("K01", "Công nghệ thông tin", "Nguyen Van A"))
    ql.them_khoa(Khoa("K02", "Khoa Toán", "Tran Van B"))
    ql.them_khoa(Khoa("K03", "Khoa Vật lý", "Le Thi C"))

    ql.hien_thi_khoa()

    # Thêm phòng học
    ql.them_phong(PhongHoc("P101", "Phòng học lý thuyết", 50, "Tốt", "K01"))
    ql.them_phong(PhongHoc("P102", "Phòng thí nghiệm", 30, "Xuống cấp", "K01"))
    ql.them_phong(PhongHoc("P201", "Phòng hội thảo", 100, "Tốt", "K02"))
    ql.them_phong(PhongHoc("P202", "Phòng máy tính", 40, "Tốt", "K03"))

    ql.hien_thi_phong()

    # Sắp xếp phòng học theo số chỗ ngồi
    print("\nDanh sách phòng học sau khi sắp xếp theo số chỗ ngồi:")
    ql.sap_xep_phong_theo_so_cho()

    # Thống kê phòng học
    ql.thong_ke_phong_hoc()

    # Tìm kiếm phòng học thuộc một khoa cụ thể
    ql.tim_phong_theo_khoa("K01")

    # Xóa phòng học
    print("\nXóa phòng P102:")
    ql.xoa_phong("P102")
    ql.hien_thi_phong()


if __name__ == "__main__":
    main()