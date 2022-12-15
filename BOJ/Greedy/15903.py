from heapq import heappush, heappop, heapify
N, M = map(int, input().split())
A = list(map(int, input().split()))


heapify(A)
for i in range(M):
    B = heappop(A) + heappop(A)
    for j in range(2):
        heappush(A, B)

print(sum(A))