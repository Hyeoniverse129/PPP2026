def sum_n(n):
    total = 0
    for i in range (1, n+1):
        total += i
    return total

def main():
    n = int(input("1부터 어디까지의 합을 구할까요? -> "))
    sum = sum_n(n)
    print(sum) #함수 안에다가 넣으면?
    
if __name__ == "__main__":
    main()