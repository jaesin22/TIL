import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

height = 0
ans = float('inf')

for i in range(257):
#     각 도달하고 싶은 높이마다 2차원 리스트를 탐색해준다.
# 블록 높이와 도달 높이를 비교해가며 가져온 블록(max), 사용한 블럭(min)에 블럭 개수를 추가해준다.
# 이후 총 사용한 블록과 가져온 블록 + 원래 있던 블럭 개수를 비교해서 도달 높이로 만드는 게 가능한지 확인한다. 
# 가능하다면 걸리는 시간을 계산하고 최솟값 비교를 해준다.
    max = 0
    min = 0
    for j in range(N):
        for k in range(M):
            if graph[j][k] < i:
                min += (i - graph[j][k])
            else:
                max += (graph[j][k] - i)
    
    inventory = max + B
    if inventory < min:
        continue
    time = max * 2 + min
    if time <= ans:
        # 시간이 같을 때는 높이가 높은 순으로 출력하라는 조건에 맞게
        # for i in range(257)은 항상 i가 오름차순으로 돌기 때문에
        # 시간이 같아도 최종적으로는 높이가 높은 순으로 나오게 된다.
        ans = time
        height = i

print(ans, height)