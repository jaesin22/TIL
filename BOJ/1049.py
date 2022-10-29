import sys
input = sys.stdin.readline

n,m = map(int,input().split())

pricePackage = [[0] for _ in range(m)]
priceOne = [[0] for _ in range(m)]

for i in range(m):
    package, one = map(int,input().split())
    pricePackage[i] = package
    priceOne[i] = one

minOne = min(priceOne)
minPackage = min(pricePackage)

NumOfPackage, NumOfOne = 0, 0
if minOne * 6 >= minPackage: #패키지 가격이 제일 쌀떄
    NumOfPackage = n // 6
    NumOfOne = n % 6
    
    if minPackage <= (NumOfOne * minOne): #나머지 개수를 개당 가격으로 곱했는데 패키지 가격보다 비싸면 그냥 패키지 한개 사주고 개당은 안삼
        NumOfPackage +=1
        NumOfOne = 0
else:
    NumOfOne = n

print(NumOfPackage * minPackage + NumOfOne * minOne)