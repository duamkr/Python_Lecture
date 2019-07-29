# 숫자 야구 게임


import random

pt = random.sample(range(1,10),3) # 랜덤 샘플 1 ~ 10 까지

try_cnt = 0
st_cnt = 0
ba_cnt = 0

while(st_cnt < 3) :
    num = input("숫자입력 : ")
    if(num[0] == num[1] == num[2]) :      # 입력된 숫자가 각각 다른지를 구분, try_cnt 에 1을 더하는 것은 입력횟수도 시도횟수에 포함하깅 위함
        print("1 ~  9까지 각기 다른 숫자 3개 입력해 주세요")
        try_cnt += 1
        continue
    elif(num[0] == num[1]) :
        print("1 ~  9까지 각기 다른 숫자 3개 입력해 주세요")
        try_cnt += 1
        continue
    elif(num[0] == num[2]) :
        print("1 ~  9까지 각기 다른 숫자 3개 입력해 주세요")
        try_cnt += 1
        continue
    elif(num[1] == num[2]) :
        print("1 ~  9까지 각기 다른 숫자 3개 입력해 주세요")
        try_cnt += 1
        continue
    else :
        pass     # 3개의 숫자가 모두 다르다면 다음 소스로 넘어감

    st_cnt = 0
    ba_cnt = 0

    for i in range(0,3) :
        for k in range(0,3):
            if(num[i] == str(pt[k]) and i == k) :
                st_cnt += 1
            elif(num[i] == str(pt[k]) and i != k) :
                ba_cnt += 1

        print(st_cnt, "스트라이크", ba_cnt, "볼")
        try_cnt += 1





