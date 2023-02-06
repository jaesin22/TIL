import sys
input = sys.stdin.readline

T, W = map(int, input().split())
arr = []
dp = [0] * T
for i in range(T):
    arr.append(int(input()))

