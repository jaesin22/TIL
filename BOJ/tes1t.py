from collections import deque
import sys
input = sys.stdin.readline

def bfs(p):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    start = []
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                start.append((i, j))
    
    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1
        
        while queue:
            a, b = queue.popleft()

            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
                    if p[nx][ny] == 'O':
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[a][b] + 1

                    if p[nx][ny] == 'P' and distance[a][b] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    
    for i in places:
        answer.append(bfs(i))
        
    return answer

place = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(place)