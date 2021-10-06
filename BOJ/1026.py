N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

def array(N, A, B):
     cnt = 0
     A.sort(reverse = True)
