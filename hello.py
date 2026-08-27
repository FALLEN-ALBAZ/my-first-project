import math

def giai_phuong_trinh_bac_2(a, b, c):
    # Xử lý trường hợp a = 0 (trở thành phương trình bậc 1: bx + c = 0)
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm" if c == 0 else "Phương trình vô nghiệm"
        return f"Phương trình có một nghiệm: x = {-c / b}"
    
    # Tính toán Delta
    delta = b**2 - 4*a*c
    
    # Biện luận theo hệ số Delta
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1:.2f}, x2 = {x2:.2f}"
    
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x1 = x2 = {x:.2f}"
    
    else:
        # Sử dụng thư viện cmath nếu bạn muốn xuất ra nghiệm phức
        return "Phương trình vô nghiệm (trong tập số thực)"

# Chạy thử nghiệm
a = 1
b = -3
c = 2

ket_qua = giai_phuong_trinh_bac_2(a, b, c)
print(f"Giải phương trình {a}x^2 + {b}x + {c} = 0:")
print(ket_qua)