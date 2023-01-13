import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
M = int(input())
S = input()
A = "IOI"


for i in range(1, N):
    A = A + "OI"

print(A)
count = Counter(S)
print(count)
print(count("IOI"))
print(A)