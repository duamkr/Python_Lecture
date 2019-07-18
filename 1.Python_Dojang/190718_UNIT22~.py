a = [10, 20, 30]
a.append(500)          # method  /  객체.method - 리스트 끝에 값 추가


# 약수구하기 , divisor = [] <- 빈 리스트 활용
divisor = []
n = 60

for i in range(1, n+1):
    if n % i == 0:
        divisor.append(i)

divisor

# 리스트 안에 리스트 생성
a.append([500,600])

# 리스트 끝에 리스트 연걸 .extend
a = [10,20,30]
a.extend([500,600])

# 리스트 특정 자리에 값 추가하기 .insert

a.insert(3,25)
a.insert(len(a),750)     # 맨뒤에 값 붙이기


## 리스트의 값을 삭제하는 방법들 .pop, .remove, del
# 리스트 특정위치 값 삭제
a.pop()     # 아무값도 넣지 않으면 맨 마지막 끝 값이 삭제됨
a.pop(0)    # 0번째 값 삭제

# 리스트 특정 값 삭제
a.remove(20)     # 20의 값 삭제
del a[1]         # del 명령어를 통해서도 pop()와 같이 삭제 가능


# 리스트 특정값의 인덱스 구하기
a = [10,20,30,40,50]
a.index(20)     # 리스트 a의 20의 값의 인덱스 산출

# 리스트 특정 값 개수 구하기
a.count(20)    # 20의 값이 몇개인지 산출

# 리스트 순서 뒤집기
a.reverse()

# 리스트 요소 정렬하기 오름차순 및 내림차순
a.sort()     # 오름차순
a.sort(reverse = True)     # 내림차순

# 리스트 복사
a = [10,20,30]
b = a.copy()

# 반복문으로 리스트의 요소를 출력
a = [38,21,53,62,19]


for i in a:     # for 반복문으로 출력
    print(i)

for element in a:     # element 로 출력
    print(element)

# 인덱스와 값 함께 출력하기
for index, value in enumerate(a):
    print(index, value)

# 인덱스와 값 함께 출력하기( 인덱스 번호 지정 가능)
for index, value in enumerate(a, start=101):
    print(index, value)


# 리스트의 max, min 값 구하기
min(a)
max(a)
sum(a)

# 리스트 표현식 사용하기 (if, for 반복문 등)
a = [i for i in range(10)]
b = list(i for i in range(10))
c = [i + 5 for i in range(10)]
d = [i * 2 for i in range(10)]
e = [i*i for i in range(10)]
e

# 리스트 표현식 사용하기 if문
a = [i for i in range(10) if i % 2 ==0]     # 2로 나눠지는 놈(짝수)만 가져와라
b = [i*i for i in range(10) if i % 2 ==1]   # 홀수의 제곱

# for 반복문과 if조건문 여러번 사용하기
m = [i * k for i in range(2,10) for k in range(1,10)]
m
# 리스트에 map사용하기

a = [1.2, 2.5, 3.7, 4.6]
b= list(map(int, a))     # b에 a의 값을 정수로 적용

a = input().split()




## Unit 23 . 2차원 리스트 사용하기

# 2차원 리스트 만들기
from pprint import pprint
a = [[10,20],
     [30,40],
     [50,60]]
a[0][0]
a[1][1]
a

#  2차원 리스트 출력
for i in a:
    print(i)


for i in a:
    for j in i:
        print(j, end=' ')
    print()


# a [] 빈리스트, line[]빈 리스트 활용 2차원 리스트 만들기
a = []
for i in range(3):
    line = []
    for k in range(2):
        line.append(0)
    a.append(line)

a = [[0 for k in range(2)] for i in range(3)]
b = [[0] * 2 for i in range(3)]


# 톱니형 리스트 만들기

a = [3,1,3,2,5]
b = []

for i in a:
    line = []
    for j in range(i):
        line.append(0)
        b.append(line)

print(b)

a = [[0] * i for i in [3, 1, 3, 2, 5]]


# sorted로 2차원 리스트 정렬하기
students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]

print(sorted(students, key=lambda student: student[1]))  # 안쪽 리스트의 인덱스 1을 기준으로 정렬
print(sorted(students, key=lambda student: student[2]))  # 안쪽 리스트의 인덱스 2를 기준으로 정렬


# 23.4 2차원 리스트의 할당과 복사 알아보기

# a = b 지정 후 2차원 리스트 값 변경시 둘다 변경됨
a = [[10, 20], [30, 40]]
b = a
b[0][0] = 500
a
b

# method 중 .copy로 2차원 리스트 복사 후 값 변경시 역시 둘다 변경됨
a = [[10, 20], [30, 40]]
b = a.copy()
b[0][0] = 500
a
b

# copy모듈 중 deepcopy() 함수를 사용해야 함
import copy
a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)
b[0][0] = 500
a
b


## Unit 24. 문자열 응용하기

# 문자열 변경하기
'Hello, world!' .replace('world', 'Python')

# 문자 변경하기
table = str.maketrans('aeiou', '12345')
'apple'.translate(table)

# 문자열 분리하기
'apple pear grape pineapple orange'.split()     # split로 공백으로 구분  = 값은 리스트로 저장됨
f= 'apple, pear, grape, pineapple, orange'.split(', ')    # split로 콤마로 구분  = 값은 리스트로 저장됨

# 문자열 연결하기 ,
' '.join(f)
'-'.join(f)


# 구두점을 간단하게 삭제하기

import string
string.punctuation
', python. '.strip(string.punctuation + ' ')     # + ' '공백도 추가 삭제
'^^^, python.!!!'.strip(string.punctuation).strip().upper()     #  -> 순서대로 하나씩 메소드가 적용 = method chaining

'I am %s.' % 'james'

# format 메서드로 여러값 넣기 {}{}{} 로 인덱스 순서를 지정가능
'Hello, {0} {2} {1}'.format('Python', 'Script', '.3.6')

