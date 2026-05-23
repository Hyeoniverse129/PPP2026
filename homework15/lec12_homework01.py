def read_rainfall(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset

def read_tavg(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[4]))
    return dataset

def get_days_over_5mm(rainfall):
    count_5mm = 0
    for r in rainfall:
        if r >= 5:
            count_5mm += 1
    return count_5mm

def main():
    filename = r"lec12\weather_2023.csv"
    output = r"lec12\homework15_result.txt"

    rainfall = read_rainfall(filename)
    tavgs = read_tavg(filename)
    days_over_5mm = get_days_over_5mm(rainfall)
    rainfalls = read_rainfall(filename)
    
    with open(output, 'w', encoding = 'utf-8') as f:
        f.write(f"연 평균 온도는 {sum(tavgs) / len(tavgs):0.1f}\n")
        f.write(f"5mm 이상인 총 강우일수는 {days_over_5mm}일입니다.\n")
        f.write(f"총 강수량은 {sum(rainfalls)}\n")

    print(f"결과가 '{output}' 파일에 성공적으로 저장되었습니다.")

if __name__ == "__main__":
    main()