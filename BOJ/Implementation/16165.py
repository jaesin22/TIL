import sys

N, M = map(int, input().split())
group = []
for i in range(N):
    name = input().rstrip()
    A = int(input())
    for j in range(A):
        B = input().rstrip()
        group.append([name, B])

group.sort()

for j in range(M):
    name = input().rstrip()
    A = int(input())
    if A == 0:
        for i in group:
            if i[0] == name:
                print(i[1])
                
    elif A == 1:
        for i in group:
            if i[1] == name:
                print(i[0])