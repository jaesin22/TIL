# import sys
# from queue import PriorityQueue

# queue = PriorityQueue()

# N = int(sys.stdin.readline())

# for i in  range(N):
#     x = int(sys.stdin.readline())
#     queue.put(x)

#     if x == 0:
#         print(queue[])

from queue import PriorityQueue

queue = PriorityQueue()

queue.put(3)
queue.put(4)
queue.put(2)
queue.put(5)
queue.put(1)

print(queue)

for x in range(5):
    print(queue[x])