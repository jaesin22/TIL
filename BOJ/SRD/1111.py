import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    A = N // H + 1
    J = N % H
    if J == 0:
        if A < 10:
            print(H, 0, J-1, sep='')
        else:
            print(H, A-1, sep='')
    else:
        if A < 10:
            print(J, 0, A, sep='')
        else:
            print(J, A, sep='')
