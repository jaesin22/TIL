def solution(dartResult):
    answer = 0
    arr = []
    A = ''
    for i in dartResult:        
        if i.isdigit():
            A += i
            continue
        else:
            if i == 'D':
                B = int(A)
                answer += B**2
                arr.append(B**2)
            elif i == 'S':
                B = int(A)
                answer += B
                arr.append(B)
            elif i == 'T':
                B = int(A)
                answer += B**3
                arr.append(B**3)
            elif i == '*':
                if(len(arr)) == 1:
                    arr[-1] *= 2
                else:
                    arr[-1] *= 2
                    arr[-2] *= 2


            elif i == '#':
                arr[-1] *= -1

            A = ''
    print(sum(arr))
    return sum(arr)