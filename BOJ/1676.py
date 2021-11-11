N = int(input())
cnt = 1
num = 0
for x in range(1, N+1):
    cnt = cnt * x

n_cnt = list(map(int, str(cnt)))

for i in reversed(n_cnt):
    if i == 0:
        num = num + 1
    else:
        break

print(num)
