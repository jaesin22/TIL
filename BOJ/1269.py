import sys
input = sys.stdin.readline
A, B = map(int, input().split())

arr = []
for x in range(2):
    key = list(map(int, input().split()))
    arr.append(key)

A = list(set(arr[0]) - set(arr[1])) # 집합으로 만들어 빼기
B = list(set(arr[1]) - set(arr[0]))
print(len(A) + len(B))