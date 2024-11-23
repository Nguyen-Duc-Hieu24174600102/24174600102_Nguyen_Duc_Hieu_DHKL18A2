 

#bài 6  Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải là số âm hay không
nhap_vao_chuoi = input("nhap vao ky tu:")
if nhap_vao_chuoi.startswith('-') and chuoi_nhap[1:].isdigit():
    print(" chuoi la so am")
else:
    print(" chuoi khong phai so am")