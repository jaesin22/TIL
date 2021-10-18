import sys
N = int(sys.stdin.readline())

M, K = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

A.sort(reverse=True)
num = M * K
cnt = 0
if sum(A) < M * K:
    print("STRESS")
else :
    for x in A:
        if num <= 0:
            print(cnt)
            break
        else:
            num = num - x
            cnt += 1