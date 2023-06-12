import sys
input = sys.stdin.readline
tree = {}
V = int(input())
for i in range(V):
    A = list(map(int, input().split()))
    tree[A[0]][A[1]] = A[2]

print(tree)
