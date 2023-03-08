import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().rstrip())))


res = arr.pop(0)
k = len(res)
A = []
cnt = 1

for i in range(len(res) - 1, -1, -1):
    a = res[i:k]
    a = ''.join(map(str, a))
    A.append(a)
    for j in arr:            
        s = j[i:k]
        s = ''.join(map(str, s))
        if s in A:
            cnt += 1
        else:
            A.append(s)
        
        if len(A) == N:
            print(cnt)
            sys.exit()
    A = []
