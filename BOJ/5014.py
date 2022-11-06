import sys
input = sys.stdin.readline
from collections import deque


F, S, G, U, D = map(int, input().split())
queue = deque()
queue.append((S, 0))

visited = [0]* (F+1)
visited[S] = 1
res = F

while queue:
    s, cnt = queue.popleft()

    if s == G:
        res = min(res, cnt)
        break
    
    if s + U <= F and not visited[s+U]:
        visited[s+U] = 1
        queue.append((s + U , cnt + 1))
    if s - D >= 1 and not visited[s-D]:
        visited[s-D] = 1
        queue.append((s-D, cnt + 1))
    

if res == F:
    print("use the stairs")
else:
    print(res)