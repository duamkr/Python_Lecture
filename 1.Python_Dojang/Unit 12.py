


for i in range(10) :
    print(i, end = ' ')
    i = 10

for i in range(10):
    i = 10
    print(i, end=' ')

# 시퀀스 개체로 반복하기

a = [10, 20, 30, 40, 50]

 # 구식
for i in range(len(a)) :
    print(a[i])

 # python에서는 시퀀스객체는 a자체를 지정해 반복문 지정 가능
for i in a :
    print(i)

# ex라는 리스트를 생성 후 for 문에 적용 a 에 ex리스트를 적용
ex = [18,28,38,48,58]
for a in ex :
    print(a)

for letter in 'Python' :
    print(letter)

# 딕셔너리 적용

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

# for 문으로 a에 lux(딕셔너리)를 적용시 키값만 표시됨(벨류값 제외)
for a in lux :
    print(a)

# 아래의 적용, a, + '=', lux[a](value값) 적용
for a in lux:
    print(a, '=', lux[a])

# nCr  /  n! / r!(n-r)! / 10 C 5

factorial = 1
for i in range(1,11) :
    factorial *= i

nominator = factorial
factoria = 1
for i in range(1,6) :
    factorial *= i


denom = factorial
nominator / (denom * denom)


import random as rd

for i in range(10) :
    print(rd.randint(1,6))


# i = 0부터 시작해서 i !=3 이라는 while 조건식설정,
# 1~6까지 randint설정 후 돌리면 3이 나오기 전까지 돌아감
i = 0
while i != 3 :
    i = rd.randint(1,6)
    print(i)

# while 조건식에 True를 설정 후 시작
# 주사위 2개를 던져 10이 넘을 경우 break
while True :
    dice = rd.randint(1, 6)
    dice2 = rd.randint(1, 6)
    print(dice,dice2)
    if dice + dice2 >=10:
        break

print("Total count =", count)


# continue 활용 1~100까지 홀수만 출력

for i in range(100) :
    if i % 2 == 0 :
        continue
    print(i, end=' ')


# 계단식 별 출력하기

for i in range(5) :
    for k in range(i) :
        print('*', end = '')
    print()

for i in range(1,6) :
    for k in range(i) :
        print('*', end='')
    print()

# 계단식 별 출력(빈칸 적용)
for i in range(5) :
    for k in range(5) :
        if k == i :
            print('*', end='')
        else :
            print(' ', end='')
    print()

# 계단신 별 출력(빈칸 적용)
for i in (range(5)):
    for k in range(i):
        print(' ', end='')
    print('*')


# 반대로
for i in reversed(range(5)) :
    for k in range(i) :
        print(' ', end='')
    print('*')


# Bubble sort  오름차순
#aList = [5, 4, 21, 3, 15,1]
aList = list(map(int, (input('숫자들을 입력하세요').split())))
for i in range(0, len(aList)-1) :
    for k in range(i + 1, len(aList)) :
        if aList[i] > aList[k] :
            aList[i], aList[k] = aList[k], aList[i]

print(aList)

for i in range(5) :
    print(i)
    for k in range(5):
        print(k, end='')
        if k == 4 :
            break
    print()

for i in range(5) :
    print(i)
    for k in range(5):
        print(k, end='')
        if k == i :
            break
    print()


# FizzBuzz 문제
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# FizzBuzz 코드 단축하기

for i in range(1, 101) :
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)




# 터틀 그래픽스 그림그리기(사각형)

import turtle as t
t.shape('turtle')
t.forward(100)
t.right(45)
t.forward(50)


import cvxopt