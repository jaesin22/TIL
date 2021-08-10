(n, k) = map(int, input().split())


cnt = 0
arr = [0 for _ in range(0, n + 1)]

for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if arr[j] != 0:
            continue
        arr[j] = 1
        cnt += 1
        if cnt == k:
            print(j)
            exit(0)