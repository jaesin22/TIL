from collections import Counter
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(str, input().rstrip())))

cnt_arr = []
res = []
cnt = 0
for i in range(M):
    for j in range(N):
        cnt_arr.append(arr[j][i])

    counter = Counter(cnt_arr).most_common()
    counter.sort(key=lambda x : (-x[1], x[0]))
    res.append(counter[0][0])
    cnt += N - counter[0][1]
    cnt_arr = []

print(''.join(res))
print(cnt)