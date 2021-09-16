import sys

N = int(sys.stdin.readline())
res = []
for x in range(N):
    C = int(input())
    res.append(C)


res.sort(reverse=True)
cnt = 0
for i in range(2, len(res), 3):
    cnt += res[i]

print(sum(res) - cnt)