import sys
input = sys.stdin.readline
from itertools import combinations

res = int(1e9)
N, M = map(int, input().split())
graph = []

house = []
chicken = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i, j))
        if graph[i][j] == 2:
            chicken.append((i, j))


for i in combinations(chicken, M):
    temp = 0
    for nx, ny in house:
        len_chicken = int(1e10)
        # 각 집마다 M번 만큼
        for j in range(M):
            len_chicken = min(len_chicken, abs(nx - i[j][0]) + abs(ny - i[j][1]))
        # 제일 최소값 추가
        temp += len_chicken
    res = min(res, temp)

print(res)