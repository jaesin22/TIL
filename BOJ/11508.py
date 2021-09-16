import sys

N = int(sys.stdin.readline())
res = [] # 유제품 가격 리스트
for x in range(N):
    C = int(input())
    res.append(C)


res.sort(reverse=True) # 내림차순으로 정렬
cnt = 1
result = 0
for i in res:
    if cnt % 3 != 0: #count에서 3을 나눴을 때 나머지가 3이 아닐 때 result에 i 값을 더해줌
        result += i
        cnt += 1
    else: # 만약 리스트 원소가 3의 배수 자리에 있다면 result에 원소 값을 더하지 않음
        cnt += 1


print(result)