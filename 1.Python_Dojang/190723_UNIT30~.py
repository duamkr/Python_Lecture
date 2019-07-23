def print_numbers(a,b,c) :
    print(a)
    print(b)
    print(c)

x = [10,20,30]
print_numbers(*x)

# 가변 인수 함수 만들기

def print_numbers(*args):      # * agrs는 arguments를 가변인수로 사용, 앞에 *을 붙이면 개수에 상관없이 출력됨
    for arg in args:
        print(arg)


print_numbers(10)
print_numbers(10,20,30,40)

y = [100,200,300,400]
print_numbers(y)

# 함수 지정시 a는 고정인수, 뒤는 가변인수 지정
def print_numbers(a, *args) :
    print(a)
    print(args)

print_numbers(1)  # 고정인수 1은 나오지만 가변인수가 입력 안될 시 ()로만 표시됨
print_numbers(1,20,30,40)

print_numbers(*y)

# 키워드 인수 사용하기

def personal_info(name, age, address) :
    print('이름:', name)
    print('나이:', age)
    print('주소:', address)


personal_info('홍길동','429세', '대한민국')
personal_info(address ='대한민국', name='홍길동',age = '429세')    # 키워드는 = ' ' 으로 지정해주면 순서에 상관없이 지정된 함수에 맞춰 출력됨

# 키워드 인수와 딕셔너리 언패킹 사용하기

# **를 두개 붙임
x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)     # ** 제대로 찍었을 시 key, value값  잘 표시됨
personal_info(*x)      # 하나만 찍으면 key값 만 나옴


# 키워드 인수를 사용한 가변 인수 함수 만들기
# kwargs = key word arguments
def personal_info(**kwargs):
    for kw, arg in kwargs.items() :
        print(kw,':', arg, sep='')


x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
x2 = {'name': '홍길동', 'old': 30, 'address': '서울시 용산구 이촌동'}

personal_info(**x2)

# 자주 사용하는 딕셔너리 가변인수 활용
def personal_info(**kwargs):
    if 'name' in kwargs:    # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])

personal_info(**x)      # name, age, adderess가 다 있어서 출력
personal_info(**x2)     # age는 없어서 old는 제외되서 출력


# 위치 인수와 키워드 인수를 함께 사용

def custom_print(*args, **kwargs) :
    print(*args, **kwargs)


custom_print(1,2,3,sep = ':', end='')


# 매개변수에 초깃값 지정
def personal_info(name, age, address='비공개'):  # 매개변수 중 address의 초기값을 지정해줌,
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)


personal_info('홍길동', 30)     # 초기값으로 지정해서 address를 입력하지 않아도 '비공개'로 출력됨
personal_info('홍길동', 30,'용산구')    # 그렇지만 값을 넣어주면 넣어준 값으로 출력됨


# Unit 31 함수에서 재귀호출 사용하기

def hello():
    print('Hello, world!')
    hello()

hello()

def hello(count):
    if count == 0 :
        return

    print('Hello, world!', count)

    count -= 1
    hello(count)


hello(5)

# 재귀호출로 팩토리얼 구하기

def factorial(n) :
    if n == 1 :    # n = 1일때
        return 1   # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n-1) # n과 factorial 함수에 n-1을 넣어 반환한 값을 곱함


factorial(2)

# 등차수열

def ari_seq(n, d) :
    if n == 1 :
        return 1
    return ari_seq(n-1, d) + d

ari_seq(5,3)     # An = 5, 간격이 3인 등차수열


## Unit32 람다 표현식 사용하기

def plus_ten(x) :
    return x + 10

plus_ten(10)

lambda x : x + 10     # 이렇게 저장하면 함수 이름이 없어 불러올 수 없음

plus_ten = lambda x: x+10
plus_ten(1)

aa = ari_seq    # 위에서 지정한 등차수열의 함수를 aa로 지정이 가능
aa(5,3)


# 람다 표현식을 인수로 사용하기

def plus_ten(x) :
    return x +10


list(map(plus_ten, [1,2,3]))          # plus_ten의 함수를 지정 후 적용
list(map(lambda x:x+10, [1,2,3]))     # 함수를 사용하지 않고 바로 lambda함수를 적용 가능


# 람다 표현식과 map, filter, reduce 함수 활용하기
# 람다 표현식에 조건부 표현식 사용하기

# x % 3 ==0 이면 x를 str(문자열)로 만들어라
a = [1,2,3,4,5,6,7,8,9,10]
list(map(lambda x : str(x) if x % 3 == 0 else x, a))     # if 다음의 반환값이 if앞에 나옴

# map에 여러객체 넣기
a = [1,2,3,4,5]
b = [2,4,6,8,10]
list(map(lambda x, y : x * y, a,b))

#filter 사용하기

def f(x) :
    return x > 5 and x < 10


a = [8,3,2,10,15,7,1,9,0,11]
list(filter(f,a))                        # 함수식으로 filter사용

list(filter(lambda x : 5 < x <10, a))    # 람다식으로 filter 사용


# Unit 33 .클로저 사용하기

x = 10  # 전역 변수

def foo():
    print(x)  # 전역 변수 출력

foo()
print(x)  # 전역 변수 출력



# 클로저는 따로 공부할것..


# 함수안에서 함수 만들기

def print_hello() :
    hello = 'Hello, world!'
    def print_message():
        print(hello)
    print_message()

print_hello()

