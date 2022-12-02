import sys
input = sys.stdin.readline

N = int(input())
res = []
for x in range(N):
    res.append(list(map(int, input().split())))

k = 2
for i in range(1, N):
    for j in range(k):
        if 