import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(5)]
arr = [list(map(int, input().split())) for _ in range(5)]
bingo = 0
cnt = 0

def chk():
    bingo_cnt = 0
    x, y, k = 0, 0, 0
    for i in range(5):
        #가로
        if sum(graph[i]) == 0 :
            bingo_cnt += 1
        
        #세로
        k = 0
        for j in range(5):
            k += graph[j][i]
        if k == 0 :
            bingo_cnt += 1
            
        #대각선
        x += graph[i][i]
        y += graph[i][4-i]
    
    if x == 0 :
        bingo_cnt += 1
    if y == 0 :
        bingo_cnt += 1
    
    if bingo_cnt >= 3 :
        return True
    else :
        return False
    

for i in range(5):
    for j in range(5):
        a = arr[i][j]
        for k in range(5):
            for l in range(5):
                if graph[k][l] == a:
                    graph[k][l] = 0
                    cnt += 1
                    if cnt > 11 and chk():
                        print(cnt)
                        sys.exit()

                    
