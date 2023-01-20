N, M = map(int, input().split())

S = set()
for i in range(N):
    S.add(input().strip())

cnt = 0
for i in range(M):
    A = input().rstrip()
    if A in S:
        cnt += 1

print(cnt)
