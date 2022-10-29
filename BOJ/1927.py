from queue import PriorityQueue
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
queue = []
for x in range(N):
    a = int(input())
    if a == 0:
        if len(queue) == 0:
            print(0)
            continue
        print(heappop(queue))
        continue
    heappush(queue, a)