import sys
input = sys.stdin.readline
import heapq

T = int(input())
for _ in range(T):
    max_heap, min_heap = [], []
    visited = [False] * 1000001
    N = int(input())

    for i in range(N):
        a, b = map(str, input().split())
        if a == 'I':
            heapq.heappush(min_heap, (int(b), i))
            # 부호를 마이너스로 바꿔서 최소 힙에 넣어준 뒤에 최솟값부터 pop을 해줄 때 다시 부호를 바꿔주면 최대 힙과 동일하다.
            heapq.heappush(max_heap, (int(b) * -1, i))
            visited[i] = True
        elif a == 'D':
            #삭제연산시, key값을 기준으로 해당 노드가 다른힙에서 삭제된 노드인가를 먼저 판단한다.
            if b == '-1':
                # 이미 상대힙에 의해 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 계쏙 버리다가 이후 삭제대상노드가 나오면 삭제한다.
                while min_heap and not visited[min_heap[0][1]]: # visit이 False일떄 -> 해당노드가 삭제된상태
                    #min_heap[0][1] == heappush에서 넣은 i를 가리킴
                    heapq.heappop(min_heap) # 버림 (상대힙에서 이미 삭제된노드이므로)
                if min_heap:
                    visited[min_heap[0][1]] = False # visit이 Ture엿으므로 False로 바꾸고 내가 삭제함
                    heapq.heappop(min_heap)
            else:
                while max_heap and not visited[max_heap[0][1]]: #이미 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 모두 버린다.
                    heapq.heappop(max_heap) # 버림 (상대힙에서 이미 삭제된노드이므로)
                if max_heap:
                    visited[max_heap[0][1]] = False # visit이 Ture엿으므로 False로 바꾸고 내가 삭제함
                    heapq.heappop(max_heap)

    # 모든 연산이 끝난 후에도 쓰레기 노드가 들어있을 수 있으므로, 결과를 내기 전 모두 비우고 각 힙의 첫번째 원소값을 출력한다.
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')