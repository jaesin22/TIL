from collections import deque
S = int(input())
visited = [[0]* (S+1) for _ in range(S+1)]
queue = deque()
queue.append((1,0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수
while queue:
    s,c = queue.popleft()
    if visited[s][s] == 0: # 방문하지 않았으면
        visited[s][s] = visited[s][c] + 1
        queue.append((s,s)) # 화면에 있는 이모티콘 복사해서 클립보드에 저장
    if s+c <= S and visited[s+c][c] == 0: # 2번 연산
        visited[s+c][c] = visited[s][c] + 1
        queue.append((s+c, c))
    if s-1 >= 0 and visited[s-1][c] == 0: # 3번 연산
        visited[s-1][c] = visited[s][c] + 1
        queue.append((s-1, c))
answer = 0
for i in range(S+1):
    if visited[S][i] != 0:
        if answer == 0 or answer > visited[S][i]:
            answer = visited[S][i]
print(answer)