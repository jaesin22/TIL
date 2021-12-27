N = int(input())

cnt = 0

for i in range(1, N+1):
    array = list(map(int, str(i)))
    if i < 100:
        cnt += 1
    elif array[0] - array[1] == array[1] - array[2]:
        cnt += 1

print(cnt)
