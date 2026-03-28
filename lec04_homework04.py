import math

print(f"{'각':^2} | {'라디안':^6} | {'sin':^9} | {'cos':^9} | {'tan':^9}")
print("-" * 58)

for angle in range(0, 91):
    rad = math.radians(angle)
    sin = math.sin(rad)
    cos = math.cos(rad)
    
    angle_d = f"{angle}°"
    
    if angle == 90:
        tan = "정의되지 않음"
        print(f"{angle_d:^3} | {rad:9.4f} | {sin:9.4f} | {cos:9.4f} | {tan:^12}")
    else:
        tan = math.tan(rad)
        print(f"{angle_d:^3} | {rad:9.4f} | {sin:9.4f} | {cos:9.4f} | {tan:9.4f}")