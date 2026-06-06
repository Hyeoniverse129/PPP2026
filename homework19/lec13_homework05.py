import random

def gugudan_correct():
    a = random.randint(2, 9)
    b = random.randint(1, 9)
    ans = input(f"{a} x {b} = ")
    if int(ans) == a * b:
        print("정답!")
        return True
    else:
        print(f"틀렸습니다! 정답은 {a * b}입니다.")
        return False

def main():
    count = int(input("문제 수를 입력하세요: "))
    score = 0
    point = 100 // count

    for i in range(count):
        print(f"\n[{i+1}/{count}번 문제]")
        if gugudan_correct():
            score += point

    print(f"\n=== 결과 ===")
    print(f"총 점수: {score}점")

if __name__ == "__main__":
    main()
