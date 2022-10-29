X = int(input())
N = int(input())

res = []
for x in range(N):
    a, b = map(int, input().split())
    res.append(a*b)

if sum(res) == X:
    print('Yes')
else:
    print('No')