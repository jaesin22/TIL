import sys
N = int(sys.stdin.readline())
cnt = 0

res = []
for _ in range(N):
    res.append(int(sys.stdin.readline()))


for i in range(N-1, 0,-1):
    if res[i] <= res[i -1]:
        cnt += res[i -1] - res[i] + 1 # 1. 3, 2. pass, 3. 
        res[i - 1] = res[i] - 1 

print(cnt)