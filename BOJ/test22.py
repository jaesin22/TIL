from itertools import permutations

arr = ['김', '이', '박', '최', '심', '안', '유', '지', '남', '신', '현', '재', '승', '영', '진', '나', '다', '지', '경', '강', '민', '균', '승', '성', '린', '희', '연', '영']

res = list(permutations(arr, 3))

for i in res:
    print(i)