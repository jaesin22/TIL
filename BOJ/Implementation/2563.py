N = int(input())

visited = [[0] * 100 for _ in range(100)]
for i in range(N):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            visited[i][j] = 1

res = 0
for i in visited:
    res += sum(i)

print(res)


