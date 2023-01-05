import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))

end = 0 # 끝 포인터
result = 0 # 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이(출력값)
tmp = 0 # 현재 짝수 부분 수열의 길이
count = 0 # 지우려는 홀수 카운트

# start를 N까지 계속 증가시키며 반복
for start in range(N):
    # end를 가능한 만큼 이동
    while count <= K and end < N:

        # 각 포인터에 대해 "홀수" 라면 count(홀수 카운트)를 +1 해주고, "짝수" 라면 tmp(부분수열 길이) 를 +1 한다.
        if S[end] % 2 == 1: # 홀수
            count += 1
        else: # 짝수
            tmp += 1
        end += 1 # 끝 점 이동
        
        # 만약 start = 0 부터 end = N 까지 돌았을 때도 홀수 개수가 K개를 넘지 않는다면, 바로 전체 짝수 부분 수열 길이를 출력
        if start == 0 and end == N: 
            result = tmp
            break
    
    if count == K + 1:
        result = max(tmp, result)
    

    # start 포인터 한 칸 뒤로 옮기기 전 start 값이 "홀수" 라면 count -1(홀수 카운트), "짝수"라면 tmp -1(부분수열 길이 -1)
    if S[start] % 2 == 1: # 시작점이 홀수
        count -= 1
    else: #시작점이 짝수
        tmp -= 1

print(result)