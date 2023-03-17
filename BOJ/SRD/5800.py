K = int(input())
cnt = 1

for i in range(K):
    A = list(map(int, input().split()))
    s = A.pop(0)
    res = 0

    A.sort(reverse=True)
    for i in range(len(A)-1):
        res = max(res, A[i] - A[i+1])

    print("Class " + str(cnt))
    print("Max " + str(max(A)) + ", Min " + str(min(A)) + ", Largest gap " + str(res))
    cnt += 1
