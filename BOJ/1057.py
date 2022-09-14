import sys

a,b,c = map(int, input().split())
print(a)
d = 1
numb = []
for x in range(a):
    numb.append(d)
    d = d + 1

print(numb)