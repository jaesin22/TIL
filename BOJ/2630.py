import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

white, blue = 0, 0

def recursion(x, y, n):
    global white, blue
    current = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if current != graph[i][j]:
                temp = n // 2

                recursion(x, y, temp) # 1
                recursion(x, y + temp, temp)
                recursion(x + temp, y, temp)
                recursion(x + temp, y + temp, temp)
                return

    if current == 1: blue += 1
    else: white += 1
    return

recursion(0,0,N)
print(white)
print(blue)