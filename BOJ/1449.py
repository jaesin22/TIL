import sys
N, L = map(int, sys.stdin.readline())
loc = list(int, sys.stdin.readline())

cnt = 0
loc.sort()

for x in range(N):
    if 