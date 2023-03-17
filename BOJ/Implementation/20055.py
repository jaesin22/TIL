import sys
from collections import deque
input = sys.stdin.readline

def rotate():
    belt.appendleft(belt.pop())
    robots.pop()
    robots.appendleft(0)
    robots[-1] = 0


N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robots = deque([0] * N )

count = 0
while True:
    rotate()
    count += 1
    
    ### 2. 로봇 이동
    for i in range(N-2,-1,-1):
        if robots[i] == 1:
            if robots[i+1] != 1 and belt[i+1] >= 1:
                robots[i+1] = 1
                robots[i] = 0
                belt[i+1] -= 1

    ### 3. 로봇 올리기
    if belt[0] != 0:
        robots[0] = 1
        belt[0] -= 1

    if belt.count(0) >= K:
        break

print(count)