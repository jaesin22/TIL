import sys
input = sys.stdin.readline

L, C = map(int, input().split())
A = list(map(str, input().split()))
A.sort()
B = ['a','e','i','o','u']
arr = []

def tracking(start):
    if len(arr) == L:
        vo = 0
        co = 0
        for i in range(L):
            if arr[i] in B: 
                vo += 1
            else: 
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(arr))
            return
    
    for i in range(start, C):
        arr.append(A[i])
        tracking(i+1)
        arr.pop()


tracking(0)