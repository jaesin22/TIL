import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
see = deque()
hear = deque()
cnt = 0

for _ in range(a):
    see.append(sys.stdin.readline().rstrip())

for _ in range(b):
    hear.append(sys.stdin.readline().rstrip())

res = list(sorted(set(hear).intersection(see)))

print(len(res))

for i in res:
    print(i)