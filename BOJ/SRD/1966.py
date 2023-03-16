from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0
    compare = queue[M]
    idx = [i for i in range(N)]
    idx[M] = "!"

    while queue:
        if queue[0] == max(queue):
            cnt += 1
            if idx[0] == "!":
                print(cnt)
                break
            queue.popleft()
            idx.pop(0)
        else:
            queue.append(queue.popleft())
            idx.append(idx.pop(0))
