
#bài 2  # Bài 2: Viết chương trình nhập vào chuỗi ký tự, trả về chuỗi ký tự sau khi loại bỏ tất cả các dấu cách thừa
# Nhập chuỗi từ người dùng
chuoi_nhap_vao = input("nhap vao chuoi ky tu:")
tach_chuoi=chuoi_nhap_vao.split() 
chuoi_ket_qua = " ".join(tach_chuoi) 
print(f"chuoi ket qua: {chuoi_ket_qua}")  


