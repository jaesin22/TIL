## REST API

### REST API란

- RESTful API는 HTTP 프로토콜을 기반으로하는 웹 서비스 아키텍처입니다. 자원, 메소드, 메시지 등을 정의하여 클라이언트-서버 간의 통신을 가능하게 한다. 또한, RESTful API는 표준 HTTP 메소드(GET, POST, PUT, DELETE)를 사용하여 서버와 통신한다.
- REST API의 정의
  - REST 기반으로 서비스 API를 구현한 것
  - 최근 오픈 API나 마이크로 서비스 등을 제공하는 업체 대부분은 REST API를 사용한다.

### REST API의 특징

- REST는 HTTP 표준을 기반으록 구현하므로, HTTP를 지원하는 프로그램 언어로 클라이언트, 서버를 구현할 수 있다.
- 즉, REST API를 제작하면 델파이 클라이언트 뿐 아니라, 자바, C#, 웹 등을 이용해 클라이언트를 제작할 수 있다.

### REST API 설계 기본 규칙

참고 용어

- 도큐먼트 : 객체 인스턴스나 데이터베이스 레코드와 유사한 개념
- 컬렉션 : 서버에서 관리하는 디렉터리라는 리소스
- 스토어 : 클라이언트에서 관리하는 리소스 저장소

1. URI는 정보의 자원을 표현해야 한다.

   1. resource는 동사가 아닌 명사를, 대문자가 아닌 소문자를 사용한다.
   2. resource의 document 이름으로는 단수 명사를 사용해야 한다.
   3. resource의 컬렉션 이름으로는 복수 명사를 사용해야 한다.
   4. resource의 스토어 이름으로는 복수 명사를 사용해야 한다.
      - ex. GET /Member/1 -> GET /members/1

2. 자원의 대한 행위는 HTTP Method(GET, PUT, POST, DELETE)
   1. URI에 HTTP Method가 들어가면 안된다.
      - ex. GET /members/delete/1 -> DELETE /members/1
   2. URI에 행위에 대한 동사 표현이 들어가면 안된다(즉, CRUD 기능을 나타내는 것은 URI에 사용하지 않는다.)
      - ex. GET /members/show/1 -> GET /members/1
      - ex. GET /members/insert/2 -> POST /members/2
   3. 경로 부분 중 변하는 부분은 유일한 값으로 대체한다.(즉, :id는 하나의 특정 resource를 나타내는 고유 값이다.)
      - ex. students를 생성하는 route: POST /students
      - ex. id=12인 students를 삭제하는 route: DELETE /students/12

### REST API 설계 규칙

1. 슬래시 구분자(/)는 계층 관계를 나타내는데 사용한다.
   - ex. http://restapi.example.com/houses/apartments
2. URI 마지막 문자로 슬래시를 포함하지 않는다.
   - ex. http://restapi.example.com/houses/apartments/ (X)
3. 하이픈(-)은 URI 가독성을 높이는 데 사용한다.
   - 불가피하게 긴 URI 경로를 사용하게 된다면 하이픈을 사용해 가독성을 높인다.
4. 밑줄(\_)은 URI에 사용하지 않는다.
5. URI 경로에는 소문자가 적합하다.
6. 파일 확장자를 URI에 포함하지 않는다.
   - REST API에서는 메세지 바디 내용의 포맷을 나타내기 위한 파일 확장자를 URI 안에 포함시키지 않는다.
   - Accecpt Header를 사용한다.
   - Ex. http://restapi.example.com/members/soccer/345/photo.jpg (X)
   - Ex. GET /members/soccer/345/photo HTTP/1.1 Host: restapi.example.com Accept: image/jpg (O)\
7. 리소스 간에 연관 관계가 있는 경우
   - /리소스명/리소스 ID/관계가 있는 다른 리솟 ㅡ명
   - ex. GET: /users/{userid}/devices (일반적으로 소유 'has'의 관계를 표현할 때)
