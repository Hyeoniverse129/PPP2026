print("### 칼로리 구하기 ###")

Ha = float(input("한라봉 섭취량(g)을 입력하시오: "))
St = float(input("딸기(설향) 섭취량(g)을 입력하시오: "))
Ba = float(input("바나나 섭취량(g)을 입력하시오: "))

Ha_kcal = Ha * 0.5
St_kcal = St * 0.34
Ba_kcal = Ba * 0.77

print(f"----------\n섭취한 한라봉의 칼로리: {Ha_kcal}\n섭취한 딸기(설향)의 칼로리: {St_kcal}\n섭취한 바나나의 칼로리: {Ba_kcal}\n----------")