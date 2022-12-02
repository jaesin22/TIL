import sys
input = sys.stdin.readline

n = int(input())
papers = []

for _ in range(n):
    row = list(map(int,input().rsplit()))
    papers.append(row)

blue_cnt, white_cnt = 0, 0

def check(row,col,n):
    global blue_cnt, white_cnt

    curr = papers[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if curr != papers[i][j]: # 현재 칸과 다른 색일 경우 1/4로 분할
                next_n = n // 2
                check(row, col, next_n)
                check(row, col + next_n, next_n)
                check(row + next_n, col, next_n)
                check(row + next_n, col + next_n, next_n)
                return
    if curr == 0:
        white_cnt += 1
    else:
        blue_cnt += 1
    return

check(0,0,n)
print(white_cnt)
print(blue_cnt)

# 조건이 만족하지 않는 경우(색상이 모두 같은 경우가 아닌 경우)는 4개로 쪼개서 다시 푸는 방식
# 4개로 쪼개는 것은 재귀함수를 호출하여 풀고, 전달인자로 그 사분면의 가장 왼쪽 위의 좌표와 크기를 넣는다
#조건이 만족하는 경우(하나의 색상으로만 구성되는 경우)는 해당 색상의 값을 카운팅해준다