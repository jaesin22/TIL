a = int(input())

for x in range(a):
    c = list(input())

    while len(c) != 0:
        if c[0] == ')':
            print('NO')
            break
        else:
            if ')' in c:
                c.remove(')')
                c.remove('(')
            else:
                print("NO")
                break
    if len(c) == 0: print("YES")