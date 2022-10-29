N = int(input())
star = '*'
space = ' '
space_cnt = 0
cnt = 1
res = []
for x in range(N):
    res.append(cnt)
    cnt += 2

res.sort(reverse=True)

for x in res:
    for i in range(space_cnt):
        print(space, end='')
    space_cnt += 1
    for y in range(x):
        print(star, end='')
    print('')
