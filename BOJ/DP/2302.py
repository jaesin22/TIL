import sys
input = sys.stdin.readline

# - 점화식을 구하면 쉽게 풀 수 있는 문제이다.

# - 좌석이 1개일 때 경우의 수는 1개이고 좌석이 2개일 때 경우의 수는 2개이고 좌석이 3개일 때 경우의 수는 3개이다.

# - 점화식: dp[n] = dp[n - 1] + dp[n - 2]

# VIP들 같은 경우에는 움직이지 못하기 때문에 주위 사람들과 자리 변경이 불가능하다. 따라서 양 옆을 분할한다라고 생각할 수 있다. 즉 문제에서 소개한 예시로 보면 9개의 자리가 있을 때, 4와 7에서 자리를 분할하고 있다. 

# 문제에서 주어진 vip석을 제외하고 경우의 수를 구해야 하므로 vip석과 vip석 사이에 존재하는 좌석의 갯수의 경우의 수
#  그러니까 dp테이블에 vip석 사이를 조회해주면 해당 가지수를 각각 구해줄 수 있고 이를 서로 곱하면 총 가짓수를 구할 수 있다.



N = int(input())
M = int(input())
VIP = []
for i in range(M):
    VIP.append(int(input()))

dp = [0] * 41
dp[0] = 1
dp[1] = 1 # 1
dp[2] = 2 # 1 2, 2 1
# dp[3] = 3 # 1 2 3, 1 3 2, 2 1 3
# dp[4] -> 1243, 2143 | 1324, 1234, 2134
for i in range(3, N + 1):
    dp[i] = dp[i-1] + dp[i-2] #  점화식


idx_diff = 0
answer = 1
for i in VIP:
	answer *= dp[i - 1 - idx_diff]
	idx_diff = i

answer *= dp[N - idx_diff]

print(answer)