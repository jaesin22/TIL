import sys
input = sys.stdin.readline

def binary_search(l, target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    if l[mid] == target:
        return cnt.get(target)
    
    elif l[mid] > target:
        return binary_search(l, target, start, mid - 1)
    
    else:
        return binary_search(l, target, mid + 1, end)


N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

cnt = {}
for i in A:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in B:
    print(binary_search(A, i, 0, len(A)-1), end=' ')