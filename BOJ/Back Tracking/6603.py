import sys
input = sys.stdin.readline

def solve(start):
    if len(arr) == 6:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(start, len(A)):
        if visited[i] == 0:
            arr.append(A[i])
            visited[i] = 1
            solve(i)
            visited[i] = 0
            arr.pop()


while True:
    A = list(map(int, input().split()))
    D = A.pop(0)
    visited = [0] * len(A)
    if D == 0:
        sys.exit()
    
    arr = []
    solve(0)
    print()
