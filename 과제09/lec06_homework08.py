
def average(nums):
    total = 0
    for n in nums:
        total += n
    result = total / len(nums) #len: 리스트 갯수
    return result

def main():
    num_input = input("숫자들을 띄어쓰기로 구분하여 입력하시오: ")
    str_list = num_input.split()

    nums = []
    for s in str_list:
        nums.append(int(s))         

    print(average(nums))

if __name__ == "__main__":
    main()