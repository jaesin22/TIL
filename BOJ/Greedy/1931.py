N = int(input())
arr = []

for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x:(x[1],x[0])) # 빨리 끝나는 시간대로 정렬
cnt = 1
end = arr[0][1] # 제일 빨리 끝나는 시간
for i in range(1,N) : 
    if arr[i][0] >= end : # 다음 시작시간과 비교하면서 해당 값이 끝나는 시간과 같거나 클 때
        cnt += 1  # 카운트 추가
        end = arr[i][1] # 해당 값 대입

print(cnt)