import sys
input = sys.stdin.readline
H, W = map(int, input().split())

graph = []
for _ in range(H):
    graph.append(input().rstrip())


visited = [[-1] * W for _ in range(H)]
for i in range(H):
    cloud = False
    cnt = 1
    for j in range(W):
        if graph[i][j] == 'c':
            cloud = True
            visited[i][j] = 0
            cnt = 1
        
        if graph[i][j] == '.' and cloud == True:
            visited[i][j] = cnt
            cnt += 1
        else:
            continue

for i in visited:
    for j in i:
        print(j, end =' ')
    print('')