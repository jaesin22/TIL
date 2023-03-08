import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(str(input().strip()))

for i in range(1, len(arr[0]) + 1):
    res = []
    for j in range(N):
        if arr[j][-i:] in res:
            break
        else:
            res.append(arr[j][-i:])

    if len(res) == N:
        print(i)
        break