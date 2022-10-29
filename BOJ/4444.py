import sys
input = sys.stdin.readline
N = int(input())

dp_table = [0] * (N+1)
dp_table[1] = 1
dp_table[2] = 2

for x in range(3, N+1):
    dp_table[x] = dp_table[x-1] + dp_table[x-2]

print(dp_table[N]%10007)