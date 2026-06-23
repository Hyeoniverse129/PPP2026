print("### 원 넓이 계산하기 ###")

import math

radius = float(input("반지름을 입력하시오: "))

area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print(f"원의 둘레는 {circumference:0.1f}, 넓이는 {area:0.2f} 입니다.")