import sys
input = sys.stdin.readline

while True:
    A = input().rstrip()
    stack = []
    if A == 'QUIT':
        sys.exit()
    elif A == '':
        continue
    else:
        if 'NUM' in A:
            B = A.split(' ')
            stack.append(int(B[1]))
        if A == 'POP':
            stack.pop()
        if A == 'INV':
            stack[-1] = -stack[-1]
        if A == 'DUP':
            stack.append(stack[-1])
        if A == 'SWP':
            temp = stack[-1]
            stack[-2] = temp
            temp = stack[-1]
        if A == 'ADD':
            break
        if A == 'SUB':
            break
        if A == 'MUL':
            break
        if A == 'DIV':
            break
        if A == 'MOD':
            break