N = int(input())
cnt = 0
for x in range(N*2-1,1,-2):
    print(' '*cnt + '*'*x)
    cnt += 1

for x in range(1, N*2+1, 2):
    print(' '*cnt+ '*'*x)
    cnt -= 1
