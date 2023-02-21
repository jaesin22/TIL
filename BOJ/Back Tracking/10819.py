N = int(input())
A = list(map(int, input().split()))
visited = [0] * N
arr = []
ans = 0

def solve():
    global ans
    if len(arr) == N:
        total = 0
        for i in range(N-1):
            total += abs(arr[i] - arr[i+1])
        ans = max(ans, total)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(A[i])
            solve()
            visited[i] = 0
            arr.pop()

solve()
print(ans)