from collections import deque

N = int(input())
card = [(i+1) for i in range(N)]
queue = deque(card)

while len(queue) > 1:
    A = queue.popleft()
    B = queue.popleft()
    queue.append(B)

print(queue[0])