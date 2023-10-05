## 호이스팅

호이스팅 이전에 자바스크립트에서는 어떻게 변수를 생성하는지에 대해 이해할 필요가 있다.

자바스크립트에서는 var, let, const 키워드를 붙여 변수를 생성한다.
이는 기본적으로 3단계를 거쳐서 실행되지만, 실행되는 순서가 조금씩 다르다.

let의 경우 선언 단계와 초기화 단계가 분리되어 있고, 그 사이에 TDZ가 존재한다. 이 TDZ에 접근할 경우 Reference Error가 발생한다.

const의 경우 let과는 달리 선언 단계와 초기화 단계가 동시에 실행된다. 하지만 그 전에 TDZ가 생성되어 TDZ에 접근할 경우 역시 Reference Error를 발생한다.

```javascript
// let
console.log(value); // 선언 단계 -> TDZ
let value = "Hello World"; // 초기화 단계
// ReferenceError 발생

// const
console.log(value); // TDZ
const value = "Hello World";

// ReferenceError 발생

// var
console.log(value); // undefined 출력
var value = "Hello World"; // Assignment phase

// 에러 발생 x
```

var와 let, const의 차이는 TDZ의 유무이다.
여기서 TDZ(Temporal Dead Zone)은 스코프 혹은 라이프 사이클의 시작지점부터 초기화 단계 직전까지의 구간을 의미한다.

### 호이스팅(Hoisting)

호이스팅이란 스코프(함수) 안에 존재하는 모든 선언들을 해당 스코프(함수)의 최상단으로 끌어올리는 것을 말한다.
자바스크립트 엔진은 코드를 실행하기 전에 실행 가능한 코드를 형상화하고 구분하는 과정을 거치는데, 이 과정에서 코드 실행을 위한 모든 선언들을 스코프에 등록한다.

호이스팅의 대상은 변수, 함수 총 2가지이다.

여기서 중요한 점은 선언에서만 호이스팅이 일어난다. 선언에서만 호이스팅이 일어나기 때문에 값을 할당하더라도 할당된 값은 호이스팅이 일어나지 않는다.

```javascript
console.log(value); // undefined
var value = "Hello World";

// 해당 코드에서 var가 에러가 나지 않는 이유는 값이 할당되진 않지만 선언과 동시에 undefined로 값이 초기화 되어있기 때문
```

let, const는 호이스팅이 되지 않는다 라고 생각했는데, let과 const도 호이스팅은 된다.
다만 아무런 값이 할당이 되어있지 않기 때문에 에러가 나는 것 뿐..

함수 선언의 경우 선언, 초기화, 할당을 동시에 진행한다. 때문에 TDZ도 존재하지 않는다.

함수 선언식으로 생성된 fun1 함수와 fun2 함수가 있다.
fun1 함수의 경우 제대로 호출되지만 fun2 함수의 경우 함수가 할당되지 않은 것을 볼 수 있다.
호이스팅은 선언만 스코프(함수)의 위로 끌어올리기 때문에 함수를 할당할지라도 할당한 값은 호이스팅 되지 않기 때문에 에러가 발생한다.

```javascript
fun1();
fun2();

function fun1() {
  console.log(value);
  var value = "Hello World";
}
// undefined

var fun2 = function () {
  console.log(value);
  var value = "Hello World";
};
// TypeError: fun2 is not a function
```

결론 : 의도치 않은 동작을 방지하기 위해 var 대신 let 사용을 지향하자.
