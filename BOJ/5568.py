import sys
from itertools import permutations # 순열 활용

N = int(sys.stdin.readline()) 
K = int(sys.stdin.readline())

res = []
arr = []
for x in range(N):
    res.append(sys.stdin.readline().rstrip())


for y in permutations(res, K): 
    arr.append(''.join(y)) # join으로 list 요소 합쳐주기

arr = set(arr)
print(len(arr)) 