N, K = map(int, input().split())
array = [i for i in range(1,N+1)]   
result = []
num = 0

for t in range(N):
    num += K - 1
    if num >= len(array):
        num = num%len(array)

    result.append(str(array.pop(num)))

print("<",", ".join(result)[:],">", sep='')