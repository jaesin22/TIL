import sys

input = sys.stdin.readline
N = int(input())
res = []
array = []
for x in range(N):
    x, y = map(int, input().split())
    res.append([x,y])


for i in range(N):
    cnt = 0
    for j in range(N):
        if res[i][0] < res[j][0] and res[i][1] < res[j][1]:
            cnt += 1
    array.append(cnt + 1)

for a in array:
    print(a, end = ' ')
            