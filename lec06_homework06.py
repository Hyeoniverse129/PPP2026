#2. 1-n까지 리스트를 돌려주는 함수를 만드시오. 함수는 get_range_list(n)


def get_range_list(n):
    result = [] #상자 만들기
    for i in range(1, n + 1):
        result.append(i) #숫자 넣기
    return result

def main():
    n = int(input("1 - n까지 리스트를 돌려 받을 숫자를 입력하시오: "))
    print(get_range_list(n))

if __name__ == "__main__":
    main()