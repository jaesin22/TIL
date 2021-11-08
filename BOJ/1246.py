n, m = map(int, input().split())
res = []

for _ in range(m):
    data = int(input())
    res.append(data)

res.sort(reverse=True)

sum = 0

results = []

for i in range(m):
    sum = res[i] * (m-i) 
    
    results.append((res[i], sum))

print(results)

res = sorted(results, key=lambda x : -x[1])


print(res[0][0], res[0][1])