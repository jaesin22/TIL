from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
N, M = 5, 5
graph = [list(map(int, input().split())) for _ in range(5)]
res = set()

def search(x, y, string):
    string += str(graph[x][y])

    if len(string) == 6:
        res.add(string)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            search(nx, ny, string)
                
        


for i in range(N):
    for j in range(M):
        search(i, j, '')

print(len(res))