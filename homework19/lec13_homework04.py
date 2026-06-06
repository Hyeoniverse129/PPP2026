import time

def countdown(n):
    for i in range(n, 0, -1):
        print(i, end="\r")
        time.sleep(1)
    print("펑!  ")

def main():
    n = int(input("몇 초부터 카운트다운 할까요? "))
    print(f"{n}초 카운트다운 시작!")
    countdown(n)

if __name__ == "__main__":
    main()
