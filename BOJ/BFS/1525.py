import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

target = '1234567890'
start = ""               # 시작 문자열
for _ in range(3):
    start += ''.join(list(input().split()))

def bfs():
    check = set([start])
    queue = deque()
    queue.append((start, 0))

    while queue:
        temp, cnt = queue.popleft()
        if temp == '123456780':
            return cnt
        
        idx = temp.index('0') # 0인 곳의 인덱스 
        a, b = idx // 3, idx % 3 # 이차원 맵 내 좌표로 변환
        for i in range(4): # 4방향 중 위치 바꿀 수 있는 곳
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                nextTemp = list(temp) # 위치 교환 쉽게 하기 위해 리스트로 변환
                nextIdx = nx * 3 + ny  # 위치 교환할 인덱스
                nextTemp[idx], nextTemp[nextIdx] = nextTemp[nextIdx], nextTemp[idx] # 위치 교환
                nextTemp = ''.join(nextTemp) # 문자열로 재변환

                if nextTemp in check: # 이미 방문한 곳인지 확인
                    continue
                
                check.add(nextTemp) # 방문 표시
                print(check)
                queue.append((nextTemp, cnt + 1)) # (위치 교환한 문자열, 횟수+1)해서 큐에 담기
    return -1
                

print(bfs())