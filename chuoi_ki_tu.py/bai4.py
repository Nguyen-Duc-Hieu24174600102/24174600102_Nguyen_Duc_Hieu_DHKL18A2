

#bài 4  Viết chương trình nhập vào chuỗi ký tự, trả về kết quả đếm số ký tự là chữ, số ký tự là số và số ký tự là ký tự đặc biệt (Không là số, không là chữ) trong chuỗi
#yêu cầu (số ký tự là chữ,số kỷ tự là số and số đặc biệt)
# Nhập chuỗi từ người dùng
chuoi_nhap = input("Nhap vao chuoi ky tu: ")

chu_so = 0
chu_cai = 0
ky_tu_dac_biet = 0

for chu in chuoi_nhap:
    if chu.isdigit():
        chu_so =chu_so + 1
    elif chu.isalpha():
        chu_cai =  chu_cai + 1
    else:
        ky_tu_dac_biet =ky_tu_dac_biet + 1

print(f"So ky tu la chu: {chu_cai}")
print(f"So ky tu la so: {chu_so}")
print(f"So ky tu dac biet: {ky_tu_dac_biet}")

