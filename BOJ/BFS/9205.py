import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited = []

    while queue:
        a, b = queue.popleft()
        visited.append([a, b])
        if a == festival_x and b == festival_y:
            print("happy")
            return

        # 현재 위치에서 갈 수 있는 편의점 넣기
        for nx, ny in store:
            dist = abs(a - nx) + abs(b - ny) #맨해튼 거리
            if 1000 >= dist and [nx, ny] not in visited: # 맥주를 마시며 걸어갈 수 있느 ㄴ거리라면 큐에 넣기
                queue.append((nx, ny))
                visited.append([nx, ny])

    print("sad")
    return
T = int(input())
for _ in range(T):
    N = int(input())
    store = []
    home_x, home_y = map(int, input().split()) # 상근이 집 (출발 좌표)

    for _ in range(N):
        store_x, store_y = map(int, input().split())
        store.append([store_x, store_y])
    
    festival_x, festival_y = map(int, input().split())
    store.append([festival_x, festival_y])

    bfs(home_x, home_y)