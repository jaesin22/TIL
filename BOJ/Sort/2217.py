import sys

N = int(sys.stdin.readline().rstrip())
res = []
cnt = 0

for x in range(N):
    K = int(sys.stdin.readline().rstrip())
    res.append(K)

res.sort(reverse=True)
for i in range(len(res)): 
    temp_max = res[i] * (i + 1)
    if temp_max > cnt:
        cnt = temp_max
    
print(cnt)
