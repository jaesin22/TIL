import sys
input = sys.stdin.readline

N = int(input())
array = [int(input()) for _ in range(N)]
if N == 1 or N == 2:
    print(sum(array))

else:
    dp = [0] * (N+1)
    dp[0] = array[0]
    dp[1] = array[0] + array[1]

    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2] + array[i], dp[i-3] + array[i-1] + array[i])
    
    print(dp[N-1])

