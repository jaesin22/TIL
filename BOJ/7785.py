import sys
n = int(sys.stdin.readline())

res = []
for x in range(n):
    A, B = list(sys.stdin.readline().rstrip().split())

    if B == 'enter':
        res.append(A)
    elif B == 'leave':
       res.remove(A)

res.sort(reverse=True)
for i in res:
    print(i)