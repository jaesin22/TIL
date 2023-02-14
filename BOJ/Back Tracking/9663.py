import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
visited = [0] * N

def chk(x):
    for i in range(x):
        if visited[x] == visited[i] or abs(visited[x] - visited[i]) == x- i:
            return False
    return True


def solve(x, N):
    global cnt
    if x == N:
        cnt += 1
    else:
        for i in range(N):
            visited[x] = i
            if chk(x):
                solve(x + 1, N)

solve(0, N)
print(cnt)
