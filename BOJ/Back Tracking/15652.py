N, M = map(int, input().split())
arr = []
visited = [0] * N


def solved(start):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, N):
        arr.append(i+1)
        solved(i)
        arr.pop()

solved(0)