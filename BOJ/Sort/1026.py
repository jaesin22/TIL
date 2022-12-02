import sys
N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

def array(N, A, B):
    cnt = 0
    A.sort(reverse = True)
    B.sort()
    for x in range(N):
        cnt += A[x] * B[x]
    return cnt
    
print(array(N,A,B))