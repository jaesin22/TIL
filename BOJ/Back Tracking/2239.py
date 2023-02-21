import sys
input = sys.stdin.readline

graph = [list(map(int, input().rstrip())) for _ in range(9)]
visited = []
for i in range(9):
    graph.append(list(map(int, input().rstrip())))
    for j in range(9):
        if graph[i][j] == 0:
            visited.append((i, j))

def dfs(x, y):
    numbers = [(i+1) for i in range(9)]

    for i in range(9):
        if graph[x][i] in numbers:
            numbers.remove(graph[x][i])
        if graph[i][y] in numbers:
            numbers.remove(graph[i][y])

    x1 = (x // 3) * 3
    y1 = (y // 3) * 3

    for i in range(x1, x1+3):
        for j in range(y1, y1+3):
            if graph[i][j] in numbers:
                numbers.remove(graph[i][j])
    
    return numbers

flag = False

def solve(start):
    global flag
    if flag:
        return
    if start == len(visited):
        for i in graph:
            print(*i, sep="")
        flag = True
        return

    r, c = visited[start]
    for i in dfs(r, c):
        graph[r][c] = i
        solve(start + 1)
    graph[r][c] = 0

solve(0)