def ten_div(X):
    return 10 / x

# 특정 예외만 처리하기

y = [10,20,30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
except IndexError:           # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
    print('잘못된 인덱스입니다.')




# 예외와는 상관없이 항상 코드 실행하기

try :
    x = int(input('나눌 숫자를 입력'))
    y = 10 / x
except ZeroDivisionError:
    print('숫자를 0으로 나눌 수 없습니다.')
else :
    print(y)
finally :          # 예외 발생여부에 상관없이 항상 코드를 실행하는 finally
    print('코드 실행이 끝났습니다.')


# 예외 발생시키기 : Raise

try :
    x = int(input('3의 배수를 입력하세요'))
    if x % 3 != 0:
        raise Exception('3의 배수가 아닙니다.')
    print(x)
except Exception as e :
    print('예외가 발생했습니다.', e)

