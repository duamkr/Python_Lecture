print('Hello, world!')

# Unit 29. 함수사용하기
def hello() :
    print("Hello, world!")

hello()

# 덧셈 함수 만들기
def add(a,b):
    """a,b의 덧셈함수"""
    print(a+b)

add(1,2)

# 함수의 결과를 반환하기

def add(a,b) :
    return a+b

add(10,20)

def not_ten(a):
    if a == 10 :
        return
    print('10이 아닙니다')

not_ten(10)


# 학점 계산 함수
def grade(a) :
    if a >= 90 :
        gr = 'A'
    elif a >= 80 :
        gr = 'B'
    elif a >= 70 :
        gr = 'C'
    elif a >= 60 :
        gr = 'D'
    else :
        gr= 'F'
    return gr


def grade2(a) :
    if score >= 90 :
        return = 'A'
    if score >= 80:
        return = 'B'
    if score >= 70 :
        return = 'C'
    if score >= 60 :
        return = 'D'
    return gr

# 함수에서 값을 여러 개 반환하기
def add_sub(a,b) :
    return a + b, a - b

add_sub(10,20)

def mySum(n) :
    sum = 0
    for i in range(n+1) :
        sum += i
    return sum

mySum(100)


matrix = []
for i in range(row):
    matrix.append(list(input()))