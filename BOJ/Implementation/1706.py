import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
for i in range(R):
    graph.append(input().strip())

res = []
for i in range(R):
    str = ''
    for j in range(C):
        if graph[i][j] == '#':
            res.append(str)
            continue
        str += graph[i][j]
        
    res.append(str)

for i in range(C):
    str = ''
    for j in range(R):
        if graph[j][i] == '#':
            res.append(str)
            continue
        str += graph[j][i]
    
    res.append(str)


C = list(set(res))
result = []
for i in C:
    if len(i) > 1:
        result.append(i)

result.sort()
print(result[0])