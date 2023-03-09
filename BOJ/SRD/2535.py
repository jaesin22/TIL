N = int(input())
arr = []
for i in range(N):
    country, number, score = map(int, input().split())
    arr.append((country, number, score))

arr.sort(key = lambda x : (-x[2], -x[0]))

cnt = 0
res = []
cnt_arr = []
for i in range(len(arr)):
    if len(res) == 3:
        break
    cnt_arr.append(arr[i][0])
    if cnt_arr.count(arr[i][0]) > 2:
        continue
    else:
        res.append((arr[i][0], arr[i][1]))

for i in res:
    print(i[0], i[1])