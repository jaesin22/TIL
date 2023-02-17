N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
visited = [0] * N

def solve(start, depth):
    global diff
    if depth == N // 2:
        a, b = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] == 1 and visited[j] == 1:
                    a += graph[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    b += graph[i][j]
        diff = min(diff, abs(a - b))
        return

    for i in range(start, N):
        if visited[i] == 0:
            visited[i] = 1
            solve(i + 1, depth + 1)
            visited[i] = 0

diff = int(1e9)
solve(0, 0)
print(diff)