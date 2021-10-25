import sys
T = int(sys.stdin.readline())
res = 0
for x in range(T):
    a, b = map(int, sys.stdin.readline().split())
    A, B = a, b
    while a != 0:
        b = b % a
        a, b = b, a

    lcm = A * B //b

    print(lcm)

