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
        arr.append(A[i])
        solved(i)
        arr.pop()

solved(0)