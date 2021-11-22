from collections import deque
graph_list = {
    1: set([3, 4]),
    2: set([3, 4, 5]),
    3: set([1, 5]),
    4: set([1]),
    5: set([3, 5])
}

root_node = 1


def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        # print(n)  # 1 3 4 5
        if n not in visited:  # n 값이 visited에 없을 때
            visited.append(n)  # visited에 n을 삼입
            # print(graph[n]) # {3, 4} {1, 5} {1} {3,5}
        # print(set(visited)) # {1} {1, 3} {1, 3, 4} {1, 3, 4, 5}
        # print(graph[n] - set(visited))  # {3, 4} {5} set() set()
        queue += graph[n] - set(visited)
        print(queue)  # deque([3, 4]) deque([4, 5]) deque([5]) deque([])
    return visited


print(BFS_with_adj_list(graph_list, root_node))


print({1, 6} - {1, 6})
