# 자바스크립트 try-catch 정리

## try-catch를 쓰는 이유

#### 에러가 발생했을 때, 스크립트가 죽는 것을 방지하고, 에러를 잡아서 후 처리를 하기 위함
-------------
## 기본적인 예외처리 문법 예시
```javascript
try {
    ....
} catch(err) {
    ....
}
```

## 동작 순서
 1. 먼저 try {} 안의 코드가 실행된다.
 2. 에러가 없다면 try의 마지막 줄 까지 실행됨.
 3. try문 실행 중 에러가 있다면, 실행이 중단되고, catch문으로 넘어가 매개변수 err가 error 객체 던짐
 -------------

## 동작 예시
#### 에러가 없는 예시는 그냥 실행되므로 건너 뜀.

### 에러가 있는 예시
```javascript
try {
    const str = 'test';
    detail(); // <- detail 함수가 없으므로 실행이 안됨.
} catch(err) {
    console.log(err); // 에러 메세지 확인
}
```
## 추가 사항

1. 추가적으로 문법이 잘못된 경우에는 try-catch 동작 안함
2. setTimeout 함수 내부의 예외를 잡으려면 함수 내부에 try-catch를 구현해야 함.
-------------

## 에러 객체

#### 위에 catch 문에 있는 err 변수가 error 객체임. 변수 이름은 상관없음
#### 추가적으로 catch문에서 err 안쓰고도 사용 가능

1. err.name > error의 name 값
2. err.message > 에러 세부 내용
3. err.stack > 호출 스택(?)
-------------
