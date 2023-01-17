
def recursion(s, l, r, c):
    if l >= r:
        return [1, c]
    elif s[l] != s[r]:
        return [0, c]
    else: return recursion(s, l+1, r-1, c + 1)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1, 1)

N = int(input())
for i in range(N):
    A = input()
    print(isPalindrome(A)[0], isPalindrome(A)[1])