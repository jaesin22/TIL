import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
N, M = len(maps[0]), len(maps[1])
print(N, M)
def bfs(graph):
    queue = deque()
    queue.append((0, 0, 1))
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    
    while queue:
        a, b, c = queue.popleft()
        if a == N-1 and b == M-1:
            return c
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, c + 1))
                    
    return -1
    

def solution(maps):
    answer = bfs(maps)
    return answer

print(solution(maps))