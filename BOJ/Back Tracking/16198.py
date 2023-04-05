N = int(input())
A = list(map(int, input().split()))
res = 0

def solve(count):
    global res
    if len(A) == 2:
        # 맨 앞구슬과 맨 뒤구슬만 남았을 때의 총합을 구해서 최대값 비교
        res = max(res, count)
        return
    
    for i in range(1, len(A) - 1):
        a = A[i-1] * A[i+1]
        temp = A[i]
        del A[i]
        solve(count + a)
         # 위에서 제거했던 구슬을 해당 위치에 다시 넣어주기
        A.insert(i, temp)

solve(0)
print(res)