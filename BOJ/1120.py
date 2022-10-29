import sys
input = sys.stdin.readline
a, b = input().split()
b = list(b)
len_a = len(a)

max_cnt = 0
while len_a <= len(b):
    cnt = 0
    for i in range(len_a):
        if a[i] == b[i]:
            cnt += 1
    max_cnt = max(max_cnt, cnt)
    del b[0]
print(len_a - max_cnt)