N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
arr = []
visited = [0] * N

def solved(start):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(N):
        if visited[i] == 0:
            arr.append(A[i])
            visited[i] = 1
            solved(i + 1)
            visited[i] = 0
            arr.pop()

solved(0)