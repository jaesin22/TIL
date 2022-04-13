import sys
sys.setrecursionlimit(10**4)	# recursion limit 제한 설정

# 하 좌 상 우
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y):
    global ch_matrix, matrix
    ch_matrix[x][y] = 1		# 현재 위치 체크
    cnt = 1			# 현재 위치의 크기 1

    for d in range(4):		# 현재 위치 기준으로 하,좌,상,우 탐색
        nx = x + dx[d]		# 탐색할 좌표
        ny = y + dy[d]
        
        # 탐색할 좌표가 지도를 벗어나지 않고, 값이 #이고, 이미 탐색한 곳이 아니라면
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == '#' and ch_matrix[nx][ny] == 0:
            ch_matrix[nx][ny] = 1	# 좌표 체크
            cnt += dfs(nx, ny)		# dfs 실행 후 값을 cnt에 추가
    return cnt 			# 모두 탐색 후 합한 값을 리턴


# 입력 받음
N, M, K = map(int, input().split())
garbage = [tuple(map(int, input().split())) for _ in range(K)]

# 지도 생성
matrix = []			
for _ in range(N):
    matrix.append(['.' for _ in range(M)])
for x, y in garbage:
    matrix[x-1][y-1] = '#'
    
largest = 0			# 가장 큰 음쓰 크기

# 탐색 확인용 지도 생성
ch_matrix = []			
for _ in range(N):
    ch_matrix.append([0 for _ in range(M)])

# 지도에서 음쓰 위치 탐색
for x in range(N):
    for y in range(M):
        # 음쓰 탐색한 경우
        if matrix[x][y] == '#' and ch_matrix[x][y] == 0:
            ch_matrix[x][y] = 1	# 음쓰 위치 체크
            largest = max(largest, dfs(x, y))	# dfs 후 largest 값과 비교 후 저장.

print(largest)			# 출력