import sys
N = list(map(int, sys.stdin.readline().split()))

S_CNT = list(map(int, sys.stdin.readline().split()))

team = list(map(int, sys.stdin.readline().split()))

def solve(S,R):
    que_S = S.copy() 
    que_S = sorted(que_S)
    que_R = R.copy()
    for s in que_S:
        if s-1 in que_R: que_R.remove(s-1)
        elif s+1 in que_R: que_R.remove(s+1)
    res = len(S)-(len(R)-len(que_R))
    return res
    
print(solve(S_CNT, team))