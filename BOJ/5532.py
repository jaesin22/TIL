
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

while True:
    if B > 0 or A > 0:
        L = L - 1
        B -= D
        A -= C
    else:
        break

print(L)
