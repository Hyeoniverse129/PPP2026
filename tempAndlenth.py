print("### 온도 + 길이 변환 프로그램 ###")
print('='* 10)
print("1. 화씨 -> 섭씨")
print("2. 섭씨 -> 화씨")
print("3. 피트(ft) -> cm")
print("4. cm -> 피트(ft)")
print('='* 10)

choice = int(input("원하는 기능(1 ~ 4)을 선택하시오: "))

if choice == 1:
    tempF = float(input("화씨 온도(℉)를 입력하시오: "))
    tempF = (tempC - 32) * 5/9
    print(f"화씨 {tempF:0.1f} -> 섭씨 {tempC:0.1f}")

elif choice == 2:
    tempC = float(input("섭씨 온도(℃)를 입력하시오: "))
    tempF = tempC * 9/5 + 32
    print(f"섭씨 {tempC:0.1f} -> 화씨 {tempF:0.1f}")

elif choice == 3:
    ft = float(input("cm로 변환할 ft를 입력하시오: "))
    cm = ft / 0.0328
    print(f"ft {ft:0.1f} -> cm {cm:0.1f}")
elif choice == 4:
    cm = float(input("ft로 변환할 cm를 입력하시오: "))
    ft = cm * 0.0328
    print(f"cm {cm:0.1f} -> ft {ft:0.1f}")
    
else:
    print("사용을 종료합니다.")