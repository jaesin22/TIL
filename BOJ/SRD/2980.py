N, L = map(int, input().split())
res = 0
postition = 0

for _ in range(N):
    D, R, G = map(int, input().split())

#     - 경과 시간에 (신호등 위치 - 현재위치)만큼 더해준다.

# - 현재위치를 d로 갱신한다.

# - 이후 빨간불과 초록불의 시간을 더하고 이를 경과시간에 나눈 나머지가 빨간불 이하라면 대기해야한다.

# - 따라서 대기하는 시간만큼 경과시간에 더한다.
    res += (D-postition)
    postition = D
    if res % (R + G) <= R:
        res += (R - (res % (R+G)))

# - N개의 신호를 입력받은 후에

# - 마지막 신호등과 L과의 거리를 경과 시간에 더하고 출력한다.
res += (L - postition)
print(res)