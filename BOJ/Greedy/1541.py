import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    res = 0
    cnt = 0

    # 뒤에서 부터 접근한다면 단순히 현재 max값보다 현재 인덱스값이 더 작다면 그 차이만큼 이익을 더하면된다.
    for i in range(len(A)-1, -1, -1):
        if A[i] > cnt:
            cnt = A[i]  
        else:
            res += cnt - A[i]
    print(res)