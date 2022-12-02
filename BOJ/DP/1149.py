import sys
input = sys.stdin.readline

N = int(input())
rgb =[]
for x in range(N):
    rgb.append(list(map(int, input().split())))

for i in range(1, len(rgb)):
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

print(min(rgb[N-1][0], rgb[N-1][1], rgb[N-1][2]))

# 0, 1, 2 = 각각 빨강 초록 파랑
# rgb[i][0]은 i번째 집을 빨강으로 칠했을 때의 최소값을 나타내나
# rgb[i][1]과 rgb[i][2]도 마찬가지로 i번째 집을 초록, 파랑으로 칠했을 때의 최솟값을 나타낸다
# 이 3개 중에서 가장 작은 값을 출력해주면 된다