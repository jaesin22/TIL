from collections import deque
s = [] #톱니바퀴배열 
for _ in range(4):
    s.append(deque(list(input())))
K = int(input()) #회전횟수
R = [list(map(int, input().split())) for _ in range(K)] 

#왼쪽 톱니바퀴 확인
def left(num, direction): 
    if num < 0: #첫번째톱는 확인안함
        return 
    if s[num][2] != s[num+1][6]: #극이 다른경우
        left(num-1, -direction)  #그 왼쪽 톱니바퀴도 조사 
        s[num].rotate(direction) #현재 톱니바퀴는 회전 

#오른쪽 톱니바퀴 확인
def right(num, direction): 
    if num > 3: #마지막은 확인안함
        return 
    if s[num][6] != s[num-1][2]: #극이 다른경우
        right(num+1, -direction) #그 오른족 톱니바퀴도 조사
        s[num].rotate(direction) #현재 톱니바퀴는 회전


for i in range(K): 
    num = R[i][0] - 1 #돌아가는 톱니바퀴
    direction = R[i][1] #시계, 반시계방향
    left(num-1, -direction) #왼쪽조사
    right(num+1, -direction) #오른쪽조사
    s[num].rotate(direction) #현재 톱니바퀴는 회전

res = 0 #점수

if s[0][0] == '1':
    res += 1
if s[1][0] == '1':
    res += 2
if s[2][0] == '1':
    res += 4
if s[3][0] == '1':
    res += 8
    
print(res)