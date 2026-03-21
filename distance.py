print("### 두 지점 사이 거리 구하기 ###")

import math

x1 = float(input("x1을 입력하시오: "))
y1 = float(input("y1을 입력하시오: "))
x2 = float(input("x2을 입력하시오: "))
y2 = float(input("y2을 입력하시오: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"두 지점 사이의 거리는 {distance} 입니다.")