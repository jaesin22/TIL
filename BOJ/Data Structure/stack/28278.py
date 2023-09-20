import sys
from collections import deque
input = sys.stdin.readline
N =int(input())
stack = deque()

for i in range(N):
    order = list(map(int, input().split()))
    if order[0] == 1:
        stack.append(order[1])
    elif order[0] == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif order[0] == 3:
        print(len(stack))
    elif order[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 5:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])