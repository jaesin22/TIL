T = int(input())
for tc in range(T):
    N = int(input())
    if N == 1 or N == 2:
        print(N)
        continue
    if N == 3:
        print(4)
        continue
    
    dp = [0] * (N+1)

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, N+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        dp[i] %= 1000000009

    print(dp[N])