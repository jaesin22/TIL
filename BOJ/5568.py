import sys
from itertools import permutations

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

res = []
arr = []
for x in range(N):
    res.append(sys.stdin.readline().rstrip())


for y in permutations(res, K):
    arr.append(''.join(y))

arr = set(arr)
print(len(arr))