import sys
n = int(sys.stdin.readline())
dic = {}

for case in range(n):
    x = int(sys.stdin.readline())
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])