N, X = map(int, input().split())
A = list(map(int, input().split()))
res = []

for i in A:
    if i < X:
        res.append(i)

for y in res:
    print(y, end=' ')

