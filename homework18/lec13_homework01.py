
def toggle_ch(alphabet):
    if ord(alphabet) >= 65 and ord(alphabet) <= 90:   
        return chr(ord(alphabet) + 32)                 
    elif ord(alphabet) >= 97 and ord(alphabet) <= 122: 
        return chr(ord(alphabet) - 32)                 
    return alphabet                                   

def toggle_text(text: str) -> str:
    result = ""
    for c in text:
        result += toggle_ch(c)
    return result

def main():
    text = input("문자열을 입력하세요: ")
    print("변환 결과:", toggle_text(text))

if __name__ == "__main__":
    main()
