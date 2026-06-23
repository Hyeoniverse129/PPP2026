#  고민거리
# - 프로그램 실행시. 한라봉. 딸기. 바나나 순인데, 순서를 바꿔서 입력하면? 딸기, 바나나, 한라봉 순으로 입력?
# - 만약 딸기만 300g 먹었다면?
# - 만약 칼로리DB에 항목이 20개가 있고, 그 중 내가 먹은 게 5가지라면?
# - 홈페이지에 이런 데이터가 있는데, 코드를 가지고 올 수는 없을까?

cal_dict = {
        "한라봉": 50, "딸기": 34, "바나나": 77 
}
eat_dict = {
        "한라봉": 100, "딸기": 200, "바나나": 500 
}
eat_dict = {
        "딸기": 300, "망고": 200
}

total_cal = 0
for key, val in eat_dict.items():
    #print(key, val)
    if key in cal_dict:
        total_cal += val * cal_dict[key] # ket - 한라봉... val - 먹은양
print(total_cal)
