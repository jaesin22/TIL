import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
visited = [0] * (N+1)

def solve():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(N):
        arr.append(i+1)
        solve()
        arr.pop()

solve()