#3. 연도(y)를 주면, 윤년인지(True) 아닌지를(False) 알려주는 is_leap_year(y) 함수를 만드시오.
def is_leap_year(y):
    if y % 4 == 0:        # 조건1: 4로 나누었을때 나누어 떨어지면 일단 윤년
        if y % 100 == 0:  # 조건2: but, 100으로도 나누어 떨어진다면 윤년 아님
            return False
        return True
    return False

def main():
    y = int(input("윤년임을 확인할 연도를 입력하시오: "))
    if is_leap_year(y) == True:
        print(f"[{y}]년은 윤년입니다.")
    else:
        print(f"[{y}]년은 윤년이 아닙니다.")

if __name__ == "__main__":
    main()