import sys
import heapq
N = int(sys.stdin.readline())

res = []
for _ in range(N):
    M, K = map(int, sys.stdin.readline().split())
    res.append([M, K])

res.sort()

room = []
for start, end in res:
    if room and room[0] <= start:
        heapq.heappop(room)
    heapq.heappush(room, end)

print(len(room))