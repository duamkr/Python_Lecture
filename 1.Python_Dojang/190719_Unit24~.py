print('hello')

# setdefault: 키-값 쌍 추가
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
x
x.setdefault('f',100)
x
# update: 키의 값 수정, 키가 없으면 키-값 쌍 추가
x.update(e=90)    # key 값이 문자열인 경우, update 할땐 e 에 '를 붙이지 않음
x.update(a=900, f=60)
y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})     # key 값이 문자열이 아닌 경우, 딕셔너리처럼 값을 넣어서 수정해야함
y
y.update([[2, 'TWO'], [4, 'FOUR']])
y


# 딕셔너리에서 키-값 쌍 삭제하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')
x

# 딕셔너리에서 임의의 키-값 쌍 삭제하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.popitem()

# 딕셔너리에서 키값 가져오기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.get('a')

x.items()   # items 는 딕셔너리의 key-value을 모두 가져옴
x.keys()    # keys 는 딕셔너리의 key만 가져옴
x.values()  # value 는 딕셔너리의 value 값만 가져옴

# 리스트와 튜플로 딕셔너리 만들기
keys = ['a', 'b', 'c', 'd']    # keys변수에 값을 지정
x = dict.fromkeys(keys)        # dict.fromekeys() 를 통해 값이 없는 딕셔너리 생성
x
y = dict.fromkeys(keys,100)    # 키변수와 100(value값)을 같이 지정하면 key와 value값을 같이 지정 가능
y


# defaultdict 사용하기 # defaultdict는 없는 키에 접근하더라도 에러가 발생하지 않으며 기본값을 반환
# defaultdict(기본값생성함수)
from collections import defaultdict
y = defaultdict(int)
y['z']    # z값이 없지만 z를 입력하면 key가 생성되고, 기본값 int로 지정한 value값 0이 반영됨
y['a']
y['b']
# lambda 함수 익명함수
z = defaultdict(lambda: 'python')     # lambda 함수로 z의 value값을 'python'으로 지정 후 값이 python으로 입력됨
z['a']
z[0]
z


# 딕셔너리의 값 가져오기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# 딕셔너리의 key 출력
for i in x :
    print(i)

for key in x.keys():
    print(key)

# 딕셔너리의 key, value값 둘다 가져오기, items()
for key, value in x.items():
    print(key,value)

# 딕셔너리의 value값 가져오기

for value in x.values():
    print(value, end =' ')

# 딕셔너리의 표현식 사용하기

keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
x = {key : None for key in keys}

# 딕셔너리 표현식에서 if 조건문 사용하기

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

for key, value in x.items():
    if value == 20 :
        del x[key]

print(x)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
x

# 세트 만들기

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
fruits2 = {'orange', 'orange', 'cherry'}     # 중복값은 삭제
fruits2

'orange' in fruits    # fruits안에 orange가 있는지 확인 / true , false로 구분
a = set('apple')
a
c =set()     # 빈 껍데기 set 만드는 식
set('유아낫에브띵별처럼쏟아지는운명에')


# 연산 집합 사용하기

# .union () 합집합
a = {1,2,3,4}
b = {3,4,5,6}
set.union(a,b)
a | b

# .intersection() 교집합
set.intersection(a,b)
a & b

# 차집합 , set - set
a - b

# 대칭차집합 = setsymmetric_difference 메서드와 동일

a ^ b


# 세트가 같은지 다른지
a = {1,2,3,4}
a == {1,2,3,4}
a == (4,2,3,1)

a.remove(3)    # remove는 값이 없으면 오류
a.discard(3)   # discard는 값이 없으면 오류 패스

a.clear        # a의 모든것을 clear





## Unit 27.  파일 사용하기
import os
os .getcwd()
os.chdir("c:\Temp")
os.getcwd()

# 파일을 열고, write로 입력
file = open('hello.txt','w')
file.write('Hello, world!')
file.close()

# 파일을 열고 read() 출력
file = open('hello.txt', 'r')
s = file.read()
s
file.close()

# 자동으로 파일 객체 닫기 / with open
with open('hello.txt','r') as file :
    s = file.read()
    print(s)


# 반복문으로 무자열 여러줄을 파일에 쓰기
with open('hello.txt', 'w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))

# 리스트에 있는 문자열 파일에 쓰기

lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

with open('hello.txt', 'w') as file :
    file.writelines(lines)


# 파일의 내용을 한줄씩 리스트로 가져오기

with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    lines = file.readlines()
    print(lines)

# 파일의 내용을 한 줄씩 읽기 while 문

with open('hello.txt','r') as file :
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))

# 파일의 내용을 한 줄씩 읽기 for 반복문

with open('hello.txt','r') as file :
    for line in file :
        print(line.strip('\n'))

# 파이썬 객체를 파일에 저장하기

import pickle

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

with open('james.p', 'wb') as file:  # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)


# 파일에서 파이썬 객체 읽기
import pickle

with open('james.p', 'rb') as file:  # james.p 파일을 바이너리 읽기 모드(rb)로 열기
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)

os.mkdir('help')     # 디렉토리에 help폴더 생성
os.listdir()         # 디렉토리 리스트 출력


# 회문판별

word = input('단어를 입력하시오')

word = word.upper()
is_palindrome = True
for i in range(len(word) // 2) :
    if word[i] != word[-1 -i]:
        is_palindrome = False
        break
print(is_palindrome)

# 반복문으로 N-gram만들기

text = 'Hello'

for i in range(len(text) - 1):  # 2-gram이므로 문자열의 끝에서 한 글자 앞까지만 반복함
    print(text[i], text[i + 1], sep='')