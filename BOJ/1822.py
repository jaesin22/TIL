import sys

A, B = map(int, sys.stdin.readline().split())

C = set(list(map(int, sys.stdin.readline().split())))
D = set(list(map(int, sys.stdin.readline().split())))
E = C - D


print(len(E))
F = sorted(E)
for x in F:
    print(x, end = ' ')