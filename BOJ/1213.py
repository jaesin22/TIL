paper = ...

def isFilledSquare(y,x,n):
    for i in range(y, y+n):
        for j in range(x, x+n):
            if paper[i][j] != paper[y][x]:
                return False
    return True


def cut(y,x,n):
    if n == 1 or isFilledSquare(y,x,n):
        if paper[y][x] == 0:
            return [1,0]
        else:
            return [0,1]
    else:
        n2 = n/2
        lu = cut(y,x,n2)
        ru = cut(y,x+n2,n2)
        ld = cut(y+n2,x,n2)
        rd = cut(y+n2,x+n2,n2)
        
        return [
            lu[0] + ru[0] + ld[0] + rd[0],
            lu[1] + ru[1] + ld[1] + rd[1],
        ]
    
rst = cut(0,0,8)

# 나중에 다시 풀어볼 것