import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# 현재 자신을 포함하여 만들 수 있는 LIS 길이 저장
# (자기 자신을 포함하므로 dp 리스트 1로 초기화)
dp = [1] * N
# i를 기준으로
for i in range(1, N):
    # i보다 인덱스가 작은 모든 원소들 전부 탐색
    for j in range(i):
        # LIS 만들기
        if A[i] > A[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))