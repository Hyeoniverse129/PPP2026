import random

def lotto():
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    return numbers

def main():
    print("=== 로또 번호 추출기 ===")
    count = int(input("몇 게임 추출할까요? "))

    for i in range(count):
        numbers = lotto()
        print(f"{i+1}게임: {numbers}")

if __name__ == "__main__":
    main()
