i,a = 1,0
x = int(input())
while x > a:
    b = a
    a += i
    i += 1
d = x-b
print(d,'/',i-d,sep='')