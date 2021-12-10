import heapq
import sys

input = sys.stdin.readline
heap = []
heapq.heapify(heap)
N = int(input())
array = []

for i in range(N):
    array.append(int(input()))

for x in array:
    if x == 0 and len(heap) == 0:
        print(0)
    elif x == 0:
        print(abs(heapq.heappop(heap)))
    else:
        heapq.heappush(heap,  -x)