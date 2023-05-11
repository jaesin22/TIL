n = int(input())
answer = [[0] * i for i in range(1, n+1)]
cnt = 1
dx = [1,0,1]
dy = [0,1,-1]

def recursion(cnt, n):
    global answer
    for i in range(n-1):
        answer[i][0] = cnt
        cnt += 1
    for j in range(n-1):
        answer[n-1][j] = cnt
        cnt += 1
    for k in range(n-1, 0, -1):
        answer[k][k] = cnt
        cnt += 1



recursion(cnt, n)

for _ in answer:
    print(_)