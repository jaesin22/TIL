# https://developer-ellen.tistory.com/51 참고
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def chk(line):
    visited = [0] * N
    for i in range(N-1):
        if line[i] == line[i+1]:
            continue
        elif abs(line[i] - line[i+1]) > 1:
            return False
        elif line[i] > line[i + 1]:
            tmp = line[i+1]
            for j in range(i+1, i + L + 1):
                if 0 <= j < N:
                    if tmp != line[j]:
                        return False
                    # 경사로를 2번 놓을 수는 없음
                    elif visited[j] == 1:
                        return False
                    #경사로 처리
                    visited[j] = 1
                else:
                    return False
        
        #아래에서 위로 올라가는 거, 오른쪽에서 왼쪽 방향으로
        else:
            tmp = line[i]
            for j in range(i, i-L, -1):
                if 0 <= j < N:
                    if tmp != line[j]:
                        return False
                    elif visited[j] == 1:
                        return False
                    visited[j] = 1
                else:
                    return False
                
    return True

res = 0
for line in graph:
    if chk(line):
        res += 1

for i in range(N):
    temp = []
    for j in range(N):
        temp.append(graph[j][i])
    if chk(temp):
        res += 1

print(res)
        