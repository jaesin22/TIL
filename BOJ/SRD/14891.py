import sys
from collections import deque
input = sys.stdin.readline

def left(num, direction):
    if num < 0:
        return
    
    if s[num][2] != s[num+1][6]:
        left(num-1, -direction)
        s[num].rotate(direction)

def right(num, direction):
    if num > 3:
        return
    
    if s[num][6] != s[num-1][2]:
        right(num+1, -direction)
        s[num].rotate(direction)


s = []
for _ in range(4):
    s.append(deque(list(input().strip())))

K = int(input())
R = [list(map(int, input().split())) for _ in range(K)] 

for i in range(K):
    num = R[i][0] - 1 #돌아가는 톱니바퀴
    direction = R[i][1] #시계, 반시계방향
    left(num-1, -direction) #왼쪽조사
    right(num+1, -direction) #오른쪽조사
    s[num].rotate(direction) #현재 톱니바퀴는 회전

res = 0

if s[0][0] == '1':
    res += 1
if s[1][0] == '1':
    res += 2
if s[2][0] == '1':
    res += 4
if s[3][0] == '1':
    res += 8
    
print(res)