import sys
from itertools import combinations
N = int(input())
arr = []

for _ in range(N):
    a, b = map(int, input().split())
    if N == 1:
        print(abs(a-b))
        sys.exit()
    arr.append((a, b))

combi = []
for i in range(1, N + 1):
    combi.append(combinations(arr, i))

res = []
for i in combi:
    for j in i:
        s, b = 1, 0
        for k in j:
            s *= k[0]
            b += k[1]
        
        res.append(abs(s - b))

print(min(res))