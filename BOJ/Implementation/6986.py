import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(float(input()))

arr.sort()
res = []
for i in range(K, len(arr)-K):
    res.append(arr[i])

for j in range(K):
    arr[j] = arr[K]

for k in range(len(arr)-1, len(arr)-K-1, -1):
    arr[k] = arr[len(arr)-K-1]

print("{:.2f}".format(sum(res) / len(res)+ 0.00000001))
print("{:.2f}".format(sum(arr) / len(arr)+ 0.00000001))