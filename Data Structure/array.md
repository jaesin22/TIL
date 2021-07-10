## 배열(array)
* 가장 기본적인 순차적인(sequential) 자료구조 [매우 기본, 중요]


### C언어
```C
int A = {2, 4, 0, 5};
// A[0] = 2, A[1] = 4, A=[2] = 0, A[3] = 5
```
* A = A 나름대로 주소 값 가지고 있음.
* A[2](쓰기) = A[2](읽기) + 1(산술)

* A[2]의 주소 : RAM
    + A[0] 주소 + 2* 4 bytes


## python : list(리스트)

```python
A = [2,4,0,5]
```

* A.append() : 맨 뒤에 6을 삼입(insert)
* A.pop() : 맨 뒤의 값을 지우고 리턴
    + A.pop(1) : A[1]을 제거하고 리턴
* A.insert(1, 10) : A[1]에 10을 삼입
    + 1번째에 값이 들어가있다면 값을 한칸씩 미룸
* A.remove(value) : A에서 value 제거
* A.index(value), A.count(value)
----------------------------------
리스트 : 용량(capacity) 자동조절(dynamic array)

```python
import sys

A = [] # 빈 리스트
print(sys.getsizeof(A)) # 28 bytes
A.append(10) # A = [10]
print(sys.getsizeOf(A)) # A 44 bytes
```

### A.append(x)의 동작 : 
```python
if A.n < A.capacity:
    A[n] = x
    A.n = n+1
    else :
        A.n == A.capacity
        B = A.capacity # *2 크기의 리스트를 새로 할당
        for i in range(n) :
            B[i] = A[i]
        del A
        A = B
        A.n = n + 1
        A[n] = x
```
