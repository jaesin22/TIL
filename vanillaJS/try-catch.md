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
## throw 연산자
#### 자바스크립트는 Error, SyntaxError, ReferenceError, TypeError 등의 표준 에러 객체 관련 생성자를 지원한다. 이 생성자를 통해 에러 객체 생성이 가능하다.

```javascript
    let error = new Error(message);
    let syntaxError = new SyntaxError(message);
    // 등등..
```
### throw 연산자를 사용해 에러 던지기
-------------
```javascript
let json = '{ "age": 30 }'; // 불완전한 데이터

try {
  let user = JSON.parse(json); // <-- 에러 없음

  if (!user.name) {
    throw new SyntaxError("불완전한 데이터: 이름 없음"); // (*)
  }
  alert( user.name );
} catch(e) {
  alert( "JSON Error: " + e.message ); // JSON Error: 불완전한 데이터: 이름 없음
}
```
### 에러 다시 던지기
-------------
#### 다시 던지는 이유는?
#### 에러 종류와 상관없이 동일한 에러를 뿌림으로 인해 디버깅이 힘들기 때문

### 다시 던지는 기술
1. catch가 모든 에러를 받는다.
2. catch(err) {...} 블록 안에서 에러 객체 err를 분석한다.
3. 에러 처리 방법을 알지 못하면 throw err를 한다.

### 보통은 에러를 `instanceof` 명령어로 체크한다.
```javascript
if(e instanceof SystaxError) {
    alert(e.message);
} else {
    throw e;
}
```
#### 이 방법 외에도 try-catch문을 밖에다 하나 더 만들어 예상하지 못한 에러도 처리할 수 있다.


## finally

#### fianlly절은 무언가를 실행하고, 실행 결과에 상관없이 실행을 완료하고 싶을 때 사용됨.

```javascript
try {
    // 코드 실행
} catch(e) {
    // 에러 핸들링
} finally {
     // 항상 실행
}
```
## 추가 사항
1. finally 절은 try-catch 문을 빠져나가는 경우에도 실행 됨. return 을 사용해도 마찬가지
2. catch절 없이 try..finally도 사용 가능 에러 처리를 하고 싶지 않으나, 프로세스 마무리 되었는지 확실히 하고 싶은 경우에 사용



## 참고 링크 (참고라고 하지만 거의 베낀 수준..)
['try..catch'와 에러 핸들링](https://ko.javascript.info/try-catch)