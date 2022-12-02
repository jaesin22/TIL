import sys
N = int(sys.stdin.readline())
grade = []

for _ in range(N):
    a,b,c,d = list(map(str,input().split()))
    grade.append( [a, int(b),int(c),int(d)])

grade.sort(key = lambda x : (-x[1] , x[2],-x[3],x[0]) ) # 마이너스(-)는 reverse라는 뜻

for i in grade :
    print(i[0])