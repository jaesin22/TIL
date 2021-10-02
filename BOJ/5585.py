import sys

N = int(sys.stdin.readline())

money = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in money:
    cnt += N // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    N %= coin

print(cnt)
