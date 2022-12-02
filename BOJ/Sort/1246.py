n, m = map(int, input().split())
res = []

for _ in range(m):
    res.append(int(input()))

res.sort()

price, ans = 0,0

for i in range(m):
    result = min(m-i, n)
    if ans < res[i] * result:
        price = res[i]
        ans = res[i] * result


print(price, ans)