import sys
res = []

def push(X):
    res.append(X)


def pop():
    if len(res) == 0:
        print('-1')
    else:
        print(res[0])
        res.pop(0)

def size():
    print(len(res))

def empty():
    if len(res) == 0:
        print('1')
    else:
        print('0')

def front():
    if len(res) == 0:
        print('-1')
    else:
        print(res[0])


def back():
    if len(res) == 0:
        print('-1')
    else:
        print(res[-1])


N = int(sys.stdin.readline())

for x in range(N):
    A = sys.stdin.readline().rstrip()

    if A == 'pop':
        pop()
    elif A == 'size':
        size()
    elif A == 'empty':
        empty()
    elif A == 'front':
        front()
    elif A == 'back':
        back()
    else:
        B = A.split(' ')
        push(int(B[1]))
