import sys
input = sys.stdin.readline

N = int(input())
egg = []
S, W = 0, 1
for i in range(N):
    a, b = map(int, input().split())
    egg.append([a, b])

res = 0
def solve(idx):
    global res
    if idx == N:
        eggs = 0
        for i in range(N):
            # 계란이 깨져있으면
            if egg[i][S] <= 0:
                eggs += 1
        res = max(res, eggs)
        return

    # 자기가 깨져있는 경우 다음 계란으로
    if egg[idx][S] <= 0:
        solve(idx + 1)
        return
    
    # 자기 말고 다 깨져있는 상황인 경우
    chk = True
    for target in range(N):
        # 자기 자신은 제외
        if target == idx:
            continue
    
        if egg[target][S] > 0:
            chk = False
            break
    
    if chk:
        res = max(res, N - 1)
        return
    
    # 때려보기
    for target in range(N):
        if target == idx:
            continue
        # 이미 깨졌으면 continue
        if egg[target][S] <= 0:
            continue

        egg[idx][S] -= egg[target][W]
        egg[target][S] -= egg[idx][W]
        solve(idx + 1)
        # 복구
        egg[idx][S] += egg[target][W]
        egg[target][S] += egg[idx][W]


solve(0)
print(res)
