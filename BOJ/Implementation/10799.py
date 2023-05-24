A = list(input())

stack = []
res = 0
for i in range(len(A)):
    if A[i] == '(':
        stack.append('(')
    else:
        if A[i-1] == '(':
            stack.pop()
            res += len(stack)
        
        else:
            stack.pop()
            res += 1
            
print(res)