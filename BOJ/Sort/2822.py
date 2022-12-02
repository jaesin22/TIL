arr = []
res = []
cnt = 0
for x in range(8):
    arr.append(int(input()))


for i in range(5):
    cnt += max(arr)
    idx = arr.index(max(arr))
    res.append(idx+1)
    arr[idx] = 0

print(cnt)
print(*(sorted(res)))