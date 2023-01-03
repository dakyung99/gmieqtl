# GMI eqtl 데이터 조회 웹사이트

## 🔗 Deployment URL

https://gmieqtl.snu.ac.kr

<br />

## 📌 Summary

**GMI eqtl 데이터 조회 웹사이트**입니다.


#### * 주요 기능
- [x] 간략한 프로젝트 설명
- [x] 실험 데이터 조회 (검색 및 정렬)
- [x] 실험 데이터 CSV 다운로드

<br />

## 🤔 Background

단순히 데이터베이스의 데이터를 불러와서 검색, 정렬 기능과 함께 조회하는 것이 주요 기능이었기 때문에 React와 Django를 이용해서 프론트 엔드와 백 엔드를 각각 개발하는 것은 매우 비효율적이라 생각했습니다. 그래서 빠른 속도로 결과물을 만들어내는 Django 풀 스택을 선택하였습니다.

다만 배포 방식에서 고민이 있었는데, 백 엔드가 없는 간단한 정적 웹사이트를 배포하기 위한 무료 호스팅 서비스는 익히 알고 있었지만, Django 풀 스택 웹사이트를 배포하기 위한 무료 호스팅 서비스로는 무엇이 있는지 알지 못했습니다. 그러다가 검색을 통해 Heroku라는 것을 알게 됐고, 이번 기회에 Heroku라는 호스팅 서비스에 대해 익혀보자는 목표를 가지게 되었습니다.

<br />

## 🔍 Meaning

Django 풀 스택을 무료로 배포할 수 있도록 하는 Heroku라는 무료 호스팅 서비스에 대해 알게 되었고, 그것의 사용 방법을 익혔다는 것에 의미를 둘 수 있을 것 같습니다.

<br />

## 🔨 Technology Stack(s)

- Frontend : Django Template Engine, Vanilla JS
- Backend : Django
- Database : PostgreSQL (SQLite3 in Local)
- Deployment : Heroku

#### * 로컬 SQLite3 서버의 데이터를 원격 PostgreSQL 서버에 넣는 법

    1. EXCEL 파일을 CSV 파일로 변환하고, 프로젝트 폴더에 data.csv라는 이름으로 위치시킨다.
    
    2. read-csv.py 스크립트를 실행하여 로컬 SQLite3 서버에 CSV 파일의 데이터를 넣는다.
    
    3. python manage.py dumpdata > dump.json 명령어를 실행하여 JSON 덤프를 뜬다.
       
    4. dump.json 파일의 인코딩을 UTF8로 변경한다. (메모장 등 이용)
    
    5. Git 커밋 후 Heroku 전용 원격 리포지토리에 푸시한다. (git push heroku master)
    
    6. Heroku 콘솔에 접속하여 데이터베이스를 리셋하고, 마이그레이션을 수행한다.
    
    7. python manage.py loaddata dump.json 명령어를 실행하여 JSON 덤프를 씌운다.
