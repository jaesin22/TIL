import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())


graph = [[] for _ in range(N + 1)]

visited = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(root, tree, parents):
    for i in tree[root]:
        if parents[i] == 0:
            parents[i] == root
            DFS(i, tree, parents)


DFS(1, graph, visited)

for i in range(2, N+1):
    print(visited[i])
