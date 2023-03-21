import sys
input = sys.stdin.readline

S = list(input().rstrip())
A = list(input().rstrip())

chk = False
while A:
    if A[-1] == 'B':
        A.pop()
        A.reverse()
    elif A[-1] == 'A':
        A.pop()
    if A == S:
        chk = True
        break

if chk:
    print(1)
else:
    print(0)