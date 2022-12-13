import sys

N, K = map(int, sys.stdin.readline().split())
cnt = 0

coin = []
for x in range(N):
    A = int(sys.stdin.readline().rstrip())
    coin.append(A)

coin.sort(reverse=True)
for y in coin:
    cnt += K // y
    K %= y

print(cnt)
