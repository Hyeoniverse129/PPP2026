print("### BMI 계산하기 ###")

import math

height = float(input("신장(cm)을 입력하시오: "))
weight = float(input("체중(kg)을 입력하시오: "))

height_m = height * 0.01

BMI = weight / math.pow(height_m, 2)

print(f"BMI는 {BMI} 입니다.")