# 프로퍼티

#### 자바스크립트에서 객체는 property로 구성된다.    프로퍼티는 "키" : "값"의 형식으로 지정해주면 된다.    프로퍼티에는 함수도 지정할 수 있다.
-------------
##  객체의 프로퍼티에 접근
#### 객체.프로퍼티와 같은 방식으로 접근하면 된다.

```javascript
var car = new Object();
car.make = "Ford";
car.model = "Mustang";
car.year = "1969";
```
#### car 객체를 생성한 뒤 그 안에 make, model, year 프로퍼티를 넣었다.    자바스크립트에서 객체의 프로퍼티를 추가할 때에는 단지 '객체.추가할 프로퍼티'와 같은 형식을 사용하면 된다.    이렇게 사용하면 car객체에 한해 프로퍼티를 추가할 수 있다.

## 객체 프로퍼티 나열, 순회
#### 객체 프로퍼티가 무엇인지 정확히 알아야 하는 경우 3가지 방법으로 프로퍼티를 알아낼 수 있다.

```javascript
var car = new Object();
car.make = "Ford";
car.model = "Mustang";
car.year = "1969";

//case 1
for(var i in car) {
    if(car.hasOwnProperty(i)) {
        document.write(i + "<br>");
    }
}

//case 2
document.write(Object.keys(car) + "<br>");

//case 3
document.write(Object.getOwnPropertyNames(car) + "<br>")
```