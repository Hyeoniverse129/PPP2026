def read_dates(weather_filename):
    dates = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            token = line.split(",")
            date = [int(token[0]), int(token[1]), int(token[2])]
            dates.append(date)

    return dates

def read_weather_col(weather_filename, col_idx):
    values = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            value = float(tokens[col_idx])
            values.append(value)

    return values        

def get_max_diff(dates, tmax, tmin, target_year):
    max_diff = -999

    for i in range(len(dates)):
        if dates[i][0] == target_year:
            diff = tmax[i] - tmin[i]
            if diff > max_diff:
                max_diff = diff
                max_diff_date = dates[i]

    return max_diff_date, max_diff

def main():
    weather_filename = "weather(146)_2001-2022.csv"
    dates = read_dates(weather_filename)
    tmax = read_weather_col(weather_filename, 3)
    tmin = read_weather_col(weather_filename, 5)
    
    for year in range(2001, 2022):
        date, temp_diff = get_max_diff(dates, tmax, tmin, year)
        print(f"일교차가 가장 큰 날: {date}")
        print(f"일교차가 가장 큰 날의 일교차는 {temp_diff:.1f}도")

if __name__ == "__main__":
    main()