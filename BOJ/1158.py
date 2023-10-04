N, K = map(int, input().split())
arr = [i+1 for i in range(N)]
res = []
cnt = 0

while arr:
    for i in range(N):
        if i == K-1:
            print(res)
            res.append(arr.pop(K))
        else:
            if len(res) <= 2:
                res.append(arr.pop(0))

print(res)