s = input()
cnt = 0
prev = '?'

for i in s:
    if i != prev:
        prev=i
        cnt += 1

print((cnt) // 2)