# ๐ Wanted X Wecode PreOnBoarding Backend Course | ์นด๋ฅ

์ํฐ๋ 4์ฃผ์ฐจ ๊ธฐ์ ๊ณผ์  : Cardoc Corporation Assignment Project
โ ์นด๋ฅ ๊ธฐ์ ๊ณผ์ ์๋๋ค.

- [์นด๋ฅ ์ฌ์ดํธ](https://www.cardoc.co.kr/)
- [์นด๋ฅ ์ฑ์ฉ๊ณต๊ณ  ๋งํฌ](https://www.wanted.co.kr/wd/57545?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic)

<br>

# ๐ ๋ชฉ์ฐจ    
- Assignment Requirements 
- Development Enviornment
- Database Schema 
- Directory Tree 
- API Specifications
- How to install and Run Server

<br>

# ๐ Assignment Requirements 


> ๐ ์นด๋ฅ์์ ์ค์ ๋ก ์ฌ์ฉํ๋ ํ๋ ์์ํฌ๋ฅผ ํ ๋๋ก ํ์ด์ด API๋ฅผ ์ค๊ณ ๋ฐ ๊ตฌํํฉ๋๋ค.

<br>

- ๋ฐ์ดํฐ๋ฒ ์ด์ค ํ๊ฒฝ์ ๋ณ๋๋ก ์ ๊ณตํ์ง ์์ต๋๋ค.
 **RDB์ค ์ํ๋ ๋ฐฉ์์ ์ ํ**ํ๋ฉด ๋๋ฉฐ, sqlite3 ๊ฐ์ ๋ณ๋์ ์ค์น์์ด ์ด์ฉ ๊ฐ๋ฅํ in-memory DB๋ ์ข์ผ๋ฉฐ, ๊ฐ๋ฅํ๋ค๋ฉด Docker๋ก ์ค๋นํ์๋ ๋ฉ๋๋ค.  
 
- ๋จ, ๊ฒฐ๊ณผ ์ ์ถ ์ README.md ํ์ผ์ ์คํ ๋ฐฉ๋ฒ์ ์๋ฒฝํ ์์ ํ์ฌ DB๋ฅผ ํฌํจํ์ฌ ์ ์ฒด์ ์ธ ์๋ฒ๋ฅผ ๊ตฌ๋ํ๋๋ฐ ๋ฌธ์ ์๋๋ก ํด์ผํฉ๋๋ค.

- ๋ฐ์ดํฐ๋ฒ ์ด์ค ๊ด๋ จ์ฒ๋ฆฌ๋ raw query๊ฐ ์๋ **ORM์ ์ด์ฉํ์ฌ ๊ตฌํ**ํฉ๋๋ค.

- Response Codes API๋ฅผ ์ฑ๊ณต์ ์ผ๋ก ํธ์ถํ  ๊ฒฝ์ฐ 200๋ฒ ์ฝ๋๋ฅผ ๋ฐํํ๊ณ , ๊ทธ ์ธ์ ๊ฒฝ์ฐ์๋ ์๋์ ์ฝ๋๋ก ๋ฐํํฉ๋๋ค.

<br>

### **[ํ์ ํฌํจ ์ฌํญ]**

- README ์์ฑ
    - ํ๋ก์ ํธ ๋น๋, ์์ธํ ์คํ ๋ฐฉ๋ฒ ๋ช์
    - ๊ตฌํ ๋ฐฉ๋ฒ๊ณผ ์ด์ ์ ๋ํ ๊ฐ๋ตํ ์ค๋ช
    - ์๋ฃ๋ ์์คํ์ด ๋ฐฐํฌ๋ ์๋ฒ์ ์ฃผ์
    - Swagger๋ Postman์ ํตํ API ํ์คํธํ ๋ ํ์ํ ์์ธ ๋ฐฉ๋ฒ
    - ํด๋น ๊ณผ์ ๋ฅผ ์งํํ๋ฉด์ ํ๊ณ  ๋ด์ฉ ๋ธ๋ก๊ทธ ํฌ์คํ
- Swagger๋ Postman์ ์ด์ฉํ์ฌ API ํ์คํธ ๊ฐ๋ฅํ๋๋ก ๊ตฌํ

<br>

### **[๊ธฐ๋ฅ ๊ฐ๋ฐ]**
- ์ฌ์ฉ์ ์์ฑ API(ํ์๊ฐ์/๋ก๊ทธ์ธ)    
  - ID/Password๋ก ์ฌ์ฉ์๋ฅผ ์์ฑํ๋ API.    
  - ์ธ์ฆ ํ ํฐ์ ๋ฐ๊ธํ๊ณ  ์ดํ์ API๋ ์ธ์ฆ๋ ์ฌ์ฉ์๋ง ํธ์ถํ  ์ ์๋ค.
- ์ฌ์ฉ์๊ฐ ์์ ํ ํ์ด์ด ์ ๋ณด๋ฅผ ์ ์ฅํ๋ API   
  - ์๋์ฐจ ์ฐจ์ข ID(trimID)๋ฅผ ์ด์ฉํ์ฌ ์ฌ์ฉ์๊ฐ ์์ ํ ์๋์ฐจ ์ ๋ณด๋ฅผ ์ ์ฅํ๋ค.    
  - ํ ๋ฒ์ ์ต๋ 5๋ช๊น์ง์ ์ฌ์ฉ์์ ๋ํ ์์ฒญ์ ๋ฐ์ ์ ์๋๋ก ํด์ผํ๋ค.
- ์ฌ์ฉ์๊ฐ ์์ ํ ํ์ด์ด ์ ๋ณด ์กฐํ API     
  - ์ฌ์ฉ์ ID๋ฅผ ํตํด์ 2๋ฒ API์์ ์ ์ฅํ ํ์ด์ด ์ ๋ณด๋ฅผ ์กฐํํ  ์ ์์ด์ผ ํ๋ค.

<br>

# โ๏ธ Development Enviornment

- Back-End: `Python 3.9.7`, `Django 3.2.9`, `MySQL`
- Deploy: `AWS EC2`, `AWS RDS`
- ETC: `Git`, `Github`, `Postman API Documentation`

<br>

### โก๏ธ Server Deploy (AWS EC2)

API Base URI : http://13.124.75.95:8000

<br>
<br>


# ๐ Database Schema
![แแณแแณแแตแซแแฃแบ 2021-11-29 แแฉแแฅแซ 1 30 21](https://user-images.githubusercontent.com/65930935/143778013-a7202d33-481d-4b8a-84dd-b3433f8ed301.png)

<br>
<br>

# ๐ฒ Directory Tree 

cf. ๊ธฐํ python cache ํ์ผ๊ณผ migration ํ์ผ์ ์ ์ธํ๊ณ  ํ์ํ์์ต๋๋ค.

```
โโโ README.md
โโโ cardoc.vuerd.json
โโโ cars
โย ย  โโโ admin.py
โย ย  โโโ apps.py
โย ย  โโโ cardoc.py
โย ย  โโโ models.py
โย ย  โโโ tests.py
โย ย  โโโ urls.py
โย ย  โโโ views.py
โโโ config
โย ย  โโโ asgi.py
โย ย  โโโ settings.py
โย ย  โโโ urls.py
โย ย  โโโ wsgi.py
โโโ core
โย ย  โโโ admin.py
โย ย  โโโ apps.py
โย ย  โโโ models.py
โย ย  โโโ tests.py
โย ย  โโโ utils.py
โย ย  โโโ validation.py
โย ย  โโโ views.py
โโโ manage.py
โโโ my_settings.py
โโโ requirements.txt
โโโ users
    โโโ admin.py
    โโโ apps.py
    โโโ models.py
    โโโ tests.py
    โโโ urls.py
    โโโ views.py
```

<br>
<br>

# ๐ API Specifications

[Postman API Document ๋ณด๋ฌ๊ฐ๊ธฐ](https://documenter.getpostman.com/view/14348138/UVJbJyG7)

<br>

## User Auth
์ฌ์ฉ์ ์ธ์ฆ, ์ธ๊ฐ์ ํ์ํ ์ ๋ณด๋ค์ ์ ๊ณตํ๋ APIs ์๋๋ค.

<br>

### ๐๐ป `POST` Sign-up
- ํ์๊ฐ์์ ํ์ํ `id`์ `password`๋ฅผ `request body`์ ํฌํจ์์ผ์ API๋ฅผ ํธ์ถํฉ๋๋ค.
- ๋น๋ฐ๋ฒํธ๋ ์ซ์์ ๋ฌธ์, ํน์๊ธฐํธ๋ฅผ ํฌํจํ ์ต์ 8๊ธ์ ์ด์์ ์กฐํฉ์ผ๋ก ๋์ด ์๋์ง ํ์์ ๊ฒ์ฌํฉ๋๋ค.
- `bcrypt` ๋ชจ๋์ ํตํด์ ๋น๋ฐ๋ฒํธ๋ ์ํธํ๋ฅผ ํ์ฌ ์ ์ฅํฉ๋๋ค.
- ์ด๋ฏธ `User` ํ์ด๋ธ์ ์กด์ฌํ๋ `id`๋ฅผ ๊ฐ์ผ๋ก ์์ฒญ์ ๋ณด๋์ ์์๋ 400 ์๋ฌ๋ฅผ ๋ฐํํฉ๋๋ค.

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

### ๐๐ป `POST` Sign-in
- `Request body`์ ํฌํจ๋ `id` ์ `password` ๋ฅผ ํตํด์ User Table์ ์ผ์นํ ์ ๋ณด๊ฐ ์๋์ง ํ์ธํฉ๋๋ค.
- ์ผ์นํ๋ ์ ๋ณด๋ฅผ ์ฐพ์๋ค๋ฉด, `user id` ์ ๋ณด๋ฅผ `payload`์ ๋ด์ `jwt`์ ๋ฐํํฉ๋๋ค.

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
์ฌ์ฉ์์ ์ฐจ๋ ์ ๋ณด๋ฅผ ๋ฑ๋กํ๊ณ  ์กฐํํ๋ APIs ์๋๋ค

<br>

### ๐๐ป `POST` Car owned by user
- ์ฌ์ฉ์๊ฐ ์์ ํ ์ฐจ๋ ์ ๋ณด๋ฅผ ์ ์ฅํฉ๋๋ค.
- `Request body` ์ ์ฌ์ฉ์์ `id`์ cardoc ์ฐจ๋ ์ ๋ณด ์กฐํ์ ํ์ํ `trimId`์ ํฌํจ์์ผ ํธ์ถํฉ๋๋ค.
- ์ต๋ 5๋ช์ ์ ์ ์ ์ฐจ๋ ์ ๋ณด ์ ์ฅ์ ํ ๋ฒ์ API ํธ์ถ๋ก ์งํํ  ์ ์์ต๋๋ค.
- cardoc API๋ฅผ ํตํด ํธ์ถํ ์ฐจ๋ ์ ๋ณด ์ค ํ์ด์ด ์ ๋ณด๋ฅผ ์ ์ฅํฉ๋๋ค.
- `{ํญ}/{ํธํ๋น}R{ํ  ์ฌ์ด์ฆ}` ํ์์ ํ์ด์ด ์ ๋ณด์ ๋ํ ์ ํจ์ฑ ๊ฒ์ฌ๋ฅผ ์งํํ์ฌ ๋ฐ์ดํฐ๋ฅผ ์ ์ฅํฉ๋๋ค.

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
            "message": "Already Registered ์คํผ๋ฌ์ค GH270 ๊ณ ๊ธํ"
        },
        {
            "User": "id_example2",
            "message": "Register ์ํ๋ผ SS"
        },
        {
            "User": "id_example2",
            "message": "Register 5์๋ฆฌ์ฆ GT x๋๋ผ์ด๋ธ ์ต์คํด๋ฃจ์๋ธ"
        }
    ]
}
```

<br>

### ๐๐ป `GET` Car list owned by user
- ์ฌ์ฉ์๊ฐ ๋ณด์ ํ ์ฐจ๋์ ๋ชจ๋ธ ๋ช์นญ๊ณผ ํ์ด์ด ์ ๋ณด์ ๋ชฉ๋ก์ ๋ถ๋ฌ์ต๋๋ค.
- ์ฌ์ฉ์ ์ธ์ฆ์ ์ํด `Authorization Header`์ `Bearer` ํ์์ `jwt`์ ์ ๋ฌํฉ๋๋ค.
- `Query Parameter`๋ฅผ ํตํด์ `Pagination`์ ๋ํ ์์ฒญ์ `offset`๊ณผ `limit`์ผ๋ก ๋ณด๋ผ ์ ์์ต๋๋ค.

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
      "model_name": "์คํผ๋ฌ์ค GH270 ๊ณ ๊ธํ",
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
      "model_name": "์ํ๋ผ SS",
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
      "model_name": "5์๋ฆฌ์ฆ GT x๋๋ผ์ด๋ธ ์ต์คํด๋ฃจ์๋ธ",
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

# ๐ How to install and Run Server

### ๋ก์ปฌ ๋ฐ ํ์คํธ์ฉ

1. Github Repository๋ฅผ Cloneํ๋ค.

```
git clone https://github.com/wanted-InfinityLoop/cardoc-InfinityLoop-ted.git
```

2. ๊ฐ์ํ๊ฒฝ์ผ๋ก [miniconda](https://docs.conda.io/en/latest/miniconda.html)๋ฅผ ์ค์นํ๋ค.

```
conda create -n deer python=3.9
conda actvate deer
```

3. ๊ฐ์ํ๊ฒฝ ์์ฑ ํ, requirements.txt๋ฅผ ์ค์นํ๋ค.

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

4. ํ๋ก์ ํธ๋ฅผ ์ํ MySQL Database๋ฅผ ์์ฑํ๋ค.
```
mysql -u root -p          # mysqlclient ์ ์

CREATE DATABASE cardoc CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

5. ๋ฐ์ดํฐ๋ฒ ์ด์ค๋ฅผ ์ฐ๊ฒฐํ์ฌ, migrate ํ ๋ก์ปฌ ์๋ฒ ๊ฐ๋

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



