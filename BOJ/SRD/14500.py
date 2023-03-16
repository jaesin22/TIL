import sys
input = sys.stdin.readline
 
N, M = map(int, input().split())
graph = []
check = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().split())))
 
block = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
 
    [[0, 0], [0, 1], [1, 0], [1, 1]],
 
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [0, 1], [0, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 0], [1, 0], [2, 0], [2, -1]],
    [[0, 0], [-1, 0], [0, 1], [0, 2]],
 
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [-1, 1], [0, 1], [-1, 2]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    [[0, 0], [1, 0], [1, -1], [2, -1]],
 
    [[0, 0], [1, -1], [1, 0], [1, 1]],
    [[0, 0], [1, 0], [1, 1], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [1, 0], [1, -1], [2, 0]]
]
 
def solve(x, y):
    result = 0 # 해당 지점에서 발생할 수 있는 최종값
    for i in range(len(block)): # 각 블록의 유형에 대해
        s = 0 # 산출값 초기화
        v_list = [[x + nx, y + ny] for nx, ny in block[i]]
        # print(v_list)
        for v in v_list: # 블록의 각 지점에 대해
            if 0 <= v[0] < N and 0 <= v[1] < M: # 범위 내라면
                s += graph[v[0]][v[1]] # 값 반영
            else: # 범위 밖이면 더 볼 필요 없음
                break
        result = max(result, s) # 각 블록에 대해 최대값 점검
    return result # 최종값 반환
 
res = 0
for i in range(N):
    for j in range(M):
        res = max(res, solve(i, j))
print(res)