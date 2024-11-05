# Nhập tử số và mẫu số từ người dùng
numerator = int(input("Nhập tử số: "))
denominator = int(input("Nhập mẫu số: "))

# Kiểm tra nếu mẫu số bằng 0
if denominator == 0:
    print("Mẫu số không thể bằng 0.")
else:
    # Sử dụng vòng lặp để tìm ước chung lớn nhất (GCD) bằng phương pháp Euclid
    a, b = abs(numerator), abs(denominator)  # Lấy giá trị tuyệt đối để tránh số âm
    while b != 0:
        a, b = b, a % b  # Cập nhật a và b theo thuật toán Euclid

    gcd = a  # Sau khi kết thúc vòng lặp, a là GCD của tử số và mẫu số

    # Chia cả tử số và mẫu số cho GCD để tối giản phân số
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd

    # In kết quả
    print(f"Phân số tối giản là: {simplified_numerator}/{simplified_denominator}")