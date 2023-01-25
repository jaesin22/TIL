import sys
input = sys.stdin.readline



def divstar(graph, x, y, n):
    temp = n // 3
    star(graph, x, y, temp)
    star(graph, x, y + temp, temp)
    star(graph, x, y + temp * 2, temp)
    star(graph, x + temp, y, temp)
    blank(graph, x + temp, y + temp, temp)
    star(graph, x + temp, y + temp * 2, temp)
    star(graph, x + temp * 2, y, temp)
    star(graph, x + temp * 2, y + temp, temp)
    star(graph, x + temp * 2, y + temp * 2, temp)


def blank(graph, x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            graph[i][j] = ' '

def star(graph, x, y, n):
    if n == 1:
        return
    
    divstar(graph, x, y, n)


N = int(input())
graph = [['*'] * N for _ in range(N)]

divstar(graph, 0, 0, N)

for i in range(N):
    for j in range(N):
        print(graph[i][j], end='')
    print()
