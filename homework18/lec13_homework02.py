
def caesar_encode(text: str, shift: int = 3) -> str:
    result = ""
    for c in text:
        if ord(c) >= 65 and ord(c) <= 90:
            result += chr((ord(c) - 65 + shift) % 26 + 65)
        elif ord(c) >= 97 and ord(c) <= 122:
            result += chr((ord(c) - 97 + shift) % 26 + 97)
        else:
            result += c
    return result

def caesar_decode(text: str, shift: int = 3) -> str:
    result = ""
    for c in text:
        if ord(c) >= 65 and ord(c) <= 90:
            result += chr((ord(c) - 65 - shift) % 26 + 65)
        elif ord(c) >= 97 and ord(c) <= 122:
            result += chr((ord(c) - 97 - shift) % 26 + 97)
        else:
            result += c
    return result

def main():
    text = input("암호화할 문자열을 입력하세요: ")
    encoded = caesar_encode(text)
    decoded = caesar_decode(encoded)
    print("암호화:", encoded)
    print("복호화:", decoded)

if __name__ == "__main__":
    main()
