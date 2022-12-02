N = int(input())

graph = []
for x in range(N):
    graph.append(list(map(int, input().split())))


white, blue = 0, 0
def recursion(x, y, n):
    global white, blue

    num = graph[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != graph[i][j]:
                slicer = n // 2
                recursion(x, y, slicer)
                recursion(x, y + slicer, slicer)
                recursion(x + slicer, y, slicer)
                recursion(x + slicer, y + slicer, slicer)
                return
    
    if num == 1: blue += 1
    else: white += 1
    return



recursion(0,0,N)
print(white)
print(blue)