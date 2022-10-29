import sys
input = sys.stdin.readline
N, M=map(int,input().split())
A = 1
for i in range(M):
	A *= N-i
	A //= i+1
print(A)