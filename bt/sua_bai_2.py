ds_so = []
while True:
    n = input("Nhập vào số phần tử n trong dãy A: ")
    if n.lstrip('-').isdigit():  
        n = int(n)
        break
    else:
        print("Yêu cầu nhập lại số nguyên hợp lệ!")

for i in range(n):
    while True:
        so = input(f"Nhập giá trị số thứ {i + 1}: ")
        if so.replace('.', '', 1).lstrip('-').isdigit():  
            so = float(so)
            break
        else:
            print("Yêu cầu nhập vào số thực hợp lệ!")
    ds_so.append(so)
tong = sum(ds_so)
print(f"Tổng các số vừa nhập: {tong}")