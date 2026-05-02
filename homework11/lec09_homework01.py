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

def read_rainfall(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset

def main():
    weather_filename = "weather(146)_2022-2022.csv"
    rainfall = read_rainfall(weather_filename)
    
    tavgs = read_tavg("weather(146)_2022-2022.csv")
    print(f"연 평균 온도는 {sum(tavgs) / len(tavgs):0.1f}")

    days_over_5mm = get_days_over_5mm(rainfall)
    print(f"5mm 이상인 총 강우일수는 {days_over_5mm}일입니다.")

    rainfalls = read_rainfall("weather(146)_2022-2022.csv")
    print(f"총 강수량은 {sum(rainfalls)}")

if __name__ == "__main__":
    main()