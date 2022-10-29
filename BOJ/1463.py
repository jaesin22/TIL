import sys
input = sys.stdin.readline
N = int(input())

res = [0] * (N+1)

for i in range(2, N+1):
    res[i] = res[i-1] + 1 # 2와 3으로 나누어 떨이지지 않는 경우는 무조건 1을 빼야 하기 때문에 +1을 통해 횟수를 1 추가한다

    if i % 2 == 0:
        res[i] = min(res[i], res[i//2] + 1) # 2와 3으로 나누어 떨어지는 경우는 1을 빼는 것보다 훨씬 이득이기 때문에 min(dp[i]), dp[i//2]+1를 통해 최소값을 선택하면 된다.
    if i % 3 == 0:
        res[i] = min(res[i], res[i//3] + 1)
    

print(res[N])