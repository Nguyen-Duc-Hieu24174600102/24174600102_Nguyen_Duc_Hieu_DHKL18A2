number = int(input("Nhập một số nguyên: "))
if number < 0:
    print(f"{number} không phải là số chính phương.")
else:

    is_perfect_square = True
    for i in range(0, number + 1):
        if i * i == number:  
            is_perfect_square = True
            break  

    if is_perfect_square:
        print(f"{number} là số chính phương.")
    else:
        print(f"{number} không phải là số chính phương.")