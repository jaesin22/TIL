from collections import deque
N, K = map(int, input().split())

res = list(range(1, N+1))

for x in res:
    deque.push(x)
