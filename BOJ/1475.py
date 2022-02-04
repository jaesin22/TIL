arr = [0] * 10
cnt = 0
n = input()

for i in n:
    arr[int(i)] += 1

six_nine = arr.pop(6) + arr.pop(8)  # 6과 9가 필요한 갯수를 추출하고 삭제

if six_nine % 2 == 0:
    six_nine = six_nine//2  # 6과 9를 통틀어 필요한 개수를 계산
else:
    six_nine = six_nine//2+1

if six_nine >= max(arr):
    print(six_nine)
# 6,9와 나머지 수 중 제일 많이 카운팅된것 비교하여 출력
else:
    print(max(arr))
