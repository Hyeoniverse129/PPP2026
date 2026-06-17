import tkinter as tk
from tkinter import ttk, messagebox

bikes = {
    "파이톤16": {"v": 48, "ah": 15, "speed": {1: 13, 2: 16, 3: 19, 4: 22, 5: 25}},
    "비아지오v6": {"v": 48, "ah": 20, "speed": {1: 15, 2: 17, 3: 19, 4: 21, 5: 23}},
}

rate = {1: 8, 2: 10, 3: 12, 4: 14, 5: 16}

def main():
    def check():
        bike = bikes[model.get()]
        lev = int(level.get())

        try:
            km = float(dist.get())
            now = float(batt.get())
        except:
            messagebox.showerror("오류", "숫자로 입력하세요")
            return

        cap = bike["v"] * bike["ah"]
        use = km * rate[lev]
        have = cap * now / 100

        if have >= use:
            nam = (have - use) / cap * 100
            result.config(text="도착 가능!\n도착하면 약 " + str(int(nam)) + "% 남습니다", fg="green")
        else:
            bujok = use - have
            result.config(text="배터리 부족!\n" + str(int(bujok)) + "Wh 모자랍니다", fg="red")
            messagebox.showwarning("충전 알림", "배터리가 부족합니다. 충전하고 출발하세요")

    def show_info(e=None):
        bike = bikes[model.get()]
        lev = int(level.get())
        s = bike["speed"][lev]
        cap = bike["v"] * bike["ah"]
        info.config(text=str(lev) + "단 = " + str(s) + "km/h / 배터리 " + str(cap) + "Wh")

    root = tk.Tk()
    root.title("전기자전거 배터리 예측")
    root.geometry("400x450")

    tk.Label(root, text="전기자전거 배터리 소모 예측", font=("맑은 고딕", 14)).pack(pady=10)

    f = tk.Frame(root)
    f.pack(pady=5)

    tk.Label(f, text="자전거 모델").grid(row=0, column=0, pady=5)
    model = ttk.Combobox(f, values=list(bikes.keys()), state="readonly")
    model.current(0)
    model.grid(row=0, column=1, pady=5)
    model.bind("<<ComboboxSelected>>", show_info)

    tk.Label(f, text="속도 단계").grid(row=1, column=0, pady=5)
    level = ttk.Combobox(f, values=[1, 2, 3, 4, 5], state="readonly")
    level.current(2)
    level.grid(row=1, column=1, pady=5)
    level.bind("<<ComboboxSelected>>", show_info)

    info = tk.Label(root, text="", fg="gray")
    info.pack()

    tk.Label(f, text="거리 (km)").grid(row=2, column=0, pady=5)
    dist = tk.Entry(f)
    dist.grid(row=2, column=1, pady=5)

    tk.Label(f, text="현재 배터리 (%)").grid(row=3, column=0, pady=5)
    batt = tk.Entry(f)
    batt.grid(row=3, column=1, pady=5)

    tk.Button(root, text="예측하기", command=check, width=15).pack(pady=10)

    result = tk.Label(root, text="값을 입력하고 버튼을 누르세요", font=("맑은 고딕", 11))
    result.pack(pady=10)

    show_info()
    root.mainloop()


if __name__ == "__main__":
    main()
