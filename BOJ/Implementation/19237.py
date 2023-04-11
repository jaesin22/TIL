import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]    

N, M, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int ,input().split()))
shark_dir = [[] for _ in range(M)]
rank = [[] for _ in range(M)]

for i in range(M):
    for _ in range(4):
        rank[i].append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            shark_dir[graph[i][j]-1] = [i,j,direction[graph[i][j]-1]-1]
        graph[i][j] = [0, 0]

def smell(graph, shark_dir):
    for i in range(len(shark_dir)):
        if shark_dir[i]:
            x, y, d = shark_dir[i]
            graph[x][y] = [k, i]
    return graph

def next(graph):
    for i in range(N):
        for j in range(N):
            if graph[i][j][0] > 0:
                graph[i][j][0] -= 1
    return graph

def search(shark_dir):
  #임시배열 생성 (겹치는 상어를 제거하기위해)
  temp=[[[]for j in range(N)] for _ in range(N)]
  for i in range(len(shark_dir)): #상어배열을 돌면서 
    if shark_dir[i]: 
      x,y,d=shark_dir[i] 
      candidate=[] #빈자리 
      my_candidate=[] #내냄새가 있는 곳 
      for k in range(4): #상하좌우 
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<N and 0<=ny<N: #범위안에있으면 
          if graph[nx][ny][0]==0: #빈자리라면 
            candidate.append((nx,ny,k))
          elif graph[nx][ny][1]==i: #내냄새가 남아있는곳이라면
            my_candidate.append((nx,ny,k))
      new_d=d #상어의 다음방향 
      if not candidate: #빈자리가 없다면 
        candidate=my_candidate #최종후보군은 내냄새가 남아있는 곳 
      if len(candidate)>=2: #후보군이 여러개라면 
        shark_rank=rank[i][d] #우선순위대로 
        for r in shark_rank:
          flag=False
          for a,b,c in candidate: 
            if r-1==c: #우선순위와 일치하면 
              new_d=r-1 #방향 업데이트 
              flag=True #탈출 
              break
          if flag:
            break
      else: #후보군이 하나라면 
        new_d=candidate[0][2] #바로 방향업데이트 
      shark_dir[i]=[x+dx[new_d],y+dy[new_d],new_d] #상어 최종정보 업데이트
      temp[x+dx[new_d]][y+dy[new_d]].append(i) #임시배열에 저장 

    #임시배열을 돌면서  
    for i in range(N):
      for j in range(N):
        if len(temp[i][j])>1: #상어가 겹치는 칸이있으면 
            temp[i][j].sort() #정렬해서 맨앞 상어만 살리기 
            for k in temp[i][j][1:]:
                shark_dir[k]=[] #나머지 상어는 삭제 

    cnt=0 #남은 상어의 개수 
    for i in range(M):
        if shark_dir[i]!=[]:
            cnt+=1

  return shark_dir, cnt


for i in range(1000):
    graph = smell(graph, shark_dir)
    shark_dir, live = search(shark_dir)
    graph = next(graph)

    if live == 1:
        print(i + 1)
        break
else:
    print(-1)
        