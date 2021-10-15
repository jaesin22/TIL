import sys
from collections import Counter

N = int(sys.stdin.readline())
res = []
for x in range(N):
    res.append(int(sys.stdin.readline()))


print(round(sum(res) / N)) # 1
res.sort()
result = Counter(res)
print(res[N // 2]) # 2
sorted_result = sorted(result.items(), key=lambda x: (-x[1], x[0]))
if len(res) > 1:
    if sorted_result[0][1] == sorted_result[1][1]:
        print(sorted_result[1][0])
    else:
        print(sorted_result[0][0])
else:
    print(sorted_result[0][0])


print(res[-1] - res[0]) # 4째줄