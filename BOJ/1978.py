import sys
import math
N = int(sys.stdin.readline())

res = list(map(int, sys.stdin.readline().split()))
cnt = 0

def isPrime(num):
    if num == 1:
        return False
    n = int(math.sqrt(num))
    for i in range(2,n+1):
        if num%i==0:
            return False
    return True


for i in res:
    if isPrime(i):
        cnt+=1

print(cnt)