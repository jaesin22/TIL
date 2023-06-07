# 다시 풀어볼 것
import sys
input = sys.stdin.readline

N = int(input())


# 파라미터로 전달받은 수열의 값에서 발생할 수 있는 모든 대칭 성분을 조사하여 대칭이 발생하는지 확인한다.
# 만약 조사 과정 중 대칭이 존재한다면 False 를 반환하고 대칭이 존재하지 않는다면 True를 반환한다.
def chk(seq):
    for i in range(1, len(seq) // 2 + 1):
        if seq[-2*i:-i] == seq[-i:]:
            return False
    return True


def recursion(seq):
    if N == len(seq):
        print(seq)
        sys.exit()

    for i in range(1, 4):
        if chk(seq+str(i)):
            recursion(seq+str(i))

recursion('1')
