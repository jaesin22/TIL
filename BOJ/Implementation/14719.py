height, weight = map(int, input().split())
ground = list(map(int, input().split()))
rain = 0
# for문을 통해서 양 옆 비교하기

for i in range(1, weight-1):
    left = max(ground[:i])
    right = max(ground[i+1:])
    std = min(left, right)

    if ground[i] < std:
        rain += std - ground[i]

# 값 출력
print(rain)