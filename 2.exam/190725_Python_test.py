# 3. 두개의 정수를 입력받아 작은수에서부터 큰 수까지(큰수 포함)홀수의 합

a,b = map(int,input().split())

ab_sum = 0
for i in range(a,b+1):
    if i % 2 == 1:
        ab_sum += i
print(ab_sum)


# 4. 연 복리 이자율을 입력받아(단위%) 원금의 2배가 되는데 최소 몇년이 걸리는지 알아보는 프로그램 while loop






# 5. bts 리스트가 주어졌을때 아래와 같은 답이 나오도록 print 문을 작성하시오
bts = ['RM','진','슈가', '제이홉', '지민', '뷔', '정국']
print(bts[5])
print("["+"'"+bts[0]+"'", end = ']')
print("["+"'"+bts[5]+"'","'"+bts[6], sep=', ', end = ']')
print("["+"'"+bts[2]+"'","'"+bts[3]+"'","'"+bts[4]+"'", sep=', ', end = ']')
print("["+"'"+bts[0]+"'","'"+bts[2]+"'","'"+bts[5]+"'","'"+bts[6]+"'", sep=', ', end = ']')

# 6. 다음과 같은 딕셔너리 vegetables가 주어졌을때 내림차순으로 출력, 가격의 길이 7, 1000단위 , 찍은뒤 우측정렬..

vegetables = {'가지': 800, '오이':600, '수박':15000., '호박':1000, '깻잎':500}
vvv = vegetables

for key, value in vegetables.items():
     print(key, value)


vegetables['가지'] = '800'.rjust(7)
vegetables['오이'] = '600'.rjust(7)
vegetables['수박'] = '15000'.rjust(7)
vegetables['호박'] = '1000'.rjust(7)
vegetables['깻잎'] = '500'.rjust(7)
vegetables

map(dict(vegetables,rjust(7)))


# 7 앞에서부터 읽을때나 뒤에서부터 읽을때나 모양이 같은 대칭수 , 세자리 수 대칭수

for i in range(101,1000) :
    for k in range(i, 1000):
        result = i * k
        word = str(result)
            if word == ''.join(reversed(word)):
                maxword = i * k
                aword = i
                bword = k

print(maxword, aword, bword)

# 8. 다음의 규칙대로 동작하는 프로그램을 작성하시오
row , col= map(int, input().split())

matrix = []
for a in range(row):
    matrix.append(list(input()))


def pang(a, b):
    for r in range(a - 1, a + 1):      # 입력되는 [a][b] 좌표의 주변값 -1~ +2 까지 matrix[r][c]가 == '*'이면 count에 1씩 더해서 누적
        for c in range(b - 1, b + 1):
            if matrix[r][c] == matrix[r-1][c] and matrix[r+1][c]:
                return '*'
            if matrix[r][c] == matrix[r][c-1] and matrix[r][c+1]:
                return '*'


for l in range(row):                       # 입력한 가로 x 세로, row와 col의 좌표값 입력
    for p in range(col):
        print(pang(l, p), end='')    # 만들어 함수(주변의 지뢰 개수 count 프린트
    print()


# 9. 다음과 같은 리스트 a가 주어졌을때 a의 각 원소를 제곱한 값을 원소로 갖는 리스트 b를 람다표신식을 사용하여 구하시오

a=[1,3,5,7,9]
b_list = list(map(lambda x : x ** 2, a))





