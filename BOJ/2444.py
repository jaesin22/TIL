N = int(input())

for i in range(1, N+1):
    print(' '*(N-i), '*'*(i-1), '*', '*'*(i-1), sep='')

for j in range(N-1, 0, -1):
    print(' '*(N-j), '*'*(j-1), '*', '*'*(j-1), sep='')