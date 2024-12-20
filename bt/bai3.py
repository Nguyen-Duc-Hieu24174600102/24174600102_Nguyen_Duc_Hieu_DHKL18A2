
n = input("Nhập vào số nguyên dương n: ")


while not n.isdigit() or int(n) <= 0:
    n = input("Vui lòng nhập vào một số nguyên dương hợp lệ: ")


n = int(n)
A = []  
B = [] 
for i in range(n):
    if i % 2 == 0:
        B.append(i)  
    else:
        A.append(i)  

print("Danh sách A (số lẻ nhỏ hơn n):", A)
print("Danh sách B (số chẵn nhỏ hơn n):", B)