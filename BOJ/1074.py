import sys

input = sys.stdin.readline
N, r, c = map(int, input().split())

result = 0
def solved(block_size, x, y):
    global result
    if x == r and y == c:
        print(result)
        sys.exit(0)

    if block_size == 1: # 정복
        result += 1
        return
    
    if not (x <= r < x+block_size and y <= c < y+block_size): # 백트래킹, 가지치기
        result += block_size*block_size
        return
    
    nbs = block_size // 2
    # 4번 재귀
    solved(nbs, x, y)
    solved(nbs, x, y+nbs)
    solved(nbs, x+nbs, y)
    solved(nbs, x+nbs, y+nbs)




solved(block_size=2**N, x=0, y=0)