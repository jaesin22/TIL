from collections import deque

max = 10 ** 5
n, k = map(int, input().split())
visited = [0] * (max + 1)

def BFS():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x])
            break
        
        for nx in (x-1, x+1, x * 2):
            if 0 <= nx <= max and not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)


BFS()