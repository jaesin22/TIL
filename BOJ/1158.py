N, K = map(int, input().split())
array = [i for i in range(1,N+1)]  # 맨 처음에 원에 앉아있는 사람들
result = [] # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for t in range(N):
    num += K - 1
    if num >= len(array): # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        num = num%len(array)

    result.append(str(array.pop(num)))

print("<",", ".join(result)[:],">", sep='')