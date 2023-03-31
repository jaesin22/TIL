import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def spring_summer():
    for i in range(N):
        for j in range(N):
            len_t = len(tree[i][j])
            for k in range(len_t):
                if tree[i][j][k] <= energy[i][j]:
                    energy[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    for _ in range(k, len_t):
                        energy[i][j] += tree[i][j].pop() // 2
                    break

def fall_winter():
    for i in range(N):
        for j in range(N):
            for k in tree[i][j]:
                if k % 5 == 0:
                    for l in range(8):
                        nx = i + dx[l]
                        ny = j + dy[l]
                        if 0 <= nx < N and 0 <= ny < N:
                            tree[nx][ny].appendleft(1)
            energy[i][j] += A[i][j]

dead = deque()
N, M, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

energy = [[5] * N for _ in range(N)]
tree = [[deque() for i in range(N)] for i in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    tree[a-1][b-1].append(c)

for _ in range(K):
    spring_summer()
    fall_winter()

res = 0
for i in range(N):
    for j in range(N):
        res += len(tree[i][j])

print(res)