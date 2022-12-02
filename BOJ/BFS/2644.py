import sys
from collections import deque

def bfs(v, target):
    # queue에 정점과 cnt를 넣어줌
    queue = deque([[v,0]])

    while queue:
        temp = queue.popleft()
        v = temp[0]
        cnt = temp[1]

        if v == target:
            return cnt
        # 방문 안한 정점이면 방문해준다.
        if not visited[v]:
            visited[v] = True
            # 해당 정점과 연결된 정점들 중에 방문 안한 정점이 있으면 queue에 추가
        for i in graph[v]:
            if not visited[i]:
                queue.append((i, cnt + 1))
    # 해당 정점과 연결된 모든 정점을 확인했는데 target을 찾지 못했으면
    # 연결되지 않았으므로 촌수를 계산할 수 없음       

    return -1

# 전체 사람의 수 n, 우리가 촌수를 구해야 하는 사람 q1, q2
n = int(input())
q1, q2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    # x가 y의 부모
    x, y = map(int, input().split())

    # 양방향 그래프 추가
    graph[x].append(y)
    graph[y].append(x)

print(bfs(q1, q2))