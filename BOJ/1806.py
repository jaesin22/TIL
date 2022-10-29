import sys
input = sys.stdin.readline
N, S = map(int, input().split())

items = []
for _ in range(N):
    items.append(list(map(int, input().split())))

j = len(items)-1

i = 0
# while i < j:
#     if items[i] + items[j] == S:
#         print()
