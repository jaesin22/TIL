A = input()
N = int(input())
arr = []
for i in range(N):
    arr.append(input())

res = 0
for i in arr:
    i = i * 2
    if A in i:
        res += 1
            
print(res)