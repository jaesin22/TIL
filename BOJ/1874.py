import sys
input = sys.stdin.readline

N = int(input())
now = 1
stack, res = [], []
flag = True

for i in range(N):
    A = int(input())
    while now <= A:
        stack.append(now)
        res.append('+')
        now += 1
    if stack[-1] == A:
        stack.pop()
        res.append('-')
    else:
        flag = False
    

if not flag:
    print('NO')
    sys.exit()

for i in res:
    print(i)
