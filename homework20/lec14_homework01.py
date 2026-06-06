import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

MONTH = 6
DAY   = 18
YEAR  = 2006

def download_weather(filename, stid, sy, ey):
    url = f"https://api.taegon.kr/stations/{stid}/?sy={sy}&ey={ey}&format=csv"
    if not os.path.exists(filename):
        resp = requests.get(url)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(resp.text)

def main():
    download_weather("jeonju.csv", 146, 1980, 2024)
    download_weather("suwon.csv",  119, 1980, 2024)

    df_jj = pd.read_csv("jeonju.csv", skipinitialspace=True)
    df_sw = pd.read_csv("suwon.csv",  skipinitialspace=True)

    # 1) 전주 2012년 연 강수량
    ans1 = df_jj[df_jj["year"] == 2012]["rainfall"].sum()
    print(f"1) 전주시 2012년 연 강수량: {ans1:.1f} mm")

    # 2) 전주 2024년 최대기온
    ans2 = df_jj[df_jj["year"] == 2024]["tmax"].max()
    print(f"2) 전주시 2024년 최대기온: {ans2} °C")

    # 3) 전주 2020년 최대 일교차
    df_jj["tdiff"] = df_jj["tmax"] - df_jj["tmin"]
    ans3 = df_jj[df_jj["year"] == 2020]["tdiff"].max()
    print(f"3) 전주시 2020년 최대 일교차: {ans3:.1f} °C")

    # 4) 수원·전주 2019년 강수량 차이
    prec_jj = df_jj[df_jj["year"] == 2019]["rainfall"].sum()
    prec_sw = df_sw[df_sw["year"] == 2019]["rainfall"].sum()
    print(f"4) 2019년 강수량 차이: {abs(prec_jj - prec_sw):.1f} mm")

    # 5) 전주·수원 연평균기온 선그래프 (1980~2024)
    avg_jj = df_jj.groupby("year")["tavg"].mean()
    avg_sw = df_sw.groupby("year")["tavg"].mean()

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(avg_jj.index, avg_jj.values, color="r", label="전주(146)")
    ax.plot(avg_sw.index, avg_sw.values, color="b", label="수원(119)")
    ax.set_title("전주 & 수원 연평균 기온 (1980~2024)")
    ax.set_xlabel("연도")
    ax.set_ylabel("기온 (°C)")
    ax.legend()
    fig.savefig("q5_avg_temp.png")
    plt.close()
    print("5) 저장 완료: q5_avg_temp.png")

    # 6) 전주 연간 강수량 막대그래프 (1980~2024)
    rain_jj = df_jj.groupby("year")["rainfall"].sum()

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(rain_jj.index, rain_jj.values, color="b")
    ax.set_title("전주시 연간 강수량 (1980~2024)")
    ax.set_xlabel("연도")
    ax.set_ylabel("강수량 (mm)")
    fig.savefig("q6_rainfall.png")
    plt.close()
    print("6) 저장 완료: q6_rainfall.png")

    # 7) 생일 기준 연도별 기온 선그래프
    df_bd = df_jj[(df_jj["month"] == MONTH) & (df_jj["day"] == DAY)]

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df_bd["year"], df_bd["tavg"], color="r", label=f"{MONTH}/{DAY} 기온")
    ax.set_title(f"전주시 {MONTH}/{DAY} 연도별 기온")
    ax.set_xlabel("연도")
    ax.set_ylabel("기온 (°C)")
    ax.legend()
    fig.savefig("q7_birthday_temp.png")
    plt.close()

    # 1980~2014 순위 분석
    df_range = df_bd[(df_bd["year"] >= 1980) & (df_bd["year"] <= 2014)]
    df_sorted = df_range.sort_values("tavg", ascending=False).reset_index(drop=True)
    my_rank = df_sorted[df_sorted["year"] == YEAR].index[0] + 1
    print(f"7) 내 년도({YEAR}): {len(df_range)}개 연도 중 {my_rank}번째로 기온이 높은 해")
    print(f"   가장 높은 해: {int(df_sorted.iloc[0]['year'])}년 ({df_sorted.iloc[0]['tavg']}°C)")
    print(f"   가장 낮은 해: {int(df_sorted.iloc[-1]['year'])}년 ({df_sorted.iloc[-1]['tavg']}°C)")
    print("7) 저장 완료: q7_birthday_temp.png")

if __name__ == "__main__":
    main()
