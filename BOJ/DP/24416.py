N = int(input())

def fibo(N):
    global count
    if N == 1 or N == 2:
        return 1
    
    else: 
        count += 1
        return fibo(N-1) + fibo(N - 2)


dp = [0] * 41
dp[0] = 1
dp[1] = 1
cnt = 0
for i in range(2, N):
    dp[i] = dp[i-2] + dp[i-1]
    cnt += 1
count = 1
fibo(N)
print(count, cnt)