N = int(input())
res = []
cnt = 0
for x in range(N):
    res.append(int(input()))

res.sort()

for i in range(N):
    cnt += abs(res[i] - (i + 1))

print(cnt)
