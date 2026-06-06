import PySimpleGUI as sg
import time

def main():
    layout = [
        [sg.Text("몇 초부터 카운트다운 할까요?")],
        [sg.InputText(key="-INPUT-")],
        [sg.Text("", size=(20, 1), key="-OUTPUT-")],
        [sg.Button("시작"), sg.Button("종료")]
    ]

    window = sg.Window("카운트다운", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "종료":
            break

        if event == "시작":
            n = int(values["-INPUT-"])
            for i in range(n, 0, -1):
                window["-OUTPUT-"].update(f"⏱ {i} 초")
                window.refresh()
                time.sleep(1)
            window["-OUTPUT-"].update("펑!")

    window.close()

if __name__ == "__main__":
    main()
