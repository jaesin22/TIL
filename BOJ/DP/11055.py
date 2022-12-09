N = int(input())
numbers = list(map(int, input().split()))

dp = [0] * (N+1)
dp[0] = numbers[0]
for i in range(1, N):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + numbers[i])


# print(dp)
print(max(dp))