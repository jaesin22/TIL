import sys
input = sys.stdin.readline

n,m = map(int,input().split())
rs = []

def rec():

    if len(rs) == m:
        print(' '.join(map(str,rs)))
        return
    else:
        for i in range(1,n+1):
            if i not in rs: #본인을 제외한, 이미 배열에 없는
                rs.append(i) #[1]
                rec()
                rs.pop()
        return

rec()