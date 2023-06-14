import sys
input = sys.stdin.readline

def stick(block):
    global graph

    x, y = len(block), len(block[0])
    for i in range(N-x+1):
        for j in range(M-y+1):
            if graph[i][j] == 0 or block[0][0] == 0:
                cnt = 0
                flag = True
                for nx in range(x):
                    for ny in range(y):
                        if block[nx][ny] == 1:
                            if graph[nx+i][ny+j] == 0:
                                cnt += 1
                                graph[nx+i][ny+j] = 1
                            else:
                                flag = False
                                break
                    if not flag:
                        break
                if not flag:
                    rollback(cnt, i, j, x, y, block)
                else:
                    return cnt
    return 0


def rollback(cnt, i, j, x, y, block):
    global graph
    tmp = 0
    if tmp == cnt:
        return
    
    for k in range(x):
        for l in range(y):
            if block[k][l] == 1:
                graph[i+k][j+l] = 0
                tmp += 1

                if tmp == cnt:
                    return


def rotate(block):
    x, y = len(block), len(block[0])
    tmp = [[0] * x for _ in range(y)]

    for i in range(x):
        for j in range(y):
            tmp[j][x-i-1] = block[i][j]
    
    return tmp



N, M, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
sticker = []
for _ in range(K):
    a, b = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(a)]
    sticker.append(arr)

res = 0
for block in sticker:
    for _ in range(4):
        cnt = stick(block)
        if cnt != 0:
            res += cnt
            break
        block = rotate(block)

print(res)