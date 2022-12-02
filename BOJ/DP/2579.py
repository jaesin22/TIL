import sys
input = sys.stdin.readline
n = int(input().strip())
stairs = [int(input().strip()) for _ in range(n)]
dp = [0 for _ in range(n+1)]

if n>=3:
    dp[0] = stairs[0]
    dp[1] = stairs[0]+stairs[1]
    dp[2] = max(stairs[0]+stairs[2],stairs[1]+stairs[2])

    for i in range(3,n):
        dp[i] = max( stairs[i-1]+dp[i-3]+stairs[i], dp[i-2],stairs[i] )
        		#max(직전칸의 값+3개 전 계단의 최댓값+현재값, 2개 전 계단의 최댓값 + 현재값)
    print(dp[-2])
else:
    if n==1: print(stairs[0])
    elif n==2: print(stairs[0]+stairs[1])
    elif n==3: print(max(stairs[0]+stairs[2],stairs[1]+stairs[2]))