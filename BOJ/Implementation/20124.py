import sys
input = sys.stdin.readline

N = int(input())
res = []
cnt = 0

for _ in range(N):
    a, b = map(str, input().split())
    res.append((a, int(b)))
    if int(b) > cnt:
        cnt = int(b)

res.sort(key=lambda x: x[1], reverse=True)

name = []
for i, j in res:
    if j == cnt:
        name.append(i)

name.sort()
print(name[0])