import sys
input = sys.stdin.readline

def chk(x, y):
    if 0 <= x < 8 and 0 <= y < 8:
        return True
    else:
        return False

str_arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
num = ['8', '7', '6', '5', '4', '3', '2', '1']
graph = [[0] * 8 for _ in range(8)]
cnt = 0
for i in range(8):
    for j in range(8):
        graph[i][j] = str_arr[j] + num[i]

king, stone, N = map(str, input().split())
king_x, king_y = 0, 0
stone_x, stone_y = 0, 0
for i in range(8):
    for j in range(8):
        if graph[i][j] == king:
            king_x, king_y = i, j
        elif graph[i][j] == stone:
            stone_x, stone_y = i, j

arr = []
for i in range(int(N)):
    arr.append(input().strip())

x, y = 0, 0
for i in arr:
    if i == 'R':
        x, y = king_x, king_y
        king_y += 1
    elif i == 'L':
        x, y = king_x, king_y
        king_y -= 1
    elif i == 'B':
        x, y = king_x, king_y
        king_x += 1
    elif i == 'T':
        x, y = king_x, king_y
        king_x = king_x - 1
    elif i == 'RT':
        x, y = king_x, king_y
        king_x, king_y = king_x - 1, king_y + 1
    elif i == 'LT':
        x, y = king_x, king_y
        king_x, king_y = king_x - 1, king_y - 1
    elif i == 'RB':
        x, y = king_x, king_y
        king_x, king_y = king_x + 1, king_y + 1
    elif i == 'LB':
        x, y = king_x, king_y
        king_x, king_y = king_x + 1, king_y - 1

    if not chk(king_x, king_y):
        king_x, king_y = x, y

    if king_x == stone_x and king_y == stone_y:
        nx, ny = stone_x, stone_y
        stone_x += king_x - x
        stone_y += king_y - y
        if not chk(stone_x, stone_y):
            stone_x, stone_y = nx, ny
            king_x, king_y = x, y
            
print(graph[king_x][king_y])
print(graph[stone_x][stone_y])