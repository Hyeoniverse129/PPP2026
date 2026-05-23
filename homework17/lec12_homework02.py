def str2int(text: str, x_value: int = None) -> int:
    try:
        return int(text)
    except ValueError:
        return x_value

def main():
    values = []
    while True:
        x = input("X=>? ")
        x_value = str2int(x) # 정수 or None
        if x_value == -1:
            break # -1이 결과에 포함됨. 그래서 나중에 결과값이 달라질 수 있음.
        if x_value is not None:
            values.append(x_value)

    print(f"입력된 값은 {values} 입니다.  총 {len(values)}개의 자연수가 입력되었고, 평균은 {sum(values)/len(values)}입니다.")

if __name__ == "__main__":
    main()