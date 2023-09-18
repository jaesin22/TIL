from itertools import permutations
N = int(input())
arr = ['1','2','3','4','5','6','7','8','9']
num = list(permutations(arr, 3))

for _ in range(N):
    n, s, b = map(int, input().split())
    n = list(str(n))
    cnt = 0
    for i in range(len(num)):
        strike, ball = 0, 0
        i -= cnt  # num[0]부터 조회해야함
        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
            elif n[j] in num[i]:
                ball += 1

        if (strike != s) or (ball != b): # 입력받은 s,b와 다르면 num에서 삭제
            num.remove(num[i])
            cnt += 1

print(len(num))