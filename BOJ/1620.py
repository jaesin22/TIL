import sys
N, M = map(int, sys.stdin.readline().split())
book = {}

for i in range(1, N+1):
    a = sys.stdin.readline().rstrip()
    book[i] = a
    book[a] = i

for _ in range(M):
    question = sys.stdin.readline().rstrip()
    if question.isdigit():
        print(book[int(question)])
    else:
        print(book[question])