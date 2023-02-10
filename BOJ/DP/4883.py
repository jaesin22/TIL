import sys
input = sys.stdin.readline

cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    
    
    dp = [[0] * 3 for _ in range(N)]

    dp[1][0] = graph[0][1] + graph[1][0]
    dp[1][1] = min(dp[1][0], graph[0][1], graph[0][1] + graph[0][2]) + graph[1][1]
    dp[1][2] = min(dp[1][1], graph[0][1], graph[0][1] + graph[0][2]) + graph[1][2]

    for i in range(2, N):
        for j in range(3):
            if j == 0:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + graph[i][j]
            elif j == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j], dp [i-1][j+1]) + graph[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + graph[i][j]
    
    print(str(cnt) + '. ' + str(dp[N-1][1]))
    cnt += 1