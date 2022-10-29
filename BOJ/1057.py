import sys

n, kim, lim = map(int, sys.stdin.readline().split())
cnt = 0

while lim != kim:
    lim -= lim//2
    kim -= kim//2
    cnt += 1

print(cnt)