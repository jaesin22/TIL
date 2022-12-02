from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque()
queue.append((N, 0))
graph = [-1] * 100001
graph[N] = 0
res = []
while queue:
    target, cnt = queue.popleft()

    if target == K:
        break

    for i in(target + 1, target - 1, target*2):
        if 0 <= i < 100001 and graph[i] == -1:
            # 순간이동 일 때
            if i == target * 2:
                graph[i] = graph[target] + 1
                queue.appendleft((i, cnt + 1))
                
            else:
                graph[i] = graph[target] + 1
                queue.append((i, cnt + 1))

print(cnt)
print(res)