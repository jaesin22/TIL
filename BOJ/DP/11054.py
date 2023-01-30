import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dpup = [0] * N
dpdown = [0] * N
sumdp = [0] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dpup[i] = max(dpup[i], dpup[j])
    dpup[i] += 1

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            dpdown[i] = max(dpdown[i], dpdown[j])
    dpdown[i] += 1

for i in range(N):
    sumdp[i] = dpup[i] + dpdown[i] - 1

# print(dpup)
# print(dpdown)
print(max(sumdp))