N = int(input())
cnt = 0
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(key = lambda x : (x[0], x[1]))

time = 0
for i in range(N):
    start, end = arr[i][0], arr[i][1]
    if time < start:
        time = start
    time += end

print(time)