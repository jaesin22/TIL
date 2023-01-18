from collections import deque
import sys
input = sys.stdin.readline

def print_arr():
    print('[', end='')
    for i in range(len(queue)):
        if i == len(queue) - 1:
            print(queue[i], end='')
        else:
            print(queue[i], end=',')
    print(']')

T = int(input())
for i in range(T):
    chk = False
    cnt = 0 #reverse 체크 횟수
    A = input().rstrip()
    B = int(input())
    arr = input().rstrip()
    queue = deque()
    if B == 0 and arr == '[]' and A == 'D':
        print('error')
        continue

    arr_split = arr.split(']')
    arr_split = arr_split[0].split('[')
    arr_split = arr_split[1].split(',')
    arr_split = ' '.join(arr_split).split()

    for i in arr_split:
        queue.append(i)

    for i in A:
        if i == 'R':
           cnt += 1
           # num.reverse(), 시간이 오래걸림
  
        if i == 'D':
           if queue:
           # cnt이 짝수개라면 뒤집지않고 제거해주면 됨, pop()해줌
               if cnt % 2 == 1:
                   queue.pop()
           # cnt 홀수개라면 뒤집고 제거해줘야 함, popleft()로 해줌
               else :
                   queue.popleft()
           else:
               chk = True
               break
    
    if chk == True:
        print('error')
        continue
    else:
       if cnt % 2 == 1:
           print('[',end='')
           print(','.join(reversed(list(queue))), end='')
           print(']')  
       else:
           queue = ','.join(queue)
           print('[',end='')
           print((queue), end='')
           print(']')