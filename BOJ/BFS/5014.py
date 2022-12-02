import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)
visited[S] = 1
queue = deque()
queue.append((S, 0))

res = F
while queue:
    s, cnt = queue.popleft()

    if s == G:
        res = min(res, cnt)
        break

    if s+U <= F and visited[s+U] == 0:
        visited[s+U] = 1
        queue.append((s+U, cnt+1))
    if s-D >= 1 and visited[s-D] == 0:
        visited[s-D] = 1
        queue.append((s-D, cnt+1))

    

if F == res:
    print("use the stairs")
else:
    print(res)