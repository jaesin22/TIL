## 순차적 자료구조(Seguential Data Structures) 소거

1. 배열, 리스트
    - index로 임의의 원소를 접근
    - 연산자 [] A[2] = 1
    - 삼입(append, insert)
    - 삭제(pop, remove)
2. stack, queue, dequeue
    - 제한된 접근(삽입, 삭제)만 허용
* stack : LIFO(Last In First Out), 차근차근 위로 올라가면서 쌓이듯이 삽입됨. 삭제될 때는 맨 위에 값부터 삭제됨.
* queue : FIfO(First In First Out), 선착순, 차근차근 위로 올라가면서 쌓이듯이 삽입됨. 삭제될 때는 들어온 순서대로 삭제됨.
* dequeue : stack + queue 

3. linked list(연결 리스트)
연결되지 않은 독립된 공간에 띄어져 있음, 연속되지 않게 저장됨 