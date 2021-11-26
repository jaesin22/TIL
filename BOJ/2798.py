import sys
N, M = map(int, sys.stdin.readline().split())

card = list(map(int, sys.stdin.readline().split()))

total = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            total.append(card[i] + card[j] + card[k])

total = list(set(total))

total.sort(reverse=True)
for x in range(len(total)):
    if total[x] <= M:
        print(total[x])
        break

