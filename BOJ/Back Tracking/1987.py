import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]
R, C = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(R)]
arr = set()
arr.add(graph[0][0])
res = -int(1e9)

def dfs(x, y, cnt):
    global res
    res = max(res, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if graph[nx][ny] not in arr:
                arr.add(graph[nx][ny])
                dfs(nx, ny, cnt+1)
                arr.remove(graph[nx][ny])
    return

dfs(0,0,1)
print(res)