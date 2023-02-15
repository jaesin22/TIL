import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
visited = [0] * N

def solve(start):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(start, N):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(i+1)
            solve(i + 1)
            visited[i] = 0
            arr.pop()

solve(0)