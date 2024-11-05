# Nhập số từ người dùng
num = int(input("Nhập một số: "))

# Kiểm tra nếu số nhập vào nhỏ hơn 2
if num < 2:
    print("Số phải lớn hơn hoặc bằng 2.")
else:
    # Tìm các thừa số nguyên tố
    factors = []
    divisor = 2  # Bắt đầu với thừa số nhỏ nhất là 2
    
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1
    
    # In các thừa số nguyên tố
    print("Thừa số nguyên tố là:", factors)