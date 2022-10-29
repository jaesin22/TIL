import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
A = int(input())
cnt = 0
j = len(numbers) - 1
i = 0
numbers.sort()
while (i < j):
    if numbers[i] + numbers[j] == A:
        cnt += 1
        i += 1
        j -= 1
    elif numbers[i] + numbers[j] < A:
        i += 1
    else:
        j -= 1
print(cnt)
