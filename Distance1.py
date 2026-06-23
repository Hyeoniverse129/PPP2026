print("### 사분면 출력하기 ###")

x1 = int(input("x1을 입력하시오: "))
y1 = int(input("y1을 입력하시오: "))

if x1 > 0 and y1 > 0:
    print(f"입력한 좌표 ({x1}, {y1})은/는 1사분면입니다.")
elif x1 < 0 and y1 > 0:
    print(f"입력한 좌표 ({x1}, {y1})은/는 2사분면입니다.")
elif x1 < 0 and y1 < 0:
    print(f"입력한 좌표 ({x1}, {y1})은/는 3사분면입니다.")
elif x1 > 0 and y1 < 0:
    print(f"입력한 좌표 ({x1}, {y1})은/는 4사분면입니다.")
else:
    print(f"입력한 좌표 ({x1}, {y1})은/는 원점입니다.")