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
### 메소드 실행에서의 this
#### 메소드 실행에서의 this는 메소드를 소유하고 있는 객체를 가리킨다.   객체 내부의 속성으로 정의된 함수가 실행될 때, this는 객체 자신이 되는 것이다.
```javascript
var myObject =  {
    myMethod : function() {
        this; 
    }
};
myObject.myMethod(); // 여기서는 myObject가 this가 된다.
```
-------------
### Arrow Function에서의 this
#### Arrow Function에서 this는 arrow function이 정의된 곳의 문맥을 그대로 따른다.
```javascript
function es6this() {
    console.log('Inside `objFunction`: ', this.foo); // 13
        foo: 25,
    bar: () => console.log('Inside `bar`:', this.foo) // 13
  };
}
objFunction.call({foo: 13}).bar();
```
#### 출력값은 둘 다 13이 된다. arrow function이 자신을 둘러싼 환경의 this 문맥을 그대로 따르기 때문이다. 9라인에서 간접 실행이 일어나며 this의 문맥이 결정되면 arrow function도 그대로 따른다. 따라서 arrow function은 실행 도중 this의 스코프를 바꾸고 싶지 않을 때 유용하다.


### 참고: https://kim-solshar.tistory.com/42 [김솔샤르의 인사이트]