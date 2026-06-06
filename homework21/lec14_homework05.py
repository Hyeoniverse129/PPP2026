import PySimpleGUI as sg
import random

def lotto():
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    return numbers

def main():
    layout = [
        [sg.Text("몇 게임 추출할까요?")],
        [sg.InputText(key="-INPUT-")],
        [sg.Multiline("", size=(35, 10), key="-OUTPUT-", disabled=True)],
        [sg.Button("추출"), sg.Button("종료")]
    ]

    window = sg.Window("🎰 로또 번호 추출기", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "종료":
            break

        if event == "추출":
            count = int(values["-INPUT-"])
            result = ""
            for i in range(count):
                numbers = lotto()
                result += f"{i+1}게임: {numbers}\n"
            window["-OUTPUT-"].update(result)

    window.close()

if __name__ == "__main__":
    main()

