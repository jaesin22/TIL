import sys

input = sys.stdin.readline 
A, B = map(int, input().split())
res = []
for i in range(A):
    res.append(input())
rep = []

for i in range(A-7):
    for j in range(B-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:
                    if res[k][l] != 'W':
                        first_W = first_W+1
                    if res[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if res[k][l] != 'B':
                        first_W = first_W+1
                    if res[k][l] != 'W':
                        first_B = first_B + 1
        rep.append(first_W)
        rep.append(first_B)

print(min(rep))