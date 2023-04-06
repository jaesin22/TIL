import sys
input = sys.stdin.readline
def dfs(start):
    global num

    for edge in graph[start]:
        if visited[edge] == 0 and edge != number[0]:
            visited[edge] = visited[start] + 1
            dfs(edge) 
    

N = int(input())
number = list(map(int, input().split()))
M = int(input())
graph = [[] * (N+1) for _ in range(N+1)]
num = 0
visited = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(number[0])

if visited[number[1]] == 0:
    print(-1)
else:
    print(visited[number[1]])