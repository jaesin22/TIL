## 클로저(closure)의 개념

클로저는 함수가 선언될(생성될) 그 당시에 주변의 환경과 함께 갇히는 것을 말한다.

예시를 통해 알아보자.

```javascript
function sayHello() {
  const a = "Hello";
  const b = "World";

  function sumString() {
    console.log(a + " " + b);
  }

  return sumString;
}

const myFunc = sayHello();

myFunc(); // 'Hello World'
```

예제를 살펴보면, myFunc 라는 변수는 sayHello 함수를 호출하고 있다. 그래서 myFunc를 실행하게 되면 어떠한 문제 없이 Hello world가 잘 출력된다.
여기서 살펴볼 점은 myFunc의 부분은 변수 a와 b가 담겨있는 sayHello 함수 스코프의 바깥에 있는데도 불구하고 a와 b를 합친 Hello world를 잘 출력하는 점이다.

그 이유는 바로 클로저 때문이다. 모든 자바스크립트 함수는 선언(생성)될 당시에 클로저가 형성되어 주변 환경 즉 레시컬 스코프를 기억할 수 있게 된다.

### 활용 사례

#### 콜백함수 내부에서 외부 데이터를 사용할 때

```javascript
const fruits = ["apple", "banana", "peach"];
const ul = document.createElement("ul");

const fruitBuilder = function (fruit) {
  return function () {
    console.log("your choice is " + fruit);
  };
};

fruits.forEach(function (fruit) {
  let li = document.createElement("li");
  li.innerText = fruit;
  li.addEventListener("click", fruitBuilder(fruit));
  ul.appendChild(li);
});

document.body.appendChild(ul);
```

fruitBuilder라는 함수는 또 다른 익명 함수를 반환한다. 그리고 forEach문 안에 fruitBuilder 함수를 실행하면서 fruit 값을 인자로 전달한다. 그렇게 되면 함수의 실행결과 즉 console.log()가 담긴 익명 함수를 리스너에 콜백 함수로서 전달한다. 이후에 클릭 이벤트가 발생하게 되면 함수의 실행 컨텍스트가 열리면서 fruitBuilder의 인자로 넘어온 fruit를 참조하게 된다.

결론은 fruitBuilder의 실행 결과로 반환된 함수에는 클로저가 존재하게 된다.
