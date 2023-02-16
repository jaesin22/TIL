N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
arr = []
visited = [0] * N

def solved(start):
    if len(arr) == M:
       print(*arr)
       return
    
    curr = 0
    for i in range(start, N):
        if A[i] != curr:
            arr.append(A[i])
            curr = A[i]
            solved(i)
            arr.pop()


solved(0)