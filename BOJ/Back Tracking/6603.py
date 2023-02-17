import sys
input = sys.stdin.readline

def solve():
    if len(arr) == 6:
        print(' '.join(map(str, arr)))
        return
    


while True:
    A = list(map(int, input().split()))
    D = A.pop(0)
    visited = [0] * len(A)
    if D == 0:
        sys.exit()
    
    arr = []
