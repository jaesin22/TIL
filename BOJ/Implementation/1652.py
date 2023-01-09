N = int(input())

graph = []
for _ in range(N):
    graph.append(input().strip())

x, y = 0, 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if graph[i][j] == '.':
            cnt += 1
        
        else:
            if cnt >= 2:
                x += 1
                cnt = 0
                continue
            else:
                cnt = 0
                continue
    if cnt >= 2:
        x += 1
        cnt = 0

for i in range(N):
    cnt = 0
    for j in range(N):
        if graph[j][i] == '.':
            cnt += 1

        else:
            if cnt >= 2:
                y += 1
                cnt = 0
                continue
            else:
                cnt = 0
                continue
    if cnt >= 2:
        y += 1
        cnt = 0

print(x, y)