from collections import Counter
card = []
score = []
res = 0
def chk_seq(score):
    for i in range(4):
        if score[i] + 1 != score[i+1]:
            return False
            
    return True
    
def one(card, score):
    flag = True
    if Counter(card).most_common(1)[0][1] == 5:
       if not chk_seq(score):
           return 0
    else:
        flag = False

    if not flag:
        return 0
    else:
        return 900 + score[-1]     

def two(card, score):
    if Counter(score).most_common(1)[0][1] == 4:
        return 800 + Counter(score).most_common(1)[0][0]
    else:
        return 0

def three(card, score):
    a = Counter(score).most_common(2)[0][1]
    b = Counter(score).most_common(2)[1][1]
    if a == 3:
        if b == 2:
            c = Counter(score).most_common(2)[0][0]
            d = Counter(score).most_common(2)[1][0]
            return c * 10 + d + 700

    return 0

def four(card, score):
    if Counter(card).most_common(1)[0][1] == 5:
        return score[-1] + 600
    else:
        return 0

def five(card, score):
    if chk_seq(score):
        return score[-1] + 500
    
    return 0

def six(card, score):
    for i in range(len(Counter(score).most_common(5))):
        if Counter(score).most_common(5)[i][1] == 3:
            return Counter(score).most_common(5)[i][0] + 400
    return 0

def seven(card, score):
    for i in range(len(Counter(score).most_common(5))):
        if Counter(score).most_common(5)[i][1] == 2:
            for j in range(i+1, len(Counter(score).most_common(5))):
                if Counter(score).most_common(5)[j][1] == 2:
                    a = Counter(score).most_common(5)[i][0]
                    b = Counter(score).most_common(5)[j][0]
                    if a < b: return b * 10 + a + 300
                    else: return a * 10 + b + 300
    return 0

def eight(card, score):
    for i in range(len(Counter(score).most_common(5))):
        if Counter(score).most_common(5)[i][1] == 2:
            return Counter(score).most_common(5)[i][0] + 200
    return 0

for _ in range(5):
    a, b = map(str, input().split())
    card.append(a)
    score.append(int(b))


score.sort()
res = max(res, one(card, score))
res = max(res, two(card, score))
res = max(res, three(card, score))
res = max(res, four(card, score))
res = max(res, five(card, score))
res = max(res, six(card, score))
res = max(res, seven(card, score))
res = max(res, eight(card, score))
if res == 0:
    res = score[-1] + 100

print(res)