import sys

count={}
N = int(sys.stdin.readline())

for _ in range(N):
    book = sys.stdin.readline().rstrip()
    if book not in count:
        count[book] = 1
    else:
        count[book] +=1 

target = max(count.values())
arr = []

for book, number in count.items():
    if number == target:
        arr.append(book)
print(sorted(arr)[0])