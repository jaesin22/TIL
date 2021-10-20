import sys
import heapq
N = int(sys.stdin.readline())

res = []
for _ in range(N):
    M, K = map(int, sys.stdin.readline().split())
    res.append([M, K])


res.sort()

room = []
heapq.heappush(room, res[0][1])

for i in range(1, N):
    if res[i][0] < room[0]:  # 현재 회의실 끝나는 시간보다 다음 회의 시작 시간이 빠르면
        heapq.heappush(room, res[i][1])  # 새로운 회의실 개설
    else:  # 현재 회의실에 이어서 회의 개최 가능
        heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop 후 새 시간 push
        heapq.heappush(room, res[i][1])

print(len(room))


