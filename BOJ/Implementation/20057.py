import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
sand = 0

count = 0
x, y = N // 2, N // 2

def move(cnt, dx, dy, direction):
    global sand
    


# 1. y - 1
# 2. x + 1
# 3. y + 2
# 3. x - 2
# 4. y - 3
# 5. x + 3
# 6. y + 4
# 7. x - 4
# 8. y - 5
