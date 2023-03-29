import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

blocks = [
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
    
    [[0, 0], [0, 1], [1, 1], [0, 2]],
    [[0, 0], [1, 0], [1, -1], [2, 0]],
    [[0 ,0], [0, 1], [-1, 1], [0, 2]],
    [[0, 0], [1, 0], [1, 1], [2, 0]]
]

def cal(x, y):
    result = 0
    for i in range(len(blocks)):
        s = 0 # 산출값 초기화
        v_list = [[x + ax, y + ay] for ax, ay in blocks[i]]
        
        for nx, ny in v_list:
            if 0 <= nx < N and 0 <= ny < M:
                s += graph[nx][ny]
            else:
                break
        result = max(result, s)
    return result

res = 0
for i in range(N):
    for j in range(M):
        res = max(res, cal(i, j))

print(res)