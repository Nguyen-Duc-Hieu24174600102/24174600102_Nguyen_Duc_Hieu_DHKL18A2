    
#bài 8  Viết chương trình nhập vào 2 xâu ký tự str_1 và str_2. Kiểm tra xem str_2 có nằm trong str_1 hay không và ngược lại
# Nhập vào 2 chuỗi ký tự
str_1 = input("Nhap vao chuoi str_1: ")
str_2 = input("Nhap vao chuoi str_2: ")

# Kiểm tra xem str_2 có nằm trong str_1
found_in_str_1 = False
for i in range(len(str_1) - len(str_2) + 1):  # Lặp qua từng vị trí của str_1
    # Kiểm tra phần con của str_1 có giống str_2 không
    if str_1[i:i + len(str_2)] == str_2:
        found_in_str_1 = True# Nếu có, gán thành True và thoát vòng lặp
        break

if found_in_str_1:
    print(f"'{str_2}' nam trong '{str_1}'")
else:
    print(f"'{str_2}' khong nam trong '{str_1}'")

# Kiểm tra xem str_1 có nằm trong str_2
found_in_str_2 = False
for i in range(len(str_2) - len(str_1) + 1):  # Lặp qua từng vị trí của str_2
    # Kiểm tra phần con của str_2 có giống str_1 không
    if str_2[i:i + len(str_1)] == str_1:
        found_in_str_2 = True  # Nếu có, gán thành True và thoát vòng lặp
        break

if found_in_str_2:
    print(f"'{str_1}' nam trong '{str_2}'")
else:
    print(f"'{str_1}' khong nam trong '{str_2}'")



