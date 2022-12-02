S = input()
res = []
for i in range(len(S)):
    res.append(S)
    S = S[1:len(S)]

for x in sorted(res):
    print(x)
