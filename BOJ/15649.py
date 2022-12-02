N, M = map(int, input().split())

s = []

def f():
    if len(s) == M:
      #  print(s)
        print(' '.join(map(str, s)))
    
    for i in range(1, N+1):
        if i in s:
            continue
        s.append(i)
        f()
        s.pop()

f()