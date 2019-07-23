n = int(input('10~30값 입력하시오'))

def bo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return bo(n - 1) + bo(n - 2)

bo(10)




