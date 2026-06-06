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

    print("=== 단어 맞추기 게임 ===")
    print(f"글자 수: {len(word)}글자")

    while wrong < MAX_TRIES:
        print()
        print("단어:", get_display(word, guessed))
        print(f"남은 기회: {MAX_TRIES - wrong}번")

        letter = input("알파벳 입력: ").lower()

        if letter in guessed:
            print("이미 입력한 알파벳입니다!")
            continue

        guessed.append(letter)

        if letter in word:
            print("정답 알파벳!")
            if all(c in guessed for c in word):
                print(f"\n축하합니다! 정답은 [{word}] 입니다!")
                return
        else:
            wrong += 1
            print("틀렸습니다!")

    print(f"\n게임 오버! 정답은 [{word}] 였습니다.")

if __name__ == "__main__":
    main()
