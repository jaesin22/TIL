import sys
import heapq
input = sys.stdin.readline
N = int(input())
iterable = [list(map(int, input().split())) for _ in range(N)]

q = []
for i in iterable[0]:
    heapq.heappush(q, i)

for x in range(1, N):
    for y in iterable[x]:
        if q[0] < y:
            heapq.heappush(q, y)
            heapq.heappop(q)

print(q[0])


