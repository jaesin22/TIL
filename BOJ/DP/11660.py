from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
graph = []
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))
    
for i in range(N):
    graph.append(list(map(int, input().split())))
