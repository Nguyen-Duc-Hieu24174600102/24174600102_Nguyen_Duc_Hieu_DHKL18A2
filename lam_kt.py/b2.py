n = int(input("Nhập một số nguyên dương n: "))


sum_of_perfect_numbers = 0


for num in range(n, 2001):
    sum_of_divisors = 0
    

    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    

    if sum_of_divisors == num:
        sum_of_perfect_numbers += num


print(f"Tổng các số hoàn hảo trong khoảng từ {n} đến 2000 là: {sum_of_perfect_numbers}")