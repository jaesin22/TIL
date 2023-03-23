import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
arr = deque()
graph = [[[] for _ in range(N)] for _ in range(N)]
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    arr.append((r-1, c-1, m, s, d))

for _ in range(K):
    # 파이어 볼 이동
    while arr:
        cr, cc, cm, cs, cd = arr.popleft()
        nr = (cr + cs * dx[cd]) % N  # 1번-N번 행 연결되어있기 때문
        nc = (cc + cs * dy[cd]) % N
        graph[nr][nc].append((cm, cs, cd))

    for i in range(N):
        for j in range(N):
            # 2개 이상인 경우 -> 4개의 파이어볼로 쪼개기
            if len(graph[i][j]) > 1:
                sum_m, sum_s, odd, even, cnt = 0, 0, 0, 0, len(graph[i][j])
                while graph[i][j]:
                    nm, ns, nd = graph[i][j].pop(0)
                    sum_m += nm
                    sum_s += ns
                    if nd % 2:
                        odd += 1
                    else:
                        even += 1
                
                if odd == cnt or even == cnt: # 모두 홀수거나 짝수인 경우
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                
                if sum_m // 5 : #질량 0이면 소멸
                    for d in nd:
                        arr.append((i, j, sum_m // 5, sum_s // cnt, d))

            if len(graph[i][j]) == 1:
                arr.append((i, j) + graph[i][j].pop())


res = 0
for i in arr:
    res += i[2]
    
print(res)