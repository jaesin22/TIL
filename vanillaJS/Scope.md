## 함수의 범위(scope)

스코프는 범위라는 뜻임

### 전역 변수와 지역 변수

전역 변수란 자바스크립트에서 제일 바깥 범위(함수 안에 포함되지 않은)에 변수를 만드는 것이다. 전역 변수를 만드는 일은 최대한 지양해야 한다.

```javascript
var x = "global";
function ex() {
  var x = "local";
  x = "change";
}
ex(); // x를 바꿔본다.
console / log(x); // 여전히 'global'
```

위 코드를 보면 x여도 ex 함수 바깥의 x는 전역변수고, ex 함수 안의 x는 ex 함수의 지역변수입니다. 지역 변수는 함수 안에 들어있는 변수를 의미한다.

### 스코프(scope)

스코프를 한글로 풀면 범위라는 말이다. 범위라는 말처럼 함수 안에서 선언된 변수는 함수 안에서만 사용할 수 있다. var x = 'local'은 ex 함수 안에서만 그 데이터를 사용할 수 있다. 밑에 살짝 다른 예시를 보자.

```javascript
var x = "global";
function ex() {
  x = "change";
}
ex(); // x를 바꿔본다.
console / log(x); // 'change'
```

아까와는 달리 ex 함수 안에서 var를 선언하지 않았다. ex 함수 안에서 x=change를 했을 때 전역변수 값이 바뀌었다. 그 이유는 자바스크립트는 변수의 범위를 호출한 함수의 지역 스코프부터 전역 변수들이 있는 전역 스코프까지 점차 넓혀가며 찾기 때문이다. 첫 번째 예시에서는 ex 범위 안에 바로 x(ex의 지역 변수)가 있었기 때문에 지역 변수 x를 바꾸고, 전역 변수 x는 바꾸지 않았다.

### 스코프 체인

전역 변수와 지역 변수의 관계에서 스코프 체인이라는 개념이 나온다. 내부 함수에서는 외부 함수의 변수에 접근이 가능하지만, 외부 함수에서는 내부 함수의 변수에 접근할 수 없다. 아래 enemy가 undefined인 것을 보면 알 수 있다.

```javascript
var name = "zero";
function outer() {
  console.log("외부", name);
  function inner() {
    var enemy = "nero";
    console.log("내부", name);
  }
  inner();
}
outer();
console.log(emeny); // undefined
```

inner 함수는 name 변수를 찾기 위해 먼저 자기 자신의 스코프에서 찾고, 없으면 한 단계 올라가 outer 스코프에서 찾고, 없으면 다시 올라가 전역 스코프에서 찾는다. 전역 스코프에서 name 변수를 찾아서 'zero'라는 값을 얻었다. 만약 전역 스코프에도 없다면, 변수를 찾지 못햇다는 에러가 발생한다.
이렇게 꼬리를 물고 계속 범위를 넓히면서 찾는 관계를 스코프 체인이라고 부른다.

### 렉시컬 스코핑

스코프는 함수를 호출할 때가 아니라 선언할 때 생긴다. 정적 스코프라고도 불린다.

```javascript
var name = "zero";
function log() {
  console.log(name);
}

function wrapper() {
  var name = "nero";
  log();
}
wrapper();
```

위 코드의 출력은 'zero'이다. 스코프는 함수를 "선언"할 때 생긴다고 했다. log 함수 안의 name은 wrapper 함수 안의 지역 변수 name이 아니라, 전역 변수 name을 가리키고 있는 것이다. 이런 것을 lexical scoping이라고 한다.

함수를 처음 선언하는 순간, 함수 내부의 변수는 자기 스코프로부터 가장 가까운 곳(상위 범위에서)에 있는 변수를 계속 참조하게 된다. 위의 예시에서는 log 함수 안의 변수는 선언시 가장 가까운 전역 변수 name을 참조하게 된다. 그래서 wrapper 안에서 log를 호출해도 지역 변수 name='nero'를 참조하는 게 아니라, 그대로 전역 변수 name의 값인 zero가 나오게 되는 것이다.
