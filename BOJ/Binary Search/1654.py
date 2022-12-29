N, K = map(int, input().split())
arr = []

for i in range(N):
    arr.append(int(input()))

result = 0

start, end = 1, max(arr)
while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        result = 0
        break
    # 몫의 합을 저장하는 변수
    cnt = 0
    for i in arr:
        # mid로 나눈 몫을 저장
        cnt += i // mid

    if cnt >= K:
        # K개를 만들 수 있을 때, 답을 더 큰 값으로 계속 갱신
        result = max(result, mid)
        # 현재 mid로 나눈 값이 N보다 크거나 같다면,
		# left를 움직여 길이가 더 긴 경우는 가능한지 검사
        start = mid + 1
    else:
        # 현재 mid로 나눈 값이 N보다 작다면,
		# right 움직여 길이가 더 짧은 경우는 가능한지 검사
        end = mid - 1

print(result)