import random

CHOSUNG_LIST = [
    "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ",
    "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"
]

WORD_LIST = [
    "사과", "바나나", "포도", "딸기", "수박",
]

def get_chosung(word: str) -> str:
    result = ""
    for c in word:
        code = ord(c) - 0xAC00
        if code >= 0:         
            chosung_index = code // 28 // 21
            result += CHOSUNG_LIST[chosung_index]
        else:
            result += c      
    return result

def main():
    word = random.choice(WORD_LIST) 
    chosung = get_chosung(word)   

    print("=== 초성 게임 ===")
    print(f"초성 힌트: {chosung}")
    answer = input("단어를 맞춰보세요: ")

    if answer == word:
        print("정답입니다!")
    else:
        print(f"틀렸습니다. 정답은 [{word}] 입니다.")

if __name__ == "__main__":
    main()
