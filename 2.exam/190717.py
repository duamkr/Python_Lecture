# 조건문

# 1.  연도를 입력으로 받아 윤년인지 아닌지를 출력하는 프로그램을 작성하시오.윤년은 연도가 4의 배수이면서,
# 100의 배수가 아닐 때 또는 400의 배수일 때이다. 예를들어, 2012년은 4의 배수라서 윤년이지만,
# 1900년은 4의 배수이지만, 100의 배수이기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.)

year = int(input('년도'))
if year % 4 == 0 :
    if year == 400 :
        print(year, '년은 윤년입니다.')
    elif year % 100 == 0 :
        print(year, '년은 윤년이 아닙니다.')
    else :
        print(year, '년은 윤년입니다.')
else :
    print(year, '년은 윤년이 아닙니다.')


# 2.  상근이의 알람을 45분 일찍 맞춰주는 프로그램

h, m = map(int, input('상근이의알람시간').split(':'))

if  m >= 45 :
    m -= 45
else :
    h -= 1
    m += 15

print('45분 일찍 알림', h,':',m)

# 3. 세 정수 a, b, c를 입력으로 받아 두번째로 큰 정수를 출력하는 프로그램 작성
a, b, c = map(int, input().split())

if a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)
elif b > a and b > c:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if a > b:
        print(a)
    else:
        print(b)



a, b, c = map(int, input().split())
d = [a, b, c]
d.sort()
print(d[1])

# 피타고라스 정리
a, b, c = map(int, input().split())

if a*a + b*b == c*c and a < b < c and a + b > c :
    if a < 332 and b < 333 and c < 338 :
        print('피타고라스 정리입니다.')
    else :
    print('피타고라스 땡탈락')
    for a in range(1,333) :

# 피타고라스 정의가 맞는지까지는 했습니다만 그 이후는 너무 어렵습니다.

    outerBreak = False
    for a in range(1, 333):
        if outerBreak:
            break
        for b in range(a + 1, 500):
            c = 1000 - a - b
            if c < b:
                continue
            if a ** 2 + b ** 2 == c ** 2:
                print(a, b, c, a + b + c)
                print(a ** 2, b ** 2, c ** 2)
                outerBreak = True
                break;


# 반복문
# 1. 두정수의 테스트 케이스 출력
t = int(input())
a, b = map(int,input().split())

if a > 0 and b <10 :
    for i in range(1,t+1) :
        print('Case #'+ str(i) + ':', a, '+', b, '=', a+b)


# 2. 별 그리기
star = int(input('5이상 9이하 홀수를 입력하시오'))

for i in range(1,star+1) :
    if i % 2 == 1 :
    print(('*' * i).center(star))

for i in reversed((range(1,star))) :
    if i % 2== 1 :
    print(('*' * i).center(star))


# 3. 디지털 시계에 하루동안 (00:00 ~ 23 : 59) 3이 표시되는 시간을 초로 환산하면 총 몇초일까요
all_time = 0
for h in range(24):
    for m in range(60):
        time = str(h) + str(m)
        if '3' in time:
            all_time += 60

print(all_time)

# 4. 1~1000 에서 각 숫자의 개수를 구하시오

a,  b = map(int, input().split())
text = ""
for i in range(a,b+1) :
    text += str(i)
for k in range(0,10) :
    print(k,'=', text.count(str(k)))

# 5. 완전수 구하기..

def getDivisor(number):
    result = list()
    for i in range(1, number):
        if number % i == 0:
            result.append(i)
    return result

n = int(input('정수 입력> '))
for i in range(1, n+1):
    div = getDivisor(i)
    if i == sum(div):
        print(i)



# 6. 자연수 1~10까지 자연수를 각각 제곱 후 합의제곱+제곱의합
a= 0
b= 0
n = int(input())
for i in range(1, n+1) :    #  합의 제곱
    a += i
    b += i**2

print(a*a - b)