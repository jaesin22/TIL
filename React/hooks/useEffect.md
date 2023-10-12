## useEffect란?

한 마디로 useEffect hook은 "리액트 컴포넌트가 렌더링 될 때마다 특정 작업을 실행할 수 있도록 하는 Hook"이다. class 컴포넌트 때는 라이프사이클이 컴포넌트에 중심이 맞춰져 있었다. 그러나 함수 컴포넌트에서는 조금 다르게 적용한다. 특정 데이터에 대해서 라이프사이클이 진행된다.

데이터는 여러 개일 수 있으므로 클래스 컴포넌트에서는 componentWillMount,
componentDidMount, componentDidUpdate, componentWillUnmount를 컴포넌트 당 한 번씩만 사용했다면, useEffect는 데이터의 개수에 따라 여러 번 사용하게 된다.

아래 예시를 보자.

```javascript
useEffect(() => {
  console.log("variable change");
}, [num]);
```

위 코드는 컴포넌트가 첫 렌더링될 때 한 번 실행되고, 그 다음부터는 num 변수의 값이 바뀔 때 마다 실행된다.

특수한 경우도 있다.

```javascript
useEffect(() => {
  console.log("variable change");
}, []);
```

위의 코드를 보면 배열이 빈 배열이다. deps가 없어서 변경되는 것이 없으므로 처음 한 번만 실행되고 나서 다시는 재실행 될 일이 없다. 단, 컴포넌트가 언마운트될 때는 return의 함수가 실행된다.
