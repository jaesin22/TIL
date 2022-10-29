import sys
input = sys.stdin.readline
N = int(input())


for x in range(N):
    T = int(input())
    res = [0] * (101)
    res[0] = 1
    res[1] = 1
    res[2] = 1
    for y in range(3, T+1):
        res[y] = res[y-3] + res[y-2]
    print(res[T-1])
