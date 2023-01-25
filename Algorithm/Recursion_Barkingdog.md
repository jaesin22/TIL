## 재귀

- 재귀란 하나의 함수에서 자기 자신을 다시 호출해 작업을 수행하는 알고리즘
- 단순한 형태의 제귀함수 예제

### 예제

1. 1부터 N까지의 합을 구하는 함수 만들기
2. 재귀로 N부터 1까지 출력하기

```python
# 1번
def recursive_function(i):
    if i == N:
        return
    recursive_function(i + 1)

recursive_function(1)

# 2번
def recursive_function(i):
    if i == 0:
        return
    print(i)
    recursive_function(i - 1)
recursive_function(N)
```

### 수학적 귀납법

- 예를 들어 어떤 문자열이 올바른 괄호 쌍인지 판단하는 문제를 짠다고 해보자. 여는 괄호가 넣었을 때 스택에 넣고 등등.. 각각의 상황에 따라 해야할 일이 정해져있는 코드를 짜왔다. 그러나 귀납적인 방법은 차이가 있다.
- 도미노 예시를 통해 귀납법으로 생각해보면 1번 도미노가 쓰러진다, k번 도미노가 쓰러지면 k+1 도미노도 쓰러진다가 참이니까 모든 도미노가 쓰러진다는 설명
- 재귀를 할 때는 1번 도미노가 쓰러진다, k번 도미노가 쓰러지면 k+1 도미노도 쓰러진다까지만 생각한 후에 바로 모든 도미노가 쓰러진다는 결론에 도달할 수 있어야 함. 즉 지금까지 당연하게 생각하던 절차지향적인 사고를 탈피해야 함

#### 귀납적 사고 예시

```python
def recursive_function(i):
    if i == 0:
        return
    print(i)
    recursive_function(i - 1)
recursive_function(N)
```

1. recursive_function(1)이 1을 출력한다.
2. recursive_function(k)가 k, k-1, k-2 ... 1를 출력하면 recursive_function(k+1)은 k+1, k, k-1 ... 1을 출력한다.

### 재귀 함수의 조건

- 특정 입력에 대해서는 자기 자신을 호출하지 않고 종료되더야 함(Base condition)
- 모든 입력은 base condition으로 수렴해야 한다.

### 재귀에 대한 팁

1. 함수의 인자로 어떤 것을 받고 어디까지 계산한 후 자기 자신에게 넘겨줄지 명확하게 정해야 함
2. 모든 재귀 함수는 반복문만으로 동일한 동작을 하는 함수를 만들 수 있음
3. 재귀는 반복문으로 구현했을 때에 비해 코드가 간결하지만 메모리/시간에서는 손해를 봄
4. 한 함수가 자기 사진을 여러 번 호출하게 되면 비효율적일 수 있음

### 연습 문제 1 - 거듭제곱

- 문제 : BOJ 1629번(곱셈)
- 힌트

  1. a의 n승 X a의 n승 = a의 2n승
  2. 12의 58승 = 4(mod 67) -> 12의 116승 = 16(mod 67)
  3. 1번 도미노가 쓰러진다. k번 도미노가 쓰러지면 k+1 도미노도 쓰러진다.
  4. 1승을 계산할 수 있다. k승을 계산했으면 2k승과 2k+1승도 O(1)에 계산할 수 있다.

- 답

```python
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def ac(a, b):
    if b == 1:
        return a % C

    temp = ac(a, b // 2)

    #짝수 일 때 temp * temp
    if b % 2 == 0:
        return temp * temp % C

    #홀수일 때 temp * temp * a
    else:
        return temp * temp * a % C

print(ac(A,B))
```

### 연습 문제 2 - 하노이 탑

- 문제 : BOJ 11729번(하노이 탑 이동 순서)
- 힌트

  1. n-1개의 원판을 기둥 1에서 기둥 2로 옮긴다.
  2. n번 원판을 기둥 1에서 3으로 옮긴다.
  3. n-1개의 원판을 기둥 2에서 3으로 옮긴다
     -> 원판이 n-1개일 때 옮길 수 있으면 원판이 n개일 때도 옮길 수 있다.

  - 함수의 정의
    - 원판 n개를 a번 기둥에서 b번 기둥으로 옮기는 방법을 출력하는 함수
  - base condition
    - n = 1일 때 print(a, b)
  - 재귀 식
    - n-1개의 원판을 기둥 a에서 기둥 6-a-b로 옮긴다 -> function(a, 6-a-b, n-1)
    - n번 원판을 기둥 a에서 기둥 b로 옮긴다. -> print(a, b)
    - n-1개의 원판을 기둥 6-a-b에서 기둥 b로 옮긴다. -> function(6-a-b, b, n-1)

- 답

```python
def hanoi(n, a, b):
    if n > 1:
        hanoi(n-1, a, 6-a-b)              # 기둥이 1개 이상이면 그룹으로 묶인 n-1개 원판을
                                          # 중간으로 먼저 다 옮긴다
    print(a, b)

    if n > 1:
        hanoi(n-1, 6-a-b, b)

n = int(input())

print(2**n -1)                               #총 이동해야 하는 횟수
hanoi(n, 1, 3)
```

### 연습 문제 3 - Z

- 문제 : BOJ 1074번(Z)
- 힌트

  - 함수의 정의
    - 2n \* 2n 배열에서 (r, c)를 방문하는 순서를 반환하는 함수
  - base condition
    - n = 0일 때 return 0
  - 재귀 식
    - (r,c)가 1번 사각형일 때
    - (r,c)가 2번 사각형일 때
    - (r,c)가 3번 사각형일 때
    - (r,c)가 4번 사각형일 때

- 답

```python
import sys

input = sys.stdin.readline
N, r, c = map(int, input().split())

result = 0
def solved(block_size, x, y):
    global result
    if x == r and y == c:
        print(result)
        sys.exit(0)

    if block_size == 1: # 정복
        result += 1
        return

    if not (x <= r < x+block_size and y <= c < y+block_size): # 백트래킹, 가지치기
        result += block_size*block_size
        return

    nbs = block_size // 2
    # 4번 재귀
    solved(nbs, x, y) # 1사분면
    solved(nbs, x, y+nbs) # 2사분면
    solved(nbs, x+nbs, y) # 3사분면
    solved(nbs, x+nbs, y+nbs) # 4사분면
```
