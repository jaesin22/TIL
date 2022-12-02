import sys
N, L = map(int, sys.stdin.readline().split())
loc = list(map(int, sys.stdin.readline().split()))

cnt = 1
loc.sort()

start = loc[0] # 출발점
end = start + L - 0.5

for i in loc:
    if end > i:
        continue
    else:
        cnt += 1
        end = i + L - 0.5

print(cnt)