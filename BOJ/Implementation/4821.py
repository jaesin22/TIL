import sys
input = sys.stdin.readline

while True:
    N = int(input())
    visited = [0] * (N+1)
    if N == 0 :
        break
    A = input().rstrip()
    B = A.split(',')
    for i in B:
        if '-' in i:
            x,y = i.split('-')
            x, y = int(x), int(y)
            if x > N:
                continue
            if y >= N:
                y -= y-N

            if x <= y:
                for j in range(x, y+1):
                    visited[j] = 1
        else:
            if int(i) > N:
                continue 
            visited[int(i)] = 1

    print(sum(visited))