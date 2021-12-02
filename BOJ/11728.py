import sys

input = sys.stdin.readline


N, M = map(int, input().split())


A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = A + B
res.sort()

for x in res:
    print(x, end=' ')
