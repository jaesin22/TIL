import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

blue, white = 0, 0

def solution(x, y, N):
    global blue, white
    color = board[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != board[i][j]:
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        white += 1
    else :
        blue += 1

solution(0,0,N)
print(white)
print(blue)

# 조건이 만족하지 않는 경우(색상이 모두 같은 경우가 아닌 경우)는 4개로 쪼개서 다시 푸는 방식
# 4개로 쪼개는 것은 재귀함수를 호출하여 풀고, 전달인자로 그 사분면의 가장 왼쪽 위의 좌표와 크기를 넣는다
#조건이 만족하는 경우(하나의 색상으로만 구성되는 경우)는 해당 색상의 값을 카운팅해준다