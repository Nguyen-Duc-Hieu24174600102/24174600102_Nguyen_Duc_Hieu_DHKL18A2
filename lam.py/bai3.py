
full_name = input("Nhập vào họ tên đầy đủ: ")
parts = full_name.strip().split()
last_name = parts[0]
first_name = parts[-1]
print(f"Họ: {last_name}, Tên: {first_name}")