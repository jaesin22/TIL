N = int(input())

res = 0 
for i in range(N):
    arr = []
    for j in str(i):
        arr.append(int(j))

    if sum(arr) + i == N:
        res = i
        break

print(res)