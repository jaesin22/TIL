import math
N = int(input())
count = math.factorial(N)
visited = [0] * (N+1)
arr = []

def recursion(start):
    if len(arr) == N:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(i)
            recursion(i)
            arr.pop()
            visited[i] = 0


recursion(1)