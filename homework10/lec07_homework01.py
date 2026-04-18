import statistics

def text2list(text):
    num_list = [int(x) for x in text.split()]
    return num_list

def count_list(nums):
    return len(nums)

def average_list(nums):
    return sum(nums) / len(nums)

def max_list(nums):
    return max(nums)

def min_list(nums):
    return min(nums)

def median_list(nums):
    return statistics.median(nums)

def read_text(filename):
    with open(filename) as f:
        text = f.read()
    return text

def main():
    input_text = read_text("numbers1.txt")
    nums = text2list(input_text) # nums = [5, 10, 3, 4, 7]
    print("주어진 리스트는", nums)
    print("개수:", count_list(nums))
    print("평균:", average_list(nums))
    print("최댓값:", max_list(nums))
    print("최솟값:", min_list(nums))
    print("중앙값", median_list(nums))

if __name__ == "__main__":
    main()