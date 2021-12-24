import sys
from collections import deque

N = int(sys.stdin.readline())
d = deque([0] * (N+1))

d[0] = 0
d[1] = 1
d[2] = 1
for x in range(3, N+1):
    if d[x] != 0:
        d[x] = d[x]
    d[x] = d[x - 1] + d[x - 2]


print(d[N] % 1000000007)
