N = int(input())
star = '*'
space = ' '
cnt = N-1
star_cnt = 1
for x in range(N):
    for y in range(cnt):
        print(space, end="")
    cnt = cnt - 1
    for i in range(star_cnt):
        print(star, end="")
    print('')
    star_cnt += 2