from collections import deque
N = int(input())
queue = deque()
for i in range(1, N + 1):
    queue.append(i)

res = []
while queue:
    res.append(queue.popleft())

    if len(queue) == 0:
        break

    queue.append(queue.popleft())

print(" ".join(map(str, res)))