N, K, A, B = map(int, input().split())
res = [K for x in range(N)]
print(res)
cnt = 0
res_count = 0
while True:
    for x in range(A):
        if res_count == N:
            res_count = 0

        res[res_count] =  res[res_count] + B
        res_count = res_count + 1

    for y in res:
        if y == 0:
            break
        y = y - 1
        cnt = cnt + 1


print(cnt)

