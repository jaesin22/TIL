N = int(input())
res = []
cnt = 1
for x in N:
    res.append(input())

for y in res:
    if cnt < y:
        cnt = cnt * 10

