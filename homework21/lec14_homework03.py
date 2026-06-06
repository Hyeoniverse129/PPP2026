import PySimpleGUI as sg
import random

def main():
    total = 5          # 문제 수
    score = 0
    current = 0
    a = random.randint(2, 9)
    b = random.randint(1, 9)

    layout = [
        [sg.Text(f"문제 {current+1}/{total}: {a} x {b} = ?", key="-QUESTION-", size=(30, 1))],
        [sg.InputText(key="-INPUT-")],
        [sg.Text("", size=(30, 1), key="-OUTPUT-")],
        [sg.Button("확인"), sg.Button("종료")]
    ]

    window = sg.Window("구구단 문제집", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "종료":
            break

        if event == "확인":
            ans = int(values["-INPUT-"])
            if ans == a * b:
                window["-OUTPUT-"].update("✅ 정답!")
                score += 100 // total
            else:
                window["-OUTPUT-"].update(f"❌ 틀렸습니다! 정답은 {a * b}")

            current += 1
            window["-INPUT-"].update("")

            if current < total:
                a = random.randint(2, 9)
                b = random.randint(1, 9)
                window["-QUESTION-"].update(f"문제 {current+1}/{total}: {a} x {b} = ?")
            else:
                window["-QUESTION-"].update(f"게임 종료! 최종 점수: {score}점")
                window["-OUTPUT-"].update("")

    window.close()

if __name__ == "__main__":
    main()
