col , row = map(int, input().split())

matrix = []
for a in range(row):
    matrix.append(list(input()))



def countMines(a, b):
    if matrix[a][b] == '*':            # matrix[][], 인덱스가 별이면 별을 반환(그대로 표시)
        return '*'

    count = 0
    for r in range(a - 1, a + 2):      # 입력되는 [a][b] 좌표의 주변값 -1~ +2 까지 matrix[r][c]가 == '*'이면 count에 1씩 더해서 누적
        for c in range(b - 1, b + 2):
            if r < 0 or c < 0 or r >= row or c >= col:
                continue
            if matrix[r][c] == '*':
                count += 1
    return count                       # 누적된 값을 반환


for l in range(row):                       # 입력한 가로 x 세로, row와 col의 좌표값 입력
    for p in range(col):
        print(countMines(l, p), end='')    # 만들어 함수(주변의 지뢰 개수 count 프린트
    print()
