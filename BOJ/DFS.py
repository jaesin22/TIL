from collections import deque

graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1


def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()  # 1 4 3 5 6 2
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
            # print(graph[n])  # {3, 4} {1} {1, 5} {2, 6} {3, 5} {3, 4, 5}
            # print(set(visited)) # {1} {1, 4} {1, 3, 4} {1, 3, 4, 5} {1, 3, 4, 5, 6} {1, 2, 3, 4, 5, 6}
            # print(graph[n] - set(visited))  # {3,4} set() {5} {2,6} set() set()

    return visited  # [1] [1, 4] [1,4,3] [1,4,3,5] [1,4,3,5,6] [1,4,3,5,6,2]


print(DFS_with_adj_list(graph_list, root_node))
print({1} - {1, 4})
