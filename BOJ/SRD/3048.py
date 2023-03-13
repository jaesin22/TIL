N1, N2 = map(int, input().split())
ant1 = list(input())
ant2 = list(input())
T = int(input())
ant1.reverse()
ant = ant1 + ant2

for _ in range(T):
    for i in range(len(ant)-1):
        # 두 개미 그룹이 만났다면 위치를 바꾼다
        if ant[i] in ant1 and ant[i+1] in ant2:          
            ant[i], ant[i+1] = ant[i+1], ant[i]

             # 위치를 바꾼 개미가 선두 개미이면 반복을 멈춘다.
            if ant[i+1] == ant1[-1]:
                break

print(''.join(ant))
# CBADEF
# CBDAEF
# CDBEAF