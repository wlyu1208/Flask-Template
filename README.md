# Flask-Template
 - Respository for Simple Flask Application Template

## Objective(개요)
 - Flask Application Template

## Development Environment (개발 환경)
- Language : `python 3.9`
- OS : `Linux`

## How to Use(사용 방법)

Assuming Dokcer is installed on the computer.

### `docker-compose`를 이용하여 실행

```shell
docker compose up
```

패키지 설치하기

```shell
cd api
pip install -r requirements.txt
```

스토리지 초기화하기

```shell
cd api
flask storage init
```

데이터베이스 초기화하기

```shell
cd api
flask db init
flask db migrate -m "Initial migration."
```

서비스 시작하기

```shell
cd api
flask run
```

### Flask app을 컨테이너로 빌드하여 테스트

```shell
docker-compose -f docker-compose-build.yml up --build
```