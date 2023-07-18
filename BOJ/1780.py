import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

one, minus, zero = 0, 0, 0

def recursion(x, y, n):
    global minus, zero, one
    curr = graph[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if curr != graph[i][j]:
                temp = n // 3
                # 1, 2, 3
                recursion(x, y, temp)
                recursion(x, y + temp, temp)
                recursion(x, y + temp * 2, temp)
                # 4, 5, 6
                recursion(x+ temp, y, temp)
                recursion(x + temp, y + temp, temp)
                recursion(x + temp, y + temp * 2, temp)
                # 7, 8, 9
                recursion(x + temp * 2, y, temp)
                recursion(x + temp * 2, y + temp, temp)
                recursion(x + temp * 2, y + temp * 2, temp)
                return

    if graph[x][y] == 0: zero += 1
    elif graph[x][y] == 1: one += 1
    else: minus += 1
    return


recursion(0, 0, N)
print(minus, zero, one, sep='\n')