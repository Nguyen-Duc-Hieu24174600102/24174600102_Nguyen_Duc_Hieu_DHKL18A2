#bài 7  Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải số thập phân hay không
nhap_vao_chuoi = input("nhap vao ky tu:")
if nhap_vao_chuoi.isdecimal() and  nhap_vao_chuoi.isdigit():    
             print(nhap_vao_chuoi.isdecimal())
             print("chuoi la so thap phan") #true
else:
         print(" chuoi la so thap phan")     #false                          
