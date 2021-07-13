## Stack

* stack :  삼입 : push, 삭제 : pop, top : stack 제일 위에 값 리턴, len : stack 안의 데이터 개수 출력
* 리스트 : 삼입 :  append, 삭제 : pop

```python
class Stack:
    def __init__(self):
        self.items = [] # 데이터 저장을 위한 리스트 준비

    def push(self, val):
        self.items.append(val)
    
    def pop(self):
        try: # pop할 아이템이 없으면
            return self.items.pop()
        except IndexError: # indexError 발생
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print*("Stack is empty")

    def __len__(self): # len()으로 호출하면 item 수 반환
        return len(self.items)
```
-----------------
### 예 1: 괄호 맞추기
  - (2+5) * 7 - ((3-1)/ 2+7)
  - (()())
  - 문제 : 입력 : 왼쪽과 오른쪽 괄호의 문자열이 주어진다. ex) (()()) ((())) 등등..
  - 출력 : 괄호 쌍이 맞춰져 있으면 True, 아니면 False
  - 해결 방법
    * '(' 일 때 스택에 push 하고 ')'일 때 pop을 해서 짝이 맞을 때 마다 맨 위의 스택을 비워줌. 그렇게 해서 stack의 len이 0이면 true, 0이 아니면 false
  -  코드
```python
  S = Stack() # 위에 기술해놓은 클래스 호출
  for p in parseL :
    if p == '(' : S.push(p)
    elif p == ')' S.pop()
    else : print("Not allowed Symbol")
  if len(S) > 0 : return False
  else : return True
```

### 예 2: 계산기 코드 작성
  * 2+3*5 입력
    - 이항 연산자(binary opeerator) -> 2+3, 3*5 같은 거
    - 단항 연산자(unary operator) -> +3-6 같은 거..
    - infix 수식 > 2+3*5 같은거 연산자가 피 연산자 사이에 있는 형식으로 쓰면 형식을 infix 수식
    - postfix 수식 > 2 3 5 * + 

  * 어떻게 infix를 postfix로 바꿀 수 있는가?
    1. 괄호치기 (2 +(3*5))
    2. 연산자의 오른쪽 괄호 다음으로 연산자 이동
    3. 괄호 지우기
  * 예시 3 * (2+5) * 4를 postfix로
    1. 괄호 치기 > ((3 * (2+5)) * 4)
    2. 3 2 5 4 *+*