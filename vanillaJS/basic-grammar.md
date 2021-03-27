# 자바스크립트 기초 용어 정리

## NaN(Not a Number)
#### 표현 불가능한 수치형 결과를 나타냄.
#### Math.sqrt(-9) -> 음수의 제곱근은 허수임. 허수는 자바스크립트에서 표현 불가

### NaN 사용 방법 예시
```javascript
var num = 0/0;
if(isNaN(num)) {
    num = 0;
}
```
#### `isNaN()` 함수는 인자로 받은 값이 `NaN`이거나 숫자가 아닐 시 `true`를 반환한다.


## 이벤트 핸들러(Event Handler)
#### 영어 뜻 그대로 이벤트에 대한 동작을 다룬다 라는 뜻.

#### 쉽게 생각하면 마우스가 버튼에 닿았을 때는 Action이고, 닿았을 때 버튼 색깔이 변하는 건 사건에 대한 동작이다.    이 2개를 묶은 것이 이벤트 핸들러

### 이벤트 핸들러의 종류 
-------------
#### OnClick, onKeyUp, onSelect 등등 여러가지가 있다.

## property
#### 기본적으로 property는 어떤 값을 나타낸다. 그런데 이 값이 다른 값과 연관을 가지고 있을 때 property라고 부른다.


## method(메소드)
#### 프로퍼티의 값으로 함수가 올 수도 있는데, 이러한 프로퍼티를 메소드라고 한다.
```javascript
var person = {
    person.age = 20
    person.birthday = 2000.6.8
    person.style = function() { // 이 부분이 메소드0
        console.log("nice style");
    }

person.style() // nice style
person.style // function() {console.log("nice style"); }
}
```
#### 메소드를 참조할 때 메소드 이름 뒤에 괄호({})를 붙이지 않으면, 메소드가 아닌 프로퍼티 그 자체를 참조하게 된다.   따라서 괄호를 사용하지 않고 프로퍼티 그 자체를 참조하게 되면 해당 메소드의 정의 그 자체가 반환된다.


