from collections import Counter
import sys

n = sys.stdin.readline().rstrip()
card = list(map(int,sys.stdin.readline().split()))
m = sys.stdin.readline().rstrip()
test = list(map(int,sys.stdin.readline().split()))

count = Counter(card)

for i in range(len(test)):
    if test[i] in count:
        print(count[test[i]], end=' ')
    else:
        print(0, end=' ')