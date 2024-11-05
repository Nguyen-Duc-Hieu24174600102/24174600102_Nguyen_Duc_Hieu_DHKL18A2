choice = input("Chọn chế độ chuyển đổi (1: Hệ 10 sang hệ 2, 2: Hệ 2 sang hệ 10): ")

if choice == "1":
    # Chuyển đổi từ hệ 10 sang hệ 2
    decimal_number = int(input("Nhập số ở hệ cơ số 10: "))
    
    if decimal_number == 0:
        print("Số nhị phân tương ứng: 0")
    else:
        binary_number = ""
        while decimal_number > 0:
            remainder = decimal_number % 2
            binary_number = str(remainder) + binary_number
            decimal_number = decimal_number // 2
        print("Số nhị phân tương ứng:", binary_number)

elif choice == "2":
    # Chuyển đổi từ hệ 2 sang hệ 10
    binary_number = input("Nhập số ở hệ cơ số 2: ")
    decimal_number = 0
    power = 0
    
    for digit in binary_number[::-1]:
        decimal_number += int(digit) * (2 ** power)
        power += 1
    print("Số hệ 10 tương ứng:", decimal_number)

else:
    print("Lựa chọn không hợp lệ.")