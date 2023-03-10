import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort()
res = []
for i in arr:
    cnt = 0
    for j in range(i, i + 5):
        if j not in arr:
            cnt += 1

    res.append(cnt)

print(min(res))