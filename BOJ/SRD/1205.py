import sys
input = sys.stdin.readline

N, score, P = map(int, input().split())
if N == 0:
    print(1)
else:
    A = list(map(int, input().split()))
    A.append(score)
    A.sort(reverse=True)
    index = A.index(score) + 1
    if index > P:
        print(-1)
        sys.exit()
    else:
        if N == P and score == A[-1]:
            print(-1)
        else:
            print(index)