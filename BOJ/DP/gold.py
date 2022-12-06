# 이코테 2021 DP 예제문제 금광

T = int(input()) # 테스트 케이스 입력
for tc in range(T):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    idx = 0
    for i in range(N):
        dp.append(array[idx:idx + M])
        idx += M

    # DP 진행
    for j in range(1, M):
        for i in range(N):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            # 왼쪽 아래에서 오는 경우
            if i == N-1:
                left_down = 0
            else: 
                left_down = dp[i + 1][j - 1]

            #왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left, left_down, left_up)
    res = 0
    for i in range(N):
        res = max(res, dp[i][M-1])
    print(res) 

