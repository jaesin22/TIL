from re import A
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
res = []
a_index, b_index = 0,0


while  a_index < N and b_index < M:
    if arr_a[a_index] <= arr_b[b_index]:
        res.append(arr_a[a_index])
        a_index += 1
    else:
        res.append(arr_b[b_index])
        b_index += 1

while a_index < len(arr_a):
    res.append(arr_a[a_index])
    a_index += 1

while b_index < len(arr_b):
    res.append(arr_b[b_index])
    b_index += 1

print(*res)