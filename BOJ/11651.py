N = int(input())
res = []
for i in range(N):
    x, y = map(int, input().split())
    res.append([x,y])

res.sort(key = lambda x : (x[1], x[0]))

for i in range(N):
    print(res[i][0], res[i][1])