## 자료구조와 알고리즘 성능 1 : 가상 컴퓨터 + 가상 언어 + 가상 코드

#### 자료구조 + 알고리즘 -> 코드(c, java, python) 곧 컴퓨터 -> HW/SW 상이, 다양한 크기 입력

+ 가상컴퓨터(Virtual Machine) + 가상 언어(pseudo language) + 가상코드(Pseudo Code)

+ 가상 컴퓨터 : Turing Machine --> von Neumann : RAM(Random Access Machine)
    * RAM = CPU + Memory + 기본연산(단위 시간에 수행되는 연산)
    * 기본 연산:
        - 배정, 대입, 복사 연산 : A(쓰기) = B(읽기) : 1시간
        - 산술연산 = +, -, *, / : 1시간
        - 비교연산 : > >= < <= == !=    A < B <-> A-B < 0
        - 논리연산 : AND, OR, NOT 
        - 비트연산 : bit-AND, OR, NOT

    * 위의 연산을 1단위시간으로 할 수 있는 기본연산으로 정의한 가상의 컴퓨터를 램 모델이라 부른다.

+ 가상 언어(pseudo/ virtual Languages)
    - 배정, 산술, 비교, 논리. bit-논리 : 기본연산 표현
    - 비교 : if, if-else, else-if(elif) .... else
    - 반복 : for, while 
    - 함수 : 정의 ,호출, return 

+ 가상코드(pseudo code)
algorithm ArrayMax(A, n) :



    