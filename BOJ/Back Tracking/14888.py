N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
arr = []
min_res = int(1e9)
max_res = - int(1e9)
def solve(add, sub, mul, div, num, start):
    global max_res, min_res
    if start == N:
        max_res = max(max_res, num)
        min_res = min(min_res, num)
        return

    if add:
        solve(add-1, sub, mul, div, num + A[start], start + 1)
    if sub:
        solve(add, sub-1, mul, div, num - A[start], start + 1)
    if mul:
        solve(add, sub, mul-1, div, num * A[start], start + 1)
    if div:
        solve(add, sub, mul, div-1, int(num / A[start]), start + 1)
    
solve(add, sub, mul, div, A[0], 1)
print(max_res)
print(min_res)