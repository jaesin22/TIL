N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
arr = []
visited = [0] * N


def solved(start):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(start, N):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(A[i])
            solved(i + 1)
            visited[i] = 0
            arr.pop()

solved(0)