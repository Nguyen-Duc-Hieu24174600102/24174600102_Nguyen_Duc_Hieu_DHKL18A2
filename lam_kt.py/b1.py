import math

# Nhập chiều dài đường chéo của hình vuông
n = float(input("Nhập chiều dài đường chéo của hình vuông: "))

# Tính cạnh của hình vuông từ chiều dài đường chéo
cạnh = n/ math.sqrt(2)


chu_vi = 4 * cạnh

print(f"Chu vi của hình vuông là: {chu_vi:.2f}")

