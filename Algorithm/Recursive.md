## 재귀함수

* 재귀함수(Recursive Function)란 자기 자신을 다시 호출하는 함수를 의미한다.
* 단순한 형태의 제귀함수 예제
```python
def recursive_function():
    print('재귀 함수를 호출한다.')
    recursive_function()

recursive_function()
```

### 재귀 함수의 종료 조건
* 재귀함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다.
* 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있다.
    - 종료 조건을 포함한 재귀 함수 예제
```python
def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i + 1 ' 번째 재귀함수를 호출한다')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료한다.')

recursive_function(1)
```

### 팩토리얼 구현 예제
* n! = 1 * 2 * 3 * ... x(n -1) * n
* 수학적으로 0!rhk 1!의 값은 1이다.

```python
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차레대로 곱하기
    for i range(1, n + 1):
        result *= i
    return result
```

```python
# 재귀적으로 구현한 n!
def factorial_iterative(n):
     if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)를 그대로 코드 작성하기
    return n * factorial_recursive(n - 1)
```

### 최대공약수 계산(유클리드 호제법) 예제
* 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘으로는 유클리드 호제법이 있다.
* 유클리드 호제법
    - 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 하자.
    - 이때, A와 B의 최대 공약수는 B와 R의 최대공약수와 같다.
* 유클리드 호제법의 아이디어를 그대로 재귀 함수로 작성할 수 있다.
    - 예시 : GCD(192, 162)

```python
def gcd(a, b):
    if a % b == 0:
        return b
        else:
            return gcd(b, a%b)
    print(gcd(192, 162))
```