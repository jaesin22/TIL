N = int(input())
a, b, c = 0, 1, 1
temp = 0

for i in range(N):
    temp = c
    a = b
    b = temp
    c = a + b

print(a)
