import sys
from collections import Counter
n = int(sys.stdin.readline())

for x in range(n):
    a = int(sys.stdin.readline())
    res = []
    for i in range(a):
        a, b = sys.stdin.readline().rstrip().split()
        res.append(b)
    
    wear = Counter(res)
    cnt = 1

    for items in wear:
        cnt *= wear[items] + 1
    
    print(cnt - 1)
