import sys
input = sys.stdin.readline

def recursion(x, y, n):
    global A
    current = graph[x][y]
    if n == 1:
        A += graph[x][y]
        return

    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != current:
                temp = n // 2
                A += '('

                recursion(x, y, temp)
                recursion(x, y + temp, temp)
                recursion(x + temp, y, temp)
                recursion(x + temp, y + temp, temp)
                A += ')'
                return

    A += current
    return



N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(str, input().rstrip())))
A = ''

recursion(0,0,N)
print(A)