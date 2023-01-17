import sys
input = sys.stdin.readline

def merge_sort(L):
    if len(L) == 1:
        return L
    
    mid = (len(L)+1) // 2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])

    i, j = 0, 0
    L2 = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L2.append(left[i])
            res.append(left[i])
            i += 1
        else:
            L2.append(right[j])
            res.append(right[j])
            j += 1
    
    while i < len(left):
        L2.append(left[i])
        res.append(left[i])
        i += 1
    while j < len(right):
        L2.append(right[j])
        res.append(right[j])
        j += 1

    return L2
    
N, K = map(int, input().split())
A = list(map(int, input().split()))
res = []
merge_sort(A)

if len(res) >= K:
    print(res[K-1])
else:
    print(-1)
