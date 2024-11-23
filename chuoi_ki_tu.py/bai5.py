
#bài 5 Viết chương trình nhập vào chuỗi ký tự, đếm xem có bao nhiêu chữ cái viết hoa, bao nhiêu chữ cái viết thường
nhap_vao_chuoi = input("nhap vao chuoi ky tu")
viet_hoa=0
viet_thuong=0
for chu in chuoi_nhap:
    if chu.isupper():# isupper kiểm tra chữ hoa
       viet_hoa=viet_hoa+1
    elif chu.islower():#islower kiểm tra chữ cái in thường
        viet_thuong=viet_thuong+1
print(f"chu cai in hoa: {viet_hoa}")  
print(f"chu cai in thuong: {viet_thuong}")   

