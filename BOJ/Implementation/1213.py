import sys
from collections import Counter
input = sys.stdin.readline

A = list(map(str, input().strip()))
A.sort()
chk = Counter(A)

cnt = 0
middle = ''

for i in chk:
    if chk[i] % 2 != 0:
        middle += i
        cnt += 1
        A.remove(i)
    
    if cnt > 1:
        print("I'm Sorry Hansoo")
        sys.exit()

res = ''
for i in range(0, len(A), 2):
    res += A[i]

print(res + middle + res[::-1])