import PySimpleGUI as sg
import random

WORDS = ["python", "smartfarm"]
MAX_TRIES = 6

def get_display(word, guessed):
    result = ""
    for c in word:
        if c in guessed:
            result += c + " "
        else:
            result += "_ "
    return result.strip()

def main():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0

    layout = [
        [sg.Text(f"글자 수: {len(word)}글자")],
        [sg.Text(get_display(word, guessed), key="-WORD-", size=(30, 1))],
        [sg.Text(f"남은 기회: {MAX_TRIES}번", key="-TRIES-", size=(20, 1))],
        [sg.Text("", size=(30, 1), key="-OUTPUT-")],
        [sg.InputText(key="-INPUT-")],
        [sg.Button("입력"), sg.Button("종료")]
    ]

    window = sg.Window("단어 맞추기", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "종료":
            break

        if event == "입력":
            letter = values["-INPUT-"].lower()
            window["-INPUT-"].update("")

            if letter in guessed:
                window["-OUTPUT-"].update("이미 입력한 알파벳입니다!")
                continue

            guessed.append(letter)

            if letter in word:
                window["-OUTPUT-"].update("정답 알파벳!")
                window["-WORD-"].update(get_display(word, guessed))

                if all(c in guessed for c in word):
                    window["-OUTPUT-"].update(f"축하합니다! 정답은 [{word}] 입니다!")
                    window["-WORD-"].update(word)
            else:
                wrong += 1
                window["-OUTPUT-"].update("틀렸습니다!")
                window["-TRIES-"].update(f"남은 기회: {MAX_TRIES - wrong}번")

                if wrong >= MAX_TRIES:
                    window["-OUTPUT-"].update(f"게임 오버! 정답은 [{word}]")

    window.close()

if __name__ == "__main__":
    main()
