import sys
input = sys.stdin.readline

dp = [1] * 1001
N = int(input())
box = list(map(int, input().split()))

for x in range(1, N):
    for y in range(x):
        if box[x] > box[y]:
            dp[x] = max(dp[x], dp[y]+1)

print(max(dp))

# 1. 상자를 입력받고 dp array를 1(해당 상자 1개)로 초기화 해서 만든다
# 2. for문을 돌면서 주어진 상자 순서보다 앞에 있는 상자 중 크기가 작을때 상자의 수+1 과 비교해서 큰 값을 dp에 저장한다.
# 3. dp중 max인 값을 출력한다.