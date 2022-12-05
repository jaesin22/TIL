from itertools import permutations
N = int(input())
arr = ['1','2','3','4','5','6','7','8','9']
num = list(permutations(arr, 3))
for i in range(N):
    A, S, B = map(int, input().split())
    A = list(str(A))
    cnt = 0
    for i in range(len(num)):
        strike, ball = 0,0
        i -= cnt # num[0] 부터 조회
        for j in range(3):
            if num[i][j] == A[j]: # 입력한 숫자(한자리)와 num의 숫자(한자리) 가 같으면 strike ++
                strike += 1
            elif A[j] in num[i]: # 입력한 숫자(1자리)가 num 안에 들어있으면 ball ++
                ball += 1
        if (strike != S) or (ball != B): # 입력받은 S, B와 다르면 num에서 삭제
            num.remove(num[i])
            cnt += 1

print(len(num))

