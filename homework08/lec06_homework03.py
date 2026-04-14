def f2c(temp_f):
    temp_c = (temp_f - 32) / 1.8
    return temp_c

def c2f(temp_c):
    temp_f = temp_c * 1.8 +32
    return temp_f # 또는 간단하게 return tc * 1.8 + 32 로 표현.
    
def main():
    print(f2c(80))
    print(c2f(26.67))
    #어떤 처리를 하냐?
if __name__ == "__main__":
    main() 
