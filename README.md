# 🎊 Wanted X Wecode PreOnBoarding Backend Course | 카닥

원티드 4주차 기업 과제 : Cardoc Corporation Assignment Project
✅ 카닥 기업 과제입니다.

- [카닥 사이트](https://www.cardoc.co.kr/)
- [카닥 채용공고 링크](https://www.wanted.co.kr/wd/57545?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic)

<br>

# 🔖 목차    
- Assignment Requirements 
- Development Enviornment
- Database Schema 
- Directory Tree 
- API Specifications
- How to install and Run Server

<br>

# 📖 Assignment Requirements 


> 😁 카닥에서 실제로 사용하는 프레임워크를 토대로 타이어 API를 설계 및 구현합니다.

<br>

- 데이터베이스 환경은 별도로 제공하지 않습니다.
 **RDB중 원하는 방식을 선택**하면 되며, sqlite3 같은 별도의 설치없이 이용 가능한 in-memory DB도 좋으며, 가능하다면 Docker로 준비하셔도 됩니다.  
 
- 단, 결과 제출 시 README.md 파일에 실행 방법을 완벽히 서술하여 DB를 포함하여 전체적인 서버를 구동하는데 문제없도록 해야합니다.

- 데이터베이스 관련처리는 raw query가 아닌 **ORM을 이용하여 구현**합니다.

- Response Codes API를 성공적으로 호출할 경우 200번 코드를 반환하고, 그 외의 경우에는 아래의 코드로 반환합니다.

<br>

### **[필수 포함 사항]**

- README 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

<br>

### **[기능 개발]**
- 사용자 생성 API(회원가입/로그인)    
  - ID/Password로 사용자를 생성하는 API.    
  - 인증 토큰을 발급하고 이후의 API는 인증된 사용자만 호출할 수 있다.
- 사용자가 소유한 타이어 정보를 저장하는 API   
  - 자동차 차종 ID(trimID)를 이용하여 사용자가 소유한 자동차 정보를 저장한다.    
  - 한 번에 최대 5명까지의 사용자에 대한 요청을 받을 수 있도록 해야한다.
- 사용자가 소유한 타이어 정보 조회 API     
  - 사용자 ID를 통해서 2번 API에서 저장한 타이어 정보를 조회할 수 있어야 한다.

<br>

# ⚒️ Development Enviornment

- Back-End: `Python 3.9.7`, `Django 3.2.9`, `MySQL`
- Deploy: `AWS EC2`, `AWS RDS`
- ETC: `Git`, `Github`, `Postman API Documentation`

<br>

### ➡️ Server Deploy (AWS EC2)

API Base URI : http://13.124.75.95:8000

<br>
<br>


# 📋 Database Schema
![스크린샷 2021-11-29 오전 1 30 21](https://user-images.githubusercontent.com/65930935/143778013-a7202d33-481d-4b8a-84dd-b3433f8ed301.png)

<br>
<br>

# 🌲 Directory Tree 

cf. 기타 python cache 파일과 migration 파일은 제외하고 표시하였습니다.

```
├── README.md
├── cardoc.vuerd.json
├── cars
│   ├── admin.py
│   ├── apps.py
│   ├── cardoc.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── utils.py
│   ├── validation.py
│   └── views.py
├── manage.py
├── my_settings.py
├── requirements.txt
└── users
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

<br>
<br>

# 🔖 API Specifications

[Postman API Document 보러가기](https://documenter.getpostman.com/view/14348138/UVJbJyG7)

<br>

## User Auth
사용자 인증, 인가에 필요한 정보들을 제공하는 APIs 입니다.

<br>

### 👉🏻 `POST` Sign-up
- 회원가입에 필요한 `id`와 `password`를 `request body`에 포함시켜서 API를 호출합니다.
- 비밀번호는 숫자와 문자, 특수기호를 포함한 최소 8글자 이상의 조합으로 되어 있는지 형식을 검사합니다.
- `bcrypt` 모듈을 통해서 비밀번호는 암호화를 하여 저장합니다.
- 이미 `User` 테이블에 존재하는 `id`를 값으로 요청을 보냈을 시에는 400 에러를 반환합니다.

### Example
**Request**
```
curl --location --request POST 'http://13.124.75.95:8000/users/signup' \
--data-raw '{
    "id": "id_example",
    "password": "password_example"
}'
```

**Response**
```
{
    "message": "User id_example has created!"
}
```

<br>

### 👉🏻 `POST` Sign-in
- `Request body`에 포함된 `id` 와 `password` 를 통해서 User Table에 일치한 정보가 있는지 확인합니다.
- 일치하는 정보를 찾았다면, `user id` 정보를 `payload`에 담은 `jwt`을 반환합니다.

### Example
**Request**
```
curl --location --request POST 'http://13.124.75.95:8000/users/signin' \
--data-raw '{
    "id": "id_example",
    "password": "password_example"
}'
```

**Response**
```
{
    "message": "User id_example has signed in!",
    "token": "jwt_token_example"
}
```

<br>

## Car Request
사용자의 차량 정보를 등록하고 조회하는 APIs 입니다

<br>

### 👉🏻 `POST` Car owned by user
- 사용자가 소유한 차량 정보를 저장합니다.
- `Request body` 에 사용자의 `id`와 cardoc 차량 정보 조회에 필요한 `trimId`을 포함시켜 호출합니다.
- 최대 5명의 유저의 차량 정보 저장을 한 번의 API 호출로 진행할 수 있습니다.
- cardoc API를 통해 호출한 차량 정보 중 타이어 정보를 저장합니다.
- `{폭}/{편평비}R{휠 사이즈}` 형식의 타이어 정보에 대한 유효성 검사를 진행하여 데이터를 저장합니다.

### Example
**Request**
```
curl --location --request POST 'http://13.124.75.95:8000/cars' \
--data-raw '[
    {
        "id": "id_example",
        "trimId": "*"
    },
    {
        "id": "id_example",
        "trimId": 5000
    },
    {
        "id": "id_example2",
        "trimId": 11000
    },
    {
        "id": "id_example2",
        "trimId": 15000
    }
]'
```

**Response**
```
{
    "results": [
        {
            "User": "id_example",
            "message": "INVALID_TRIM_VALUE"
        },
        {
            "User": "id_example",
            "message": "Already Registered 오피러스 GH270 고급형"
        },
        {
            "User": "id_example2",
            "message": "Register 임팔라 SS"
        },
        {
            "User": "id_example2",
            "message": "Register 5시리즈 GT x드라이브 익스클루시브"
        }
    ]
}
```

<br>

### 👉🏻 `GET` Car list owned by user
- 사용자가 보유한 차량의 모델 명칭과 타이어 정보의 목록을 불러옵니다.
- 사용자 인증을 위해 `Authorization Header`에 `Bearer` 형식의 `jwt`을 전달합니다.
- `Query Parameter`를 통해서 `Pagination`에 대한 요청을 `offset`과 `limit`으로 보낼 수 있습니다.

### Example
**Request**
```
curl --location --request GET 'http://13.124.75.95:8000/cars/users/tire?offset=0&limit=3'
```

**Response**
```
{
  "results": [
    {
      "model_name": "오피러스 GH270 고급형",
      "front_tire": {
        "width": 225,
        "aspect_ratio": 60,
        "wheel_size": 16
      },
      "rear_tire": {
        "width": 225,
        "aspect_ratio": 60,
        "wheel_size": 16
      }
    },
    {
      "model_name": "임팔라 SS",
      "front_tire": {
        "width": 235,
        "aspect_ratio": 50,
        "wheel_size": 18
      },
      "rear_tire": {
        "width": 235,
        "aspect_ratio": 50,
        "wheel_size": 18
      }
    },
    {
      "model_name": "5시리즈 GT x드라이브 익스클루시브",
      "front_tire": {
        "width": 245,
        "aspect_ratio": 45,
        "wheel_size": 19
      },
      "rear_tire": {
        "width": 275,
        "aspect_ratio": 40,
        "wheel_size": 19
      }
    }
  ]
}
```

<br>
<br>

# 🔖 How to install and Run Server

### 로컬 및 테스트용

1. Github Repository를 Clone한다.

```
git clone https://github.com/wanted-InfinityLoop/cardoc-InfinityLoop-ted.git
```

2. 가상환경으로 [miniconda](https://docs.conda.io/en/latest/miniconda.html)를 설치한다.

```
conda create -n deer python=3.9
conda actvate deer
```

3. 가상환경 생성 후, requirements.txt를 설치한다.

```
pip install -r requirements.txt

Django==3.2.9
django-cors-headers==3.10.0
PyMySQL==1.0.2
mysql-client==0.0.1
bcrypt==3.2.0
PyJWT==2.3.0
requests==2.26.0
cryptography==36.0.0

```

4. 프로젝트를 위한 MySQL Database를 생성한다.
```
mysql -u root -p          # mysqlclient 접속

CREATE DATABASE cardoc CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

5. 데이터베이스를 연결하여, migrate 후 로컬 서버 가동

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



