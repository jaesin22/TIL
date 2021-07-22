## 연결리스트(Linked List) - 한방향 vs 양방향
* 연결리스트 1개에 data값(key)와 link로 구성된다. key와 link를 감싸면 node
  - 가장 앞에있는 노드 -> head node'
  - 연결리스트 장점 : 배열에서 사이에 5를 insert 했을 때 배열은 한칸씩 이동을 해야 하지만, linked list는 링크를 a와 b 곧 넣을려고 하는 위치의 바로 이전의 값과 그 다음의 값을 알고 있다면 시간복잡도가 O(1)이 된다.


### 한방향 연결리스트 : pushFront, pushBack
#### 한방향 연결리스트 pushFront, pushBack 예제
```python
* L = singlyLinkedList()
* L.pushFront(5) # L에 5를 넣었을 때 예시

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def pushFront(self, key) :
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    def pushBack(self, key):
        V = Node(key)
        if len(self) == 0 : self.head = V
        else : 
            tail = self.head
            while tail.next != None: tail = tail.next
            tail.next = V
        self.size += 1

```

### 한방향 연결리스트 : PopFront, PopBack
#### PopFront, PopBack 예제
```python
def popFront(self):
    if len(self) == 0:
        return None
    else : #하나 이상의 노드 존재
        x = self.head
        key = x.key
        self.head = x.next
        self.size -= 1
        del x
        return key

def popBack(self):
    if len(self) == 0 : return None
    else :
        prev, tail = None, self.head
        while tail.next != None :
            prev = tail
            tail = tail.next
        if len(self) == 1:
            self.head = None
        else prev.next = tail.next

        key = tail.key
        del tail
        self.size -= 1
        return key
```

#### push/popfront, push/popback의 시간 복잡도 구하기
* pushFront, pushPop : O(1)
* pushBack, popBack : O(n)