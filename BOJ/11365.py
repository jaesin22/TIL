while True:
    N = input()
    if N == 'END':
        break
    rev_N = "".join(reversed(N))
    print(rev_N)