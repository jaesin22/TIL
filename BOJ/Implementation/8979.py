n, k = map(int, input().split())
rank_table = []

for _ in range(n):
    ranking = list(map(int, input().split()))
    if ranking[0] != k:
        rank_table.append(ranking)
    else:
        standard = ranking

count = 1
for i in range(len(rank_table)):
    if rank_table[i][1] > standard[1]:
        count += 1

    elif rank_table[i][1] == standard[1]:
        if rank_table[i][2] > standard[2]:
            count += 1

        elif rank_table[i][2] == standard[2]:
            if rank_table[i][3] > standard[3]:
                count += 1
    