n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    # Max의 첫번째 마지막 계단의 전 계단을 밟은 경우.
    # 마지막 계단은 S[i] 이고 마지막 계단 밟기 전 마지막 계단 1칸 전 계단을 밟으면
    # 1칸 전에서 2칸 전의 게단을 밟을 수 있으므로 dp[i-3]도 추가한다
    # MAx의 두 번째, 마지막 계단의 전 계단을 밟지 않은 경우
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])