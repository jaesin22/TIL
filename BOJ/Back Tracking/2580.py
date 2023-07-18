import sys
input = sys.stdin.readline

graph = [list(map(str, input().split())) for _ in range(9)]
visited = [(i, j) for i in range(9) for j in range(9) if graph[i][j] == 0]


def chk(x, y):
    numbers = [i+1 for _ in range(9)]

    for i in range(9):
        if graph[x][i] in numbers:
            numbers.remove(graph[x][i])
        if graph[i][y] in numbers:
            numbers.remove(graph[i][y])

    x1 = (x // 3) * 3
    y1 = (y // 3) * 3

    for i in range(x1, x1 + 3):
        for j in range(y1, y1 + 3):
            if graph[i][j] in numbers:
                numbers.remove(graph[i][j])
    
    return numbers
    
flag = False

def solve(start) :
    global flag
    if flag:
        return

    if start == len(visited):
        for i in graph:
            print(*i)
        flag = True
        return

    r, c = visited[start]
    func = chk(r, c)

    for i in func:
        graph[r][c] = func
        solve(start + 1)
        graph[r][c] = 0

solve(0)