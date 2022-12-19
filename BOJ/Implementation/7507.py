import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    M = int(input())
    arr = []
    for j in range(M):
        d, s, e = map(int, input().split())
        arr.append([d, s, e])
    
    arr.sort()
    cnt = 1
    start_date, start_time, end_time = arr[0][0], arr[0][1], arr[0][2]
    for i in range(len(arr) - 1):
        if  start_time >= arr[i+1][2]:
            cnt += 1
            start_time = arr[i+1][1]
            end_time = arr[i+1][2]
            start_date = arr[i+1][0]
        
        elif end_time > arr[i+1][2]:
            start_time = arr[i+1][1]
            end_time = arr[i+1][2]
            start_date = arr[i+1][0]
        else:
            continue
    print(cnt)

# 1) 현재 보려고 하는 경기가 바로 다음에 진행될 경기와 시간이 겹치지 않을 경우 : 다음 경기가 시작되기 전까지 공백기간이 생기면 비효율적이므로, 현재 보려고 하는 경기를 본다.(경기수 +1)


# 2) 현재 보려고 하는 경기가 바로 다음에 진행될 경기와 시간이 겹치는 경우 : 아래와 같이 서로 다른 두 가지 케이스가 존재한다.

# 2)-1 다음에 진행될 경기의 종료시간이 현재 진행될 경기의 종료시간보다 늦는 경우 : 다음에 진행될 경기를 안 보는게 이득이다. 
# 현재 경기가 종료된 뒤에, (다다음, 또는 다다다음 ... 경기 중)시작 시간은 바로 다음에 진행될 경기보다 늦지만  종료시간은 더 이른 경기가 존재 할 수 있기 때문이다.

# 2)-2 다음에 진행될 경기의 종료시간이 현재 진행될 경기의 종료시간보다 이른 경우 : 다음에 진행될 경기를 보는게 이득이다. 
# 종료시간이 더 빠르면, 차후에 진행될 경기의 시작시간에 맞춰 경기를 더 볼 수도 있기 떄문이다.