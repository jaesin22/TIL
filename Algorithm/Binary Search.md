## 이진 탐색(Binary Search) 알고리즘

* 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
* 이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
    - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.


### 이진탐색의 시간 복잡도
* 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 log2 N에 비례한다.
* 예를 들어 초기 데이터 개수가 32개일 때, 이상적으로 1단계를 거치면 16개 가량의 데이터만 남습니다.
    - 2단계를 거치면 8개 가량의 데이터만 남는다.
    - 3단계를 거치면 4개 가량의 데이터만 남는다.

* 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며 시간 복잡도는O(log N)을 보장한다.

### 이진 탐색 소스코드 : 재귀 방식

```python
import sys

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target: 
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, sys.stdin.readline().split()))
# 전체 원소 입력 받기
array = list(map(int, sys.stdin.readline().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소 X")
else: 
    print(result + 1)
```
