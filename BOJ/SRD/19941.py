N, K = map(int, input().split())
table = list(input())
res = 0
for i in range(len(table)):
    if table[i] == 'P':
        for j in range(i-K, i + K + 1):
            if 0 <= j < N:
                if table[j] == 'H':
                    res += 1
                    table[j] = '@'
                    break

print(res)