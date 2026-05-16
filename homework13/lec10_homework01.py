def read_rainfall(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset

def read_months(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(int(tokens[1]))
    return dataset

def sumifs(rainfall, months, selected):
    total = 0.0
    for i in range(len(rainfall)):
        if months[i] in selected:
            total = total + rainfall[i]
    return total

def main():
    rainfall = read_rainfall("weather(146)_2022-2022.csv")
    months = read_months("weather(146)_2022-2022.csv")
    total_rainfall = sumifs(rainfall, months, selected=[6, 7, 8])
    
    print(f"여름철(6월-8월) 총 강수량은 {total_rainfall:0.1f}mm")

if __name__ == "__main__":
    main()