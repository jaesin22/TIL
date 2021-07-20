## Queue
* 큐(Queue) : FIFO(First-in First-out) 규칙의 순차적 자료구조
 - stack에서 push -> Queue에서는 Enqueue
  + Enqueue(n)를 하면 배열에 순차적으로 쌓임.
 - stack에서 pop -> Queue에서는 Dequeue
  + Queue에서는 First Out이므로 stack의 pop과 다르게 처음에 들어왔던 n값이 delete됨

* dequeue 될 값이 어느 인덱스인지, enqueue는 어느 인덱스에 넣어줘야 하는지 알아야 함(stack는 하나의 인덱스만 알아도 됨)
### queue 구현 예시
```python
class Queue :
    def __init__(self) :
        self.items = [] # 빈 리스트
        self.front_index = 0

    def enqueue(self, val) :
        self.items.append(val)

    def dequeue(self) :
        if self.front_index == len(self.items) : 
            print("Q is empty")
            return None
            else : x = self.items[front_index]
            self.front_index += 1
            return x
```

### 큐 활용 예 : Josephus problem
```python
Josephus(n, k) :

```
* stack + queue = dequeue
  - python 에서는 deque라는 class를 제공함