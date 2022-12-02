import sys
input = sys.stdin.readline

N = int(input())
graph = []
for x in range(N):
    graph.append(list(map(int, input().split())))


minus, zero, plus = 0,0,0

def recursion(x, y, n):
    global minus, zero, plus
    current = graph[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if current != graph[i][j]:
                next_n = n // 3
                # 1, 2, 3
                recursion(x, y, next_n)
                recursion(x, y + next_n, next_n)
                recursion(x, y + next_n*2, next_n)
                # 4, 5, 6
                recursion(x + next_n, y, next_n)
                recursion(x + next_n, y + next_n, next_n)
                recursion(x + next_n, y + next_n * 2, next_n)
                # 7, 8, 9
                recursion(x + next_n * 2, y, next_n)
                recursion(x + next_n * 2, y + next_n, next_n)
                recursion(x + next_n * 2, y + next_n * 2, next_n)
                return
    if graph[x][y] == -1: minus += 1
    elif graph[x][y] == 0: zero += 1
    else: plus += 1
    return



recursion(0,0,N)
print(minus, zero, plus, sep='\n')