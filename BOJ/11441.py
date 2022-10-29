import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
S = [0] * (N+1)
for i in range(len(A)):
    S[i] = S[i-1] + A[i]

for x in range(M):
    a, b = map(int, input().split())
    print(S[b-1] - S[a-2])
