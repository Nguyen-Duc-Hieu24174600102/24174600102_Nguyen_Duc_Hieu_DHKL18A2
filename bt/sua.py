ds_so = []
while True:
    n = input("Nhập vào số phần tử n trong dãy A: ")
    if not n.isdigit():  
        try:
            n = int(n)  
            break
        except ValueError:
            print("Yêu cầu nhập lại số nguyên hợp lệ (có thể là số âm)!")
    else:
        n = int(n)
        break

for i in range(n):
    while True:
        so = input(f"Nhập giá trị số thứ {i + 1}: ")
        try:
            so = float(so)  
            break
        except ValueError:
            print("Yêu cầu nhập vào số thực hợp lệ!")
    ds_so.append(so)

tong = sum(ds_so)
print(f"Tổng các số vừa nhập: {tong}")