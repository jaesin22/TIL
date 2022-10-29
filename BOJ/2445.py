N = int(input())

for x in range(1, N+1):
    print('*'*x+ ' '*(2*(N-x)) + '*'*x)

for y in range(N-1, 0, -1):
    print('*'*y +  ' '*(2*(N-y)) + '*'*y)
