N = int(input())
res = []
cnt = 1
for x in N:
    res.append(input())

for y in res:
    inty = int(y)
    for i in range(len(y)):
        if cnt < inty:
            cnt = cnt * 10

