import sys

N = int(sys.stdin.readline())

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                N -= 1

print(N)