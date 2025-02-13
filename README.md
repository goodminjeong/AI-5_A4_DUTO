# Backend - <a href="https://github.com/goodminjeong/AI-5_A4_DUTO_Frontend">Frontend 바로가기!</a>
# Django-rest-framework-Project-Two Rabbits
DRF를 이용한 커뮤니티 사이트

## 🖥️ 프로젝트 소개 - <a href="https://www.notion.so/woongpang/S-A-5e8bad4c4aa648e7b6ff860e47a08718">S.A. 바로가기!</a>
개발 공부 자료도 얻고 휴식을 위한 미디어 컨텐츠(왓챠피디아 참조)를 추천받는 개발자 연습생을 위한 커뮤니티 사이트
<br>
이름하여 <두 마리 토끼>입니다!

## 🕰️ 개발 기간
* 23.05.08 - 23.05.14

### 🧑‍🤝‍🧑 팀원 구성 및 역할 분담
- 팀장😄  : <a href="https://mdhtora.tistory.com/">마동휘</a> - 회원가입, 프로필 조회, 수정
- 팀원😄1 : <a href="https://hanilcome.tistory.com/">윤보영</a> - 로그인, 팔로우 기능, 내가 쓴 글 조회, 좋아요 게시글 조회
- 팀원😄2 : <a href="https://guco.tistory.com/">구민정</a> - 메인페이지 게시글 리스트 조회, 팔로잉 게시글 리스트 조회, 카테고리별 게시글 리스트 조회, 별점 기능
- 팀원😄3 : <a href="http://allitail.tistory.com/">원윤희</a> - 게시글 등록, 조회, 수정, 삭제, 좋아요
- 팀원😄4 : <a href="https://woongpang.tistory.com/">이기웅</a> - 댓글 등록, 조회, 수정, 삭제

### ⚙️ 개발 환경
- `Python 3.11`
- **IDE** : `visual studio code`, `pycharm`
- **Framework** : `Django-Rest-Framework`
- **Workbench** : `MySQL Workbench 8.0 CE`
- **Database** : `Mysql DB(6.4.5)`
- 그외 : **requirements.txt** : `requirements.txt`
- **FRONT-END** : https://github.com/goodminjeong/AI-5_A4_DUTO_Frontend 실행화면은 frontend repository에 있음

### 🔑 프로젝트 설치 및 실행 방법
#### 깃허브 클론하기
```
$ git init
$ git clone git@github.com:goodminjeong/AI-5_A4_DUTO_Backend.git
```
#### 패키지 밎 라이브러리 설치
```
$ pip install -r requirements.txt
```
#### DB 연동
```
$ python manage.py makemigrations
$ python manage.py migrate
```
#### 카테고리 초기 데이터 설정
```
$ python manage.py loaddata category_data
```
#### 백엔드 서버 실행
```
$ python manage.py runserver
```
#### 프론트엔드 라이브서버 실행
- vscode 확장팩 <Live Server> 설치
- index.html에서 마우스 우클릭 후 Open with Live Server 클릭(단축키 Alt+L+O)

## 📌 주요 기능
#### 로그인 
- DB값 검증
- 로그인 시 JWT Token 생성

#### 회원가입 
- 주소 API 연동
- ID , Email 중복방지

#### 회원탈퇴
- 데이터베이스에서 완전소멸이 아닌 유저의 "is_active = False" 로 변환함

#### 프로필>상세보기
- 프로필 정보 수정
- 좋아요한 게시글 보기, 내가 쓴 게시글 보기
- 사용자 본인의 프로필만 수정 버튼이 보임

#### 메인 페이지 
- 전체 게시글 조회
- 최근 12개의 게시글이 최신순으로 정렬되어 있음
- 남긴 별점이 보임

#### 카테고리
- 공부, 휴식 두 카테고리로 글을 나눌 수 있음(카테고리별 게시글 조회)
- 카테고리별 팔로잉 게시글 조회
- 해당 카테고리에서 글쓰기 버튼을 누르면 자동으로 카테고리가 설정됨
- 자신이 팔로잉한 사람들이 쓴 게시글들을 모아볼 수 있음

#### 게시글 작성
- 별점 추가, 이미지 첨부
- 제목, 내용, 별점 필수, 이미지 선택 가능
- 게시글 수정 시 원래 내용 불러오는 기능
- 수정하지 않은 내용은 그대로 다시 DB에 저장됨
- 본인이 쓴 게시글만 수정, 삭제 가능

#### 상세 페이지
- 게시글 수정, 삭제
- 좋아요 기능
- 팔로우 기능
- 카테고리 별 페이지
- 타인이 작성한 게시글에는 수정, 삭제 버튼 안 보임

#### 댓글 작성
- 댓글 작성
- 작성자만 본인 댓글을 수정, 삭제 가능
- 작성자에게만 본인 댓글관련 수정, 삭제 버튼이 보여짐
- 댓글 수정 시 기존 내용을 한번 더 확인시켜줌
- 댓글 수정 시 변경된 값이 없을 경우 백엔드로 요청 하지않음

#### 팔로우 기능
- 상세페이지를 들어갔을때 작성자가 본인이면 팔로우 버튼 x, 다른 사람일 경우 팔로우 버튼이 생김

#### 내가 쓴 게시글
- 프로필 페이지에서 본인이 작성한 글만 보이게 하는 기능 

#### 좋아요 한 게시글 보기
- 프로필 페이지에서 본인이 좋아요한 글만 보이게 하는 기능
