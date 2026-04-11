def gugudan(dan):
    result = 0
    for n in range(1, 10):
        result = dan * n
        print(f"{dan} x {n} = {result}")

def main():
    dan = int(input("출력할 단수를 입력하시오: "))
    gugudan(dan)

if __name__ == "__main__":
    main()