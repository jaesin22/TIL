T = int(input())

res = [0] * 100000
res[0] = 1
res[1] = 2
res[2] = 4

for i in range(T):
    N = int(input())
    for j in range(3, N):
        res[j] = res[j-1] + res[j-2] + res[j-3]
    print(res[N-1])