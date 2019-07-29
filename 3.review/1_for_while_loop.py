# for 반복문
## 횟수를 정해 반복문을 돌리는 경우 for 반복문 사용
for i in range(10) :
    print(i)
    print("안녕 제비야 박씨를 물어다줘")
    print("내가 한가해 보이니 나도 세계 곳곳을 돌아다녀야해")


for i in range(100) :
    print(i)
    print("안녕 제비야 박씨를 물어다줘")
    print("내가 한가해 보이니 나도 세계 곳곳을 돌아다녀야해")

    if i > 10 :      # i 가 10보다 커지면 break해라 (100번 반복으로 정햇지만 아래 if조건문에 맞춰 break됨
        break


for i in range(3) :
    print(i)
    print("안녕 제비야 박씨를 물어다줘")
    print("내가 한가해 보이니 나도 세계 곳곳을 돌아다녀야해")

    if i == 1 :      # continue가 보이면 첫번째 루프로 돌아 , 특정 조건에선 보이지 않게 할때 사용함, 여기선 i == 1일때는 "안녕 나는 진영이야"라는 문장은 보이지 않음
        continue
    print("안녕 나는 진영이야")


for i in range(100) :
    print(i)
    if i % 2 == 0 :
        print("안녕 나는 짝수야")
    elif i == 77 :
        print("안녕 나는 행운의 숫자!")
    else :
        print("안녕 나는 홀수야")



# while 반복문(무한loop) , break, continue
i = 0
while i < 3:
    print(i)     # loop를 돌리는 i를 print
    print("안녕 제비야 박씨를 물어다줘")
    print("내가 한가해 보이니 나도 세계 곳곳을 돌아다녀야해")
    i = i + 1    # while 의 조건 중 i > 3 보다 작으면 loop 반복, 한번 돌떄마다 i + 1 을 해서 0으로부터 시작한 i는 한번 돌면 1이되고 2번돌면 2가되는 조건임

i = 0
while True :
    print(i)  # loop를 돌리는 i를 print
    print("안녕 제비야 박씨를 물어다줘")
    print("내가 한가해 보이니 나도 세계 곳곳을 돌아다녀야해")
    i = i + 1


    if i > 2:     # i 가 2보다 커지면 break 걸어라
        break




a,b,c = map(int, input().split())


def baseball (a,b,c) :




