import sys
K = int(sys.stdin.readline())
res = []
for x in range(K):
    y = int(sys.stdin.readline())
    if y == 0:
        res.pop(-1)
    else:
        res.append(y)

print(sum(res))