import sys
import math

def isPrime(num):
    #만약 1이라면 소수가 아니므로 false
    if num ==1 : return False

    #제곱근까지만 확인
    sq = int(math.sqrt(num))

    for i in range(2, sq+1):
        #나눠지면 소수가 아님
        if num % i == 0 : return False
    
    return True

#자연수 M과 N 입력
M, N = map(int, sys.stdin.readline().split())

#M부터 N까지 소수면 소수 출력
for i in range(M, N+1):
    if isPrime(i):
        print(i)
