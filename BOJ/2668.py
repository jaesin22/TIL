import sys
N = int(sys.stdin.readline())
arr = [0] # 두번째 줄 숫자 담을 리스트(범위 초과 방지를 위해 0 하나 그냥 넣어줌)

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

ans = set()

#dfs 정의
def dfs(first, second, num):
    first.add(num) # 첫번째 줄 집합에 num 추가
    second.add(arr[num]) # 두번째 줄 집합에 arr[num] 추가
    if arr[num] in first: # arr[num]이 첫번째 줄 집합에 있을 때
        if first == second: # 첫번째 줄 집합과 두번째 줄 집합이 같다면
            ans.update(first) # 결과 업데이트
            return True
        return False
    return dfs(first, second, arr[num]) # 아니라면 다음 dfs 실행


# dfs 실행
for i in range(1, N+1):
    if i not in ans:
        dfs(set(), set(), i)

print(len(ans))

for x in sorted(ans):
    print(x)