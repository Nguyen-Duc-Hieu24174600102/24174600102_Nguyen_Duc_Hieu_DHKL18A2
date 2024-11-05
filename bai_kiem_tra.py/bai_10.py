a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))


while b != 0:
    a, b = b, a % b
print(f"Ước chung lớn nhất của hai số là: {a}")