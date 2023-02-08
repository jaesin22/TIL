import sys
input = sys.stdin.readline

T, W = map(int, input().split())
arr = [0]
for _ in range(T):
    arr.append(int(input()))

dp = [[0] * (W+1) for _ in range(T+1)]

# dp[t][move] : 이제까지 움직인 횟수가 move번 일때, t초부터 받을 수 있는 자두 개수. move가 짝수면 1번나무, 홀수면 2번나무에 위치한 것으로 판단할 수 있다.
for i in range(1, T+1):
    if arr[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, W + 1):
        if j > i:
            break
        
        if arr[i] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
            
        elif arr[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
print(max(dp[-1]))
print(dp)