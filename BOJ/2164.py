import sys
from collections import deque
N = int(sys.stdin.readline())


deq = deque()
for x in range(1, N+1):
    deq.append(x)

for y in range(len(deq)):
    if len(deq) > 1:
        deq.popleft()
        deq.append(deq[0])
        deq.popleft()

print(deq[0])