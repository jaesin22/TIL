import sys
sys.setrecursionlimit(10 ** 8)

def dfs(x, y):
    if 0 <= x < h and 0 <= y < w:
        if graph[x][y] == 1:
            graph[x][y] = 3
            dfs(x - 1, y - 1)
            dfs(x - 1, y)
            dfs(x - 1, y + 1)
            dfs(x, y - 1)
            dfs(x, y + 1)
            dfs(x + 1, y - 1)
            dfs(x + 1, y)
            dfs(x + 1, y + 1)
            return True
        return False


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0 : break
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
