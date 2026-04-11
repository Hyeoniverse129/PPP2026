#1. 숫자 리스트를 매개변수로 받아서 평균을 구하는 함수를 완성하시오. 함수는 average(nums)

def average(nums):
    total = 0
    for n in nums:
        total += n
    result = total / len(nums) #len: 리스트 갯수
    return result

def main():
    nums = [10, 20, 30, 40, 50]
    print(average(nums))

if __name__ == "__main__":
    main()