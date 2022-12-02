import sys
input = sys.stdin.readline
N = int(input())
res = []
cnt = 1
for x in range(N):
    a, b = map(int, input().split())
    res.append([a, b])

res.sort(key=lambda x:(x[1],x[0]))
end_time = res[0][1]

for y in range(1, N):
    if res[y][0] >= end_time :
        cnt += 1
        end_time = res[y][1]

print(cnt)