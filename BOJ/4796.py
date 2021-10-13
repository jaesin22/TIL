import sys

i = 1
while True:
    L, P, V = map(int, sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0:
        break

    res = (V//P) *L
    res += min((V%P), L)
    print('Case %d: %d' %(i, res))
    i += 1


