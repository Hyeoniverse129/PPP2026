
#마트에서 물건을 샀을 때, 총 구매금액을 구해보자.
mart = {
    "우유": 2800, 
    "계란": 300, 
    "빵": 1200, 
    "물": 1700}

#cart = ["물", "물", "계란", "빵", "빵", "빵"]
cart = ["계란", "계란", "빵"]

total = 0
for item in cart:
    total += mart[item]
    print(total)
print(f"총 {total:,}원입니다.")

