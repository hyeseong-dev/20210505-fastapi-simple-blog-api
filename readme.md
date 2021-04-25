# Simple APIs using FastAPI Webfamework 🚄

- 진행기간 : 2021년 04월 23일 ~ 2021년 4월 26일
- 리팩토링 : 2021년 03월 17일 ~ 2021년 3월 18일
<img width="933" alt="Screen Shot 2020-12-24 at 5 49 39 PM" src="https://media.vlpt.us/images/hyeseong-dev/post/6291b043-39ed-4036-b603-ab9865b4f34f/image.png">

## **🏠프로젝트 소개**

> 안녕하세요. 이번 토이프로젝트는 FastAPI 웹프레임워크에 대한 학습을 주 목적으로 해보았습니다.
<특징>
1. Starlette 프레임워크를 기반으로 비동기 API 서버를 지원
2. Pydantic 라이브러리와의 호환으로 데이터 검증 지원
3. OpenAPI 지원을 통해 자동 스웨거 생성 가능
4. 성능적인 측면에서는 Node와 Go에 필적할만한 수준

<장점>
1. swagger
 - flask로 flasgger라는 Flask extension 라이브러리를 이용해 작성해야한다. 
 flasgger는 docstring, *.yml또는 python 딕셔너리 형태를 지원하며 다양한 방법으로 작성할 수 있는 문서 이지만. API 유지보수 시 swagger 정의 파일을 따로 업데이트 해줘야 하는 수고가 필요하다.
 - FastAPI는 별도의 스웨거 파일 정의 없이 자동으로 생성하여 준다. 요청과 응답 부분에 pydantic 모델을 사용하며 배포시 자동으로 json 형태 변환되어 스웨거의 요청과 응답 모델에 자동으로 매핑 된다. 이는 의사소통 비용 절감을 가져다 주었고 개발자가 문서를 따로 신경쓰지 않아도 되기에 굉장한 생산성을 가져다 준다.

2. 비동기
 - Gevent Flask는 기본적으로 비동기 지원이 안되므로 Gevent(코루틴을 기반으로 동시성을 가능하게 해주는 라이브러리)의 monkey patching를 통해 I/O bound 작업을 비동기로 실행하였다. 하지만 테스트중 문제가 발생한다. 구글 라이브러리는 grpc를 사용한다. monkey patching은 비동기적으로 작동하기 위해 내부에서 소켓에 대한 부분을 코루틴 형식으로 바꾼다. 이 부분의 영향으로 다른 라이브러리가 사용하는 소켓까지 오버라이드 해버려서 제대로 동작하지 않게 한다. 물론, 해당 이슈는 해결되 었지만 여전히 논란의 여지가 있다점을 보면 잠재적으로 비동기 지원의 한계와 우려가 있음을 시사한다.
- FastAPI는 python 3.4부터 추가된 asyncio를 이용하여 비동기 프로그래밍이 가능하다. I/O 작업을 많은 코드 수정없이 쉽게 비동기로 처리할 수 있으며 속도 또한 uvicorn에 uvloop를 사용시 gevent 보다 월등히 빠르다.

3. python 3.6부터 제공된 type hint, DI를 통한 재사용성과 확장성등
---

## ⭐️ **구현 기능**

1. Path Parameters
2. API 문서 - swagger/redocs
3. Query Parameters
4. Request Body
5. Pydantic Schemas
6. Sqlalchemy DB 설정
7. Modeling
8. Blog data를 DB에 저장
9. Blog data를 DB로부터 요청
10. 삭제, 수정
11. 예외처리
12. User API CRUD
13. Relationship User to BLog & Blog to User
14. API Router 기본 사용, parametser를 이용한 Router 사용
15. 로그인 기능 
16. 비밀번호 인증
17. JWT access token 생성 및 반환
18. Routes behind authentication
19. Deta를 이용한 fastest Deployment


# **레퍼런스**
1. https://fastapi.tiangolo.com/
2. https://tech.madup.com/FastAPI/
3. https://www.youtube.com/watch?v=7t2alSnE2-I&t=13701s