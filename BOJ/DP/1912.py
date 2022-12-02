import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * 100001

seq = list(map(int, input().split()))


for i in range(1, N):
    seq[i] = max(seq[i], seq[i-1] + seq[i])

print(max(seq))

#예시 리스트 : seq=[10,-3,3,1,5,6,-35,12,21,1]
# 위 리스트에서 i=8일 때 max(seq[8], seq[7] + seq[8])을 비교하게 되면
# # max(21,33)로서 max인 수 33이 seq[8]에 저장되게 된다.
# 이렇게 i=1부터 9까지 seq[1-9]를 초기화시키고
# 마지막에 print(max(seq))를 출력하면 그 안에서 max인 값이 출력되면서 풀이 끝!