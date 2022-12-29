import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
result = 0
start, end = 1, max(A)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in A: 
        # 중간값을 나무를 자르는 높이로 생각했을 때 
        #for x in arr >> 나무길이 리스트인 arr 에서 나무를 한개씩 가져와
        #자르는 높이보다 크면
        #나무를 잘라서 cnt에 더함. 
        if i > mid:
            cnt += i - mid
    
    if cnt >= M:
        start = mid + 1
        result = max(result, mid)
    else:
        end = mid - 1

print(result)