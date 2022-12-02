import sys
from collections import deque
input = sys.stdin.readline

#0 - 1 bfs 탐색
def bfs():
    graph = [-1] * 100001
    graph[N] = 0
    queue = deque()
    queue.append((N))

    while queue:
        a = queue.popleft()
        # 동생의 위치 도달 하면 리턴
        if a == K:
            return graph[a]
    # 반복문을 통해 3가지 이동 경우 확인
        for i in(a + 1, a - 1, a * 2):
            #이동하는 곳이 범위 내에 있고 이동하지 않았다면 이동
            if 0 <= i <= 100000 and graph[i] == -1:
                #순간이동일 때
                if i == a * 2:
                    graph[i] = graph[a]
                    queue.appendleft(i) # 순간이동이기에 먼저 탐색
                else:
                    graph[i] = graph[a] + 1
                    queue.append(i)


N, K = map(int, input().split())
print(bfs())


# - 0 - 1 bfs 탐색을 통해 문제를 수행한다.

# - 동생의 위치에 도달했다면 리턴하고 도달하지 못했다면 이동한다.

# - 이동은 3가지 방법을 반복문을 통해 수행한다.

# - 이동하는 곳이 범위 내에 있고 이동하지 않은 곳이라면 이동한다.

# - 순간이동이라면 이전에 초로 갱신하고 appendleft()로 탐색한다.

# - 순간이동이 아니라면 이전에 초에 +1 해주고 append()로 탐색한다. 

# - 위 탐색과정이 다른 것이 0 - 1 bfs 탐색이 된다.