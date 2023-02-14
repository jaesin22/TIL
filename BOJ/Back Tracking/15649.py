N, M = map(int, input().split())
visited = [False] * N
res = []

def solve(depth, N, M):
    if depth == M: # 탈출 조건
        print(' '.join(map(str, res)))
        return
    
    for i in range(len(visited)): 
        if not visited[i]: # 탐사 안했다면
            visited[i] = True # 탐사 시작(중복 제거)
            res.append(i + 1)
            solve(depth+1, N, M) # 깊이 우선 탐색
            visited[i] = False # 깊이 탐사 완료
            res.pop() # 탐사 내용 제거

solve(0, N, M)