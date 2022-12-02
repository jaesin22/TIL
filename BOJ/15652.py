n, m = map(int, input().split())

S = []

def f(start):
    if len(S) == m:
        print(' '.join(map(str, S)))
        return
        
    

    for x in range(start, n+1):
        S.append(x)
        f(x)
        S.pop()


f(1)