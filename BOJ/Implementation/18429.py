from itertools import permutations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = permutations(A, N)
cnt = 0
for i in B:
    s = 500
    flag = True
    for j in i:
        s -= K
        s += j
        if s < 500:
            flag = False
    
    if flag:
        cnt += 1

print(cnt)