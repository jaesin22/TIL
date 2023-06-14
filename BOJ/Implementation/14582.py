A = list(map(int, input().split()))
B = list(map(int, input().split()))

a, b = 0, 0
flag = False
for i in range(9):
    a += A[i]
    if a > b:
        flag = True
    b += B[i]
if flag:
    print('Yes')
else:
    print('No')