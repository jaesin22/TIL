N = int(input())
M = int(input())


res = list()

for x in range(N, M+1):
    cnt = 0
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                cnt += 1
                break
        if cnt == 0:
            res.append(x)


if len(res) > 0:
    print(sum(res))
    print(min(res))

else:
    print(-1)
