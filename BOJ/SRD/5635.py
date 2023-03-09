import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
for i in range(N):
    A = list(map(str, input().split()))
    count = A.pop(0)

    counter = Counter(A).most_common(n=2)
    if int(count) / counter[0][1] < 2.0:
        print(counter[0][0])
    else:
        print('SYJKGW')
