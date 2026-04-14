cal_dict = {
        "한라봉": 50, "딸기": 34, "바나나": 77 
}
eat_dict = {
        "한라봉": 100, "딸기": 200, "바나나": 500 
}

def total_cal(): 
    total = 0
    for key, val in eat_dict.items():
        if key in cal_dict:
                total += val * cal_dict[key] # ket - 한라봉... val - 먹은양
    print(total)

def main():
    total_cal()

if __name__ == "__main__":
    main()