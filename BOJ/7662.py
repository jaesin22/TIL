import heapq
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap) # [1, 3, 7, 4]

for i in range(4):
    print(heapq.heappop(heap[-1]))
# 1
# 3
# 4
# 7