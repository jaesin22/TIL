import sys
input = sys.stdin.readline

L, C = map(int, input().split())
A = list(map(str, input().split()))
visited = [0] * C
arr = []
A.sort()
def solve(start):

    if len(arr) == L:
        vo = 0
        co = 0
        for i in range(L):
            if arr[i] in 'aeiou': 
                vo += 1
            else: 
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(arr))
            return
    
    for i in range(start, C):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(A[i])
            solve(i)
            visited[i] = 0
            arr.pop()

solve(0)