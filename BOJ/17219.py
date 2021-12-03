import sys
input = sys.stdin.readline

N, M = map(int, input().split())

res = {}

for x in range(N):
    a, b = input().split()
    res[a] = b

for _ in range(M):
    k = input().rstrip()
    print(res[k])

