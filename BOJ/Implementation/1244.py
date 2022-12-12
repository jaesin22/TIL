import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
K = int(input())

def switch(sw):
    if sw == 0:
        sw = 1
    elif sw == 1:
        sw = 0
    return sw 
    

def B(R):
    count = 0
    a, b = R-2, R
    while True:
        if count == 0:
            A[R-1] = switch(A[R-1])
            count += 1
        if a == -1 or b == N:
            break
        if A[a] == A[b]:
            A[a], A[b] = switch(A[a]), switch(A[b])
            if count == 0:
                A[R-1] = A[a]
                count += 1
        elif A[a] != A[b]:
            if count == 0:
                A[R-1] = switch(A[R-1])
                break
            else:
                break

        a, b = a - 1, b + 1

for i in range(K):
    jender, num = map(int, input().split())
    cnt = num
    if jender == 1:
        while True:
            if cnt-1 >= N:
                break
            A[cnt-1] = switch(A[cnt-1])
            cnt = cnt + num
    if jender == 2:
        B(num)

for i in range(0, N, 20):
    print(*A[i:i+20])