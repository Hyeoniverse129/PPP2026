print("### 사다리꼴 넓이 계산하기 ###")

top = float(input("사다리꼴의 윗변의 길이를 입력하시오: "))
bottom = float(input("사다리꼴의 밑변의 길이를 입력하시오: "))
height = float(input("사다리꼴의 높이를 입력하시오: "))

area = (top + bottom) * height * 0.5

print(f"사다리꼴의 넓이는 {area} 입니다.")