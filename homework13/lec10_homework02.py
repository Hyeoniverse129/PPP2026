def read_rainfall(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset

def read_years(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(int(tokens[0]))
    return dataset

def sumifs(rainfall, years, selected):
    total = 0.0
    for i in range(len(rainfall)):
        if years[i] in selected:
            total = total + rainfall[i]
    return total

def main():
    rainfall = read_rainfall("weather(146)_2001-2022.csv")
    years = read_years("weather(146)_2001-2022.csv")
    total_rainfall_21 = sumifs(rainfall, years, selected=[2021])
    total_rainfall_22 = sumifs(rainfall, years, selected=[2022])
    
    print(f"2021년 총 강수량은 {total_rainfall_21:0.1f}mm")
    print(f"2022년 총 강수량은 {total_rainfall_22:0.1f}mm")


if __name__ == "__main__":
    main()