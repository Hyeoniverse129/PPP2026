print("### BMI 계산하기 - 비만도 측정 ###")

height = float(input("신장(cm)을 입력하시오: "))
weight = float(input("체중(kg)을 입력하시오: "))

height_m = height * 0.01

BMI = weight / (height_m**2)

print(f"BMI는 {BMI} 입니다.")

if BMI <= 24.9:
    print("비만 전단계입니다.")
elif 29.9 >= BMI >= 25:
    print("1단계 비만입니다.") 
elif 34.9 >= BMI >= 30:
    print("2단계 비만입니다.")
else:
    print("3단계 비만입니다.")