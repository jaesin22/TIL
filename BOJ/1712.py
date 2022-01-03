A, B, C = list(map(int, input().split()))

if C <= B:
    print('-1')
else:
    print(int(A / (C-B) + 1))
