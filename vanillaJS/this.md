# this

## this의 기본 개념
1. 함수 실행시에는 전역(window) 객체를 가리킨다.
2. 메소드 실행시에는 메소드를 소유하고 있는 객체를 가리킨다.
3. 생성자 실행시에는 새롭게 만들어진 객체를 가리킨다.

#### this는 기본적으로 window이다. 
```javascript
function a{ console.log(this)};;
a(); // window {}
```
#### 기본적으로는 window이지만 아닐 때인 경우가 있다.
```javascript
var obj = funtcion(){
    console.log(this); // 여기서의 this는 obj를 가리킴
}
```
#### 위의 예제를 보면 객체의 메소드를 호출할 때 this를 내부적으로 바꿔준다(window에서 obj로).

### 생성자의 경우
```javascript
function Person(name, age) {
    this.name = name;
    this.age = age;
}
Person.prototype.sayHi = function() {
    console.log(this.name, this.age);
}
```
#### 위의 예시를 new로 호출하지 않았을 경우
```javascript
Person('Jaesin', '22')
console.log(window.name, window.age); // Jaesin 22
```
#### 그냥 함수에서 this가 window를 가리키므로 window.~~ 가 되버린다. 이것을 막으려면 Person을 호출할 때 앞에 new 를 붙여서 사용해야 한다.
```javascript
var T = new Person('Jaesin', 22) // Person{name: "Jaesin", age: 22}
T.sayHi(); // Jaesin 22
```
