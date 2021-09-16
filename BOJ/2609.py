import sys
a, b = list(map(int, sys.stdin.readline().split()))

def GCD(a, b):
    if b == 0: # b가 0일 때 a를 return
        return a
    else: # a를 b로 나눈 나머지가 b의 인자로 입력된다(재귀 호출)
        print(a%b)
        return GCD(b, a%b) # a,b 나누기를 반복하여 나머지가 0이 되었을 때 수가 a과 b의 최대공약수
    

def LCM(a, b):
    g = GCD(a,b)
    return g * (a/g) * (b/g) # 최소공배수 = 최대공약수 * (a/최대공약수) * (b/최대공약수)

print(GCD(a, b))
print(int(LCM(a, b)))